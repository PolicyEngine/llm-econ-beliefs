# Referee 3 (LLM evaluation methodologist) — RSOS round-3 re-review (soundness)

## Recommendation: **Accept**

## Summary

My round-2 report (Minor Revision) listed six residuals. This round I independently re-verified every one against the provider code, the committed request logs, and the failure manifest — not against the authors' narrative — and then ran a fresh regression pass over `git diff e17d305..cfbceb2` in my lane (harness disclosure, structured-output mechanism, protocol confounds). **All six residuals are resolved and verifiable on the page.** The failure trail is fully auditable (58/58 replacement IDs resolve to the correct cell and quantity; the original budget-exhaustion signatures are retained in the committed logs). `pytest` passes (71). The harness table remains fully consistent with `providers.py`. I found no regressions in my lane. The only new items are one minor wording imprecision and a few cosmetic/optional notes — none soundness-relevant and none changing a reported number. The tree was left clean.

---

## Per-residual verification (with evidence)

### 1. A16 gpt-5.5 budget cell + the "40" — VERIFIED, cross-checks against the manifest

`paper/tables/harness-disclosure.md:5` (and `.csv`) now reads the completion budget as **`1200 (8000 for the 40 re-elicited runs)`**. The hardcoded source (`paper/build_tables.py:1938`) was edited from `"8000"` to that string.

- The **40** cross-checks exactly against `results/failure-manifest.csv`: the four gpt-5.5 rows sum to 5 + 5 + 15 + 15 = **40**.
- The split is real in code: `OPENAI_MAX_COMPLETION_TOKENS_BY_MODEL = {"gpt-5.5": 8000}` (`providers.py:46-48`) with a 1200 default (`build_openai_chat_payload`, `providers.py:391`); the rerun path (`scripts/rerun_failed_runs.py:62`) calls `run_openai_prompt_batch_logged` with no explicit budget, so it falls back to 8000.
- I confirmed the split in the **committed logs**: the 40 rerun IDs show `completion_tokens` up to **2857** (impossible under a 1200 cap), while the 15 original cap-gains draws are 3 batch-of-5 calls with `reasoning_tokens == completion_tokens` at ~930–1146/choice (all reasoning, zero output) — the exact "budget exhausted at the 1200-token cap" signature the manifest states. `verify_paper_prose.py`'s table-derived check ("gpt-5.5 budget discloses 1200 base") passes.

### 2. Main-text replacement paragraph — "unchanged settings" corrected AND archive phrasing made honest — VERIFIED

`paper/paper.qmd:161` now ends:
> "All other affected cells replaced at most 5 of 15 runs — under identical settings for the `claude-sonnet-5` and `grok-4.3` slots, and at the same raised 8,000-token budget for the two partially affected `gpt-5.5` cells."

This removes the round-2 "unchanged settings" mischaracterization. The manifest confirms exactly **two partial gpt-5.5 cells** (`labor_supply.income_elasticity.prime_age`, `…substitution_elasticity.secondary`, 5 each) versus **two full cap-gains cells** (15 each) — matching the paper's "capital-gains cells failed in full … partially affected cells" split precisely.

Archive honesty — the same sentence now carries:
> "(this archiving postdates the July round, whose audit trail is the manifest plus the retained request logs; because the July replacement happened in place, a per-slot include-versus-exclude sensitivity is not reconstructible for that round)."

Verified end-to-end: `scripts/rerun_failed_runs.py:100-108` does write `failed-runs-archive.jsonl` going forward, but **no such archive is committed** anywhere in `results/` (confirmed by `find`), and the original failed draws **are** retained in `requests.jsonl`. The new phrasing exactly describes the actual state and proactively discloses the include-vs-exclude limitation I raised. This resolves the round-2 overstatement.

### 3. A17 width quantification + reasoning-mode scope-out — VERIFIED by recomputation

`paper/paper.qmd:431` now reads:
> "Pooled centers move by at most `0.03` (median `0.00`); pooled widths move more, from `-15` to `+7` percent across the nine quantities with no consistent direction … width comparisons across waves carry the extra mechanism noise. The ablation isolates the output mechanism and completion budget only — `Claude Opus 4.7` runs without extended reasoning on both paths, so the July models' always-on or adaptive reasoning modes remain confounded with model identity."

I recomputed `(Native − LiteLLM)/LiteLLM` from `paper/tables/mechanism-ablation.csv`: range **−15.10% (Frisch) to +6.75% (cap-gains)** → rounds to **−15 to +7 percent**; signs are mixed (4 up, 4 down, 1 zero) = "no consistent direction." The verify script's table-derived check ("ablation width range prose") passes. The reasoning-mode confound is now explicitly scoped out, and the center-inference is narrowed to "cross-wave differences **in centers**." Both parts of the round-2 residual are addressed.

### 4. `scripts/rerun_failed_runs.py` docstring — VERIFIED

The module docstring (`:1-13`) no longer claims replacement "does not select on elicited values." It now reads: "The replacement policy conditions only on failure status, but truncation-type failures correlate with response length, so replacement is not provably independent of elicited values; see results/failure-manifest.csv and the paper's harness-disclosure appendix." Correct.

### 5. `llm_econ_beliefs/providers.py` docstring — VERIFIED

The module docstring (`:1-6`) no longer says "locally available CLIs." It now reads "Provider adapters: OpenAI Chat Completions, LiteLLM, and native Anthropic APIs. Each adapter … returns raw text plus a request log (request ID, token usage, cost inputs) for the audit trail." Accurate for the three panel paths. (Minor optional note below re: a now-undocumented dead CLI helper.)

### 6. OpenAI-only system message — DISCLOSED; string matches the payload — VERIFIED (one minor wording caveat)

`paper/paper.qmd:147` (A16 paragraph) now discloses it:
> "the OpenAI path wraps the elicitation prompt with a one-line system message ("Follow the user's instructions exactly and return only the final answer."), while the Anthropic and LiteLLM paths send the prompt as a bare user message; the instruction is format-only and appears verbatim in every logged OpenAI request."

- **String match:** `providers.py:405-406` contains exactly `"Follow the user's instructions exactly and return only the final answer."` — verbatim.
- **"bare user message" for the other paths:** confirmed — `run_anthropic_prompt_logged` (`:166`) and `run_litellm_prompt_logged` (`:268`) both send `messages=[{"role": "user", "content": prompt}]` with no system role.
- **"every OpenAI request":** confirmed — all four GPT models and the 40 gpt-5.5 reruns route through `run_openai_prompt_batch_logged` → `build_openai_chat_payload`, which adds the system message unconditionally; the Responses API path (`build_openai_response_payload`, no system message) was **not** used for any panel run (no `openai_responses` provider tag in any committed log; `tool_regime` is `none` for all 118 gpt-5.5 rows).

Caveat is new finding A below.

---

## Fresh methods pass — new findings

**A. (Minor / wording) A16's "appears verbatim in every logged OpenAI request" slightly overstates what the committed logs show.** The committed `requests.jsonl` entries store only usage/cost metadata — `RequestLog` (`llm_econ_beliefs/models.py:162-188`) has no `prompt`, `messages`, or payload field — and the system string appears in **no** committed artifact (`grep -rl` over `results/` returns nothing; the only logs are metadata-only `requests.jsonl` and output-only `runs.jsonl`). The claim is fully supported by the committed **code** (`providers.py:405-406`, added unconditionally) and the verbatim string is printed in the paper itself, so it is independently checkable — just not from the "logs." The wording is defensible (every request that was logged did contain the instruction), but "logged" invites a reader to look in `requests.jsonl` and not find it. This exactly parallels the archive-phrasing class the authors already corrected in item 2. Suggested one-clause fix: attribute the string to the request **payload** / `providers.py` and note that committed request logs record usage metadata only. Not soundness-blocking; changes no result.

**B. (Trivial / data hygiene) Provider-tag inconsistency on the gpt-5.5 reruns.** The 40 gpt-5.5 rerun rows are tagged `provider: "openai"` while all other OpenAI panel rows are `"openai_chat_completions"` (`results/gpt-5.5-elasticities-batch15/requests.jsonl`), even though both go through the identical Chat Completions builder. A reader filtering logs by `provider == "openai_chat_completions"` would silently drop the 40 reruns. Cosmetic provenance labeling from `rerun_failed_runs.py`; no paper claim is affected.

**C. (Trivial / optional) `mechanism-ablation.md` table note is looser than the main text.** The note (`paper/tables/mechanism-ablation.md:1`) says "widths move up to 15 percent in either direction," but the positive side maxes at +6.75%; the main-text A17 is precise (−15 to +7). A defensible magnitude reading exists ("movements, in either direction, up to 15%"), so this is optional polish only.

**D. (Reproducibility, disclosed — primarily Referee 4's lane; flagged because I surfaced it via permitted tooling)** `scripts/verify_paper_prose.py` is sensitive to a transient a = 1.5 **fallback** state of Table 4. On my first run it reported 5 spurious top-rate FAILs carrying a = 1.5 numbers (e.g., Gemini 3.1 Pro 43.2%, spread 10.4, revenue-max 55.0–65.5%); on re-run against the committed a = 1.621 tables **all checks pass and the script exits 0**. I confirmed the committed prose and tables are internally consistent at a = 1.621 (`toy-top-rate-labor-tax.csv`: GPT-5.4 nano 30.1% … Gemini 3.1 Pro 40.2%, spread 10.1; matches `paper.qmd`), and the fallback is disclosed in the Table-4 footnote ("falls back to a = 1.5 and prints a warning; every number in this section comes from the microdata build committed with the paper"). So **the committed manuscript is not desynced** — the earlier failure reflected a momentary rebuild without PolicyEngine microdata, now reverted (tree clean, files identical to HEAD). Note the script correctly returns 1 on real failure (`verify_paper_prose.py:293`); the "EXIT: 0" I first observed was `tail`'s code through a pipe, not the script's. Optionally the committed-artifact build could hard-fail rather than silently fall back, but nothing here needs to change for soundness.

**Regression sweep result:** none in my lane. The harness table's mechanism/budget/sampling/reasoning/identifier columns all reconcile with `providers.py` (`OPENAI_/LITELLM_MAX_COMPLETION_TOKENS_BY_MODEL`, `ANTHROPIC_MAX_OUTPUT_TOKENS = 32000`, `_litellm_output_mode`, the alias maps; native Claude sends no sampling parameter; reasoning always-on/adaptive/off per `providers.py:148-151`). The deletion of the `model-overview` table leaves no dangling `{{< include >}}`. The a = 1.470 → 1.621 edit in the CRRA-robustness section is a genuine internal-consistency **fix** (it now matches the Table-4 baseline). The added A14/A15 caveats (subpanel top-three coarseness; max single-cell between-run shares of 29%/25%) are honest disclosures that strengthen the draft.

Residual carryover, non-blocking: the A16 table is still a hardcoded dict in `build_tables.py` (currently consistent, could silently desync); an unused `run_claude_prompt` CLI adapter (`providers.py:356-381`) survives in the module and is no longer described by the docstring — optional dead-code cleanup.

---

## Verdict: **Accept**

Every soundness-relevant concern from my round-1 Major Revision was cleared in round 2, and all six round-2 residuals are now resolved and independently verified this round against the code, the committed request logs, and the manifest — not merely against the authors' description. The re-elicitation trail is fully auditable: 58/58 replacement request IDs resolve exactly once to the correct directory and quantity, the 1200/8000 gpt-5.5 budget split is confirmed from token usage, and the original budget-exhaustion signatures are retained. The harness disclosure (A16), the cross-mechanism ablation with its now-quantified width movement and explicit reasoning-mode scope-out (A17), and the honest failure/archive accounting all match the underlying artifacts. The remaining items (A–D) are minor wording or cosmetic data-hygiene points that change no reported number and no soundness conclusion; the single genuine wording imprecision (A16 "logged") is a take-it-or-leave-it copy edit that does not warrant another review round. The manuscript clears the RSOS soundness bar in my area.

**Relevant files:** `/Users/maxghenis/llm-econ-beliefs/paper/paper.qmd` (lines 147, 161, 431); `/Users/maxghenis/llm-econ-beliefs/paper/tables/harness-disclosure.{md,csv}`; `/Users/maxghenis/llm-econ-beliefs/paper/tables/mechanism-ablation.{md,csv}`; `/Users/maxghenis/llm-econ-beliefs/paper/tables/toy-top-rate-labor-tax.csv`; `/Users/maxghenis/llm-econ-beliefs/results/failure-manifest.csv`; `/Users/maxghenis/llm-econ-beliefs/results/gpt-5.5-elasticities-batch15/requests.jsonl`; `/Users/maxghenis/llm-econ-beliefs/llm_econ_beliefs/providers.py` (lines 1-6, 46-48, 137-166, 248-268, 384-423, 488-513); `/Users/maxghenis/llm-econ-beliefs/llm_econ_beliefs/models.py` (lines 162-188); `/Users/maxghenis/llm-econ-beliefs/scripts/rerun_failed_runs.py` (lines 1-13, 62, 100-108); `/Users/maxghenis/llm-econ-beliefs/scripts/verify_paper_prose.py` (lines 125-165, 291-295); `/Users/maxghenis/llm-econ-beliefs/paper/build_tables.py` (lines 1938, 442-448).