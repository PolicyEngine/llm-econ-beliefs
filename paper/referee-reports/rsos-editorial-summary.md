# Editorial summary — Royal Society Open Science simulated round

**Date:** 2026-07-07. **Panel:** rsos-referee1 (statistics), rsos-referee2 (public finance), rsos-referee3 (LLM methods), rsos-referee4 (reproducibility), rsos-referee5 (prior-round adjudication). Reviewed draft: the 17-model panel at PolicyEngine/llm-econ-beliefs main (post-#3).

## Editorial decision: Major revisions (unanimous, 5/5)

Every referee judged the underlying machinery sound and the revision path clear; none recommended reject. The recurring theme is artifact–prose desynchronization introduced by the July table regeneration, plus disclosure gaps around the extension's protocol heterogeneity.

## Critical issues (must address)

1. **Pareto fallback contradiction (4 referees).** The prose describes a microdata-calibrated `a = 1.470` top-tax exercise; the committed Table 4/A13 were silently built on the `a = 1.500` fallback (the PolicyEngine subprocess failed during regeneration). None of the three headline top-rate percentages in the text reproduce from the committed tables, and the A13 note mislabels 1.500 as "the microdata estimate." Fix: make the microdata build actually run (or re-baseline all text on 1.500), and reconcile footnote + both table notes to one value.
2. **Gemini 3.5 Flash is bimodal, not near-zero (referees 5, 2).** On both sign-sensitive quantities the runs split into a negative mode and a large-positive mode (cap gains: 10 neg / 5 pos, mean +0.01 but median −0.40; income: 11 neg / 4 pos). The "centers essentially at zero" framing is sign-canceling-mean masking; `paper.qmd:257` ("negative for every model") contradicts the data; 18 silent quantile repairs concentrate in exactly these cells. Fix: report the bimodality as the finding, correct the contradicted sentences, and disclose repair counts.
3. **Stale prose numbers vs regenerated tables (referees 1, 4, 5).** Rank-spread figures, stability medians, A13 shift ranges, and several top/bottom model namings still reflect the April build. Fix: reconcile every in-text number to one committed build.
4. **The 58 re-elicited failures are untraceable (referees 3, 1, 4, 5).** In-place replacement leaves no committed failure manifest; truncation failures correlate with response length, so "does not select on elicited values" is asserted, not shown. Fix: commit a failure manifest, add an include-vs-exclude sensitivity note, and soften the claim.
5. **Protocol heterogeneity disclosure (referees 3, 1).** Output mechanism, completion budget, sampling regime, and reasoning mode vary with model identity — most acutely for within-Claude April→July comparisons. Fix: per-model harness-disclosure table, within/between-run variance decomposition, explicit caveat on the width ranking for the three no-sampling-parameter models, and ideally a same-model cross-mechanism ablation.
6. **Quantity-count mislabels with a consequently wrong claim (referees 1, 2).** A1/A2/A4/A6 are computed over 13 quantities but labeled "nine-quantity"; "capital gains has the largest spread-to-width ratio" is wrong under either count (TFP persistence at 13; IES at 9).
7. **Benchmark attribution corrections (referee 2).** The ETI band exceeds the actual Saez–Slemrod–Giertz 0.12–0.40 window; Eissa–Liebman 1996 is a participation response, not an elasticity; Imbens–Rubin–Sacerdote is an MPE; capital-gains band uncited. Add all anchor sources to references.bib.
8. **Welfare-weight normalization (referee 2).** `ḡ = a/(a+γ)` is threshold-normalized, not the textbook utilitarian object; it roughly halves the implied optimal rate vs Diamond–Saez. State the normalization, add a `ḡ→0` reference column, qualify the "utilitarian" label.

## Secondary requests

- Dated model snapshots instead of floating aliases where providers offer them (referee 3).
- Cost-accounting scope consistency: April total excludes clarify probes, July includes them; "$60.89 across 6,630 runs" covers 510 probe runs (referee 4).
- RSOS-required statements: data accessibility, funding, competing interests, ethics, license, archived DOI (referee 4).
- Capital-gains audit: suppress implied-τ for non-sign-consistent rows; flag pole-straddling intervals as uninformative (referees 1, 2).
- Monte Carlo standard errors + rank-stability diagnostic to substantiate R=15 for the width ranking (referee 1).
- Support-bounds registry table; tail-extrapolation sensitivity note; residual "posterior/prior" language cleanup (referee 1).

## Noted strengths

- Pooling machinery verified correct (LTV decomposition, nonparametric mixture interval, REML/Bayes) — no correctness errors found (referee 1).
- Byte-identical regeneration of 32/34 tables and both comparison CSVs from committed artifacts; 71/71 tests pass; headline counts verified against raw runs.jsonl (referee 4).
- Estimand now carefully defined; prior rounds' headline asks (domain-split rankings, policy translation, sign-convention clarifiers) genuinely resolved — 10 of 26 prior findings fully resolved, 11 partial (referee 5).
- Saez formula usage and sign-convention algebra correct throughout (referee 2).

## Prior-round adjudication

10/26 resolved, 11/26 partial, 5/26 unresolved (2 renamed, 3 unaddressed). The July extension reintroduced the sign-instability issue the v4 clarifier had closed (as bimodality in gemini-3.5-flash) — see critical issue 2.
