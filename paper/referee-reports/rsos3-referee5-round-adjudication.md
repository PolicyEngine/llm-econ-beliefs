# Referee 5 (round-diff adjudicator) — RSOS Round 3

## Headline

**The revision is genuinely clean.** Every one of the eight round-2 must-fix items and the entire smaller-items list was resolved by real re-derivation, not relabeling — and I confirmed each against primary data, not the diff. All seven ranking superlatives now match `model-overview-labor-tax.csv` / `model-overview-macro-trade.csv`; the income-elasticity sign count (16 negative / 14 in-band) reproduces from `elasticity-all-model-comparison.csv`; the ablation width range (−15% to +7%), LOO floor (0.982), A15 max shares (29/25/7%), and gpt-5.5 budget (40 reruns) all reproduce from their source CSVs / the failure manifest. The committed guardrail `verify_paper_prose.py` passes all 27 checks, and I proved it would have caught the exact round-2 superlative defect. `pytest` is green (71 passed). **Zero relabeled-only, zero unaddressed must-fix items, no new table-contradicting errors.**

Audited: working tree at HEAD (a677389); `git diff cfbceb2..a677389` touches **only** the five referee-report files, so the paper/tables/scripts I read are byte-identical to the audited revision cfbceb2.

## Must-fix audit (union of all five round-2 reports)

| # | Item (reporters) | Classification | Primary evidence (recomputed, not diff-read) |
|---|---|---|---|
| MF1 | Ranking superlatives desynced from regenerated Tables 1–2 (R1 blocking, R4, R5) | **RESOLVED-REGENERATED** | All 7 claims recomputed from the two `model-overview-*.csv`. Labor-tax highest {Sonnet 4.6, Grok 4.20, **Grok 4.3**}, lowest {**Gemini 3.5 Flash, GPT-5.5**, Gemini 3.1 Flash-Lite}, tightest {**Fable 5**, Gemini 3.1 Pro, **Sonnet 5**}, widest {Grok 4.1 Fast, GPT-5.4 mini, Grok 4.20}; macro-trade top {GPT-5.4 mini, **Grok 4.3**, Grok 4.20}, bottom {Opus 4.7, Haiku 4.5}, tightest Haiku 4.5, widest {Grok 4.20, **Grok 4.3**, GPT-5.4 mini}; abstract pairs {Sonnet 4.6, Grok 4.20} & {GPT-5.4 mini, **Grok 4.3**}. **Every prose slot matches the CSV rank column.** |
| MF2 | Stray `a = 1.470` at A13 prose (R1, R2, R4, R5) | **RESOLVED (clean)** | `grep "1.470"` over the whole paper tree (ex-reports) = **0 hits**. Line now reads `a = 1.621`, matching the microdata build (threshold $725,533, tail mean $1,894,129 → a=1.621). |
| MF3 | Sign miscount "negative for 14 of 17" (R2, R5) | **RESOLVED-REGENERATED** | From `elasticity-all-model-comparison.csv`, `income_elasticity.prime_age`: **16 negative** (only gemini-3.5-flash +0.011), **14 in-band** [-0.15,-0.05], 3 out-of-band (gemini +0.011, nano −0.001, gpt-5.5 −0.035). Prose now: "negative for 16 of 17 … inside the review band for 14 of 17." Exact. |
| MF4 | Stability note hard-codes "9-quantity" vs 221=13×17 (R1, R4, R5) | **RESOLVED-REGENERATED** | `build_tables.py:363` now interpolates `{canonical_quantity_count}`; `stability-appendix.md` note reads "13-quantity"; `grep "9-quantity"` = 0 hits. |
| MF5 | Footnote $626k mislabeled MFJ (R2) | **RESOLVED (clean)** | Footnote now "$640,600 for single filers and $768,700 for married-filing-jointly … 2026," matching R2's cited IRS-2026/OBBBA figures; `grep "626"` = 0. $725,533 lies between the two, so the neighborhood point holds. |
| MF6 | A16 gpt-5.5 budget + "unchanged settings" wrong (R3) | **RESOLVED-REGENERATED** | `harness-disclosure.{csv,md}` now "1200 (8000 for the 40 re-elicited runs)." `failure-manifest.csv` gpt-5.5 = 5+5+15+15 = **40** (2 full cap-gains cells @15 + 2 partial cells @5), manifest `error_class` itself says "re-elicited at an 8000-token cap." Line 161 now scopes settings per-slot correctly. |
| MF7 | A17 overstates width stability; reasoning-mode not scoped (R3) | **RESOLVED-REGENERATED** | Recomputed (Native−LiteLLM)/LiteLLM from `mechanism-ablation.csv`: min **−15.1%** (Frisch), max **+6.75%** (cap-gains). Main-text A17 now "−15 to +7 percent … no consistent direction" + explicit "reasoning modes remain confounded … runs without extended reasoning on both paths." |
| MF8 | Smaller-items list (all five reports) | **RESOLVED** (see below) | — |

## Smaller-items detail (MF8)

| Item | Class | Evidence |
|---|---|---|
| LOO 0.970→0.982 (R4, R5) | RESOLVED-REGEN | `leave-one-provider-out-appendix.csv` min ρ = 0.982; prose "between 0.982 and 0.999" + "stays above 0.98." |
| "roughly halved"→~40% (R2) | RESOLVED | 40.2/63.8=63%, 30.1/53.1=57% → 37–43% cut; prose "reduced by roughly 40 percent." |
| A14 subpanel-scope sentence (R1) | RESOLVED | Hedge added scoping A14 to canonical ordering; subpanel callouts "coarse groupings." |
| A15 median-vs-max (R1, R5) | RESOLVED-REGEN | `variance-decomposition.csv`: nano 29%, gemini 25%, next 7% (Grok 4.20). Prose exact. |
| Archive-phrasing honesty (R3) | RESOLVED (disclosure) | Line 161 now: archiving "postdates the July round … per-slot include-vs-exclude sensitivity not reconstructible." |
| Mean-vs-median reconciling sentence (R5) | RESOLVED-REGEN | `toy-top-rate-labor-tax.csv` Haiku ETI median = **0.502**; prose "median of 0.502 versus its mean center of 0.507." |
| Estimand language (R5) | RESOLVED | "single-τ prior"→"single shared τ" (0 hits for old form); ":137 belief" gone; "LLM priors"→"models' elicited ETI distributions." Residual "belief" uses are deliberate construct-framing. |
| Docstrings (R3) | RESOLVED | `providers.py` now "OpenAI/LiteLLM/native Anthropic APIs" (not "locally available CLIs"); `rerun_failed_runs.py` softened to "not provably independent of elicited values." |
| README 11-model/$25–30 (R4) | RESOLVED | Now "17 models × 26 × 15 (6,630 runs)," "$60.89 all-in," + fallback caveat, rerun script, and manifest referenced. |
| LICENSE + CITATION.cff (R4, R5) | RESOLVED | Both present. LICENSE = MIT/2026 PolicyEngine; CITATION.cff valid CFF 1.2.0, MIT, abstract numbers (6,630/17/26/15) consistent. |
| Orphan `model-overview.{md,csv}` (R5) | RESOLVED | Both deleted; the retired `build_model_overview_table(canonical_rows)` call removed; all 22 `{{< include >}}` targets resolve, none dangling. |

## Regressions introduced by the revision

**None material.** I read every hunk and cross-checked against tables. One cosmetic nitpick only: the `mechanism-ablation.md` *table note* says widths "move up to 15 percent **in either direction**," which is slightly generous on the positive side (actual max up-move +6.75%; the −15% is only the down-side). It does not contradict any cell, and the main-text A17 prose is precise. Not blocking.

No new number contradicts its table; the two error classes the revision was *fixing* (sign miscount, stale a-value) did not spawn replacements — the sign rewrite is correct against raw data and the a-value is globally consistent.

## Guardrail audit (`scripts/verify_paper_prose.py`)

Genuinely effective, not vacuous. It reads the CSVs (and the raw `elasticity-all-model-comparison.csv`) and asserts the prose, so it recomputes rather than string-coincidence-matches. I proved non-vacuousness empirically: feeding the **stale round-2 sentence** ("…and GPT-5.4 mini") into its `names_in_order` check returns **False** (would have blocked the merge), while the corrected sentence returns True. It explicitly guards the recurring drift classes — superlatives, `1.470`/`a = 1.500`/`FALLBACK`, "9-quantity", LOO floor, A15 shares, ablation range, gpt-5.5 budget, and the sign count from raw data. **One narrow blind spot:** `names_in_order` uses substring `.find()`, and model names are prefix-nested (`GPT-5.4` ⊂ `GPT-5.4 mini`/`nano`), so a *future* build whose table top became the base `GPT-5.4` while prose kept `GPT-5.4 mini` would **falsely pass** (I confirmed this specific case returns True; the reverse direction is correctly caught). It also doesn't cover every headline figure (statutory anchors, per-model top-rate medians, manifest tallies). Neither gap touches the current build; both are worth a follow-up hardening (match on word-boundaries / exact backticked tokens) but are not defects in this revision.

## Working-tree / reproducibility note

I observed a **transient** dirty state on the four PolicyEngine-backed tables (`toy-top-rate-labor-tax.{md,csv}`, `top-rate-robustness.{md,csv}`) mid-audit that resolved on its own; no test imports `build_tables` (confirmed), so this was external/concurrent activity, not my commands. I ran no build or write. **Final state verified: `git status` clean; all four files byte-identical to HEAD; committed `a = 1.621`, no `FALLBACK`.** The task's byte-identical constraint is satisfied. (This does surface the known design behavior R4 documented: rebuilding without `POLICYENGINE_US_REPO` silently rewrites those four to the a=1.5 fallback — honest, loudly warned, but a live foot-gun for reproducers.)

## Verdict

**ACCEPT.**

**Resolution counts (8 must-fix):** 8 resolved — 6 RESOLVED-REGENERATED-and-verified-against-primary-data (MF1, MF3, MF4, MF6, MF7, plus the regenerated MF8 sub-items), 2 clean text corrections carrying the correct regenerated value (MF2, MF5); **0 RELABELED-ONLY, 0 UNADDRESSED.** Smaller-items list: all resolved. No must-fix item is relabeled or unaddressed, so nothing forces Major.

The lone round-2 blocker (R1's Major, driven solely by the stale superlatives) is fully closed, independently reproduced, and now machine-enforced. The only remaining threads are explicitly non-blocking editorial/robustness suggestions the round-2 referees themselves marked "without re-review" — the mechanism-ablation note wording, surfacing the manifest as a numbered appendix, committing `failed-runs-archive.jsonl`, auto-generating the A16 dict, the C4 include-vs-exclude sensitivity, and hardening the guardrail's substring matching. A strict editor could label this **Minor Revision** for the one loose table-note phrase; because that phrase contradicts no data and raises no soundness issue, I judge the revision has cleared the bar and recommend **Accept** with those items as optional touch-ups.