import Link from "next/link";

import { PageBand, ProvenanceFooter } from "@/components/site-chrome";
import {
  getSummaryData,
  loadArchivedBatchRows,
  loadCostRows,
  loadVerbatimPrompt,
  slugForModel,
  totalRunCount,
} from "@/lib/site-data";

export function generateMetadata() {
  const modelCount = getSummaryData().stats.modelCount;
  return {
    title: "Process · AI beliefs · PolicyEngine",
    description: `How the ${modelCount}-model panel was produced: the verbatim elicitation prompt, the generation pipeline, what it cost, and what comes next.`,
  };
}

const REPO = "https://github.com/PolicyEngine/llm-econ-beliefs";

function formatUsd(value: number): string {
  return `$${value.toFixed(2)}`;
}

function formatPerRunUsd(value: number): string {
  return value >= 0.01 ? `$${value.toFixed(3)}` : `$${value.toFixed(5)}`;
}

export default function ProcessPage() {
  const data = getSummaryData();
  const runCount = totalRunCount();
  const prompt = loadVerbatimPrompt(
    "tax.elasticity_of_taxable_income.top_earners",
  );
  const costRows = loadCostRows();
  const trackedRows = costRows.filter((row) => row.totalCostUsd !== null);
  const trackedTotal = trackedRows.reduce(
    (total, row) => total + (row.totalCostUsd ?? 0),
    0,
  );
  const archivedBatches = loadArchivedBatchRows();
  const archivedTracked = archivedBatches.reduce(
    (total, row) => total + row.trackedCostUsd,
    0,
  );

  const cellStyle = { color: "var(--foreground)" };
  const mutedStyle = { color: "var(--muted-foreground)" };

  return (
    <div>
      <PageBand
        title="Process"
        lede={
          <>
            The full production story behind the panel: the exact prompt every
            model received, how {runCount.toLocaleString()} runs became the
            tables on this site, what the elicitation cost, and where the
            project goes next.{" "}
            <Link
              href="/methods"
              className="underline underline-offset-2"
              style={{ color: "var(--foreground)" }}
            >
              Methods
            </Link>{" "}
            covers the estimand, pooling, and per-model harness; this page
            covers how the data came to exist.
          </>
        }
        aside={
          <div
            className="flex items-center gap-5 text-sm"
            style={mutedStyle}
          >
            <span>
              <span className="text-lg font-semibold" style={cellStyle}>
                {data.stats.modelCount}
              </span>{" "}
              models
            </span>
            <span>
              <span className="text-lg font-semibold" style={cellStyle}>
                {data.stats.quantityCount}
              </span>{" "}
              quantities
            </span>
            <span>
              <span className="text-lg font-semibold" style={cellStyle}>
                {runCount.toLocaleString()}
              </span>{" "}
              runs
            </span>
          </div>
        }
      />

      <div className="mx-auto max-w-[1100px] px-5 py-8">
        {/* 1 · The prompt */}
        <section className="max-w-3xl">
          <h2 className="text-lg font-semibold" style={cellStyle}>
            The prompt, verbatim
          </h2>
          <p className="mt-1.5 text-sm leading-relaxed" style={mutedStyle}>
            One template covers all {data.stats.quantityCount}{" "}
            quantities: a memory-only preamble, the quantity&apos;s definition block
            (name, definition, target interpretation, population, units), and
            a task list that requests five subjective quantiles, a point
            estimate pinned to the median, up to three recall-anchor
            citations, and a brief reasoning summary — returned as JSON in
            the shape printed at the bottom of the prompt. Below is the text
            for the{" "}
            <Link
              href="/quantities/tax-elasticity-of-taxable-income-top-earners"
              className="underline underline-offset-2"
              style={cellStyle}
            >
              elasticity of taxable income
            </Link>
            {prompt
              ? prompt.otherWordingCount === 0
                ? `, read from the archived request logs — every one of the ${prompt.totalModels} models received this identical text`
                : `, read from the archived request logs — ${prompt.modelCount} of ${prompt.totalModels} models received exactly this text`
              : ""}
            . Each quantity page shows its own text under &quot;What the
            models were asked.&quot;
          </p>
          {prompt ? (
            <pre
              className="mt-3 overflow-x-auto whitespace-pre-wrap rounded-lg border p-4 font-mono text-xs leading-relaxed"
              style={{
                borderColor: "var(--border)",
                background: "var(--card)",
                color: "var(--foreground)",
              }}
            >
              {prompt.text}
            </pre>
          ) : null}
          <p className="mt-2 text-xs leading-relaxed" style={mutedStyle}>
            Two sign-ambiguous quantities —{" "}
            <Link
              href="/quantities/labor-supply-income-elasticity-prime-age"
              className="underline underline-offset-2"
            >
              income elasticity of labor supply
            </Link>{" "}
            and{" "}
            <Link
              href="/quantities/tax-capital-gains-realizations-elasticity"
              className="underline underline-offset-2"
            >
              capital-gains realizations
            </Link>{" "}
            — carry an extra sign-convention block that defines what the
            reported sign means without calling either direction correct.
            That clarifier text was revised two days into the April 2026
            wave: seven April models keep the original wording, and the four
            April premium models were re-elicited under both. The affected
            quantity pages carry the model-by-model comparison — the two
            headline quantities barely move, while the net-of-tax sibling
            moves materially for two models (paper, Appendix Tables
            A18–A19). How the JSON is enforced (strict schema, forced
            function call, or JSON-object mode) follows each provider&apos;s
            API surface and is disclosed per model in the{" "}
            <Link href="/methods" className="underline underline-offset-2">
              Methods harness table
            </Link>
            .
          </p>
        </section>

        {/* 2 · Pipeline */}
        <section className="mt-10 max-w-3xl">
          <h2 className="text-lg font-semibold" style={cellStyle}>
            From prompt to panel
          </h2>
          <ol
            className="mt-2 list-decimal space-y-2.5 pl-5 text-sm leading-relaxed"
            style={mutedStyle}
          >
            <li>
              <span style={cellStyle}>Registries fix the design.</span>{" "}
              Quantity definitions live in{" "}
              <a
                className="underline underline-offset-2"
                href={`${REPO}/blob/main/llm_econ_beliefs/data/quantities.toml`}
              >
                quantities.toml
              </a>
              ; the model roster, waves, and frontier flags live in{" "}
              <a
                className="underline underline-offset-2"
                href={`${REPO}/blob/main/llm_econ_beliefs/model_registry.py`}
              >
                model_registry.py
              </a>
              . Analysis, paper tables, and this dashboard all read the same
              two registries, so a model or quantity exists everywhere or
              nowhere.
            </li>
            <li>
              <span style={cellStyle}>The runner elicits each cell.</span>{" "}
              <a
                className="underline underline-offset-2"
                href={`${REPO}/blob/main/scripts/run_v4_new_models.py`}
              >
                run_v4_new_models.py
              </a>{" "}
              runs 15 independent draws per model-quantity cell through each
              provider&apos;s structured-output path, one quantity per
              subprocess so request-log cost aggregation survives provider
              quirks. Completion budgets are truncation guards — reasoning
              tokens count against them on models that reason, so budgets
              were raised where required rather than tuned.
            </li>
            <li>
              <span style={cellStyle}>A grid gate admits the panel.</span>{" "}
              <a
                className="underline underline-offset-2"
                href={`${REPO}/blob/main/scripts/check_panel_grid.py`}
              >
                check_panel_grid.py
              </a>{" "}
              verifies every cell against the exact 15-run parsed grid before
              anything downstream runs. Failed slots re-run as fresh
              independent draws and every failure is archived, as Methods
              discloses.
            </li>
            <li>
              <span style={cellStyle}>
                Aggregation turns runs into intervals.
              </span>{" "}
              Each run&apos;s five quantiles become a piecewise-uniform
              distribution; the headline interval is the equal-weight
              90 percent mixture across the 15 runs, with REML and Bayesian
              hierarchical estimators alongside —{" "}
              <Link href="/methods" className="underline underline-offset-2">
                Methods
              </Link>{" "}
              carries the estimand discussion.
            </li>
            <li>
              <span style={cellStyle}>
                Tables build, prose is pinned, pages generate.
              </span>{" "}
              <a
                className="underline underline-offset-2"
                href={`${REPO}/blob/main/paper/build_tables.py`}
              >
                build_tables.py
              </a>{" "}
              regenerates every paper table from the committed artifacts, and{" "}
              <a
                className="underline underline-offset-2"
                href={`${REPO}/blob/main/scripts/verify_paper_prose.py`}
              >
                verify_paper_prose.py
              </a>{" "}
              pins the paper&apos;s quoted numbers to those tables so stale
              claims fail instead of shipping. This site is statically
              generated from the same results tree and table CSVs at build
              time — there is no separate dashboard database to drift.
            </li>
          </ol>
        </section>

        {/* 3 · Costs */}
        <section className="mt-10">
          <h2 className="text-lg font-semibold" style={cellStyle}>
            What it cost
          </h2>
          <p
            className="mt-1.5 max-w-3xl text-sm leading-relaxed"
            style={mutedStyle}
          >
            The paper&apos;s Data section carries the full accounting:{" "}
            <span style={cellStyle}>$66.59</span> of request-log-tracked
            spend — $23.15 for the April main-panel rerun, $37.74 for the
            July frontier additions across their main panel and clarify
            probes, $2.71 for the late Grok 4.5 addition, and $2.99 for the
            late Gemini 3.6 Flash addition. The five original Chinese-lab
            models cost $29.25 at the OpenRouter account level, including
            the failed calls their recovery replaced; per-request costs for
            those models, for Kimi K3 (logged tokens imply roughly $10.69 at
            list prices), and for the GPT-5.6 family are untracked in the
            request logs and appear as em dashes below rather than as
            zeros. Dispersion among tracked models is large — the most
            expensive, Claude Fable 5, whose always-on reasoning is billed
            as output tokens, costs roughly 310 times the cheapest, Grok 4.1
            Fast.
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
                  <th className="px-3 py-2 font-medium">Serving path</th>
                  <th className="px-3 py-2 font-medium">Runs</th>
                  <th className="px-3 py-2 font-medium">Tokens</th>
                  <th className="px-3 py-2 font-medium">Tracked cost</th>
                  <th className="px-3 py-2 font-medium">Per run</th>
                </tr>
              </thead>
              <tbody>
                {costRows.map((row) => (
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
                    </td>
                    <td className="px-3 py-2 font-mono" style={mutedStyle}>
                      {row.servingProviderPath}
                    </td>
                    <td className="px-3 py-2 font-mono" style={mutedStyle}>
                      {row.runs.toLocaleString()}
                    </td>
                    <td className="px-3 py-2 font-mono" style={mutedStyle}>
                      {row.totalTokens !== null
                        ? row.totalTokens.toLocaleString()
                        : "—"}
                    </td>
                    <td className="px-3 py-2 font-mono" style={cellStyle}>
                      {row.totalCostUsd !== null
                        ? formatUsd(row.totalCostUsd)
                        : "—"}
                    </td>
                    <td className="px-3 py-2 font-mono" style={mutedStyle}>
                      {row.costPerRunUsd !== null
                        ? formatPerRunUsd(row.costPerRunUsd)
                        : "—"}
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
          <p className="mt-2 max-w-3xl text-xs leading-relaxed" style={mutedStyle}>
            Tracked cells above sum to {formatUsd(trackedTotal)} across the
            main elicitation batches this site serves ({trackedRows.length} of{" "}
            {costRows.length}{" "}
            models); the paper&apos;s $66.59 additionally
            includes the clarify probes archived alongside them. Costs are
            estimated from logged token usage at provider list prices;
            sources and as-of dates are recorded in{" "}
            <a
              className="underline underline-offset-2"
              href={`${REPO}/blob/main/llm_econ_beliefs/pricing.py`}
            >
              pricing.py
            </a>
            .
          </p>

          <h3 className="mt-6 text-sm font-semibold" style={cellStyle}>
            Archived batches outside the main panel
          </h3>
          <p
            className="mt-1 max-w-3xl text-xs leading-relaxed"
            style={mutedStyle}
          >
            Every other archived batch in the results tree: the Armington and
            IES clarify probes feed the paper&apos;s appendix cross-prompt
            tables, and the ablation, pilot, and connectivity-probe batches
            are kept for provenance. None of these runs enter the headline
            panel.
          </p>
          <details className="mt-2">
            <summary
              className="cursor-pointer text-xs font-medium"
              style={cellStyle}
            >
              All {archivedBatches.length} archived batches
            </summary>
            <div
              className="mt-2 overflow-x-auto rounded-lg border"
              style={{ borderColor: "var(--border)", background: "var(--card)" }}
            >
            <table className="w-full text-left text-xs">
              <thead>
                <tr
                  className="border-b"
                  style={{ borderColor: "var(--border)", ...mutedStyle }}
                >
                  <th className="px-3 py-2 font-medium">Batch</th>
                  <th className="px-3 py-2 font-medium">Runs</th>
                  <th className="px-3 py-2 font-medium">Tokens</th>
                  <th className="px-3 py-2 font-medium">Tracked cost</th>
                </tr>
              </thead>
              <tbody>
                {archivedBatches.map((batch) => (
                  <tr
                    key={batch.dirName}
                    className="border-b last:border-b-0"
                    style={{ borderColor: "var(--border)" }}
                  >
                    <td className="px-3 py-2 font-mono" style={cellStyle}>
                      <a
                        className="underline-offset-2 hover:underline"
                        href={`${REPO}/tree/main/results/${batch.dirName}`}
                      >
                        {batch.dirName}
                      </a>
                    </td>
                    <td className="px-3 py-2 font-mono" style={mutedStyle}>
                      {batch.runs.toLocaleString()}
                    </td>
                    <td className="px-3 py-2 font-mono" style={mutedStyle}>
                      {batch.totalTokens !== null
                        ? batch.totalTokens.toLocaleString()
                        : "—"}
                    </td>
                    <td className="px-3 py-2 font-mono" style={mutedStyle}>
                      {batch.hasCostData
                        ? `${formatUsd(batch.trackedCostUsd)}${batch.fullyTracked ? "" : " (partial)"}`
                        : "—"}
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
            </div>
          </details>
          <p className="mt-2 max-w-3xl text-xs leading-relaxed" style={mutedStyle}>
            Tracked cells across these archived batches add{" "}
            {formatUsd(archivedTracked)}; &quot;partial&quot; marks batches
            where some cost cells are untracked, so the batch total is a
            floor, not a sum.
          </p>
        </section>

        {/* 4 · Next steps */}
        <section className="mt-10 max-w-3xl">
          <h2 className="text-lg font-semibold" style={cellStyle}>
            What comes next
          </h2>
          <ul
            className="mt-2 list-disc space-y-2.5 pl-5 text-sm leading-relaxed"
            style={mutedStyle}
          >
            <li>
              <span style={cellStyle}>New models join as labs ship.</span>{" "}
              The registry-first recipe — add the model to the registry and
              harness config, elicit the identical panel, pass the grid gate
              — is how the panel grew from 11 models to{" "}
              {data.stats.modelCount}, and it is how the next model joins.
              The{" "}
              <a
                className="underline underline-offset-2"
                href={`${REPO}#reproducing-the-v4-panel`}
              >
                README
              </a>{" "}
              documents the path end to end.
            </li>
            <li>
              <span style={cellStyle}>
                Capability re-pins with each PolicyBench release.
              </span>{" "}
              The capability correlations pin to a named PolicyBench release;
              each new release that scores more of the panel refreshes the
              cut and gives the post-hoc run-consistency association — the
              strongest and least protected number in the paper — an
              out-of-sample test.
            </li>
            <li>
              <span style={cellStyle}>
                Tool-enabled elicitation is the designed contrast.
              </span>{" "}
              The v4 panel is deliberately memory-only; the prompt builder
              already supports a tools-on regime, and comparing what a model
              answers from memory against what it answers with search and
              code in hand is a natural next experiment.
            </li>
            <li>
              <span style={cellStyle}>The paper hardens toward review.</span>{" "}
              Every number quoted in the manuscript stays pinned to the
              generated tables by the verification script as the panel
              grows, so review revisions and model additions cannot silently
              disagree.
            </li>
          </ul>
        </section>

        <ProvenanceFooter runCount={runCount} />
      </div>
    </div>
  );
}
