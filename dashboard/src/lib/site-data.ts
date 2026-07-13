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

export { resolveResultsDir };
