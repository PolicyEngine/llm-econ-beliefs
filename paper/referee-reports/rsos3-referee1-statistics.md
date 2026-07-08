# Referee Report (Round 3) — Royal Society Open Science

**Referee 1 (uncertainty-quantification / elicitation & ranking-inference statistician)**

**Overall Recommendation:** `Accept`

## Summary

My round-2 recommendation was Major Revision (borderline), held there by a single systematic defect: the abstract and the "Rankings depend on domain" section named specific models as most/least elastic and tightest/widest that the committed 17-model tables contradicted — six enumerated superlatives written against an earlier build. I re-verified each of those six independently in this round by recomputing the top/bottom-3 by both rank columns directly from `model-overview-labor-tax.csv` and `model-overview-macro-trade.csv`, and **all six now match the tables exactly, in the correct order**. The two smaller residuals (B1 stale `a=1.470`, B2 "9-quantity" stability note) are fixed, and both round-2 minor notes (A14 scope, A15 median-vs-max) are addressed with numerically correct sentences. I then did a fresh pass over the `e17d305..cfbceb2` diff, recomputing every quantitative claim the authors changed (income sign/band counts, the LOO 0.982 bound, the ablation width range, the cap-gains sign-consistency count, the new Table-4 median-vs-mean parenthetical, and the "reduced by ~40 percent" restatement) — all reconcile with the committed artifacts, and I found no regression introduced by the fixes. The authors' new `scripts/verify_paper_prose.py` runs clean (27/27) and, on audit, genuinely pins rank *order* (not mere presence) for the ranking trios; it would have caught the round-2 errors. Nothing on the page now contradicts the committed data in my lane.

## Re-verification of round-2 findings (each recomputed, not trusted from the response letter)

Ground truth I recomputed from the committed CSVs (top/bottom-3 by each rank column):

| Subpanel | Most elastic (top-3) | Least elastic (bottom-3) | Tightest | Widest (top-3) |
|---|---|---|---|---|
| Labor-tax | Sonnet 4.6 (4.92), Grok 4.20 (5.75), Grok 4.3 (7.33) | Gemini 3.5 Flash (14.67), GPT-5.5 (13.17), Gemini 3.1 Flash-Lite (10.42) | Fable 5 (4.83), Gemini 3.1 Pro (5.5), Sonnet 5 (6.17) | Grok 4.1 Fast (15.17), GPT-5.4 mini (14.5), Grok 4.20 (13.67) |
| Macro-trade | GPT-5.4 mini (4.33), Grok 4.3 (4.5), Grok 4.20 (4.67) | Opus 4.7 (14.5), Haiku 4.5 (13.5), Gemini 3 Flash (12.33) | Haiku 4.5 (2.0) | Grok 4.20 (16.0), Grok 4.3 (15.67), GPT-5.4 mini (14.5) |

| # | Round-2 finding (severity) | Status | Evidence (recomputed) |
|---|---|---|---|
| A-1 | Abstract macro-trade top pair "GPT-5.4 mini and GPT-5.4 nano" (BLOCKING) | **Fixed** | Now reads "GPT-5.4 mini and Grok 4.3." Matches macro top-2 (4.33, 4.5). Abstract labor pair "Sonnet 4.6 and Grok 4.20" still correct. |
| A-2 | Labor-tax highest trio named GPT-5.4 mini as 3rd (BLOCKING) | **Fixed** | Now "Sonnet 4.6, Grok 4.20, Grok 4.3" — exact top-3, correct order. |
| A-3 | Labor-tax lowest trio (Gemini 3.1 Pro / Flash-Lite / Grok 4.1 Fast) (BLOCKING) | **Fixed** | Now "Gemini 3.5 Flash, GPT-5.5, Gemini 3.1 Flash-Lite" — exact bottom-3, correct order. |
| A-4 | Repeated stale high trio / low-response side (BLOCKING) | **Fixed** | Low-response = correct bottom-3; high-response reworded to "Sonnet 4.6 and the two most recent Grok models" (= Grok 4.20 + Grok 4.3), which is accurate. |
| A-5 | Macro-trade top trio named GPT-5.4 as 2nd (BLOCKING) | **Fixed** | Now "GPT-5.4 mini, Grok 4.3, Grok 4.20" top / "Opus 4.7, Haiku 4.5" bottom — exact, correct order. |
| A-6 | Labor-tax tightest trio omitted Fable 5 (BLOCKING) | **Fixed** | Now "Fable 5, Gemini 3.1 Pro, Sonnet 5" tightest / "Grok 4.1 Fast, GPT-5.4 mini, Grok 4.20" widest; macro "Haiku 4.5" tightest / "Grok 4.20, Grok 4.3, GPT-5.4 mini" widest — all exact, correct order. |
| B-1 | Stray `a = 1.470` in A13 description | **Fixed** | Now `a = 1.621`. `grep` for `1.470`, `a = 1.500`, `1.500` across `paper.qmd` + all tables returns nothing. |
| B-2 | Stability note "9-quantity" vs 221 cells | **Fixed** | `stability-appendix.md` now reads "13-quantity canonical subpanel"; no "9-quantity"; all three rows show 221 cells. |
| C-1 | A14 scope vs subpanel callouts | **Addressed** | Added: A14 "covers the canonical-panel width ordering; the subpanel top-three and bottom-three callouts... carry correspondingly wider resampling bands... read as coarse groupings." |
| C-2 | A15 median-vs-max gap | **Addressed** | Added max single-cell shares `29%` (gpt-5.4-nano), `25%` (gemini-3.5-flash), "no other model exceeds `7%`." Recomputed from `variance-decomposition.csv`: 29, 25, then 7 — exact. |

## Fresh statistical pass over the revision diff (recomputed)

| Claim (changed in round 2) | Recomputed result | Verdict |
|---|---|---|
| Income elasticity "negative for 16 of 17 models... inside the review band for 14 of 17; the other two out-of-band are gpt-5.4-nano (−0.001) and gpt-5.5 (−0.035)" | From `elasticity-all-model-comparison.csv`: 16/17 negative centers (only gemini-3.5-flash `+0.011` positive); band `[-0.15,-0.05]` → 14/17 in range; the 3 out-of-band are gemini-3.5-flash (+0.011), gpt-5.4-nano (−0.001), gpt-5.5 (−0.035), all above the −0.05 upper edge | **Correct — and the restructure is *more* precise than round-2's phrasing** |
| LOO Spearman "between 0.982 and 0.999"; "above 0.98 even on this [macro] subpanel" | `leave-one-provider-out-appendix.csv`: overall min 0.982 (Labor/tax, omit Anthropic), max 0.999; macro-trade rows 0.992–0.999 (all ≥0.98) | **Correct** (was 0.970/0.97) |
| Ablation "widths move from −15 to +7 percent"; "centers by at most 0.03" | `mechanism-ablation.csv`: (Native−LiteLLM)/LiteLLM ranges −15.1% (Frisch) to +6.75% (cap gains) → −15/+7; max \|center change\| = 0.03 | **Correct** |
| Cap-gains "16 of 17 sign-consistent"; "eleven ordinary-income + four LTCG among fifteen informative" | `cap-gains-convention-audit.csv`: 16 sign-consistent, sole exception GPT-5.4 nano ("both negative"); among the 15 informative (gemini-3.5-flash excluded as pole-straddling), 11 ordinary-income + 4 LTCG | **Correct** |
| New parenthetical: "Haiku 4.5's ETI median 0.502 vs mean center 0.507" | `toy-top-rate-labor-tax.csv` ETI median = 0.502; benchmark text mean = 0.507 | **Correct — useful clarification** |
| "reduced by roughly 40 percent" (was "roughly halved") | Headline 30.1–40.2% vs revenue-max 53.1–63.8% → 37–43% reduction | **Correct — an improvement over "halved"** |

No regressions detected. The abstract's "nine-elasticity subset of the 13-quantity canonical panel" relabel is internally coherent (9 elasticities + 4 calibration-style parameters = 13), and the added honest caveats (failure-manifest archiving postdating the July round; OpenAI system-message asymmetry; ablation reasoning-mode confound) are all disclosure improvements with no statistical error.

## Audit of `scripts/verify_paper_prose.py`

The script passes 27/27. Adversarially: `names_in_order()` checks `positions == sorted(positions)`, so it **does verify rank order** (not just presence) for the labor high/low trios, labor tight+wide, macro top trio, and macro widest trio — it would have flagged every round-2 superlative error. Fragment-driven `sentence_with()` fails loudly (returns `""` → check fails) if prose is restructured, so drift is fail-safe. Three non-blocking robustness gaps worth a one-line hardening (the current prose is correct regardless): (i) `names_in_order` accepts an *extra* wrong model appended to a correct trio; (ii) the two abstract-pair checks use presence, not order, and both operate on the same semicolon-joined sentence, so a labor↔macro pair swap would slip through; (iii) the check confirms the named models are the right ones but not that *no other* model is superlatively named. These concern future-build resilience, not the present manuscript.

## New observation (non-blocking, reproducibility-adjacent — outside my primary lane)

While verifying, `paper/build_tables.py` was executed in this environment (by an environment hook/background process — no repo-local `.claude` hook exists) and regenerated the four microdata-dependent tables to `a=1.5` fallback values (e.g., GPT-5.4 nano top rate 30.1%→32.8%; the regenerated headline equals the robustness table's `a=1.5` column while the committed `Baseline (a=1.621)` column stays 40.2%). This is **exactly the behavior the footnote discloses** ("falls back to `a = 1.5` and prints a warning; every number in this section comes from the microdata build committed with the paper"), so it is not a soundness defect — the committed tables are the record and the prose matches them. I restored the tree to byte-identical (`git status` clean, HEAD unchanged). The only courtesy note for the editor: the exact headline top-rate figures reproduce only with PolicyEngine's certified microdata present; the paper discloses this, and `a = mean/(mean−threshold) = 1{,}894{,}129/(1{,}894{,}129 − 725{,}533) = 1.621` is arithmetically checkable from the two reported statistics without the dataset. Whether the microdata version is pinned tightly enough is properly the reproducibility referee's call.

## Verdict: **Accept**

Every issue that held my round-2 recommendation at Major Revision is resolved and, critically, I confirmed each independently by recomputing the rankings and numbers from the committed CSVs rather than trusting the response letter: all six ranking superlatives in the abstract and Results now match the tables in the correct order, the stale `a=1.470` and "9-quantity" residuals are gone, and the two minor notes are addressed with correct numbers. My fresh pass over the diff found the changed quantitative claims (income sign/band, LOO 0.982, ablation −15/+7, cap-gains 16/17, the median-vs-mean and "~40 percent" restatements) all reconcile with the artifacts, with no regression. The core machinery I cleared in round 2 (pooling, resampling SEs, variance decomposition, support bounds) is untouched and remains sound. The authors additionally shipped a machine-checkable harness that pins the ranking order and passes, which materially lowers the risk of this class of prose-to-table drift recurring. Consistent with RSOS's soundness-only standard and the instruction not to manufacture blocking issues, I have nothing left on the page to correct; the two harness-hardening suggestions and the reproducibility courtesy note are optional and non-binding.