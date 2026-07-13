# Referee 2 report (public-finance economics) — Round 4

**Manuscript:** LLM-elicited beliefs about economic elasticities (25-model panel)
**Reviewer focus:** economic substance of the 25-model extension — the tau* top-tax mechanics, the capability-ETI and US-vs-China correlates, benchmark in-range counts, and cross-section framing consistency. HEAD `fa04669`.

## Summary

This is a strong, unusually careful descriptive paper, and the extension from 17 to 25 models is executed with the same discipline that earned the prior Accept. I verified the load-bearing economics of the new claims from the committed CSVs and calibration JSON, and the headline machinery is exact:

- **tau* mechanics reconcile to the digit.** With `a = 1.62086` and `gbar = 0.61845` from `results/top-rate-calibration.json`, the inverse-elasticity map tau* = 0.382/(0.382 + 1.621 e) reproduces every Table 4 row I spot-checked (Qwen e=0.555 -> 29.8%, GPT-5.4 e=0.420 -> 35.9%, Gemini 3.1 Pro e~=0.3505 -> 40.2%). The revenue-maximizing column 1/(1+ae) reproduces 52.6% (Qwen) to 63.8% (Gemini 3.1 Pro). The headline range "29.8% to 40.2%" and "52.6-63.8%" match `toy-top-rate-labor-tax.csv` exactly.
- **The US-vs-China medians reconcile exactly** to Table 5's per-model ETI/top-rate columns: US 35.6%/0.425/width-rank 11.2 (n=20), China 32.2%/0.495/16.5 (n=5), and the deltas/p-values match `correlates-country.csv`.
- **The PolicyBench correlates are honest.** rho = -0.51/-0.50, raw p ~= 0.017/0.019, Holm 0.135, BH 0.075, family=8 all match `correlates-spearman.csv`; the "nothing survives Holm" claim appears faithfully in both the abstract and the section. No laundering into the Interpretation/Limitations sections (the correlates are not re-asserted as established there).
- **Benchmark in-range counts all match Table 3** (Frisch 25/25, cap-gains/wage/single-mother 24/25, income 21/25, ETI 22/25).
- **The US-vs-China comparison does not editorialize.** The language is mechanical throughout ("imply lower optimal top rates," "higher elicited taxable-income elasticities"), the three confounds (n=5 non-independent labs, serving-path/wave, English-only) are stated in the abstract, section, and per-row `disclosure` field, and gemini-3.5-flash's bimodality is correctly disclosed as mode-mixing rather than a stated belief. A hostile reader could still *gloss* "higher ETI -> lower top rate" as "Chinese models are more conservative on taxation," but that inference would be the reader's; the paper never makes it. See Finding 3 for the one place the country cut is presented slightly more favorably than its rigor warrants.

The problems I found are all correctable **staleness and framing** items concentrated in the appendix and the correlates framing sentence — numbers that were computed on the 17-model panel and not refreshed when the five Chinese-lab models (and Qwen 3.7 Max, the new panel-maximum ETI) joined. One of them directly contradicts the abstract. None overturns a conclusion, but the contradiction must be fixed. Verdict: **Minor Revision.**

---

## Findings (most severe first)

### Finding 1 — Capital-gains audit prose carries stale 17-model counts that contradict the abstract and Table A9 (Moderate)

**Location:** `paper/paper.qmd:400` (Appendix Table A9 discussion); contradicts abstract at `paper.qmd:12` and the table `paper/tables/cap-gains-convention-audit.csv`.

The appendix text reads: *"Sixteen of seventeen models are sign-consistent... The substantive finding concerns the remaining fifteen: eleven cluster in the ordinary-income-rate window and four in the LTCG window."* Every count is the old 17-model number. Recounting the 25-row table `cap-gains-convention-audit.csv`:

- Sign-consistent: **24 of 25** (GPT-5.4 nano is the lone "both negative" exception) — this is exactly what the **abstract** already says ("24 of 25 models return a negative w.r.t.-tax-rate elasticity paired with a positive w.r.t.-net-of-tax-rate elasticity").
- Informative (excluding GPT-5.4 nano and the pole-straddling Gemini 3.5 Flash at 65%): **23**, split **15 ordinary-income-rate** vs **8 LTCG** (I enumerated both lists from the `Band` column).

**Failure scenario:** A referee or editor reads "24 of 25" in the abstract, turns to the audit appendix, and finds "Sixteen of seventeen" describing the *same* audit of the *same* 25-model panel. This is a flat internal contradiction and reads as a table/text desync — precisely the kind of error that undermines confidence in a paper whose value proposition is reproducible bookkeeping. It also undercounts the paper's own evidence: the true split (15 vs 8) is *stronger* support for "implied tau typically lands nearer the ordinary-income rate" than the stated 11 vs 4.

**Fix:** Replace with "Twenty-four of twenty-five models are sign-consistent... The substantive finding concerns the remaining twenty-three: fifteen cluster in the ordinary-income-rate window and eight in the LTCG window." (Better: derive these counts programmatically in `build_tables.py` so they cannot drift from the table again.)

---

### Finding 2 — Appendix A13 robustness shift ranges have stale lower bounds (Minor)

**Location:** `paper/paper.qmd:269`; table `paper/tables/top-rate-robustness.csv`.

The text states moving *a* to 1.3 "shifts every model's implied top rate up by `7.9` to `8.6` percentage points" and the gamma=2 switch "raises every model's top rate by `8.3` to `9.1` percentage points." The *upper* bounds are right (Gemini 3.1 Pro: 40.2->48.8 = +8.6; 40.2->49.3 = +9.1), but the *lower* bounds are set by the highest-ETI model, which is now **Qwen 3.7 Max** (ETI 0.555), not gpt-5.4-nano. From the table's own Qwen row: a=1.3 gives 29.8->37.6 = **+7.8** (text says 7.9); gamma=2 gives 29.8->38.0 = **+8.2** at displayed precision (text says 8.3; full-precision 8.26 is borderline). These are the 17-model bounds (nano at 0.546 gave +7.9/+8.3); Qwen's higher ETI extends them downward. The a=1.7 range ("1.6 to 1.9") is correct.

**Failure scenario:** A reader subtracts the Qwen row in Table A13 (37.6 - 29.8 = 7.8) and finds it falls below the text's stated "7.9" floor, implying "every model" is wrong at the boundary.

**Fix:** Recompute the min shift from the current 25-model table (a=1.3 floor -> 7.8) and, like Finding 1, source these ranges from the table so they refresh automatically. The ordering-invariance claim is unaffected and remains true.

---

### Finding 3 — Correlates framing claims family-wise correction for both cuts, but the country cut receives none; abstract caveats the two cuts asymmetrically (Minor)

**Location:** `paper/paper.qmd:283` (section framing) and `:12` (abstract); tables `policybench-correlates.csv` (family-adjusted, family=8) vs `correlates-country.csv` (5 raw permutation p-values, no Holm/BH).

The section opener says of *both* exploratory cuts: *"I report rank statistics with permutation p-values, adjust for the full test family, and pre-commit to the framing that nothing here is causal."* Family adjustment is genuinely applied to the PolicyBench cut (Table 6 shows Holm/BH over 8 tests, and the abstract correctly says the association is "not surviving Holm correction"). But the **country cut receives no multiplicity correction at all** — Table 7 reports five raw permutation p-values (top-rate 0.050, ETI 0.033, width 0.059, |center|-labor 0.076, |center|-macro 0.243). If those five outcomes were Holm-corrected the way the sibling cut is, none would survive (smallest 0.033 x 5 = 0.165). The abstract, correspondingly, reports the country result as bare "p = 0.050" with confound caveats but *without* the "does not survive correction" language it attaches to the PolicyBench claim.

This is the one place the "no result-laundering between sections" check bites: two sibling exploratory cuts, one held to family correction and one not, under a shared sentence that implies uniform treatment. It is *mitigated* — the country rows each carry an "Exploratory" `disclosure` field, the section lists three strong confounds, and the text calls the result "directional" — so this is Minor, not a substantive overclaim.

**Failure scenario:** A reader concludes the US-vs-China ETI/top-rate gaps are "significant at p ~= 0.03-0.05" while the capability association "washes out after correction," when in fact neither survives the paper's own multiplicity standard.

**Fix:** Either (a) scope line 283 — e.g., "For the capability cut I adjust for the full eight-test family; the country contrasts are reported as raw permutation p-values, none of which survives correction across its five outcomes" — or (b) add a Holm/BH column to Table 7 and state the null survival explicitly, mirroring the PolicyBench treatment.

---

### Finding 4 — ETI "just above the band" prose names two of three out-of-band models, omitting the panel maximum (Minor)

**Location:** `paper/paper.qmd:233`; source `results/elasticity-all-model-comparison.csv`, cross-check `benchmark-comparison-labor-tax.csv`.

The text: *"`22 / 25` models fall inside the rough range, with the same two April models (`claude-haiku-4.5` at `0.507`, `gpt-5.4-nano` at `0.552`) just above the review band's upper anchor of `0.5`."* But 22/25 in-band means **three** are out, and all three are above 0.5. The mean ETI centers > 0.5 are: claude-haiku-4.5 (0.507), gpt-5.4-nano (0.552), and **qwen-3.7-max (0.554)** — the latter being the single **highest** ETI center in the entire panel (it is the `0.554` "Model max center" already printed in Table 3). The prose names only the two April (US) models and silently drops the July Chinese-lab model that is the most extreme of the three.

**Failure scenario:** The arithmetic 25 - 22 = 3 does not match the two models named, and the omitted model is the panel maximum — and, awkwardly, a Chinese-lab model, the very group whose "higher ETI" is a headline of the country cut. A skeptical reader could read the selective naming as understating how far the top of the distribution runs, or (less charitably) as trimming the Chinese-lab outlier from the benchmark discussion.

**Fix:** Name all three, e.g., "...three models sit just above the `0.5` anchor — `claude-haiku-4.5` (`0.507`), `gpt-5.4-nano` (`0.552`), and `qwen-3.7-max` (`0.554`, the panel maximum)." This also aligns the prose with Table 3's `Model max center = 0.554`.

---

## Verified vs not-reached

**Verified against the committed CSVs / JSON:**
- tau* formula, `a`/`gbar` from `top-rate-calibration.json`, headline range 29.8-40.2%, revenue-max 52.6-63.8% (Table 4). Exact.
- US-vs-China medians, deltas, and permutation p-values (Tables 5, 7). Exact.
- PolicyBench rho/raw-p/Holm/BH, family size 8, derived-transform rows, "nothing survives Holm" consistency across abstract + section (Table 6).
- All six benchmark in-range counts (Table 3), and the three ETI out-of-band models.
- Leave-one-org-out rho range -0.45 to -0.60 across nine omissions (pre-fixed item) — consistent with `correlates-sensitivity.csv` (-0.4518 openai to -0.6029 anthropic).
- Org-block permutation stability, 22/25 leaderboard join, 20 US / 5 China / 9 orgs headcounts.
- A13 baseline column matches Table 4; a=1.7 range and ordering-invariance hold.
- No editorializing on US-vs-China; gemini-3.5-flash bimodality correctly framed.

**Not reached / not independently verified (per read-only, no-provider, finalize-now constraints):**
- Did **not** re-run `build_tables.py` or pytest to regenerate tables from raw runs; I compared committed CSVs to prose only.
- Did **not** independently re-derive the Pareto `a = 1.6209` from PolicyEngine microdata; took `top-rate-calibration.json` as given (it matches the paper's `a = 1.621`).
- Did **not** audit A16 harness-disclosure or A17 mechanism-ablation numbers (outside public-finance scope; A16 GLM budget was a pre-fixed item).
- Did **not** check citation attribution for Saez 2001 / Diamond 1998 / Gruber-Saez 2002 (formulas are standard and correctly stated as written).

---

## Verdict: **Minor Revision**

The economics of the extension are sound and, where load-bearing, verified to the digit: the tau* mechanics, the US-vs-China reconciliation, the capability-correlate statistics, and the benchmark counts all match their tables, and the exploratory framing is appropriately hedged in the abstract and kept out of the conclusions. The paper earns its prior Accept on substance.

It falls short of Accept only because the 17->25 refresh left correctable errors on the page — most importantly a stale capital-gains audit count (Finding 1, "16/17") that directly contradicts the abstract's "24 of 25," plus two stale-panel numeric bounds (Findings 2, 4) and one framing asymmetry between the two correlate cuts (Finding 3). None threatens a headline conclusion; all four are mechanical fixes, and three would be permanently prevented by sourcing the counts/ranges from the tables in `build_tables.py` rather than hand-writing them. Fix these and I recommend acceptance without a further round.
