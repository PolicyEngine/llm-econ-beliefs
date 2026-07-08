# Referee 5 (Prior-Round Adjudicator) — Round-Diff Adjudication

**Journal:** Royal Society Open Science (soundness criteria: valid methods, conclusions supported by data, complete reporting).
**Manuscript:** `paper/paper.qmd` (rendered `paper.pdf`), tables in `paper/tables/`, artifacts in `results/`.
**Charge:** verify that each major finding from prior rounds (referee1–8, the 11-model panel) was genuinely resolved in the current 17-model draft rather than renamed or suppressed, and flag any prior issue the July 2026 17-model extension reintroduces.

## Executive summary

The revision has genuinely addressed a majority of the prior panel's substantive requests: the estimand is now cleanly reframed as a prompt-conditioned response distribution, the global model ranking has been replaced by domain-specific subpanels, a real policy-translation exercise with propagated uncertainty has been added, decoding settings are reported, the pooling machinery is validated with four robustness appendices, and the draft's planning sections are gone. These are real fixes, not cosmetic ones.

However, the 17-model extension reintroduced the exact failure mode the prior sign-convention fix claimed to have eliminated, and the paper's framing actively masks it. `gemini-3.5-flash` produces bimodal, wrong-sign-laden elicitations on both sign-sensitive quantities; the paper reports the run-level **mean** (≈ +0.01, "centers essentially at zero"), which cancels 5 large positive outliers against 10 negative runs, while the convention-audit table reports the **median** (−0.4, "sign-consistent") for the same cell. The two summary statistics are chosen inconsistently across the paper, and neither disclosure surfaces that one-third of that model's sign-sensitive runs carry the wrong sign or that all 18 of the paper's silently quantile-repaired runs are concentrated in exactly these cells. In addition, the headline policy table (Table 4) and several descriptive-results sentences no longer match the committed artifacts after the extension. These are soundness-relevant (conclusions-vs-data and complete-reporting) defects.

**Recommendation: Major Revisions.**

---

## Prior-findings audit

Status key: **RESOLVED** / **PARTIAL** / **RENAMED-SUPPRESSED** (narrative changed, issue persists) / **NOT ADDRESSED** / **REINTRODUCED** (fixed in round N, broken again by the 17-model extension). Referee tags: R1–R5 = round 1; R6–R8 = round-2 re-reviews.

| # | Prior finding (referees) | Claimed / apparent fix | Status | Evidence |
|---|---|---|---|---|
| 1 | Estimand slides between "belief"/"priors" and a defensible object; reframe as prompt-and-sampling-conditioned distribution (R1-1, R2-1, R3-1, R4-1, R7-1) | Title/subtitle/abstract/intro/interpretation reworded to "prompt-conditioned response distributions"; latent-prior claim explicitly disclaimed | RESOLVED (minor residue) | `paper.qmd:2-3`, `:19`, `:263`; residual "belief" language at `:137` ("generation-to-generation belief shifts") and `:259` |
| 2 | Decoding/sampling settings not reported (R1-min-a, R2-1) | Protocol section states temperature=1.0 where accepted, OpenAI n≤8 batching, per-provider reasoning configs, token budgets | RESOLVED | `paper.qmd:143-147` |
| 3 | R=15 adequacy / iid-from-latent-belief undefended (R2-1, R4-5) | Pragmatic justification + prefix-stability appendix | RESOLVED | `paper.qmd:110`, `:290-296`; `tables/stability-appendix.md` (but prose numbers stale — see #17) |
| 4 | Center/interval hybrid (mixture interval vs mean-of-run-points) unjustified (R1-min-b) | Prose explains the predictive-spread goal | PARTIAL | `paper.qmd:106-108`; justification does not confront the bimodal-sign case where the mean is misleading (see Reintroduced #R1) |
| 5 | Global "responsiveness" ranking across 9 heterogeneous quantities incoherent; use domain splits (R1-2, R3-2, R5-2, R6-1, R7-5) | Global `model-overview.md` dropped from paper; replaced by labor-tax (Table 1) and macro-trade (Table 2) | PARTIAL | `paper.qmd:191`, `:199`, `:209`; global table now an ORPHAN file (`tables/model-overview.md`, not included). Abs-value-rank aggregation across heterogeneous objects persists within each domain |
| 6 | Demote capital-gains out of the labor-tax core; it is not part of the same behavioral block (R3-2, R3-hv, R6-1, R6-hv) | — | NOT ADDRESSED | Capital-gains realizations elasticity is still one of the six quantities aggregated in the labor-tax subpanel (`paper.qmd:197`; `tables/model-overview-labor-tax.md`) |
| 7 | Redesign headline metric to be sign-aware and scale-aware; a wrong-sign answer can look "more responsive" (R2-4) | — | NOT ADDRESSED | Ranking is still average within-quantity **absolute-value** rank; "Mean absolute pooled center" retained (`tables/model-overview-labor-tax.md:1,3`). The gemini-3.5-flash cap-gains case is the exact pathology R2 warned about |
| 8 | No explicit policy calculation; add one PF translation (R1-3, R3-5, R5-5, R6-2, R8-5) | Table 4 (utilitarian top-tax from ETI), Table A12 (flat-tax+demogrant), Table A13 (robustness) | RESOLVED-with-regression | `paper.qmd:223-253`, `:380-396`; numbers do not match the committed table — see Reintroduced #R4 |
| 9 | Propagate elicited uncertainty into the policy object; don't fix a single Pareto/welfare weight (R3-5, R6-2) | Top-rate 90% intervals reported; A13 varies Pareto a and CRRA gamma | RESOLVED | `paper.qmd:247`, `:249`; `tables/top-rate-robustness.md` |
| 10 | Systematic prompt-sensitivity / sign-convention study, not one ad hoc fix (R1-5, R2-2, R3-3, R4-4, R6-3, R7-4, R8-3) | v4 embeds a symmetric direction-first sign clarifier in the main prompt; adds Armington (A7), IES (A8), cap-gains convention audit (A9) | PARTIAL / REINTRODUCED | `paper.qmd:63`, `:255-259`, `:340-366`; clarifier does **not** eliminate wrong-sign outliers for `gemini-3.5-flash` — see Reintroduced #R1 |
| 11 | Disclose that sign-fixed intervals still overlap zero/positive (R2-min-d) | Convention audit reports bootstrap intervals; benchmark table shows counts | PARTIAL | `tables/cap-gains-convention-audit.md` (implied-τ 90% intervals span negatives for gemini-3.5-flash and gpt-5.4-nano); headline mean still labeled "centers essentially at zero" (`paper.qmd:215`) |
| 12 | Separation metric beyond spread-in-centers (interval overlap / pairwise exceedance) (R1-4, R2-4) | "spread / mean 90% width" column added; paper concedes spread < within-model width on every canonical quantity | PARTIAL | `paper.qmd:217`, `:332-338`; `tables/quantity-disagreement.md`. Pairwise-exceedance / overlap probabilities still not reported |
| 13 | Pooling distributional approximation under-validated (R4-2, R7-2) | Stability (A1), REML/Bayes pooling (A2), leave-one-provider-out (A3), alternative quantile rule (A4) | RESOLVED (rank-level) | `paper.qmd:290-320`; full-distribution (tail/mixture) stability still not shown, but the requested checks exist |
| 14 | Leave-one-provider-out robustness (R4-hv, R7-hv) | Appendix Table A3, ρ ∈ [0.982, 0.999] | RESOLVED | `paper.qmd:306-312`; `tables/leave-one-provider-out-appendix.md` |
| 15 | Failure handling / is missingness ignorable; grok-4.20 concentration (R1-min-e, R2-3, R4-3, R7-3) | grok-4.20 v3 failure historicized; v4 = 100% success; `grok-failures-appendix.md` removed | PARTIAL / REINTRODUCED | `paper.qmd:158-160`; new 58 July infrastructure failures re-elicited with non-selection **asserted, not shown** — see Reintroduced #R2 |
| 16 | "Successful run" needs a precise definition incl. monotone quantiles / repair (R2-min-b) | "Successful iff machine-parseable structured output"; "no manual repair" | RENAMED-SUPPRESSED | `paper.qmd:148-149`; the definition omits the automatic quantile-repair step, and all 18 repaired runs sit in gemini-3.5-flash's sign-sensitive cells — see Reintroduced #R3 |
| 17 | "Mean \|point\|" not economically interpretable / unused (R1-min-d, R2-min-c) | Column header renamed "Mean absolute pooled center" | RENAMED-SUPPRESSED | `tables/model-overview-labor-tax.md:3`; still uninterpretable across scales, still never used in the text |
| 18 | Report effective sample size for the headline analysis as prominently as the full run count (R1-min-c) | Subpanel structure clarified; total 6,630 reported | PARTIAL | `paper.qmd:10`, `:69`; subpanel table notes still say "**11 models**" (`tables/model-overview-labor-tax.md:1`, `model-overview-macro-trade.md:1`) though 17 rows are shown |
| 19 | Citations elicited but methodologically unused (R2-min-e) | Acknowledged in limitations as noisy / future normalization | RESOLVED | `paper.qmd:286` |
| 20 | Remove planning / "still to be added" sections (R1-min-f, R2-min-a) | `draft.md` replaced by `paper.qmd`; no planning stubs remain | RESOLVED | `paper.qmd` (no missing-section placeholders); git `e562507` |
| 21 | Benchmark exercise too loose / low evidentiary bar (R3-4, R6-4) | Ranges labeled "not benchmark truths"; honesty retained | PARTIAL | `paper.qmd:211-217`; transparency preserved, evidentiary strength unchanged (centers-only vs wide hand-coded bands) |
| 22 | Be explicit the headline is a subpanel result, not a global ordering over all quantities (R4-6, R7-5) | Repeated statements; legacy row explicitly labeled | RESOLVED | `paper.qmd:69`, `:83-85`, `:191` |
| 23 | Macro-trade side underpowered (3 quantities, no downstream interpretation) (R8-2) | Acknowledged; ranking called "directional" | NOT ADDRESSED (acknowledged) | `paper.qmd:205` |
| 24 | Elevate prompt-sensitivity from robustness check to central finding (R5-4, R8-3) | Foregrounded in interpretation | PARTIAL | `paper.qmd:271`; still one of several near-coequal stories |
| 25 | Provider-mechanism heterogeneity confounds cross-model comparison (R2-3, R3-1, R6-5) | Documented in detail; framed as methods-paper limitation | PARTIAL | `paper.qmd:143-147`; heterogeneity **increased** (native Anthropic strict-JSON path added for the 3 July Claudes alongside LiteLLM forced-function-call for April Claudes) |

**Counts (26 consolidated findings): 10 RESOLVED · 11 PARTIAL · 5 UNRESOLVED (2 renamed-suppressed [#16, #17] + 3 not addressed [#6, #7, #23]).** Three of the PARTIAL rows (#10, #15, #16) are additionally flagged REINTRODUCED and are the highest-priority items below.

---

## Reintroduced issues (17-model extension)

### R1 (CRITICAL). The sign-convention clarifier no longer "eliminates wrong-sign outliers," and the mean/median split hides it

Round-1/2 history: the sign fix (formerly `income-signfix-delta.md`, now removed) was sold as moving models to the correct sign. The current abstract escalates this to a clean confirmation — "the capital-gains convention audit … confirms the sign-convention story holds up: models return a negative w.r.t.-tax-rate elasticity paired with a positive w.r.t.-net-of-tax-rate elasticity" (`paper.qmd:12`) — and the body claims "Under v4, the canonical income elasticity is negative for every model" (`paper.qmd:257`).

Both claims are refuted by the committed data for `gemini-3.5-flash`. The 15 raw capital-gains run point estimates (`results/gemini-3.5-flash-elasticities-batch15/runs.csv`) are:

```
[-0.7, -0.7, -0.7, -0.65, -0.6, -0.6, -0.5, -0.4, -0.2, -0.2, 0.4, 1.2, 1.2, 1.3, 1.3]
mean = +0.010   median = -0.400   (10 negative, 5 large wrong-sign positive)
```

and the income-elasticity runs are `[-0.05 … -0.015]` (11 negative) plus `[0.10, 0.12, 0.12, 0.15]` (4 wrong-sign positive), mean **+0.011**, median −0.020.

Consequences:
- **`paper.qmd:257` is false.** The canonical income-elasticity pooled center for gemini-3.5-flash is **+0.011** (positive), confirmed in `results/elasticity-all-model-comparison.csv` and `tables/benchmark-comparison-labor-tax.md:9` (model max center 0.011) and `tables/quantity-disagreement.md:15`. The sentence "negative for every model" is a stale round-2 claim that the extension falsified; the author updated `paper.qmd:215` to note the gemini-3.5-flash exception but left `:257` contradicting it.
- **The abstract overclaims.** In the audit itself, `gpt-5.4-nano` is `both negative` (−0.35 tax, −0.20 net-of-tax) — i.e. it violates the "negative-tax / positive-net" pattern the abstract states as a blanket result (`tables/cap-gains-convention-audit.md:5`). The story holds for 16/17, not "models return …".
- **The mean/median statistic is chosen inconsistently to make the story look cleaner.** The headline panel uses the run-level **mean** (`paper.qmd:106`), under which gemini-3.5-flash "centers essentially at zero" (`paper.qmd:215`). The convention audit uses the **median** (`tables/cap-gains-convention-audit.md:18`: tax-rate median −0.4, "sign-consistent"). Same 15 runs, opposite verdicts. Neither disclosure states that this cell is bimodal with one-third wrong-sign runs; "centers essentially at zero" mischaracterizes a sign-unstable bimodal distribution as a precise near-zero belief. The audit's own uncertainty column already reveals the incoherence — implied-τ 90% interval `[-0.889, 3.250]` for gemini-3.5-flash and `[-3.592, 5.000]` for gpt-5.4-nano — but the median-based "band" flag ("ordinary-income-rate consistent") papers over it.

Required fix (regenerate, not relabel): report the sign-instability directly (e.g., fraction of wrong-sign runs per cell), use one statistic consistently, and either drop gemini-3.5-flash from the sign-sensitive summaries or foreground it as a counterexample to the "clarifier works" narrative rather than burying it in a mean.

### R2 (MAJOR). "100% parse rate" is a post-replacement figure; the 58 re-elicited July runs revive the missingness-ignorability question

`paper.qmd:158` states "6,630 successful runs at 100% parse rate across all cells" and `:160` "every planned run for every model-quantity cell parsed cleanly into structured JSON." The next sentence concedes that "58 runs (2.3% of the extension) initially failed on infrastructure errors … and were re-elicited as fresh independent draws." The committed data confirms every cell now holds exactly 15 parsed runs (442 cells × 15 = 6,630, all `parsed_ok=True`), i.e. the 100% is measured **after** the failures were replaced.

This is the same failure-handling concern referees 2/4/7 raised for grok-4.20, now re-created and asserted away. The paper says "Because these failures are provider-side artifacts rather than content, the replacement does not select on elicited values" (`paper.qmd:160`). That is not defensible for the budget-exhaustion subset it lists: "empty responses from gpt-5.5 exhausting the completion budget on reasoning" and "three claude-sonnet-5 responses exceeding a 32,000-token output cap" are length/reasoning-correlated failures — precisely the case where re-drawing until success can select toward shorter-reasoning (and potentially different-valued) completions. "100% parse rate" should be scoped as "100% after re-elicitation of 58 infrastructure failures (initial success 97.7% on the extension)," and the non-selection claim needs either evidence (compare failed-then-replaced cells to clean cells) or downgrading to a stated assumption.

### R3 (MAJOR). Silent quantile repair is undisclosed and concentrated entirely in the reintroduced-sign model

Referee 2 explicitly asked that "successful run" specify "monotone quantiles, numeric coercion, no repair." The current definition (`paper.qmd:149`) is only "returns machine-parseable structured output," and `:148` asserts "no manual repair of malformed outputs." But the pipeline performs **automatic** quantile repair (`llm_econ_beliefs/parse.py:324`), flagged per-run as `quantiles_repaired`. In the committed main panel, 18 runs are repaired — and all 18 are in `gemini-3.5-flash`: capital-gains 9/15, income-elasticity 5/15, Marshallian wage 4/15. Several repaired runs are internally contradictory and were still counted "successful" and pooled, e.g. capital-gains run 6 reports `point_estimate = -0.7` with all five quantiles = +1.3, and run 3 reports `point = 0.4` with all quantiles = 1.0 (`results/gemini-3.5-flash-elasticities-batch15/runs.csv`). An earlier commit ("Surface silent quantile repair as a run-level flag and cell-level count") shows the authors track this; the paper does not disclose it. Because the repair is concentrated in exactly the model driving Reintroduced #R1, this is not a bookkeeping nicety — it is material to the sign-sensitive conclusions.

### R4 (MAJOR). The headline policy table does not match the prose, and its committed numbers use the fallback Pareto parameter

The policy exercise (Table 4) is the payoff referees 3/5/6/8 asked for, so its internal consistency matters. The prose asserts a microdata-calibrated Pareto tail: "In the current build, that estimate is a = 1.470" with threshold `$659,618` and tail mean `$2,062,980` (`paper.qmd:231`, `:240`, `:249`). The committed table was built **without** PolicyEngine microdata and fell back to a = 1.500 — its own note reads "fallback Pareto parameter a = 1.500 … g_bar = 0.600" (`tables/toy-top-rate-labor-tax.md:1`; `build_tables.py:33` `TOP_RATE_PARETO_A = 1.5`, fallback path `:1425-1432`, warning `:50-51`). The two do not agree numerically:

| Quantity | Prose (`paper.qmd:247`) | Committed Table 4 | Matches |
|---|---|---|---|
| Gemini 3.1 Pro top rate | 44.3% | 43.2% | neither a=1.470 (44.0%) nor a=1.500 (43.2%) exactly |
| GPT-5.4 nano top rate | 33.5% | 32.8% | prose = a=1.470, table = a=1.500 |
| GPT-5.4 top rate | 39.6% | 38.8% | prose = a=1.470, table = a=1.500 |
| Cross-model spread | "10.8 pp" | 10.4 pp | — |

Likewise `paper.qmd:249` describes moving "from the baseline 1.470 to 1.3," but Appendix Table A13's baseline column is labeled a=1.500 and reproduces the a=1.500 Table 4 column (`tables/top-rate-robustness.md:1`). So the paper's headline top-tax numbers are not reproducible from the committed artifacts — a direct paper-vs-results disagreement (Referee 4's mandate). Either rebuild the tables with the microdata a=1.470 the prose claims, or restate the prose to the a=1.500 the committed pipeline actually produces.

### R5 (MODERATE). Descriptive-results prose still names the 11-model top/bottom sets

The tables were rebuilt to 17 models; the sentences describing them were not. Verified against Tables 1–2:

- Labor-tax top-3 is `[Claude Sonnet 4.6, Grok 4.20, Grok 4.3]`, but `paper.qmd:193` and `:195` say "Claude Sonnet 4.6, Grok 4.20, and GPT-5.4 mini" — the new July model Grok 4.3 (rank 3) is missing; GPT-5.4 mini is now rank 7–8.
- Labor-tax lowest-elasticity trio is `[Gemini 3.1 Flash-Lite, GPT-5.5, Gemini 3.5 Flash]`, but `paper.qmd:193` says "Gemini 3.1 Pro, Gemini 3.1 Flash-Lite, Grok 4.1 Fast" — the two new lowest models (GPT-5.5, Gemini 3.5 Flash) are absent.
- Macro-trade top-3 is `[GPT-5.4 mini, Grok 4.3, Grok 4.20]`, but `paper.qmd:201` says "GPT-5.4 mini, GPT-5.4, and Grok 4.20" (omits Grok 4.3, rank 2) and the abstract (`:12`) says "GPT-5.4 mini and GPT-5.4 nano moving to the top" (nano is rank 4).
- Appendix A2 prose: `paper.qmd:300` says "The largest rank spread is 1.42 positions for Claude Sonnet 4.6," but `tables/pooling-robustness-appendix.md:13` shows Claude Sonnet 4.6 = 1.85 (the max), and 1.42 now belongs to Grok 4.1 Fast (`:18`). The "tighter models" list also omits the new tightest model, Claude Fable 5 (5.15).
- Stability prose: `paper.qmd:110`/`:292` report 10-run median center change "0.001" and width "0.009," but `tables/stability-appendix.md:6` now shows 0.002 and 0.006.

None of these are fatal individually, but together they show the round's prose was not re-synced to its own rebuilt tables — the classic regression-under-fix signature.

### R6 (MINOR). Orphans and stale table notes from the extension
- `tables/model-overview.md` (the retired global ranking) is still present but no longer included anywhere — orphan artifact from the domain-split fix.
- `tables/model-overview-labor-tax.md:1` and `model-overview-macro-trade.md:1` still read "11 models" while listing 17 rows.

---

## New findings (independent of the prior list)

- **Mean-vs-median is a paper-wide coherence problem, not a one-cell issue.** The paper's pooled center is a mean of run-level points (`paper.qmd:106`) but the convention audit, ETI mapping, and top-rate tables key off medians (`tables/cap-gains-convention-audit.md`, `tables/toy-top-rate-labor-tax.md`). For any bimodal cell the two diverge; the paper should state which object each claim uses and why, and check that no cross-table sentence silently switches between them (the ETI benchmark text at `paper.qmd:215` quotes mean-based centers like haiku "0.507," while Table 4 shows the median "0.502").
- **The cap-gains audit's headline reading depends on the same fragile cells it should exclude.** The substantive claim that "most sign-consistent models cluster near τ ≈ 0.5" (`paper.qmd:360`) is computed from bootstrap medians; gemini-3.5-flash (implied-τ 90% `[-0.889, 3.250]`) and gpt-5.4-nano (`[-3.592, 5.000]`) contribute despite being effectively uninformative, and the footnote's "two independent literature anchors" defense is not distinguishable in-data from simple sign noise.
- **Provider-mechanism heterogeneity grew.** Adding the native Anthropic strict-JSON path for the three July Claudes (`paper.qmd:146`) alongside the April Claudes' LiteLLM forced-function-call path means the same provider family now spans two output mechanisms and two reasoning regimes within the panel — worth an explicit within-provider caveat given referees 2/3/6's confounding concern.

The test suite is green (`71 passed`), and all 17 table `{{< include >}}` targets resolve, so there is no build/reference breakage — the defects are in the numbers and the narrative, not the plumbing.

---

## Overall recommendation

**Major Revisions.**

The revision resolves or partially resolves 21 of 26 consolidated prior findings, and the genuinely-resolved set includes the panel's headline asks (estimand precision, domain-split rankings, an uncertainty-propagated policy translation, pooling robustness). That is real progress and the underlying dataset and code are sound. But the 17-model extension reintroduced the precise sign-convention failure the prior fix claimed to eliminate (gemini-3.5-flash), and the manuscript's choices — reporting a sign-canceling mean, switching to a median where that reads better, leaving 18 silent quantile repairs in those same cells undisclosed, and stating "negative for every model" against its own data — mean the current draft's sign-convention and cost/parse-rate conclusions are not yet supported by the artifacts. Combined with a headline policy table whose numbers do not reproduce from the committed build and several stale descriptive sentences, these are soundness-level (conclusions-vs-data and complete-reporting) problems that must be fixed before acceptance, but all are addressable by regenerating tables/statistics and correcting scope rather than by new data collection.

Priority fixes: Reintroduced #R1 (sign statistic + gemini-3.5-flash), #R3 (disclose repair), #R4 (Table 4 Pareto reproducibility), #R2 (parse-rate scoping), then #R5/#R6 (re-sync prose and table notes).
