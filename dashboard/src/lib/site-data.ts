import fs from "node:fs";
import path from "node:path";

import { parse as parseCsv } from "csv-parse/sync";

import {
  loadDashboardSummaryData,
  loadRunPayload,
  resolveResultsDir,
  sumCompleteOrNull,
} from "@/lib/dashboard-data";
import type {
  DashboardSummaryData,
  ModelSummary,
  QuantitySummary,
} from "@/lib/dashboard-types";
import { compareModelNames } from "@/lib/model-meta";

const MODEL_REGISTRY_FIELDS = [
  "model_id",
  "display_label",
  "organization",
  "serving_provider_path",
  "model_family",
  "wave",
  "organization_label",
  "wave_label",
  "is_frontier",
] as const;

export interface ModelRegistryRow {
  modelId: string;
  displayLabel: string;
  organization: string;
  servingProviderPath: string;
  modelFamily: string;
  wave: string;
  organizationLabel: string;
  waveLabel: string;
  isFrontier: boolean;
}

export interface QuantityRegistryRow {
  quantityId: string;
  name: string;
  domain: string;
  description: string;
  population: string;
  unit: string;
  preferredInterpretation: string;
  lowerSupport: string;
  upperSupport: string;
  benchmarkSummary: string;
  benchmarkSource: string;
}

/** Elicited quantity definitions emitted from llm_econ_beliefs/data/quantities.toml. */
export function loadQuantityRegistry(
  resultsDir: string = resolveResultsDir(),
): Map<string, QuantityRegistryRow> {
  const csvPath = path.join(resultsDir, "quantity-registry.csv");
  const rows = readRequiredCsv(csvPath, "quantity-registry.csv");
  const registry = new Map<string, QuantityRegistryRow>();
  for (const row of rows) {
    const quantityId = row.quantity_id?.trim();
    if (!quantityId || !row.description?.trim()) {
      throw new Error(
        `quantity-registry.csv row missing quantity_id/description: ${JSON.stringify(row)}`,
      );
    }
    registry.set(quantityId, {
      quantityId,
      name: row.name.trim(),
      domain: row.domain.trim(),
      description: row.description.trim(),
      population: row.population.trim(),
      unit: row.unit.trim(),
      preferredInterpretation: row.preferred_interpretation.trim(),
      lowerSupport: row.lower_support.trim(),
      upperSupport: row.upper_support.trim(),
      benchmarkSummary: row.benchmark_summary.trim(),
      benchmarkSource: row.benchmark_source.trim(),
    });
  }
  return registry;
}

function readRequiredCsv(csvPath: string, artifactName: string): Record<string, string>[] {
  if (!fs.existsSync(csvPath)) {
    throw new Error(`Missing required dashboard artifact: ${csvPath}`);
  }
  const rows = parseCsv(fs.readFileSync(csvPath, "utf-8"), {
    columns: true,
    skip_empty_lines: true,
  }) as Record<string, string>[];
  if (rows.length === 0) {
    throw new Error(`${artifactName} must contain at least one data row`);
  }
  return rows;
}

/** Canonical model metadata emitted from llm_econ_beliefs/model_registry.py. */
export function loadModelRegistry(
  resultsDir: string = resolveResultsDir(),
): Map<string, ModelRegistryRow> {
  const csvPath = path.join(resultsDir, "model-registry.csv");
  const rows = readRequiredCsv(csvPath, "model-registry.csv");
  const headers = new Set(Object.keys(rows[0]));
  const missingHeaders = MODEL_REGISTRY_FIELDS.filter((field) => !headers.has(field));
  const extraHeaders = [...headers].filter(
    (field) => !(MODEL_REGISTRY_FIELDS as readonly string[]).includes(field),
  );
  if (missingHeaders.length > 0 || extraHeaders.length > 0) {
    throw new Error(
      `model-registry.csv has invalid columns; missing=${missingHeaders.join(",") || "none"}, extra=${extraHeaders.join(",") || "none"}`,
    );
  }

  const registry = new Map<string, ModelRegistryRow>();
  for (const [index, row] of rows.entries()) {
    const blankFields = MODEL_REGISTRY_FIELDS.filter((field) => !row[field]?.trim());
    if (blankFields.length > 0) {
      throw new Error(
        `model-registry.csv row ${index + 2} has blank fields: ${blankFields.join(", ")}`,
      );
    }
    const modelId = row.model_id.trim();
    if (registry.has(modelId)) {
      throw new Error(`model-registry.csv has duplicate model_id: ${modelId}`);
    }
    registry.set(modelId, {
      modelId,
      displayLabel: row.display_label.trim(),
      organization: row.organization.trim(),
      servingProviderPath: row.serving_provider_path.trim(),
      modelFamily: row.model_family.trim(),
      wave: row.wave.trim(),
      organizationLabel: row.organization_label.trim(),
      waveLabel: row.wave_label.trim(),
      isFrontier: row.is_frontier.trim() === "true",
    });
  }
  return registry;
}

/** Models admitted by both artifacts from the complete-grid comparison build. */
export function loadGatedComparisonModelIds(
  resultsDir: string = resolveResultsDir(),
  registry: ReadonlyMap<string, ModelRegistryRow> = loadModelRegistry(resultsDir),
): Set<string> {
  const comparisonRows = readRequiredCsv(
    path.join(resultsDir, "elasticity-all-model-comparison.csv"),
    "elasticity-all-model-comparison.csv",
  );
  const rollupRows = readRequiredCsv(
    path.join(resultsDir, "elasticity-model-rollup.csv"),
    "elasticity-model-rollup.csv",
  );

  const modelSet = (rows: Record<string, string>[], artifactName: string) => {
    const ids = new Set<string>();
    for (const [index, row] of rows.entries()) {
      const modelId = row.model_name?.trim();
      if (!modelId) {
        throw new Error(`${artifactName} row ${index + 2} has a blank model_name`);
      }
      if (!registry.has(modelId)) {
        throw new Error(`${artifactName} contains unregistered model: ${modelId}`);
      }
      ids.add(modelId);
    }
    return ids;
  };

  const comparisonModels = modelSet(
    comparisonRows,
    "elasticity-all-model-comparison.csv",
  );
  const rollupModels = modelSet(rollupRows, "elasticity-model-rollup.csv");
  const comparisonOnly = [...comparisonModels].filter((id) => !rollupModels.has(id));
  const rollupOnly = [...rollupModels].filter((id) => !comparisonModels.has(id));
  if (comparisonOnly.length > 0 || rollupOnly.length > 0) {
    throw new Error(
      `Gated comparison artifacts disagree; comparison_only=${comparisonOnly.sort().join(",") || "none"}, rollup_only=${rollupOnly.sort().join(",") || "none"}`,
    );
  }
  return comparisonModels;
}

let cachedInputs:
  | {
      resultsDir: string;
      registry: Map<string, ModelRegistryRow>;
      gatedModelIds: Set<string>;
    }
  | undefined;

function getSiteInputs() {
  const resultsDir = resolveResultsDir();
  if (!cachedInputs || cachedInputs.resultsDir !== resultsDir) {
    const registry = loadModelRegistry(resultsDir);
    cachedInputs = {
      resultsDir,
      registry,
      gatedModelIds: loadGatedComparisonModelIds(resultsDir, registry),
    };
  }
  return cachedInputs;
}

/* ------------------------------------------------------------------ */
/* Panel structure                                                     */
/* ------------------------------------------------------------------ */

export const LABOR_TAX_QUANTITY_IDS = [
  "labor_supply.extensive_margin.single_mothers",
  "labor_supply.frisch_elasticity.prime_age",
  "labor_supply.income_elasticity.prime_age",
  "labor_supply.marshallian_wage_elasticity.prime_age",
  "tax.capital_gains_realizations.elasticity",
  "tax.elasticity_of_taxable_income.top_earners",
] as const;

export const MACRO_TRADE_QUANTITY_IDS = [
  "household.intertemporal_elasticity_of_substitution",
  "production.capital_labor_substitution",
  "trade.armington_elasticity.import_domestic",
] as const;

export const CALIBRATION_QUANTITY_IDS = [
  "household.annual_discount_factor",
  "household.relative_risk_aversion.crra",
  "macro.tfp_persistence.ar1",
  "production.capital_share",
] as const;

export const CANONICAL_QUANTITY_IDS: readonly string[] = [
  ...LABOR_TAX_QUANTITY_IDS,
  ...MACRO_TRADE_QUANTITY_IDS,
  ...CALIBRATION_QUANTITY_IDS,
];

export const HEADLINE_QUANTITY_IDS: readonly string[] = [
  ...LABOR_TAX_QUANTITY_IDS,
  ...MACRO_TRADE_QUANTITY_IDS,
];

export type Subpanel = "labor-tax" | "macro-trade" | "calibration" | "simulation";

export function subpanelForQuantity(quantityId: string): Subpanel {
  if ((LABOR_TAX_QUANTITY_IDS as readonly string[]).includes(quantityId)) {
    return "labor-tax";
  }
  if ((MACRO_TRADE_QUANTITY_IDS as readonly string[]).includes(quantityId)) {
    return "macro-trade";
  }
  if ((CALIBRATION_QUANTITY_IDS as readonly string[]).includes(quantityId)) {
    return "calibration";
  }
  return "simulation";
}

export const SUBPANEL_LABELS: Record<Subpanel, string> = {
  "labor-tax": "Labor and tax",
  "macro-trade": "Macro and trade",
  calibration: "Calibration parameters",
  simulation: "Simulation-facing coefficients",
};

/* ------------------------------------------------------------------ */
/* Slugs                                                               */
/* ------------------------------------------------------------------ */

export function slugForQuantity(quantityId: string): string {
  return quantityId.replace(/[._]/g, "-");
}

export function slugForModel(modelName: string): string {
  return modelName.replace(/\./g, "-");
}

/* ------------------------------------------------------------------ */
/* Benchmarks (staged from paper/tables at deploy time)                */
/* ------------------------------------------------------------------ */

export interface BenchmarkBand {
  lower: number;
  upper: number;
  sources: string;
}

function resolveTablesDir(): string | null {
  const localPath = path.resolve(process.cwd(), "..", "paper", "tables");
  if (fs.existsSync(localPath)) return localPath;
  const bundledPath = path.resolve(process.cwd(), "tables");
  if (fs.existsSync(bundledPath)) return bundledPath;
  return null;
}

/** Review bands keyed by quantity display name, from the paper's Table 3 CSV. */
export function loadBenchmarkBands(): Map<string, BenchmarkBand> {
  const bands = new Map<string, BenchmarkBand>();
  const tablesDir = resolveTablesDir();
  if (!tablesDir) return bands;
  const csvPath = path.join(tablesDir, "benchmark-comparison-labor-tax.csv");
  if (!fs.existsSync(csvPath)) return bands;

  const rows = parseCsv(fs.readFileSync(csvPath, "utf-8"), {
    columns: true,
  }) as Record<string, string>[];
  for (const row of rows) {
    const match = /\[\s*(-?[\d.]+)\s*,\s*(-?[\d.]+)\s*\]/.exec(
      row["Rough review range"] ?? "",
    );
    if (!match) continue;
    bands.set(row["Quantity"], {
      lower: Number(match[1]),
      upper: Number(match[2]),
      sources: row["Benchmark sources"] ?? "",
    });
  }
  return bands;
}

export interface HarnessRow {
  model: string;
  providerPath: string;
  mechanism: string;
  budget: string;
  sampling: string;
  reasoning: string;
  identifier: string;
  identifierType: string;
}

/** Per-model harness configuration, from the paper's Table A16 CSV. */
export interface OverviewRankRow {
  model: string;
  organization: string;
  absRank: number;
  widthRank: number;
}

/** Per-model average ranks from the subpanel overview tables. */
export function loadModelOverview(
  subpanel: "labor_tax" | "macro_trade",
): OverviewRankRow[] {
  const tablesDir = resolveTablesDir();
  if (!tablesDir) return [];
  const stem =
    subpanel === "labor_tax"
      ? "model-overview-labor-tax.csv"
      : "model-overview-macro-trade.csv";
  const csvPath = path.join(tablesDir, stem);
  if (!fs.existsSync(csvPath)) return [];
  const rows = parseCsv(fs.readFileSync(csvPath, "utf-8"), {
    columns: true,
  }) as Record<string, string>[];
  return rows.map((row) => ({
    model: row["Model"] ?? "",
    organization: row["Organization"] ?? "",
    absRank: Number(row["Avg abs-elasticity rank (1=highest)"]),
    widthRank: Number(row["Avg predictive-uncertainty rank (1=narrowest)"]),
  }));
}

export function loadHarnessRows(): HarnessRow[] {
  const tablesDir = resolveTablesDir();
  if (!tablesDir) return [];
  const csvPath = path.join(tablesDir, "harness-disclosure.csv");
  if (!fs.existsSync(csvPath)) return [];

  const rows = parseCsv(fs.readFileSync(csvPath, "utf-8"), {
    columns: true,
  }) as Record<string, string>[];
  return rows.map((row) => ({
    model: row["Model"] ?? "",
    providerPath: row["Provider path"] ?? "",
    mechanism: row["Output mechanism"] ?? "",
    budget: row["Completion budget"] ?? "",
    sampling: row["Sampling"] ?? "",
    reasoning: row["Reasoning config"] ?? "",
    identifier: row["API identifier"] ?? "",
    identifierType: row["Identifier type"] ?? "",
  }));
}

/* ------------------------------------------------------------------ */
/* Site-wide data                                                      */
/* ------------------------------------------------------------------ */

export interface SlimRun {
  runIndex: number;
  pointEstimate: number | null;
  p05: number | null;
  p25: number | null;
  p50: number | null;
  p75: number | null;
  p95: number | null;
  reasoningSummary: string | null;
}

let cachedSummaryData: DashboardSummaryData | null = null;

export function getSummaryData(): DashboardSummaryData {
  const { resultsDir, gatedModelIds } = getSiteInputs();
  cachedSummaryData ??= loadDashboardSummaryData(resultsDir, gatedModelIds);
  return cachedSummaryData;
}

export function getQuantityBySlug(slug: string): QuantitySummary | null {
  return (
    getSummaryData().quantities.find(
      (quantity) => slugForQuantity(quantity.quantityId) === slug,
    ) ?? null
  );
}

export function getModelNameBySlug(slug: string): string | null {
  return (
    getSummaryData().modelNames.find(
      (modelName) => slugForModel(modelName) === slug,
    ) ?? null
  );
}

export function loadSlimRuns(
  quantityId: string,
  modelName: string,
): SlimRun[] {
  const { resultsDir, gatedModelIds } = getSiteInputs();
  const payload = loadRunPayload(
    quantityId,
    modelName,
    resultsDir,
    gatedModelIds,
  );
  if (!payload) return [];
  return payload.runs
    .filter((run) => run.parsedOk)
    .map((run) => ({
      runIndex: run.runIndex,
      pointEstimate: run.pointEstimate,
      p05: run.quantiles["p05"] ?? null,
      p25: run.quantiles["p25"] ?? null,
      p50: run.quantiles["p50"] ?? null,
      p75: run.quantiles["p75"] ?? null,
      p95: run.quantiles["p95"] ?? null,
      reasoningSummary: run.reasoningSummary,
    }));
}

/** Ordered model summaries for one quantity, sorted by pooled center. */
export function modelsByCenter(quantity: QuantitySummary): ModelSummary[] {
  return [...quantity.modelSummaries].sort((left, right) => {
    const a = left.intervals.pooled.center ?? 0;
    const b = right.intervals.pooled.center ?? 0;
    return a - b;
  });
}

/** Panel median of pooled centers for a quantity. */
export function panelMedianCenter(quantity: QuantitySummary): number | null {
  const centers = quantity.modelSummaries
    .map((summary) => summary.intervals.pooled.center)
    .filter((value): value is number => value !== null)
    .sort((a, b) => a - b);
  if (centers.length === 0) return null;
  const mid = Math.floor(centers.length / 2);
  return centers.length % 2 === 1
    ? centers[mid]
    : (centers[mid - 1] + centers[mid]) / 2;
}

/** Exact tie-averaged ranks (1 is smallest unless `reverse` is true). */
export function tieAveragedRanks(
  values: ReadonlyMap<string, number>,
  reverse = false,
): Map<string, number> {
  const ordered = [...values.entries()].sort(([leftKey, left], [rightKey, right]) => {
    const valueOrder = reverse ? right - left : left - right;
    return valueOrder || leftKey.localeCompare(rightKey);
  });
  const ranks = new Map<string, number>();
  let index = 0;

  while (index < ordered.length) {
    let tieEnd = index;
    while (
      tieEnd + 1 < ordered.length &&
      ordered[tieEnd + 1][1] === ordered[index][1]
    ) {
      tieEnd += 1;
    }
    const averageRank = (index + 1 + tieEnd + 1) / 2;
    for (let tiedIndex = index; tiedIndex <= tieEnd; tiedIndex += 1) {
      ranks.set(ordered[tiedIndex][0], averageRank);
    }
    index = tieEnd + 1;
  }

  return ranks;
}

export interface ModelProfileRow {
  quantity: QuantitySummary;
  summary: ModelSummary;
  panelMedian: number | null;
  widthRank: number | null;
}

/** One row per canonical quantity for a model profile page. */
export function buildModelProfile(modelName: string): {
  rows: ModelProfileRow[];
  avgWidthRank: number | null;
  totalCostUsd: number | null;
  metadata: ModelRegistryRow;
  organizationLabel: string;
  waveLabel: string;
} {
  const metadata = getSiteInputs().registry.get(modelName);
  if (!metadata) {
    throw new Error(`Dashboard model is absent from model-registry.csv: ${modelName}`);
  }
  const data = getSummaryData();
  const rows: ModelProfileRow[] = [];
  const widthRanks: number[] = [];

  for (const quantityId of CANONICAL_QUANTITY_IDS) {
    const quantity = data.quantities.find((q) => q.quantityId === quantityId);
    if (!quantity) continue;
    const summary = quantity.modelSummaries.find(
      (s) => s.modelName === modelName,
    );
    if (!summary) continue;

    const widths = new Map(
      quantity.modelSummaries.flatMap((s) => {
        const { lower, upper } = s.intervals.pooled;
        return lower !== null && upper !== null
          ? [[s.modelName, upper - lower] as const]
          : [];
      }),
    );
    const widthRank = tieAveragedRanks(widths).get(modelName) ?? null;
    if (widthRank !== null) widthRanks.push(widthRank);

    rows.push({
      quantity,
      summary,
      panelMedian: panelMedianCenter(quantity),
      widthRank,
    });
  }

  const modelCosts = data.quantities.flatMap((quantity) => {
    const summary = quantity.modelSummaries.find((s) => s.modelName === modelName);
    return summary ? [summary.totalCostUsd] : [];
  });
  const totalCostUsd = sumCompleteOrNull(modelCosts);

  const avgWidthRank =
    widthRanks.length > 0
      ? widthRanks.reduce((sum, rank) => sum + rank, 0) / widthRanks.length
      : null;

  return {
    rows,
    avgWidthRank,
    totalCostUsd,
    metadata,
    organizationLabel: metadata.organizationLabel,
    waveLabel: metadata.waveLabel,
  };
}

/** Total successful runs across every result directory in the summary. */
export function totalRunCount(): number {
  return getSummaryData().quantities.reduce(
    (total, quantity) =>
      total +
      quantity.modelSummaries.reduce(
        (subtotal, summary) => subtotal + summary.nSuccessfulRuns,
        0,
      ),
    0,
  );
}

export function orderedModelNames(): string[] {
  return [...getSummaryData().modelNames].sort(compareModelNames);
}

/* ------------------------------------------------------------------ */
/* Implied top rates (paper Table 4, staged from paper/tables)         */
/* ------------------------------------------------------------------ */

export interface TopRateRow {
  modelId: string;
  displayLabel: string;
  isFrontier: boolean;
  etiMedian: number;
  etiLower: number;
  etiUpper: number;
  topRate: number;
  topRateLower: number;
  topRateUpper: number;
  revenueMax: number;
  widthPp: number;
}

const MEDIAN_INTERVAL = /(-?[\d.]+)%?\s*\[\s*(-?[\d.]+)%?\s*,\s*(-?[\d.]+)%?\s*\]/;

/** Paper Table 4: each model's elicited ETI mapped through one fixed
 *  Saez calibration. Rows come back sorted by implied top rate. */
export function loadTopRateRows(): TopRateRow[] {
  const tablesDir = resolveTablesDir();
  if (!tablesDir) return [];
  const csvPath = path.join(tablesDir, "toy-top-rate-labor-tax.csv");
  if (!fs.existsSync(csvPath)) return [];
  const registry = loadModelRegistry();
  const byLabel = new Map(
    [...registry.values()].map((row) => [row.displayLabel, row]),
  );
  const rows = parseCsv(fs.readFileSync(csvPath, "utf-8"), {
    columns: true,
  }) as Record<string, string>[];
  const parsed: TopRateRow[] = [];
  for (const row of rows) {
    const meta = byLabel.get(row["Model"]);
    const eti = MEDIAN_INTERVAL.exec(row["ETI median [90%]"] ?? "");
    const top = MEDIAN_INTERVAL.exec(row["Top rate median [90%]"] ?? "");
    if (!meta || !eti || !top) continue;
    parsed.push({
      modelId: meta.modelId,
      displayLabel: meta.displayLabel,
      isFrontier: meta.isFrontier,
      etiMedian: Number(eti[1]),
      etiLower: Number(eti[2]),
      etiUpper: Number(eti[3]),
      topRate: Number(top[1]),
      topRateLower: Number(top[2]),
      topRateUpper: Number(top[3]),
      revenueMax: Number((row["Revenue-max median"] ?? "").replace("%", "")),
      widthPp: Number(row["Top-rate 90% width (pp)"]),
    });
  }
  parsed.sort((a, b) => a.topRate - b.topRate);
  return parsed;
}

/* ------------------------------------------------------------------ */
/* Clarifier-wording ablation (paper Tables A18-A19, staged from       */
/* paper/tables)                                                       */
/* ------------------------------------------------------------------ */

export interface WordingComparisonRow {
  modelId: string;
  displayLabel: string;
  originalCenter: number;
  revisedCenter: number;
  centerChange: number;
  originalWidth: number;
  revisedWidth: number;
}

/** Paper Table A18 rows for one quantity: the four April premium models
 *  elicited under both v4 clarifier wordings, pooled per wording. Empty
 *  for the 23 quantities whose prompt text never changed. */
export function loadWordingComparisonRows(
  quantityName: string,
): WordingComparisonRow[] {
  const tablesDir = resolveTablesDir();
  if (!tablesDir) return [];
  const csvPath = path.join(tablesDir, "wording-comparison.csv");
  if (!fs.existsSync(csvPath)) return [];
  const registry = loadModelRegistry();
  const byLabel = new Map(
    [...registry.values()].map((row) => [row.displayLabel, row]),
  );
  const rows = parseCsv(fs.readFileSync(csvPath, "utf-8"), {
    columns: true,
  }) as Record<string, string>[];
  const parsed: WordingComparisonRow[] = [];
  for (const row of rows) {
    if (row["Quantity"] !== quantityName) continue;
    const meta = byLabel.get(row["Model"]);
    if (!meta) continue;
    parsed.push({
      modelId: meta.modelId,
      displayLabel: meta.displayLabel,
      originalCenter: Number(row["Original center"]),
      revisedCenter: Number(row["Revised center"]),
      centerChange: Number(row["Center change"]),
      originalWidth: Number(row["Original 90% width"]),
      revisedWidth: Number(row["Revised 90% width"]),
    });
  }
  return parsed;
}

export interface WordingTauRow {
  modelId: string;
  displayLabel: string;
  originalMedian: number;
  revisedMedian: number;
  originalBand: string;
  revisedBand: string;
}

const TAU_MEDIAN = /^(-?[\d.]+)\s*\[/;

/** Paper Table A19: the A9 implied-tau bootstrap rerun per clarifier
 *  wording for the four dual-elicited models. */
export function loadWordingTauRows(): WordingTauRow[] {
  const tablesDir = resolveTablesDir();
  if (!tablesDir) return [];
  const csvPath = path.join(tablesDir, "wording-comparison-tau.csv");
  if (!fs.existsSync(csvPath)) return [];
  const registry = loadModelRegistry();
  const byLabel = new Map(
    [...registry.values()].map((row) => [row.displayLabel, row]),
  );
  const rows = parseCsv(fs.readFileSync(csvPath, "utf-8"), {
    columns: true,
  }) as Record<string, string>[];
  const parsed: WordingTauRow[] = [];
  for (const row of rows) {
    const meta = byLabel.get(row["Model"]);
    const original = TAU_MEDIAN.exec(
      row["Original implied tau median [90%]"] ?? "",
    );
    const revised = TAU_MEDIAN.exec(
      row["Revised implied tau median [90%]"] ?? "",
    );
    if (!meta || !original || !revised) continue;
    parsed.push({
      modelId: meta.modelId,
      displayLabel: meta.displayLabel,
      originalMedian: Number(original[1]),
      revisedMedian: Number(revised[1]),
      originalBand: row["Original band"] ?? "",
      revisedBand: row["Revised band"] ?? "",
    });
  }
  return parsed;
}

/* ------------------------------------------------------------------ */
/* Verbatim prompts and costs (Process page + quantity pages)          */
/* ------------------------------------------------------------------ */

export interface VerbatimPrompt {
  /** The most widely sent archived text (ties broken deterministically). */
  text: string;
  promptVersion: string;
  /** Models whose archived runs carry exactly `text`. */
  modelCount: number;
  /** Models with any archived prompt for this quantity. */
  totalModels: number;
  /** Models whose archived text differs from `text` (0 for 23 of the 26
   *  quantities; the three sign-clarified quantities carry an earlier
   *  wording for the earliest April models). */
  otherWordingCount: number;
}

/** The exact prompt sent for one quantity, read from the archived
 *  runs.jsonl of the same experiments the dashboard displays. When the
 *  archives carry more than one wording, the majority text is returned
 *  and the split is reported so pages can disclose it instead of
 *  mislabeling the text as universal. */
export function loadVerbatimPrompt(quantityId: string): VerbatimPrompt | null {
  const { resultsDir, gatedModelIds } = getSiteInputs();
  const quantity = getSummaryData().quantities.find(
    (entry) => entry.quantityId === quantityId,
  );
  if (!quantity) return null;

  const variants = new Map<string, { promptVersion: string; models: number }>();
  for (const summary of quantity.modelSummaries) {
    const payload = loadRunPayload(
      quantityId,
      summary.modelName,
      resultsDir,
      gatedModelIds,
    );
    const run = payload?.runs.find((entry) => entry.prompt);
    if (!run?.prompt) continue;
    const variant = variants.get(run.prompt) ?? {
      promptVersion: run.promptVersion,
      models: 0,
    };
    variant.models += 1;
    variants.set(run.prompt, variant);
  }
  if (variants.size === 0) return null;

  const totalModels = [...variants.values()].reduce(
    (total, variant) => total + variant.models,
    0,
  );
  const [text, majority] = [...variants.entries()].sort(
    (a, b) => b[1].models - a[1].models || a[0].localeCompare(b[0]),
  )[0];
  return {
    text,
    promptVersion: majority.promptVersion,
    modelCount: majority.models,
    totalModels,
    otherWordingCount: totalModels - majority.models,
  };
}

/** Run payload for one gated (quantity, model) cell — the same loader the
 *  pages use, wired to the site's results dir and gate. */
export function loadRunPayloadForSite(quantityId: string, modelName: string) {
  const { resultsDir, gatedModelIds } = getSiteInputs();
  return loadRunPayload(quantityId, modelName, resultsDir, gatedModelIds);
}

export interface ArchivedBatchRow {
  dirName: string;
  runs: number;
  totalTokens: number | null;
  /** Sum of the tracked (non-null) cost cells. */
  trackedCostUsd: number;
  /** True when every cost cell in the batch is tracked. */
  fullyTracked: boolean;
  /** True when at least one cost cell is tracked. */
  hasCostData: boolean;
}

/** Every archived batch outside the main elicitation panel (clarify
 *  probes, ablations, pilots, connectivity probes) that carries a
 *  summary.csv, with per-batch run counts and tracked spend. */
export function loadArchivedBatchRows(): ArchivedBatchRow[] {
  const resultsDir = resolveResultsDir();
  const rows: ArchivedBatchRow[] = [];
  for (const entry of fs.readdirSync(resultsDir, { withFileTypes: true })) {
    if (!entry.isDirectory() || entry.name.includes("elasticities")) continue;
    const summaryPath = path.join(resultsDir, entry.name, "summary.csv");
    if (!fs.existsSync(summaryPath)) continue;
    const parsed = parseCsv(fs.readFileSync(summaryPath, "utf-8"), {
      columns: true,
      skip_empty_lines: true,
      relax_quotes: true,
    }) as Record<string, string>[];
    let runs = 0;
    let trackedCostUsd = 0;
    let untrackedCells = 0;
    let trackedCells = 0;
    let totalTokens: number | null = 0;
    for (const row of parsed) {
      runs += Number.parseInt(row.n_successful_runs ?? "0", 10) || 0;
      const cost = row.usage_estimated_total_cost_usd_total;
      if (cost) {
        trackedCostUsd += Number(cost);
        trackedCells += 1;
      } else {
        untrackedCells += 1;
      }
      const tokens = row.usage_total_tokens_total;
      if (totalTokens !== null) {
        totalTokens = tokens ? totalTokens + Number(tokens) : null;
      }
    }
    rows.push({
      dirName: entry.name,
      runs,
      totalTokens,
      trackedCostUsd,
      fullyTracked: untrackedCells === 0,
      hasCostData: trackedCells > 0,
    });
  }
  rows.sort((a, b) => a.dirName.localeCompare(b.dirName));
  return rows;
}

export interface CostRow {
  modelId: string;
  displayLabel: string;
  organizationLabel: string;
  servingProviderPath: string;
  runs: number;
  totalTokens: number | null;
  totalCostUsd: number | null;
  costPerRunUsd: number | null;
}

/** Per-model usage and tracked cost across the main elicitation batches
 *  the dashboard serves. Models whose serving path reports no
 *  per-request price come back with null cost, mirroring the paper's
 *  em-dash cost columns. */
export function loadCostRows(): CostRow[] {
  const { registry } = getSiteInputs();
  const data = getSummaryData();
  const rows: CostRow[] = [];
  for (const modelName of data.modelNames) {
    const meta = registry.get(modelName);
    if (!meta) {
      throw new Error(`Cost table model is absent from model-registry.csv: ${modelName}`);
    }
    const summaries = data.quantities.flatMap((quantity) =>
      quantity.modelSummaries.filter((summary) => summary.modelName === modelName),
    );
    const runs = summaries.reduce((total, summary) => total + summary.nSuccessfulRuns, 0);
    const totalTokens = sumCompleteOrNull(summaries.map((summary) => summary.totalTokens));
    const totalCostUsd = sumCompleteOrNull(summaries.map((summary) => summary.totalCostUsd));
    rows.push({
      modelId: modelName,
      displayLabel: meta.displayLabel,
      organizationLabel: meta.organizationLabel,
      servingProviderPath: meta.servingProviderPath,
      runs,
      totalTokens,
      totalCostUsd,
      costPerRunUsd:
        totalCostUsd !== null && runs > 0 ? totalCostUsd / runs : null,
    });
  }
  rows.sort(
    (a, b) =>
      (b.totalCostUsd ?? -1) - (a.totalCostUsd ?? -1) ||
      a.displayLabel.localeCompare(b.displayLabel),
  );
  return rows;
}

export { resolveResultsDir };
