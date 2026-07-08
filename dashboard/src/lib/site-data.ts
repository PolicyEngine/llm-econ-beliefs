import fs from "node:fs";
import path from "node:path";

import { parse as parseCsv } from "csv-parse/sync";

import {
  loadDashboardSummaryData,
  loadRunPayload,
  resolveResultsDir,
} from "@/lib/dashboard-data";
import type {
  DashboardSummaryData,
  ModelSummary,
  QuantitySummary,
} from "@/lib/dashboard-types";
import { compareModelNames } from "@/lib/model-meta";

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
  cachedSummaryData ??= loadDashboardSummaryData();
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
  const payload = loadRunPayload(quantityId, modelName);
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
  totalCostUsd: number;
  julyWave: boolean;
} {
  const data = getSummaryData();
  const rows: ModelProfileRow[] = [];
  const widthRanks: number[] = [];
  let totalCostUsd = 0;

  for (const quantityId of CANONICAL_QUANTITY_IDS) {
    const quantity = data.quantities.find((q) => q.quantityId === quantityId);
    if (!quantity) continue;
    const summary = quantity.modelSummaries.find(
      (s) => s.modelName === modelName,
    );
    if (!summary) continue;

    const widths = quantity.modelSummaries
      .map((s) => {
        const { lower, upper } = s.intervals.pooled;
        return lower !== null && upper !== null
          ? { model: s.modelName, width: upper - lower }
          : null;
      })
      .filter((entry): entry is { model: string; width: number } => !!entry)
      .sort((a, b) => a.width - b.width);
    const rankIndex = widths.findIndex((entry) => entry.model === modelName);
    const widthRank = rankIndex === -1 ? null : rankIndex + 1;
    if (widthRank !== null) widthRanks.push(widthRank);

    rows.push({
      quantity,
      summary,
      panelMedian: panelMedianCenter(quantity),
      widthRank,
    });
  }

  for (const quantity of data.quantities) {
    const summary = quantity.modelSummaries.find(
      (s) => s.modelName === modelName,
    );
    if (summary?.totalCostUsd) totalCostUsd += summary.totalCostUsd;
  }

  const avgWidthRank =
    widthRanks.length > 0
      ? widthRanks.reduce((sum, rank) => sum + rank, 0) / widthRanks.length
      : null;

  const julyWave = [
    "gpt-5.5",
    "claude-fable-5",
    "claude-opus-4.8",
    "claude-sonnet-5",
    "gemini-3.5-flash",
    "grok-4.3",
  ].includes(modelName);

  return { rows, avgWidthRank, totalCostUsd, julyWave };
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
