import type { ReactNode } from "react";
import Link from "next/link";

import { getModelLabel, getProviderForModel } from "@/lib/model-meta";
import type { BenchmarkBand, SlimRun } from "@/lib/site-data";

/* Provider families map onto the ui-kit chart palette. */
const PROVIDER_CHART_VAR: Record<string, string> = {
  anthropic: "var(--chart-1)",
  openai: "var(--chart-2)",
  google: "var(--chart-3)",
  xai: "var(--chart-4)",
  independent: "var(--chart-5)",
};

export function providerColor(modelName: string): string {
  const provider = getProviderForModel(modelName);
  return provider ? PROVIDER_CHART_VAR[provider] : "var(--chart-5)";
}

export interface StripRow {
  modelName: string;
  center: number | null;
  lower: number | null;
  upper: number | null;
  href?: string;
  runs?: SlimRun[];
  /** Extra marker (e.g. panel median) drawn as a thin vertical tick. */
  referenceValue?: number | null;
}

interface StripPlotProps {
  rows: StripRow[];
  band?: BenchmarkBand | null;
  /** Compact mode drops labels and shrinks geometry (home-page minis). */
  compact?: boolean;
  /** Show the 15 run-level intervals as faint underlays. */
  showRuns?: boolean;
  valueFormatter?: (value: number) => string;
  /** Rows used to compute the shared x-domain (defaults to `rows`).
   *  Filtered views pass the full roster so the scale stays fixed. */
  domainRows?: StripRow[];
}

function formatValue(value: number): string {
  const abs = Math.abs(value);
  if (abs >= 100) return value.toFixed(0);
  if (abs >= 10) return value.toFixed(1);
  return value.toFixed(2);
}

interface Domain {
  min: number;
  max: number;
}

function computeDomain(
  rows: StripRow[],
  band: BenchmarkBand | null,
  showRuns: boolean,
): Domain | null {
  const values: number[] = [];
  for (const row of rows) {
    if (row.lower !== null) values.push(row.lower);
    if (row.upper !== null) values.push(row.upper);
    if (row.center !== null) values.push(row.center);
    if (row.referenceValue !== null && row.referenceValue !== undefined) {
      values.push(row.referenceValue);
    }
    if (showRuns && row.runs) {
      for (const run of row.runs) {
        if (run.p05 !== null) values.push(run.p05);
        if (run.p95 !== null) values.push(run.p95);
      }
    }
  }
  if (band) values.push(band.lower, band.upper);
  if (values.length === 0) return null;

  let min = Math.min(...values);
  let max = Math.max(...values);
  if (min === max) {
    min -= 0.5;
    max += 0.5;
  }
  const pad = (max - min) * 0.05;
  return { min: min - pad, max: max + pad };
}

function percent(domain: Domain, value: number): string {
  return `${(((value - domain.min) / (domain.max - domain.min)) * 100).toFixed(3)}%`;
}

function percentNumber(domain: Domain, value: number): number {
  return ((value - domain.min) / (domain.max - domain.min)) * 100;
}

/** One model's strip: band, zero line, run underlays, interval, dot.
 *  Percentage x-coordinates, so the strip stretches to any container
 *  width without distorting text or markers. */
function RowStrip({
  row,
  domain,
  band,
  showRuns,
  height,
  valueFormatter,
}: {
  row: StripRow;
  domain: Domain;
  band: BenchmarkBand | null;
  showRuns: boolean;
  height: number;
  valueFormatter: (value: number) => string;
}) {
  const color = providerColor(row.modelName);
  const mid = height / 2;
  const zeroInDomain = domain.min < 0 && domain.max > 0;
  const label = getModelLabel(row.modelName);
  // The dot is the sort key, so it must dominate the row: full-opacity
  // fill over a half-opacity bar, separated by a background-color halo.
  const dotRadius = height >= 20 ? 5.5 : 3;
  const dotHalo = height >= 20 ? 2 : 1.25;
  const ariaValue =
    row.center !== null
      ? `${valueFormatter(row.center)}${
          row.lower !== null && row.upper !== null
            ? `, 90 percent interval ${valueFormatter(row.lower)} to ${valueFormatter(row.upper)}`
            : ""
        }`
      : "no estimate";

  return (
    <svg
      width="100%"
      height={height}
      role="img"
      aria-label={`${label}: ${ariaValue}`}
      style={{ display: "block" }}
    >
      {band ? (
        <rect
          x={percent(domain, band.lower)}
          y={0}
          width={`${(
            ((band.upper - band.lower) / (domain.max - domain.min)) *
            100
          ).toFixed(3)}%`}
          height={height}
          fill="var(--muted)"
        />
      ) : null}
      {showRuns && row.runs
        ? row.runs.map((run) =>
            run.p05 !== null && run.p95 !== null ? (
              <line
                key={run.runIndex}
                x1={percent(domain, run.p05)}
                x2={percent(domain, run.p95)}
                y1={mid}
                y2={mid}
                stroke={color}
                strokeOpacity={0.14}
                strokeWidth={Math.min(height - 4, 10)}
              />
            ) : null,
          )
        : null}
      {zeroInDomain ? (
        // Rows butt against each other, so per-row segments read as one
        // continuous rule; solid muted-foreground keeps it visible over
        // the faint run underlays without competing with the data marks.
        <line
          x1={percent(domain, 0)}
          x2={percent(domain, 0)}
          y1={0}
          y2={height}
          stroke="var(--muted-foreground)"
          strokeWidth={1}
        />
      ) : null}
      {row.lower !== null && row.upper !== null ? (
        <line
          x1={percent(domain, row.lower)}
          x2={percent(domain, row.upper)}
          y1={mid}
          y2={mid}
          stroke={color}
          strokeOpacity={0.45}
          strokeWidth={2.5}
          strokeLinecap="round"
        />
      ) : null}
      {row.referenceValue !== null && row.referenceValue !== undefined ? (
        <line
          x1={percent(domain, row.referenceValue)}
          x2={percent(domain, row.referenceValue)}
          y1={mid - 7}
          y2={mid + 7}
          stroke="var(--muted-foreground)"
          strokeWidth={1.5}
        />
      ) : null}
      {row.center !== null ? (
        <circle
          cx={percent(domain, row.center)}
          cy={mid}
          r={dotRadius}
          fill={color}
          stroke="var(--background)"
          strokeWidth={dotHalo}
        />
      ) : null}
    </svg>
  );
}

/** Hover card for one row: the interval values, width, run envelope, and
 *  panel median — everything the trailing column cannot fit. Pure CSS
 *  (group-hover), anchored at the row's dot. */
function RowTooltip({
  row,
  domain,
  showRuns,
  valueFormatter,
}: {
  row: StripRow;
  domain: Domain;
  showRuns: boolean;
  valueFormatter: (value: number) => string;
}) {
  if (row.center === null) return null;
  const anchor = Math.min(92, Math.max(8, percentNumber(domain, row.center)));
  const width =
    row.lower !== null && row.upper !== null ? row.upper - row.lower : null;
  const runStats = (() => {
    if (!showRuns || !row.runs || row.runs.length === 0) return null;
    const lows = row.runs
      .map((run) => run.p05)
      .filter((value): value is number => value !== null);
    const highs = row.runs
      .map((run) => run.p95)
      .filter((value): value is number => value !== null);
    if (lows.length === 0 || highs.length === 0) return null;
    return {
      count: row.runs.length,
      min: Math.min(...lows),
      max: Math.max(...highs),
    };
  })();

  return (
    <div
      aria-hidden="true"
      className="pointer-events-none absolute bottom-full z-10 mb-1 hidden -translate-x-1/2 rounded-md border px-2.5 py-1.5 text-left text-xs leading-relaxed shadow-sm group-hover:block"
      style={{
        left: `${anchor}%`,
        borderColor: "var(--border)",
        background: "var(--card)",
        color: "var(--muted-foreground)",
      }}
    >
      <p
        className="whitespace-nowrap font-medium"
        style={{ color: "var(--foreground)" }}
      >
        {getModelLabel(row.modelName)}
      </p>
      <p className="whitespace-nowrap font-mono">
        center {valueFormatter(row.center)}
        {row.lower !== null && row.upper !== null
          ? ` · 90% [${valueFormatter(row.lower)}, ${valueFormatter(row.upper)}]`
          : ""}
        {width !== null ? ` · width ${valueFormatter(width)}` : ""}
      </p>
      {runStats ? (
        <p className="whitespace-nowrap font-mono">
          {runStats.count} runs · p05–p95 envelope [
          {valueFormatter(runStats.min)}, {valueFormatter(runStats.max)}]
        </p>
      ) : null}
      {row.referenceValue !== null && row.referenceValue !== undefined ? (
        <p className="whitespace-nowrap font-mono">
          panel median {valueFormatter(row.referenceValue)}
        </p>
      ) : null}
    </div>
  );
}

function AxisStrip({
  domain,
  valueFormatter,
}: {
  domain: Domain;
  valueFormatter: (value: number) => string;
}) {
  const ticks = niceTicks(domain.min, domain.max, 5);
  return (
    <svg width="100%" height={20} aria-hidden="true" style={{ display: "block" }}>
      {ticks.map((tick) => {
        const isZero = tick === 0 && domain.min < 0 && domain.max > 0;
        return (
          <g key={tick}>
            <line
              x1={percent(domain, tick)}
              x2={percent(domain, tick)}
              y1={0}
              y2={isZero ? 6 : 4}
              stroke={isZero ? "var(--muted-foreground)" : "var(--border)"}
              strokeWidth={isZero ? 1.5 : 1}
            />
            <text
              x={percent(domain, tick)}
              y={16}
              textAnchor="middle"
              fontSize={11}
              fontWeight={isZero ? 700 : 400}
              fontFamily="var(--font-sans)"
              fill={isZero ? "var(--foreground)" : "var(--muted-foreground)"}
            >
              {isZero ? "0" : valueFormatter(tick)}
            </text>
          </g>
        );
      })}
    </svg>
  );
}

/** Interval plot: one row per model, dot = pooled center, bar = pooled
 *  90% interval, faint ticks = run-level intervals, shaded band =
 *  literature review range. Labels and values are HTML, so the plot
 *  works at any viewport width; the strips share one domain scale. */
export function StripPlot({
  rows,
  band = null,
  compact = false,
  showRuns = false,
  valueFormatter = formatValue,
  domainRows,
}: StripPlotProps): ReactNode {
  const domain = computeDomain(domainRows ?? rows, band, showRuns);
  if (!domain) return null;

  if (compact) {
    return (
      <div>
        {rows.map((row) => (
          <RowStrip
            key={row.modelName}
            row={row}
            domain={domain}
            band={band}
            showRuns={showRuns}
            height={12}
            valueFormatter={valueFormatter}
          />
        ))}
      </div>
    );
  }

  return (
    <div>
      {rows.map((row) => {
        const label = getModelLabel(row.modelName);
        return (
          <div key={row.modelName} className="flex items-center gap-3">
            <span
              className="w-28 shrink-0 truncate text-right text-xs sm:w-40 sm:text-[12.5px]"
              style={{ color: "var(--foreground)" }}
              title={label}
            >
              {row.href ? (
                <Link href={row.href} className="hover:underline">
                  {label}
                </Link>
              ) : (
                label
              )}
            </span>
            <div className="group relative min-w-0 flex-1">
              <RowStrip
                row={row}
                domain={domain}
                band={band}
                showRuns={showRuns}
                height={30}
                valueFormatter={valueFormatter}
              />
              <RowTooltip
                row={row}
                domain={domain}
                showRuns={showRuns}
                valueFormatter={valueFormatter}
              />
            </div>
            {row.center !== null ? (
              <span
                className="hidden w-44 shrink-0 font-mono text-xs md:block"
                style={{ color: "var(--muted-foreground)" }}
              >
                {valueFormatter(row.center)}
                {row.lower !== null && row.upper !== null
                  ? ` [${valueFormatter(row.lower)}, ${valueFormatter(row.upper)}]`
                  : ""}
              </span>
            ) : null}
          </div>
        );
      })}
      <div className="flex items-center gap-3">
        <span className="w-28 shrink-0 sm:w-40" />
        <div className="min-w-0 flex-1">
          <AxisStrip domain={domain} valueFormatter={valueFormatter} />
        </div>
        <span className="hidden w-44 shrink-0 md:block" />
      </div>
    </div>
  );
}

function niceTicks(min: number, max: number, count: number): number[] {
  const span = max - min;
  const rawStep = span / count;
  const magnitude = 10 ** Math.floor(Math.log10(rawStep));
  const candidates = [1, 2, 2.5, 5, 10].map((m) => m * magnitude);
  const step =
    candidates.find((candidate) => candidate >= rawStep) ??
    candidates[candidates.length - 1];
  const start = Math.ceil(min / step) * step;
  const ticks: number[] = [];
  for (let tick = start; tick <= max; tick += step) {
    ticks.push(Number(tick.toFixed(10)));
  }
  return ticks;
}
