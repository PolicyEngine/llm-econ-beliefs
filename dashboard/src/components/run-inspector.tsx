"use client";

import { useState } from "react";

import { providerColor } from "@/components/strip-plot";
import { getModelLabel } from "@/lib/model-meta";
import type { SlimRun } from "@/lib/site-data";

interface ModelRuns {
  modelName: string;
  experimentDir: string;
  runs: SlimRun[];
}

interface RunInspectorProps {
  models: ModelRuns[];
}

/** Human-first run browser: pick a model, see its 15 elicited intervals
 *  with the model's own reasoning sentence per run. Raw artifacts stay in
 *  the repository, linked per experiment directory. */
export function RunInspector({ models }: RunInspectorProps) {
  const [openModel, setOpenModel] = useState<string | null>(null);
  const active = models.find((entry) => entry.modelName === openModel);

  return (
    <section className="mt-8">
      <h2
        className="text-lg font-semibold"
        style={{ color: "var(--foreground)" }}
      >
        Run-level responses
      </h2>
      <p
        className="mt-1 max-w-2xl text-sm"
        style={{ color: "var(--muted-foreground)" }}
      >
        Each model answered 15 independent times. Pick a model to read every
        run: its elicited 90 percent interval, point estimate, and stated
        reasoning.
      </p>

      <div className="mt-3 flex flex-wrap gap-1.5">
        {models.map((entry) => {
          const selected = entry.modelName === openModel;
          return (
            <button
              key={entry.modelName}
              type="button"
              onClick={() =>
                setOpenModel(selected ? null : entry.modelName)
              }
              aria-pressed={selected}
              className="rounded-md border px-2.5 py-1.5 text-sm transition"
              style={{
                borderColor: selected
                  ? providerColor(entry.modelName)
                  : "var(--border)",
                background: selected ? "var(--foreground)" : "var(--card)",
                color: selected ? "var(--background)" : "var(--foreground)",
              }}
            >
              <span
                className="mr-1.5 inline-block h-2 w-2 rounded-full align-middle"
                style={{ background: providerColor(entry.modelName) }}
              />
              {getModelLabel(entry.modelName)}
            </button>
          );
        })}
      </div>

      {active ? <RunList key={active.modelName} entry={active} /> : null}
    </section>
  );
}

function RunList({ entry }: { entry: ModelRuns }) {
  const values = entry.runs.flatMap((run) =>
    [run.p05, run.p95, run.pointEstimate].filter(
      (value): value is number => value !== null,
    ),
  );
  const min = Math.min(...values);
  const max = Math.max(...values);
  const span = max - min || 1;
  const x = (value: number) => ((value - min) / span) * 100;
  const color = providerColor(entry.modelName);

  return (
    <div
      className="mt-4 rounded-lg border"
      style={{ borderColor: "var(--border)", background: "var(--card)" }}
    >
      <ol className="divide-y" style={{ borderColor: "var(--border)" }}>
        {entry.runs.map((run) => (
          <li key={run.runIndex} className="px-4 py-3">
            <div className="flex items-center gap-3">
              <span
                className="w-12 shrink-0 font-mono text-xs"
                style={{ color: "var(--muted-foreground)" }}
              >
                run {run.runIndex}
              </span>
              <svg
                width="100%"
                height={12}
                className="min-w-0 max-w-[420px] flex-1"
                aria-hidden="true"
                style={{ display: "block" }}
              >
                {run.p05 !== null && run.p95 !== null ? (
                  <line
                    x1={`${x(run.p05)}%`}
                    x2={`${x(run.p95)}%`}
                    y1={6}
                    y2={6}
                    stroke={color}
                    strokeOpacity={0.45}
                    strokeWidth={3}
                  />
                ) : null}
                {run.p25 !== null && run.p75 !== null ? (
                  <line
                    x1={`${x(run.p25)}%`}
                    x2={`${x(run.p75)}%`}
                    y1={6}
                    y2={6}
                    stroke={color}
                    strokeWidth={5}
                    strokeOpacity={0.8}
                  />
                ) : null}
                {run.pointEstimate !== null ? (
                  <circle
                    cx={`${x(run.pointEstimate)}%`}
                    cy={6}
                    r={2.6}
                    fill={color}
                  />
                ) : null}
              </svg>
              <span
                className="hidden w-40 shrink-0 text-right font-mono text-xs sm:block"
                style={{ color: "var(--muted-foreground)" }}
              >
                {run.pointEstimate !== null ? run.pointEstimate : "—"}
                {run.p05 !== null && run.p95 !== null
                  ? ` [${run.p05}, ${run.p95}]`
                  : ""}
              </span>
            </div>
            {run.reasoningSummary ? (
              <p
                className="mt-1.5 pl-[3.75rem] text-sm leading-relaxed"
                style={{ color: "var(--foreground)" }}
              >
                {run.reasoningSummary}
              </p>
            ) : null}
          </li>
        ))}
      </ol>
      <p
        className="border-t px-4 py-2.5 text-xs"
        style={{
          borderColor: "var(--border)",
          color: "var(--muted-foreground)",
        }}
      >
        Raw JSON responses and request logs:{" "}
        <a
          className="underline underline-offset-2"
          href={`https://github.com/PolicyEngine/llm-econ-beliefs/tree/main/results/${entry.experimentDir}`}
        >
          results/{entry.experimentDir}
        </a>
      </p>
    </div>
  );
}
