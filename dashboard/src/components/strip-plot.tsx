import type { ReactNode } from "react";

import { getModelLabel, getProviderForModel } from "@/lib/model-meta";
import type { BenchmarkBand, SlimRun } from "@/lib/site-data";

/* Provider families map onto the ui-kit chart palette. */
const PROVIDER_CHART_VAR: Record<string, string> = {
  anthropic: "var(--chart-1)",
  openai: "var(--chart-2)",
  google: "var(--chart-3)",
  xai: "var(--chart-4)",
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
  /** Compact mode drops row labels and shrinks geometry (home-page minis). */
  compact?: boolean;
  /** Show the 15 run-level intervals as faint underlays. */
  showRuns?: boolean;
  valueFormatter?: (value: number) => string;
}

const LABEL_WIDTH = 168;
const VALUE_WIDTH = 118;
const PLOT_WIDTH = 560;

function formatValue(value: number): string {
  const abs = Math.abs(value);
  if (abs >= 100) return value.toFixed(0);
  if (abs >= 10) return value.toFixed(1);
  return value.toFixed(2);
}

/** Static SVG interval plot: one row per model, dot = pooled center,
 *  bar = pooled 90% interval, faint ticks = run-level intervals,
 *  shaded band = literature review range. Server-rendered; no JS. */
export function StripPlot({
  rows,
  band = null,
  compact = false,
  showRuns = false,
  valueFormatter = formatValue,
}: StripPlotProps): ReactNode {
  const rowHeight = compact ? 12 : 30;
  const topPad = compact ? 4 : 8;
  const bottomPad = compact ? 4 : 22;
  const labelWidth = compact ? 0 : LABEL_WIDTH;
  const valueWidth = compact ? 0 : VALUE_WIDTH;
  const plotWidth = compact ? 260 : PLOT_WIDTH;
  const width = labelWidth + plotWidth + valueWidth;
  const height = topPad + rows.length * rowHeight + bottomPad;

  const values: number[] = [];
  for (const row of rows) {
    if (row.lower !== null) values.push(row.lower);
    if (row.upper !== null) values.push(row.upper);
    if (row.center !== null) values.push(row.center);
    if (showRuns && row.runs) {
      for (const run of row.runs) {
        if (run.p05 !== null) values.push(run.p05);
        if (run.p95 !== null) values.push(run.p95);
      }
    }
  }
  if (band) {
    values.push(band.lower, band.upper);
  }
  if (values.length === 0) return null;

  let min = Math.min(...values);
  let max = Math.max(...values);
  if (min === max) {
    min -= 0.5;
    max += 0.5;
  }
  const pad = (max - min) * 0.05;
  min -= pad;
  max += pad;

  const x = (value: number) =>
    labelWidth + ((value - min) / (max - min)) * plotWidth;

  const zeroInDomain = min < 0 && max > 0;
  const axisTicks = compact ? [] : niceTicks(min, max, 5);

  return (
    <svg
      viewBox={`0 0 ${width} ${height}`}
      width="100%"
      role="img"
      aria-label="Interval plot of model estimates"
      style={{ maxWidth: width, display: "block" }}
    >
      {band ? (
        <rect
          x={x(band.lower)}
          y={topPad}
          width={Math.max(x(band.upper) - x(band.lower), 1)}
          height={rows.length * rowHeight}
          fill="var(--muted)"
        >
          <title>{`Review range ${band.lower} to ${band.upper}`}</title>
        </rect>
      ) : null}

      {zeroInDomain ? (
        <line
          x1={x(0)}
          x2={x(0)}
          y1={topPad}
          y2={topPad + rows.length * rowHeight}
          stroke="var(--border)"
          strokeDasharray="3 3"
        />
      ) : null}

      {rows.map((row, index) => {
        const y = topPad + index * rowHeight + rowHeight / 2;
        const color = providerColor(row.modelName);
        const label = getModelLabel(row.modelName);
        return (
          <g key={row.modelName}>
            {!compact ? (
              <text
                x={labelWidth - 10}
                y={y + 4}
                textAnchor="end"
                fontSize={12.5}
                fontFamily="var(--font-sans)"
                fill="var(--foreground)"
              >
                {row.href ? <a href={row.href}>{label}</a> : label}
              </text>
            ) : null}

            {showRuns && row.runs
              ? row.runs.map((run) =>
                  run.p05 !== null && run.p95 !== null ? (
                    <line
                      key={run.runIndex}
                      x1={x(run.p05)}
                      x2={x(run.p95)}
                      y1={y}
                      y2={y}
                      stroke={color}
                      strokeOpacity={0.16}
                      strokeWidth={compact ? 4 : 9}
                    />
                  ) : null,
                )
              : null}

            {row.lower !== null && row.upper !== null ? (
              <line
                x1={x(row.lower)}
                x2={x(row.upper)}
                y1={y}
                y2={y}
                stroke={color}
                strokeWidth={compact ? 1.5 : 2.5}
                strokeLinecap="round"
              />
            ) : null}

            {row.referenceValue !== null &&
            row.referenceValue !== undefined ? (
              <line
                x1={x(row.referenceValue)}
                x2={x(row.referenceValue)}
                y1={y - (compact ? 3 : 8)}
                y2={y + (compact ? 3 : 8)}
                stroke="var(--muted-foreground)"
                strokeWidth={1.5}
              >
                <title>{`Panel median ${valueFormatter(row.referenceValue)}`}</title>
              </line>
            ) : null}

            {row.center !== null ? (
              <circle
                cx={x(row.center)}
                cy={y}
                r={compact ? 2.4 : 4.5}
                fill={color}
              >
                <title>{`${label}: ${valueFormatter(row.center)}${
                  row.lower !== null && row.upper !== null
                    ? ` [${valueFormatter(row.lower)}, ${valueFormatter(row.upper)}]`
                    : ""
                }`}</title>
              </circle>
            ) : null}

            {!compact && row.center !== null ? (
              <text
                x={labelWidth + plotWidth + 10}
                y={y + 4}
                fontSize={12}
                fontFamily="var(--font-mono)"
                fill="var(--muted-foreground)"
              >
                {valueFormatter(row.center)}
                {row.lower !== null && row.upper !== null
                  ? `  [${valueFormatter(row.lower)}, ${valueFormatter(row.upper)}]`
                  : ""}
              </text>
            ) : null}
          </g>
        );
      })}

      {axisTicks.map((tick) => (
        <g key={tick}>
          <line
            x1={x(tick)}
            x2={x(tick)}
            y1={topPad + rows.length * rowHeight}
            y2={topPad + rows.length * rowHeight + 4}
            stroke="var(--border)"
          />
          <text
            x={x(tick)}
            y={topPad + rows.length * rowHeight + 16}
            textAnchor="middle"
            fontSize={11}
            fontFamily="var(--font-sans)"
            fill="var(--muted-foreground)"
          >
            {valueFormatter(tick)}
          </text>
        </g>
      ))}
    </svg>
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
