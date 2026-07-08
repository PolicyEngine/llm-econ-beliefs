import Link from "next/link";
import { notFound } from "next/navigation";

import { PageBand, ProvenanceFooter } from "@/components/site-chrome";
import { StripPlot } from "@/components/strip-plot";
import {
  getModelLabel,
  getProviderForModel,
  PROVIDER_LABELS,
} from "@/lib/model-meta";
import {
  buildModelProfile,
  getModelNameBySlug,
  loadHarnessRows,
  orderedModelNames,
  slugForModel,
  slugForQuantity,
} from "@/lib/site-data";

interface PageProps {
  params: Promise<{ slug: string }>;
}

export function generateStaticParams() {
  return orderedModelNames().map((modelName) => ({
    slug: slugForModel(modelName),
  }));
}

export const dynamicParams = false;

export async function generateMetadata({ params }: PageProps) {
  const { slug } = await params;
  const modelName = getModelNameBySlug(slug);
  if (!modelName) return {};
  const label = getModelLabel(modelName);
  return {
    title: `${label} · AI beliefs · PolicyEngine`,
    description: `${label}'s elicited economic parameter beliefs across the 13-quantity canonical panel: centers, 90 percent intervals, tightness, cost, and harness configuration.`,
  };
}

export default async function ModelPage({ params }: PageProps) {
  const { slug } = await params;
  const modelName = getModelNameBySlug(slug);
  if (!modelName) notFound();

  const label = getModelLabel(modelName);
  const provider = getProviderForModel(modelName);
  const profile = buildModelProfile(modelName);
  const harness = loadHarnessRows().find(
    (row) => row.model.toLowerCase() === label.toLowerCase(),
  );

  const runCount = profile.rows.reduce(
    (total, row) => total + row.summary.nSuccessfulRuns,
    0,
  );

  return (
    <div>
      <PageBand
        title={label}
        lede={
          <>
            {provider ? PROVIDER_LABELS[provider] : "Unknown provider"} ·
            elicited {profile.julyWave ? "July 2026" : "April 2026"} · average
            interval-width rank{" "}
            {profile.avgWidthRank !== null
              ? `#${profile.avgWidthRank.toFixed(1)} of 17`
              : "—"}{" "}
            across the canonical panel ·{" "}
            {profile.totalCostUsd > 0
              ? `$${profile.totalCostUsd.toFixed(2)} total elicitation cost`
              : "cost untracked"}
            .
          </>
        }
        aside={
          <span
            className="font-mono text-xs"
            style={{ color: "var(--muted-foreground)" }}
          >
            {modelName}
          </span>
        }
      />

      <div className="mx-auto max-w-[1100px] px-5 py-8">
        <h2
          className="text-lg font-semibold"
          style={{ color: "var(--foreground)" }}
        >
          Canonical panel profile
        </h2>
        <p
          className="mt-1 max-w-2xl text-sm"
          style={{ color: "var(--muted-foreground)" }}
        >
          One row per canonical quantity, each on its own scale: this
          model&apos;s pooled center and 90 percent interval, with the
          17-model panel median as a gray tick.
        </p>

        <div
          className="mt-4 divide-y rounded-lg border"
          style={{ borderColor: "var(--border)", background: "var(--card)" }}
        >
          {profile.rows.map((row) => (
            <div
              key={row.quantity.quantityId}
              className="flex flex-wrap items-center gap-3 px-4 py-2.5"
              style={{ borderColor: "var(--border)" }}
            >
              <Link
                href={`/quantities/${slugForQuantity(row.quantity.quantityId)}`}
                className="w-64 shrink-0 text-sm hover:underline"
                style={{ color: "var(--foreground)" }}
              >
                {row.quantity.quantityName}
              </Link>
              <div className="min-w-[220px] flex-1">
                <StripPlot
                  rows={[
                    {
                      modelName,
                      center: row.summary.intervals.pooled.center,
                      lower: row.summary.intervals.pooled.lower,
                      upper: row.summary.intervals.pooled.upper,
                      referenceValue: row.panelMedian,
                    },
                  ]}
                  compact
                />
              </div>
              <span
                className="w-40 shrink-0 text-right font-mono text-xs"
                style={{ color: "var(--muted-foreground)" }}
              >
                {row.summary.intervals.pooled.center !== null
                  ? row.summary.intervals.pooled.center.toFixed(3)
                  : "—"}
                {row.panelMedian !== null
                  ? ` · med ${row.panelMedian.toFixed(3)}`
                  : ""}
              </span>
            </div>
          ))}
        </div>

        {harness ? (
          <section className="mt-8">
            <h2
              className="text-lg font-semibold"
              style={{ color: "var(--foreground)" }}
            >
              Generation harness
            </h2>
            <p
              className="mt-1 max-w-2xl text-sm"
              style={{ color: "var(--muted-foreground)" }}
            >
              From the paper&apos;s per-model disclosure (Appendix A16). The
              prompt and repeated-run design are identical across models; the
              output mechanism follows each provider&apos;s API surface.
            </p>
            <dl
              className="mt-3 grid gap-x-6 gap-y-2 rounded-lg border p-4 text-sm sm:grid-cols-2"
              style={{
                borderColor: "var(--border)",
                background: "var(--card)",
              }}
            >
              <HarnessItem label="Provider path" value={harness.providerPath} />
              <HarnessItem label="Output mechanism" value={harness.mechanism} />
              <HarnessItem label="Completion budget" value={harness.budget} />
              <HarnessItem label="Sampling" value={harness.sampling} />
              <HarnessItem label="Reasoning" value={harness.reasoning} />
              <HarnessItem
                label="API identifier"
                value={`${harness.identifier} (${harness.identifierType})`}
              />
            </dl>
          </section>
        ) : null}

        <ProvenanceFooter runCount={runCount} />
      </div>
    </div>
  );
}

function HarnessItem({ label, value }: { label: string; value: string }) {
  return (
    <div>
      <dt
        className="text-xs uppercase tracking-wide"
        style={{ color: "var(--muted-foreground)" }}
      >
        {label}
      </dt>
      <dd style={{ color: "var(--foreground)" }}>{value}</dd>
    </div>
  );
}
