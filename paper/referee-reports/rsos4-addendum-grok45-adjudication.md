# Adjudication addendum: Grok 4.5 panel addition (25 -> 26 models)

*Post-round-4 spot-check of the Grok 4.5 integration (PR #20), same round-diff charter as rsos4-referee5. Read-only, primary-data-first. Fixes applied in PR #21.*

## Headline

The integration is overwhelmingly regenerated-from-data, not asserted: every quantitative claim the charter flagged — rankings, benchmark counts, correlates, A4/A9/A14, the exact-permutation path, cost, and the archived-slot disclosure — recomputes correctly from `paper/tables/*.csv` and `results/*.csv`. But three surviving 25-model-era prose claims slipped through, all of the exact A9 class that bit in round 4, all missed by the verifier. Two of them (the labor-tax "high-response" trio and the Armington rerun count) contradict tables the same commit regenerated. None touches a substantive result. Verdict: **Minor Revision** (resolved by PR #21).

Necessary checks: pytest 140 passed; verify_paper_prose 71 checks all pass (at time of audit) — necessary, not sufficient.

## STALE — surviving 25-model-era claims the verifier did not pin

**S1 — A1 paragraph "325 cells"** -> 338 (13 x 26). The table `stability-appendix.csv` regenerated correctly to 338; the verifier pinned the table value and the prose medians but not the prose cell count.

**S2 — Table 1 discussion high-response trio** still read "Claude Sonnet 4.6, Grok 4.20, Qwen 3.7 Max" — exactly the pre-addition top three — while the line above and the abstract were updated to include Grok 4.5 (the #2 model and the subject of the round). No verifier check existed for this illustrative trio.

**S3 — A7 prose "Across all 25 model reruns"** -> 26 (`armington-clarify-delta.csv` includes Grok 4.5's rerun, delta -0.033). The verifier pinned the increases list but not the count.

**Pre-existing fossil (reconciled in the same fix):** "an 11-model follow-up on the Armington elasticity" described A7 by its April size; A7 has covered the full panel since the 25-model extension -> "a 26-model follow-up."

## VERIFIED-FROM-DATA (recomputed from primary data)

| Claim | Paper | Source | Result |
|---|---|---|---|
| Total runs | 10,140 | 26x26x15 | OK |
| Labor-tax top-3 / bottom-3 | Sonnet 4.6, Grok 4.5, Grok 4.20 / Gemini 3.5 Flash, GPT-5.5, MiniMax M3 | model-overview-labor-tax.csv | OK |
| Macro top-3 / bottom | Grok 4.3, Grok 4.20, GPT-5.6 Luna / Opus 4.7, Haiku 4.5 | model-overview-macro-trade.csv | OK |
| Benchmark in-range | 26/26, 25/26 x3, 22/26, 23/26 | benchmark-comparison-labor-tax.csv | OK |
| Capability | rho -0.5056/-0.4964 -> -0.51/-0.50, raw p 0.0144/0.0175, n=23, Holm 0.116, BH 0.070 | correlates-spearman.csv | OK |
| LOO rho range | -0.45 to -0.59 (openai -0.4500, anthropic -0.5858) | correlates-sensitivity.csv | OK |
| Country | 21 vs 5; 35.9172/32.2348 p 0.02332; ETI 0.42/0.4949 p 0.019474; width 11.6154/16.9231 p 0.070325; Holm min 0.0779 | correlates-country.csv | OK |
| A2 | max rank spread 3.92 MiniMax M3 | pooling-robustness-appendix.csv | OK |
| A3 | LOO Spearman floor 0.991-1.0 | leave-one-provider-out-appendix.csv | OK |
| A4 | 4.23 MiniMax M3; 9 of 26 < 1 rank | quantile-rule-appendix.csv | OK |
| A9 | 25/26 sign-consistent; GPT-5.4 nano both-neg; Gemini 3.5 Flash 65% uninformative; 24 informative; 16 ordinary / 8 LTCG | cap-gains-convention-audit.csv | OK |
| A14 | panel-median center SE 0.007 (0.00745); width 1-8% | resampling-stability.csv | OK |
| Stability table | 338 cells | stability-appendix.csv | OK (prose was stale — S1) |
| Registry | 26 models; grok-4.5 wave july_2026_late | model-registry.csv | OK |
| A16 aliases | 25/26 floating, only claude-haiku-4.5 dated; grok-4.5 @8000 | harness-disclosure.csv | OK |
| "seven US models" | 3 native Claude (32k) + 3 GPT-5.6 (8k) + Grok 4.5 (8k) | harness-disclosure.csv | OK |
| Exact path | max_exact=70000 >= C(26,5)=65,780; non-vacuous (old 60,000 < 65,780) | build_correlates.py | OK |
| Grok 4.5 archive | 1 line | grok-4.5-elasticities-batch15/failed-runs-archive.jsonl | OK |
| Grok 4.5 cost | $2.7139 -> $2.71; 23.15+37.74+2.71 = 63.60 | requests.csv (2.4864+0.1187+0.1088) | OK |
| Waves | registry july_2026_late; paper "fourth July wave" (July count); dashboard "five waves" (total incl. April) — different denominators, not contradictory | — | OK |
| Dashboard | 26 models, 10,140 runs, late Grok 4.5, no stale counts | dashboard/src/app/*.tsx | OK |

Note on "seven US models": correct count (the raised-budget, provider-default-reasoning set); the adjacent "(8,000-16,000 tokens)" bracket describes the Chinese models' range while three US members sit at 32k — loose framing, not a defect.

## Resolution (PR #21)

All three stale strings fixed, the 11-model fossil reconciled, and three matching verifier pins added (A1 prose cell count derived from the registry; high-response trio pinned to the labor-tax overview top three; A7 rerun count pinned to the delta table's row count): 71 -> 74 checks. The structural gap named here — free-text panel-size restatements outside the pinned set — is the same one that produced round 4's A9 finding; the added pins close the three known instances.

## Verdict: Minor Revision — resolved

- VERIFIED-FROM-DATA: 22 claim-groups (all substantive numbers).
- STALE: 3 prose restatements + 1 pre-existing fossil (all fixed and pinned in PR #21).
- UNVERIFIABLE: 0. No result, table, or figure was wrong.
