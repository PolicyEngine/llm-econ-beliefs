"use client";

import { useState } from "react";

import { ProviderMark } from "@/components/provider-mark";
import {
  getModelLabel,
  getProviderForModel,
  isJuly2026Model,
} from "@/lib/model-meta";
import type {
  IntervalMethodDefinition,
  IntervalSnapshot,
  ModelSummary,
} from "@/lib/dashboard-types";

interface IntervalPlotProps {
  models: ModelSummary[];
  method: IntervalMethodDefinition;
  onSelectModel?: (modelName: string) => void;
}

const LEFT_GUTTER = 216;
const RIGHT_GUTTER = 132;
const TOP_GUTTER = 30;
const ROW_HEIGHT = 46;
const CHART_WIDTH = 960;

export function IntervalPlot({ models, method, onSelectModel }: IntervalPlotProps) {
  const [hoveredModel, setHoveredModel] = useState<string | null>(null);

  const rows = models
    .map((model) => ({
      model,
      interval: model.intervals[method.id],
    }))
    .filter(
      (row) =>
        row.interval.center !== null ||
        row.interval.lower !== null ||
        row.interval.upper !== null,
    );

  if (!rows.length) {
    return (
      <div
        className="rounded-lg border px-6 py-8 text-center text-sm"
        style={{
          background: "var(--card)",
          borderColor: "var(--border)",
          color: "var(--muted-foreground)",
        }}
      >
        No interval data available for this method.
      </div>
    );
  }

  const allValues = rows.flatMap(({ interval }) =>
    [interval.lower, interval.center, interval.upper].filter(
      (value): value is number => value !== null,
    ),
  );
  const plotWidth = CHART_WIDTH - LEFT_GUTTER - RIGHT_GUTTER;
  const chartHeight = TOP_GUTTER + rows.length * ROW_HEIGHT + 10;
  const ticks = buildNiceTicks(
    Math.min(...allValues, 0),
    Math.max(...allValues, 0),
    6,
  );
  const domainMin = ticks[0] ?? Math.min(...allValues, 0);
  const domainMax = ticks[ticks.length - 1] ?? Math.max(...allValues, 0);
  const zeroInDomain = domainMin <= 0 && domainMax >= 0;
  const zeroX = scaleValue(0, domainMin, domainMax, plotWidth) + LEFT_GUTTER;

  return (
    <div
      className="overflow-hidden rounded-lg border"
      style={{ background: "var(--card)", borderColor: "var(--border)" }}
    >
      <svg
        viewBox={`0 0 ${CHART_WIDTH} ${chartHeight}`}
        className="h-auto w-full"
        role="img"
        aria-label={`${method.label} comparison across models`}
        onMouseLeave={() => setHoveredModel(null)}
      >
        {/* Gridlines and tick labels */}
        {ticks.map((tick) => {
          const x =
            scaleValue(tick, domainMin, domainMax, plotWidth) + LEFT_GUTTER;
          return (
            <g key={tick}>
              <line
                x1={x}
                x2={x}
                y1={TOP_GUTTER - 6}
                y2={chartHeight - 6}
                stroke="var(--border)"
                strokeWidth="1"
              />
              <text
                x={x}
                y={16}
                textAnchor="middle"
                fill="var(--muted-foreground)"
                fontSize="11"
                fontFamily="var(--font-sans), sans-serif"
                style={{ fontVariantNumeric: "tabular-nums" }}
              >
                {formatTickNumber(tick)}
              </text>
            </g>
          );
        })}

        {/* Zero reference line */}
        {zeroInDomain && (
          <line
            x1={zeroX}
            x2={zeroX}
            y1={TOP_GUTTER - 6}
            y2={chartHeight - 6}
            stroke="var(--chart-5)"
            strokeWidth="1.25"
          />
        )}

        {/* Data rows */}
        {rows.map(({ model, interval }, index) => {
          const rowTop = TOP_GUTTER + index * ROW_HEIGHT;
          const y = rowTop + ROW_HEIGHT / 2;
          const isHovered = hoveredModel === model.modelName;
          const provider = getProviderForModel(model.modelName);
          const isNew = isJuly2026Model(model.modelName);
          const lower =
            interval.lower !== null
              ? scaleValue(interval.lower, domainMin, domainMax, plotWidth) +
                LEFT_GUTTER
              : null;
          const upper =
            interval.upper !== null
              ? scaleValue(interval.upper, domainMin, domainMax, plotWidth) +
                LEFT_GUTTER
              : null;
          const center =
            interval.center !== null
              ? scaleValue(interval.center, domainMin, domainMax, plotWidth) +
                LEFT_GUTTER
              : null;

          return (
            <g
              key={model.modelName}
              onMouseEnter={() => setHoveredModel(model.modelName)}
              onClick={onSelectModel ? () => onSelectModel(model.modelName) : undefined}
              style={{ cursor: onSelectModel ? "pointer" : "default" }}
              role={onSelectModel ? "button" : undefined}
              aria-label={
                onSelectModel
                  ? `Inspect ${getModelLabel(model.modelName)} runs`
                  : undefined
              }
            >
              {/* Row hover surface */}
              <rect
                x={0}
                y={rowTop}
                width={CHART_WIDTH}
                height={ROW_HEIGHT}
                fill={isHovered ? "var(--muted)" : "transparent"}
              />

              {/* Provider mark */}
              <foreignObject x={14} y={y - 8} width={16} height={16}>
                <ProviderMark provider={provider} size={14} />
              </foreignObject>

              {/* Model label */}
              <text
                x={38}
                y={y + 4}
                fill="var(--foreground)"
                fontSize="13"
                fontFamily="var(--font-sans), sans-serif"
                fontWeight="500"
              >
                {getModelLabel(model.modelName)}
              </text>

              {/* July 2026 addition marker */}
              {isNew && (
                <g>
                  <title>Added to the panel in July 2026</title>
                  <circle
                    cx={44 + measureLabelWidth(getModelLabel(model.modelName))}
                    cy={y}
                    r={2.5}
                    fill="var(--chart-1)"
                  />
                </g>
              )}

              {/* Interval bar */}
              {lower !== null && upper !== null && (
                <line
                  x1={lower}
                  x2={upper}
                  y1={y}
                  y2={y}
                  stroke="var(--chart-1)"
                  strokeOpacity={isHovered ? 0.5 : 0.35}
                  strokeLinecap="round"
                  strokeWidth="8"
                />
              )}

              {/* Center dot */}
              {center !== null && (
                <>
                  <circle
                    cx={center}
                    cy={y}
                    r={5.5}
                    fill="var(--card)"
                    stroke="var(--chart-1)"
                    strokeWidth="2"
                  />
                  <circle cx={center} cy={y} r={2.6} fill="var(--chart-1)" />
                </>
              )}

              {/* Right-side value label */}
              <text
                x={CHART_WIDTH - 12}
                y={y + 4}
                textAnchor="end"
                fill={isHovered ? "var(--foreground)" : "var(--muted-foreground)"}
                fontSize="11.5"
                fontFamily="var(--font-sans), sans-serif"
                style={{ fontVariantNumeric: "tabular-nums" }}
              >
                {formatIntervalLabel(interval)}
              </text>
            </g>
          );
        })}
      </svg>
    </div>
  );
}

/** Approximate Inter 13px/500 label width for the addition marker offset. */
function measureLabelWidth(label: string): number {
  return label.length * 7.1;
}

function buildNiceTicks(min: number, max: number, targetCount: number): number[] {
  if (!Number.isFinite(min) || !Number.isFinite(max)) return [0];
  if (min === max) return [min];

  const roughStep = Math.abs(max - min) / Math.max(targetCount - 1, 1);
  const step = snap125(roughStep);
  const start = Math.floor(min / step) * step;
  const stop = Math.ceil(max / step) * step;
  const ticks: number[] = [];

  for (let value = start; value <= stop + step * 0.5; value += step) {
    ticks.push(Number(value.toFixed(12)));
  }

  return ticks;
}

function scaleValue(
  value: number,
  min: number,
  max: number,
  width: number,
): number {
  if (max <= min) return width / 2;
  return ((value - min) / (max - min)) * width;
}

function formatIntervalLabel(interval: IntervalSnapshot): string {
  if (
    interval.center === null ||
    interval.lower === null ||
    interval.upper === null
  )
    return "—";
  return `${formatNumber(interval.center)} [${formatNumber(interval.lower)}, ${formatNumber(interval.upper)}]`;
}

function formatNumber(value: number): string {
  const abs = Math.abs(value);
  const fractionDigits = abs >= 10 ? 1 : abs >= 1 ? 2 : 3;
  return new Intl.NumberFormat("en-US", {
    minimumFractionDigits: fractionDigits,
    maximumFractionDigits: fractionDigits,
  }).format(value);
}

function formatTickNumber(value: number): string {
  if (Math.abs(value) < 1e-10) return "0";
  return new Intl.NumberFormat("en-US", {
    maximumFractionDigits: 3,
  }).format(value);
}

function snap125(value: number): number {
  if (value <= 0 || !Number.isFinite(value)) return 1;
  const exponent = Math.floor(Math.log10(value));
  const scale = 10 ** exponent;
  const normalized = value / scale;
  if (normalized <= 1) return scale;
  if (normalized <= 2) return 2 * scale;
  if (normalized <= 5) return 5 * scale;
  return 10 * scale;
}
