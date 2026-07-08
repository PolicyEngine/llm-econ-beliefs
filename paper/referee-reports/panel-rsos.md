# Referee panel — Royal Society Open Science submission

Target journal: Royal Society Open Science (soundness-based criteria: valid methods, conclusions supported by data, complete reporting; novelty/impact are NOT review criteria).
Paper: paper/paper.qmd (render: paper.pdf). Data/artifacts: results/, paper/tables/. Prior rounds: referee-reports/referee1-8 (11-model panel); this round re-reviews after the July 2026 extension to 17 models.

## Referee 1: Uncertainty-quantification statistician
Expert in probabilistic elicitation, quantile aggregation, and meta-analysis (REML, Bayesian hierarchical). Review the estimand definition (prompt-and-sampling-conditioned elicited distributions), the law-of-total-variance pooling, piecewise-from-quantiles reconstruction, and coherence of pooled vs REML vs Bayes intervals. Scrutinize: mixed sampling regimes (temperature 1.0 for most models; Claude Fable 5/Opus 4.8/Sonnet 5 accept no sampling parameters), whether "beliefs" language overclaims relative to the measured object, support truncation, and R=15 adequacy.

## Referee 2: Public-finance economist
Expert in ETI, labor-supply elasticities, capital-gains realization responses, Saez (2001) sufficient statistics. Review the hand-coded benchmark ranges, sign-convention clarifiers, and the optimal-top-tax translation (Pareto a=1.5, welfare-weight assumptions). Scrutinize whether literature anchors are defensible and whether policy-translation caveats are adequate.

## Referee 3: LLM evaluation methodologist
Expert in LLM benchmarking, structured outputs, prompt sensitivity, contamination. Review cross-provider protocol heterogeneity: native Anthropic structured outputs vs LiteLLM forced function calls vs OpenAI strict JSON; completion budgets 1200/4000/8000/32000; provider-default reasoning configurations (always-on for Fable 5, adaptive for Sonnet 5, off for Opus 4.8); the 58 re-elicited infrastructure failures. Scrutinize model version pinning/snapshots, decoding-settings reporting, and whether mechanism differences confound cross-model comparisons.

## Referee 4: Reproducibility reviewer
Review the public repo (PolicyEngine/llm-econ-beliefs): cached-results reproduction path, scripts (run_v4_new_models.py, rerun_failed_runs.py, build_comparison_artifacts.py), whether paper tables rebuild from committed artifacts, cost accounting consistency, and paper-vs-results number agreement.

## Referee 5: Prior-round adjudicator
Read referee-reports/referee1-8 and verify each major prior finding was genuinely resolved in the current draft rather than renamed or suppressed: estimand precision, domain-split rankings replacing the global ranking, the policy-translation request, sign-convention handling, cost/success-rate reporting. Flag any prior issue the 17-model extension reintroduces (e.g., Gemini 3.5 Flash near-zero centers on sign-sensitive quantities vs the "clarifier eliminated wrong-sign outliers" claim).
