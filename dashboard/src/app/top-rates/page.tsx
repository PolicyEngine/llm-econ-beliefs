import { PageBand, ProvenanceFooter } from "@/components/site-chrome";
import { FilteredStripPlot } from "@/components/filtered-strip-plot";
import type { StripRow } from "@/components/strip-plot";
import {
  loadModelRegistry,
  loadTopRateRows,
  slugForModel,
  totalRunCount,
} from "@/lib/site-data";
import Link from "next/link";

export const metadata = {
  title: "Implied top rates · AI beliefs · PolicyEngine",
  description:
    "Each model's elicited taxable-income elasticity mapped through one fixed Saez top-rate calibration: implied top marginal rates with 90 percent bands, for all 28 models.",
};

export default function TopRatesPage() {
  const rows = loadTopRateRows();
  const registry = loadModelRegistry();
  const stripRows: StripRow[] = rows.map((row) => ({
    modelName: row.modelId,
    center: row.topRate,
    lower: row.topRateLower,
    upper: row.topRateUpper,
    href: `/models/${slugForModel(row.modelId)}`,
  }));
  const stripMeta = Object.fromEntries(
    rows.flatMap((row) => {
      const entry = registry.get(row.modelId);
      return entry
        ? [
            [
              row.modelId,
              {
                organization: entry.organization,
                organizationLabel: entry.organizationLabel,
                wave: entry.wave,
                waveLabel: entry.waveLabel,
                isFrontier: entry.isFrontier,
              },
            ],
          ]
        : [];
    }),
  );
  const frontier = rows.filter((row) => row.isFrontier);
  const frontierLow = frontier[0];
  const frontierHigh = frontier[frontier.length - 1];

  const cellStyle = { color: "var(--foreground)" };
  const mutedStyle = { color: "var(--muted-foreground)" };

  return (
    <div>
      <PageBand
        title="Implied top rates"
        lede="One fixed optimal-tax calibration applied to every model's elicited taxable-income elasticity. The exercise maps elicited parameters through a disclosed formula; it computes no optimum of its own and takes no position on what the top rate should be."
      />
      <div className="mx-auto max-w-[1100px] px-5 py-8">
        <p className="max-w-3xl text-sm" style={mutedStyle}>
          Each model&apos;s pooled ETI median enters the Saez top-rate formula
          τ* = (1 − ḡ) / (1 − ḡ + a·e) with a threshold-normalized log-utility
          welfare weight ḡ = 0.618 and a Pareto tail a = 1.621 calibrated from
          PolicyEngine US microdata. The bar spans the rate implied by each
          model&apos;s own 90 percent ETI band — the models&apos; stated
          uncertainty, propagated. Among frontier models the medians run from{" "}
          {frontierLow ? `${frontierLow.topRate.toFixed(1)}%` : "—"} (
          {frontierLow?.displayLabel}) to{" "}
          {frontierHigh ? `${frontierHigh.topRate.toFixed(1)}%` : "—"} (
          {frontierHigh?.displayLabel}).
        </p>
        <div
          className="mt-4 rounded-lg border p-4"
          style={{ borderColor: "var(--border)", background: "var(--card)" }}
        >
          <FilteredStripPlot rows={stripRows} meta={stripMeta} percent />
          <p className="mt-2 text-xs" style={mutedStyle}>
            Dot: implied top rate at the pooled ETI median. Bar: rates implied
            by the model&apos;s own 90 percent ETI interval. Sorted lowest to
            highest; color = provider family. Filters change which models
            render; the axis stays fixed to the full panel.
          </p>
        </div>

        <section className="mt-8">
          <h2 className="text-lg font-semibold" style={cellStyle}>
            Full mapping
          </h2>
          <p className="mt-1 max-w-3xl text-sm" style={mutedStyle}>
            The revenue-max column reports the ḡ → 0 Diamond–Saez benchmark
            1 / (1 + a·e) at the same ETI median. Paper Table 4 documents the
            calibration; Appendix Table A13 re-runs the mapping under
            alternative Pareto tails and CRRA curvature — the cross-model
            ordering survives every variant.
          </p>
          <div
            className="mt-3 overflow-x-auto rounded-lg border"
            style={{ borderColor: "var(--border)", background: "var(--card)" }}
          >
            <table className="w-full text-left text-xs">
              <thead>
                <tr
                  className="border-b"
                  style={{ borderColor: "var(--border)", ...mutedStyle }}
                >
                  <th className="px-3 py-2 font-medium">Model</th>
                  <th className="px-3 py-2 font-medium">ETI median [90%]</th>
                  <th className="px-3 py-2 font-medium">
                    Implied top rate [90%]
                  </th>
                  <th className="px-3 py-2 font-medium">Revenue-max</th>
                  <th className="px-3 py-2 font-medium">90% width (pp)</th>
                </tr>
              </thead>
              <tbody>
                {rows.map((row) => (
                  <tr
                    key={row.modelId}
                    className="border-b last:border-b-0"
                    style={{ borderColor: "var(--border)" }}
                  >
                    <td className="px-3 py-2" style={cellStyle}>
                      <Link
                        className="underline-offset-2 hover:underline"
                        href={`/models/${slugForModel(row.modelId)}`}
                      >
                        {row.displayLabel}
                      </Link>
                      {row.isFrontier ? (
                        <span className="ml-1.5" style={mutedStyle}>
                          · frontier
                        </span>
                      ) : null}
                    </td>
                    <td className="px-3 py-2 font-mono" style={cellStyle}>
                      {row.etiMedian.toFixed(3)} [{row.etiLower.toFixed(2)},{" "}
                      {row.etiUpper.toFixed(2)}]
                    </td>
                    <td className="px-3 py-2 font-mono" style={cellStyle}>
                      {row.topRate.toFixed(1)}% [{row.topRateLower.toFixed(1)}
                      %, {row.topRateUpper.toFixed(1)}%]
                    </td>
                    <td className="px-3 py-2 font-mono" style={mutedStyle}>
                      {row.revenueMax.toFixed(1)}%
                    </td>
                    <td className="px-3 py-2 font-mono" style={mutedStyle}>
                      {row.widthPp.toFixed(1)}
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
          <p className="mt-3 max-w-3xl text-xs" style={mutedStyle}>
            The welfare weight is a normalization choice, not an implication of
            the elicited data, and the within-model bands run far wider than
            the cross-model spread in medians: the models report far more
            parameter uncertainty than their disagreement. Elasticity source:{" "}
            <Link
              className="underline underline-offset-2"
              href="/quantities/tax-elasticity-of-taxable-income-top-earners"
            >
              elasticity of taxable income
            </Link>
            .
          </p>
        </section>
      </div>
      <ProvenanceFooter runCount={totalRunCount()} />
    </div>
  );
}
