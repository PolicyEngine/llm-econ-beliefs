# Referee 5 (round-diff adjudicator) — Round 4 adjudication

*Reviews HEAD `fa04669`: the 25-model extension (PR #15) plus the round-4a fix set (PR #17).*

## HEADLINE

The round-4a fix set is **real, not renamed** — all five findings are corrected on the page and backed by regenerated data, and both previously-identified verifier gaps are genuinely closed (the harness-budget guard now runs at `build_tables.py` import over *every* canonical model, and the capability LOO is pinned). The 25-model extension regenerated its tables and updated the abstract, headline, and correlates prose correctly. **However, the extension introduced exactly one silent regression that the verifier does not catch: the Appendix A9 (capital-gains convention audit) summary paragraph is still written for the 17-model panel.** It reads "Sixteen of seventeen models are sign-consistent... the remaining fifteen: eleven [ordinary-income] and four [LTCG]," while the regenerated A9 table holds 25 models (24 sign-consistent; 15 ordinary-income and 8 LTCG among 23 informative). This directly **contradicts the paper's own abstract** ("24 of 25 models return a negative w.r.t.-tax-rate elasticity paired with a positive w.r.t.-net-of-tax-rate elasticity"). One isolated, mechanically-fixable stale paragraph; no data or method error. **Verdict: Minor Revision.**

Baseline checks: `pytest -q` -> 139 passed. `scripts/verify_paper_prose.py` -> 50/50 checks pass. Both are necessary-not-sufficient; the defect below lives in prose the verifier never reads.

---

## PER-ITEM AUDIT

### Part A — The five round-4a fixes

**A16 — GLM budget contradiction -> VERIFIED-FROM-DATA.**
- `paper/tables/harness-disclosure.csv` GLM-5.2 completion budget = `16000`; `llm_econ_beliefs/providers.py:61` `"glm-5.2": 16000`. Prose reconciled: `paper.qmd:162` ("`16000` for `glm-5.2`, whose reasoning exhausted an 8,000-token pilot") and `:178` ("single 16,000-token protocol"). The round-3-era 8000/16000 split is gone.
- The build-time guard is real, not cosmetic: `build_tables.py:2157-2191` `_canonical_completion_budget()` resolves each row's budget from `providers.py` and `_validate_harness_budgets()` raises if the disclosed field omits it; **invoked at module import (`:2191`)**. Membership semantics correctly handle gpt-5.5's `"1200 (8000 for the 40 re-elicited runs)"`. Independently confirmed it would fire on GLM drift (canonical 16000 in {16000}).

**A2 — MiniMax/Sonnet tie -> VERIFIED-FROM-DATA.**
- `paper.qmd:340`: "The largest rank spread is `3.77` positions, shared by `MiniMax M3` and `Claude Sonnet 4.6`." `pooling-robustness-appendix.csv`: both rows = 3.77, the joint maximum (next-highest 3.23). Pinned by `verify_rank_spread_tie` (names *every* tied model).

**A14 — 1-9 percent within-paper consistency -> VERIFIED-FROM-DATA.**
- Both mentions now read "`1` to `9` percent": `paper.qmd:110` and `:440`. `resampling-stability.csv` "Median relative width MC SE" spans 1% (min) to 9% (MiniMax M3, max). Pinned by `verify_resampling_range` (asserts exactly 2 occurrences).

**Correlates rho per predictor + abstract -> VERIFIED-FROM-DATA.**
- `paper.qmd:285`: "rho = -0.51 and -0.50"; abstract `:12`: "rho ~= -0.5." `correlates-spearman.csv`: Overall x ETI = -0.5083 (->-0.51), Tax x ETI = -0.5013 (->-0.50), both n=22, raw p 0.0168/0.0187 (~=0.02). Pinned by `verify_correlates`.

**LOO range + softening -> VERIFIED-FROM-DATA.**
- `paper.qmd:285`: "stable in sign under leave-one-organization-out deletion (rho between `-0.45` and `-0.60` across all nine omissions)." `correlates-sensitivity.csv` leave_one_organization_out: 9 rows, max -0.4518 (->-0.45), min -0.6029 (->-0.60). Language softened to "stable in sign," not a strength claim. Pinned by `verify_correlates` (asserts len==9 and the exact range).

### Part B — New correlates/country section vs `results/correlates-*.csv`

All VERIFIED-FROM-DATA (recomputed from primary CSVs):
- Holm min `0.135`, BH min `0.075` — `correlates-spearman.csv` minima 0.13479 / 0.07500. OK
- Capability n=22 (22 of 25 on leaderboard); top-rate row disclosed as derived monotone transform of ETI (`is_derived=True`), not a separate test. OK
- Country top rate: `32.2%` vs `35.6%`, p=0.050, n=5/20 — `correlates-country.csv` 32.2348/35.6217, p 0.0502, china_n 5 / us_n 20. OK
- Country ETI: `0.495` vs `0.425`, p=0.033 — 0.4949/0.4255, p 0.0334. OK
- Country width rank: `16.5` vs `11.2`, p=0.059 — 16.4615/11.1923, p 0.0592. OK
- Confound disclosed on every country row ("perfectly confounded with serving path... and wave; English-language prompts"). OK
- "twenty models from four US organizations against five from Chinese labs" — organization column: OpenAI/Anthropic/Google/xAI = 4 US, Alibaba/DeepSeek/MiniMax/Moonshot/Zhipu = 5 Chinese. OK (correct but unpinned — see gaps).

### Part C — Stale 17-model sweep

**VERIFIED-FROM-DATA (current, recomputed):**
- 25 models / 9,750 runs — consistent throughout (`:10`, `:174`); "25 models" appears 7x; no surviving "17"/"n=17"/"6,630" denominators outside the one below.
- A15 max single-cell shares `37%`/`29%`/`25%` (MiniMax M3 / GPT-5.4 nano / Gemini 3.5 Flash) — `variance-decomposition.csv`. OK (`:448`)
- A3 leave-one-organization-out rho "between `0.99` and `1.0`" — CSV min 0.99, max 1.0. OK (`:348`)
- A4 largest rank change `4.08` (MiniMax M3) and "8 of 25 move by less than one rank" — `quantile-rule-appendix.csv`, recounted |shift|<1 -> exactly 8. OK (`:356`)
- A7 increases list (`+0.013` Fable, `+0.033` Qwen, `+0.167` MiniMax) and largest decreases (`-0.767`/`-0.647`/`-0.433`x2) — `armington-clarify-delta.csv`, exactly 3 positive Changes, decreases match. OK (`:382`)
- Cap-gains **abstract** "24 of 25" sign-consistent — `cap-gains-convention-audit.csv`: 24 "sign-consistent (tax<0, net>0)", sole exception GPT-5.4 nano ("both negative", -0.35/-0.2). OK
- Income-elasticity 24/25 negative (exception gemini-3.5-flash) — pinned by `verify_income_sign_counts`. OK
- tau*/top-rate and revenue-max ranges — pinned by `verify_top_rate` (passed). OK

**STALE (the regression):**
- **`paper.qmd:400` (Appendix A9 body) — STALE.** Four counts are 17-model-era leftovers:
  - "**Sixteen of seventeen** models are sign-consistent" -> data: **24 of 25** (`cap-gains-convention-audit.csv`, 25 rows, 24 sign-consistent).
  - "the **remaining fifteen**" -> data: **23** (25 - GPT-5.4 nano "not identified" - Gemini 3.5 Flash "uninformative/pole-straddling").
  - "**eleven** cluster in the ordinary-income-rate window" -> data: **15**.
  - "**four** in the LTCG window" -> data: **8**.
  - The correct facts inside the paragraph (GPT-5.4 nano = the both-negative exception; Gemini 3.5 Flash = the 65% pole-straddler) survive, which is why it superficially reads fine — but the counts contradict the abstract and the regenerated table. Not pinned anywhere in `verify_paper_prose.py`, so it passed all 50 checks silently.

**UNVERIFIABLE-THIS-ROUND (not recomputed / unpinned; no evidence of staleness, denominators are current):**
- Line 233 benchmark in-range counts (`24/25` cap-gains-realizations/wage/single-mother, `21/25` income, `22/25` ETI) — denominators current (25) and internally consistent, but numerators not recomputed from the elasticity comparison table.
- A14 "median center standard error `0.007` at the panel median" (`:110`) — the committed A14 table carries only per-model aggregates; "at the panel median" is a cell-level quantity not reconstructible from it (median of per-model medians ~= 0.008, a different statistic). Plausible, not verifiable from the committed table.
- Absolute cost figures ($23.15 / $37.74 / $60.89 / $29.25, "310x") — scoping is internally coherent and $23.15+$37.74=$60.89 checks; per-request figures are request-log-derived and out of read-only scope. Not a stale-count risk.

### Part D — Previously-open verifier gaps (from the interrupted first pass)

- "harness budgets spot-checked only for gpt-5.5" -> **CLOSED, verified real.** `verify_paper_prose.py:300-315` now loops over the full `providers.py` canonical map (LiteLLM + OpenAI + Anthropic), asserting each budget is disclosed in A16; plus the `build_tables.py` import-time guard.
- "capability LOO unpinned" -> **CLOSED, verified real.** `verify_correlates` now pins the 9-value leave-one-organization-out rho range against `correlates-sensitivity.csv`.

---

## REGRESSIONS INTRODUCED (by the 25-model extension)

1. **`paper/paper.qmd:400` — stale A9 sign-consistency/band counts** (16/17, 15, 11, 4) contradicting the abstract (24/25) and the regenerated `cap-gains-convention-audit.csv` (24/25; 23 informative; 15/8). Introduced when PR #15 regenerated the A9 table to 25 models but left its summary paragraph untouched. This is the one item the round-diff charter targets — a claim asserted rather than regenerated-from-data.

Required fix (mechanical, recomputable from the committed CSV): "Twenty-four of twenty-five models are sign-consistent"; "the remaining twenty-three: fifteen ... ordinary-income ... and eight ... LTCG."

---

## REMAINING VERIFIER GAPS (future regenerations can still silently break these)

The A9 defect proves the class is live. Unpinned claims a future panel change could desync:
1. **A9 cap-gains sign-consistency count and band split** (`cap-gains-convention-audit.csv`) — no check exists; this is the gap that just bit. **Add a pin** as the revision condition.
2. **A15 "median of `0` to `2` percent" between-run share** (`:309`, `:448`) — `verify_variance_decomposition` pins only the *max* shares, not the median range.
3. **A4 "4.08" and "8 of 25"** (`:356`) — no `quantile-rule-appendix` check.
4. **A7 increases/decreases list** (`:382`) — no `armington-clarify-delta` check.
5. **Line 233 benchmark in-range counts** (24/25, 21/25, 22/25) — unpinned.
6. **A14 "0.007" panel-median center SE** (`:110`) — unpinned and not reconstructible from the committed table.
7. **Country "four US organizations"** (`:295`) — `verify_correlates` pins us_n/china_n but not the organization count.

---

## VERDICT: **Minor Revision**

Counts:
- Round-4a fixes: **5/5 VERIFIED-FROM-DATA** (real, not renamed).
- Prior verifier gaps: **2/2 CLOSED** (confirmed genuine).
- New correlates/country section: **7/7 numeric claims VERIFIED-FROM-DATA**.
- Stale sweep: **9 VERIFIED-FROM-DATA - 1 STALE - ~5 UNVERIFIABLE-THIS-ROUND**.
- Regressions introduced: **1** (A9 stale paragraph, `paper.qmd:400`).
- Remaining verifier gaps: **7** unpinned claim clusters.

Rationale: The science, data, and the entire fix set are sound and regenerated-from-data; rounds 1-3's unanimous Accept is not undermined. But the extension shipped one reader-visible internal contradiction (abstract 24/25 vs appendix 16/17) built from stale counts. That must be corrected before publication, and the correction is mechanical. I condition the revision on (a) rewriting `paper.qmd:400` to the 24/25 - 23 - 15/8 figures, and (b) adding a `verify_paper_prose.py` pin over the A9 sign-consistency and band counts so this exact class of silent break cannot recur — without the pin, the next panel extension will reintroduce it. No re-review of methods required; a diff of the two changes suffices to move to Accept.

*Read-only pass; working tree left byte-identical; no provider/network elicitation; no files written.*
