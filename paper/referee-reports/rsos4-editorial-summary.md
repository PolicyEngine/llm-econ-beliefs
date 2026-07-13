# Round 4 editorial summary

**Scope.** Round 4 reviewed the extension from 17 to 25 models (five Chinese-lab models and the GPT-5.6 family; 9,750 runs), the new "What correlates with a model's answers?" section (Tables 5–7), the recovery disclosure, and the hardening infrastructure. Five referees: methodological statistics, public finance, LLM evaluation methodology, reproducibility, and the round-diff adjudicator.

**Process note.** The round ran in two passes. The first pass was cut short by infrastructure limits, but its partial output surfaced five findings — the A16 GLM-5.2 budget contradiction, the A2 rank-spread tie, the stale A14 width-SE range, per-predictor rho rounding, and the stale LOO range — which were verified against the artifacts, fixed, and merged (PR #17, `fa04669`) before the full panel re-reviewed the corrected tree. The adjudicator's charter for the second pass included confirming those fixes were real rather than renamed; it classified all five VERIFIED-FROM-DATA and both previously-open verifier gaps genuinely closed.

## Verdicts

| Referee | Verdict |
|---|---|
| 1 — Statistics | Minor Revision |
| 2 — Public finance | Minor Revision |
| 3 — LLM methods | Minor Revision |
| 4 — Reproducibility | Minor Revision |
| 5 — Round-diff adjudication | Minor Revision |

Unanimous Minor Revision, with every referee stating the required changes are mechanical and several recommending acceptance on revision without a further round. No finding falsified a reported number, overturned a conclusion, or found undisclosed outcome-selected censoring. Positive findings of note: the statistician recomputed the Holm/BH arithmetic by hand and reconciled both load-bearing recovery figures (109/390 and 4,168) against retained archives; the public-finance referee reproduced the tau* mechanics "to the digit"; the reproducibility referee replayed the full offline pipeline to a byte-identical tree; the adjudicator verified all seven numeric claims in the new section from primary CSVs.

## Findings and responses (all applied in the round-4 revision)

**The regression (adjudicator R1 = public finance F1; the round's most severe item).** The Appendix A9 capital-gains audit paragraph still carried 17-model counts ("Sixteen of seventeen sign-consistent… remaining fifteen: eleven … four"), contradicting the abstract's correct 24-of-25 and the regenerated 25-row table. → Rewritten from the table: twenty-four of twenty-five sign-consistent; remaining twenty-three split fifteen ordinary-income / eight LTCG. A `verify_cap_gains_audit` pin now derives all four counts from `cap-gains-convention-audit.csv`, per the adjudicator's revision condition.

**Country-cut multiplicity asymmetry (statistician F2 = public finance F3).** The capability cut was Holm/BH-adjusted over a declared eight-test family; the country cut reported five raw permutation p-values with no correction, under a shared framing sentence implying uniform treatment. → `build_correlates.py` now applies the identical standard to the country cut: Holm and BH over the four tested outcomes, with the top-rate row marked `is_derived` and mirroring the ETI row's adjusted values (one hypothesis, matching Table 6's convention). Table 7 carries the new columns; the section states "the smallest Holm-adjusted p-value is 0.134, so nothing in this cut survives correction either"; the abstract adds "likewise not surviving family correction" to the country claim.

**Budget/reasoning confound axis (LLM methods F1).** The country confound list named serving path and wave but omitted that all five Chinese-lab models ran at uniformly high completion budgets with provider-default reasoning — the axis most relevant to the width contrast. → Added to the abstract's confound clause ("serving path, completion budget, and wave"), the body's caveat list (now four caveats, noting only six US models share the high-budget configuration and that the axis bears most on the width contrast), and the `COUNTRY_DISCLOSURE` string baked into every CSV row.

**Archive-count scoping (statistician F1).** A naive `find` over `failed-runs-archive.jsonl` returns 4,319 records; the stated 4,168 excludes the 151-record GLM pilot archive, and the parenthetical didn't say so. → Scoped to "the five final-panel model directories," with the pilot's 151 records cited inline.

**GLM exhaustion mechanism (statistician F3).** "Exhausted an 8,000-token completion budget on reasoning" was an inference from an empty-response error class, not a recorded finish reason. → Softened in both mentions to the observed signal: empty, no-JSON-content responses consistent with reasoning exhausting the budget, the failure class the 16k rerun eliminated.

**PolicyBench join naming (LLM methods F3).** The three unmatched models and the release pin lived in code and table notes but not the body sentence. → Prose now names `gpt-5.4`, `grok-4.20`, `grok-4.1-fast` and the `dashboard-data-20260709b` pin inline.

**Rendered country CSV disclosure (LLM methods F4).** `paper/tables/correlates-country.csv` dropped the per-row disclosure. → The rendered table now carries Holm/BH columns and its note states the correction, the derived-row convention, and the full confound list including the budget axis.

**A13 stale bounds (public finance F2).** The a=1.3 and gamma=2 shift floors were 17-model values (7.9/8.3); Qwen 3.7 Max's higher ETI extends them to 7.8/8.2. → Corrected, and `verify_top_rate_robustness` now derives all three ranges from the table.

**ETI out-of-band trio (public finance F4).** Prose named two of the three models above the 0.5 anchor, omitting the panel maximum (`qwen-3.7-max` at 0.554). → All three named with centers; `verify_eti_outliers` pins the full set from the comparison CSV.

**README reproduction recipe (reproducibility F1).** The cached-results path omitted `build_correlates.py`, whose absence `build_tables.py` degrades around silently. → Recipe now runs pytest → build_correlates → build_tables → verify_paper_prose, documents the canonical one-way order and the fixed-point property, and the repo-layout tree is refreshed.

**CITATION.cff staleness (reproducibility F2).** Still described the 17-model/6,630-run panel. → Updated to 25 models from nine organizations, 9,750 runs; `date-released` bumped.

**Calibration fallback overwrite (reproducibility F3).** The a=1.5 fallback path unconditionally overwrote the committed microdata calibration JSON, which `build_correlates` then hard-rejects. → `build_tables.py` writes the JSON only when the microdata calibration succeeds, warning and leaving the committed artifact untouched otherwise.

**Dashboard label duplication (reproducibility F4).** Org/wave display labels were re-encoded by hand in TypeScript. → The registry CSV now carries `organization_label` and `wave_label` columns emitted from the Python source of truth; the dashboard consumes them and its hardcoded maps are deleted.

**Adjudicator's verifier-gap list (7 clusters).** All pinned this round: A9 counts, A15 median between-run share range, A4 largest-rank-change and small-move count, A7 increases list, the six benchmark in-range counts, the A14 panel-median center SE (pinned as the median of per-model medians, which rounds to the quoted 0.007), and the country cut's US-organization count. `verify_paper_prose.py` grows from 50 to 68 checks.

**Answered without change.** (a) LLM methods F2 asked whether the A16↔providers.py budget assertion covers gpt-5.5's mixed-budget cell or special-cases it: the assertion is fully generic — membership of the canonical budget over the integers in the disclosed field — so gpt-5.5's "1200 (8000 …)" passes because 8000 is disclosed, and any future budget change in `providers.py` fires on that row like any other. No hardcoded exemption exists. (b) Reproducibility F5 (dashboard methods prose hand-enumerates the roster) is accepted as a manual sync point in an auxiliary app outside the archived reproduction chain.

## Verification of this revision

140 pytest (one new country-multiplicity test), 68/68 prose checks, PDF and HTML re-rendered with string checks for every changed claim, dashboard build 58/58 pages against the extended registry schema, and the regeneration sequence (build_model_registry → build_correlates → build_tables) run end-to-end before committing.

## Editorial decision

All five verdicts are Minor Revision with mechanical fixes, every fix is applied and machine-pinned, and the adjudicator's two revision conditions (the A9 rewrite and its verifier pin) are both met. Per the adjudicator: "No re-review of methods required; a diff of the two changes suffices to move to Accept." The round-4 bar — all verdicts at Minor or better — is satisfied, and the manuscript stands at the same effective status as the round-3 unanimous Accept, now at 25 models.
