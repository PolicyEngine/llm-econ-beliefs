Implemented and left uncommitted.

1. Finding 11 — Added the canonical 25-model registry with validated organizations, serving paths, families, and waves in [model_registry.py](/Users/maxghenis/llm-econ-beliefs/llm_econ_beliefs/model_registry.py:50). Emission and dashboard staging are in [build_model_registry.py](/Users/maxghenis/llm-econ-beliefs/scripts/build_model_registry.py:13), producing [model-registry.csv](/Users/maxghenis/llm-econ-beliefs/results/model-registry.csv:1). Paper organization ablations now keep all five independent labs separate in [build_tables.py](/Users/maxghenis/llm-econ-beliefs/paper/build_tables.py:936). Dashboard server and client metadata now derive from the CSV via [site-data.ts](/Users/maxghenis/llm-econ-beliefs/dashboard/src/lib/site-data.ts:71), [next.config.ts](/Users/maxghenis/llm-econ-beliefs/dashboard/next.config.ts:11), and [model-meta.ts](/Users/maxghenis/llm-econ-beliefs/dashboard/src/lib/model-meta.ts:14).

2. Finding 12 — Implemented strict PolicyBench crosswalk validation, duplicate detection, release/condition/country assertions, bidirectional anti-join output, and exact expected exclusions in [build_correlates.py](/Users/maxghenis/llm-econ-beliefs/scripts/build_correlates.py:306). Regression coverage is in [test_correlates_pipeline.py](/Users/maxghenis/llm-econ-beliefs/tests/test_correlates_pipeline.py:84).

3. Finding 5 — Added registry-wide raw-grid gating and machine-readable exclusions in [panel_grid_gate.py](/Users/maxghenis/llm-econ-beliefs/scripts/panel_grid_gate.py:25). Comparison artifacts additionally reject missing, duplicate, partial, or malformed summaries in [build_comparison_artifacts.py](/Users/maxghenis/llm-econ-beliefs/scripts/build_comparison_artifacts.py:48). Dashboard summaries and raw-run payloads are filtered against both gated artifacts in [dashboard-data.ts](/Users/maxghenis/llm-econ-beliefs/dashboard/src/lib/dashboard-data.ts:111) and [site-data.ts](/Users/maxghenis/llm-econ-beliefs/dashboard/src/lib/site-data.ts:117). Hard-coded model findings are hidden when gated out.

4. Finding 6 — Correlates now reconstruct pooled centers and the equal-weight piecewise-uniform ETI median directly from `runs.jsonl` in [build_correlates.py](/Users/maxghenis/llm-econ-beliefs/scripts/build_correlates.py:217). The matching paper construction is factored in [build_tables.py](/Users/maxghenis/llm-econ-beliefs/paper/build_tables.py:1570). Calibration writing is wired at [build_tables.py](/Users/maxghenis/llm-econ-beliefs/paper/build_tables.py:1630); missing or fallback `a=1.5` calibration fails clearly at [build_correlates.py](/Users/maxghenis/llm-econ-beliefs/scripts/build_correlates.py:388). Legacy correlates schemas now degrade cleanly instead of crashing the paper builder.

5. Finding 7 — ETI and derived tau* are one hypothesis, with the exact derived-row label, raw p-values, Holm adjustment, BH adjustment, and family size across eight non-derived tests in [build_correlates.py](/Users/maxghenis/llm-econ-beliefs/scripts/build_correlates.py:540) and [build_correlates.py](/Users/maxghenis/llm-econ-beliefs/scripts/build_correlates.py:700).

6. Finding 8 — Added leave-one-organization-out, April-only, July-only, and organization-block permutation sensitivities in [build_correlates.py](/Users/maxghenis/llm-econ-beliefs/scripts/build_correlates.py:760). The cluster test literally moves whole PolicyBench score vectors within equal-size organization strata, yielding 1,440 exact assignments for the current overlap at [build_correlates.py](/Users/maxghenis/llm-econ-beliefs/scripts/build_correlates.py:841).

Verification:

- Python: `134 passed`.
- Dashboard: `bun test` 7 passed; ESLint passed; production build passed.
- `build_correlates.py`: exited 2 with the accepted clear missing-calibration error; crosswalk and grid exclusion JSON printed correctly.
- No full `build_tables` or microdata run; no provider/network elicitation; no supervisor interaction.
- Only registry artifacts were written; `top-rate-calibration.json` remains absent.
- Final independent review: clean.
