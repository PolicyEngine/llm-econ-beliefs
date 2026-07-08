# Referee 4 — Reproducibility & research-software review, ROUND 3 (Royal Society Open Science)

**Recommendation: Accept**

**3-sentence summary.** All five items I asked the authors to fix in round 2 are now resolved and independently verified against the committed artifacts: every ranking superlative in the abstract and body matches a fresh top/bottom-3 recomputation from `model-overview-labor-tax.csv` and `model-overview-macro-trade.csv` (in both `paper.qmd` and the rendered `paper.html`), the stray `a = 1.470` is gone (now `1.621` everywhere, zero occurrences of the old value), the stability note is correctly interpolated as "13-quantity," the README reproduction section describes the 17-model/6,630-run panel with the $60.89 two-wave cost and the PolicyEngine env vars, and both an OSI (MIT) `LICENSE` and a schema-valid `CITATION.cff` now exist. The new `scripts/verify_paper_prose.py` passes all 27 checks, and I confirmed by read-only sensitivity test that it would actually catch each round-1/round-2 failure mode (stale superlative, stale `a`-value, wrong note label). The table build is reproducible — running `build_tables.py` without PolicyEngine access changes only the 4 microdata-backed files with a loud fallback warning, the committed tables are the genuine `a = 1.621` microdata build, and the retired `model-overview.{md,csv}` orphan was removed cleanly with no dangling include, test, or build reference.

---

## Per-item re-audit (all five RESOLVED)

### 1. Stale ranking superlatives (my round-2 top priority) — RESOLVED
I recomputed top/bottom-3 by both rank columns from the two CSVs (Python `sorted`, stable-tie semantics matching the paper's own script) and checked every named model in `paper.qmd` **and** the rendered `paper.html`:

| Site (paper.qmd) | Claim | Recomputed from CSV | Verdict |
|---|---|---|---|
| Abstract L12 — labor pair | Claude Sonnet 4.6, Grok 4.20 | abs-rank #1–2: 4.92, 5.75 | Match (was "GPT-5.4 mini/nano") |
| Abstract L12 — macro pair | GPT-5.4 mini, Grok 4.3 | abs-rank #1–2: 4.33, 4.5 | Match |
| L194 highest-3 | Claude Sonnet 4.6, Grok 4.20, Grok 4.3 | 4.92, 5.75, 7.33 | Match |
| L194 lowest-3 | Gemini 3.5 Flash, GPT-5.5, Gemini 3.1 Flash-Lite | 14.67, 13.17, 10.42 | Match |
| L196 low-response-side | same three | — | Match |
| L202 macro top-3 | GPT-5.4 mini, Grok 4.3, Grok 4.20 | 4.33, 4.5, 4.67 | Match |
| L202 macro bottom-2 | Claude Opus 4.7, Claude Haiku 4.5 | 14.5, 13.5 | Match |
| L204 labor tightest-3 | Claude Fable 5, Gemini 3.1 Pro, Claude Sonnet 5 | width-rank 4.83, 5.5, 6.17 | Match |
| L204 labor widest-3 | Grok 4.1 Fast, GPT-5.4 mini, Grok 4.20 | 15.17, 14.5, 13.67 | Match |
| L204 macro tightest | Claude Haiku 4.5 | width-rank 2.0 | Match |
| L204 macro widest-3 | Grok 4.20, Grok 4.3, GPT-5.4 mini | 16.0, 15.67, 14.5 | Match |

Rendered `paper.html` confirms the same strings (abstract opens "Claude Sonnet 4.6…"; body highest-elasticity trio and macro top/bottom render correctly). Every one of the six round-2 stale sites is now correct. The authors also added the recompute-from-data guard (item below) so these cannot silently go stale again.

### 2. Stray `a = 1.470` at the A13 paragraph — RESOLVED
`paper.qmd:395` now reads "replace the microdata-calibrated `$a = 1.621$`". Repo-wide, `1.470` appears **0** times in `paper.qmd` and **0** times in `paper.html`; all a-values are `1.621` (9 occurrences in the HTML). No `1.500`/`FALLBACK` strings anywhere in the prose or committed tables.

### 3. `stability-appendix.md` note label — RESOLVED and correctly interpolated
The committed note reads "Prefix stability on the **13-quantity** canonical subpanel." At source, `paper/build_tables.py:365` builds it as `f"Prefix stability on the {canonical_quantity_count}-quantity canonical subpanel. "`, where `canonical_quantity_count` is computed at line 207 (`len({row.quantity_id for row in canonical_rows})`). The same variable now feeds four other notes (lines 374, 390, 410) — the hard-coded `9-quantity` literal from round 2 is gone (`paper.html`: 0 "9-quantity", 8 "13-quantity"). This is the correct, drift-proof fix.

### 4. README reproduction section — RESOLVED (all five sub-requirements)
`README.md` §"Reproducing the v4 panel":
- **17-model / 6,630-run panel** — L205–206 "17 models × 26 quantities × 15 runs (6,630 main-panel runs)".
- **~$60.89 two-wave cost** — L207–209 "the 11-model April wave (~$23), and the 6-model July wave (~$38 …; $60.89 all-in across both waves)".
- **`POLICYENGINE_US_REPO` / `POLICYENGINE_US_PYTHON`** — L195–200, including the honest caveat that without them the build "prints a loud warning and falls back to `a = 1.5` for those two tables only" (this also fixes the round-2 "rebuild all tables" overclaim).
- **`results/failure-manifest.csv`** — L213–214.
- **`scripts/rerun_failed_runs.py`** — L210–212.

### 5. LICENSE and CITATION.cff — RESOLVED
- `LICENSE` = **MIT** (OSI-approved) — the "public" repo is now genuinely reusable, resolving the round-2 all-rights-reserved gap.
- `CITATION.cff` — parses, and **`cffconvert --validate` (via uvx) reports "Citation metadata are valid according to schema version 1.2.0."** Fields are sane: `cff-version: 1.2.0`, one author (Ghenis, PolicyEngine), `license: MIT`, `date-released: "2026-07-07"`, `repository-code: https://github.com/PolicyEngine/llm-econ-beliefs` (correct org/repo), abstract accurately says "6,630-run dataset … 17 frontier large language models … 26 economic elasticities."

---

## Audit of the new `scripts/verify_paper_prose.py`

- **27/27 checks pass** (`.venv/bin/python scripts/verify_paper_prose.py`, exit 0). Breakdown: 8 superlative, 6 top-rate, 3 stability, 2 LOO, 3 variance-decomp, 2 ablation, 1 harness, 2 income-sign.
- **Would it catch the round-1/round-2 failure modes? Yes** — I confirmed by a read-only sensitivity test (no files written):
  - **Stale superlative:** `verify_superlatives` recomputes each trio from the CSVs and asserts `names_in_order`/membership in the actual paper sentence. Feeding it the exact round-2 rendered bug ("GPT-5.4 mini and GPT-5.4 nano moving to the top") fails, because the correct name "Grok 4.3" is absent; wrong-order fails; a removed anchor phrase (empty `sentence_with` result) fails. This is a genuine data-derived invariant — the strongest guard here.
  - **Stale `a`-value:** `verify_top_rate` extracts `a` from the table note and asserts `"$a = 1.621$" in PAPER and "1.470" not in PAPER and "a = 1.500" not in PAPER` — a direct regression block on the two known-bad strings.
  - **Wrong note label:** `verify_stability` asserts `"13-quantity canonical subpanel" in note and "9-quantity" not in note`.

**Two honest caveats on the tool (non-blocking — it is a supporting script, not the paper):**
1. The `a`-value and `9-quantity` guards are *known-bad-string blocklists*, not general invariants — they'd miss a *novel* stale value (e.g. `a = 1.55`, or an `11-quantity` label). The superlative and numeric-range checks, by contrast, are recomputed from data and are fully general. Since the note label is now interpolated from `canonical_quantity_count`, the blocklist is belt-and-suspenders there anyway.
2. `names_in_order` uses substring `str.find`, so a bare `"GPT-5.4"` would spuriously match inside `"GPT-5.4 mini"`. No live bug (no checked trio pairs bare `GPT-5.4` with a `GPT-5.4 …` variant in the current roster), but it is a latent fragility if the model set changes.

Neither caveat affects the current paper; both are optional hardening suggestions.

---

## Reproducibility verification

- **Test suite:** `.venv/bin/python -m pytest -q` → **71 passed in 2.07s.**
- **Table build without PolicyEngine env vars** (`POLICYENGINE_US_REPO`/`_PYTHON` both unset): `build_tables.py` exits 0 and changes **only the 4 microdata-backed files** — `toy-top-rate-labor-tax.{md,csv}` and `top-rate-robustness.{md,csv}`; the other 30 tables regenerate byte-identically. The build emits a loud stderr warning: *"WARNING: PolicyEngine microdata Pareto calibration FAILED — Table 4/A13 will use the FALLBACK a = 1.5, not the microdata calibration described in the paper text."* The regenerated note self-labels "using the FALLBACK Pareto parameter a = 1.500 because the PolicyEngine microdata calibration was unavailable at build time." I restored with `git checkout -- paper/tables`; **tree clean.**
  - *Factual note (not a defect):* on the env-**unset** path I observed **one** warning at build time, whereas my round-2 report (which forced fallback via `POLICYENGINE_US_REPO=/nonexistent`) saw two. Here the build located a default policyengine-us checkout, invoked it, and it raised a real computation-mode error (`self_employment_income mixes … adds/subtracts and uprating`), which the fallback caught. Both triggers — missing repo and present-but-erroring repo — degrade loudly and honestly to `a = 1.5`. The disclosure requirement is met.
- **Committed tables are the microdata build:** `toy-top-rate-labor-tax.md` and `top-rate-robustness.md` contain `a = 1.621` and **0** `FALLBACK` strings.

## Diff review `e17d305..cfbceb2` — nothing broken in my lane
- **`paper/tables/model-overview.{md,csv}` deleted** (the round-2 orphan flagged by Referee 5). Removal is clean: `build_tables.py` no longer writes a bare `model-overview` stem (only `-labor-tax`, `-macro-trade`, `-simulation`), so a rebuild does **not** resurrect the files; all **22** `{{< include >}}` shortcodes in `paper.qmd` resolve to existing files; **no** test references `model-overview`. The only remaining bare-`model-overview` mentions are inside `paper/referee-reports/*.md` (archived review documents), which are not build inputs.
- **Code diffs are docstring/honesty-only, non-regressive:** `providers.py` (expanded module docstring); `scripts/rerun_failed_runs.py` (docstring now *concedes* truncation-type failures correlate with response length so replacement "is not provably independent of elicited values" — a scientific-honesty improvement responsive to the methods referee); `build_tables.py` (orphan block removed; `9-quantity`→interpolated; ablation-note and gpt-5.5 budget "1200 (8000 for the 40 re-elicited runs)" detail added, matching the verify checks).

---

## New findings

One optional, forward-looking observation (severity: **trivial / non-blocking**):

- `paper/build_tables.py:221,229` still hard-code the **subpanel quantity counts** ("6 quantities", "3 quantities") while interpolating `{panel_model_count}`. They are correct today (labor-and-tax = 6, macro-and-trade = 3, summing to the "nine-elasticity subset"), and subpanel composition drifts far less often than the model roster that caused the original bug — but for full consistency with the now-interpolated canonical count, these two could also be computed from `len({row.quantity_id …})` per subpanel. Grading what is on the page: correct. This is a hardening suggestion for a future edit, not a revision condition.

No new correctness, data, or reproducibility defects.

---

## Verdict: **Accept**

Every item from my round-2 Minor Revision is resolved and independently verified against the committed artifacts, in both source and rendered output. The dataset (6,630 runs), the failure manifest, the derived tables, and all headline numbers are reproducible; the microdata-vs-fallback path is honest and loud; the ranking prose is now recomputed-and-guarded so it cannot silently desync; the paper carries an OSI license and a schema-valid citation file; the test suite is green (71/71); the new verification harness passes all 27 checks and demonstrably catches the historical failure modes; and the orphan-table removal left the build, includes, and tests clean. The single remaining observation is a trivial forward-looking consistency nit on two hard-coded subpanel counts that are correct as rendered. Nothing outstanding rises to Minor Revision. The working tree is byte-identical to session start (`git status` clean, HEAD `a677389`, no untracked files); no provider APIs were called and no files were written.