"use client";

import { useEffect, useMemo, useState } from "react";

import { StripPlot, type StripRow } from "@/components/strip-plot";
import type { BenchmarkBand } from "@/lib/site-data";

export interface StripModelMeta {
  organization: string;
  organizationLabel: string;
  wave: string;
  waveLabel: string;
  isFrontier: boolean;
}

type Scope = "all" | "frontier" | "april" | "july";

const SCOPES: Array<{ key: Scope; label: string }> = [
  { key: "all", label: "All models" },
  { key: "frontier", label: "Frontier (latest per lab)" },
  { key: "april", label: "April 2026" },
  { key: "july", label: "July 2026" },
];

function matchesScope(meta: StripModelMeta, scope: Scope): boolean {
  if (scope === "all") return true;
  if (scope === "frontier") return meta.isFrontier;
  if (scope === "april") return meta.wave === "april_2026";
  return meta.wave.startsWith("july_2026");
}

function Chip({
  label,
  selected,
  onClick,
}: {
  label: string;
  selected: boolean;
  onClick: () => void;
}) {
  return (
    <button
      type="button"
      onClick={onClick}
      aria-pressed={selected}
      className="rounded-full border px-2.5 py-0.5 text-xs transition-colors"
      style={
        selected
          ? {
              background: "var(--foreground)",
              borderColor: "var(--foreground)",
              color: "var(--background)",
            }
          : {
              background: "var(--card)",
              borderColor: "var(--border)",
              color: "var(--muted-foreground)",
            }
      }
    >
      {label}
    </button>
  );
}

/** Strip plot with client-side scope and lab filters. Filtering changes
 *  which models render; the shared x-domain stays fixed to the full
 *  roster so intervals remain comparable across filter states. */
export function FilteredStripPlot({
  rows,
  band = null,
  showRuns = false,
  meta,
  percent = false,
}: {
  rows: StripRow[];
  band?: BenchmarkBand | null;
  showRuns?: boolean;
  meta: Record<string, StripModelMeta>;
  /** Format values as percentages (server components cannot pass functions). */
  percent?: boolean;
}) {
  const [scope, setScope] = useState<Scope>("all");
  const [organization, setOrganization] = useState<string>("all");

  // Filters are shareable: ?scope=frontier|april|july&lab=<organization>
  // seeds the state, and changes write back via replaceState.
  useEffect(() => {
    const params = new URLSearchParams(window.location.search);
    const scopeParam = params.get("scope");
    if (scopeParam && SCOPES.some((entry) => entry.key === scopeParam)) {
      setScope(scopeParam as Scope);
    }
    const labParam = params.get("lab");
    if (labParam) setOrganization(labParam);
  }, []);
  useEffect(() => {
    const params = new URLSearchParams(window.location.search);
    if (scope === "all") params.delete("scope");
    else params.set("scope", scope);
    if (organization === "all") params.delete("lab");
    else params.set("lab", organization);
    const query = params.toString();
    window.history.replaceState(
      null,
      "",
      `${window.location.pathname}${query ? `?${query}` : ""}`,
    );
  }, [scope, organization]);

  const organizations = useMemo(() => {
    const seen = new Map<string, string>();
    for (const row of rows) {
      const rowMeta = meta[row.modelName];
      if (rowMeta && !seen.has(rowMeta.organization)) {
        seen.set(rowMeta.organization, rowMeta.organizationLabel);
      }
    }
    return [...seen.entries()];
  }, [rows, meta]);

  const filtered = rows.filter((row) => {
    const rowMeta = meta[row.modelName];
    if (!rowMeta) return true;
    if (!matchesScope(rowMeta, scope)) return false;
    return organization === "all" || rowMeta.organization === organization;
  });

  return (
    <div>
      <div className="mb-1 flex flex-wrap items-center gap-1.5">
        {SCOPES.map((entry) => (
          <Chip
            key={entry.key}
            label={entry.label}
            selected={scope === entry.key}
            onClick={() => setScope(entry.key)}
          />
        ))}
      </div>
      <div className="mb-3 flex flex-wrap items-center gap-1.5">
        <Chip
          label="All labs"
          selected={organization === "all"}
          onClick={() => setOrganization("all")}
        />
        {organizations.map(([key, label]) => (
          <Chip
            key={key}
            label={label}
            selected={organization === key}
            onClick={() => setOrganization(key)}
          />
        ))}
        <span
          className="ml-auto text-xs"
          style={{ color: "var(--muted-foreground)" }}
        >
          {filtered.length} of {rows.length} models
        </span>
      </div>
      {filtered.length > 0 ? (
        <StripPlot
          rows={filtered}
          band={band}
          showRuns={showRuns}
          domainRows={rows}
          valueFormatter={
            percent ? (value) => `${value.toFixed(1)}%` : undefined
          }
        />
      ) : (
        <p className="py-4 text-sm" style={{ color: "var(--muted-foreground)" }}>
          No models match this filter.
        </p>
      )}
    </div>
  );
}
