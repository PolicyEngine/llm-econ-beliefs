# Referee 4 Report — Reproducibility & Research-Software Review (Round 4)
**Manuscript:** LLM-elicited beliefs about economic elasticities (25-model panel)
**Repository HEAD at review:** `fa04669` · **Scope:** the reproducibility extension (model registry, grid gates, correlates pipeline, runner hardening, correlates section)

## Summary

The reproducibility extension is, on the whole, **exemplary research software**. I replayed the full offline pipeline — `build_correlates.py` then `build_tables.py` — and the working tree returned **byte-identical to HEAD**, the Pareto tail reproduced exactly (`a = 1.6208594549947215`), 139 tests passed, and all 50 prose checks passed. The single-source-of-truth design is real and enforced: `model_registry.py` hard-asserts the 25-model roster (count, unique IDs, unique labels, canonical org/serving-path/wave sets) and emits `results/model-registry.csv`, which both the Python analysis pipeline and the Next.js dashboard consume. The PolicyBench-panel crosswalk and complete-grid gating are pinned and registry-driven, so a stray 26th results directory cannot leak into outputs. The one-way DAG holds: `top-rate-calibration.json` depends only on PolicyEngine microdata, and no file transitively depends on itself. The glm-8k pilot archive and the 4,168 archived recovery records are inert — the only code path that touches `failed-runs-archive.jsonl` is the writer.

My findings are **all Minor**. None touches the correctness or determinism of the analysis code. The two that matter for RSOS/Zenodo readiness are documentation/metadata, not science: (1) the README's cached-results reproduction recipe omits `scripts/build_correlates.py`, so following it verbatim does not regenerate the new correlates layer; and (2) `CITATION.cff` still describes the retired 17-model / 6,630-run panel, which would propagate into the archived DOI record.

## Findings (most severe first)

### F1 — README cached-results recipe cannot regenerate the round-4 correlates layer · Minor
**Where:** `README.md:184-193` ("### (a) From cached results").
**What:** The round-4 paper adds a correlates-and-country section. Its tables (`paper/tables/correlates-*.csv`, `policybench-correlates.csv`) are rebuilt by `build_tables.py` **from** `results/correlates-*.csv`, and those `results/` artifacts are regenerated **only** by `scripts/build_correlates.py`. The README's reproduction section never mentions `build_correlates.py`; it lists only `pytest` and `build_tables.py`. Because `build_tables.py` degrades silently when the correlates artifacts are absent or column-stale (`build_correlates_tables` returns `[],[],""` at `paper/build_tables.py:1425,1430-1431`; `build_country_table` returns `[]` at `1400`), a newcomer starting from anything other than the committed artifacts would get a paper with the correlates tables quietly dropped, not an error. The committed `results/correlates-*.csv` currently mask this.
**Fix:** In section (a), insert `.venv/bin/python scripts/build_correlates.py` **before** the `build_tables.py` step, and add `.venv/bin/python scripts/verify_paper_prose.py` as the prose-consistency gate. Consider stating the canonical order explicitly: `build_tables` (writes calibration JSON) -> `build_correlates` (writes correlates CSVs) -> `build_tables` (reformats into `paper/tables/`).

### F2 — CITATION.cff still describes the retired 17-model / 6,630-run panel · Minor
**Where:** `CITATION.cff:19-20` (abstract; also `date-released:` at line ~11).
**What:** The abstract reads "6,630-run dataset ... 17 frontier large language models." The current panel is 25 models x 26 quantities x 15 runs = **9,750 main-panel runs**, as used consistently in `paper/paper.qmd` (8x "25 models", 2x "9,750"), the README, and the enforced registry. `CITATION.cff` is the one tracked, non-review file still carrying the old figures. Zenodo/RSOS ingest this file for the archived citation of record, so the drift would ship into the DOI metadata. `date-released: 2026-07-07` also predates the 25-model extension (commit `4172ec8`).
**Fix:** Update the abstract to "25 frontier large language models" and the correct run count (9,750 main-panel; state separately if the 6,630 was meant as some other total). Bump `date-released` on deposit. This is exactly the kind of hand-maintained roster prose the registry was built to eliminate — consider generating the count from `PANEL_MODEL_IDS` where feasible.

### F3 — Fallback path silently overwrites the committed calibration JSON and blocks build_correlates · Minor
**Where:** `README.md:194-201` (fallback note) interacting with `paper/build_tables.py:166-167` and `scripts/build_correlates.py:415-419`.
**What:** The README says that without `POLICYENGINE_US_REPO`, `build_tables.py` "falls back to `a = 1.5` for those two tables only." In fact `write_top_rate_calibration(...)` runs unconditionally (`build_tables.py:167`), so the fallback also **overwrites** `results/top-rate-calibration.json` with `a = 1.5`, dirtying the committed artifact (`1.6208... -> 1.5`). `build_correlates.load_top_rate_calibration` then hard-rejects `a = 1.5` (`build_correlates.py:415-419`), so a reproducer who runs the documented no-microdata path and then runs `build_correlates` hits a hard error. The blast radius is wider than "those two tables only." It fails loudly (no silent corruption), which is why this stays Minor.
**Fix:** Preferred — have `build_tables.py` write the calibration JSON only when the microdata calibration actually succeeds (or write the fallback to a side path), leaving the committed `a = 1.6208...` intact. Alternative — expand the README note to state that the fallback rewrites `results/top-rate-calibration.json` and therefore blocks `build_correlates.py` until a real calibration is restored.

### F4 — Org/wave display labels duplicated by hand in dashboard TypeScript · Minor (cosmetic drift)
**Where:** `dashboard/src/lib/site-data.ts:28-45` (`ORGANIZATION_LABELS`, `WAVE_LABELS`) duplicate `llm_econ_beliefs/model_registry.py:275-299` (`ORGANIZATION_DISPLAY_LABELS`, `WAVE_DISPLAY_LABELS`).
**What:** The values match the Python registry exactly today. `site-data.ts:99` throws on an unknown org/wave **key**, so *additions* to the registry fail the dashboard build loudly — good. But a **value** change (e.g. "Zhipu AI" -> "Zhipu" in Python) would leave the dashboard showing the stale label with no test to catch it. The model-level fields (id, display label, organization, family, wave) correctly flow through `results/model-registry.csv` and are **not** duplicated; only these two lookup maps are re-encoded. The dashboard is gitignored-staged and deployed separately, so this does not affect the paper's archived reproducibility.
**Fix (optional):** Emit the org/wave display labels from the Python registry into `results/model-registry.csv` (or a sibling CSV) and have the dashboard read them, or add a build-time test asserting the two maps equal the registry. Low priority.

### F5 — Dashboard methods prose hardcodes the roster size · Nit
**Where:** `dashboard/src/app/methods/page.tsx:43-46` ("25 models from nine organizations — Anthropic, OpenAI, ..., and MiniMax").
**What:** A manual sync point (the models page uses a computed `${modelCount}`; the methods page enumerates by hand). The team already fixed stale 17-model copy here in commit `6ba3f33`, so this is maintained manually. Auxiliary-app prose, not a paper-repro issue. Lowest priority.

### Stale README "Repo Layout" (documentation nit, non-blocking)
`README.md:26-40` lists a `llm_econ_beliefs/` tree that omits `model_registry.py`, `experiment.py`, `providers.py`, `pricing.py`, `provider_tags.py`, `compare.py`, `mappings.py`, and shows `paper/` as README-only (no `build_tables.py`) and no `scripts/`, `results/`, `dashboard/`. Cosmetic; worth a refresh alongside F1.

## Four-command results (mandated)

| # | Command | Result | Tree after |
|---|---------|--------|------------|
| a | `.venv/bin/python scripts/build_correlates.py` | **PASS** — exit 0, ~6.7 s; crosswalk + gate emitted, "Wrote 25 model summaries", n=22 capability correlations | — |
| b | `cd paper && POLICYENGINE_US_REPO=... PYTHONPATH=.. ../.venv/bin/python build_tables.py` | **PASS** — exit 0 (~3-4 min microdata calibration); "Wrote tables to .../paper/tables" | — |
| — | `git status --porcelain` after (a)+(b) | **CLEAN** — empty; deterministic regeneration confirmed, `a = 1.6208594549947215` reproduced exactly; **no `git checkout -- .` needed** | byte-identical |
| c | `.venv/bin/python -m pytest -q` | **PASS** — 139 passed in 2.47 s | clean |
| d | `.venv/bin/python scripts/verify_paper_prose.py` | **PASS** — exit 0, 50 ok / 0 FAIL, "all prose checks passed" | clean |

**Final tree state:** `git status --porcelain` empty; HEAD `fa04669` unchanged; no untracked non-ignored files. The four scripts were the only executions; no provider/network elicitation was made; no files were written outside `/tmp`.

## Verified vs. not-reached

**Verified on the page:**
- Deterministic full-pipeline replay -> byte-identical tree; exact `a` reproduction; 139 tests; 50 prose checks.
- Registry as single source of truth — `model_registry.py:306-347` `_validate_registry()` (count=25, unique IDs, unique labels, canonical org/serving-path/wave sets); `results/model-registry.csv` matches the dataclass row-for-row; dashboard reads the CSV (`next.config.ts:11-29`, `site-data.ts:71-114`).
- Crosswalk assertions — `validate_policybench_crosswalk` (`build_correlates.py:306-368`) pins EXPECTED_PANEL_ONLY = {gpt-5.4, grok-4.20, grok-4.1-fast}, EXPECTED_POLICYBENCH_ONLY = {grok-build-0.1}, single `source_release`, `condition=no_tools`, `country=us`; n=22 is internally consistent with the 23-row scores file and the verifier's `n_models=="22"` assertions.
- Gated inclusion — `panel_grid_gate.gate_panel_models` iterates `PANEL_MODEL_IDS`; `build_correlates.pool_model_runs` reads `{model_id}-elasticities-batch15/runs.jsonl` (`:249`) rather than globbing; the nested `results/glm-5.2-8k-pilot-archive/elasticities-batch15/` matches no registry id and no path construction -> cannot leak.
- One-way DAG / no cycle — microdata -> `top-rate-calibration.json` (build_tables) -> `correlates-*.csv` (build_correlates) -> `paper/tables/*.csv` (build_tables reformat, graceful if absent) -> prose; `top-rate-calibration.json` depends only on microdata; `build_tables` never reads `correlates-*` as an analytic input (only reformats them).
- Archive inertness — only writer reference is `rerun_failed_runs.py:129`; 4,319 archived records total minus 151 in the pilot archive = **4,168** recovery records elsewhere, matching the stated figure; nothing imports them.
- README cost caveat — `paper.qmd:203` states "`$29.25` at the OpenRouter account level ... appear as em dashes in every cost column rather than as zeros"; README rounds to "~$29" (`:209`). `OPENROUTER_API_KEY` is documented (`README.md:212`); `--models` validates against the registry (`README.md:257-258`, `run_v4_new_models.py`).
- Data-availability statement (`paper.qmd:481`) is accurate: all code, raw run-level responses, request logs, generated tables, and rebuild scripts are present in the repo; DOI archive promised on acceptance (standard RSOS pattern). No paper-referenced artifact is missing from the repo.

**Not reached / out of scope by instruction:**
- `paper/paper.pdf` byte-consistency with the current `paper.qmd` — **NOT VERIFIED** (re-rendering was explicitly excluded; I graded `.qmd` + tables + verifier, which are mutually consistent).
- Dashboard `next build` — **NOT RUN** (no provider/network; auxiliary app, outside the offline reproduction chain).
- Full from-absolute-scratch bootstrap (all derived files deleted) — reasoned about, not executed; relevant to F1/F3.

## VERDICT: **Minor Revision**

The extension is the strongest part of this manuscript on my axis — the determinism, registry enforcement, crosswalk/gate pinning, and archive inertness are all genuinely well-built, and the mandated reproduction succeeded end-to-end with a clean tree. I am not recommending Accept only because two items squarely in the reproducibility/software remit should be fixed **before the Zenodo deposit and camera-ready**: the README's cached-results recipe cannot currently regenerate the new correlates layer it introduced (F1), and the archival metadata still describes the retired 17-model panel (F2). Both are small, mechanical edits; F3 is a one-line guard worth adding; F4-F5 are optional hardening. None blocks the scientific claims, and I would be glad to clear this to Accept on a revision that addresses F1 and F2.
