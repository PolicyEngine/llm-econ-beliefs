# Referee 3 (LLM evaluation methodologist) — RSOS round-2 re-review (soundness)

## Recommendation: Minor Revision

The revision substantively and verifiably addresses all six major concerns from my round-1 report. I independently reproduced the two load-bearing new artifacts from the committed raw data, traced the full failure manifest, and cross-checked the harness disclosure against `providers.py`. Everything I checked was faithful to the underlying data. The residual items are minor accuracy/completeness fixes, none of which changes any reported number.

---

## Verification of round-1 asks

### 1. Per-model harness table (A16) — DONE; matches `providers.py`

I cross-checked every row of `paper/tables/harness-disclosure.md` (and its hardcoded source at `paper/build_tables.py:1947-1963`) against `llm_econ_beliefs/providers.py`:

- Aliases match `POLICYBENCH_LITELLM_MODEL_ALIASES` and `ANTHROPIC_MODEL_ALIASES` exactly (`claude-opus-4-7`, `xai/grok-4.20-reasoning`, `xai/grok-4-1-fast-non-reasoning`, `claude-haiku-4-5-20251001` as the lone dated snapshot, etc.).
- Output mechanisms match `_litellm_output_mode` (gemini → `json_object`, claude/grok → `function_call`), the OpenAI strict-schema payload (`build_openai_chat_payload`, `strict:True`), and the native Anthropic `output_config.format` path.
- Budgets match: `gpt-5.5`=8000, gemini-3.5-flash / grok-4.3 = 4000, native Claude = 32000, else 1200 (`OPENAI_/LITELLM_MAX_COMPLETION_TOKENS_BY_MODEL`, `ANTHROPIC_MAX_OUTPUT_TOKENS`).
- Sampling and reasoning columns match the code (native Claude sends no sampling parameter; reasoning always-on/adaptive/off per the docstring at `providers.py:143-148`).

The paper prose at lines 143-147 is likewise consistent with the code. This resolves round-1 majors 1, 4, and 5 on the disclosure axis.

One caveat (new): the A16 table is a **hardcoded dict** in `build_tables.py`, not derived from `providers.py`, so it can silently desync from the code. It is currently consistent, but a generated-from-config table would be more robust.

### 2. Cross-mechanism ablation (A17) — DONE; reproduces exactly

I recomputed the ablation from `results/claude-opus-4.7-mechanism-ablation-batch15/` (135 runs = 9 canonical × 15, confirmed) versus `results/claude-opus-4.7-elasticities-batch15/`:

- **Centers**: all 9 quantities reproduce the table to 3 decimals. Max |native − LiteLLM| = 0.030 (Frisch), median 0.000 — **exactly** matching the paper's claim at line 137 and 427 ("at most 0.03, median 0.00").
- **Widths**: all 9 reproduce the `summary.csv` pooled bounds exactly.

This is a real, honest bound. Two residuals worth a sentence each:
- The ablation holds reasoning **off on both paths** (Opus 4.7 is a non-reasoning tier), so it does **not** bound the reasoning-mode confound that distinguishes the July models the paper actually highlights — Fable 5 (always-on) and Sonnet 5 (adaptive). The main-text inference "supports reading cross-wave differences as model differences" is sound for the mechanism/budget/sampling axes but does not cover reasoning mode.
- Widths move up to 9-15% (Frisch −15.1%, Marshallian −11.0%, IES −9.3%, cap-gains +6.7%), mixed sign. The appendix phrase "widths are similarly stable" (line 427) is slightly generous; the center claim is the accurate one. Recommend qualifying the width sentence.

### 3. Failure manifest — DONE and fully traceable

`results/failure-manifest.csv` totals 58 (gpt-5.5: 40, claude-sonnet-5: 5, grok-4.3: 13), matching line 161. I verified **all 58 replacement request IDs resolve exactly once** in the correct directory's `requests.jsonl` (0 missing), including the clarify-probe batches. Better still, the **original failed first-attempt requests are retained** in `requests.jsonl`: e.g., the fully-failed gpt-5.5 capital-gains cell shows 3 batch-of-5 originals with completion_tokens ≈ 1074/choice, all reasoning and zero output — the exact budget-exhaustion signature the manifest describes — plus 15 single-draw reruns whose tokens (748, 1231) confirm completion at the 8000 budget. This is a strong, auditable trail and resolves the core of round-1 major 3.

Residuals: (i) the manifest is referenced inline only, not surfaced as an appendix table as I requested; (ii) the `failed-runs-archive.jsonl` that the paper (line 161) and script (`rerun_failed_runs.py:97-105`) say is written is **not committed anywhere in the repo** — the audit trail survives via the manifest + retained requests, but the paper's "archives failed records" phrasing overstates what a reader can retrieve; (iii) no include-vs-exclude-reruns sensitivity was added (moot for the two fully-failed cap-gains cells, but feasible for the two partial cells).

### 4. Softened replacement claim — DONE

Line 161 now states plainly: "truncation-type failures correlate with response length, so replacement is not provably independent of elicited values," and discloses the budget change. This is exactly the conditional softening I asked for. Residual: the `rerun_failed_runs.py` docstring (lines 3-6) still carries the un-softened "does not select on elicited values."

### 5. Alias-vs-snapshot disclosure — DONE

A16's "Identifier type" column plus line 150 ("Sixteen of seventeen identifiers are floating aliases … only `claude-haiku-4.5` pins a dated snapshot … re-elicitation at a later date may hit updated model builds; the elicitation dates above scope every result") squarely addresses round-1 major 2. Only haiku is pinned and no resolution timestamps are recorded, but this is now a disclosed reproducibility limitation rather than a hidden one, which clears the soundness bar.

### 6. `providers.py` matches the paper — YES

Verified in detail (see item 1). Residuals from round-1 that persist: the module docstring at `providers.py:1` still reads "adapters for running prompts against locally available CLIs" (the panel paths are HTTP/SDK), and the OpenAI-only system prompt (`providers.py:400-401`) remains an undisclosed asymmetry not represented in A16.

---

## New soundness issue (genuine, minor)

**gpt-5.5 was elicited at a mix of 1200 and 8000 tokens, and both the A16 table and line 161 mischaracterize this.** The rerun path (`rerun_failed_runs.py:59` → `run_openai_prompt_batch_logged` with no explicit budget) falls back to `OPENAI_MAX_COMPLETION_TOKENS_BY_MODEL["gpt-5.5"]=8000` for **every** gpt-5.5 rerun. From the committed data, 350 of 390 gpt-5.5 runs (90%) were collected at the original 1200 budget; only the 40 reruns used 8000. Two consequences:

- **A16 lists gpt-5.5 budget = "8000"**, which overstates the budget for the bulk of the committed gpt-5.5 data (actually 1200) and, ironically, understates cross-GPT comparability.
- **Line 161 says "All other affected cells replaced at most 5 of 15 runs under unchanged settings,"** but the two *partially*-failed gpt-5.5 cells (`labor_supply.income_elasticity.prime_age`, `…substitution_elasticity.secondary`) each mix 10 survivors at 1200 with 5 replacements at 8000 — a within-cell budget change, not "unchanged settings." The within-cell protocol change the paper attributes only to the two cap-gains cells in fact applies to all four affected gpt-5.5 cells.

This affects no reported result (the income-elasticity center of −0.035 is well-behaved) and is purely a disclosure-accuracy fix, but it should be corrected in the two places above. Note the length-correlation caveat the authors already added covers the *selection* concern; the fix here is just about accurately stating the budget.

---

## Minor items (carryover + small)

- Protocol budget list (line 147) still omits gpt-5.5's raised budget (now recoverable from A16, so partial).
- 100% parse rate (line 159) is now adequately contextualized as post-re-elicitation by the following paragraph.
- Round-1 major 6 (training-data-recall circularity for the Table 3 benchmark comparison) is only softened ("not benchmark truths … right neighborhood"), not explicitly stated as memorization circularity. Interpretive, not soundness-blocking.

---

## Recommendation and summary

**Minor Revision.** The revision resolves every soundness-blocking concern from my round-1 Major Revision via exactly the disclosure-plus-ablation route I offered — the per-model harness table (A16) matches `providers.py`, the cross-mechanism ablation (A17) reproduces exactly from raw data (centers move ≤0.03, median 0.00), and all 58 manifest request IDs are traceable to the committed request logs with failure signatures that corroborate the stated error classes. The only genuine new issue is that gpt-5.5 was run at a 1200/8000 budget mix, which A16 ("8000") and line 161 ("unchanged settings") describe imprecisely, and this changes no result. The remaining fixes (uncommitted archive file, stale docstrings, manifest not tabulated as an appendix, and the width/reasoning-mode caveats on A17) are cosmetic and can be handled in a minor revision without re-review.

**Relevant files:** `/Users/maxghenis/llm-econ-beliefs/paper/paper.qmd` (lines 137, 147, 150, 161, 419-431); `/Users/maxghenis/llm-econ-beliefs/paper/tables/harness-disclosure.md`; `/Users/maxghenis/llm-econ-beliefs/paper/tables/mechanism-ablation.md`; `/Users/maxghenis/llm-econ-beliefs/results/failure-manifest.csv`; `/Users/maxghenis/llm-econ-beliefs/llm_econ_beliefs/providers.py` (lines 1, 18-62, 400-401); `/Users/maxghenis/llm-econ-beliefs/scripts/rerun_failed_runs.py` (lines 3-6, 59, 97-105); `/Users/maxghenis/llm-econ-beliefs/paper/build_tables.py` (lines 1947-1963, 2152-2192); `/Users/maxghenis/llm-econ-beliefs/results/claude-opus-4.7-mechanism-ablation-batch15/`.