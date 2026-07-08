# Editorial summary — Royal Society Open Science simulated round 3

**Date:** 2026-07-07. **Panel:** rsos3-referee1 (statistics), rsos3-referee2 (public finance), rsos3-referee3 (LLM methods), rsos3-referee4 (reproducibility), rsos3-referee5 (round adjudication). Reviewed revision: commit cfbceb2 ("Revision round 2", PR #7) at HEAD a677389.

## Editorial decision: Accept (unanimous, 5/5)

Every referee independently re-verified their round-2 items against primary data — recomputed rankings from the model-overview CSVs, sign counts from the raw comparison CSV, budget splits from token usage in the committed request logs, width ranges from the ablation table, the ḡ = a/(a+γ) derivation re-derived analytically, and the 2026 statutory anchors confirmed by indexing consistency — and found all of them genuinely resolved. The adjudicator classified all 8 round-2 must-fix items resolved (6 regenerated-and-verified, 2 clean corrections), with **zero relabeled-only and zero unaddressed**, and proved the new verification harness non-vacuous: the exact stale round-2 sentence fails its superlative check.

## Verdict-by-verdict

- **Referee 1 (statistics), round-2 Major → Accept.** All six ranking superlatives recomputed from the CSVs match in the correct order; every changed quantitative claim in the diff reconciles; no regressions. Harness audit: `names_in_order` genuinely checks rank order and would have caught every round-2 error.
- **Referee 2 (public finance) → Accept.** All four items fixed with the right values; Saez formula, threshold-normalized welfare weight (re-derived), Diamond–Saez column, A13 shifts, benchmark attributions, and the capital-gains audit all verified sound.
- **Referee 3 (LLM methods) → Accept.** All six residuals resolved; 58/58 replacement request IDs trace; the 1200/8000 gpt-5.5 budget split confirmed from token-usage signatures; disclosed system-message string matches the payload byte-for-byte.
- **Referee 4 (reproducibility) → Accept.** All five items resolved; verify script 27/27 with demonstrated sensitivity to historical failure modes; fallback path loud and honest; CITATION.cff schema-valid; orphan-table removal clean.
- **Referee 5 (adjudicator) → Accept.** 8/8 must-fix resolved with primary evidence; smaller-items list fully resolved; no material regressions.

## Optional touch-ups noted (all non-blocking; applied post-decision)

1. `mechanism-ablation.md` note "up to 15 percent in either direction" → quantified as −15 to +7 percent (refs 3, 5).
2. A16 "appears verbatim in every logged OpenAI request" → attributed to the request builder, since committed logs store usage metadata, not payloads (ref 3).
3. Verifier hardening: prefix-nested model names ("GPT-5.4" inside "GPT-5.4 mini") could false-pass a future build; abstract pairs now order-checked (refs 1, 4, 5).
4. Interpolate the hard-coded subpanel quantity counts in the two overview notes (ref 4).
5. Provider-tag consistency for future re-elicitation logs (ref 3; committed logs untouched as the audit trail).

## Outcome

Round history: round 1 unanimous Major → round 2 four Minor + one borderline Major → round 3 **unanimous Accept**. The remaining editorial items above were applied in a post-decision polish commit with the machine-verification suite re-run.
