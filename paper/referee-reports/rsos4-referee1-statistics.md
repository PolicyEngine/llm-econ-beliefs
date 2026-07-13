# Referee 1 report (methodological statistician) — Round 4

*Round 4 reviews the extension from 17 to 25 models (five Chinese-lab models, the GPT-5.6 family), the new "What correlates with a model's answers?" section (Tables 5–7), and the recovery disclosure. An interrupted first pass of this round surfaced five findings, fixed at `fa04669` before this review; the referee was instructed not to re-report them. Tree confirmed byte-identical at HEAD `fa04669`.*

## Summary

The panel extension (17 to 25 models) and the new "What correlates with a model's answers?" section are, statistically, the most careful part of the manuscript. The correlates machinery in `scripts/build_correlates.py` is correct where I could check it: tie-averaged Spearman (mid-ranks, Pearson-on-ranks), two-sided permutation p-values with a fixed seed and the conservative `(hits+1)/(draws+1)` estimator, textbook Holm and Benjamini–Hochberg step procedures with enforced monotonicity, the derived tau* transform correctly excluded from the eight-test family, and an organization-block permutation whose 1,440-assignment reference set matches the 2!·6! combinatorics of the 6/6/4/1×6 organization-size pattern. "Nothing survives Holm" is stated plainly and is true (smallest Holm-adjusted p = 0.135, BH = 0.075; both ≫ 0.05). The country comparison's confound disclosure (serving path, wave, English prompts, attainable-p floor) is present in the abstract, the body, and the CSV disclosure column. The recovery disclosure is honest: the GLM-5.2 "109 of 390" and the "4,168 archived records" both reconcile against retained data, and the censoring is failure-slot replacement, not outcome selection — with the one outcome-correlated channel (length-truncation) disclosed twice.

I found no false number and no undisclosed outcome-selected censoring. My findings are all minor: a reproducibility-wording gap in the archive-count parenthetical, a multiplicity-correction asymmetry between the two cross-model cuts, and an interpretive-label point on the GLM budget-exhaustion mechanism. None undermines a conclusion. Consistent with the rounds 1–3 trajectory, this is a **Minor Revision** — closer to Accept than to Major.

---

## Findings (most-severe-first)

### Finding 1 — Archive-count parenthetical undercounts a naive `find` by the 151-record pilot (Minor; reproducibility/clarity)
**Location:** `paper/paper.qmd:178`
**Claim:** "the re-elicitation script archived all replaced records — `4,168` failure records across the affected directories (`failed-runs-archive.jsonl` per directory) — before an exact-grid checker verified 15 parsed runs in every cell."

**Verified:** Summing `wc -l` over every `failed-runs-archive.jsonl` gives **4,319**; excluding the GLM pilot archive (`results/glm-5.2-8k-pilot-archive/elasticities-batch15/failed-runs-archive.jsonl`, 151 records) gives **exactly 4,168** (deepseek 1,269 + glm-main 64 + kimi 1,530 + minimax 244 + qwen 1,061). The number is correct for the intended set (final-panel directories only).

**Failure scenario:** A referee or replicator auditing reproducibility runs `find results -name failed-runs-archive.jsonl | xargs wc -l`, reads **4,319**, and sees a 151-record discrepancy against the stated 4,168. Because the parenthetical literally says "`failed-runs-archive.jsonl` per directory" — and the pilot directory does contain exactly such a file — the natural verification path contradicts the text, creating a false-positive integrity flag on an otherwise clean disclosure.

**Fix:** Scope the parenthetical to exclude the pilot, e.g. "4,168 failure records across the five final-panel model directories (`failed-runs-archive.jsonl` per directory, excluding the 8k GLM-5.2 pilot archive counted separately below)"; or state the total (4,319) and net out the 151 pilot records explicitly.

### Finding 2 — The two cross-model cuts apply asymmetric multiplicity control; the country cut's five outcomes are uncorrected (Minor; multiple comparisons)
**Location:** `paper/paper.qmd:295` (and abstract, `paper.qmd:12`); data `results/correlates-country.csv`
**Observation:** The capability cut is rigorously controlled — an explicitly declared eight-test family with Holm and BH reported, and the derived tau* row removed from the family. The country cut reports five outcomes each with its own raw permutation p (ETI 0.033, tau* 0.050, width-rank 0.059, labor-tax center 0.076, macro-trade center 0.243) and **no** family-wise or FDR correction. The sub-0.05 values (ETI 0.033, tau* 0.050) are the two smallest of five uncorrected tests, and tau* is a monotone transform of ETI (not an independent fifth-of-five signal). Under even a five-test Holm, ETI's 0.033 → 0.165 and nothing would survive — the same fate as the capability cut.

**Failure scenario:** A reader contrasts the two cuts and reasonably infers that the US-vs-China ETI/top-rate gap (the section's most quotable claim, and the one most likely to be lifted into secondary coverage) cleared a bar the capability finding did not — when in fact the country cut was simply never corrected. The "exploratory / directional" labels and the attainable-p-floor disclosure blunt this but do not state the asymmetry.

**Fix:** Add one sentence at `paper.qmd:295` noting the five country outcomes are not multiplicity-corrected (parallel to the eight-test family), and that the ETI/top-rate signals would not survive a five-test Holm/BH either — so the country cut is directional on the same footing as the capability cut, not a stronger result. Optionally emit Holm/BH columns in `correlates-country.csv` for symmetry.

### Finding 3 — "Exhausted the 8k budget on reasoning" is an interpretation of an empty-response error class, not a recorded finish reason (Minor; characterization)
**Location:** `paper/paper.qmd:178`
**Claim:** "`glm-5.2` exhausted an 8,000-token completion budget on reasoning in 109 of its first 390 draws."

**Verified:** The pilot's `failed-runs-archive.jsonl` holds 151 records = **109** with error `"LiteLLM response contained no JSON content"` (empty/no-content responses) + **42** OpenRouter credit-ceiling errors; the pilot `runs.jsonl` is the full 390-draw first pass (239 parsed + 151 failed). So "109 of 390" is genuinely sourced from retained data. The retained request logs show no `finish_reason` field, and the 239 successful pilot requests all completed under ~4,900 total (completion+reasoning) tokens — so the 8k-exhaustion mechanism is *inferred* from the empty-JSON signature plus the fact that the 16k rerun resolved it, not read from a length/truncation flag.

**Failure scenario:** A reproducibility reviewer greps the pilot archive for a budget/length marker, finds only `"no JSON content"` and credit-ceiling strings, and reads the paper's confident "exhausted the 8,000-token completion budget on reasoning" as unsupported — when the mechanism is a reasonable but unstated inference from an empty-content error class on a reasoning model.

**Fix:** Soften to the observed signal, e.g. "returned empty (no-JSON-content) responses consistent with reasoning-token budget exhaustion in 109 of its first 390 draws (the failure class the 16k rerun eliminated)." Same wording applies to the parallel "empty reasoning-exhausted responses" phrasing later in the sentence, which is already appropriately hedged.

---

## Verified vs. not-reached

**Independently verified (computation or direct inspection this round):**
- Holm/BH arithmetic from the raw permutation p-values → smallest Holm 0.135, BH 0.075; "nothing survives correction" true for both (by-hand step-down/step-up, matches `correlates-spearman.csv` to full precision).
- Permutation-p integer reconciliation: 0.016849·20001 = 337 and 0.018749·20001 = 375 (clean integers), consistent with `(hits+1)/(draws+1)`, draws=20,000, seed fixed.
- 25 models (registry-counted: openai 7, anthropic 6, google 4, xai 3, five Chinese labs 1 each); 25·26·15 = **9,750** runs.
- n=22 correlation sample = 25 − 3 (gpt-5.4, grok-4.20, grok-4.1-fast lack PolicyBench), matching the code's `EXPECTED_PANEL_ONLY`.
- tau* is an exact rank-reversal of ETI (Tax −0.5013/+0.5013, Overall −0.5083/+0.5083), confirming the "derived transform, not an additional test" handling.
- rho prose rounding (−0.51, −0.50); LOO-organization range −0.45 (openai) to −0.60 (anthropic) over 9 omissions.
- Country medians/p match CSV↔prose: tau* 32.2 vs 35.6 (p 0.050), ETI 0.495 vs 0.425 (p 0.033), width-rank 16.5 vs 11.2 (p 0.059).
- tau* range 29.8–40.2 = CSV min 29.766 (qwen) / max 40.158 (gemini-3.1-pro).
- Archive total 4,319; net of 151-record pilot = 4,168 (Finding 1).
- GLM-5.2 "109/390" mapped to 109 empty-JSON records + 390-draw pilot `runs.jsonl` (Finding 3).
- Recovery is failure-slot replacement (DNS, credit-ceiling, empty-reasoning), not outcome selection; GLM and kimi had whole panels re-run, not selected cells; the length-truncation channel and the non-reconstructible July per-slot sensitivity are both disclosed. **No undisclosed outcome-selected censoring found.**
- `verify_paper_prose.py`: 50/50 pass, exit 0. Working tree byte-identical, HEAD `fa04669`, `git status` clean.

**NOT reached / NOT independently recomputed (stated per coordinator instruction):**
- The eight Spearman rho values recomputed from the 22 raw rows of `correlates-model-summary.csv` (I verified internal consistency, sign-flip, and prose rounding — not a from-scratch rho).
- The country permutation p-values via independent exact C(25,5)=53,130 enumeration (read from CSV; prose↔CSV match only).
- The organization-block permutation hit count / p=0.164 (I verified the 1,440 = 2!·6! reference-set size, not the hit count).
- The attainable-p floor "0.02–0.05" for groups of 5 vs 20.
- Benchmark in-range counts (Frisch 25/25; 24/25 for cap-gains, wage, single-mother; 21/25 income; 22/25 ETI) against `support-bounds.csv` — these sit largely outside the new section and were not re-derived this round.
- kimi-k2.6 "published cell entirely from the final pass" at the record level (only confirmed a 1,470-record archive consistent with full re-elicitation).
- An exhaustive "every new sentence has a pin" audit beyond the 50 checks the verifier enforces.

---

## VERDICT: Minor Revision

**Justification.** The new statistics are sound: the Spearman/permutation/Holm/BH pipeline is correctly implemented, the derived-transform bookkeeping is right, "nothing survives correction" is stated plainly and is true, and the confound disclosure for the country cut is thorough and appears in the abstract, body, and artifact. The recovery disclosure withstands scrutiny — the two load-bearing figures (109/390 and 4,168) both reconcile against retained archives, and the censoring is infrastructure-failure replacement with the one outcome-correlated channel disclosed. Nothing here reopens what rounds 1–3 settled, and no finding falsifies a reported number or a conclusion.

The three findings are genuine but minor and mechanical: a reproducibility-wording fix so the 4,168 count survives a naive `find` (Finding 1), a one-sentence acknowledgment that the country cut is uncorrected while the capability cut is Holm/BH-controlled (Finding 2), and a softening of "exhausted the 8k budget" to match the empty-response evidence actually retained (Finding 3). All three are edits to `paper.qmd` prose plus, optionally, symmetry columns in `correlates-country.csv`; none requires re-elicitation or reanalysis. I recommend acceptance once these are addressed.
