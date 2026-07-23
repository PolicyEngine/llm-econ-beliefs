"use client";

import { useEffect, useMemo, useRef, useState } from "react";

import { StripPlot, type StripRow } from "@/components/strip-plot";
import type { BenchmarkBand } from "@/lib/site-data";

export interface StripModelMeta {
  organization: string;
  organizationLabel: string;
  isFrontier: boolean;
}

type Scope = "all" | "frontier";

const SCOPES: Array<{ key: Scope; label: string }> = [
  { key: "all", label: "All models" },
  { key: "frontier", label: "Frontier (latest per lab)" },
];

function matchesScope(meta: StripModelMeta, scope: Scope): boolean {
  return scope === "all" || meta.isFrontier;
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
 *  roster so intervals remain comparable across filter states. Wave
 *  membership stays visible on model pages, Methods, and Generations —
 *  it is disclosure metadata, not a filter anyone needs here. */
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
  const wroteBackOnce = useRef(false);

  // Lab list is fixed by the full roster (stable dropdown); counts follow
  // the active scope so the numbers always describe what selecting a lab
  // would show.
  const organizations = useMemo(() => {
    const counts = new Map<string, { label: string; count: number }>();
    for (const row of rows) {
      const rowMeta = meta[row.modelName];
      if (!rowMeta) continue;
      const entry = counts.get(rowMeta.organization) ?? {
        label: rowMeta.organizationLabel,
        count: 0,
      };
      if (matchesScope(rowMeta, scope)) entry.count += 1;
      counts.set(rowMeta.organization, entry);
    }
    return [...counts.entries()]
      .map(([key, { label, count }]) => ({ key, label, count }))
      .sort((a, b) => b.count - a.count || a.label.localeCompare(b.label));
  }, [rows, meta, scope]);

  // Filters are shareable: ?scope=frontier&lab=<organization> seeds the
  // state, and changes write back via replaceState. Unknown params
  // (including retired scopes from old links) are ignored.
  useEffect(() => {
    const params = new URLSearchParams(window.location.search);
    const scopeParam = params.get("scope");
    if (scopeParam && SCOPES.some((entry) => entry.key === scopeParam)) {
      setScope(scopeParam as Scope);
    }
    const labParam = params.get("lab");
    if (labParam && organizations.some((entry) => entry.key === labParam)) {
      setOrganization(labParam);
    }
    // organizations is derived from build-time props, so it cannot change
    // between mount and this read.
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);
  useEffect(() => {
    // The mount invocation runs before the URL-seeded state lands and would
    // strip a shared link's params — skip it; every later invocation is a
    // real filter change.
    if (!wroteBackOnce.current) {
      wroteBackOnce.current = true;
      return;
    }
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

  const filtered = rows.filter((row) => {
    const rowMeta = meta[row.modelName];
    if (!rowMeta) return true;
    if (!matchesScope(rowMeta, scope)) return false;
    return organization === "all" || rowMeta.organization === organization;
  });

  const labSelected = organization !== "all";
  const scopedTotal = rows.filter((row) => {
    const rowMeta = meta[row.modelName];
    return !rowMeta || matchesScope(rowMeta, scope);
  }).length;

  return (
    <div>
      <div className="mb-3 flex flex-wrap items-center gap-1.5">
        {SCOPES.map((entry) => (
          <Chip
            key={entry.key}
            label={entry.label}
            selected={scope === entry.key}
            onClick={() => setScope(entry.key)}
          />
        ))}
        <label
          className="ml-1 flex items-center gap-1.5 text-xs"
          style={{ color: "var(--muted-foreground)" }}
        >
          Lab
          <select
            value={organization}
            onChange={(event) => setOrganization(event.target.value)}
            className="rounded-md border px-2 py-0.5 text-xs"
            style={{
              borderColor: labSelected ? "var(--foreground)" : "var(--border)",
              background: labSelected ? "var(--foreground)" : "var(--card)",
              color: labSelected ? "var(--background)" : "var(--foreground)",
            }}
          >
            <option value="all">All labs ({scopedTotal})</option>
            {organizations.map((entry) => (
              <option key={entry.key} value={entry.key}>
                {entry.label} ({entry.count})
              </option>
            ))}
          </select>
        </label>
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
