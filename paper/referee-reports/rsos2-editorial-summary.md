# Editorial summary — Royal Society Open Science simulated round 2

**Date:** 2026-07-07. **Panel:** rsos2-referee1 (statistics), rsos2-referee2 (public finance), rsos2-referee3 (LLM methods), rsos2-referee4 (reproducibility), rsos2-referee5 (round adjudication). Reviewed revision: commit e17d305 ("Revision round 1", PR #6), diffed against the round-1 state.

## Editorial decision: Minor revision (4 minor, 1 borderline major)

Verdicts: referee 1 **major (borderline)**; referees 2, 3, 4 **minor**; referee 5 **minor (borderline major)**. The adjudicator's regenerate-not-relabel audit passes cleanly — zero relabel-only fixes; seven of eight round-1 critical findings were resolved by genuine regeneration, independently reproduced (a = 1.621 top-rate spot checks to the decimal, bimodality counts against raw runs.jsonl, full 58-slot manifest trace). Every remaining defect is a mechanical prose-vs-table reconciliation.

## Consolidated must-fix list

1. **Ranking superlatives desynchronized from the regenerated Tables 1–2** (referees 1, 4, 5 — the one recurring round-1 item). Abstract macro-trade top pair; labor-tax highest/lowest trios; macro-trade top trio; labor-tax tightest trio; macro-trade widest trio. July models (Grok 4.3, GPT-5.5, Gemini 3.5 Flash, Claude Fable 5) now occupy named slots.
2. **Stray `a = 1.470`** in the A13 description (referees 1, 2, 4, 5) — everywhere else reads 1.621.
3. **Sign miscount introduced by the round-1 fix** (referees 2, 5): "negative for 14 of 17" conflates the sign count (16 of 17) with the in-band count (14 of 17).
4. **Stability-table note** hard-codes "9-quantity" while reporting 221 = 13×17 cells (referees 1, 4, 5).
5. **Statutory-anchor footnote**: $626k is the 2025 single threshold mislabeled MFJ; 2026 anchors are $640,600 single / $768,700 MFJ (referee 2).
6. **A16 gpt-5.5 budget** should read 1200 with 8000 for the 40 re-elicited runs; the "unchanged settings" sentence is wrong for the two partially replaced gpt-5.5 cells (referee 3).
7. **A17 overstates width stability** ("similarly stable" vs ±15%) and does not scope out the reasoning-mode axis (referee 3).
8. Smaller items: LOO bound 0.970→0.982; "roughly halved"→~40%; A14 scope sentence; A15 median-vs-max note; archive-phrasing honesty (July predates archiving); mean-vs-median reconciling sentence; residual estimand language; rerun-script and providers docstrings; README reproduction section still 11-model/$25–30; LICENSE + CITATION.cff absent; orphan model-overview table.

## Resolution of round-1 criticals (adjudicator)

7/8 resolved by genuine regeneration (C5, C7, C8 clean; C1, C2, C4, C6 with the minor residuals above), C3 partial (the superlatives), 0 unaddressed, 0 relabel-only.

## Disposition

All eight items plus the smaller list were applied in revision round 2, with a committed machine-verification script (`scripts/verify_paper_prose.py`) asserting every superlative and headline number against the regenerated tables so this class of drift fails a check rather than a referee.
