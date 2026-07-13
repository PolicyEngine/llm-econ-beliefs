# Referee 3 report (LLM evaluation methodology) — Round 4

*Round 4 reviews the extension from 17 to 25 models, the correlates section, and the recovery disclosure, at HEAD `fa04669`.*

## Summary

This round extends a 17-model panel to 25 models and adds a cross-model correlates section (PolicyBench capability join + US-vs-Chinese-lab cut). My mandate was LLM-methods validity: protocol comparability across serving paths, the GLM-5.2/Kimi re-elicitation history, PolicyBench join validity, GPT-5.6 pooling equivalence, and wave entanglement.

The methods disclosure here is unusually strong for this literature. The five-tier serving-path heterogeneity is disclosed per-model in Appendix Table A16, mirrored in a machine-readable `serving_provider_path` column in `results/model-registry.csv`, bounded empirically by a same-model cross-mechanism ablation (A17), and the draw-regime concern is bounded by a variance decomposition (A15). The PolicyBench join is protected by a build-time crosswalk assertion (`build_correlates.py:306`) that hard-pins the release, the `no_tools`/`us` condition, the exact 3 unmatched panel models, and the 1 leaderboard-only model. The GLM-5.2 8k pilot is structurally excluded from every analysis path. This is the kind of harness bookkeeping most papers in this space omit entirely.

I found no Major issues and nothing that invalidates a result. My findings are refinements: the most substantive is that the country-result confound caveat names "serving path and wave" but omits the completion-budget / reasoning-length axis, which is uniform-high across all five Chinese-lab models and is the axis most relevant to the one reasoning-sensitive outcome (interval width). The rest are naming/rendering completeness items and one build-assertion detail I could not verify. **Verdict: Minor Revision.**

---

## Verified (confirmed against code/artifacts this round)

- **GLM-5.2 8k pilot excluded from all analysis (Focus 2): VERIFIED.** No analysis/build script uses glob-based directory discovery — `grep -rn "rglob\|\.glob(\|glob("` across `scripts/`, `llm_econ_beliefs/`, and `paper/build_tables.py` returned empty. Every loader constructs paths explicitly as `f"{model_id}-elasticities-batch15"` from the 25-entry registry (`build_correlates.py:249`, `build_comparison_artifacts.py:127`, `paper/build_tables.py:1520`). The pilot lives at `results/glm-5.2-8k-pilot-archive/elasticities-batch15/` — its top-level name `glm-5.2-8k-pilot-archive` is not a registry `model_id`, and the nested `elasticities-batch15` can only be reached through a `/` that string-formatting never produces. `check_panel_grid.py` uses explicit model lists (`OPEN_WEIGHTS_MODELS`, `--models`), not globs. The Data section (`paper.qmd:178`) states the pilot "enters no analysis," and `providers.py:59-61` corroborates the "109 of its first 390 runs" figure. Kimi-k2.6's full-panel re-elicitation is likewise disclosed at `paper.qmd:178`.
- **Country/OpenRouter confound disclosed at every appearance (Focus 1): VERIFIED (with one rendering gap, Finding 4).** Abstract (`paper.qmd:12`), body (`paper.qmd:295`), table note (`correlates-country.md:1`), and a per-row `disclosure` column in the source artifact `results/correlates-country.csv` all state the perfect country↔serving-path confound. A16 shows "LiteLLM via OpenRouter" for all five; `model-registry.csv` tags them `openrouter_via_litellm`.
- **PolicyBench release pin + crosswalk (Focus 3): VERIFIED.** `policybench-scores.csv` carries `source_release = dashboard-data-20260709b` on every row; `validate_policybench_crosswalk` (`build_correlates.py:306-368`) asserts a single release, `condition=no_tools`, `country=us`, `EXPECTED_PANEL_ONLY={gpt-5.4, grok-4.20, grok-4.1-fast}`, and `EXPECTED_POLICYBENCH_ONLY={grok-build-0.1}`. 25 panel − 3 unmatched = 22 overlap, matching the prose. The section is consistently framed as descriptive/non-causal (`paper.qmd:283-285`); no implication that models trained on the benchmark.
- **GPT-5.6 pooling equivalence + A16 accuracy, 24/25 rows (Focus 4): VERIFIED.** GPT-5.6 Sol/Luna/Terra run the identical OpenAI Chat Completions path as older GPT models: same `temperature=1.0`, same one-line system message (`providers.py:437-438`, applied unconditionally to all OpenAI requests), same strict JSON schema, same `n≤8` batching. The only difference is the completion budget (8000 vs 1200), set in `OPENAI_MAX_COMPLETION_TOKENS_BY_MODEL` (`providers.py:67-73`) — a non-binding truncation guard given 100% parse rate. No temperature/system-prompt/schema difference that breaks pooling. I cross-checked all 25 A16 budget cells against `providers.py`: **24 match exactly** (native Claude 32000 = `ANTHROPIC_MAX_OUTPUT_TOKENS`; gemini-3.5-flash/grok-4.3 = 4000; the five OpenRouter models = 8000 except glm-5.2 = 16000; all 1200-defaults correct). The one exception is gpt-5.5 (Finding 5).
- **A15/A17 bound the mechanism and draw-regime confounds honestly.** A17 isolates output-mechanism + budget on Opus 4.7 (centers move ≤0.03) and correctly discloses it does *not* bound reasoning-mode; A15 shows between-run variance is a 0-2% median share, bounding the no-sampling-parameter Claude concern.

---

## Findings (most severe first)

### Finding 1 — Country caveat omits the completion-budget / reasoning-length axis (Minor)
**Where:** `paper.qmd:12` (abstract), `paper.qmd:295` (body), `paper/tables/correlates-country.md:1`, and `COUNTRY_DISCLOSURE` in `scripts/build_correlates.py:919-923`.

Every place the country result appears, the confound list reads "serving path and wave." But all five Chinese-lab models also ran at the **high end of the completion-budget range with provider-default reasoning on** (8000, glm-5.2 at 16000; A16), whereas the 20 US-lab models span 1200-32000, with most April models at 1200. Completion budget / reasoning-length therefore co-varies with the country grouping, and it is precisely the axis most relevant to the one reasoning-sensitive outcome the cut reports: **the wider-interval finding** (avg width rank 16.5 vs 11.2, p=0.059).

**Concrete failure scenario:** A reader takes "Chinese-lab models state wider intervals" at face value with only "serving path and wave" flagged as alternatives, and does not consider that these are uniformly high-budget reasoning-on models while much of the US comparison group is low-budget. The width gap could be a reasoning-configuration artifact rather than a lab-origin signal, and the caveat as written does not surface that possibility.

**Why it is Minor, not Major:** (a) budget is *not perfectly* confounded with country — six US models (gpt-5.6×3 at 8000, native Claude×3 at 32000) also sit at the high end, so the axis is de-confoundable, unlike serving path; (b) the mechanism is weak — A15 shows the draw-regime component is a negligible variance share and widths are dominated by models' own stated quantiles, not token counts; (c) all three country findings are already flagged exploratory/directional with p at 0.033-0.059.

**Fix:** Add "completion budget and reasoning configuration" to the co-varying-axis list in the abstract, `paper.qmd:295`, and the `COUNTRY_DISCLOSURE` string — or add one sentence noting that A15 (draw-regime negligible) plus non-binding budgets argue against a budget-width artifact. One clause each.

### Finding 2 — GLM budget assertion is real; the parallel case (gpt-5.5) is NOT VERIFIED (Minor / needs author confirmation)
**Where:** `paper/tables/harness-disclosure.csv:2` / `.md:5` (gpt-5.5 = "1200 (8000 for the 40 re-elicited runs)") vs `providers.py:67-68` (gpt-5.5 = 8000, unconditional); A16 builder/assertion in `paper/build_tables.py` (**not read this round**).

The round-4 fix added a build-time assertion that A16 budgets match `providers.py`. For 24/25 rows this is a clean integer match. gpt-5.5 is the exception: A16 correctly documents the *historical mixed* budget that produced the data (1200 main + 8000 for 40 reruns), while current `providers.py` would run it entirely at 8000. A16 documenting the data-generating config is the *right* choice — but it means the A16↔`providers.py` assertion cannot be naively generic for this cell.

**Concrete failure scenario:** If the assertion special-cases gpt-5.5 by hardcoding the display string rather than deriving it, the "build-time assertion against providers.py" guarantee silently does not cover gpt-5.5 — a future edit to gpt-5.5's budget in `providers.py` would not be caught for that row.

**Fix:** Confirm the A16 builder either (a) derives gpt-5.5's "1200 (8000 for …)" string from a recorded historical value with its own assertion, or (b) explicitly exempts gpt-5.5 with a comment. I did not read the builder, so I mark this **NOT VERIFIED**; low risk since the paper builds cleanly.

### Finding 3 — The 3 unmatched PolicyBench models and the release pin are not named in prose (Minor)
**Where:** `paper.qmd:285` ("22 of the 25 panel models appear on the leaderboard"; "pinned release").

The three unmatched models (gpt-5.4, grok-4.20, grok-4.1-fast) are pinned in code (`build_correlates.py:74`) and visible as em-dashes in Table 5, and the release `dashboard-data-20260709b` appears in the Table 5/6 notes and the scores CSV — but neither is stated in the body sentence itself.

**Concrete failure scenario:** A reader of the prose alone cannot tell *which* 3 models are dropped from the n=22 correlation, and must reverse-engineer it from dashes, leaving open a (baseless here, but unrebutted) worry that the drop is outcome-correlated.

**Fix:** In `paper.qmd:285`, name the three unmatched models parenthetically and state the release pin inline (e.g., "…22 of 25 (all but gpt-5.4, grok-4.20, and grok-4.1-fast, which are absent from the pinned dashboard-data-20260709b leaderboard)"). One sentence.

### Finding 4 — Rendered `paper/tables/correlates-country.csv` drops the `disclosure` column (trivial)
**Where:** `paper/tables/correlates-country.csv` (4 data columns, no disclosure) vs `results/correlates-country.csv` (per-row `disclosure` column).

The paper *includes* the `.md` version, which carries the note, so the manuscript itself is fine. But the shipped table CSV, read in isolation, presents "China − US −3.387, p 0.050" with no confound warning.

**Fix:** Have `build_tables.py` carry the `disclosure` (or a `note` column) into the rendered `paper/tables/correlates-country.csv`, matching the source artifact. Cosmetic.

---

## Not reached / NOT VERIFIED (stated honestly, not verified now)

- **A16↔`providers.py` assertion handling of the gpt-5.5 mixed-budget cell** (Finding 2) — did not read the A16 builder/assertion in `paper/build_tables.py`.
- **External PolicyBench semantic properties** — that the headline predictor is *household-weighted* and that the tax predictor is built from exactly *seven* tax variables are properties of the external release `dashboard-data-20260709b`. `policybench-scores.csv` carries only aggregate columns (`policybench_within_dollar`, `policybench_tax_within_dollar`, `policybench_fedtax_within_dollar`, composite), so I could confirm the paper's *labels* are internally consistent but could not independently verify these two numeric properties from this repo. No evidence against them; flagging as a verification limit, not a finding.
- **`within_wave` sensitivity values** — `build_correlates.py:794-819` computes april-only/july-only Spearman into `results/correlates-sensitivity.csv`, but I did not read the output values. The wave entanglement is disclosed in the abstract, body, and A16 (`paper.qmd:151`, "harness mechanism is confounded with elicitation wave"), and the prose robustness claims lean on leave-one-organization-out and organization-block permutation rather than within-wave rho, so I saw no within-wave overclaiming in prose — but I did not confirm the CSV values themselves (Focus 5 partially verified).
- **`parse.py` quantile-repair uniformity across serving paths** — the paper discloses repair occurs and where it concentrates (gemini-3.5-flash sign-unstable cells, `paper.qmd:233`); I did not audit the repair implementation for cross-provider symmetry. Out of the round-4 extension scope.

---

## VERDICT: Minor Revision

The LLM-methods substance is sound and the disclosure is well above field norm: serving-path heterogeneity, the GLM/Kimi re-elicitation history, and the PolicyBench join are all documented in prose, machine-readable artifacts, and build-time assertions, and the pilot archive is provably excluded. The required changes are small and need no new elicitation: add completion-budget/reasoning to the country-result confound list (Finding 1, the one substantive item), name the 3 unmatched models + release pin in prose (Finding 3), confirm the gpt-5.5 A16 assertion (Finding 2), and carry the disclosure column into the rendered country CSV (Finding 4). None blocks the descriptive, explicitly-exploratory claims the paper makes.
