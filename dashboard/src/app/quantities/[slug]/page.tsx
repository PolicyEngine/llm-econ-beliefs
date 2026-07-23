import Link from "next/link";
import { notFound } from "next/navigation";

import { FilteredStripPlot } from "@/components/filtered-strip-plot";
import { RunInspector } from "@/components/run-inspector";
import { PageBand, ProvenanceFooter } from "@/components/site-chrome";
import { QUANTITY_FORMULAS } from "@/lib/quantity-formulas";
import {
  SUBPANEL_LABELS,
  getQuantityBySlug,
  getSummaryData,
  loadBenchmarkBands,
  loadModelRegistry,
  loadQuantityRegistry,
  loadSlimRuns,
  loadVerbatimPrompt,
  modelsByCenter,
  slugForModel,
  slugForQuantity,
  subpanelForQuantity,
} from "@/lib/site-data";

interface PageProps {
  params: Promise<{ slug: string }>;
}

const basePath = process.env.NEXT_PUBLIC_BASE_PATH ?? "";

export function generateStaticParams() {
  return getSummaryData().quantities.map((quantity) => ({
    slug: slugForQuantity(quantity.quantityId),
  }));
}

export const dynamicParams = false;

export async function generateMetadata({ params }: PageProps) {
  const { slug } = await params;
  const quantity = getQuantityBySlug(slug);
  if (!quantity) return {};
  const modelCount = getSummaryData().stats.modelCount;
  return {
    title: `${quantity.quantityName} · AI beliefs · PolicyEngine`,
    description: `What ${modelCount} frontier language models answer for the ${quantity.quantityName.toLowerCase()}: pooled centers, 90 percent intervals, and all ${15 * modelCount} run-level responses.`,
  };
}

export default async function QuantityPage({ params }: PageProps) {
  const { slug } = await params;
  const quantity = getQuantityBySlug(slug);
  if (!quantity) notFound();

  const band = loadBenchmarkBands().get(quantity.quantityName) ?? null;
  const subpanel = subpanelForQuantity(quantity.quantityId);
  const ordered = modelsByCenter(quantity);
  const definition = loadQuantityRegistry().get(quantity.quantityId) ?? null;
  const formula = QUANTITY_FORMULAS[quantity.quantityId] ?? null;
  const verbatimPrompt = loadVerbatimPrompt(quantity.quantityId);
  const registry = loadModelRegistry();
  const stripMeta = Object.fromEntries(
    ordered.flatMap((summary) => {
      const entry = registry.get(summary.modelName);
      return entry
        ? [
            [
              summary.modelName,
              {
                organization: entry.organization,
                organizationLabel: entry.organizationLabel,
                isFrontier: entry.isFrontier,
              },
            ],
          ]
        : [];
    }),
  );

  const modelRuns = ordered.map((summary) => ({
    modelName: summary.modelName,
    experimentDir: summary.experimentDir,
    runsJsonHref: `${basePath}/api/runs/${slugForQuantity(quantity.quantityId)}/${slugForModel(summary.modelName)}`,
    runs: loadSlimRuns(quantity.quantityId, summary.modelName),
  }));
  const runsByModel = new Map(
    modelRuns.map((entry) => [entry.modelName, entry.runs]),
  );

  const rows = ordered.map((summary) => ({
    modelName: summary.modelName,
    center: summary.intervals.pooled.center,
    lower: summary.intervals.pooled.lower,
    upper: summary.intervals.pooled.upper,
    runs: runsByModel.get(summary.modelName),
    href: `/models/${slugForModel(summary.modelName)}`,
  }));

  const runCount = ordered.reduce(
    (total, summary) => total + summary.nSuccessfulRuns,
    0,
  );

  return (
    <div>
      <PageBand
        title={quantity.quantityName}
        lede={
          <>
            {SUBPANEL_LABELS[subpanel]} subpanel · pooled centers and 90
            percent intervals from 15 independent runs per model
            {band ? (
              <>
                {" "}
                · shaded region marks the review range{" "}
                <span className="font-mono">
                  [{band.lower}, {band.upper}]
                </span>
              </>
            ) : null}
            .
          </>
        }
        aside={
          <span
            className="font-mono text-xs"
            style={{ color: "var(--muted-foreground)" }}
          >
            {quantity.quantityId}
          </span>
        }
      />

      <div className="mx-auto max-w-[1100px] px-5 py-8">
        {definition ? (
          <div
            className="mb-6 rounded-lg border p-4"
            style={{ borderColor: "var(--border)", background: "var(--card)" }}
          >
            <h2
              className="text-sm font-semibold"
              style={{ color: "var(--foreground)" }}
            >
              What the models were asked
            </h2>
            <p
              className="mt-1.5 max-w-3xl text-sm leading-relaxed"
              style={{ color: "var(--foreground)" }}
            >
              {definition.description}
            </p>
            <dl
              className="mt-3 grid gap-y-1.5 text-xs"
              style={{ color: "var(--muted-foreground)" }}
            >
              {formula ? (
                <div>
                  <dt className="inline font-medium">In standard notation: </dt>
                  <dd
                    className="inline font-serif text-[13px]"
                    style={{ color: "var(--foreground)" }}
                    dangerouslySetInnerHTML={{ __html: formula }}
                  />
                  <span> (shorthand for display; the models received only the prose definition above)</span>
                </div>
              ) : null}
              <div>
                <dt className="inline font-medium">Population: </dt>
                <dd className="inline">{definition.population}</dd>
              </div>
              <div>
                <dt className="inline font-medium">Interpretation: </dt>
                <dd className="inline">{definition.preferredInterpretation}</dd>
              </div>
            </dl>
            {verbatimPrompt ? (
              <details className="mt-3">
                <summary
                  className="cursor-pointer text-xs font-medium"
                  style={{ color: "var(--foreground)" }}
                >
                  The exact prompt, verbatim
                </summary>
                <pre
                  className="mt-2 overflow-x-auto whitespace-pre-wrap rounded-md border p-3 font-mono text-xs leading-relaxed"
                  style={{
                    borderColor: "var(--border)",
                    background: "var(--muted)",
                    color: "var(--foreground)",
                  }}
                >
                  {verbatimPrompt.text}
                </pre>
                <p
                  className="mt-1.5 text-xs"
                  style={{ color: "var(--muted-foreground)" }}
                >
                  Read from the archived request logs;{" "}
                  {verbatimPrompt.otherWordingCount === 0
                    ? `all ${verbatimPrompt.totalModels} models received this identical text`
                    : `${verbatimPrompt.modelCount} of ${verbatimPrompt.totalModels} models received exactly this text, and the other ${verbatimPrompt.otherWordingCount} an earlier v4 wording — every model's prompt is archived verbatim`}
                  . How the JSON response is enforced varies by provider
                  — see the{" "}
                  <Link
                    href="/methods"
                    className="underline underline-offset-2"
                  >
                    Methods harness table
                  </Link>{" "}
                  and the{" "}
                  <Link
                    href="/process"
                    className="underline underline-offset-2"
                  >
                    Process
                  </Link>{" "}
                  page.
                </p>
              </details>
            ) : null}
          </div>
        ) : null}

        <div
          className="rounded-lg border p-4"
          style={{ borderColor: "var(--border)", background: "var(--card)" }}
        >
          <FilteredStripPlot rows={rows} band={band} showRuns meta={stripMeta} />
          <p
            className="mt-2 text-xs"
            style={{ color: "var(--muted-foreground)" }}
          >
            Dot: pooled center (mean of run point estimates). Bar: pooled 90
            percent mixture interval. Faint underlay: each run&apos;s elicited
            p05–p95. Models sorted by center; color = provider family. Filters
            change which models render; the axis stays fixed to the full
            panel.
          </p>
        </div>

        {band?.sources ? (
          <p
            className="mt-3 text-xs leading-relaxed"
            style={{ color: "var(--muted-foreground)" }}
          >
            Review-range sources: {band.sources}. These are hand-coded
            literature anchors, not benchmark truths.
          </p>
        ) : null}

        {quantity.quantityId ===
        "tax.elasticity_of_taxable_income.top_earners" ? (
          <p
            className="mt-3 text-sm"
            style={{ color: "var(--muted-foreground)" }}
          >
            Each model&apos;s elicited ETI implies a top marginal rate under
            one fixed Saez calibration —{" "}
            <Link
              className="underline underline-offset-2"
              href="/top-rates"
              style={{ color: "var(--foreground)" }}
            >
              see the implied top rates for all 28 models
            </Link>
            .
          </p>
        ) : null}

        <details className="mt-6">
          <summary
            className="cursor-pointer text-sm font-medium"
            style={{ color: "var(--foreground)" }}
          >
            Alternative estimators (REML and Bayesian hierarchical)
          </summary>
          <div
            className="mt-3 overflow-x-auto rounded-lg border"
            style={{ borderColor: "var(--border)", background: "var(--card)" }}
          >
            <table className="w-full text-left text-xs">
              <thead>
                <tr
                  className="border-b"
                  style={{
                    borderColor: "var(--border)",
                    color: "var(--muted-foreground)",
                  }}
                >
                  <th className="px-3 py-2 font-medium">Model</th>
                  <th className="px-3 py-2 font-medium">Pooled 90%</th>
                  <th className="px-3 py-2 font-medium">REML predictive 90%</th>
                  <th className="px-3 py-2 font-medium">
                    Bayes predictive 90%
                  </th>
                </tr>
              </thead>
              <tbody>
                {ordered.map((summary) => (
                  <tr
                    key={summary.modelName}
                    className="border-b last:border-b-0"
                    style={{ borderColor: "var(--border)" }}
                  >
                    <td
                      className="px-3 py-2"
                      style={{ color: "var(--foreground)" }}
                    >
                      <Link
                        href={`/models/${slugForModel(summary.modelName)}`}
                        className="hover:underline"
                      >
                        {summary.modelName}
                      </Link>
                    </td>
                    <IntervalCell snapshot={summary.intervals.pooled} />
                    <IntervalCell snapshot={summary.intervals.remlPredictive} />
                    <IntervalCell
                      snapshot={summary.intervals.bayesPredictive}
                    />
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
          <p
            className="mt-2 text-xs"
            style={{ color: "var(--muted-foreground)" }}
          >
            The paper&apos;s headline object is the pooled mixture interval;
            the alternatives are robustness estimators (paper, Appendix A2).
          </p>
        </details>

        <RunInspector models={modelRuns} />

        <ProvenanceFooter
          runCount={runCount}
          extra={
            <p className="mt-1">
              Result directories:{" "}
              {ordered.slice(0, 3).map((summary, index) => (
                <span key={summary.experimentDir}>
                  {index > 0 ? ", " : ""}
                  <a
                    className="underline underline-offset-2"
                    href={`https://github.com/PolicyEngine/llm-econ-beliefs/tree/main/results/${summary.experimentDir}`}
                  >
                    {summary.experimentDir}
                  </a>
                </span>
              ))}
              {ordered.length > 3 ? `, and ${ordered.length - 3} more` : ""}.
            </p>
          }
        />
      </div>
    </div>
  );
}

function IntervalCell({
  snapshot,
}: {
  snapshot: { center: number | null; lower: number | null; upper: number | null };
}) {
  return (
    <td
      className="px-3 py-2 font-mono"
      style={{ color: "var(--muted-foreground)" }}
    >
      {snapshot.lower !== null && snapshot.upper !== null
        ? `[${round(snapshot.lower)}, ${round(snapshot.upper)}]`
        : "—"}
    </td>
  );
}

function round(value: number): string {
  return Math.abs(value) >= 10 ? value.toFixed(1) : value.toFixed(2);
}
