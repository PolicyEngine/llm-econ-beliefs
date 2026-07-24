Note: Same four models (the April premium tier), same quantities, same repeated-run design, two v4 clarifier wordings: the superseded April 19 elicitation (original wording — plain conditionals with the conventional direction first; the net-of-tax sibling's definition line states the conversion identity backwards) versus the published April 21 re-elicitation (revised wording — symmetric if-and-only-if clauses, worked magnitude example, corrected identity). April 19 runs are read from git history (commit ddca2375); every cell's prompt text is byte-verified against the original wording preserved in the seven holdout models' committed archives and against the current prompt builder's revised wording. Each cell pools 15 runs with the headline piecewise-uniform mixture. The comparison is not a pure wording experiment: the April 21 re-elicitation also moved to the per-quantity fallback harness that added request logging, and two days elapsed between elicitations, so wording is confounded with harness path and time.

| Model | Quantity | Original center | Revised center | Center change | Original 90% width | Revised 90% width |
| --- | --- | --- | --- | --- | --- | --- |
| Claude Opus 4.7 | Income elasticity of labor supply | -0.05 | -0.05 | 0 | 0.219 | 0.22 |
| Claude Opus 4.7 | Capital gains realizations elasticity | -0.7 | -0.7 | 0 | 1.647 | 1.527 |
| Claude Opus 4.7 | Capital gains realizations elasticity (net-of-tax-rate convention) | 0.7 | 0.7 | 0 | 1.538 | 1.652 |
| Claude Sonnet 4.6 | Income elasticity of labor supply | -0.093 | -0.097 | -0.003 | 0.39 | 0.395 |
| Claude Sonnet 4.6 | Capital gains realizations elasticity | -0.7 | -0.7 | 0 | 1.4 | 1.4 |
| Claude Sonnet 4.6 | Capital gains realizations elasticity (net-of-tax-rate convention) | 4.6 | 3.367 | -1.233 | 8.871 | 7.647 |
| Gemini 3.1 Pro | Income elasticity of labor supply | -0.05 | -0.073 | -0.023 | 0.241 | 0.315 |
| Gemini 3.1 Pro | Capital gains realizations elasticity | -0.67 | -0.709 | -0.039 | 0.997 | 0.997 |
| Gemini 3.1 Pro | Capital gains realizations elasticity (net-of-tax-rate convention) | 0.373 | 2.077 | 1.703 | 4.832 | 4.598 |
| Grok 4.20 | Income elasticity of labor supply | -0.095 | -0.107 | -0.011 | 0.522 | 0.577 |
| Grok 4.20 | Capital gains realizations elasticity | -0.553 | -0.473 | 0.08 | 1.762 | 1.807 |
| Grok 4.20 | Capital gains realizations elasticity (net-of-tax-rate convention) | 0.67 | 0.65 | -0.02 | 1.854 | 1.901 |
