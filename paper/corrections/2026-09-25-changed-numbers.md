# Changed published numbers

Old: `origin/main (published; results/ and paper/ identical to 959a9d0)`  
New: `this branch (regenerated)`

138 files changed; 2762 CSV cells changed.

## `paper/tables/armington-clarify-delta.csv` (7 cells)

| line | row | column | old | new |
|---|---|---|---|---|
| 18 | Gemini 3 Flash / [0.6512, 5.783] / [0, 5.903] | Clarified pooled 90% interval | [0, 5.903] | [0, 5.923] |
| 20 | Gemini 3.1 Pro / [0.5471, 4.933] / [0, 5.592] | Clarified pooled 90% interval | [0, 5.592] | [0, 5.625] |
| 21 | Gemini 3.5 Flash / [0.6111, 5.062] / [0.5137, 3.815] | Clarified center | 1.387 | 1.453 |
| 21 | Gemini 3.5 Flash / [0.6111, 5.062] / [0.5137, 3.815] | Change | -0.367 | -0.3 |
| 27 | Inkling / [0.7158, 5.05] / [0, 5.681] | Old center | 1.66 | 1.713 |
| 27 | Inkling / [0.7158, 5.05] / [0, 5.681] | Change | -0.18 | -0.233 |
| 27 | Inkling / [0.7158, 5.05] / [0, 5.681] | Clarified pooled 90% interval | [0, 5.681] | [0, 5.709] |

## `paper/tables/benchmark-comparison-labor-tax.csv` (3 cells)

| line | row | column | old | new |
|---|---|---|---|---|
| 2 | Capital gains realizations elasticity / [-1, -0.2] / 30 / 31 | Models in range | 30 / 31 | 31 / 31 |
| 2 | Capital gains realizations elasticity / [-1, -0.2] / 30 / 31 | Model max center | 0.01 | -0.327 |
| 6 | Income elasticity of labor supply / [-0.15, -0.05] / 26 / 31 | Model max center | 0.011 | -0.001 |

## `paper/tables/cap-gains-convention-audit.csv` (9 cells)

| line | row | column | old | new |
|---|---|---|---|---|
| 21 | Gemini 3.5 Flash / Google / 0.452 [-0.889, 3.250] | epsilon w.r.t. tax rate (median) | -0.4 | -0.6 |
| 21 | Gemini 3.5 Flash / Google / 0.452 [-0.889, 3.250] | Implied tau median [90%] | 0.452 [-0.889, 3.250] | 0.429 [0.200, 0.500] |
| 21 | Gemini 3.5 Flash / Google / 0.452 [-0.889, 3.250] | Share of draws in (0, 1) | 65% | 100% |
| 21 | Gemini 3.5 Flash / Google / 0.452 [-0.889, 3.250] | Band (LTCG [0.15, 0.37], ordinary-income [0.37, 0.55]) | uninformative (pole-straddling) | ordinary-income-rate consistent |
| 27 | Inkling / Thinking Machines / 0.333 [0.200, 0.500] | Implied tau median [90%] | 0.333 [0.200, 0.500] | 0.333 [0.211, 0.476] |
| 27 | Inkling / Thinking Machines / 0.333 [0.200, 0.500] | Share of draws in (0, 1) | 94% | 100% |
| 28 | Kimi K2.6 / Moonshot AI / 0.400 [0.185, 0.560] | Implied tau median [90%] | 0.400 [0.185, 0.560] | 0.381 [0.200, 0.542] |
| 28 | Kimi K2.6 / Moonshot AI / 0.400 [0.185, 0.560] | Share of draws in (0, 1) | 94% | 100% |
| 29 | Kimi K3 / Moonshot AI / 0.444 [0.143, 0.545] | Implied tau median [90%] | 0.444 [0.143, 0.545] | 0.444 [0.190, 0.545] |

## `paper/tables/correlates-country.csv` (16 cells)

| line | row | column | old | new |
|---|---|---|---|---|
| 2 | Implied optimal top rate (%) / 35.843 (24) / 32.942 (7) | Holm p | 0.209* | 0.237* |
| 3 | ETI pooled median / 0.421 (24) / 0.479 (7) | Holm p | 0.209 | 0.237 |
| 4 | Avg interval-width rank (1 = tightest) / 13.789 (24) / 20.308 (7) | US median (n) | 13.789 (24) | 13.865 (24) |
| 4 | Avg interval-width rank (1 = tightest) / 13.789 (24) / 20.308 (7) | China median (n) | 20.308 (7) | 20.462 (7) |
| 4 | Avg interval-width rank (1 = tightest) / 13.789 (24) / 20.308 (7) | China - US | +6.519 | +6.596 |
| 4 | Avg interval-width rank (1 = tightest) / 13.789 (24) / 20.308 (7) | Permutation p | 0.029 | 0.055 |
| 4 | Avg interval-width rank (1 = tightest) / 13.789 (24) / 20.308 (7) | Holm p | 0.107 | 0.222 |
| 4 | Avg interval-width rank (1 = tightest) / 13.789 (24) / 20.308 (7) | BH p | 0.057 | 0.139 |
| 5 | Mean |center|, labor-and-tax / 0.368 (24) / 0.324 (7) | China median (n) | 0.324 (7) | 0.334 (7) |
| 5 | Mean |center|, labor-and-tax / 0.368 (24) / 0.324 (7) | China - US | -0.044 | -0.034 |
| 5 | Mean |center|, labor-and-tax / 0.368 (24) / 0.324 (7) | Permutation p | 0.027 | 0.079 |
| 5 | Mean |center|, labor-and-tax / 0.368 (24) / 0.324 (7) | Holm p | 0.107 | 0.237 |
| 5 | Mean |center|, labor-and-tax / 0.368 (24) / 0.324 (7) | BH p | 0.057 | 0.139 |
| 6 | Mean |center|, macro-and-trade / 1.162 (24) / 1.038 (7) | Permutation p | 0.169 | 0.168 |
| 6 | Mean |center|, macro-and-trade / 1.162 (24) / 1.038 (7) | Holm p | 0.209 | 0.237 |
| 6 | Mean |center|, macro-and-trade / 1.162 (24) / 1.038 (7) | BH p | 0.169 | 0.168 |

## `paper/tables/correlates-model-summary.csv` (24 cells)

| line | row | column | old | new |
|---|---|---|---|---|
| 2 | Claude Opus 5 / Anthropic / July 2026 late | Avg width rank | 13.0 | 13.1 |
| 4 | Gemini 3.5 Flash / Google / July 2026 frontier | Avg width rank | 13.3 | 11.1 |
| 5 | GPT-5.5 / OpenAI / July 2026 frontier | Avg width rank | 15.1 | 15.3 |
| 7 | Qwen 3.8 Max / Alibaba / August 2026 | Avg width rank | 19.4 | 19.5 |
| 9 | Claude Opus 4.8 / Anthropic / July 2026 frontier | Avg width rank | 11.0 | 11.2 |
| 10 | Gemini 3.1 Flash-Lite / Google / April 2026 | Avg width rank | 13.9 | 14.2 |
| 11 | Claude Opus 4.7 / Anthropic / April 2026 | Avg width rank | 9.5 | 9.6 |
| 12 | Gemini 3 Flash / Google / April 2026 | Avg width rank | 12.9 | 13.0 |
| 14 | Grok 4.5 / xAI / July 2026 late | Avg width rank | 18.8 | 19.0 |
| 15 | GPT-5.4 / OpenAI / April 2026 | Avg width rank | 15.3 | 15.4 |
| 16 | Gemini 3.6 Flash / Google / July 2026 late | Avg width rank | 7.5 | 7.6 |
| 17 | GPT-5.6 Sol / OpenAI / July 2026 GPT-5.6 | Avg width rank | 17.4 | 17.5 |
| 19 | Claude Fable 5 / Anthropic / July 2026 frontier | Avg width rank | 6.8 | 6.9 |
| 20 | Grok 4.3 / xAI / July 2026 frontier | Avg width rank | 18.7 | 18.8 |
| 21 | MiniMax M3 / MiniMax / July 2026 independent labs | Avg width rank | 18.8 | 19.0 |
| 22 | Inkling / Thinking Machines / August 2026 | Avg width rank | 12.7 | 12.1 |
| 23 | Claude Sonnet 5 / Anthropic / July 2026 frontier | Avg width rank | 9.8 | 10.0 |
| 24 | DeepSeek V4 Pro / DeepSeek / July 2026 independent labs | Avg width rank | 20.4 | 20.5 |
| 25 | GPT-5.6 Terra / OpenAI / July 2026 GPT-5.6 | Avg width rank | 13.8 | 13.9 |
| 27 | Kimi K2.6 / Moonshot AI / July 2026 independent labs | Avg width rank | 22.7 | 22.5 |
| 28 | Claude Sonnet 4.6 / Anthropic / April 2026 | Avg width rank | 13.7 | 13.8 |
| 29 | Grok 4.20 / xAI / April 2026 | Avg width rank | 23.8 | 24.0 |
| 30 | Claude Haiku 4.5 / Anthropic / April 2026 | Avg width rank | 9.3 | 9.4 |
| 32 | Qwen 3.7 Max / Alibaba / July 2026 independent labs | Avg width rank | 20.3 | 20.5 |

## `paper/tables/ies-clarify-delta.csv` (4 cells)

| line | row | column | old | new |
|---|---|---|---|---|
| 18 | Gemini 3 Flash / [0.1, 1.979] / [0, 1.667] | Clarified pooled 90% interval | [0, 1.667] | [0, 1.671] |
| 20 | Gemini 3.1 Pro / [0.2857, 2.499] / [0, 1.767] | Clarified pooled 90% interval | [0, 1.767] | [0, 1.754] |
| 21 | Gemini 3.5 Flash / [0.07895, 2.11] / [0.1037, 1.899] | Old center | 0.933 | 0.987 |
| 21 | Gemini 3.5 Flash / [0.07895, 2.11] / [0.1037, 1.899] | Change | -0.367 | -0.42 |

## `paper/tables/leave-one-organization-out-appendix.csv` (12 cells)

| line | row | column | old | new |
|---|---|---|---|---|
| 2 | Labor/tax / Alibaba / Claude Sonnet 4.6 | Max avg-rank shift | 1.833 | 1.667 |
| 3 | Labor/tax / Anthropic / Grok 4.20 | Spearman rho | 0.994 | 0.993 |
| 3 | Labor/tax / Anthropic / Grok 4.20 | Top retained model, full panel | Grok 4.20 | Grok 4.5 |
| 3 | Labor/tax / Anthropic / Grok 4.20 | Top retained model, leave-out | Grok 4.20 | Grok 4.5 |
| 6 | Labor/tax / MiniMax / Claude Sonnet 4.6 | Max avg-rank shift | 0.833 | 0.5 |
| 7 | Labor/tax / Moonshot AI / Claude Sonnet 4.6 | Max avg-rank shift | 2.0 | 1.667 |
| 8 | Labor/tax / OpenAI / Claude Sonnet 4.6 | Max avg-rank shift | 5.667 | 5.583 |
| 9 | Labor/tax / Thinking Machines / Claude Sonnet 4.6 | Spearman rho | 0.999 | 1.0 |
| 9 | Labor/tax / Thinking Machines / Claude Sonnet 4.6 | Max avg-rank shift | 1.0 | 0.917 |
| 11 | Labor/tax / xAI / Claude Sonnet 4.6 | Max avg-rank shift | 3.5 | 3.333 |
| 18 | Macro/trade / OpenAI / Grok 4.3 | Top retained model, leave-out | Grok 4.20 | Grok 4.3 |
| 21 | Macro/trade / xAI / GPT-5.6 Luna | Top retained model, leave-out | GPT-5.4 nano | GPT-5.6 Luna |

## `paper/tables/leave-one-provider-out-appendix.csv` (12 cells)

| line | row | column | old | new |
|---|---|---|---|---|
| 2 | Labor/tax / Alibaba / Claude Sonnet 4.6 | Max avg-rank shift | 1.833 | 1.667 |
| 3 | Labor/tax / Anthropic / Grok 4.20 | Spearman rho | 0.994 | 0.993 |
| 3 | Labor/tax / Anthropic / Grok 4.20 | Top retained model, full panel | Grok 4.20 | Grok 4.5 |
| 3 | Labor/tax / Anthropic / Grok 4.20 | Top retained model, leave-out | Grok 4.20 | Grok 4.5 |
| 6 | Labor/tax / MiniMax / Claude Sonnet 4.6 | Max avg-rank shift | 0.833 | 0.5 |
| 7 | Labor/tax / Moonshot AI / Claude Sonnet 4.6 | Max avg-rank shift | 2.0 | 1.667 |
| 8 | Labor/tax / OpenAI / Claude Sonnet 4.6 | Max avg-rank shift | 5.667 | 5.583 |
| 9 | Labor/tax / Thinking Machines / Claude Sonnet 4.6 | Spearman rho | 0.999 | 1.0 |
| 9 | Labor/tax / Thinking Machines / Claude Sonnet 4.6 | Max avg-rank shift | 1.0 | 0.917 |
| 11 | Labor/tax / xAI / Claude Sonnet 4.6 | Max avg-rank shift | 3.5 | 3.333 |
| 18 | Macro/trade / OpenAI / Grok 4.3 | Top retained model, leave-out | Grok 4.20 | Grok 4.3 |
| 21 | Macro/trade / xAI / GPT-5.6 Luna | Top retained model, leave-out | GPT-5.4 nano | GPT-5.6 Luna |

## `paper/tables/model-overview-labor-tax.csv` (45 cells)

- row order changed; rows matched by identity
| line | row | column | old | new |
|---|---|---|---|---|
| 2 | Claude Sonnet 4.6 / Anthropic | Avg predictive-uncertainty rank (1=narrowest) | 15.83 | 16.0 |
| 3 | Grok 4.20 / xAI | Avg abs-elasticity rank (1=highest) | 9.83 | 10.17 |
| 3 | Grok 4.20 / xAI | Avg predictive-uncertainty rank (1=narrowest) | 23.83 | 24.33 |
| 4 | Grok 4.5 / xAI | Avg predictive-uncertainty rank (1=narrowest) | 17.17 | 17.67 |
| 5 | Qwen 3.7 Max / Alibaba / — | Avg predictive-uncertainty rank (1=narrowest) | 23.83 | 24.33 |
| 6 | GPT-5.6 Terra / OpenAI / — | Avg abs-elasticity rank (1=highest) | 12.33 | 12.67 |
| 6 | GPT-5.6 Terra / OpenAI / — | Avg predictive-uncertainty rank (1=narrowest) | 17.33 | 17.5 |
| 7 | GLM-5.2 / Zhipu AI / — | Mean absolute pooled center | 0.37 | 0.369 |
| 8 | Grok 4.3 / xAI | Avg predictive-uncertainty rank (1=narrowest) | 17.67 | 18.0 |
| 9 | Claude Haiku 4.5 / Anthropic | Avg predictive-uncertainty rank (1=narrowest) | 11.67 | 11.83 |
| 10 | Inkling / Thinking Machines / — | Avg abs-elasticity rank (1=highest) | 13.42 | 12.42 |
| 10 | Inkling / Thinking Machines / — | Avg predictive-uncertainty rank (1=narrowest) | 13.83 | 12.5 |
| 10 | Inkling / Thinking Machines / — | Mean absolute pooled center | 0.341 | 0.36 |
| 10 | Inkling / Thinking Machines / — | Mean pooled 90% width | 1.125 | 0.921 |
| 11 | Kimi K3 / Moonshot AI / — | Avg abs-elasticity rank (1=highest) | 14.58 | 15.08 |
| 12 | Gemini 3 Flash / Google | Avg predictive-uncertainty rank (1=narrowest) | 10.0 | 10.17 |
| 13 | GPT-5.4 / OpenAI | Avg abs-elasticity rank (1=highest) | 15.08 | 15.17 |
| 13 | GPT-5.4 / OpenAI | Avg predictive-uncertainty rank (1=narrowest) | 16.33 | 16.5 |
| 14 | Claude Fable 5 / Anthropic | Avg predictive-uncertainty rank (1=narrowest) | 6.17 | 6.33 |
| 16 | Claude Opus 4.7 / Anthropic | Avg predictive-uncertainty rank (1=narrowest) | 9.83 | 10.17 |
| 17 | Claude Opus 4.8 / Anthropic | Avg predictive-uncertainty rank (1=narrowest) | 10.5 | 10.83 |
| 18 | GPT-5.4 nano / OpenAI | Avg abs-elasticity rank (1=highest) | 16.17 | 16.5 |
| 19 | Qwen 3.8 Max / Alibaba / — | Avg abs-elasticity rank (1=highest) | 16.58 | 17.08 |
| 19 | Qwen 3.8 Max / Alibaba / — | Avg predictive-uncertainty rank (1=narrowest) | 19.5 | 19.67 |
| 20 | Claude Opus 5 / Anthropic / — | Avg predictive-uncertainty rank (1=narrowest) | 14.5 | 14.67 |
| 21 | Kimi K2.6 / Moonshot AI / — | Avg abs-elasticity rank (1=highest) | 16.92 | 17.0 |
| 21 | Kimi K2.6 / Moonshot AI / — | Avg predictive-uncertainty rank (1=narrowest) | 20.33 | 20.0 |
| 21 | Kimi K2.6 / Moonshot AI / — | Mean absolute pooled center | 0.324 | 0.334 |
| 21 | Kimi K2.6 / Moonshot AI / — | Mean pooled 90% width | 1.205 | 1.102 |
| 22 | DeepSeek V4 Pro / DeepSeek / — | Avg abs-elasticity rank (1=highest) | 17.0 | 17.33 |
| 22 | DeepSeek V4 Pro / DeepSeek / — | Avg predictive-uncertainty rank (1=narrowest) | 20.67 | 20.83 |
| 24 | GPT-5.6 Sol / OpenAI / — | Avg abs-elasticity rank (1=highest) | 17.75 | 17.58 |
| 24 | GPT-5.6 Sol / OpenAI / — | Avg predictive-uncertainty rank (1=narrowest) | 12.83 | 13.0 |
| 26 | Claude Sonnet 5 / Anthropic | Avg predictive-uncertainty rank (1=narrowest) | 8.67 | 9.0 |
| 27 | Gemini 3.1 Flash-Lite / Google | Avg predictive-uncertainty rank (1=narrowest) | 11.33 | 12.0 |
| 28 | GPT-5.6 Luna / OpenAI / — | Avg abs-elasticity rank (1=highest) | 19.92 | 19.75 |
| 29 | Gemini 3.6 Flash / Google | Avg abs-elasticity rank (1=highest) | 21.17 | 21.0 |
| 29 | Gemini 3.6 Flash / Google | Avg predictive-uncertainty rank (1=narrowest) | 6.5 | 6.83 |
| 30 | MiniMax M3 / MiniMax / — | Avg abs-elasticity rank (1=highest) | 21.42 | 21.75 |
| 30 | MiniMax M3 / MiniMax / — | Avg predictive-uncertainty rank (1=narrowest) | 22.67 | 23.17 |
| 31 | GPT-5.5 / OpenAI | Avg predictive-uncertainty rank (1=narrowest) | 9.5 | 10.0 |
| 32 | Gemini 3.5 Flash / Google | Avg abs-elasticity rank (1=highest) | 26.5 | 25.17 |
| 32 | Gemini 3.5 Flash / Google | Avg predictive-uncertainty rank (1=narrowest) | 11.67 | 6.83 |
| 32 | Gemini 3.5 Flash / Google | Mean absolute pooled center | 0.218 | 0.309 |
| 32 | Gemini 3.5 Flash / Google | Mean pooled 90% width | 1.059 | 0.841 |

## `paper/tables/model-overview-macro-trade.csv` (7 cells)

| line | row | column | old | new |
|---|---|---|---|---|
| 3 | Grok 4.20 / xAI | Avg abs-elasticity rank (1=highest) | 6.83 | 7.17 |
| 4 | GPT-5.6 Luna / OpenAI / — | Avg abs-elasticity rank (1=highest) | 7.5 | 7.17 |
| 9 | Gemini 3.5 Flash / Google | Avg abs-elasticity rank (1=highest) | 10.5 | 10.67 |
| 9 | Gemini 3.5 Flash / Google | Mean absolute pooled center | 1.153 | 1.16 |
| 10 | Grok 4.5 / xAI | Avg abs-elasticity rank (1=highest) | 11.33 | 11.5 |
| 11 | Kimi K2.6 / Moonshot AI / — | Avg abs-elasticity rank (1=highest) | 12.0 | 11.67 |
| 17 | Inkling / Thinking Machines / — | Mean absolute pooled center | 1.069 | 1.087 |

## `paper/tables/model-overview-simulation.csv` (13 cells)

- row order changed; rows matched by identity
| line | row | column | old | new |
|---|---|---|---|---|
| 13 | Claude Haiku 4.5 / Anthropic | Avg abs-elasticity rank (1=highest) | 12.5 | 12.58 |
| 15 | Kimi K2.6 / Moonshot AI / — | Avg abs-elasticity rank (1=highest) | 13.5 | 13.58 |
| 17 | Inkling / Thinking Machines / — | Avg abs-elasticity rank (1=highest) | 16.71 | 16.5 |
| 20 | Claude Fable 5 / Anthropic | Avg abs-elasticity rank (1=highest) | 17.83 | 17.88 |
| 21 | Gemini 3.1 Pro / Google | Avg abs-elasticity rank (1=highest) | 18.79 | 18.88 |
| 23 | GPT-5.6 Sol / OpenAI / — | Avg abs-elasticity rank (1=highest) | 19.25 | 19.38 |
| 25 | Qwen 3.8 Max / Alibaba / — | Avg abs-elasticity rank (1=highest) | 21.92 | 22.08 |
| 28 | MiniMax M3 / MiniMax / — | Avg abs-elasticity rank (1=highest) | 25.08 | 24.71 |
| 28 | MiniMax M3 / MiniMax / — | Mean absolute pooled center | 0.173 | 0.174 |
| 30 | Gemini 3 Flash / Google | Avg abs-elasticity rank (1=highest) | 27.17 | 27.25 |
| 31 | Gemini 3.5 Flash / Google | Avg abs-elasticity rank (1=highest) | 27.46 | 27.29 |
| 31 | Gemini 3.5 Flash / Google | Mean absolute pooled center | 0.165 | 0.167 |
| 32 | Gemini 3.1 Flash-Lite / Google | Avg abs-elasticity rank (1=highest) | 28.75 | 28.83 |

## `paper/tables/policybench-correlates.csv` (19 cells)

| line | row | column | old | new |
|---|---|---|---|---|
| 2 | Tax within-$1 (domain-matched) / Mean |center|, labor-and-tax / no | Spearman rho | 0.085 | 0.074 |
| 2 | Tax within-$1 (domain-matched) / Mean |center|, labor-and-tax / no | Raw permutation p | 0.665 | 0.704 |
| 2 | Tax within-$1 (domain-matched) / Mean |center|, labor-and-tax / no | BH-adjusted p | 0.760 | 0.805 |
| 3 | Tax within-$1 (domain-matched) / Mean |center|, macro-and-trade / no | Spearman rho | 0.236 | 0.237 |
| 3 | Tax within-$1 (domain-matched) / Mean |center|, macro-and-trade / no | Raw permutation p | 0.227 | 0.223 |
| 3 | Tax within-$1 (domain-matched) / Mean |center|, macro-and-trade / no | BH-adjusted p | 0.453 | 0.446 |
| 4 | Tax within-$1 (domain-matched) / Avg interval-width rank (1 = tightest) / no | Spearman rho | -0.274 | -0.254 |
| 4 | Tax within-$1 (domain-matched) / Avg interval-width rank (1 = tightest) / no | Raw permutation p | 0.158 | 0.193 |
| 4 | Tax within-$1 (domain-matched) / Avg interval-width rank (1 = tightest) / no | Holm-adjusted p | 0.949 | 1.000 |
| 4 | Tax within-$1 (domain-matched) / Avg interval-width rank (1 = tightest) / no | BH-adjusted p | 0.422 | 0.446 |
| 7 | Overall within-$1 (leaderboard headline) / Mean |center|, labor-and-tax / no | Spearman rho | 0.021 | 0.014 |
| 7 | Overall within-$1 (leaderboard headline) / Mean |center|, labor-and-tax / no | Raw permutation p | 0.915 | 0.942 |
| 7 | Overall within-$1 (leaderboard headline) / Mean |center|, labor-and-tax / no | BH-adjusted p | 0.915 | 0.942 |
| 8 | Overall within-$1 (leaderboard headline) / Mean |center|, macro-and-trade / no | Spearman rho | 0.115 | 0.118 |
| 8 | Overall within-$1 (leaderboard headline) / Mean |center|, macro-and-trade / no | Raw permutation p | 0.555 | 0.546 |
| 8 | Overall within-$1 (leaderboard headline) / Mean |center|, macro-and-trade / no | BH-adjusted p | 0.739 | 0.728 |
| 9 | Overall within-$1 (leaderboard headline) / Avg interval-width rank (1 = tightest) / no | Spearman rho | -0.180 | -0.167 |
| 9 | Overall within-$1 (leaderboard headline) / Avg interval-width rank (1 = tightest) / no | Raw permutation p | 0.357 | 0.394 |
| 9 | Overall within-$1 (leaderboard headline) / Avg interval-width rank (1 = tightest) / no | BH-adjusted p | 0.571 | 0.630 |

## `paper/tables/pooling-robustness-appendix.csv` (110 cells)

- row order changed; rows matched by identity
| line | row | column | old | new |
|---|---|---|---|---|
| 2 | Claude Fable 5 | Avg pooled rank | 6.85 | 6.92 |
| 2 | Claude Fable 5 | Avg REML rank | 7.73 | 7.81 |
| 2 | Claude Fable 5 | Avg Bayes rank | 7.0 | 7.23 |
| 3 | Gemini 3.6 Flash | Avg pooled rank | 7.46 | 7.62 |
| 3 | Gemini 3.6 Flash | Avg REML rank | 10.23 | 10.46 |
| 3 | Gemini 3.6 Flash | Avg Bayes rank | 9.12 | 9.27 |
| 3 | Gemini 3.6 Flash | Max rank spread | 2.77 | 2.85 |
| 4 | Claude Haiku 4.5 | Avg pooled rank | 9.31 | 9.38 |
| 4 | Claude Haiku 4.5 | Avg REML rank | 8.38 | 8.62 |
| 4 | Claude Haiku 4.5 | Avg Bayes rank | 8.23 | 8.46 |
| 4 | Claude Haiku 4.5 | Max rank spread | 1.08 | 0.92 |
| 5 | Claude Opus 4.7 | Avg pooled rank | 9.46 | 9.62 |
| 5 | Claude Opus 4.7 | Avg REML rank | 13.15 | 13.38 |
| 5 | Claude Opus 4.7 | Avg Bayes rank | 11.77 | 11.92 |
| 5 | Claude Opus 4.7 | Max rank spread | 3.69 | 3.77 |
| 6 | Claude Sonnet 5 | Avg pooled rank | 9.77 | 9.92 |
| 6 | Claude Sonnet 5 | Avg REML rank | 12.15 | 12.46 |
| 6 | Claude Sonnet 5 | Avg Bayes rank | 11.46 | 11.62 |
| 6 | Claude Sonnet 5 | Max rank spread | 2.38 | 2.54 |
| 7 | Claude Opus 4.8 | Avg pooled rank | 11.04 | 11.19 |
| 7 | Claude Opus 4.8 | Avg REML rank | 14.42 | 14.73 |
| 7 | Claude Opus 4.8 | Avg Bayes rank | 13.77 | 13.92 |
| 7 | Claude Opus 4.8 | Max rank spread | 3.38 | 3.54 |
| 8 | Gemini 3.1 Pro | Avg REML rank | 9.85 | 10.0 |
| 8 | Gemini 3.1 Pro | Avg Bayes rank | 10.15 | 10.31 |
| 8 | Gemini 3.1 Pro | Max rank spread | 1.35 | 1.19 |
| 9 | Inkling | Avg pooled rank | 12.69 | 12.08 |
| 9 | Inkling | Avg REML rank | 11.0 | 9.23 |
| 9 | Inkling | Avg Bayes rank | 12.15 | 9.85 |
| 9 | Inkling | Max rank spread | 1.69 | 2.85 |
| 10 | Gemini 3 Flash | Avg pooled rank | 12.92 | 13.0 |
| 10 | Gemini 3 Flash | Avg REML rank | 13.0 | 13.31 |
| 10 | Gemini 3 Flash | Avg Bayes rank | 12.0 | 12.23 |
| 10 | Gemini 3 Flash | Max rank spread | 1.0 | 1.08 |
| 11 | Claude Opus 5 | Avg pooled rank | 13.0 | 13.08 |
| 11 | Claude Opus 5 | Avg REML rank | 14.15 | 14.38 |
| 11 | Claude Opus 5 | Avg Bayes rank | 13.08 | 13.23 |
| 11 | Claude Opus 5 | Max rank spread | 1.15 | 1.31 |
| 12 | Gemini 3.5 Flash | Avg pooled rank | 13.31 | 11.08 |
| 12 | Gemini 3.5 Flash | Avg REML rank | 15.69 | 13.31 |
| 12 | Gemini 3.5 Flash | Avg Bayes rank | 17.15 | 14.0 |
| 12 | Gemini 3.5 Flash | Max rank spread | 3.85 | 2.92 |
| 13 | Claude Sonnet 4.6 | Avg pooled rank | 13.77 | 13.85 |
| 13 | Claude Sonnet 4.6 | Avg REML rank | 18.31 | 18.38 |
| 13 | Claude Sonnet 4.6 | Avg Bayes rank | 17.23 | 17.54 |
| 14 | GPT-5.6 Terra | Avg pooled rank | 13.85 | 13.92 |
| 14 | GPT-5.6 Terra | Avg REML rank | 14.46 | 14.62 |
| 14 | GPT-5.6 Terra | Avg Bayes rank | 15.38 | 15.62 |
| 14 | GPT-5.6 Terra | Max rank spread | 1.54 | 1.69 |
| 15 | Gemini 3.1 Flash-Lite | Avg pooled rank | 13.92 | 14.23 |
| 15 | Gemini 3.1 Flash-Lite | Avg REML rank | 14.12 | 14.42 |
| 15 | Gemini 3.1 Flash-Lite | Avg Bayes rank | 13.69 | 14.0 |
| 16 | GPT-5.5 | Avg pooled rank | 15.08 | 15.31 |
| 16 | GPT-5.5 | Avg REML rank | 17.77 | 18.08 |
| 16 | GPT-5.5 | Avg Bayes rank | 16.77 | 17.0 |
| 16 | GPT-5.5 | Max rank spread | 2.69 | 2.77 |
| 17 | GPT-5.4 | Avg pooled rank | 15.31 | 15.38 |
| 17 | GPT-5.4 | Avg REML rank | 18.38 | 18.62 |
| 17 | GPT-5.4 | Avg Bayes rank | 17.38 | 17.77 |
| 17 | GPT-5.4 | Max rank spread | 3.08 | 3.23 |
| 18 | GPT-5.6 Sol | Avg pooled rank | 17.38 | 17.46 |
| 18 | GPT-5.6 Sol | Avg REML rank | 19.46 | 19.62 |
| 18 | GPT-5.6 Sol | Avg Bayes rank | 19.0 | 19.15 |
| 18 | GPT-5.6 Sol | Max rank spread | 2.08 | 2.15 |
| 19 | Grok 4.3 | Avg pooled rank | 18.69 | 18.85 |
| 19 | Grok 4.3 | Avg REML rank | 18.19 | 18.35 |
| 19 | Grok 4.3 | Avg Bayes rank | 17.69 | 18.0 |
| 19 | Grok 4.3 | Max rank spread | 1.0 | 0.85 |
| 20 | GPT-5.4 nano | Avg Bayes rank | 18.15 | 18.23 |
| 21 | Kimi K3 | Avg REML rank | 18.31 | 18.38 |
| 21 | Kimi K3 | Avg Bayes rank | 18.69 | 19.0 |
| 21 | Kimi K3 | Max rank spread | 0.46 | 0.62 |
| 22 | MiniMax M3 | Avg pooled rank | 18.77 | 19.0 |
| 22 | MiniMax M3 | Avg REML rank | 14.31 | 14.15 |
| 22 | MiniMax M3 | Avg Bayes rank | 17.38 | 17.69 |
| 22 | MiniMax M3 | Max rank spread | 4.46 | 4.85 |
| 23 | Grok 4.5 | Avg pooled rank | 18.85 | 19.08 |
| 23 | Grok 4.5 | Avg REML rank | 19.46 | 19.69 |
| 23 | Grok 4.5 | Avg Bayes rank | 18.04 | 18.27 |
| 24 | Grok 4.1 Fast | Avg REML rank | 17.92 | 18.08 |
| 24 | Grok 4.1 Fast | Avg Bayes rank | 17.5 | 17.73 |
| 24 | Grok 4.1 Fast | Max rank spread | 1.69 | 1.46 |
| 25 | Qwen 3.8 Max | Avg pooled rank | 19.38 | 19.46 |
| 25 | Qwen 3.8 Max | Avg REML rank | 18.19 | 18.35 |
| 25 | Qwen 3.8 Max | Avg Bayes rank | 18.46 | 18.62 |
| 25 | Qwen 3.8 Max | Max rank spread | 1.19 | 1.12 |
| 26 | Qwen 3.7 Max | Avg pooled rank | 20.31 | 20.54 |
| 26 | Qwen 3.7 Max | Avg REML rank | 18.42 | 18.58 |
| 26 | Qwen 3.7 Max | Avg Bayes rank | 18.81 | 19.12 |
| 26 | Qwen 3.7 Max | Max rank spread | 1.88 | 1.96 |
| 27 | DeepSeek V4 Pro | Avg pooled rank | 20.38 | 20.46 |
| 27 | DeepSeek V4 Pro | Avg Bayes rank | 18.31 | 18.69 |
| 27 | DeepSeek V4 Pro | Max rank spread | 4.15 | 4.23 |
| 28 | GLM-5.2 | Avg REML rank | 17.0 | 17.23 |
| 28 | GLM-5.2 | Avg Bayes rank | 18.5 | 18.81 |
| 28 | GLM-5.2 | Max rank spread | 3.85 | 3.62 |
| 29 | Kimi K2.6 | Avg pooled rank | 22.69 | 22.54 |
| 29 | Kimi K2.6 | Avg REML rank | 19.31 | 18.54 |
| 29 | Kimi K2.6 | Avg Bayes rank | 20.08 | 19.0 |
| 29 | Kimi K2.6 | Max rank spread | 3.38 | 4.0 |
| 30 | GPT-5.4 mini | Avg REML rank | 21.31 | 21.54 |
| 30 | GPT-5.4 mini | Avg Bayes rank | 21.27 | 21.58 |
| 30 | GPT-5.4 mini | Max rank spread | 1.85 | 1.58 |
| 31 | Grok 4.20 | Avg pooled rank | 23.77 | 24.0 |
| 31 | Grok 4.20 | Avg REML rank | 23.0 | 23.23 |
| 31 | Grok 4.20 | Avg Bayes rank | 22.23 | 22.38 |
| 31 | Grok 4.20 | Max rank spread | 1.54 | 1.62 |
| 32 | GPT-5.6 Luna | Avg REML rank | 25.85 | 26.0 |
| 32 | GPT-5.6 Luna | Avg Bayes rank | 25.54 | 25.77 |
| 32 | GPT-5.6 Luna | Max rank spread | 0.62 | 0.38 |

## `paper/tables/quantile-rule-appendix.csv` (66 cells)

- row order changed; rows matched by identity
| line | row | column | old | new |
|---|---|---|---|---|
| 2 | Claude Fable 5 | Avg piecewise-uniform rank | 6.85 | 6.92 |
| 2 | Claude Fable 5 | Avg transformed-normal rank | 8.15 | 8.23 |
| 3 | Gemini 3.6 Flash | Avg piecewise-uniform rank | 7.46 | 7.62 |
| 3 | Gemini 3.6 Flash | Avg transformed-normal rank | 9.31 | 9.46 |
| 4 | Claude Haiku 4.5 | Avg piecewise-uniform rank | 9.31 | 9.38 |
| 4 | Claude Haiku 4.5 | Avg transformed-normal rank | 8.23 | 8.46 |
| 4 | Claude Haiku 4.5 | Rank shift | -1.08 | -0.92 |
| 5 | Claude Opus 4.7 | Avg piecewise-uniform rank | 9.46 | 9.62 |
| 5 | Claude Opus 4.7 | Avg transformed-normal rank | 13.38 | 13.62 |
| 5 | Claude Opus 4.7 | Rank shift | 3.92 | 4.0 |
| 6 | Claude Sonnet 5 | Avg piecewise-uniform rank | 9.77 | 9.92 |
| 6 | Claude Sonnet 5 | Avg transformed-normal rank | 12.08 | 12.31 |
| 6 | Claude Sonnet 5 | Rank shift | 2.31 | 2.38 |
| 7 | Claude Opus 4.8 | Avg piecewise-uniform rank | 11.04 | 11.19 |
| 7 | Claude Opus 4.8 | Avg transformed-normal rank | 14.42 | 14.73 |
| 7 | Claude Opus 4.8 | Rank shift | 3.38 | 3.54 |
| 9 | Inkling | Avg piecewise-uniform rank | 12.69 | 12.08 |
| 9 | Inkling | Avg transformed-normal rank | 11.69 | 9.77 |
| 9 | Inkling | Rank shift | -1.0 | -2.31 |
| 10 | Gemini 3 Flash | Avg piecewise-uniform rank | 12.92 | 13.0 |
| 10 | Gemini 3 Flash | Avg transformed-normal rank | 12.62 | 12.77 |
| 10 | Gemini 3 Flash | Rank shift | -0.31 | -0.23 |
| 11 | Claude Opus 5 | Avg piecewise-uniform rank | 13.0 | 13.08 |
| 11 | Claude Opus 5 | Avg transformed-normal rank | 14.38 | 14.62 |
| 11 | Claude Opus 5 | Rank shift | 1.38 | 1.54 |
| 12 | Gemini 3.5 Flash | Avg piecewise-uniform rank | 13.31 | 11.08 |
| 12 | Gemini 3.5 Flash | Avg transformed-normal rank | 14.46 | 13.0 |
| 12 | Gemini 3.5 Flash | Rank shift | 1.15 | 1.92 |
| 13 | Claude Sonnet 4.6 | Avg piecewise-uniform rank | 13.77 | 13.85 |
| 13 | Claude Sonnet 4.6 | Avg transformed-normal rank | 18.19 | 18.35 |
| 13 | Claude Sonnet 4.6 | Rank shift | 4.42 | 4.5 |
| 14 | GPT-5.6 Terra | Avg piecewise-uniform rank | 13.85 | 13.92 |
| 14 | GPT-5.6 Terra | Avg transformed-normal rank | 14.08 | 14.15 |
| 15 | Gemini 3.1 Flash-Lite | Avg piecewise-uniform rank | 13.92 | 14.23 |
| 15 | Gemini 3.1 Flash-Lite | Avg transformed-normal rank | 13.77 | 14.08 |
| 16 | GPT-5.5 | Avg piecewise-uniform rank | 15.08 | 15.31 |
| 16 | GPT-5.5 | Avg transformed-normal rank | 17.38 | 17.69 |
| 16 | GPT-5.5 | Rank shift | 2.31 | 2.38 |
| 17 | GPT-5.4 | Avg piecewise-uniform rank | 15.31 | 15.38 |
| 17 | GPT-5.4 | Avg transformed-normal rank | 16.77 | 17.0 |
| 17 | GPT-5.4 | Rank shift | 1.46 | 1.62 |
| 18 | GPT-5.6 Sol | Avg piecewise-uniform rank | 17.38 | 17.46 |
| 18 | GPT-5.6 Sol | Avg transformed-normal rank | 19.62 | 19.69 |
| 19 | Grok 4.3 | Avg piecewise-uniform rank | 18.69 | 18.85 |
| 19 | Grok 4.3 | Avg transformed-normal rank | 18.15 | 18.38 |
| 19 | Grok 4.3 | Rank shift | -0.54 | -0.46 |
| 21 | MiniMax M3 | Avg piecewise-uniform rank | 18.77 | 19.0 |
| 21 | MiniMax M3 | Rank shift | -4.92 | -5.15 |
| 22 | Kimi K3 | Avg transformed-normal rank | 18.46 | 18.54 |
| 22 | Kimi K3 | Rank shift | -0.31 | -0.23 |
| 23 | Grok 4.5 | Avg piecewise-uniform rank | 18.85 | 19.08 |
| 23 | Grok 4.5 | Avg transformed-normal rank | 19.08 | 19.31 |
| 24 | Grok 4.1 Fast | Avg transformed-normal rank | 17.31 | 17.46 |
| 24 | Grok 4.1 Fast | Rank shift | -1.88 | -1.73 |
| 25 | Qwen 3.8 Max | Avg piecewise-uniform rank | 19.38 | 19.46 |
| 25 | Qwen 3.8 Max | Avg transformed-normal rank | 18.15 | 18.23 |
| 26 | Qwen 3.7 Max | Avg piecewise-uniform rank | 20.31 | 20.54 |
| 26 | Qwen 3.7 Max | Avg transformed-normal rank | 17.85 | 18.0 |
| 26 | Qwen 3.7 Max | Rank shift | -2.46 | -2.54 |
| 27 | DeepSeek V4 Pro | Avg piecewise-uniform rank | 20.38 | 20.46 |
| 27 | DeepSeek V4 Pro | Avg transformed-normal rank | 16.62 | 16.69 |
| 29 | Kimi K2.6 | Avg piecewise-uniform rank | 22.69 | 22.54 |
| 29 | Kimi K2.6 | Avg transformed-normal rank | 19.31 | 18.69 |
| 29 | Kimi K2.6 | Rank shift | -3.38 | -3.85 |
| 31 | Grok 4.20 | Avg piecewise-uniform rank | 23.77 | 24.0 |
| 31 | Grok 4.20 | Avg transformed-normal rank | 23.08 | 23.31 |

## `paper/tables/quantity-disagreement.csv` (10 cells)

| line | row | column | old | new |
|---|---|---|---|---|
| 4 | Capital gains realizations elasticity / GPT-5.4 mini / Gemini 3.5 Flash | Highest model | Gemini 3.5 Flash | MiniMax M3 |
| 4 | Capital gains realizations elasticity / GPT-5.4 mini / Gemini 3.5 Flash | Highest center | 0.01 | -0.327 |
| 4 | Capital gains realizations elasticity / GPT-5.4 mini / Gemini 3.5 Flash | Spread | 0.94 | 0.603 |
| 4 | Capital gains realizations elasticity / GPT-5.4 mini / Gemini 3.5 Flash | Mean pooled 90% width | 1.894 | 1.797 |
| 4 | Capital gains realizations elasticity / GPT-5.4 mini / Gemini 3.5 Flash | Spread / mean width | 0.496 | 0.335 |
| 12 | Income elasticity of labor supply / Grok 4.20 / Gemini 3.5 Flash | Highest model | Gemini 3.5 Flash | GPT-5.4 nano |
| 12 | Income elasticity of labor supply / Grok 4.20 / Gemini 3.5 Flash | Highest center | 0.011 | -0.001 |
| 12 | Income elasticity of labor supply / Grok 4.20 / Gemini 3.5 Flash | Spread | 0.118 | 0.106 |
| 12 | Income elasticity of labor supply / Grok 4.20 / Gemini 3.5 Flash | Mean pooled 90% width | 0.377 | 0.373 |
| 12 | Income elasticity of labor supply / Grok 4.20 / Gemini 3.5 Flash | Spread / mean width | 0.312 | 0.284 |

## `paper/tables/resampling-stability.csv` (74 cells)

| line | row | column | old | new |
|---|---|---|---|---|
| 2 | Claude Fable 5 / 3% / [6.62, 8.08] | Avg width rank (mean) | 7.44 | 7.53 |
| 2 | Claude Fable 5 / 3% / [6.62, 8.08] | Avg width rank 90% interval | [6.62, 8.08] | [6.77, 8.16] |
| 3 | Gemini 3.6 Flash / 2% / [7.08, 8.54] | Avg width rank (mean) | 7.83 | 8.0 |
| 3 | Gemini 3.6 Flash / 2% / [7.08, 8.54] | Avg width rank 90% interval | [7.08, 8.54] | [7.30, 8.69] |
| 4 | Claude Haiku 4.5 / 5% / [8.31, 10.00] | Avg width rank (mean) | 9.2 | 9.3 |
| 4 | Claude Haiku 4.5 / 5% / [8.31, 10.00] | Avg width rank 90% interval | [8.31, 10.00] | [8.38, 10.08] |
| 5 | Claude Opus 4.7 / 2% / [9.15, 10.85] | Avg width rank (mean) | 10.07 | 10.25 |
| 5 | Claude Opus 4.7 / 2% / [9.15, 10.85] | Avg width rank 90% interval | [9.15, 10.85] | [9.31, 11.08] |
| 6 | Claude Sonnet 5 / 2% / [9.69, 11.08] | Avg width rank (mean) | 10.34 | 10.52 |
| 6 | Claude Sonnet 5 / 2% / [9.69, 11.08] | Avg width rank 90% interval | [9.69, 11.08] | [9.84, 11.31] |
| 7 | Gemini 3.1 Pro / 2% / [10.30, 11.69] | Avg width rank (mean) | 11.06 | 11.05 |
| 8 | Claude Opus 4.8 / 1% / [10.69, 12.08] | Model | Claude Opus 4.8 | Gemini 3.5 Flash |
| 8 | Claude Opus 4.8 / 1% / [10.69, 12.08] | Median center MC SE | 0.0 | 0.0038 |
| 8 | Claude Opus 4.8 / 1% / [10.69, 12.08] | Median relative width MC SE | 1% | 2% |
| 8 | Claude Opus 4.8 / 1% / [10.69, 12.08] | Avg width rank (mean) | 11.4 | 11.25 |
| 8 | Claude Opus 4.8 / 1% / [10.69, 12.08] | Avg width rank 90% interval | [10.69, 12.08] | [10.54, 11.85] |
| 9 | Inkling / 4% / [10.85, 13.39] | Model | Inkling | Claude Opus 4.8 |
| 9 | Inkling / 4% / [10.85, 13.39] | Median center MC SE | 0.0137 | 0.0 |
| 9 | Inkling / 4% / [10.85, 13.39] | Median relative width MC SE | 4% | 1% |
| 9 | Inkling / 4% / [10.85, 13.39] | Avg width rank (mean) | 12.37 | 11.57 |
| 9 | Inkling / 4% / [10.85, 13.39] | Avg width rank 90% interval | [10.85, 13.39] | [10.92, 12.23] |
| 10 | Gemini 3 Flash / 1% / [12.38, 13.77] | Model | Gemini 3 Flash | Inkling |
| 10 | Gemini 3 Flash / 1% / [12.38, 13.77] | Median center MC SE | 0.0 | 0.0137 |
| 10 | Gemini 3 Flash / 1% / [12.38, 13.77] | Median relative width MC SE | 1% | 4% |
| 10 | Gemini 3 Flash / 1% / [12.38, 13.77] | Avg width rank (mean) | 13.11 | 11.71 |
| 10 | Gemini 3 Flash / 1% / [12.38, 13.77] | Avg width rank 90% interval | [12.38, 13.77] | [10.46, 12.85] |
| 11 | Gemini 3.5 Flash / 3% / [12.84, 14.08] | Model | Gemini 3.5 Flash | Gemini 3 Flash |
| 11 | Gemini 3.5 Flash / 3% / [12.84, 14.08] | Median center MC SE | 0.0104 | 0.0 |
| 11 | Gemini 3.5 Flash / 3% / [12.84, 14.08] | Median relative width MC SE | 3% | 1% |
| 11 | Gemini 3.5 Flash / 3% / [12.84, 14.08] | Avg width rank (mean) | 13.48 | 13.21 |
| 11 | Gemini 3.5 Flash / 3% / [12.84, 14.08] | Avg width rank 90% interval | [12.84, 14.08] | [12.46, 13.92] |
| 12 | Claude Opus 5 / 3% / [12.85, 14.46] | Avg width rank (mean) | 13.67 | 13.78 |
| 12 | Claude Opus 5 / 3% / [12.85, 14.46] | Avg width rank 90% interval | [12.85, 14.46] | [13.00, 14.62] |
| 13 | GPT-5.6 Terra / 3% / [12.69, 14.69] | Avg width rank (mean) | 13.73 | 13.82 |
| 13 | GPT-5.6 Terra / 3% / [12.69, 14.69] | Avg width rank 90% interval | [12.69, 14.69] | [12.77, 14.85] |
| 14 | Gemini 3.1 Flash-Lite / 5% / [12.92, 14.85] | Avg width rank (mean) | 13.94 | 14.16 |
| 14 | Gemini 3.1 Flash-Lite / 5% / [12.92, 14.85] | Avg width rank 90% interval | [12.92, 14.85] | [13.08, 15.08] |
| 15 | Claude Sonnet 4.6 / 1% / [13.46, 15.23] | Avg width rank (mean) | 14.27 | 14.36 |
| 15 | Claude Sonnet 4.6 / 1% / [13.46, 15.23] | Avg width rank 90% interval | [13.46, 15.23] | [13.53, 15.38] |
| 16 | GPT-5.5 / 2% / [14.85, 16.00] | Model | GPT-5.5 | GPT-5.4 |
| 16 | GPT-5.5 / 2% / [14.85, 16.00] | Median center MC SE | 0.0047 | 0.0 |
| 16 | GPT-5.5 / 2% / [14.85, 16.00] | Median relative width MC SE | 2% | 3% |
| 16 | GPT-5.5 / 2% / [14.85, 16.00] | Avg width rank (mean) | 15.4 | 15.58 |
| 16 | GPT-5.5 / 2% / [14.85, 16.00] | Avg width rank 90% interval | [14.85, 16.00] | [14.62, 16.31] |
| 17 | GPT-5.4 / 3% / [14.54, 16.23] | Model | GPT-5.4 | GPT-5.5 |
| 17 | GPT-5.4 / 3% / [14.54, 16.23] | Median center MC SE | 0.0 | 0.0047 |
| 17 | GPT-5.4 / 3% / [14.54, 16.23] | Median relative width MC SE | 3% | 2% |
| 17 | GPT-5.4 / 3% / [14.54, 16.23] | Avg width rank (mean) | 15.49 | 15.59 |
| 17 | GPT-5.4 / 3% / [14.54, 16.23] | Avg width rank 90% interval | [14.54, 16.23] | [15.07, 16.23] |
| 18 | GPT-5.6 Sol / 3% / [16.69, 18.31] | Avg width rank (mean) | 17.57 | 17.67 |
| 18 | GPT-5.6 Sol / 3% / [16.69, 18.31] | Avg width rank 90% interval | [16.69, 18.31] | [16.77, 18.38] |
| 19 | MiniMax M3 / 9% / [16.38, 19.38] | Avg width rank (mean) | 18.04 | 18.18 |
| 19 | MiniMax M3 / 9% / [16.38, 19.38] | Avg width rank 90% interval | [16.38, 19.38] | [16.38, 19.62] |
| 20 | Kimi K3 / 3% / [17.69, 19.62] | Avg width rank (mean) | 18.69 | 18.74 |
| 20 | Kimi K3 / 3% / [17.69, 19.62] | Avg width rank 90% interval | [17.69, 19.62] | [17.77, 19.69] |
| 22 | Grok 4.1 Fast / 2% / [17.38, 20.15] | Avg width rank (mean) | 18.83 | 18.87 |
| 22 | Grok 4.1 Fast / 2% / [17.38, 20.15] | Avg width rank 90% interval | [17.38, 20.15] | [17.38, 20.16] |
| 23 | Qwen 3.8 Max / 7% / [17.76, 20.16] | Avg width rank (mean) | 19.04 | 19.13 |
| 23 | Qwen 3.8 Max / 7% / [17.76, 20.16] | Avg width rank 90% interval | [17.76, 20.16] | [17.84, 20.23] |
| 24 | Grok 4.5 / 3% / [18.08, 19.92] | Avg width rank (mean) | 19.05 | 19.21 |
| 24 | Grok 4.5 / 3% / [18.08, 19.92] | Avg width rank 90% interval | [18.08, 19.92] | [18.23, 20.00] |
| 25 | Grok 4.3 / 5% / [18.31, 20.23] | Avg width rank (mean) | 19.24 | 19.38 |
| 25 | Grok 4.3 / 5% / [18.31, 20.23] | Avg width rank 90% interval | [18.31, 20.23] | [18.46, 20.38] |
| 26 | Qwen 3.7 Max / 8% / [17.60, 20.77] | Avg width rank (mean) | 19.35 | 19.5 |
| 26 | Qwen 3.7 Max / 8% / [17.60, 20.77] | Avg width rank 90% interval | [17.60, 20.77] | [17.76, 20.93] |
| 27 | GLM-5.2 / 7% / [18.46, 21.31] | Avg width rank (mean) | 19.83 | 19.87 |
| 28 | DeepSeek V4 Pro / 7% / [18.62, 21.08] | Avg width rank (mean) | 19.88 | 19.98 |
| 28 | DeepSeek V4 Pro / 7% / [18.62, 21.08] | Avg width rank 90% interval | [18.62, 21.08] | [18.69, 21.15] |
| 29 | Kimi K2.6 / 5% / [20.15, 22.92] | Median relative width MC SE | 5% | 4% |
| 29 | Kimi K2.6 / 5% / [20.15, 22.92] | Avg width rank (mean) | 21.69 | 21.6 |
| 29 | Kimi K2.6 / 5% / [20.15, 22.92] | Avg width rank 90% interval | [20.15, 22.92] | [20.15, 22.77] |
| 30 | GPT-5.4 mini / 4% / [22.07, 23.77] | Avg width rank (mean) | 22.98 | 22.99 |
| 31 | Grok 4.20 / 3% / [23.30, 24.77] | Avg width rank (mean) | 24.1 | 24.27 |
| 31 | Grok 4.20 / 3% / [23.30, 24.77] | Avg width rank 90% interval | [23.30, 24.77] | [23.46, 25.00] |

## `paper/tables/stability-appendix.csv` (5 cells)

| line | row | column | old | new |
|---|---|---|---|---|
| 2 | (row) | 90th pct abs change in pooled center | 0.048 | 0.0433 |
| 2 | (row) | 90th pct abs change in pooled width | 0.2687 | 0.249 |
| 3 | (row) | Median abs change in pooled center | 0.0027 | 0.0023 |
| 3 | (row) | 90th pct abs change in pooled center | 0.025 | 0.0233 |
| 3 | (row) | 90th pct abs change in pooled width | 0.1339 | 0.1296 |

## `paper/tables/variance-decomposition.csv` (47 cells)

| line | row | column | old | new |
|---|---|---|---|---|
| 2 | Claude Fable 5 / 0% / 1% | Median between-run SD | 0.012 | 0.014 |
| 2 | Claude Fable 5 / 0% / 1% | Max between-run variance share | 1% | 0% |
| 3 | Claude Haiku 4.5 / 0% / 4% | Median between-run SD | 0.018 | 0.026 |
| 3 | Claude Haiku 4.5 / 0% / 4% | Max between-run variance share | 4% | 3% |
| 4 | Claude Opus 4.7 / 0% / 0% | Median between-run SD | 0.0 | 0.008 |
| 5 | Claude Opus 4.8 / 0% / 1% | Median between-run SD | 0.0 | 0.015 |
| 6 | Claude Opus 5 / 0% / 1% | Median between-run SD | 0.029 | 0.031 |
| 7 | Claude Sonnet 4.6 / 0% / 1% | Median between-run SD | 0.0 | 0.004 |
| 8 | Claude Sonnet 5 / 0% / 1% | Median between-run SD | 0.01 | 0.026 |
| 9 | DeepSeek V4 Pro / 1% / 4% | Median between-run SD | 0.054 | 0.069 |
| 9 | DeepSeek V4 Pro / 1% / 4% | Max between-run variance share | 4% | 5% |
| 10 | GLM-5.2 / 1% / 13% | Median between-run SD | 0.06 | 0.058 |
| 11 | GPT-5.4 / 0% / 1% | Median between-run SD | 0.0 | 0.011 |
| 12 | GPT-5.4 mini / 1% / 5% | Median between-run SD | 0.034 | 0.062 |
| 13 | GPT-5.4 nano / 2% / 29% | Median between-run SD | 0.098 | 0.088 |
| 13 | GPT-5.4 nano / 2% / 29% | Max between-run variance share | 29% | 27% |
| 14 | GPT-5.5 / 0% / 1% | Median between-run SD | 0.018 | 0.025 |
| 15 | GPT-5.6 Luna / 0% / 5% | Median between-run SD | 0.051 | 0.057 |
| 15 | GPT-5.6 Luna / 0% / 5% | Median between-run variance share | 0% | 1% |
| 16 | GPT-5.6 Sol / 0% / 1% | Median between-run SD | 0.036 | 0.035 |
| 17 | GPT-5.6 Terra / 0% / 2% | Median between-run SD | 0.014 | 0.024 |
| 17 | GPT-5.6 Terra / 0% / 2% | Max between-run variance share | 2% | 1% |
| 18 | Gemini 3 Flash / 0% / 1% | Median between-run SD | 0.0 | 0.011 |
| 19 | Gemini 3.1 Flash-Lite / 0% / 3% | Median between-run SD | 0.025 | 0.035 |
| 20 | Gemini 3.1 Pro / 0% / 3% | Median between-run SD | 0.025 | 0.026 |
| 21 | Gemini 3.5 Flash / 0% / 25% | Median between-run SD | 0.041 | 0.032 |
| 21 | Gemini 3.5 Flash / 0% / 25% | Max between-run variance share | 25% | 1% |
| 22 | Gemini 3.6 Flash / 0% / 3% | Median between-run SD | 0.022 | 0.028 |
| 22 | Gemini 3.6 Flash / 0% / 3% | Max between-run variance share | 3% | 2% |
| 23 | Grok 4.1 Fast / 0% / 4% | Median between-run SD | 0.0 | 0.029 |
| 24 | Grok 4.20 / 0% / 7% | Median between-run SD | 0.042 | 0.055 |
| 24 | Grok 4.20 / 0% / 7% | Max between-run variance share | 7% | 6% |
| 25 | Grok 4.3 / 0% / 6% | Median between-run SD | 0.046 | 0.049 |
| 25 | Grok 4.3 / 0% / 6% | Max between-run variance share | 6% | 5% |
| 26 | Grok 4.5 / 0% / 4% | Median between-run SD | 0.034 | 0.041 |
| 26 | Grok 4.5 / 0% / 4% | Max between-run variance share | 4% | 3% |
| 27 | Inkling / 1% / 9% | Median between-run SD | 0.053 | 0.045 |
| 27 | Inkling / 1% / 9% | Median between-run variance share | 1% | 0% |
| 27 | Inkling / 1% / 9% | Max between-run variance share | 9% | 3% |
| 28 | Kimi K2.6 / 1% / 6% | Median between-run SD | 0.1 | 0.103 |
| 28 | Kimi K2.6 / 1% / 6% | Max between-run variance share | 6% | 4% |
| 29 | Kimi K3 / 0% / 2% | Median between-run SD | 0.034 | 0.048 |
| 30 | MiniMax M3 / 1% / 37% | Median between-run SD | 0.062 | 0.071 |
| 30 | MiniMax M3 / 1% / 37% | Max between-run variance share | 37% | 33% |
| 31 | Qwen 3.7 Max / 0% / 18% | Median between-run SD | 0.048 | 0.058 |
| 31 | Qwen 3.7 Max / 0% / 18% | Max between-run variance share | 18% | 16% |
| 32 | Qwen 3.8 Max / 0% / 15% | Median between-run SD | 0.06 | 0.071 |

## `paper/tables/wording-comparison.csv` (1 cells)

| line | row | column | old | new |
|---|---|---|---|---|
| 10 | Gemini 3.1 Pro / Capital gains realizations elasticity (net-of-tax-rate convention) | Original 90% width | 4.832 | 4.793 |

## `results/claude-fable-5-armington-clarify-batch15/summary.csv` (2 cells)

| line | row | column | old | new |
|---|---|---|---|---|
| 2 | claude-fable-5 / trade.armington_elasticity.import_domestic / Armington elasticity | between_run_sd | 0.0 | 0.04092540639857954 |
| 2 | claude-fable-5 / trade.armington_elasticity.import_domestic / Armington elasticity | total_sd | 2.5159803423980347 | 2.516313170537845 |

## `results/claude-fable-5-elasticities-batch15/summary.csv` (50 cells)

| line | row | column | old | new |
|---|---|---|---|---|
| 2 | claude-fable-5 / household.annual_discount_factor / Annual discount factor | between_run_sd | 0.004988876515698593 | 0.005147504789269829 |
| 2 | claude-fable-5 / household.annual_discount_factor / Annual discount factor | total_sd | 0.12616937607174467 | 0.12617574796687359 |
| 3 | claude-fable-5 / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | between_run_sd | 0.0 | 0.017293222821543584 |
| 3 | claude-fable-5 / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | total_sd | 0.729562464007633 | 0.7297673906420075 |
| 5 | claude-fable-5 / labor_supply.extensive_margin.single_mothers / Employment participation elasticity of single mothers | between_run_sd | 0.04988876515698587 | 0.04355504180536007 |
| 5 | claude-fable-5 / labor_supply.extensive_margin.single_mothers / Employment participation elasticity of single mothers | total_sd | 0.6805605838816506 | 0.6801256215664214 |
| 6 | claude-fable-5 / labor_supply.frisch_elasticity.prime_age / Frisch elasticity of labor supply | between_run_sd | 0.012472191289246468 | 0.013641379044005158 |
| 6 | claude-fable-5 / labor_supply.frisch_elasticity.prime_age / Frisch elasticity of labor supply | total_sd | 1.2622482592800657 | 1.26226035338286 |
| 7 | claude-fable-5 / labor_supply.income_elasticity.prime_age / Income elasticity of labor supply | between_run_sd | 0.01569146972791976 | 0.013675708391158385 |
| 7 | claude-fable-5 / labor_supply.income_elasticity.prime_age / Income elasticity of labor supply | total_sd | 0.3048895565063957 | 0.3047924612657676 |
| 8 | claude-fable-5 / labor_supply.marshallian_wage_elasticity.prime_age / Uncompensated wage elasticity of labor supply | between_run_sd | 0.008000000000000002 | 0.007577305296446466 |
| 8 | claude-fable-5 / labor_supply.marshallian_wage_elasticity.prime_age / Uncompensated wage elasticity of labor supply | total_sd | 0.5945244166091452 | 0.5945188790105829 |
| 9 | claude-fable-5 / labor_supply.policy_response.substitution_elasticity.all / Substitution elasticity of labor supply in a tax-benefit simulation | between_run_sd | 0.0 | 0.005916924876994808 |
| 9 | claude-fable-5 / labor_supply.policy_response.substitution_elasticity.all / Substitution elasticity of labor supply in a tax-benefit simulation | total_sd | 0.6289393629136455 | 0.6289671948696707 |
| 10 | claude-fable-5 / labor_supply.policy_response.substitution_elasticity.primary.decile_1 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 1 | between_run_sd | 0.0040000000000000036 | 0.004159126510859386 |
| 10 | claude-fable-5 / labor_supply.policy_response.substitution_elasticity.primary.decile_1 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 1 | total_sd | 0.6181007536532104 | 0.6181018039125917 |
| 11 | claude-fable-5 / labor_supply.policy_response.substitution_elasticity.primary.decile_10 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 10 | between_run_sd | 0.029769484749021476 | 0.023326213199364842 |
| 11 | claude-fable-5 / labor_supply.policy_response.substitution_elasticity.primary.decile_10 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 10 | total_sd | 0.6293931777690495 | 0.6291213414137389 |
| 12 | claude-fable-5 / labor_supply.policy_response.substitution_elasticity.primary.decile_2 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 2 | between_run_sd | 0.014142135623730942 | 0.015175821412877637 |
| 12 | claude-fable-5 / labor_supply.policy_response.substitution_elasticity.primary.decile_2 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 2 | total_sd | 0.6192608721514526 | 0.6192853408028752 |
| 13 | claude-fable-5 / labor_supply.policy_response.substitution_elasticity.primary.decile_3 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 3 | between_run_sd | 0.01024152766382482 | 0.008604585340903356 |
| 13 | claude-fable-5 / labor_supply.policy_response.substitution_elasticity.primary.decile_3 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 3 | total_sd | 0.6174959873913712 | 0.6174710069666789 |
| 14 | claude-fable-5 / labor_supply.policy_response.substitution_elasticity.primary.decile_4 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 4 | between_run_sd | 0.045528989543903664 | 0.038859447585711596 |
| 14 | claude-fable-5 / labor_supply.policy_response.substitution_elasticity.primary.decile_4 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 4 | total_sd | 0.6268372108361858 | 0.6263881038674559 |
| 15 | claude-fable-5 / labor_supply.policy_response.substitution_elasticity.primary.decile_5 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 5 | between_run_sd | 0.03343982987729188 | 0.02899810338625614 |
| 15 | claude-fable-5 / labor_supply.policy_response.substitution_elasticity.primary.decile_5 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 5 | total_sd | 0.6293307015746527 | 0.629110323967285 |
| 16 | claude-fable-5 / labor_supply.policy_response.substitution_elasticity.primary.decile_6 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 6 | between_run_sd | 0.03116978594016256 | 0.025668993401031945 |
| 16 | claude-fable-5 / labor_supply.policy_response.substitution_elasticity.primary.decile_6 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 6 | total_sd | 0.6273208398507985 | 0.6270715890373106 |
| 17 | claude-fable-5 / labor_supply.policy_response.substitution_elasticity.primary.decile_7 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 7 | between_run_sd | 0.045382326466980025 | 0.03702512660342973 |
| 17 | claude-fable-5 / labor_supply.policy_response.substitution_elasticity.primary.decile_7 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 7 | total_sd | 0.6284921682531578 | 0.6279440341304311 |
| 18 | claude-fable-5 / labor_supply.policy_response.substitution_elasticity.primary.decile_8 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 8 | between_run_sd | 0.0332398689661811 | 0.02803373959277562 |
| 18 | claude-fable-5 / labor_supply.policy_response.substitution_elasticity.primary.decile_8 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 8 | total_sd | 0.627634109175083 | 0.6273799300795864 |
| 19 | claude-fable-5 / labor_supply.policy_response.substitution_elasticity.primary.decile_9 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 9 | between_run_sd | 0.040966110655299245 | 0.03361681953361375 |
| 19 | claude-fable-5 / labor_supply.policy_response.substitution_elasticity.primary.decile_9 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 9 | total_sd | 0.6292311059715836 | 0.6287953984052012 |
| 20 | claude-fable-5 / labor_supply.policy_response.substitution_elasticity.secondary / Secondary-earner substitution elasticity in a tax-benefit simulation | between_run_sd | 0.03399346342395191 | 0.034822151315250786 |
| 20 | claude-fable-5 / labor_supply.policy_response.substitution_elasticity.secondary / Secondary-earner substitution elasticity in a tax-benefit simulation | total_sd | 0.6257690734874434 | 0.6258146370931251 |
| 21 | claude-fable-5 / macro.tfp_persistence.ar1 / TFP persistence | between_run_sd | 0.0 | 0.001444722195517975 |
| 21 | claude-fable-5 / macro.tfp_persistence.ar1 / TFP persistence | total_sd | 0.12741381618786699 | 0.1274220066463316 |
| 22 | claude-fable-5 / production.capital_labor_substitution / Elasticity of substitution between capital and labor | between_run_sd | 0.0339934634239519 | 0.02673428925971708 |
| 22 | claude-fable-5 / production.capital_labor_substitution / Elasticity of substitution between capital and labor | total_sd | 1.24624785467329 | 1.2460709778918873 |
| 23 | claude-fable-5 / production.capital_share / Capital share in production | between_run_sd | 0.005734883511361733 | 0.003544792738025119 |
| 23 | claude-fable-5 / production.capital_share / Capital share in production | total_sd | 0.10746891023299095 | 0.10737431412276091 |
| 24 | claude-fable-5 / tax.capital_gains_realizations.elasticity / Capital gains realizations elasticity | between_run_sd | 0.012472191289246483 | 0.026617141511105603 |
| 24 | claude-fable-5 / tax.capital_gains_realizations.elasticity / Capital gains realizations elasticity | total_sd | 1.3132570700150237 | 1.3134675666384423 |
| 25 | claude-fable-5 / tax.capital_gains_realizations.elasticity.net_of_tax_rate / Capital gains realizations elasticity (net-of-tax-rate convention) | between_run_sd | 0.20612833111653744 | 0.18905613510865543 |
| 25 | claude-fable-5 / tax.capital_gains_realizations.elasticity.net_of_tax_rate / Capital gains realizations elasticity (net-of-tax-rate convention) | total_sd | 1.5892073495928716 | 1.5870832786383118 |
| 26 | claude-fable-5 / tax.elasticity_of_taxable_income.top_earners / Elasticity of taxable income | between_run_sd | 0.03858612300930074 | 0.03829771533655761 |
| 26 | claude-fable-5 / tax.elasticity_of_taxable_income.top_earners / Elasticity of taxable income | total_sd | 0.6777001354663514 | 0.6776837756079322 |
| 27 | claude-fable-5 / trade.armington_elasticity.import_domestic / Armington elasticity | between_run_sd | 0.04988876515698587 | 0.06570768600399797 |
| 27 | claude-fable-5 / trade.armington_elasticity.import_domestic / Armington elasticity | total_sd | 2.566461815418262 | 2.5668180420729305 |

## `results/claude-fable-5-ies-clarify-batch15/summary.csv` (2 cells)

| line | row | column | old | new |
|---|---|---|---|---|
| 2 | claude-fable-5 / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | between_run_sd | 0.024944382578492935 | 0.03517653889865926 |
| 2 | claude-fable-5 / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | total_sd | 0.682510683677064 | 0.6829611994835432 |

## `results/claude-haiku-4.5-armington-clarify-batch15/summary.csv` (2 cells)

| line | row | column | old | new |
|---|---|---|---|---|
| 2 | claude-haiku-4.5 / trade.armington_elasticity.import_domestic / Armington elasticity | between_run_sd | 0.294089933334837 | 0.2847758133846498 |
| 2 | claude-haiku-4.5 / trade.armington_elasticity.import_domestic / Armington elasticity | total_sd | 2.4886858563640906 | 2.4876023932024722 |

## `results/claude-haiku-4.5-elasticities-batch15/summary.csv` (52 cells)

| line | row | column | old | new |
|---|---|---|---|---|
| 2 | claude-haiku-4.5 / household.annual_discount_factor / Annual discount factor | between_run_sd | 0.0 | 0.000820145651021119 |
| 2 | claude-haiku-4.5 / household.annual_discount_factor / Annual discount factor | total_sd | 0.1253567160147393 | 0.12535939888532047 |
| 3 | claude-haiku-4.5 / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | between_run_sd | 0.0 | 0.014002975874196655 |
| 3 | claude-haiku-4.5 / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | total_sd | 0.6437748916438969 | 0.6439271654810382 |
| 4 | claude-haiku-4.5 / household.relative_risk_aversion.crra / Coefficient of relative risk aversion | between_run_sd | 0.1699673171197595 | 0.19136962489729997 |
| 4 | claude-haiku-4.5 / household.relative_risk_aversion.crra / Coefficient of relative risk aversion | total_sd | 6.275135578437949 | 6.275751745585721 |
| 5 | claude-haiku-4.5 / labor_supply.extensive_margin.single_mothers / Employment participation elasticity of single mothers | between_run_sd | 0.09428090415820635 | 0.09110684508982969 |
| 5 | claude-haiku-4.5 / labor_supply.extensive_margin.single_mothers / Employment participation elasticity of single mothers | total_sd | 0.678891017681696 | 0.6784575021489719 |
| 6 | claude-haiku-4.5 / labor_supply.frisch_elasticity.prime_age / Frisch elasticity of labor supply | between_run_sd | 0.08881941729649484 | 0.08588390743064474 |
| 6 | claude-haiku-4.5 / labor_supply.frisch_elasticity.prime_age / Frisch elasticity of labor supply | total_sd | 1.269634240856616 | 1.2694322598005072 |
| 7 | claude-haiku-4.5 / labor_supply.income_elasticity.prime_age / Income elasticity of labor supply | between_run_sd | 0.018427033281447004 | 0.018032578542429505 |
| 7 | claude-haiku-4.5 / labor_supply.income_elasticity.prime_age / Income elasticity of labor supply | total_sd | 0.30482875201587456 | 0.3048051613553958 |
| 8 | claude-haiku-4.5 / labor_supply.marshallian_wage_elasticity.prime_age / Uncompensated wage elasticity of labor supply | between_run_sd | 0.018499249234015476 | 0.019750203937062415 |
| 8 | claude-haiku-4.5 / labor_supply.marshallian_wage_elasticity.prime_age / Uncompensated wage elasticity of labor supply | total_sd | 0.5924334995498557 | 0.5924738810464325 |
| 9 | claude-haiku-4.5 / labor_supply.policy_response.substitution_elasticity.all / Substitution elasticity of labor supply in a tax-benefit simulation | between_run_sd | 0.0073029674334022165 | 0.009008730333527712 |
| 9 | claude-haiku-4.5 / labor_supply.policy_response.substitution_elasticity.all / Substitution elasticity of labor supply in a tax-benefit simulation | total_sd | 0.6396295770470073 | 0.6396513266790137 |
| 10 | claude-haiku-4.5 / labor_supply.policy_response.substitution_elasticity.primary.decile_1 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 1 | between_run_sd | 0.049888765156985884 | 0.048672020253484 |
| 10 | claude-haiku-4.5 / labor_supply.policy_response.substitution_elasticity.primary.decile_1 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 1 | total_sd | 0.643892912939204 | 0.6437997825411251 |
| 11 | claude-haiku-4.5 / labor_supply.policy_response.substitution_elasticity.primary.decile_10 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 10 | between_run_sd | 0.030912061651652344 | 0.031897997150639755 |
| 11 | claude-haiku-4.5 / labor_supply.policy_response.substitution_elasticity.primary.decile_10 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 10 | total_sd | 0.6445952433719766 | 0.6446432768938527 |
| 12 | claude-haiku-4.5 / labor_supply.policy_response.substitution_elasticity.primary.decile_2 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 2 | between_run_sd | 0.03496029493900505 | 0.037679179337607074 |
| 12 | claude-haiku-4.5 / labor_supply.policy_response.substitution_elasticity.primary.decile_2 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 2 | total_sd | 0.6422929605890308 | 0.6424466869363991 |
| 13 | claude-haiku-4.5 / labor_supply.policy_response.substitution_elasticity.primary.decile_3 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 3 | between_run_sd | 0.0436959189551305 | 0.04546064842867462 |
| 13 | claude-haiku-4.5 / labor_supply.policy_response.substitution_elasticity.primary.decile_3 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 3 | total_sd | 0.6424236541324493 | 0.6425460984327204 |
| 14 | claude-haiku-4.5 / labor_supply.policy_response.substitution_elasticity.primary.decile_4 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 4 | between_run_sd | 0.024997777679003567 | 0.02830678167663871 |
| 14 | claude-haiku-4.5 / labor_supply.policy_response.substitution_elasticity.primary.decile_4 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 4 | total_sd | 0.6424338800824392 | 0.6425711441371903 |
| 15 | claude-haiku-4.5 / labor_supply.policy_response.substitution_elasticity.primary.decile_5 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 5 | between_run_sd | 0.0 | 0.005477884831047672 |
| 15 | claude-haiku-4.5 / labor_supply.policy_response.substitution_elasticity.primary.decile_5 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 5 | total_sd | 0.6436613132005925 | 0.6436846225701942 |
| 16 | claude-haiku-4.5 / labor_supply.policy_response.substitution_elasticity.primary.decile_6 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 6 | between_run_sd | 0.025525586292102196 | 0.025848307488112256 |
| 16 | claude-haiku-4.5 / labor_supply.policy_response.substitution_elasticity.primary.decile_6 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 6 | total_sd | 0.6422797990578388 | 0.642292705643013 |
| 17 | claude-haiku-4.5 / labor_supply.policy_response.substitution_elasticity.primary.decile_7 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 7 | between_run_sd | 0.050552502960343665 | 0.0509509131964831 |
| 17 | claude-haiku-4.5 / labor_supply.policy_response.substitution_elasticity.primary.decile_7 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 7 | total_sd | 0.6429330911706305 | 0.6429645400192939 |
| 18 | claude-haiku-4.5 / labor_supply.policy_response.substitution_elasticity.primary.decile_8 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 8 | between_run_sd | 0.039474323581566564 | 0.04262636768740943 |
| 18 | claude-haiku-4.5 / labor_supply.policy_response.substitution_elasticity.primary.decile_8 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 8 | total_sd | 0.6418380139187077 | 0.6420395790845851 |
| 19 | claude-haiku-4.5 / labor_supply.policy_response.substitution_elasticity.primary.decile_9 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 9 | between_run_sd | 0.028472208672083495 | 0.032186850317067896 |
| 19 | claude-haiku-4.5 / labor_supply.policy_response.substitution_elasticity.primary.decile_9 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 9 | total_sd | 0.6413319852290058 | 0.641507632023536 |
| 20 | claude-haiku-4.5 / labor_supply.policy_response.substitution_elasticity.secondary / Secondary-earner substitution elasticity in a tax-benefit simulation | between_run_sd | 0.0793025150224688 | 0.077592632811799 |
| 20 | claude-haiku-4.5 / labor_supply.policy_response.substitution_elasticity.secondary / Secondary-earner substitution elasticity in a tax-benefit simulation | total_sd | 0.6477041891686873 | 0.6474970613403929 |
| 21 | claude-haiku-4.5 / macro.tfp_persistence.ar1 / TFP persistence | between_run_sd | 0.027968235951204068 | 0.02637683116339457 |
| 21 | claude-haiku-4.5 / macro.tfp_persistence.ar1 / TFP persistence | total_sd | 0.1414405548474537 | 0.14113449456300736 |
| 22 | claude-haiku-4.5 / production.capital_labor_substitution / Elasticity of substitution between capital and labor | between_run_sd | 0.016996731711975965 | 0.016226692686914238 |
| 22 | claude-haiku-4.5 / production.capital_labor_substitution / Elasticity of substitution between capital and labor | total_sd | 1.2269627218596877 | 1.2269522963424455 |
| 23 | claude-haiku-4.5 / production.capital_share / Capital share in production | between_run_sd | 0.014452988925785868 | 0.014674089030971865 |
| 23 | claude-haiku-4.5 / production.capital_share / Capital share in production | total_sd | 0.10761471269714419 | 0.10764463009778466 |
| 24 | claude-haiku-4.5 / tax.capital_gains_realizations.elasticity / Capital gains realizations elasticity | between_run_sd | 0.034960294939005085 | 0.03615014983832479 |
| 24 | claude-haiku-4.5 / tax.capital_gains_realizations.elasticity / Capital gains realizations elasticity | total_sd | 1.329104387255652 | 1.329136216997089 |
| 25 | claude-haiku-4.5 / tax.capital_gains_realizations.elasticity.net_of_tax_rate / Capital gains realizations elasticity (net-of-tax-rate convention) | between_run_sd | 0.20401524997465806 | 0.22173692495587852 |
| 25 | claude-haiku-4.5 / tax.capital_gains_realizations.elasticity.net_of_tax_rate / Capital gains realizations elasticity (net-of-tax-rate convention) | total_sd | 1.3698192931307887 | 1.3725705582956382 |
| 26 | claude-haiku-4.5 / tax.elasticity_of_taxable_income.top_earners / Elasticity of taxable income | between_run_sd | 0.10292176100751914 | 0.10183265138887865 |
| 26 | claude-haiku-4.5 / tax.elasticity_of_taxable_income.top_earners / Elasticity of taxable income | total_sd | 0.6959307117490616 | 0.6957704762028607 |
| 27 | claude-haiku-4.5 / trade.armington_elasticity.import_domestic / Armington elasticity | between_run_sd | 0.0 | 0.029309649529729188 |
| 27 | claude-haiku-4.5 / trade.armington_elasticity.import_domestic / Armington elasticity | total_sd | 2.4920510573064556 | 2.4922234104866643 |

## `results/claude-haiku-4.5-ies-clarify-batch15/summary.csv` (2 cells)

| line | row | column | old | new |
|---|---|---|---|---|
| 2 | claude-haiku-4.5 / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | between_run_sd | 0.0 | 0.016017351702311944 |
| 2 | claude-haiku-4.5 / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | total_sd | 0.6462583547708387 | 0.6464568173255401 |

## `results/claude-opus-4.7-armington-clarify-batch15/summary.csv` (2 cells)

| line | row | column | old | new |
|---|---|---|---|---|
| 2 | claude-opus-4.7 / trade.armington_elasticity.import_domestic / Armington elasticity | between_run_sd | 0.0 | 0.06246143254485568 |
| 2 | claude-opus-4.7 / trade.armington_elasticity.import_domestic / Armington elasticity | total_sd | 2.5811021951225928 | 2.5818578528304426 |

## `results/claude-opus-4.7-elasticities-batch15/summary.csv` (52 cells)

| line | row | column | old | new |
|---|---|---|---|---|
| 2 | claude-opus-4.7 / household.annual_discount_factor / Annual discount factor | between_run_sd | 0.0 | 0.0011022703842524719 |
| 2 | claude-opus-4.7 / household.annual_discount_factor / Annual discount factor | total_sd | 0.12574271019294386 | 0.12574754139412295 |
| 3 | claude-opus-4.7 / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | between_run_sd | 0.0 | 0.010817295821455984 |
| 3 | claude-opus-4.7 / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | total_sd | 0.7917975768956216 | 0.791871464738228 |
| 4 | claude-opus-4.7 / household.relative_risk_aversion.crra / Coefficient of relative risk aversion | between_run_sd | 0.0 | 0.08249579113843067 |
| 4 | claude-opus-4.7 / household.relative_risk_aversion.crra / Coefficient of relative risk aversion | total_sd | 6.335042258475209 | 6.335579371472054 |
| 5 | claude-opus-4.7 / labor_supply.extensive_margin.single_mothers / Employment participation elasticity of single mothers | between_run_sd | 0.0 | 0.017676883838002148 |
| 5 | claude-opus-4.7 / labor_supply.extensive_margin.single_mothers / Employment participation elasticity of single mothers | total_sd | 0.7035410189020807 | 0.7037630549410789 |
| 6 | claude-opus-4.7 / labor_supply.frisch_elasticity.prime_age / Frisch elasticity of labor supply | between_run_sd | 0.0649786289653931 | 0.06559100971593253 |
| 6 | claude-opus-4.7 / labor_supply.frisch_elasticity.prime_age / Frisch elasticity of labor supply | total_sd | 1.2783986429427159 | 1.2784299154083931 |
| 7 | claude-opus-4.7 / labor_supply.income_elasticity.prime_age / Income elasticity of labor supply | between_run_sd | 0.0 | 0.0007168604389202143 |
| 7 | claude-opus-4.7 / labor_supply.income_elasticity.prime_age / Income elasticity of labor supply | total_sd | 0.29968193787562325 | 0.2996827952648897 |
| 8 | claude-opus-4.7 / labor_supply.marshallian_wage_elasticity.prime_age / Uncompensated wage elasticity of labor supply | between_run_sd | 0.0 | 0.0031642095730564854 |
| 8 | claude-opus-4.7 / labor_supply.marshallian_wage_elasticity.prime_age / Uncompensated wage elasticity of labor supply | total_sd | 0.5982118771806525 | 0.5982202455803567 |
| 9 | claude-opus-4.7 / labor_supply.policy_response.substitution_elasticity.all / Substitution elasticity of labor supply in a tax-benefit simulation | between_run_sd | 0.0 | 0.009871198283671327 |
| 9 | claude-opus-4.7 / labor_supply.policy_response.substitution_elasticity.all / Substitution elasticity of labor supply in a tax-benefit simulation | total_sd | 0.6399045425773371 | 0.6399806748384412 |
| 10 | claude-opus-4.7 / labor_supply.policy_response.substitution_elasticity.primary.decile_1 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 1 | between_run_sd | 0.023151673805580447 | 0.023947280058959138 |
| 10 | claude-opus-4.7 / labor_supply.policy_response.substitution_elasticity.primary.decile_1 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 1 | total_sd | 0.6517609639788706 | 0.6517897102508514 |
| 11 | claude-opus-4.7 / labor_supply.policy_response.substitution_elasticity.primary.decile_10 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 10 | between_run_sd | 0.03440930106817051 | 0.03402602761939094 |
| 11 | claude-opus-4.7 / labor_supply.policy_response.substitution_elasticity.primary.decile_10 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 10 | total_sd | 0.6361296535385779 | 0.6361090367748808 |
| 12 | claude-opus-4.7 / labor_supply.policy_response.substitution_elasticity.primary.decile_2 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 2 | between_run_sd | 0.013266499161421598 | 0.014188669188240783 |
| 12 | claude-opus-4.7 / labor_supply.policy_response.substitution_elasticity.primary.decile_2 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 2 | total_sd | 0.6489399026275254 | 0.6489594097904394 |
| 13 | claude-opus-4.7 / labor_supply.policy_response.substitution_elasticity.primary.decile_3 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 3 | between_run_sd | 0.020396078054371138 | 0.02421173957677007 |
| 13 | claude-opus-4.7 / labor_supply.policy_response.substitution_elasticity.primary.decile_3 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 3 | total_sd | 0.6385857529642271 | 0.6387190088154745 |
| 14 | claude-opus-4.7 / labor_supply.policy_response.substitution_elasticity.primary.decile_4 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 4 | between_run_sd | 0.0 | 0.0034742705069633613 |
| 14 | claude-opus-4.7 / labor_supply.policy_response.substitution_elasticity.primary.decile_4 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 4 | total_sd | 0.6360526816930252 | 0.6360621702667472 |
| 15 | claude-opus-4.7 / labor_supply.policy_response.substitution_elasticity.primary.decile_5 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 5 | between_run_sd | 0.0 | 0.0040900964400474565 |
| 15 | claude-opus-4.7 / labor_supply.policy_response.substitution_elasticity.primary.decile_5 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 5 | total_sd | 0.636800015485413 | 0.6368131504696736 |
| 16 | claude-opus-4.7 / labor_supply.policy_response.substitution_elasticity.primary.decile_6 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 6 | between_run_sd | 0.0 | 0.004930066485916329 |
| 16 | claude-opus-4.7 / labor_supply.policy_response.substitution_elasticity.primary.decile_6 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 6 | total_sd | 0.6364554350725063 | 0.6364745292538334 |
| 17 | claude-opus-4.7 / labor_supply.policy_response.substitution_elasticity.primary.decile_7 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 7 | between_run_sd | 0.0 | 0.0036364665389480456 |
| 17 | claude-opus-4.7 / labor_supply.policy_response.substitution_elasticity.primary.decile_7 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 7 | total_sd | 0.6346185523166215 | 0.6346289710006418 |
| 18 | claude-opus-4.7 / labor_supply.policy_response.substitution_elasticity.primary.decile_8 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 8 | between_run_sd | 0.0 | 0.0030982073669928757 |
| 18 | claude-opus-4.7 / labor_supply.policy_response.substitution_elasticity.primary.decile_8 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 8 | total_sd | 0.6298543261915585 | 0.6298619460731939 |
| 19 | claude-opus-4.7 / labor_supply.policy_response.substitution_elasticity.primary.decile_9 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 9 | between_run_sd | 0.0 | 0.0028143481581985445 |
| 19 | claude-opus-4.7 / labor_supply.policy_response.substitution_elasticity.primary.decile_9 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 9 | total_sd | 0.6307709282210847 | 0.6307772066621022 |
| 20 | claude-opus-4.7 / labor_supply.policy_response.substitution_elasticity.secondary / Secondary-earner substitution elasticity in a tax-benefit simulation | between_run_sd | 0.0024944382578492965 | 0.014919469010509579 |
| 20 | claude-opus-4.7 / labor_supply.policy_response.substitution_elasticity.secondary / Secondary-earner substitution elasticity in a tax-benefit simulation | total_sd | 0.6358054526434255 | 0.635975582820948 |
| 21 | claude-opus-4.7 / macro.tfp_persistence.ar1 / TFP persistence | between_run_sd | 0.0 | 0.0029124254878403464 |
| 21 | claude-opus-4.7 / macro.tfp_persistence.ar1 / TFP persistence | total_sd | 0.1315205307166908 | 0.13155277352538874 |
| 22 | claude-opus-4.7 / production.capital_labor_substitution / Elasticity of substitution between capital and labor | between_run_sd | 0.0 | 0.0015590239111557757 |
| 22 | claude-opus-4.7 / production.capital_labor_substitution / Elasticity of substitution between capital and labor | total_sd | 1.2390560503194896 | 1.2390570311284663 |
| 23 | claude-opus-4.7 / production.capital_share / Capital share in production | between_run_sd | 0.0 | 0.0015732132722552342 |
| 23 | claude-opus-4.7 / production.capital_share / Capital share in production | total_sd | 0.11200429679257845 | 0.1120153449309513 |
| 24 | claude-opus-4.7 / tax.capital_gains_realizations.elasticity / Capital gains realizations elasticity | between_run_sd | 0.0 | 0.013097921802925678 |
| 24 | claude-opus-4.7 / tax.capital_gains_realizations.elasticity / Capital gains realizations elasticity | total_sd | 1.3348982483070886 | 1.334962504675277 |
| 25 | claude-opus-4.7 / tax.capital_gains_realizations.elasticity.net_of_tax_rate / Capital gains realizations elasticity (net-of-tax-rate convention) | between_run_sd | 0.0 | 0.021522597943143904 |
| 25 | claude-opus-4.7 / tax.capital_gains_realizations.elasticity.net_of_tax_rate / Capital gains realizations elasticity (net-of-tax-rate convention) | total_sd | 1.3436240380238647 | 1.3437964048834845 |
| 26 | claude-opus-4.7 / tax.elasticity_of_taxable_income.top_earners / Elasticity of taxable income | between_run_sd | 0.0 | 0.007823575482689058 |
| 26 | claude-opus-4.7 / tax.elasticity_of_taxable_income.top_earners / Elasticity of taxable income | total_sd | 0.6799997446894946 | 0.6800447493445643 |
| 27 | claude-opus-4.7 / trade.armington_elasticity.import_domestic / Armington elasticity | between_run_sd | 0.12472191289246472 | 0.14898886050827945 |
| 27 | claude-opus-4.7 / trade.armington_elasticity.import_domestic / Armington elasticity | total_sd | 2.577568520751033 | 2.5788566466879597 |

## `results/claude-opus-4.7-ies-clarify-batch15/summary.csv` (2 cells)

| line | row | column | old | new |
|---|---|---|---|---|
| 2 | claude-opus-4.7 / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | between_run_sd | 0.0 | 0.0278208554864871 |
| 2 | claude-opus-4.7 / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | total_sd | 0.7001019766989505 | 0.700654535258124 |

## `results/claude-opus-4.7-mechanism-ablation-batch15/summary.csv` (18 cells)

| line | row | column | old | new |
|---|---|---|---|---|
| 2 | claude-opus-4.7 / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | between_run_sd | 0.0 | 0.020667002685440396 |
| 2 | claude-opus-4.7 / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | total_sd | 0.7657429444300772 | 0.7660217894710596 |
| 3 | claude-opus-4.7 / labor_supply.extensive_margin.single_mothers / Employment participation elasticity of single mothers | between_run_sd | 0.027080128015453224 | 0.021900342463075772 |
| 3 | claude-opus-4.7 / labor_supply.extensive_margin.single_mothers / Employment participation elasticity of single mothers | total_sd | 0.7075558968888763 | 0.7073765891580587 |
| 4 | claude-opus-4.7 / labor_supply.frisch_elasticity.prime_age / Frisch elasticity of labor supply | between_run_sd | 0.022110831935702683 | 0.020593620910908838 |
| 4 | claude-opus-4.7 / labor_supply.frisch_elasticity.prime_age / Frisch elasticity of labor supply | total_sd | 1.2807528981466765 | 1.280727603530292 |
| 5 | claude-opus-4.7 / labor_supply.income_elasticity.prime_age / Income elasticity of labor supply | between_run_sd | 0.0 | 0.0012092238098144698 |
| 5 | claude-opus-4.7 / labor_supply.income_elasticity.prime_age / Income elasticity of labor supply | total_sd | 0.30002180244849613 | 0.30002423929853844 |
| 6 | claude-opus-4.7 / labor_supply.marshallian_wage_elasticity.prime_age / Uncompensated wage elasticity of labor supply | between_run_sd | 0.0 | 0.0019899748742132416 |
| 6 | claude-opus-4.7 / labor_supply.marshallian_wage_elasticity.prime_age / Uncompensated wage elasticity of labor supply | total_sd | 0.5959927607222535 | 0.595996082900998 |
| 7 | claude-opus-4.7 / production.capital_labor_substitution / Elasticity of substitution between capital and labor | between_run_sd | 0.0 | 0.008352478008883862 |
| 7 | claude-opus-4.7 / production.capital_labor_substitution / Elasticity of substitution between capital and labor | total_sd | 1.2370744638729987 | 1.2371026606775835 |
| 8 | claude-opus-4.7 / tax.capital_gains_realizations.elasticity / Capital gains realizations elasticity | between_run_sd | 0.0 | 0.016467560704474603 |
| 8 | claude-opus-4.7 / tax.capital_gains_realizations.elasticity / Capital gains realizations elasticity | total_sd | 1.3391087158172699 | 1.3392099661118615 |
| 9 | claude-opus-4.7 / tax.elasticity_of_taxable_income.top_earners / Elasticity of taxable income | between_run_sd | 0.0 | 0.005280993172584952 |
| 9 | claude-opus-4.7 / tax.elasticity_of_taxable_income.top_earners / Elasticity of taxable income | total_sd | 0.6833143035968149 | 0.6833347103644662 |
| 10 | claude-opus-4.7 / trade.armington_elasticity.import_domestic / Armington elasticity | between_run_sd | 0.12472191289246472 | 0.15324725844928586 |
| 10 | claude-opus-4.7 / trade.armington_elasticity.import_domestic / Armington elasticity | total_sd | 2.612012447860419 | 2.613529834236534 |

## `results/claude-opus-4.8-armington-clarify-batch15/summary.csv` (2 cells)

| line | row | column | old | new |
|---|---|---|---|---|
| 2 | claude-opus-4.8 / trade.armington_elasticity.import_domestic / Armington elasticity | between_run_sd | 0.12472191289246472 | 0.12293855737273343 |
| 2 | claude-opus-4.8 / trade.armington_elasticity.import_domestic / Armington elasticity | total_sd | 2.6657022995826076 | 2.6656194558363606 |

## `results/claude-opus-4.8-elasticities-batch15/summary.csv` (52 cells)

| line | row | column | old | new |
|---|---|---|---|---|
| 2 | claude-opus-4.8 / household.annual_discount_factor / Annual discount factor | between_run_sd | 0.0 | 0.0008463155439905582 |
| 2 | claude-opus-4.8 / household.annual_discount_factor / Annual discount factor | total_sd | 0.1269733690910552 | 0.12697618953305118 |
| 3 | claude-opus-4.8 / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | between_run_sd | 0.0 | 0.016431676725154998 |
| 3 | claude-opus-4.8 / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | total_sd | 0.7285579363830077 | 0.7287432103743174 |
| 4 | claude-opus-4.8 / household.relative_risk_aversion.crra / Coefficient of relative risk aversion | between_run_sd | 0.0 | 0.07637626158259744 |
| 4 | claude-opus-4.8 / household.relative_risk_aversion.crra / Coefficient of relative risk aversion | total_sd | 6.340827528800953 | 6.341287494139762 |
| 5 | claude-opus-4.8 / labor_supply.extensive_margin.single_mothers / Employment participation elasticity of single mothers | between_run_sd | 0.024944382578492935 | 0.022053281438874847 |
| 5 | claude-opus-4.8 / labor_supply.extensive_margin.single_mothers / Employment participation elasticity of single mothers | total_sd | 0.7203710704676214 | 0.7202767552591619 |
| 6 | claude-opus-4.8 / labor_supply.frisch_elasticity.prime_age / Frisch elasticity of labor supply | between_run_sd | 0.043461349368017654 | 0.040718034497423033 |
| 6 | claude-opus-4.8 / labor_supply.frisch_elasticity.prime_age / Frisch elasticity of labor supply | total_sd | 1.2739446340228273 | 1.2738539947733414 |
| 7 | claude-opus-4.8 / labor_supply.income_elasticity.prime_age / Income elasticity of labor supply | between_run_sd | 0.016 | 0.01549238164030595 |
| 7 | claude-opus-4.8 / labor_supply.income_elasticity.prime_age / Income elasticity of labor supply | total_sd | 0.30003301901624096 | 0.3000063772470327 |
| 8 | claude-opus-4.8 / labor_supply.marshallian_wage_elasticity.prime_age / Uncompensated wage elasticity of labor supply | between_run_sd | 0.0 | 0.00470448958147664 |
| 8 | claude-opus-4.8 / labor_supply.marshallian_wage_elasticity.prime_age / Uncompensated wage elasticity of labor supply | total_sd | 0.6021382627769141 | 0.6021566405199085 |
| 9 | claude-opus-4.8 / labor_supply.policy_response.substitution_elasticity.all / Substitution elasticity of labor supply in a tax-benefit simulation | between_run_sd | 0.0 | 0.006856383886568758 |
| 9 | claude-opus-4.8 / labor_supply.policy_response.substitution_elasticity.all / Substitution elasticity of labor supply in a tax-benefit simulation | total_sd | 0.6363989216678483 | 0.6364358549767605 |
| 10 | claude-opus-4.8 / labor_supply.policy_response.substitution_elasticity.primary.decile_1 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 1 | between_run_sd | 0.02211083193570266 | 0.01850605006177408 |
| 10 | claude-opus-4.8 / labor_supply.policy_response.substitution_elasticity.primary.decile_1 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 1 | total_sd | 0.6566356147480547 | 0.656524116507197 |
| 11 | claude-opus-4.8 / labor_supply.policy_response.substitution_elasticity.primary.decile_10 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 10 | between_run_sd | 0.0 | 0.007325298628724981 |
| 11 | claude-opus-4.8 / labor_supply.policy_response.substitution_elasticity.primary.decile_10 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 10 | total_sd | 0.6378115447894203 | 0.6378536091194176 |
| 12 | claude-opus-4.8 / labor_supply.policy_response.substitution_elasticity.primary.decile_2 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 2 | between_run_sd | 0.02743882083634223 | 0.028896058939277904 |
| 12 | claude-opus-4.8 / labor_supply.policy_response.substitution_elasticity.primary.decile_2 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 2 | total_sd | 0.6399271258423798 | 0.6399912653483814 |
| 13 | claude-opus-4.8 / labor_supply.policy_response.substitution_elasticity.primary.decile_3 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 3 | between_run_sd | 0.0 | 0.0037267799624996364 |
| 13 | claude-opus-4.8 / labor_supply.policy_response.substitution_elasticity.primary.decile_3 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 3 | total_sd | 0.6364199729301748 | 0.636430884569042 |
| 14 | claude-opus-4.8 / labor_supply.policy_response.substitution_elasticity.primary.decile_4 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 4 | between_run_sd | 0.0 | 0.003584302194601082 |
| 14 | claude-opus-4.8 / labor_supply.policy_response.substitution_elasticity.primary.decile_4 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 4 | total_sd | 0.6347567611560615 | 0.634766880874826 |
| 15 | claude-opus-4.8 / labor_supply.policy_response.substitution_elasticity.primary.decile_5 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 5 | between_run_sd | 0.0 | 0.0033850160019316382 |
| 15 | claude-opus-4.8 / labor_supply.policy_response.substitution_elasticity.primary.decile_5 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 5 | total_sd | 0.6358542209325796 | 0.6358632310576788 |
| 16 | claude-opus-4.8 / labor_supply.policy_response.substitution_elasticity.primary.decile_6 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 6 | between_run_sd | 0.0 | 0.003584302194601082 |
| 16 | claude-opus-4.8 / labor_supply.policy_response.substitution_elasticity.primary.decile_6 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 6 | total_sd | 0.6361371598257023 | 0.6361472575853278 |
| 17 | claude-opus-4.8 / labor_supply.policy_response.substitution_elasticity.primary.decile_7 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 7 | between_run_sd | 0.0 | 0.003061862178478962 |
| 17 | claude-opus-4.8 / labor_supply.policy_response.substitution_elasticity.primary.decile_7 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 7 | total_sd | 0.6366849364743392 | 0.6366922987859467 |
| 18 | claude-opus-4.8 / labor_supply.policy_response.substitution_elasticity.primary.decile_8 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 8 | between_run_sd | 0.0 | 0.0037267799624996364 |
| 18 | claude-opus-4.8 / labor_supply.policy_response.substitution_elasticity.primary.decile_8 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 8 | total_sd | 0.6364199729301748 | 0.636430884569042 |
| 19 | claude-opus-4.8 / labor_supply.policy_response.substitution_elasticity.primary.decile_9 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 9 | between_run_sd | 0.0 | 0.004598731709214312 |
| 19 | claude-opus-4.8 / labor_supply.policy_response.substitution_elasticity.primary.decile_9 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 9 | total_sd | 0.6333550840563293 | 0.6333717793155402 |
| 20 | claude-opus-4.8 / labor_supply.policy_response.substitution_elasticity.secondary / Secondary-earner substitution elasticity in a tax-benefit simulation | between_run_sd | 0.0669991708074726 | 0.054695536076234466 |
| 20 | claude-opus-4.8 / labor_supply.policy_response.substitution_elasticity.secondary / Secondary-earner substitution elasticity in a tax-benefit simulation | total_sd | 0.651229262838962 | 0.6500786610523034 |
| 21 | claude-opus-4.8 / macro.tfp_persistence.ar1 / TFP persistence | between_run_sd | 0.0 | 0.005011833219713317 |
| 21 | claude-opus-4.8 / macro.tfp_persistence.ar1 / TFP persistence | total_sd | 0.13573041218410362 | 0.13582291141000066 |
| 22 | claude-opus-4.8 / production.capital_labor_substitution / Elasticity of substitution between capital and labor | between_run_sd | 0.0 | 0.003337497399083457 |
| 22 | claude-opus-4.8 / production.capital_labor_substitution / Elasticity of substitution between capital and labor | total_sd | 1.2381764004418399 | 1.2381808985362357 |
| 23 | claude-opus-4.8 / production.capital_share / Capital share in production | between_run_sd | 0.006992058987800999 | 0.005728195372211251 |
| 23 | claude-opus-4.8 / production.capital_share / Capital share in production | total_sd | 0.10857350300858656 | 0.10849944188284513 |
| 24 | claude-opus-4.8 / tax.capital_gains_realizations.elasticity / Capital gains realizations elasticity | between_run_sd | 0.0 | 0.014497605166218173 |
| 24 | claude-opus-4.8 / tax.capital_gains_realizations.elasticity / Capital gains realizations elasticity | total_sd | 1.3275296345300756 | 1.3276087944538149 |
| 25 | claude-opus-4.8 / tax.capital_gains_realizations.elasticity.net_of_tax_rate / Capital gains realizations elasticity (net-of-tax-rate convention) | between_run_sd | 0.04988876515698587 | 0.05056321675772708 |
| 25 | claude-opus-4.8 / tax.capital_gains_realizations.elasticity.net_of_tax_rate / Capital gains realizations elasticity (net-of-tax-rate convention) | total_sd | 1.322785662804909 | 1.32281127139219 |
| 26 | claude-opus-4.8 / tax.elasticity_of_taxable_income.top_earners / Elasticity of taxable income | between_run_sd | 0.023570226039551605 | 0.025807244891481337 |
| 26 | claude-opus-4.8 / tax.elasticity_of_taxable_income.top_earners / Elasticity of taxable income | total_sd | 0.6812407491726646 | 0.681321815786539 |
| 27 | claude-opus-4.8 / trade.armington_elasticity.import_domestic / Armington elasticity | between_run_sd | 0.2 | 0.22979967121144648 |
| 27 | claude-opus-4.8 / trade.armington_elasticity.import_domestic / Armington elasticity | total_sd | 2.769641472986872 | 2.7719527012158376 |

## `results/claude-opus-4.8-ies-clarify-batch15/summary.csv` (2 cells)

| line | row | column | old | new |
|---|---|---|---|---|
| 2 | claude-opus-4.8 / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | between_run_sd | 0.0 | 0.01861451046898627 |
| 2 | claude-opus-4.8 / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | total_sd | 0.6906062151794208 | 0.6908570361836408 |

## `results/claude-opus-5-armington-clarify-batch15/summary.csv` (2 cells)

| line | row | column | old | new |
|---|---|---|---|---|
| 2 | claude-opus-5 / trade.armington_elasticity.import_domestic / Armington elasticity | between_run_sd | 0.26532998322843193 | 0.2605597606862749 |
| 2 | claude-opus-5 / trade.armington_elasticity.import_domestic / Armington elasticity | total_sd | 2.6954070245099864 | 2.694941635113211 |

## `results/claude-opus-5-elasticities-batch15/summary.csv` (52 cells)

| line | row | column | old | new |
|---|---|---|---|---|
| 2 | claude-opus-5 / household.annual_discount_factor / Annual discount factor | between_run_sd | 0.00464279609239471 | 0.003982867476245381 |
| 2 | claude-opus-5 / household.annual_discount_factor / Annual discount factor | total_sd | 0.12626798612254986 | 0.12624544347112976 |
| 3 | claude-opus-5 / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | between_run_sd | 0.08164965809277262 | 0.06740579846472161 |
| 3 | claude-opus-5 / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | total_sd | 0.7772624011733604 | 0.7758954280557256 |
| 4 | claude-opus-5 / household.relative_risk_aversion.crra / Coefficient of relative risk aversion | between_run_sd | 0.06798692684790378 | 0.12075474455827123 |
| 4 | claude-opus-5 / household.relative_risk_aversion.crra / Coefficient of relative risk aversion | total_sd | 6.428670282198507 | 6.429444850322097 |
| 5 | claude-opus-5 / labor_supply.extensive_margin.single_mothers / Employment participation elasticity of single mothers | between_run_sd | 0.06110100926607785 | 0.062337789502034786 |
| 5 | claude-opus-5 / labor_supply.extensive_margin.single_mothers / Employment participation elasticity of single mothers | total_sd | 0.7357719868727449 | 0.7358757254681889 |
| 6 | claude-opus-5 / labor_supply.frisch_elasticity.prime_age / Frisch elasticity of labor supply | between_run_sd | 0.03213858878185054 | 0.03121415277295434 |
| 6 | claude-opus-5 / labor_supply.frisch_elasticity.prime_age / Frisch elasticity of labor supply | total_sd | 1.2777825584451632 | 1.277759641368873 |
| 7 | claude-opus-5 / labor_supply.income_elasticity.prime_age / Income elasticity of labor supply | between_run_sd | 0.0135400640077266 | 0.017497805735450248 |
| 7 | claude-opus-5 / labor_supply.income_elasticity.prime_age / Income elasticity of labor supply | total_sd | 0.3048205650916253 | 0.3050219939201106 |
| 8 | claude-opus-5 / labor_supply.marshallian_wage_elasticity.prime_age / Uncompensated wage elasticity of labor supply | between_run_sd | 0.014966629547095765 | 0.011432361474729924 |
| 8 | claude-opus-5 / labor_supply.marshallian_wage_elasticity.prime_age / Uncompensated wage elasticity of labor supply | total_sd | 0.6033298330929775 | 0.603252506326239 |
| 9 | claude-opus-5 / labor_supply.policy_response.substitution_elasticity.all / Substitution elasticity of labor supply in a tax-benefit simulation | between_run_sd | 0.0024944382578492965 | 0.007269685917103515 |
| 9 | claude-opus-5 / labor_supply.policy_response.substitution_elasticity.all / Substitution elasticity of labor supply in a tax-benefit simulation | total_sd | 0.6339389670062008 | 0.6339757408607999 |
| 10 | claude-opus-5 / labor_supply.policy_response.substitution_elasticity.primary.decile_1 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 1 | between_run_sd | 0.0 | 0.011333161763407207 |
| 10 | claude-opus-5 / labor_supply.policy_response.substitution_elasticity.primary.decile_1 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 1 | total_sd | 0.6192349109990489 | 0.6193386113876282 |
| 11 | claude-opus-5 / labor_supply.policy_response.substitution_elasticity.primary.decile_10 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 10 | between_run_sd | 0.01203698005684519 | 0.01156222296965424 |
| 11 | claude-opus-5 / labor_supply.policy_response.substitution_elasticity.primary.decile_10 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 10 | total_sd | 0.6202435610306648 | 0.6202345291187126 |
| 12 | claude-opus-5 / labor_supply.policy_response.substitution_elasticity.primary.decile_2 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 2 | between_run_sd | 0.010456258094238738 | 0.012200705808362975 |
| 12 | claude-opus-5 / labor_supply.policy_response.substitution_elasticity.primary.decile_2 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 2 | total_sd | 0.6146965432453462 | 0.6147286915108703 |
| 13 | claude-opus-5 / labor_supply.policy_response.substitution_elasticity.primary.decile_3 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 3 | between_run_sd | 0.022449944320643643 | 0.024353610273085437 |
| 13 | claude-opus-5 / labor_supply.policy_response.substitution_elasticity.primary.decile_3 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 3 | total_sd | 0.6291046382227151 | 0.6291754478415911 |
| 14 | claude-opus-5 / labor_supply.policy_response.substitution_elasticity.primary.decile_4 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 4 | between_run_sd | 0.034576806613039836 | 0.03367131156076672 |
| 14 | claude-opus-5 / labor_supply.policy_response.substitution_elasticity.primary.decile_4 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 4 | total_sd | 0.631548416812027 | 0.6314994888710872 |
| 15 | claude-opus-5 / labor_supply.policy_response.substitution_elasticity.primary.decile_5 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 5 | between_run_sd | 0.01236482466066095 | 0.011586941883958082 |
| 15 | claude-opus-5 / labor_supply.policy_response.substitution_elasticity.primary.decile_5 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 5 | total_sd | 0.620131936006811 | 0.6201169134839727 |
| 16 | claude-opus-5 / labor_supply.policy_response.substitution_elasticity.primary.decile_6 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 6 | between_run_sd | 0.01540562667772179 | 0.013508783151054806 |
| 16 | claude-opus-5 / labor_supply.policy_response.substitution_elasticity.primary.decile_6 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 6 | total_sd | 0.6201068288340862 | 0.6200626041421589 |
| 17 | claude-opus-5 / labor_supply.policy_response.substitution_elasticity.primary.decile_7 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 7 | between_run_sd | 0.018785337071473826 | 0.014249619877971022 |
| 17 | claude-opus-5 / labor_supply.policy_response.substitution_elasticity.primary.decile_7 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 7 | total_sd | 0.6302038625185769 | 0.6300849713420493 |
| 18 | claude-opus-5 / labor_supply.policy_response.substitution_elasticity.primary.decile_8 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 8 | between_run_sd | 0.03282275633357646 | 0.028198502718328074 |
| 18 | claude-opus-5 / labor_supply.policy_response.substitution_elasticity.primary.decile_8 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 8 | total_sd | 0.6307427147595304 | 0.6305189881712084 |
| 19 | claude-opus-5 / labor_supply.policy_response.substitution_elasticity.primary.decile_9 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 9 | between_run_sd | 0.03275498265743532 | 0.024456117162515122 |
| 19 | claude-opus-5 / labor_supply.policy_response.substitution_elasticity.primary.decile_9 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 9 | total_sd | 0.6280739926774375 | 0.6276959081080229 |
| 20 | claude-opus-5 / labor_supply.policy_response.substitution_elasticity.secondary / Secondary-earner substitution elasticity in a tax-benefit simulation | between_run_sd | 0.042216373863966844 | 0.038952307020537626 |
| 20 | claude-opus-5 / labor_supply.policy_response.substitution_elasticity.secondary / Secondary-earner substitution elasticity in a tax-benefit simulation | total_sd | 0.6497803988015233 | 0.6495764979328198 |
| 21 | claude-opus-5 / macro.tfp_persistence.ar1 / TFP persistence | between_run_sd | 0.0012472191289246482 | 0.0030398282115204306 |
| 21 | claude-opus-5 / macro.tfp_persistence.ar1 / TFP persistence | total_sd | 0.12830732826347493 | 0.12833727239625717 |
| 22 | claude-opus-5 / production.capital_labor_substitution / Elasticity of substitution between capital and labor | between_run_sd | 0.028252826800556127 | 0.02121298082673805 |
| 22 | claude-opus-5 / production.capital_labor_substitution / Elasticity of substitution between capital and labor | total_sd | 1.2460285426773605 | 1.24588879820793 |
| 23 | claude-opus-5 / production.capital_share / Capital share in production | between_run_sd | 0.003999999999999981 | 0.003428272969813751 |
| 23 | claude-opus-5 / production.capital_share / Capital share in production | total_sd | 0.10812631502090507 | 0.10810667442649208 |
| 24 | claude-opus-5 / tax.capital_gains_realizations.elasticity / Capital gains realizations elasticity | between_run_sd | 0.03201388587611461 | 0.03985217127780564 |
| 24 | claude-opus-5 / tax.capital_gains_realizations.elasticity / Capital gains realizations elasticity | total_sd | 1.3282984834407932 | 1.3285105072139165 |
| 25 | claude-opus-5 / tax.capital_gains_realizations.elasticity.net_of_tax_rate / Capital gains realizations elasticity (net-of-tax-rate convention) | between_run_sd | 0.2638181191654584 | 0.2554284255042018 |
| 25 | claude-opus-5 / tax.capital_gains_realizations.elasticity.net_of_tax_rate / Capital gains realizations elasticity (net-of-tax-rate convention) | total_sd | 1.6020305799723882 | 1.6006703782235188 |
| 26 | claude-opus-5 / tax.elasticity_of_taxable_income.top_earners / Elasticity of taxable income | between_run_sd | 0.028720878971384024 | 0.03126271296964202 |
| 26 | claude-opus-5 / tax.elasticity_of_taxable_income.top_earners / Elasticity of taxable income | total_sd | 0.6812633709187333 | 0.6813752628976847 |
| 27 | claude-opus-5 / trade.armington_elasticity.import_domestic / Armington elasticity | between_run_sd | 0.2160246899469287 | 0.22862572519780494 |
| 27 | claude-opus-5 / trade.armington_elasticity.import_domestic / Armington elasticity | total_sd | 2.7513484825122068 | 2.7523665322369 |

## `results/claude-opus-5-ies-clarify-batch15/summary.csv` (2 cells)

| line | row | column | old | new |
|---|---|---|---|---|
| 2 | claude-opus-5 / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | between_run_sd | 0.03559026084010437 | 0.030317853192833782 |
| 2 | claude-opus-5 / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | total_sd | 0.7109256788394503 | 0.7106812410559947 |

## `results/claude-sonnet-4.6-armington-clarify-batch15/summary.csv` (2 cells)

| line | row | column | old | new |
|---|---|---|---|---|
| 2 | claude-sonnet-4.6 / trade.armington_elasticity.import_domestic / Armington elasticity | between_run_sd | 0.23570226039551584 | 0.23524136541008248 |
| 2 | claude-sonnet-4.6 / trade.armington_elasticity.import_domestic / Armington elasticity | total_sd | 2.539165900886002 | 2.5391231590190078 |

## `results/claude-sonnet-4.6-elasticities-batch15/summary.csv` (48 cells)

| line | row | column | old | new |
|---|---|---|---|---|
| 2 | claude-sonnet-4.6 / household.annual_discount_factor / Annual discount factor | between_run_sd | 0.0 | 0.002315617268318185 |
| 2 | claude-sonnet-4.6 / household.annual_discount_factor / Annual discount factor | total_sd | 0.12656356275273967 | 0.1265847443414885 |
| 3 | claude-sonnet-4.6 / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | between_run_sd | 0.0 | 0.005612486080160903 |
| 3 | claude-sonnet-4.6 / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | total_sd | 0.7261593221264264 | 0.7261810112576004 |
| 4 | claude-sonnet-4.6 / household.relative_risk_aversion.crra / Coefficient of relative risk aversion | between_run_sd | 0.0 | 0.21187981394072342 |
| 4 | claude-sonnet-4.6 / household.relative_risk_aversion.crra / Coefficient of relative risk aversion | total_sd | 6.4413340793831075 | 6.444817901056458 |
| 5 | claude-sonnet-4.6 / labor_supply.extensive_margin.single_mothers / Employment participation elasticity of single mothers | between_run_sd | 0.0 | 0.0028062430400804515 |
| 5 | claude-sonnet-4.6 / labor_supply.extensive_margin.single_mothers / Employment participation elasticity of single mothers | total_sd | 0.7319522506435938 | 0.7319576300730953 |
| 6 | claude-sonnet-4.6 / labor_supply.frisch_elasticity.prime_age / Frisch elasticity of labor supply | between_run_sd | 0.0627162924074226 | 0.06606099874779031 |
| 6 | claude-sonnet-4.6 / labor_supply.frisch_elasticity.prime_age / Frisch elasticity of labor supply | total_sd | 1.2759488163497956 | 1.2761175902583064 |
| 7 | claude-sonnet-4.6 / labor_supply.income_elasticity.prime_age / Income elasticity of labor supply | between_run_sd | 0.012472191289246471 | 0.013718195540554482 |
| 7 | claude-sonnet-4.6 / labor_supply.income_elasticity.prime_age / Income elasticity of labor supply | total_sd | 0.30977657495183347 | 0.30982924284551033 |
| 8 | claude-sonnet-4.6 / labor_supply.marshallian_wage_elasticity.prime_age / Uncompensated wage elasticity of labor supply | between_run_sd | 0.0 | 0.004273822124931689 |
| 8 | claude-sonnet-4.6 / labor_supply.marshallian_wage_elasticity.prime_age / Uncompensated wage elasticity of labor supply | total_sd | 0.599113627694187 | 0.5991288713160504 |
| 9 | claude-sonnet-4.6 / labor_supply.policy_response.substitution_elasticity.all / Substitution elasticity of labor supply in a tax-benefit simulation | between_run_sd | 0.06236095644623236 | 0.05549524504155489 |
| 9 | claude-sonnet-4.6 / labor_supply.policy_response.substitution_elasticity.all / Substitution elasticity of labor supply in a tax-benefit simulation | total_sd | 0.6295127083705301 | 0.6288696870841632 |
| 10 | claude-sonnet-4.6 / labor_supply.policy_response.substitution_elasticity.primary.decile_1 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 1 | between_run_sd | 0.01959591794226543 | 0.016555512677051118 |
| 10 | claude-sonnet-4.6 / labor_supply.policy_response.substitution_elasticity.primary.decile_1 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 1 | total_sd | 0.6371470885910097 | 0.6370608271586002 |
| 11 | claude-sonnet-4.6 / labor_supply.policy_response.substitution_elasticity.primary.decile_10 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 10 | between_run_sd | 0.01720465053408526 | 0.01864020445762928 |
| 11 | claude-sonnet-4.6 / labor_supply.policy_response.substitution_elasticity.primary.decile_10 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 10 | total_sd | 0.6333906925780047 | 0.6334313117194845 |
| 12 | claude-sonnet-4.6 / labor_supply.policy_response.substitution_elasticity.primary.decile_2 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 2 | between_run_sd | 0.02867441755680876 | 0.02713989478404235 |
| 12 | claude-sonnet-4.6 / labor_supply.policy_response.substitution_elasticity.primary.decile_2 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 2 | total_sd | 0.6381136458343452 | 0.638046531740959 |
| 13 | claude-sonnet-4.6 / labor_supply.policy_response.substitution_elasticity.primary.decile_3 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 3 | between_run_sd | 0.0339934634239519 | 0.026678247485336978 |
| 13 | claude-sonnet-4.6 / labor_supply.policy_response.substitution_elasticity.primary.decile_3 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 3 | total_sd | 0.6341828863453612 | 0.6338328696641305 |
| 14 | claude-sonnet-4.6 / labor_supply.policy_response.substitution_elasticity.primary.decile_4 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 4 | between_run_sd | 0.049888765156985884 | 0.04269727417789363 |
| 14 | claude-sonnet-4.6 / labor_supply.policy_response.substitution_elasticity.primary.decile_4 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 4 | total_sd | 0.6332833730294485 | 0.6327574566047317 |
| 15 | claude-sonnet-4.6 / labor_supply.policy_response.substitution_elasticity.primary.decile_5 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 5 | between_run_sd | 0.0339934634239519 | 0.028639492934679472 |
| 15 | claude-sonnet-4.6 / labor_supply.policy_response.substitution_elasticity.primary.decile_5 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 5 | total_sd | 0.6318140999886316 | 0.6315486694978024 |
| 16 | claude-sonnet-4.6 / labor_supply.policy_response.substitution_elasticity.primary.decile_6 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 6 | between_run_sd | 0.0 | 0.0016188130082117407 |
| 16 | claude-sonnet-4.6 / labor_supply.policy_response.substitution_elasticity.primary.decile_6 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 6 | total_sd | 0.6306984851469573 | 0.6307005626461912 |
| 17 | claude-sonnet-4.6 / labor_supply.policy_response.substitution_elasticity.primary.decile_7 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 7 | between_run_sd | 0.012472191289246468 | 0.008719231617522265 |
| 17 | claude-sonnet-4.6 / labor_supply.policy_response.substitution_elasticity.primary.decile_7 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 7 | total_sd | 0.6300309262691441 | 0.629967806717137 |
| 18 | claude-sonnet-4.6 / labor_supply.policy_response.substitution_elasticity.primary.decile_8 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 8 | between_run_sd | 0.016996731711975945 | 0.012492597808302324 |
| 18 | claude-sonnet-4.6 / labor_supply.policy_response.substitution_elasticity.primary.decile_8 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 8 | total_sd | 0.6313883302778973 | 0.6312831375240608 |
| 19 | claude-sonnet-4.6 / labor_supply.policy_response.substitution_elasticity.primary.decile_9 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 9 | between_run_sd | 0.0 | 0.005685410177717078 |
| 19 | claude-sonnet-4.6 / labor_supply.policy_response.substitution_elasticity.primary.decile_9 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 9 | total_sd | 0.6290926159512957 | 0.6291183063091818 |
| 20 | claude-sonnet-4.6 / labor_supply.policy_response.substitution_elasticity.secondary / Secondary-earner substitution elasticity in a tax-benefit simulation | between_run_sd | 0.0 | 0.0038242646351946204 |
| 20 | claude-sonnet-4.6 / labor_supply.policy_response.substitution_elasticity.secondary / Secondary-earner substitution elasticity in a tax-benefit simulation | total_sd | 0.6400536273105039 | 0.6400650520324738 |
| 22 | claude-sonnet-4.6 / production.capital_labor_substitution / Elasticity of substitution between capital and labor | between_run_sd | 0.03399346342395193 | 0.03520534997222247 |
| 22 | claude-sonnet-4.6 / production.capital_labor_substitution / Elasticity of substitution between capital and labor | total_sd | 1.2325562867471813 | 1.2325903054588379 |
| 23 | claude-sonnet-4.6 / production.capital_share / Capital share in production | between_run_sd | 0.0 | 0.001906567596493766 |
| 23 | claude-sonnet-4.6 / production.capital_share / Capital share in production | total_sd | 0.11033357250729363 | 0.11035004405174573 |
| 25 | claude-sonnet-4.6 / tax.capital_gains_realizations.elasticity.net_of_tax_rate / Capital gains realizations elasticity (net-of-tax-rate convention) | between_run_sd | 0.22110831935702666 | 0.2576118958605928 |
| 25 | claude-sonnet-4.6 / tax.capital_gains_realizations.elasticity.net_of_tax_rate / Capital gains realizations elasticity (net-of-tax-rate convention) | total_sd | 2.409760246257798 | 2.41338340187473 |
| 26 | claude-sonnet-4.6 / tax.elasticity_of_taxable_income.top_earners / Elasticity of taxable income | between_run_sd | 0.0 | 0.004244277192748974 |
| 26 | claude-sonnet-4.6 / tax.elasticity_of_taxable_income.top_earners / Elasticity of taxable income | total_sd | 0.7068306118787506 | 0.7068433544837058 |
| 27 | claude-sonnet-4.6 / trade.armington_elasticity.import_domestic / Armington elasticity | between_run_sd | 0.24944382578492943 | 0.22575958205331823 |
| 27 | claude-sonnet-4.6 / trade.armington_elasticity.import_domestic / Armington elasticity | total_sd | 2.710946380468964 | 2.708869772514811 |

## `results/claude-sonnet-4.6-ies-clarify-batch15/summary.csv` (2 cells)

| line | row | column | old | new |
|---|---|---|---|---|
| 2 | claude-sonnet-4.6 / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | between_run_sd | 0.0 | 0.023116552511133644 |
| 2 | claude-sonnet-4.6 / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | total_sd | 0.7060179067999779 | 0.7063962483777941 |

## `results/claude-sonnet-5-armington-clarify-batch15/summary.csv` (2 cells)

| line | row | column | old | new |
|---|---|---|---|---|
| 2 | claude-sonnet-5 / trade.armington_elasticity.import_domestic / Armington elasticity | between_run_sd | 0.12472191289246472 | 0.08522910301065009 |
| 2 | claude-sonnet-5 / trade.armington_elasticity.import_domestic / Armington elasticity | total_sd | 2.734351741170921 | 2.7328351375245616 |

## `results/claude-sonnet-5-elasticities-batch15/summary.csv` (52 cells)

| line | row | column | old | new |
|---|---|---|---|---|
| 2 | claude-sonnet-5 / household.annual_discount_factor / Annual discount factor | between_run_sd | 0.004988876515698593 | 0.0044247096577691445 |
| 2 | claude-sonnet-5 / household.annual_discount_factor / Annual discount factor | total_sd | 0.12675651281755373 | 0.12673556212970902 |
| 3 | claude-sonnet-5 / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | between_run_sd | 0.0 | 0.022453655975512445 |
| 3 | claude-sonnet-5 / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | total_sd | 0.6988749639798079 | 0.6992355697076947 |
| 4 | claude-sonnet-5 / household.relative_risk_aversion.crra / Coefficient of relative risk aversion | between_run_sd | 0.0 | 0.2146711956043993 |
| 4 | claude-sonnet-5 / household.relative_risk_aversion.crra / Coefficient of relative risk aversion | total_sd | 6.431963897856808 | 6.435545299782728 |
| 5 | claude-sonnet-5 / labor_supply.extensive_margin.single_mothers / Employment participation elasticity of single mothers | between_run_sd | 0.036514837167011066 | 0.034386891882421305 |
| 5 | claude-sonnet-5 / labor_supply.extensive_margin.single_mothers / Employment participation elasticity of single mothers | total_sd | 0.7352896490877289 | 0.735187046305602 |
| 6 | claude-sonnet-5 / labor_supply.frisch_elasticity.prime_age / Frisch elasticity of labor supply | between_run_sd | 0.03399346342395189 | 0.03200585883865635 |
| 6 | claude-sonnet-5 / labor_supply.frisch_elasticity.prime_age / Frisch elasticity of labor supply | total_sd | 1.2734076794395248 | 1.2733561707157979 |
| 7 | claude-sonnet-5 / labor_supply.income_elasticity.prime_age / Income elasticity of labor supply | between_run_sd | 0.0 | 0.0013381164207779347 |
| 7 | claude-sonnet-5 / labor_supply.income_elasticity.prime_age / Income elasticity of labor supply | total_sd | 0.3000124372421917 | 0.3000154213628952 |
| 8 | claude-sonnet-5 / labor_supply.marshallian_wage_elasticity.prime_age / Uncompensated wage elasticity of labor supply | between_run_sd | 0.0074833147735478825 | 0.006236095644623231 |
| 8 | claude-sonnet-5 / labor_supply.marshallian_wage_elasticity.prime_age / Uncompensated wage elasticity of labor supply | total_sd | 0.5910077786666131 | 0.5909933022745125 |
| 9 | claude-sonnet-5 / labor_supply.policy_response.substitution_elasticity.all / Substitution elasticity of labor supply in a tax-benefit simulation | between_run_sd | 0.0 | 0.011851511858549253 |
| 9 | claude-sonnet-5 / labor_supply.policy_response.substitution_elasticity.all / Substitution elasticity of labor supply in a tax-benefit simulation | total_sd | 0.6376384653547809 | 0.637748595320549 |
| 10 | claude-sonnet-5 / labor_supply.policy_response.substitution_elasticity.primary.decile_1 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 1 | between_run_sd | 0.07756287771866126 | 0.07726598360353813 |
| 10 | claude-sonnet-5 / labor_supply.policy_response.substitution_elasticity.primary.decile_1 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 1 | total_sd | 0.6446218001881241 | 0.644586144359309 |
| 11 | claude-sonnet-5 / labor_supply.policy_response.substitution_elasticity.primary.decile_10 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 10 | between_run_sd | 0.06259570450296267 | 0.058842123989158945 |
| 11 | claude-sonnet-5 / labor_supply.policy_response.substitution_elasticity.primary.decile_10 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 10 | total_sd | 0.637948677620526 | 0.6375913178605173 |
| 12 | claude-sonnet-5 / labor_supply.policy_response.substitution_elasticity.primary.decile_2 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 2 | between_run_sd | 0.04519587001780878 | 0.04189035290692436 |
| 12 | claude-sonnet-5 / labor_supply.policy_response.substitution_elasticity.primary.decile_2 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 2 | total_sd | 0.6337811202089673 | 0.6335539782317947 |
| 13 | claude-sonnet-5 / labor_supply.policy_response.substitution_elasticity.primary.decile_3 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 3 | between_run_sd | 0.03590109871423003 | 0.03545487742657325 |
| 13 | claude-sonnet-5 / labor_supply.policy_response.substitution_elasticity.primary.decile_3 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 3 | total_sd | 0.634304209788612 | 0.6342791104868581 |
| 14 | claude-sonnet-5 / labor_supply.policy_response.substitution_elasticity.primary.decile_4 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 4 | between_run_sd | 0.036184711320298435 | 0.0354381934578437 |
| 14 | claude-sonnet-5 / labor_supply.policy_response.substitution_elasticity.primary.decile_4 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 4 | total_sd | 0.6334776754375625 | 0.6334354722463844 |
| 15 | claude-sonnet-5 / labor_supply.policy_response.substitution_elasticity.primary.decile_5 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 5 | between_run_sd | 0.07395494123676478 | 0.06485812722139504 |
| 15 | claude-sonnet-5 / labor_supply.policy_response.substitution_elasticity.primary.decile_5 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 5 | total_sd | 0.637504618719652 | 0.6365134580055808 |
| 16 | claude-sonnet-5 / labor_supply.policy_response.substitution_elasticity.primary.decile_6 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 6 | between_run_sd | 0.0448998886412873 | 0.0410100258744398 |
| 16 | claude-sonnet-5 / labor_supply.policy_response.substitution_elasticity.primary.decile_6 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 6 | total_sd | 0.6327557322274265 | 0.6324916117142495 |
| 17 | claude-sonnet-5 / labor_supply.policy_response.substitution_elasticity.primary.decile_7 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 7 | between_run_sd | 0.049888765156985884 | 0.04532170806823395 |
| 17 | claude-sonnet-5 / labor_supply.policy_response.substitution_elasticity.primary.decile_7 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 7 | total_sd | 0.6346874755867384 | 0.6343448273612705 |
| 18 | claude-sonnet-5 / labor_supply.policy_response.substitution_elasticity.primary.decile_8 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 8 | between_run_sd | 0.026532998322843202 | 0.026289235228299988 |
| 18 | claude-sonnet-5 / labor_supply.policy_response.substitution_elasticity.primary.decile_8 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 8 | total_sd | 0.6332005178719718 | 0.6331903503072533 |
| 19 | claude-sonnet-5 / labor_supply.policy_response.substitution_elasticity.primary.decile_9 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 9 | between_run_sd | 0.044251804734069575 | 0.04199992063484565 |
| 19 | claude-sonnet-5 / labor_supply.policy_response.substitution_elasticity.primary.decile_9 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 9 | total_sd | 0.6340300597500617 | 0.633876871149104 |
| 20 | claude-sonnet-5 / labor_supply.policy_response.substitution_elasticity.secondary / Secondary-earner substitution elasticity in a tax-benefit simulation | between_run_sd | 0.09104333522498442 | 0.07836541896071818 |
| 20 | claude-sonnet-5 / labor_supply.policy_response.substitution_elasticity.secondary / Secondary-earner substitution elasticity in a tax-benefit simulation | total_sd | 0.6534047314303406 | 0.6517591526442537 |
| 21 | claude-sonnet-5 / macro.tfp_persistence.ar1 / TFP persistence | between_run_sd | 0.0 | 0.001356977851289017 |
| 21 | claude-sonnet-5 / macro.tfp_persistence.ar1 / TFP persistence | total_sd | 0.13157949514140366 | 0.13158649220400837 |
| 22 | claude-sonnet-5 / production.capital_labor_substitution / Elasticity of substitution between capital and labor | between_run_sd | 0.03055050463303894 | 0.02620909511346522 |
| 22 | claude-sonnet-5 / production.capital_labor_substitution / Elasticity of substitution between capital and labor | total_sd | 1.229025005961139 | 1.2289247530305147 |
| 23 | claude-sonnet-5 / production.capital_share / Capital share in production | between_run_sd | 0.009977753031397158 | 0.006956691423051322 |
| 23 | claude-sonnet-5 / production.capital_share / Capital share in production | total_sd | 0.10733340450308199 | 0.10709481650491877 |
| 24 | claude-sonnet-5 / tax.capital_gains_realizations.elasticity / Capital gains realizations elasticity | between_run_sd | 0.03399346342395189 | 0.032387626238014625 |
| 24 | claude-sonnet-5 / tax.capital_gains_realizations.elasticity / Capital gains realizations elasticity | total_sd | 1.3329503356172812 | 1.3329103495734438 |
| 25 | claude-sonnet-5 / tax.capital_gains_realizations.elasticity.net_of_tax_rate / Capital gains realizations elasticity (net-of-tax-rate convention) | between_run_sd | 0.0 | 0.011437025642865193 |
| 25 | claude-sonnet-5 / tax.capital_gains_realizations.elasticity.net_of_tax_rate / Capital gains realizations elasticity (net-of-tax-rate convention) | total_sd | 1.3226069584977493 | 1.3226564074702933 |
| 26 | claude-sonnet-5 / tax.elasticity_of_taxable_income.top_earners / Elasticity of taxable income | between_run_sd | 0.04422166387140532 | 0.03771291408640929 |
| 26 | claude-sonnet-5 / tax.elasticity_of_taxable_income.top_earners / Elasticity of taxable income | total_sd | 0.685862747445386 | 0.6854738628617919 |
| 27 | claude-sonnet-5 / trade.armington_elasticity.import_domestic / Armington elasticity | between_run_sd | 0.2315167380558045 | 0.26696982767513067 |
| 27 | claude-sonnet-5 / trade.armington_elasticity.import_domestic / Armington elasticity | total_sd | 2.886537983082464 | 2.889597621930546 |

## `results/claude-sonnet-5-ies-clarify-batch15/summary.csv` (2 cells)

| line | row | column | old | new |
|---|---|---|---|---|
| 2 | claude-sonnet-5 / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | between_run_sd | 0.0 | 0.016612411691931492 |
| 2 | claude-sonnet-5 / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | total_sd | 0.6744752847378637 | 0.6746798366221155 |

## `results/correlates-country.csv` (16 cells)

| line | row | column | old | new |
|---|---|---|---|---|
| 2 | Implied optimal top rate (%) / True / Exploratory. Lab country is perfectly confounded with serving path (every Chinese lab ran via OpenRouter JSON mode) and elicitation wave, and co-varies with completion budget and reasoning configuration; prompts are English-language. | holm_adjusted_p | 0.2091 | 0.2371 |
| 3 | ETI pooled median / False / Exploratory. Lab country is perfectly confounded with serving path (every Chinese lab ran via OpenRouter JSON mode) and elicitation wave, and co-varies with completion budget and reasoning configuration; prompts are English-language. | holm_adjusted_p | 0.2091 | 0.2371 |
| 4 | Avg interval-width rank (1 = tightest) / False / Exploratory. Lab country is perfectly confounded with serving path (every Chinese lab ran via OpenRouter JSON mode) and elicitation wave, and co-varies with completion budget and reasoning configuration; prompts are English-language. | us_median | 13.7885 | 13.8654 |
| 4 | Avg interval-width rank (1 = tightest) / False / Exploratory. Lab country is perfectly confounded with serving path (every Chinese lab ran via OpenRouter JSON mode) and elicitation wave, and co-varies with completion budget and reasoning configuration; prompts are English-language. | china_median | 20.3077 | 20.4615 |
| 4 | Avg interval-width rank (1 = tightest) / False / Exploratory. Lab country is perfectly confounded with serving path (every Chinese lab ran via OpenRouter JSON mode) and elicitation wave, and co-varies with completion budget and reasoning configuration; prompts are English-language. | china_minus_us | 6.5192 | 6.5962 |
| 4 | Avg interval-width rank (1 = tightest) / False / Exploratory. Lab country is perfectly confounded with serving path (every Chinese lab ran via OpenRouter JSON mode) and elicitation wave, and co-varies with completion budget and reasoning configuration; prompts are English-language. | permutation_p | 0.028617 | 0.055464 |
| 4 | Avg interval-width rank (1 = tightest) / False / Exploratory. Lab country is perfectly confounded with serving path (every Chinese lab ran via OpenRouter JSON mode) and elicitation wave, and co-varies with completion budget and reasoning configuration; prompts are English-language. | holm_adjusted_p | 0.1072 | 0.2219 |
| 4 | Avg interval-width rank (1 = tightest) / False / Exploratory. Lab country is perfectly confounded with serving path (every Chinese lab ran via OpenRouter JSON mode) and elicitation wave, and co-varies with completion budget and reasoning configuration; prompts are English-language. | bh_adjusted_p | 0.0572 | 0.1394 |
| 5 | Mean |center|, labor-and-tax / False / Exploratory. Lab country is perfectly confounded with serving path (every Chinese lab ran via OpenRouter JSON mode) and elicitation wave, and co-varies with completion budget and reasoning configuration; prompts are English-language. | china_median | 0.3237 | 0.3342 |
| 5 | Mean |center|, labor-and-tax / False / Exploratory. Lab country is perfectly confounded with serving path (every Chinese lab ran via OpenRouter JSON mode) and elicitation wave, and co-varies with completion budget and reasoning configuration; prompts are English-language. | china_minus_us | -0.0442 | -0.0337 |
| 5 | Mean |center|, labor-and-tax / False / Exploratory. Lab country is perfectly confounded with serving path (every Chinese lab ran via OpenRouter JSON mode) and elicitation wave, and co-varies with completion budget and reasoning configuration; prompts are English-language. | permutation_p | 0.026791 | 0.079033 |
| 5 | Mean |center|, labor-and-tax / False / Exploratory. Lab country is perfectly confounded with serving path (every Chinese lab ran via OpenRouter JSON mode) and elicitation wave, and co-varies with completion budget and reasoning configuration; prompts are English-language. | holm_adjusted_p | 0.1072 | 0.2371 |
| 5 | Mean |center|, labor-and-tax / False / Exploratory. Lab country is perfectly confounded with serving path (every Chinese lab ran via OpenRouter JSON mode) and elicitation wave, and co-varies with completion budget and reasoning configuration; prompts are English-language. | bh_adjusted_p | 0.0572 | 0.1394 |
| 6 | Mean |center|, macro-and-trade / False / Exploratory. Lab country is perfectly confounded with serving path (every Chinese lab ran via OpenRouter JSON mode) and elicitation wave, and co-varies with completion budget and reasoning configuration; prompts are English-language. | permutation_p | 0.169396 | 0.16827 |
| 6 | Mean |center|, macro-and-trade / False / Exploratory. Lab country is perfectly confounded with serving path (every Chinese lab ran via OpenRouter JSON mode) and elicitation wave, and co-varies with completion budget and reasoning configuration; prompts are English-language. | holm_adjusted_p | 0.2091 | 0.2371 |
| 6 | Mean |center|, macro-and-trade / False / Exploratory. Lab country is perfectly confounded with serving path (every Chinese lab ran via OpenRouter JSON mode) and elicitation wave, and co-varies with completion budget and reasoning configuration; prompts are English-language. | bh_adjusted_p | 0.1694 | 0.1683 |

## `results/correlates-model-summary.csv` (30 cells)

| line | row | column | old | new |
|---|---|---|---|---|
| 2 | gpt-5.4 / openai / april_2026 | avg_width_rank | 15.307692307692308 | 15.384615384615385 |
| 5 | claude-opus-4.7 / anthropic / april_2026 | avg_width_rank | 9.461538461538462 | 9.615384615384615 |
| 6 | claude-sonnet-4.6 / anthropic / april_2026 | avg_width_rank | 13.73076923076923 | 13.807692307692308 |
| 7 | claude-haiku-4.5 / anthropic / april_2026 | avg_width_rank | 9.307692307692308 | 9.384615384615385 |
| 9 | gemini-3-flash-preview / google / april_2026 | avg_width_rank | 12.923076923076923 | 13.0 |
| 10 | gemini-3.1-flash-lite-preview / google / april_2026 | avg_width_rank | 13.923076923076923 | 14.23076923076923 |
| 11 | grok-4.20 / xai / april_2026 | avg_width_rank | 23.76923076923077 | 24.0 |
| 13 | gpt-5.5 / openai / july_2026_frontier | avg_width_rank | 15.076923076923077 | 15.307692307692308 |
| 14 | claude-fable-5 / anthropic / july_2026_frontier | avg_width_rank | 6.846153846153846 | 6.923076923076923 |
| 15 | claude-opus-4.8 / anthropic / july_2026_frontier | avg_width_rank | 11.038461538461538 | 11.192307692307692 |
| 16 | claude-sonnet-5 / anthropic / july_2026_frontier | avg_width_rank | 9.846153846153847 | 10.0 |
| 17 | gemini-3.5-flash / google / july_2026_frontier | mean_abs_center_labor_tax | 0.21794444444444447 | 0.30894444444444447 |
| 17 | gemini-3.5-flash / google / july_2026_frontier | mean_abs_center_macro_trade | 1.1533333333333333 | 1.16 |
| 17 | gemini-3.5-flash / google / july_2026_frontier | avg_width_rank | 13.307692307692308 | 11.076923076923077 |
| 18 | grok-4.3 / xai / july_2026_frontier | avg_width_rank | 18.692307692307693 | 18.846153846153847 |
| 19 | deepseek-v4-pro / deepseek / july_2026_independent | avg_width_rank | 20.384615384615383 | 20.46153846153846 |
| 20 | qwen-3.7-max / alibaba / july_2026_independent | avg_width_rank | 20.307692307692307 | 20.53846153846154 |
| 21 | kimi-k2.6 / moonshot / july_2026_independent | mean_abs_center_labor_tax | 0.32366666666666666 | 0.3342222222222222 |
| 21 | kimi-k2.6 / moonshot / july_2026_independent | avg_width_rank | 22.692307692307693 | 22.53846153846154 |
| 22 | glm-5.2 / zhipu / july_2026_independent | mean_abs_center_labor_tax | 0.3698888888888889 | 0.3687777777777778 |
| 23 | minimax-m3 / minimax / july_2026_independent | avg_width_rank | 18.76923076923077 | 19.0 |
| 24 | gpt-5.6-sol / openai / july_2026_gpt56 | avg_width_rank | 17.384615384615383 | 17.46153846153846 |
| 26 | gpt-5.6-terra / openai / july_2026_gpt56 | avg_width_rank | 13.846153846153847 | 13.923076923076923 |
| 27 | grok-4.5 / xai / july_2026_late | avg_width_rank | 18.76923076923077 | 19.0 |
| 29 | gemini-3.6-flash / google / july_2026_late | avg_width_rank | 7.461538461538462 | 7.615384615384615 |
| 30 | claude-opus-5 / anthropic / july_2026_late | avg_width_rank | 13.0 | 13.076923076923077 |
| 31 | qwen3.8-max / alibaba / august_2026 | avg_width_rank | 19.384615384615383 | 19.46153846153846 |
| 32 | inkling / thinkingmachines / august_2026 | mean_abs_center_labor_tax | 0.34099999999999997 | 0.3598888888888889 |
| 32 | inkling / thinkingmachines / august_2026 | mean_abs_center_macro_trade | 1.0688888888888888 | 1.0866666666666667 |
| 32 | inkling / thinkingmachines / august_2026 | avg_width_rank | 12.692307692307692 | 12.076923076923077 |

## `results/correlates-posthoc.csv` (8 cells)

| line | row | column | old | new |
|---|---|---|---|---|
| 2 | Overall within-$1 (leaderboard headline) / Max between-run variance share / Post hoc: computed after the eight-test family was declared, prompted in review of the width result; raw permutation p only, outside the Holm/BH family by construction. | spearman_rho | -0.3891625615763547 | -0.4247400109469075 |
| 2 | Overall within-$1 (leaderboard headline) / Max between-run variance share / Post hoc: computed after the eight-test family was declared, prompted in review of the width result; raw permutation p only, outside the Holm/BH family by construction. | raw_p | 0.04129793510324484 | 0.02424878756062197 |
| 3 | Overall within-$1 (leaderboard headline) / Median between-run SD / Post hoc: computed after the eight-test family was declared, prompted in review of the width result; raw permutation p only, outside the Holm/BH family by construction. | spearman_rho | -0.25246744674571703 | -0.36179529282977557 |
| 3 | Overall within-$1 (leaderboard headline) / Median between-run SD / Post hoc: computed after the eight-test family was declared, prompted in review of the width result; raw permutation p only, outside the Holm/BH family by construction. | raw_p | 0.19549022548872558 | 0.05934703264836758 |
| 4 | Tax within-$1 (domain-matched) / Max between-run variance share / Post hoc: computed after the eight-test family was declared, prompted in review of the width result; raw permutation p only, outside the Holm/BH family by construction. | spearman_rho | -0.5894593241775006 | -0.5938398858063162 |
| 4 | Tax within-$1 (domain-matched) / Max between-run variance share / Post hoc: computed after the eight-test family was declared, prompted in review of the width result; raw permutation p only, outside the Holm/BH family by construction. | raw_p | 0.00119994000299985 | 0.0009499525023748813 |
| 5 | Tax within-$1 (domain-matched) / Median between-run SD / Post hoc: computed after the eight-test family was declared, prompted in review of the width result; raw permutation p only, outside the Holm/BH family by construction. | spearman_rho | -0.4404226581361552 | -0.4985626703795767 |
| 5 | Tax within-$1 (domain-matched) / Median between-run SD / Post hoc: computed after the eight-test family was declared, prompted in review of the width result; raw permutation p only, outside the Holm/BH family by construction. | raw_p | 0.019449027548622568 | 0.006349682515874206 |

## `results/correlates-spearman.csv` (19 cells)

| line | row | column | old | new |
|---|---|---|---|---|
| 2 | Tax within-$1 (domain-matched) / Mean |center|, labor-and-tax / False | spearman_rho | 0.08514716666010344 | 0.0741957625880644 |
| 2 | Tax within-$1 (domain-matched) / Mean |center|, labor-and-tax / False | raw_p | 0.6653167341632918 | 0.704314784260787 |
| 2 | Tax within-$1 (domain-matched) / Mean |center|, labor-and-tax / False | bh_adjusted_p | 0.760361981900905 | 0.8049311820123279 |
| 3 | Tax within-$1 (domain-matched) / Mean |center|, macro-and-trade / False | spearman_rho | 0.23572897265064005 | 0.2372672597164746 |
| 3 | Tax within-$1 (domain-matched) / Mean |center|, macro-and-trade / False | raw_p | 0.22663866806659666 | 0.22308884555772213 |
| 3 | Tax within-$1 (domain-matched) / Mean |center|, macro-and-trade / False | bh_adjusted_p | 0.4532773361331933 | 0.44617769111544425 |
| 4 | Tax within-$1 (domain-matched) / Avg interval-width rank (1 = tightest) / False | spearman_rho | -0.27443467055234627 | -0.25359441563225327 |
| 4 | Tax within-$1 (domain-matched) / Avg interval-width rank (1 = tightest) / False | raw_p | 0.15809209539523023 | 0.19264036798160092 |
| 4 | Tax within-$1 (domain-matched) / Avg interval-width rank (1 = tightest) / False | holm_adjusted_p | 0.9485525723713814 | 1.0 |
| 4 | Tax within-$1 (domain-matched) / Avg interval-width rank (1 = tightest) / False | bh_adjusted_p | 0.4215789210539473 | 0.44617769111544425 |
| 7 | Overall within-$1 (leaderboard headline) / Mean |center|, labor-and-tax / False | spearman_rho | 0.02079912424740011 | 0.014230979748221127 |
| 7 | Overall within-$1 (leaderboard headline) / Mean |center|, labor-and-tax / False | raw_p | 0.9154542272886356 | 0.9419029048547573 |
| 7 | Overall within-$1 (leaderboard headline) / Mean |center|, labor-and-tax / False | bh_adjusted_p | 0.9154542272886356 | 0.9419029048547573 |
| 8 | Overall within-$1 (leaderboard headline) / Mean |center|, macro-and-trade / False | spearman_rho | 0.11548987411056376 | 0.11824278200233504 |
| 8 | Overall within-$1 (leaderboard headline) / Mean |center|, macro-and-trade / False | raw_p | 0.5545222738863057 | 0.5458227088645567 |
| 8 | Overall within-$1 (leaderboard headline) / Mean |center|, macro-and-trade / False | bh_adjusted_p | 0.7393630318484076 | 0.727763611819409 |
| 9 | Overall within-$1 (leaderboard headline) / Avg interval-width rank (1 = tightest) / False | spearman_rho | -0.18004949760951985 | -0.16671229751397384 |
| 9 | Overall within-$1 (leaderboard headline) / Avg interval-width rank (1 = tightest) / False | raw_p | 0.35703214839258035 | 0.39378031098445077 |
| 9 | Overall within-$1 (leaderboard headline) / Avg interval-width rank (1 = tightest) / False | bh_adjusted_p | 0.5712514374281286 | 0.6300484975751213 |

## `results/deepseek-v4-pro-armington-clarify-batch15/summary.csv` (2 cells)

| line | row | column | old | new |
|---|---|---|---|---|
| 2 | deepseek-v4-pro / trade.armington_elasticity.import_domestic / Armington elasticity | between_run_sd | 0.3575223380744513 | 0.3643161020627859 |
| 2 | deepseek-v4-pro / trade.armington_elasticity.import_domestic / Armington elasticity | total_sd | 2.6230367261376015 | 2.623971354010304 |

## `results/deepseek-v4-pro-elasticities-batch15/summary.csv` (52 cells)

| line | row | column | old | new |
|---|---|---|---|---|
| 2 | deepseek-v4-pro / household.annual_discount_factor / Annual discount factor | between_run_sd | 0.00869226987360354 | 0.008150766835089814 |
| 2 | deepseek-v4-pro / household.annual_discount_factor / Annual discount factor | total_sd | 0.12728596959427835 | 0.12725013752448364 |
| 3 | deepseek-v4-pro / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | between_run_sd | 0.06798692684790378 | 0.06879720601561924 |
| 3 | deepseek-v4-pro / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | total_sd | 0.7855324406272333 | 0.785602984089999 |
| 4 | deepseek-v4-pro / household.relative_risk_aversion.crra / Coefficient of relative risk aversion | between_run_sd | 0.0 | 0.4087856678287806 |
| 4 | deepseek-v4-pro / household.relative_risk_aversion.crra / Coefficient of relative risk aversion | total_sd | 6.5680575197948246 | 6.580766315981411 |
| 5 | deepseek-v4-pro / labor_supply.extensive_margin.single_mothers / Employment participation elasticity of single mothers | between_run_sd | 0.053748384988657 | 0.047220375780894525 |
| 5 | deepseek-v4-pro / labor_supply.extensive_margin.single_mothers / Employment participation elasticity of single mothers | total_sd | 0.6808905014758247 | 0.6804063124339751 |
| 6 | deepseek-v4-pro / labor_supply.frisch_elasticity.prime_age / Frisch elasticity of labor supply | between_run_sd | 0.09345230512584125 | 0.09606840734023277 |
| 6 | deepseek-v4-pro / labor_supply.frisch_elasticity.prime_age / Frisch elasticity of labor supply | total_sd | 1.2807314397770257 | 1.280924988587891 |
| 7 | deepseek-v4-pro / labor_supply.income_elasticity.prime_age / Income elasticity of labor supply | between_run_sd | 0.0272437556556034 | 0.03193563839975647 |
| 7 | deepseek-v4-pro / labor_supply.income_elasticity.prime_age / Income elasticity of labor supply | total_sd | 0.3077746334576649 | 0.3082253847069994 |
| 8 | deepseek-v4-pro / labor_supply.marshallian_wage_elasticity.prime_age / Uncompensated wage elasticity of labor supply | between_run_sd | 0.0541602560309064 | 0.05275690054917514 |
| 8 | deepseek-v4-pro / labor_supply.marshallian_wage_elasticity.prime_age / Uncompensated wage elasticity of labor supply | total_sd | 0.6107341813569778 | 0.6106113309626673 |
| 9 | deepseek-v4-pro / labor_supply.policy_response.substitution_elasticity.all / Substitution elasticity of labor supply in a tax-benefit simulation | between_run_sd | 0.02357022603955158 | 0.02871870277169373 |
| 9 | deepseek-v4-pro / labor_supply.policy_response.substitution_elasticity.all / Substitution elasticity of labor supply in a tax-benefit simulation | total_sd | 0.645287968662054 | 0.6454965304580137 |
| 10 | deepseek-v4-pro / labor_supply.policy_response.substitution_elasticity.primary.decile_1 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 1 | between_run_sd | 0.05734883511361751 | 0.05599770828644092 |
| 10 | deepseek-v4-pro / labor_supply.policy_response.substitution_elasticity.primary.decile_1 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 1 | total_sd | 0.6401782293063221 | 0.640058606474612 |
| 11 | deepseek-v4-pro / labor_supply.policy_response.substitution_elasticity.primary.decile_10 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 10 | between_run_sd | 0.0590668171555645 | 0.05354752302602075 |
| 11 | deepseek-v4-pro / labor_supply.policy_response.substitution_elasticity.primary.decile_10 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 10 | total_sd | 0.6402942867237776 | 0.6398087385652407 |
| 12 | deepseek-v4-pro / labor_supply.policy_response.substitution_elasticity.primary.decile_2 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 2 | between_run_sd | 0.04642796092394707 | 0.04773676081735473 |
| 12 | deepseek-v4-pro / labor_supply.policy_response.substitution_elasticity.primary.decile_2 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 2 | total_sd | 0.6384739074978363 | 0.6385704137629095 |
| 13 | deepseek-v4-pro / labor_supply.policy_response.substitution_elasticity.primary.decile_3 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 3 | between_run_sd | 0.05055250296034367 | 0.049407714197503845 |
| 13 | deepseek-v4-pro / labor_supply.policy_response.substitution_elasticity.primary.decile_3 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 3 | total_sd | 0.6357456601853012 | 0.635655654510452 |
| 14 | deepseek-v4-pro / labor_supply.policy_response.substitution_elasticity.primary.decile_4 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 4 | between_run_sd | 0.04508756911709578 | 0.044150166729268664 |
| 14 | deepseek-v4-pro / labor_supply.policy_response.substitution_elasticity.primary.decile_4 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 4 | total_sd | 0.6378669858729692 | 0.6378014110990976 |
| 15 | deepseek-v4-pro / labor_supply.policy_response.substitution_elasticity.primary.decile_5 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 5 | between_run_sd | 0.0541602560309064 | 0.05319063200727487 |
| 15 | deepseek-v4-pro / labor_supply.policy_response.substitution_elasticity.primary.decile_5 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 5 | total_sd | 0.63985680689771 | 0.6397754632160672 |
| 16 | deepseek-v4-pro / labor_supply.policy_response.substitution_elasticity.primary.decile_6 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 6 | between_run_sd | 0.04166533331199932 | 0.037266256706152946 |
| 16 | deepseek-v4-pro / labor_supply.policy_response.substitution_elasticity.primary.decile_6 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 6 | total_sd | 0.6359894019906657 | 0.6357163623294066 |
| 17 | deepseek-v4-pro / labor_supply.policy_response.substitution_elasticity.primary.decile_7 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 7 | between_run_sd | 0.058309518948453 | 0.0521244877406217 |
| 17 | deepseek-v4-pro / labor_supply.policy_response.substitution_elasticity.primary.decile_7 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 7 | total_sd | 0.6380503202029689 | 0.6375148416573008 |
| 18 | deepseek-v4-pro / labor_supply.policy_response.substitution_elasticity.primary.decile_8 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 8 | between_run_sd | 0.04422166387140534 | 0.05364299167231034 |
| 18 | deepseek-v4-pro / labor_supply.policy_response.substitution_elasticity.primary.decile_8 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 8 | total_sd | 0.6423849280869947 | 0.643102177599589 |
| 19 | deepseek-v4-pro / labor_supply.policy_response.substitution_elasticity.primary.decile_9 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 9 | between_run_sd | 0.0640694068092478 | 0.0630584913658211 |
| 19 | deepseek-v4-pro / labor_supply.policy_response.substitution_elasticity.primary.decile_9 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 9 | total_sd | 0.6404961921996275 | 0.6403958593453479 |
| 20 | deepseek-v4-pro / labor_supply.policy_response.substitution_elasticity.secondary / Secondary-earner substitution elasticity in a tax-benefit simulation | between_run_sd | 0.0674948557710553 | 0.06307050728263482 |
| 20 | deepseek-v4-pro / labor_supply.policy_response.substitution_elasticity.secondary / Secondary-earner substitution elasticity in a tax-benefit simulation | total_sd | 0.6564617647746981 | 0.6560216322229355 |
| 21 | deepseek-v4-pro / macro.tfp_persistence.ar1 / TFP persistence | between_run_sd | 0.005416025603090645 | 0.00660331356214439 |
| 21 | deepseek-v4-pro / macro.tfp_persistence.ar1 / TFP persistence | total_sd | 0.1276910727868023 | 0.12774693924361205 |
| 22 | deepseek-v4-pro / production.capital_labor_substitution / Elasticity of substitution between capital and labor | between_run_sd | 0.062360956446232366 | 0.07419915018980264 |
| 22 | deepseek-v4-pro / production.capital_labor_substitution / Elasticity of substitution between capital and labor | total_sd | 1.2683174686918448 | 1.2689546195151695 |
| 23 | deepseek-v4-pro / production.capital_share / Capital share in production | between_run_sd | 0.012649110640673502 | 0.011652968148358893 |
| 23 | deepseek-v4-pro / production.capital_share / Capital share in production | total_sd | 0.11156005482847942 | 0.11145150290597251 |
| 24 | deepseek-v4-pro / tax.capital_gains_realizations.elasticity / Capital gains realizations elasticity | between_run_sd | 0.19821424996424675 | 0.20170409432301234 |
| 24 | deepseek-v4-pro / tax.capital_gains_realizations.elasticity / Capital gains realizations elasticity | total_sd | 1.335157463143913 | 1.3356800156349824 |
| 25 | deepseek-v4-pro / tax.capital_gains_realizations.elasticity.net_of_tax_rate / Capital gains realizations elasticity (net-of-tax-rate convention) | between_run_sd | 0.33025242870668897 | 0.3373176873841961 |
| 25 | deepseek-v4-pro / tax.capital_gains_realizations.elasticity.net_of_tax_rate / Capital gains realizations elasticity (net-of-tax-rate convention) | total_sd | 1.4340443488415708 | 1.435687901321175 |
| 26 | deepseek-v4-pro / tax.elasticity_of_taxable_income.top_earners / Elasticity of taxable income | between_run_sd | 0.14704496666741854 | 0.16302636971429568 |
| 26 | deepseek-v4-pro / tax.elasticity_of_taxable_income.top_earners / Elasticity of taxable income | total_sd | 0.7523519834123151 | 0.7556380627949101 |
| 27 | deepseek-v4-pro / trade.armington_elasticity.import_domestic / Armington elasticity | between_run_sd | 0.3844765561412324 | 0.386147064672976 |
| 27 | deepseek-v4-pro / trade.armington_elasticity.import_domestic / Armington elasticity | total_sd | 2.606434985441481 | 2.6066819266390495 |

## `results/deepseek-v4-pro-ies-clarify-batch15/summary.csv` (2 cells)

| line | row | column | old | new |
|---|---|---|---|---|
| 2 | deepseek-v4-pro / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | between_run_sd | 0.0 | 0.04551525995629258 |
| 2 | deepseek-v4-pro / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | total_sd | 0.7542726444875368 | 0.7556446659052858 |

## `results/elasticity-all-model-comparison.csv` (74 cells)

| line | row | column | old | new |
|---|---|---|---|---|
| 392 | gemini-3.5-flash-elasticities-batch15 / gemini-3.5-flash / household.annual_discount_factor | pooled_point_estimate | 0.9599999999999999 | 0.9606666666666667 |
| 392 | gemini-3.5-flash-elasticities-batch15 / gemini-3.5-flash / household.annual_discount_factor | reml_predictive_90_interval | [0.8682, 0.9889] | [0.8694, 0.989] |
| 392 | gemini-3.5-flash-elasticities-batch15 / gemini-3.5-flash / household.annual_discount_factor | bayes_predictive_90_interval | [0.921, 0.9805] | [0.9219, 0.9807] |
| 393 | gemini-3.5-flash-elasticities-batch15 / gemini-3.5-flash / household.intertemporal_elasticity_of_substitution | pooled_point_estimate | 0.9333333333333333 | 0.9866666666666667 |
| 393 | gemini-3.5-flash-elasticities-batch15 / gemini-3.5-flash / household.intertemporal_elasticity_of_substitution | reml_predictive_90_interval | [0.01868, 4.648] | [0.02079, 4.681] |
| 393 | gemini-3.5-flash-elasticities-batch15 / gemini-3.5-flash / household.intertemporal_elasticity_of_substitution | bayes_predictive_90_interval | [0.09686, 3.572] | [0.1308, 3.477] |
| 396 | gemini-3.5-flash-elasticities-batch15 / gemini-3.5-flash / labor_supply.frisch_elasticity.prime_age | pooled_point_estimate | 0.39333333333333337 | 0.4 |
| 396 | gemini-3.5-flash-elasticities-batch15 / gemini-3.5-flash / labor_supply.frisch_elasticity.prime_age | reml_predictive_90_interval | [0.1012, 1.404] | [0.1034, 1.429] |
| 396 | gemini-3.5-flash-elasticities-batch15 / gemini-3.5-flash / labor_supply.frisch_elasticity.prime_age | bayes_predictive_90_interval | [0.1833, 0.8208] | [0.1876, 0.8345] |
| 397 | gemini-3.5-flash-elasticities-batch15 / gemini-3.5-flash / labor_supply.income_elasticity.prime_age | pooled_point_estimate | 0.011 | -0.030333333333333334 |
| 397 | gemini-3.5-flash-elasticities-batch15 / gemini-3.5-flash / labor_supply.income_elasticity.prime_age | pooled_90_interval | [-0.1452, 0.15] | [-0.1494, 0.009901] |
| 397 | gemini-3.5-flash-elasticities-batch15 / gemini-3.5-flash / labor_supply.income_elasticity.prime_age | reml_predictive_90_interval | [-0.1088, 0.1314] | [-0.09334, 0.03845] |
| 397 | gemini-3.5-flash-elasticities-batch15 / gemini-3.5-flash / labor_supply.income_elasticity.prime_age | bayes_predictive_90_interval | [-0.1197, 0.1401] | [-0.06481, 0.01105] |
| 398 | gemini-3.5-flash-elasticities-batch15 / gemini-3.5-flash / labor_supply.marshallian_wage_elasticity.prime_age | pooled_point_estimate | 0.07333333333333333 | 0.05333333333333334 |
| 398 | gemini-3.5-flash-elasticities-batch15 / gemini-3.5-flash / labor_supply.marshallian_wage_elasticity.prime_age | pooled_90_interval | [-0.1477, 0.3462] | [-0.1495, 0.3462] |
| 398 | gemini-3.5-flash-elasticities-batch15 / gemini-3.5-flash / labor_supply.marshallian_wage_elasticity.prime_age | reml_predictive_90_interval | [-0.09987, 0.2932] | [-0.1557, 0.2724] |
| 398 | gemini-3.5-flash-elasticities-batch15 / gemini-3.5-flash / labor_supply.marshallian_wage_elasticity.prime_age | bayes_predictive_90_interval | [-0.02557, 0.2115] | [-0.06569, 0.1751] |
| 399 | gemini-3.5-flash-elasticities-batch15 / gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.all | pooled_point_estimate | 0.24333333333333332 | 0.24666666666666667 |
| 399 | gemini-3.5-flash-elasticities-batch15 / gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.all | reml_predictive_90_interval | [0.0853, 0.6481] | [0.0872, 0.6609] |
| 399 | gemini-3.5-flash-elasticities-batch15 / gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.all | bayes_predictive_90_interval | [0.1354, 0.4249] | [0.1387, 0.4327] |
| 401 | gemini-3.5-flash-elasticities-batch15 / gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_10 | pooled_point_estimate | 0.14 | 0.152 |
| 401 | gemini-3.5-flash-elasticities-batch15 / gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_10 | reml_predictive_90_interval | [0.0445, 0.4165] | [0.04884, 0.4538] |
| 401 | gemini-3.5-flash-elasticities-batch15 / gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_10 | bayes_predictive_90_interval | [0.07178, 0.2652] | [0.08013, 0.285] |
| 403 | gemini-3.5-flash-elasticities-batch15 / gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_3 | pooled_point_estimate | 0.14400000000000002 | 0.14866666666666667 |
| 403 | gemini-3.5-flash-elasticities-batch15 / gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_3 | reml_predictive_90_interval | [0.03763, 0.5109] | [0.03903, 0.528] |
| 403 | gemini-3.5-flash-elasticities-batch15 / gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_3 | bayes_predictive_90_interval | [0.06703, 0.2985] | [0.0701, 0.3066] |
| 404 | gemini-3.5-flash-elasticities-batch15 / gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_4 | pooled_point_estimate | 0.13866666666666666 | 0.142 |
| 404 | gemini-3.5-flash-elasticities-batch15 / gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_4 | reml_predictive_90_interval | [0.04175, 0.4495] | [0.04245, 0.4564] |
| 404 | gemini-3.5-flash-elasticities-batch15 / gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_4 | bayes_predictive_90_interval | [0.07083, 0.2734] | [0.0722, 0.2771] |
| 405 | gemini-3.5-flash-elasticities-batch15 / gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_5 | pooled_point_estimate | 0.13933333333333334 | 0.14400000000000002 |
| 405 | gemini-3.5-flash-elasticities-batch15 / gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_5 | reml_predictive_90_interval | [0.04052, 0.4417] | [0.04256, 0.4621] |
| 405 | gemini-3.5-flash-elasticities-batch15 / gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_5 | bayes_predictive_90_interval | [0.06772, 0.2726] | [0.07197, 0.2823] |
| 406 | gemini-3.5-flash-elasticities-batch15 / gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_6 | pooled_point_estimate | 0.156 | 0.14400000000000002 |
| 406 | gemini-3.5-flash-elasticities-batch15 / gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_6 | reml_predictive_90_interval | [0.03992, 0.5565] | [0.03725, 0.5229] |
| 406 | gemini-3.5-flash-elasticities-batch15 / gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_6 | bayes_predictive_90_interval | [0.06599, 0.3492] | [0.0677, 0.3002] |
| 407 | gemini-3.5-flash-elasticities-batch15 / gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_7 | pooled_point_estimate | 0.14066666666666666 | 0.14400000000000002 |
| 407 | gemini-3.5-flash-elasticities-batch15 / gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_7 | reml_predictive_90_interval | [0.04269, 0.4357] | [0.04379, 0.4461] |
| 407 | gemini-3.5-flash-elasticities-batch15 / gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_7 | bayes_predictive_90_interval | [0.07166, 0.2675] | [0.07352, 0.2741] |
| 411 | gemini-3.5-flash-elasticities-batch15 / gemini-3.5-flash / macro.tfp_persistence.ar1 | pooled_point_estimate | 0.9546666666666667 | 0.956 |
| 411 | gemini-3.5-flash-elasticities-batch15 / gemini-3.5-flash / macro.tfp_persistence.ar1 | reml_predictive_90_interval | [0.8367, 0.9882] | [0.8411, 0.9886] |
| 411 | gemini-3.5-flash-elasticities-batch15 / gemini-3.5-flash / macro.tfp_persistence.ar1 | bayes_predictive_90_interval | [0.9043, 0.9785] | [0.9067, 0.9793] |
| 412 | gemini-3.5-flash-elasticities-batch15 / gemini-3.5-flash / production.capital_labor_substitution | pooled_point_estimate | 0.7733333333333333 | 0.74 |
| 412 | gemini-3.5-flash-elasticities-batch15 / gemini-3.5-flash / production.capital_labor_substitution | reml_predictive_90_interval | [0.4318, 1.321] | [0.4166, 1.278] |
| 412 | gemini-3.5-flash-elasticities-batch15 / gemini-3.5-flash / production.capital_labor_substitution | bayes_predictive_90_interval | [0.5402, 1.073] | [0.5368, 1.01] |
| 414 | gemini-3.5-flash-elasticities-batch15 / gemini-3.5-flash / tax.capital_gains_realizations.elasticity | pooled_point_estimate | 0.010000000000000009 | -0.55 |
| 414 | gemini-3.5-flash-elasticities-batch15 / gemini-3.5-flash / tax.capital_gains_realizations.elasticity | pooled_90_interval | [-1.139, 1.3] | [-1.293, -0.0263] |
| 414 | gemini-3.5-flash-elasticities-batch15 / gemini-3.5-flash / tax.capital_gains_realizations.elasticity | reml_predictive_90_interval | [-1.971, 1.293] | [-0.9997, -0.02719] |
| 414 | gemini-3.5-flash-elasticities-batch15 / gemini-3.5-flash / tax.capital_gains_realizations.elasticity | bayes_predictive_90_interval | [-2.165, 1.337] | [-0.9257, -0.1071] |
| 518 | kimi-k2.6-elasticities-batch15 / kimi-k2.6 / tax.capital_gains_realizations.elasticity | pooled_point_estimate | -0.38999999999999996 | -0.4533333333333333 |
| 518 | kimi-k2.6-elasticities-batch15 / kimi-k2.6 / tax.capital_gains_realizations.elasticity | pooled_90_interval | [-1.499, 0.7] | [-1.513, 0.06911] |
| 518 | kimi-k2.6-elasticities-batch15 / kimi-k2.6 / tax.capital_gains_realizations.elasticity | reml_predictive_90_interval | [-1.289, 0.4287] | [-0.9892, 0.09498] |
| 518 | kimi-k2.6-elasticities-batch15 / kimi-k2.6 / tax.capital_gains_realizations.elasticity | bayes_predictive_90_interval | [-1.262, 0.3776] | [-0.7745, -0.07156] |
| 526 | glm-5.2-elasticities-batch15 / glm-5.2 / labor_supply.frisch_elasticity.prime_age | pooled_point_estimate | 0.43666666666666665 | 0.43 |
| 526 | glm-5.2-elasticities-batch15 / glm-5.2 / labor_supply.frisch_elasticity.prime_age | reml_predictive_90_interval | [0.03161, 4.066] | [0.03104, 4.021] |
| 526 | glm-5.2-elasticities-batch15 / glm-5.2 / labor_supply.frisch_elasticity.prime_age | bayes_predictive_90_interval | [0.1059, 1.688] | [0.104, 1.661] |
| 566 | minimax-m3-elasticities-batch15 / minimax-m3 / labor_supply.policy_response.substitution_elasticity.secondary | pooled_point_estimate | 0.36000000000000004 | 0.38 |
| 566 | minimax-m3-elasticities-batch15 / minimax-m3 / labor_supply.policy_response.substitution_elasticity.secondary | reml_predictive_90_interval | [0.08447, 1.222] | [0.09083, 1.291] |
| 566 | minimax-m3-elasticities-batch15 / minimax-m3 / labor_supply.policy_response.substitution_elasticity.secondary | bayes_predictive_90_interval | [0.1295, 0.8598] | [0.1535, 0.8427] |
| 701 | kimi-k3-elasticities-batch15 / kimi-k3 / tax.capital_gains_realizations.elasticity.net_of_tax_rate | pooled_point_estimate | 0.85 | 0.7166666666666667 |
| 701 | kimi-k3-elasticities-batch15 / kimi-k3 / tax.capital_gains_realizations.elasticity.net_of_tax_rate | reml_predictive_90_interval | [-0.1144, 1.552] | [-0.1503, 1.496] |
| 701 | kimi-k3-elasticities-batch15 / kimi-k3 / tax.capital_gains_realizations.elasticity.net_of_tax_rate | bayes_predictive_90_interval | [-0.09545, 1.533] | [0.08824, 1.151] |
| 794 | inkling-elasticities-batch15 / inkling / labor_supply.policy_response.substitution_elasticity.primary.decile_4 | pooled_point_estimate | 0.19266666666666668 | 0.2006666666666667 |
| 794 | inkling-elasticities-batch15 / inkling / labor_supply.policy_response.substitution_elasticity.primary.decile_4 | reml_predictive_90_interval | [0.07643, 0.452] | [0.081, 0.4769] |
| 794 | inkling-elasticities-batch15 / inkling / labor_supply.policy_response.substitution_elasticity.primary.decile_4 | bayes_predictive_90_interval | [0.1088, 0.3244] | [0.1193, 0.3314] |
| 801 | inkling-elasticities-batch15 / inkling / macro.tfp_persistence.ar1 | pooled_point_estimate | 0.948 | 0.952 |
| 801 | inkling-elasticities-batch15 / inkling / macro.tfp_persistence.ar1 | reml_predictive_90_interval | [0.8494, 0.984] | [0.8579, 0.9851] |
| 801 | inkling-elasticities-batch15 / inkling / macro.tfp_persistence.ar1 | bayes_predictive_90_interval | [0.903, 0.9739] | [0.9106, 0.9751] |
| 804 | inkling-elasticities-batch15 / inkling / tax.capital_gains_realizations.elasticity | pooled_point_estimate | -0.36666666666666664 | -0.48000000000000004 |
| 804 | inkling-elasticities-batch15 / inkling / tax.capital_gains_realizations.elasticity | pooled_90_interval | [-1.563, 1.2] | [-1.597, -0.05661] |
| 804 | inkling-elasticities-batch15 / inkling / tax.capital_gains_realizations.elasticity | reml_predictive_90_interval | [-1.66, 0.6498] | [-0.939, -0.04352] |
| 804 | inkling-elasticities-batch15 / inkling / tax.capital_gains_realizations.elasticity | bayes_predictive_90_interval | [-1.676, 0.6487] | [-0.7381, -0.2065] |
| 807 | inkling-elasticities-batch15 / inkling / trade.armington_elasticity.import_domestic | pooled_point_estimate | 1.66 | 1.7133333333333334 |
| 807 | inkling-elasticities-batch15 / inkling / trade.armington_elasticity.import_domestic | reml_predictive_90_interval | [0.6465, 3.676] | [0.683, 3.849] |
| 807 | inkling-elasticities-batch15 / inkling / trade.armington_elasticity.import_domestic | bayes_predictive_90_interval | [0.898, 2.761] | [1.01, 2.737] |

## `results/elasticity-model-rollup.csv` (9 cells)

| line | row | column | old | new |
|---|---|---|---|---|
| 17 | gemini-3.5-flash | mean_pooled_interval_width | 1.1845444863048173 | 1.134285622420689 |
| 17 | gemini-3.5-flash | mean_pooled_point_estimate | 0.45365384615384613 | 0.43160256410256415 |
| 21 | kimi-k2.6 | mean_pooled_interval_width | 1.5618333333266936 | 1.5380819071909526 |
| 21 | kimi-k2.6 | mean_pooled_point_estimate | 0.47333333333333333 | 0.47089743589743593 |
| 22 | glm-5.2 | mean_pooled_point_estimate | 0.4959871794871795 | 0.4957307692307692 |
| 23 | minimax-m3 | mean_pooled_point_estimate | 0.4439615384615384 | 0.44473076923076926 |
| 28 | kimi-k3 | mean_pooled_point_estimate | 0.47871794871794876 | 0.47358974358974354 |
| 32 | inkling | mean_pooled_interval_width | 1.2245120862101417 | 1.177497001996292 |
| 32 | inkling | mean_pooled_point_estimate | 0.46847435897435896 | 0.46662820512820513 |

## `results/gemini-3-flash-preview-armington-clarify-batch15/summary.csv` (3 cells)

| line | row | column | old | new |
|---|---|---|---|---|
| 2 | gemini-3-flash-preview / trade.armington_elasticity.import_domestic / Armington elasticity | pooled_upper_bound | 5.902517142197389 | 5.923188148479939 |
| 2 | gemini-3-flash-preview / trade.armington_elasticity.import_domestic / Armington elasticity | between_run_sd | 0.20928844424038795 | 0.33184464402577757 |
| 2 | gemini-3-flash-preview / trade.armington_elasticity.import_domestic / Armington elasticity | total_sd | 2.632325331886726 | 2.6448924113786925 |

## `results/gemini-3-flash-preview-elasticities-batch15/summary.csv` (50 cells)

| line | row | column | old | new |
|---|---|---|---|---|
| 2 | gemini-3-flash-preview / household.annual_discount_factor / Annual discount factor | between_run_sd | 0.00869226987360354 | 0.006792591961508924 |
| 2 | gemini-3-flash-preview / household.annual_discount_factor / Annual discount factor | total_sd | 0.1284333133272759 | 0.12831874267706267 |
| 3 | gemini-3-flash-preview / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | between_run_sd | 0.0 | 0.06067445005015616 |
| 3 | gemini-3-flash-preview / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | total_sd | 0.7857147091449076 | 0.7880539277584725 |
| 4 | gemini-3-flash-preview / household.relative_risk_aversion.crra / Coefficient of relative risk aversion | between_run_sd | 0.0 | 0.10503121229213501 |
| 4 | gemini-3-flash-preview / household.relative_risk_aversion.crra / Coefficient of relative risk aversion | total_sd | 6.887210802559255 | 6.888011628506767 |
| 5 | gemini-3-flash-preview / labor_supply.extensive_margin.single_mothers / Employment participation elasticity of single mothers | between_run_sd | 0.0 | 0.010630799071042973 |
| 5 | gemini-3-flash-preview / labor_supply.extensive_margin.single_mothers / Employment participation elasticity of single mothers | total_sd | 0.6767450950033632 | 0.6768285879748284 |
| 6 | gemini-3-flash-preview / labor_supply.frisch_elasticity.prime_age / Frisch elasticity of labor supply | between_run_sd | 0.012472191289246468 | 0.029523295886469052 |
| 6 | gemini-3-flash-preview / labor_supply.frisch_elasticity.prime_age / Frisch elasticity of labor supply | total_sd | 1.300494270353477 | 1.3007695478702854 |
| 8 | gemini-3-flash-preview / labor_supply.marshallian_wage_elasticity.prime_age / Uncompensated wage elasticity of labor supply | between_run_sd | 0.0 | 0.009565563234854482 |
| 8 | gemini-3-flash-preview / labor_supply.marshallian_wage_elasticity.prime_age / Uncompensated wage elasticity of labor supply | total_sd | 0.6143960449091449 | 0.614470503767268 |
| 9 | gemini-3-flash-preview / labor_supply.policy_response.substitution_elasticity.all / Substitution elasticity of labor supply in a tax-benefit simulation | between_run_sd | 0.0 | 0.01211548595806209 |
| 9 | gemini-3-flash-preview / labor_supply.policy_response.substitution_elasticity.all / Substitution elasticity of labor supply in a tax-benefit simulation | total_sd | 0.6397551973216005 | 0.6398699066997916 |
| 10 | gemini-3-flash-preview / labor_supply.policy_response.substitution_elasticity.primary.decile_1 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 1 | between_run_sd | 0.016275407487644934 | 0.013387556411334607 |
| 10 | gemini-3-flash-preview / labor_supply.policy_response.substitution_elasticity.primary.decile_1 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 1 | total_sd | 0.6404798374829782 | 0.6404129605184454 |
| 11 | gemini-3-flash-preview / labor_supply.policy_response.substitution_elasticity.primary.decile_10 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 10 | between_run_sd | 0.02867441755680876 | 0.029946034795945854 |
| 11 | gemini-3-flash-preview / labor_supply.policy_response.substitution_elasticity.primary.decile_10 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 10 | total_sd | 0.6383664982681274 | 0.6384248811637034 |
| 12 | gemini-3-flash-preview / labor_supply.policy_response.substitution_elasticity.primary.decile_2 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 2 | between_run_sd | 0.014696938456699069 | 0.01424952240915073 |
| 12 | gemini-3-flash-preview / labor_supply.policy_response.substitution_elasticity.primary.decile_2 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 2 | total_sd | 0.6393258287272444 | 0.6393156999219296 |
| 13 | gemini-3-flash-preview / labor_supply.policy_response.substitution_elasticity.primary.decile_3 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 3 | between_run_sd | 0.01414213562373095 | 0.017055220771234704 |
| 13 | gemini-3-flash-preview / labor_supply.policy_response.substitution_elasticity.primary.decile_3 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 3 | total_sd | 0.6374204808793363 | 0.6374917646526894 |
| 14 | gemini-3-flash-preview / labor_supply.policy_response.substitution_elasticity.primary.decile_4 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 4 | between_run_sd | 0.015860503004493758 | 0.017630198209007433 |
| 14 | gemini-3-flash-preview / labor_supply.policy_response.substitution_elasticity.primary.decile_4 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 4 | total_sd | 0.6361636079744826 | 0.6362101888876384 |
| 15 | gemini-3-flash-preview / labor_supply.policy_response.substitution_elasticity.primary.decile_5 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 5 | between_run_sd | 0.0220504472113883 | 0.02282174888614416 |
| 15 | gemini-3-flash-preview / labor_supply.policy_response.substitution_elasticity.primary.decile_5 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 5 | total_sd | 0.6374959945407936 | 0.6375231392314757 |
| 16 | gemini-3-flash-preview / labor_supply.policy_response.substitution_elasticity.primary.decile_6 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 6 | between_run_sd | 0.02054804667656325 | 0.020479434128467085 |
| 16 | gemini-3-flash-preview / labor_supply.policy_response.substitution_elasticity.primary.decile_6 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 6 | total_sd | 0.6371344289516582 | 0.6371322198378886 |
| 17 | gemini-3-flash-preview / labor_supply.policy_response.substitution_elasticity.primary.decile_7 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 7 | between_run_sd | 0.021249836600678966 | 0.023060331499978246 |
| 17 | gemini-3-flash-preview / labor_supply.policy_response.substitution_elasticity.primary.decile_7 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 7 | total_sd | 0.6376446230289861 | 0.637707525916945 |
| 18 | gemini-3-flash-preview / labor_supply.policy_response.substitution_elasticity.primary.decile_8 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 8 | between_run_sd | 0.024349309823666232 | 0.030368688187378496 |
| 18 | gemini-3-flash-preview / labor_supply.policy_response.substitution_elasticity.primary.decile_8 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 8 | total_sd | 0.6360193709925648 | 0.6362782477903132 |
| 19 | gemini-3-flash-preview / labor_supply.policy_response.substitution_elasticity.primary.decile_9 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 9 | between_run_sd | 0.018926759422104516 | 0.01872708970686286 |
| 19 | gemini-3-flash-preview / labor_supply.policy_response.substitution_elasticity.primary.decile_9 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 9 | total_sd | 0.6365688024697549 | 0.6365628970843686 |
| 20 | gemini-3-flash-preview / labor_supply.policy_response.substitution_elasticity.secondary / Secondary-earner substitution elasticity in a tax-benefit simulation | between_run_sd | 0.042687494916219 | 0.04111517022003221 |
| 20 | gemini-3-flash-preview / labor_supply.policy_response.substitution_elasticity.secondary / Secondary-earner substitution elasticity in a tax-benefit simulation | total_sd | 0.6485118145501368 | 0.6484102163068617 |
| 21 | gemini-3-flash-preview / macro.tfp_persistence.ar1 / TFP persistence | between_run_sd | 0.0 | 0.002812867259971963 |
| 21 | gemini-3-flash-preview / macro.tfp_persistence.ar1 / TFP persistence | total_sd | 0.12752894415473776 | 0.1275599616629154 |
| 22 | gemini-3-flash-preview / production.capital_labor_substitution / Elasticity of substitution between capital and labor | between_run_sd | 0.05617433182117571 | 0.04385154881339233 |
| 22 | gemini-3-flash-preview / production.capital_labor_substitution / Elasticity of substitution between capital and labor | total_sd | 1.2254218944691841 | 1.2249188635261612 |
| 23 | gemini-3-flash-preview / production.capital_share / Capital share in production | between_run_sd | 0.0 | 0.0015068362736394246 |
| 23 | gemini-3-flash-preview / production.capital_share / Capital share in production | total_sd | 0.10472921432596223 | 0.10474005389004193 |
| 24 | gemini-3-flash-preview / tax.capital_gains_realizations.elasticity / Capital gains realizations elasticity | between_run_sd | 0.060184900284225976 | 0.05634874049662119 |
| 24 | gemini-3-flash-preview / tax.capital_gains_realizations.elasticity / Capital gains realizations elasticity | total_sd | 1.3113481321186649 | 1.3111776698618858 |
| 25 | gemini-3-flash-preview / tax.capital_gains_realizations.elasticity.net_of_tax_rate / Capital gains realizations elasticity (net-of-tax-rate convention) | between_run_sd | 0.016996731711975927 | 0.028394052585395787 |
| 25 | gemini-3-flash-preview / tax.capital_gains_realizations.elasticity.net_of_tax_rate / Capital gains realizations elasticity (net-of-tax-rate convention) | total_sd | 1.3306959723518115 | 1.3308903426528673 |
| 26 | gemini-3-flash-preview / tax.elasticity_of_taxable_income.top_earners / Elasticity of taxable income | between_run_sd | 0.0 | 0.010163934058992895 |
| 26 | gemini-3-flash-preview / tax.elasticity_of_taxable_income.top_earners / Elasticity of taxable income | total_sd | 0.6771543552494759 | 0.6772306301319285 |
| 27 | gemini-3-flash-preview / trade.armington_elasticity.import_domestic / Armington elasticity | between_run_sd | 0.22110831935702666 | 0.2657706822724349 |
| 27 | gemini-3-flash-preview / trade.armington_elasticity.import_domestic / Armington elasticity | total_sd | 2.7193311575540857 | 2.7233264789795424 |

## `results/gemini-3-flash-preview-ies-clarify-batch15/summary.csv` (3 cells)

| line | row | column | old | new |
|---|---|---|---|---|
| 2 | gemini-3-flash-preview / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | pooled_upper_bound | 1.6674280916804687 | 1.6708378030449937 |
| 2 | gemini-3-flash-preview / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | between_run_sd | 0.0415739709641549 | 0.06878408246098804 |
| 2 | gemini-3-flash-preview / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | total_sd | 0.723256035923122 | 0.7253289932420321 |

## `results/gemini-3.1-flash-lite-preview-armington-clarify-batch15/summary.csv` (2 cells)

| line | row | column | old | new |
|---|---|---|---|---|
| 2 | gemini-3.1-flash-lite-preview / trade.armington_elasticity.import_domestic / Armington elasticity | between_run_sd | 0.2 | 0.2321681622349531 |
| 2 | gemini-3.1-flash-lite-preview / trade.armington_elasticity.import_domestic / Armington elasticity | total_sd | 2.6228593652729457 | 2.6255081994835887 |

## `results/gemini-3.1-flash-lite-preview-elasticities-batch15/summary.csv` (52 cells)

| line | row | column | old | new |
|---|---|---|---|---|
| 2 | gemini-3.1-flash-lite-preview / household.annual_discount_factor / Annual discount factor | between_run_sd | 0.0 | 0.0016117192338893675 |
| 2 | gemini-3.1-flash-lite-preview / household.annual_discount_factor / Annual discount factor | total_sd | 0.12502653884942455 | 0.12503692676787748 |
| 3 | gemini-3.1-flash-lite-preview / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | between_run_sd | 0.0 | 0.012747548783981955 |
| 3 | gemini-3.1-flash-lite-preview / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | total_sd | 0.6874439371080864 | 0.6875621184057966 |
| 4 | gemini-3.1-flash-lite-preview / household.relative_risk_aversion.crra / Coefficient of relative risk aversion | between_run_sd | 0.0 | 0.076131465242697 |
| 4 | gemini-3.1-flash-lite-preview / household.relative_risk_aversion.crra / Coefficient of relative risk aversion | total_sd | 6.898110480011497 | 6.898530582264925 |
| 5 | gemini-3.1-flash-lite-preview / labor_supply.extensive_margin.single_mothers / Employment participation elasticity of single mothers | between_run_sd | 0.08459051693633013 | 0.08314328328587675 |
| 5 | gemini-3.1-flash-lite-preview / labor_supply.extensive_margin.single_mothers / Employment participation elasticity of single mothers | total_sd | 0.7193814617433507 | 0.7192127206188722 |
| 6 | gemini-3.1-flash-lite-preview / labor_supply.frisch_elasticity.prime_age / Frisch elasticity of labor supply | between_run_sd | 0.028674417556808756 | 0.03523492585489573 |
| 6 | gemini-3.1-flash-lite-preview / labor_supply.frisch_elasticity.prime_age / Frisch elasticity of labor supply | total_sd | 1.2719825950940613 | 1.272147397120318 |
| 7 | gemini-3.1-flash-lite-preview / labor_supply.income_elasticity.prime_age / Income elasticity of labor supply | between_run_sd | 0.012472191289246471 | 0.011874926900359803 |
| 7 | gemini-3.1-flash-lite-preview / labor_supply.income_elasticity.prime_age / Income elasticity of labor supply | total_sd | 0.29512156158286895 | 0.29509692381393005 |
| 8 | gemini-3.1-flash-lite-preview / labor_supply.marshallian_wage_elasticity.prime_age / Uncompensated wage elasticity of labor supply | between_run_sd | 0.0 | 0.005948856099191578 |
| 8 | gemini-3.1-flash-lite-preview / labor_supply.marshallian_wage_elasticity.prime_age / Uncompensated wage elasticity of labor supply | total_sd | 0.5975236803768627 | 0.5975532926024256 |
| 9 | gemini-3.1-flash-lite-preview / labor_supply.policy_response.substitution_elasticity.all / Substitution elasticity of labor supply in a tax-benefit simulation | between_run_sd | 0.04268749491621899 | 0.03404612883851685 |
| 9 | gemini-3.1-flash-lite-preview / labor_supply.policy_response.substitution_elasticity.all / Substitution elasticity of labor supply in a tax-benefit simulation | total_sd | 0.6388685745562663 | 0.63834941233013 |
| 10 | gemini-3.1-flash-lite-preview / labor_supply.policy_response.substitution_elasticity.primary.decile_1 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 1 | between_run_sd | 0.0 | 0.0037612793331820286 |
| 10 | gemini-3.1-flash-lite-preview / labor_supply.policy_response.substitution_elasticity.primary.decile_1 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 1 | total_sd | 0.63509685285002 | 0.6351079905986243 |
| 11 | gemini-3.1-flash-lite-preview / labor_supply.policy_response.substitution_elasticity.primary.decile_10 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 10 | between_run_sd | 0.03957552554574888 | 0.037818844509053956 |
| 11 | gemini-3.1-flash-lite-preview / labor_supply.policy_response.substitution_elasticity.primary.decile_10 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 10 | total_sd | 0.6352229158159974 | 0.6351158914367956 |
| 12 | gemini-3.1-flash-lite-preview / labor_supply.policy_response.substitution_elasticity.primary.decile_2 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 2 | between_run_sd | 0.03895296308797744 | 0.04171365350684221 |
| 12 | gemini-3.1-flash-lite-preview / labor_supply.policy_response.substitution_elasticity.primary.decile_2 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 2 | total_sd | 0.6356741685888385 | 0.6358493093231027 |
| 13 | gemini-3.1-flash-lite-preview / labor_supply.policy_response.substitution_elasticity.primary.decile_3 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 3 | between_run_sd | 0.025525586292102196 | 0.026694797662133025 |
| 13 | gemini-3.1-flash-lite-preview / labor_supply.policy_response.substitution_elasticity.primary.decile_3 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 3 | total_sd | 0.6340788813529259 | 0.6341270254802617 |
| 14 | gemini-3.1-flash-lite-preview / labor_supply.policy_response.substitution_elasticity.primary.decile_4 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 4 | between_run_sd | 0.03259175083088084 | 0.03480091793169957 |
| 14 | gemini-3.1-flash-lite-preview / labor_supply.policy_response.substitution_elasticity.primary.decile_4 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 4 | total_sd | 0.6345928233039583 | 0.6347101173414171 |
| 15 | gemini-3.1-flash-lite-preview / labor_supply.policy_response.substitution_elasticity.primary.decile_5 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 5 | between_run_sd | 0.03479463560186637 | 0.03734720724349934 |
| 15 | gemini-3.1-flash-lite-preview / labor_supply.policy_response.substitution_elasticity.primary.decile_5 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 5 | total_sd | 0.6350018088338192 | 0.635146789682861 |
| 16 | gemini-3.1-flash-lite-preview / labor_supply.policy_response.substitution_elasticity.primary.decile_6 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 6 | between_run_sd | 0.028237091446063158 | 0.028950743609716757 |
| 16 | gemini-3.1-flash-lite-preview / labor_supply.policy_response.substitution_elasticity.primary.decile_6 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 6 | total_sd | 0.6346275723253406 | 0.6346597259774546 |
| 17 | gemini-3.1-flash-lite-preview / labor_supply.policy_response.substitution_elasticity.primary.decile_7 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 7 | between_run_sd | 0.03282275633357645 | 0.034007286800854256 |
| 17 | gemini-3.1-flash-lite-preview / labor_supply.policy_response.substitution_elasticity.primary.decile_7 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 7 | total_sd | 0.6346970438721139 | 0.6347594030199335 |
| 18 | gemini-3.1-flash-lite-preview / labor_supply.policy_response.substitution_elasticity.primary.decile_8 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 8 | between_run_sd | 0.03881580434135903 | 0.04148801701160897 |
| 18 | gemini-3.1-flash-lite-preview / labor_supply.policy_response.substitution_elasticity.primary.decile_8 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 8 | total_sd | 0.6353994981287144 | 0.6355683370898138 |
| 19 | gemini-3.1-flash-lite-preview / labor_supply.policy_response.substitution_elasticity.primary.decile_9 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 9 | between_run_sd | 0.028015868519267587 | 0.029562316478171254 |
| 19 | gemini-3.1-flash-lite-preview / labor_supply.policy_response.substitution_elasticity.primary.decile_9 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 9 | total_sd | 0.6339982091194475 | 0.6340684275638816 |
| 20 | gemini-3.1-flash-lite-preview / labor_supply.policy_response.substitution_elasticity.secondary / Secondary-earner substitution elasticity in a tax-benefit simulation | between_run_sd | 0.04027681991198191 | 0.04644770057698108 |
| 20 | gemini-3.1-flash-lite-preview / labor_supply.policy_response.substitution_elasticity.secondary / Secondary-earner substitution elasticity in a tax-benefit simulation | total_sd | 0.6644247720982247 | 0.6648273794335222 |
| 21 | gemini-3.1-flash-lite-preview / macro.tfp_persistence.ar1 / TFP persistence | between_run_sd | 0.024944382578492935 | 0.021971913890237237 |
| 21 | gemini-3.1-flash-lite-preview / macro.tfp_persistence.ar1 / TFP persistence | total_sd | 0.13336374002245804 | 0.13283986574276396 |
| 22 | gemini-3.1-flash-lite-preview / production.capital_labor_substitution / Elasticity of substitution between capital and labor | between_run_sd | 0.06548960901462834 | 0.054505351419226106 |
| 22 | gemini-3.1-flash-lite-preview / production.capital_labor_substitution / Elasticity of substitution between capital and labor | total_sd | 1.2356692406231622 | 1.235135788756308 |
| 23 | gemini-3.1-flash-lite-preview / production.capital_share / Capital share in production | between_run_sd | 0.0 | 0.005250925844289024 |
| 23 | gemini-3.1-flash-lite-preview / production.capital_share / Capital share in production | total_sd | 0.11318156504778801 | 0.11330330484539668 |
| 24 | gemini-3.1-flash-lite-preview / tax.capital_gains_realizations.elasticity / Capital gains realizations elasticity | between_run_sd | 0.056174331821175746 | 0.07183149649623688 |
| 24 | gemini-3.1-flash-lite-preview / tax.capital_gains_realizations.elasticity / Capital gains realizations elasticity | total_sd | 1.3633646721133224 | 1.3640994969209541 |
| 25 | gemini-3.1-flash-lite-preview / tax.capital_gains_realizations.elasticity.net_of_tax_rate / Capital gains realizations elasticity (net-of-tax-rate convention) | between_run_sd | 0.2481934729198171 | 0.29755877103897005 |
| 25 | gemini-3.1-flash-lite-preview / tax.capital_gains_realizations.elasticity.net_of_tax_rate / Capital gains realizations elasticity (net-of-tax-rate convention) | total_sd | 1.4534085894124122 | 1.4626475139280823 |
| 26 | gemini-3.1-flash-lite-preview / tax.elasticity_of_taxable_income.top_earners / Elasticity of taxable income | between_run_sd | 0.042687494916218996 | 0.041905647988467305 |
| 26 | gemini-3.1-flash-lite-preview / tax.elasticity_of_taxable_income.top_earners / Elasticity of taxable income | total_sd | 0.6712994240029309 | 0.6712501603558675 |
| 27 | gemini-3.1-flash-lite-preview / trade.armington_elasticity.import_domestic / Armington elasticity | between_run_sd | 0.28674417556808757 | 0.30323185115610063 |
| 27 | gemini-3.1-flash-lite-preview / trade.armington_elasticity.import_domestic / Armington elasticity | total_sd | 2.838829766725093 | 2.840542514692885 |

## `results/gemini-3.1-flash-lite-preview-ies-clarify-batch15/summary.csv` (2 cells)

| line | row | column | old | new |
|---|---|---|---|---|
| 2 | gemini-3.1-flash-lite-preview / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | between_run_sd | 0.0 | 0.019131489458191403 |
| 2 | gemini-3.1-flash-lite-preview / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | total_sd | 0.6737165009194231 | 0.6739880840934801 |

## `results/gemini-3.1-pro-preview-armington-clarify-batch15/summary.csv` (3 cells)

| line | row | column | old | new |
|---|---|---|---|---|
| 2 | gemini-3.1-pro-preview / trade.armington_elasticity.import_domestic / Armington elasticity | pooled_upper_bound | 5.5917612987785414 | 5.6245543849455935 |
| 2 | gemini-3.1-pro-preview / trade.armington_elasticity.import_domestic / Armington elasticity | between_run_sd | 0.15713484026367722 | 0.35443704276493265 |
| 2 | gemini-3.1-pro-preview / trade.armington_elasticity.import_domestic / Armington elasticity | total_sd | 2.5213896156952424 | 2.5413263964699735 |

## `results/gemini-3.1-pro-preview-elasticities-batch15/summary.csv` (52 cells)

| line | row | column | old | new |
|---|---|---|---|---|
| 2 | gemini-3.1-pro-preview / household.annual_discount_factor / Annual discount factor | between_run_sd | 0.0 | 0.0026685670311985756 |
| 2 | gemini-3.1-pro-preview / household.annual_discount_factor / Annual discount factor | total_sd | 0.12561430302716328 | 0.125642645526907 |
| 3 | gemini-3.1-pro-preview / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | between_run_sd | 0.12472191289246472 | 0.12122797623577745 |
| 3 | gemini-3.1-pro-preview / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | total_sd | 0.8257793456957965 | 0.8252588651110901 |
| 4 | gemini-3.1-pro-preview / household.relative_risk_aversion.crra / Coefficient of relative risk aversion | between_run_sd | 0.0 | 0.4060446061976715 |
| 4 | gemini-3.1-pro-preview / household.relative_risk_aversion.crra / Coefficient of relative risk aversion | total_sd | 6.585344365837422 | 6.5978506075000585 |
| 5 | gemini-3.1-pro-preview / labor_supply.extensive_margin.single_mothers / Employment participation elasticity of single mothers | between_run_sd | 0.1284090685617215 | 0.11414598352791726 |
| 5 | gemini-3.1-pro-preview / labor_supply.extensive_margin.single_mothers / Employment participation elasticity of single mothers | total_sd | 0.7005775395264173 | 0.698104079314507 |
| 6 | gemini-3.1-pro-preview / labor_supply.frisch_elasticity.prime_age / Frisch elasticity of labor supply | between_run_sd | 0.08055363982396382 | 0.06809582708702985 |
| 6 | gemini-3.1-pro-preview / labor_supply.frisch_elasticity.prime_age / Frisch elasticity of labor supply | total_sd | 1.2644570365268337 | 1.2637245546399738 |
| 7 | gemini-3.1-pro-preview / labor_supply.income_elasticity.prime_age / Income elasticity of labor supply | between_run_sd | 0.024944382578492942 | 0.023610696728389866 |
| 7 | gemini-3.1-pro-preview / labor_supply.income_elasticity.prime_age / Income elasticity of labor supply | total_sd | 0.30182717875190324 | 0.30171988434823305 |
| 8 | gemini-3.1-pro-preview / labor_supply.marshallian_wage_elasticity.prime_age / Uncompensated wage elasticity of labor supply | between_run_sd | 0.02 | 0.02364456714671587 |
| 8 | gemini-3.1-pro-preview / labor_supply.marshallian_wage_elasticity.prime_age / Uncompensated wage elasticity of labor supply | total_sd | 0.5957219569564312 | 0.5958554485406302 |
| 9 | gemini-3.1-pro-preview / labor_supply.policy_response.substitution_elasticity.all / Substitution elasticity of labor supply in a tax-benefit simulation | between_run_sd | 0.02211083193570266 | 0.016117192338893565 |
| 9 | gemini-3.1-pro-preview / labor_supply.policy_response.substitution_elasticity.all / Substitution elasticity of labor supply in a tax-benefit simulation | total_sd | 0.6253721669711743 | 0.6251889492163327 |
| 10 | gemini-3.1-pro-preview / labor_supply.policy_response.substitution_elasticity.primary.decile_1 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 1 | between_run_sd | 0.03858612300930075 | 0.031191166840772225 |
| 10 | gemini-3.1-pro-preview / labor_supply.policy_response.substitution_elasticity.primary.decile_1 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 1 | total_sd | 0.6276484994715504 | 0.6272373066781733 |
| 11 | gemini-3.1-pro-preview / labor_supply.policy_response.substitution_elasticity.primary.decile_10 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 10 | between_run_sd | 0.038586123009300755 | 0.02931817790306135 |
| 11 | gemini-3.1-pro-preview / labor_supply.policy_response.substitution_elasticity.primary.decile_10 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 10 | total_sd | 0.6313247480496864 | 0.6308261283164059 |
| 12 | gemini-3.1-pro-preview / labor_supply.policy_response.substitution_elasticity.primary.decile_2 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 2 | between_run_sd | 0.024944382578492935 | 0.021510010589387344 |
| 12 | gemini-3.1-pro-preview / labor_supply.policy_response.substitution_elasticity.primary.decile_2 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 2 | total_sd | 0.6274382550409953 | 0.6273111048134109 |
| 13 | gemini-3.1-pro-preview / labor_supply.policy_response.substitution_elasticity.primary.decile_3 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 3 | between_run_sd | 0.030912061651652344 | 0.025637158362207164 |
| 13 | gemini-3.1-pro-preview / labor_supply.policy_response.substitution_elasticity.primary.decile_3 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 3 | total_sd | 0.6258261761685731 | 0.6255878124700889 |
| 14 | gemini-3.1-pro-preview / labor_supply.policy_response.substitution_elasticity.primary.decile_4 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 4 | between_run_sd | 0.021868292622475628 | 0.016416878171226376 |
| 14 | gemini-3.1-pro-preview / labor_supply.policy_response.substitution_elasticity.primary.decile_4 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 4 | total_sd | 0.624408992790605 | 0.6242418457172224 |
| 15 | gemini-3.1-pro-preview / labor_supply.policy_response.substitution_elasticity.primary.decile_5 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 5 | between_run_sd | 0.03055050463303894 | 0.023127665011602204 |
| 15 | gemini-3.1-pro-preview / labor_supply.policy_response.substitution_elasticity.primary.decile_5 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 5 | total_sd | 0.6277977381290888 | 0.6274803228433188 |
| 16 | gemini-3.1-pro-preview / labor_supply.policy_response.substitution_elasticity.primary.decile_6 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 6 | between_run_sd | 0.03383620677453206 | 0.028149481937210383 |
| 16 | gemini-3.1-pro-preview / labor_supply.policy_response.substitution_elasticity.primary.decile_6 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 6 | total_sd | 0.6259925929185495 | 0.6257109802723085 |
| 17 | gemini-3.1-pro-preview / labor_supply.policy_response.substitution_elasticity.primary.decile_7 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 7 | between_run_sd | 0.02449489742783179 | 0.02338387383552083 |
| 17 | gemini-3.1-pro-preview / labor_supply.policy_response.substitution_elasticity.primary.decile_7 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 7 | total_sd | 0.6267977478155666 | 0.6267553128791349 |
| 18 | gemini-3.1-pro-preview / labor_supply.policy_response.substitution_elasticity.primary.decile_8 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 8 | between_run_sd | 0.035590260840104374 | 0.026950829713057494 |
| 18 | gemini-3.1-pro-preview / labor_supply.policy_response.substitution_elasticity.primary.decile_8 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 8 | total_sd | 0.6280088131901053 | 0.6275784811479757 |
| 19 | gemini-3.1-pro-preview / labor_supply.policy_response.substitution_elasticity.primary.decile_9 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 9 | between_run_sd | 0.02357022603955159 | 0.02165063509461097 |
| 19 | gemini-3.1-pro-preview / labor_supply.policy_response.substitution_elasticity.primary.decile_9 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 9 | total_sd | 0.62730726898564 | 0.627238076145467 |
| 20 | gemini-3.1-pro-preview / labor_supply.policy_response.substitution_elasticity.secondary / Secondary-earner substitution elasticity in a tax-benefit simulation | between_run_sd | 0.10718623460542351 | 0.09585304145177427 |
| 20 | gemini-3.1-pro-preview / labor_supply.policy_response.substitution_elasticity.secondary / Secondary-earner substitution elasticity in a tax-benefit simulation | total_sd | 0.6322092821122519 | 0.6303867805209398 |
| 21 | gemini-3.1-pro-preview / macro.tfp_persistence.ar1 / TFP persistence | between_run_sd | 0.0 | 0.004927065274808329 |
| 21 | gemini-3.1-pro-preview / macro.tfp_persistence.ar1 / TFP persistence | total_sd | 0.12892734414950321 | 0.12902145574154195 |
| 22 | gemini-3.1-pro-preview / production.capital_labor_substitution / Elasticity of substitution between capital and labor | between_run_sd | 0.032659863237109024 | 0.026479814114822534 |
| 22 | gemini-3.1-pro-preview / production.capital_labor_substitution / Elasticity of substitution between capital and labor | total_sd | 1.2326326979500242 | 1.2324844347676138 |
| 23 | gemini-3.1-pro-preview / production.capital_share / Capital share in production | between_run_sd | 0.007611103000806697 | 0.006216108107168028 |
| 23 | gemini-3.1-pro-preview / production.capital_share / Capital share in production | total_sd | 0.10883629909180116 | 0.10874764876130016 |
| 24 | gemini-3.1-pro-preview / tax.capital_gains_realizations.elasticity / Capital gains realizations elasticity | between_run_sd | 0.02124983660067898 | 0.015292064027534772 |
| 24 | gemini-3.1-pro-preview / tax.capital_gains_realizations.elasticity / Capital gains realizations elasticity | total_sd | 1.3016168070903202 | 1.3015331744395402 |
| 25 | gemini-3.1-pro-preview / tax.capital_gains_realizations.elasticity.net_of_tax_rate / Capital gains realizations elasticity (net-of-tax-rate convention) | between_run_sd | 0.6415779159402404 | 0.5852995434438297 |
| 25 | gemini-3.1-pro-preview / tax.capital_gains_realizations.elasticity.net_of_tax_rate / Capital gains realizations elasticity (net-of-tax-rate convention) | total_sd | 1.751088391702588 | 1.7312607801509536 |
| 26 | gemini-3.1-pro-preview / tax.elasticity_of_taxable_income.top_earners / Elasticity of taxable income | between_run_sd | 0.04472135954999581 | 0.03874991039416163 |
| 26 | gemini-3.1-pro-preview / tax.elasticity_of_taxable_income.top_earners / Elasticity of taxable income | total_sd | 0.6687478971929557 | 0.6683751233817395 |
| 27 | gemini-3.1-pro-preview / trade.armington_elasticity.import_domestic / Armington elasticity | between_run_sd | 0.2217105219775452 | 0.21324959293956192 |
| 27 | gemini-3.1-pro-preview / trade.armington_elasticity.import_domestic / Armington elasticity | total_sd | 2.653348644218806 | 2.652655058825235 |

## `results/gemini-3.1-pro-preview-ies-clarify-batch15/summary.csv` (3 cells)

| line | row | column | old | new |
|---|---|---|---|---|
| 2 | gemini-3.1-pro-preview / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | pooled_upper_bound | 1.7674248046740788 | 1.7536330159041484 |
| 2 | gemini-3.1-pro-preview / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | between_run_sd | 0.21650635094610965 | 0.18787774449093217 |
| 2 | gemini-3.1-pro-preview / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | total_sd | 0.6945449649470748 | 0.6861601527401117 |

## `results/gemini-3.5-flash-armington-clarify-batch15/summary.csv` (17 cells)

| line | row | column | old | new |
|---|---|---|---|---|
| 2 | gemini-3.5-flash / trade.armington_elasticity.import_domestic / Armington elasticity | pooled_point_estimate | 1.3866666666666667 | 1.4533333333333334 |
| 2 | gemini-3.5-flash / trade.armington_elasticity.import_domestic / Armington elasticity | between_run_sd | 0.17838784213679537 | 0.1165933102712158 |
| 2 | gemini-3.5-flash / trade.armington_elasticity.import_domestic / Armington elasticity | total_sd | 2.579759463378105 | 2.5762241103340884 |
| 2 | gemini-3.5-flash / trade.armington_elasticity.import_domestic / Armington elasticity | reml_latent_location | 1.3718405813371213 | 1.4429951050651888 |
| 2 | gemini-3.5-flash / trade.armington_elasticity.import_domestic / Armington elasticity | reml_latent_lower | 1.085708400919996 | 1.142932418269968 |
| 2 | gemini-3.5-flash / trade.armington_elasticity.import_domestic / Armington elasticity | reml_latent_upper | 1.7264979537629686 | 1.8142562379298612 |
| 2 | gemini-3.5-flash / trade.armington_elasticity.import_domestic / Armington elasticity | reml_predictive_lower | 0.5416181291344607 | 0.5710307646514293 |
| 2 | gemini-3.5-flash / trade.armington_elasticity.import_domestic / Armington elasticity | reml_predictive_upper | 3.261374820117535 | 3.4125813365537545 |
| 2 | gemini-3.5-flash / trade.armington_elasticity.import_domestic / Armington elasticity | reml_typical_within_sd | 0.7558006941990711 | 0.7919658132985707 |
| 2 | gemini-3.5-flash / trade.armington_elasticity.import_domestic / Armington elasticity | bayes_latent_location | 1.3718825394804477 | 1.443101907160604 |
| 2 | gemini-3.5-flash / trade.armington_elasticity.import_domestic / Armington elasticity | bayes_latent_lower | 1.205087976977882 | 1.2714404447723178 |
| 2 | gemini-3.5-flash / trade.armington_elasticity.import_domestic / Armington elasticity | bayes_latent_upper | 1.5598639009491246 | 1.6359541557230495 |
| 2 | gemini-3.5-flash / trade.armington_elasticity.import_domestic / Armington elasticity | bayes_predictive_lower | 0.8084987936818554 | 0.8606843506056588 |
| 2 | gemini-3.5-flash / trade.armington_elasticity.import_domestic / Armington elasticity | bayes_predictive_upper | 2.2812069411982914 | 2.370869522119871 |
| 2 | gemini-3.5-flash / trade.armington_elasticity.import_domestic / Armington elasticity | bayes_tau_mean | 0.0302941850741212 | 0.02918769525010138 |
| 2 | gemini-3.5-flash / trade.armington_elasticity.import_domestic / Armington elasticity | bayes_interval_scale_mean | 0.30551418045935164 | 0.294085260408781 |
| 2 | gemini-3.5-flash / trade.armington_elasticity.import_domestic / Armington elasticity | bayes_typical_within_sd | 0.41776810243365586 | 0.4295094337934245 |

## `results/gemini-3.5-flash-elasticities-batch15/summary.csv` (290 cells)

| line | row | column | old | new |
|---|---|---|---|---|
| 2 | gemini-3.5-flash / household.annual_discount_factor / Annual discount factor | pooled_point_estimate | 0.9599999999999999 | 0.9606666666666667 |
| 2 | gemini-3.5-flash / household.annual_discount_factor / Annual discount factor | between_run_sd | 0.003651483716701111 | 0.0029145706754550227 |
| 2 | gemini-3.5-flash / household.annual_discount_factor / Annual discount factor | total_sd | 0.1271714380384911 | 0.12715241264587418 |
| 2 | gemini-3.5-flash / household.annual_discount_factor / Annual discount factor | reml_latent_location | 0.9603060074082159 | 0.9607301635536005 |
| 2 | gemini-3.5-flash / household.annual_discount_factor / Annual discount factor | reml_latent_lower | 0.9460047725131717 | 0.9465732446108884 |
| 2 | gemini-3.5-flash / household.annual_discount_factor / Annual discount factor | reml_latent_upper | 0.9709357759249568 | 0.9712497466853451 |
| 2 | gemini-3.5-flash / household.annual_discount_factor / Annual discount factor | reml_predictive_lower | 0.8681626654587261 | 0.8694375661837626 |
| 2 | gemini-3.5-flash / household.annual_discount_factor / Annual discount factor | reml_predictive_upper | 0.9888741299236897 | 0.9889965149536348 |
| 2 | gemini-3.5-flash / household.annual_discount_factor / Annual discount factor | reml_typical_within_sd | 0.030155407876312896 | 0.029846354689036386 |
| 2 | gemini-3.5-flash / household.annual_discount_factor / Annual discount factor | bayes_latent_location | 0.960304874811031 | 0.9607312063613487 |
| 2 | gemini-3.5-flash / household.annual_discount_factor / Annual discount factor | bayes_latent_lower | 0.9530341846407794 | 0.9535494295405287 |
| 2 | gemini-3.5-flash / household.annual_discount_factor / Annual discount factor | bayes_latent_upper | 0.9664892310620327 | 0.9668414915753261 |
| 2 | gemini-3.5-flash / household.annual_discount_factor / Annual discount factor | bayes_predictive_lower | 0.9210172966520562 | 0.9219269839355666 |
| 2 | gemini-3.5-flash / household.annual_discount_factor / Annual discount factor | bayes_predictive_upper | 0.9804643402908924 | 0.9806536514362517 |
| 2 | gemini-3.5-flash / household.annual_discount_factor / Annual discount factor | bayes_tau_mean | 0.0010744593530310805 | 0.0010557123980280882 |
| 2 | gemini-3.5-flash / household.annual_discount_factor / Annual discount factor | bayes_interval_scale_mean | 0.29321098908647786 | 0.29216497808393443 |
| 2 | gemini-3.5-flash / household.annual_discount_factor / Annual discount factor | bayes_typical_within_sd | 0.016329286464725073 | 0.016132226545479637 |
| 3 | gemini-3.5-flash / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | pooled_point_estimate | 0.9333333333333333 | 0.9866666666666667 |
| 3 | gemini-3.5-flash / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | between_run_sd | 0.21186998109427604 | 0.06916114435786101 |
| 3 | gemini-3.5-flash / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | total_sd | 0.8346072970432129 | 0.810224484496598 |
| 3 | gemini-3.5-flash / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | reml_latent_location | 0.9101210532212933 | 0.9926661861855784 |
| 3 | gemini-3.5-flash / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | reml_latent_lower | 0.6268248662170149 | 0.6879981709466875 |
| 3 | gemini-3.5-flash / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | reml_latent_upper | 1.2838654180652018 | 1.388797463224165 |
| 3 | gemini-3.5-flash / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | reml_predictive_lower | 0.018681476068356826 | 0.02078675044286401 |
| 3 | gemini-3.5-flash / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | reml_predictive_upper | 4.6479902675423554 | 4.6814958446304304 |
| 3 | gemini-3.5-flash / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | reml_typical_within_sd | 1.8480580249925564 | 1.9749892582798991 |
| 3 | gemini-3.5-flash / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | bayes_latent_location | 0.9093908434517373 | 0.9924698335795772 |
| 3 | gemini-3.5-flash / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | bayes_latent_lower | 0.7294327075254325 | 0.8151840702235325 |
| 3 | gemini-3.5-flash / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | bayes_latent_upper | 1.1216629313733413 | 1.1972015210975322 |
| 3 | gemini-3.5-flash / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | bayes_predictive_lower | 0.09685966189657338 | 0.13081650360769834 |
| 3 | gemini-3.5-flash / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | bayes_predictive_upper | 3.5719671022198267 | 3.4768802538976944 |
| 3 | gemini-3.5-flash / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | bayes_tau_mean | 0.04785521416683391 | 0.036477938275521565 |
| 3 | gemini-3.5-flash / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | bayes_interval_scale_mean | 0.34864399880421343 | 0.2927057172117013 |
| 3 | gemini-3.5-flash / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | bayes_typical_within_sd | 1.0905250566309377 | 1.0683552938721728 |
| 4 | gemini-3.5-flash / household.relative_risk_aversion.crra / Coefficient of relative risk aversion | between_run_sd | 0.0 | 0.10764525070805477 |
| 4 | gemini-3.5-flash / household.relative_risk_aversion.crra / Coefficient of relative risk aversion | total_sd | 6.901588484625197 | 6.902427914227799 |
| 5 | gemini-3.5-flash / labor_supply.extensive_margin.single_mothers / Employment participation elasticity of single mothers | between_run_sd | 0.04096611065529925 | 0.043277290683323616 |
| 5 | gemini-3.5-flash / labor_supply.extensive_margin.single_mothers / Employment participation elasticity of single mothers | total_sd | 0.6837678069994879 | 0.6839101662905411 |
| 6 | gemini-3.5-flash / labor_supply.frisch_elasticity.prime_age / Frisch elasticity of labor supply | pooled_point_estimate | 0.39333333333333337 | 0.4 |
| 6 | gemini-3.5-flash / labor_supply.frisch_elasticity.prime_age / Frisch elasticity of labor supply | between_run_sd | 0.05734883511361752 | 0.05232683080621471 |
| 6 | gemini-3.5-flash / labor_supply.frisch_elasticity.prime_age / Frisch elasticity of labor supply | total_sd | 1.2847525431857383 | 1.2845381681972536 |
| 6 | gemini-3.5-flash / labor_supply.frisch_elasticity.prime_age / Frisch elasticity of labor supply | reml_latent_location | 0.39265204399506787 | 0.40060020985117795 |
| 6 | gemini-3.5-flash / labor_supply.frisch_elasticity.prime_age / Frisch elasticity of labor supply | reml_latent_lower | 0.2816341987506109 | 0.2874023384201584 |
| 6 | gemini-3.5-flash / labor_supply.frisch_elasticity.prime_age / Frisch elasticity of labor supply | reml_latent_upper | 0.5449781303337523 | 0.555831329897022 |
| 6 | gemini-3.5-flash / labor_supply.frisch_elasticity.prime_age / Frisch elasticity of labor supply | reml_predictive_lower | 0.10124618415780479 | 0.10335909638186525 |
| 6 | gemini-3.5-flash / labor_supply.frisch_elasticity.prime_age / Frisch elasticity of labor supply | reml_predictive_upper | 1.403832835896093 | 1.4292046488475334 |
| 6 | gemini-3.5-flash / labor_supply.frisch_elasticity.prime_age / Frisch elasticity of labor supply | reml_typical_within_sd | 0.31769627235403014 | 0.32385901314849713 |
| 6 | gemini-3.5-flash / labor_supply.frisch_elasticity.prime_age / Frisch elasticity of labor supply | bayes_latent_location | 0.39259620784745797 | 0.4005456731019558 |
| 6 | gemini-3.5-flash / labor_supply.frisch_elasticity.prime_age / Frisch elasticity of labor supply | bayes_latent_lower | 0.32726227540716424 | 0.33415398184705897 |
| 6 | gemini-3.5-flash / labor_supply.frisch_elasticity.prime_age / Frisch elasticity of labor supply | bayes_latent_upper | 0.4703156417571309 | 0.47945153262451967 |
| 6 | gemini-3.5-flash / labor_supply.frisch_elasticity.prime_age / Frisch elasticity of labor supply | bayes_predictive_lower | 0.18331158580810997 | 0.18761883332314705 |
| 6 | gemini-3.5-flash / labor_supply.frisch_elasticity.prime_age / Frisch elasticity of labor supply | bayes_predictive_upper | 0.8208022720320609 | 0.8345326325362192 |
| 6 | gemini-3.5-flash / labor_supply.frisch_elasticity.prime_age / Frisch elasticity of labor supply | bayes_tau_mean | 0.01175117695046748 | 0.011764626555198386 |
| 6 | gemini-3.5-flash / labor_supply.frisch_elasticity.prime_age / Frisch elasticity of labor supply | bayes_interval_scale_mean | 0.2977892724174384 | 0.29574290122264774 |
| 6 | gemini-3.5-flash / labor_supply.frisch_elasticity.prime_age / Frisch elasticity of labor supply | bayes_typical_within_sd | 0.17334343775955913 | 0.17609883877427016 |
| 7 | gemini-3.5-flash / labor_supply.income_elasticity.prime_age / Income elasticity of labor supply | n_quantile_repaired_runs | 5 | 0 |
| 7 | gemini-3.5-flash / labor_supply.income_elasticity.prime_age / Income elasticity of labor supply | pooled_point_estimate | 0.011 | -0.030333333333333334 |
| 7 | gemini-3.5-flash / labor_supply.income_elasticity.prime_age / Income elasticity of labor supply | pooled_lower_bound | -0.14522847504826908 | -0.14940929524537827 |
| 7 | gemini-3.5-flash / labor_supply.income_elasticity.prime_age / Income elasticity of labor supply | pooled_upper_bound | 0.14999999999999997 | 0.009900990099009868 |
| 7 | gemini-3.5-flash / labor_supply.income_elasticity.prime_age / Income elasticity of labor supply | within_run_sd | 0.2941257603286201 | 0.29369602939187917 |
| 7 | gemini-3.5-flash / labor_supply.income_elasticity.prime_age / Income elasticity of labor supply | between_run_sd | 0.06851277253184256 | 0.009395889467681535 |
| 7 | gemini-3.5-flash / labor_supply.income_elasticity.prime_age / Income elasticity of labor supply | total_sd | 0.3019999385577568 | 0.29384628706084487 |
| 7 | gemini-3.5-flash / labor_supply.income_elasticity.prime_age / Income elasticity of labor supply | reml_latent_location | 0.01506225445095577 | -0.02642923774809347 |
| 7 | gemini-3.5-flash / labor_supply.income_elasticity.prime_age / Income elasticity of labor supply | reml_latent_lower | -0.01612636869120143 | -0.0420615845058987 |
| 7 | gemini-3.5-flash / labor_supply.income_elasticity.prime_age / Income elasticity of labor supply | reml_latent_upper | 0.04575404407589412 | -0.010910318607958214 |
| 7 | gemini-3.5-flash / labor_supply.income_elasticity.prime_age / Income elasticity of labor supply | reml_predictive_lower | -0.10880809271231451 | -0.09333585777853814 |
| 7 | gemini-3.5-flash / labor_supply.income_elasticity.prime_age / Income elasticity of labor supply | reml_predictive_upper | 0.1314497659371714 | 0.03844786072048212 |
| 7 | gemini-3.5-flash / labor_supply.income_elasticity.prime_age / Income elasticity of labor supply | reml_tau | 0.06424746557123487 | 0.0 |
| 7 | gemini-3.5-flash / labor_supply.income_elasticity.prime_age / Income elasticity of labor supply | reml_typical_within_sd | 0.03500217360355165 | 0.04008171602955958 |
| 7 | gemini-3.5-flash / labor_supply.income_elasticity.prime_age / Income elasticity of labor supply | bayes_latent_location | 0.015051861120380483 | -0.026523371403833762 |
| 7 | gemini-3.5-flash / labor_supply.income_elasticity.prime_age / Income elasticity of labor supply | bayes_latent_lower | -0.018220573980045618 | -0.03533014938088708 |
| 7 | gemini-3.5-flash / labor_supply.income_elasticity.prime_age / Income elasticity of labor supply | bayes_latent_upper | 0.04677948762175843 | -0.01779314586143288 |
| 7 | gemini-3.5-flash / labor_supply.income_elasticity.prime_age / Income elasticity of labor supply | bayes_predictive_lower | -0.11966277343643039 | -0.0648066507136611 |
| 7 | gemini-3.5-flash / labor_supply.income_elasticity.prime_age / Income elasticity of labor supply | bayes_predictive_upper | 0.1401045320758998 | 0.011052646467848426 |
| 7 | gemini-3.5-flash / labor_supply.income_elasticity.prime_age / Income elasticity of labor supply | bayes_tau_mean | 0.06580050996258865 | 0.00212822541180627 |
| 7 | gemini-3.5-flash / labor_supply.income_elasticity.prime_age / Income elasticity of labor supply | bayes_interval_scale_mean | 0.9567715952730389 | 0.30788151338938446 |
| 7 | gemini-3.5-flash / labor_supply.income_elasticity.prime_age / Income elasticity of labor supply | bayes_typical_within_sd | 0.034237456538654266 | 0.022241149293833046 |
| 8 | gemini-3.5-flash / labor_supply.marshallian_wage_elasticity.prime_age / Uncompensated wage elasticity of labor supply | n_quantile_repaired_runs | 4 | 0 |
| 8 | gemini-3.5-flash / labor_supply.marshallian_wage_elasticity.prime_age / Uncompensated wage elasticity of labor supply | pooled_point_estimate | 0.07333333333333333 | 0.05333333333333334 |
| 8 | gemini-3.5-flash / labor_supply.marshallian_wage_elasticity.prime_age / Uncompensated wage elasticity of labor supply | pooled_lower_bound | -0.14765587034553657 | -0.1495419309372798 |
| 8 | gemini-3.5-flash / labor_supply.marshallian_wage_elasticity.prime_age / Uncompensated wage elasticity of labor supply | within_run_sd | 0.5960619782744446 | 0.6020740806670813 |
| 8 | gemini-3.5-flash / labor_supply.marshallian_wage_elasticity.prime_age / Uncompensated wage elasticity of labor supply | between_run_sd | 0.03590109871423002 | 0.011700854669638452 |
| 8 | gemini-3.5-flash / labor_supply.marshallian_wage_elasticity.prime_age / Uncompensated wage elasticity of labor supply | total_sd | 0.597142169699422 | 0.6021877685665088 |
| 8 | gemini-3.5-flash / labor_supply.marshallian_wage_elasticity.prime_age / Uncompensated wage elasticity of labor supply | reml_latent_location | 0.09239520386065214 | 0.053018477728747904 |
| 8 | gemini-3.5-flash / labor_supply.marshallian_wage_elasticity.prime_age / Uncompensated wage elasticity of labor supply | reml_latent_lower | 0.04817332431938759 | -0.0012279967481800824 |
| 8 | gemini-3.5-flash / labor_supply.marshallian_wage_elasticity.prime_age / Uncompensated wage elasticity of labor supply | reml_latent_upper | 0.13705554510089346 | 0.10796157585219568 |
| 8 | gemini-3.5-flash / labor_supply.marshallian_wage_elasticity.prime_age / Uncompensated wage elasticity of labor supply | reml_predictive_lower | -0.09987161267520417 | -0.15570229432395877 |
| 8 | gemini-3.5-flash / labor_supply.marshallian_wage_elasticity.prime_age / Uncompensated wage elasticity of labor supply | reml_predictive_upper | 0.29323489164016525 | 0.27244373632791774 |
| 8 | gemini-3.5-flash / labor_supply.marshallian_wage_elasticity.prime_age / Uncompensated wage elasticity of labor supply | reml_typical_within_sd | 0.11964658302373896 | 0.1303388135680213 |
| 8 | gemini-3.5-flash / labor_supply.marshallian_wage_elasticity.prime_age / Uncompensated wage elasticity of labor supply | bayes_latent_location | 0.09161142224072982 | 0.053024281601650625 |
| 8 | gemini-3.5-flash / labor_supply.marshallian_wage_elasticity.prime_age / Uncompensated wage elasticity of labor supply | bayes_latent_lower | 0.06489818668515568 | 0.023384932707346984 |
| 8 | gemini-3.5-flash / labor_supply.marshallian_wage_elasticity.prime_age / Uncompensated wage elasticity of labor supply | bayes_latent_upper | 0.11799364018925163 | 0.08287227319065238 |
| 8 | gemini-3.5-flash / labor_supply.marshallian_wage_elasticity.prime_age / Uncompensated wage elasticity of labor supply | bayes_predictive_lower | -0.025568518619977 | -0.06569451775918522 |
| 8 | gemini-3.5-flash / labor_supply.marshallian_wage_elasticity.prime_age / Uncompensated wage elasticity of labor supply | bayes_predictive_upper | 0.21153964619318932 | 0.17513316676089508 |
| 8 | gemini-3.5-flash / labor_supply.marshallian_wage_elasticity.prime_age / Uncompensated wage elasticity of labor supply | bayes_tau_mean | 0.007588246875963631 | 0.005732853074690474 |
| 8 | gemini-3.5-flash / labor_supply.marshallian_wage_elasticity.prime_age / Uncompensated wage elasticity of labor supply | bayes_interval_scale_mean | 0.3366526831867316 | 0.2922180133720675 |
| 8 | gemini-3.5-flash / labor_supply.marshallian_wage_elasticity.prime_age / Uncompensated wage elasticity of labor supply | bayes_typical_within_sd | 0.06940899092568635 | 0.07045759980746627 |
| 9 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.all / Substitution elasticity of labor supply in a tax-benefit simulation | pooled_point_estimate | 0.24333333333333332 | 0.24666666666666667 |
| 9 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.all / Substitution elasticity of labor supply in a tax-benefit simulation | between_run_sd | 0.016996731711975945 | 0.0149378713342966 |
| 9 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.all / Substitution elasticity of labor supply in a tax-benefit simulation | total_sd | 0.6307648300542235 | 0.6307127095155484 |
| 9 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.all / Substitution elasticity of labor supply in a tax-benefit simulation | reml_latent_location | 0.24190731589593814 | 0.2471302521009586 |
| 9 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.all / Substitution elasticity of labor supply in a tax-benefit simulation | reml_latent_lower | 0.18889932318618893 | 0.19302421101046552 |
| 9 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.all / Substitution elasticity of labor supply in a tax-benefit simulation | reml_latent_upper | 0.308835299806933 | 0.31540746637697203 |
| 9 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.all / Substitution elasticity of labor supply in a tax-benefit simulation | reml_predictive_lower | 0.08529939942493045 | 0.08720303843098444 |
| 9 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.all / Substitution elasticity of labor supply in a tax-benefit simulation | reml_predictive_upper | 0.6481262235047323 | 0.6609014589398778 |
| 9 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.all / Substitution elasticity of labor supply in a tax-benefit simulation | reml_typical_within_sd | 0.1504182931327913 | 0.15349724349520502 |
| 9 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.all / Substitution elasticity of labor supply in a tax-benefit simulation | bayes_latent_location | 0.24191488322747687 | 0.24711610871227974 |
| 9 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.all / Substitution elasticity of labor supply in a tax-benefit simulation | bayes_latent_lower | 0.21142667221823455 | 0.21612302115005882 |
| 9 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.all / Substitution elasticity of labor supply in a tax-benefit simulation | bayes_latent_upper | 0.2765489487066417 | 0.2822859109512673 |
| 9 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.all / Substitution elasticity of labor supply in a tax-benefit simulation | bayes_predictive_lower | 0.1353919593956886 | 0.13870681701885093 |
| 9 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.all / Substitution elasticity of labor supply in a tax-benefit simulation | bayes_predictive_upper | 0.4249308969940576 | 0.43270566269892735 |
| 9 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.all / Substitution elasticity of labor supply in a tax-benefit simulation | bayes_tau_mean | 0.005329328163558939 | 0.0052948472790174525 |
| 9 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.all / Substitution elasticity of labor supply in a tax-benefit simulation | bayes_interval_scale_mean | 0.2941072859228604 | 0.29176984406519146 |
| 9 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.all / Substitution elasticity of labor supply in a tax-benefit simulation | bayes_typical_within_sd | 0.08157675816432203 | 0.0829081489952757 |
| 10 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_1 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 1 | between_run_sd | 0.022939534045447005 | 0.02314077690043175 |
| 10 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_1 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 1 | total_sd | 0.6355626673795958 | 0.6355699627106366 |
| 11 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_10 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 10 | pooled_point_estimate | 0.14 | 0.152 |
| 11 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_10 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 10 | between_run_sd | 0.02921186973360886 | 0.02061824973711936 |
| 11 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_10 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 10 | total_sd | 0.6354997989334414 | 0.6351627927809794 |
| 11 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_10 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 10 | reml_latent_location | 0.13886812051326458 | 0.15212427290394712 |
| 11 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_10 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 10 | reml_latent_lower | 0.1044737725758444 | 0.11452403981874636 |
| 11 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_10 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 10 | reml_latent_upper | 0.18415965530422893 | 0.2015600064875025 |
| 11 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_10 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 10 | reml_predictive_lower | 0.044504841712266055 | 0.04884371880053668 |
| 11 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_10 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 10 | reml_predictive_upper | 0.41649326049125224 | 0.4537772299081652 |
| 11 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_10 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 10 | reml_typical_within_sd | 0.09498024850260825 | 0.10376319466202384 |
| 11 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_10 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 10 | bayes_latent_location | 0.13884436816857115 | 0.15211067929496325 |
| 11 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_10 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 10 | bayes_latent_lower | 0.11826332042212459 | 0.13016720766531242 |
| 11 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_10 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 10 | bayes_latent_upper | 0.16287651485165183 | 0.17761273147256446 |
| 11 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_10 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 10 | bayes_predictive_lower | 0.07178069887900194 | 0.08012724588542453 |
| 11 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_10 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 10 | bayes_predictive_upper | 0.2651760041541817 | 0.28500650372800646 |
| 11 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_10 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 10 | bayes_tau_mean | 0.003972042268011725 | 0.0038579018217662067 |
| 11 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_10 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 10 | bayes_interval_scale_mean | 0.3144731780983893 | 0.29866556599120714 |
| 11 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_10 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 10 | bayes_typical_within_sd | 0.05325408648723164 | 0.05670199242900535 |
| 12 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_2 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 2 | between_run_sd | 0.01783878421367954 | 0.016803967785417036 |
| 12 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_2 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 2 | total_sd | 0.6363046789427566 | 0.6362765087252205 |
| 13 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_3 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 3 | pooled_point_estimate | 0.14400000000000002 | 0.14866666666666667 |
| 13 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_3 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 3 | between_run_sd | 0.022449944320643647 | 0.019071065926045024 |
| 13 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_3 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 3 | total_sd | 0.635552654300876 | 0.6354422727081072 |
| 13 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_3 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 3 | reml_latent_location | 0.14269323951477175 | 0.1478847059866973 |
| 13 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_3 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 3 | reml_latent_lower | 0.1029344825610108 | 0.10671122419602444 |
| 13 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_3 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 3 | reml_latent_upper | 0.19719055800938637 | 0.20428135996041952 |
| 13 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_3 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 3 | reml_predictive_lower | 0.03763269814524122 | 0.039032566761115745 |
| 13 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_3 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 3 | reml_predictive_upper | 0.5108605614841598 | 0.5279906899287412 |
| 13 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_3 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 3 | reml_typical_within_sd | 0.11412787611938775 | 0.11815366014695337 |
| 13 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_3 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 3 | bayes_latent_location | 0.14268509854106098 | 0.14788386994273717 |
| 13 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_3 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 3 | bayes_latent_lower | 0.11913873384857696 | 0.1237518810519638 |
| 13 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_3 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 3 | bayes_latent_upper | 0.17071866601245586 | 0.17655089329212065 |
| 13 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_3 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 3 | bayes_predictive_lower | 0.06703353476992024 | 0.07010311305656132 |
| 13 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_3 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 3 | bayes_predictive_upper | 0.2985412395289553 | 0.30659618692460144 |
| 13 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_3 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 3 | bayes_tau_mean | 0.004404247297997287 | 0.004319147419500898 |
| 13 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_3 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 3 | bayes_interval_scale_mean | 0.30184591816021134 | 0.29542080380682795 |
| 13 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_3 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 3 | bayes_typical_within_sd | 0.06269896020938477 | 0.06421926593790793 |
| 14 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_4 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 4 | pooled_point_estimate | 0.13866666666666666 | 0.142 |
| 14 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_4 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 4 | between_run_sd | 0.01995550606279435 | 0.02057348617355196 |
| 14 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_4 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 4 | total_sd | 0.633315633524601 | 0.633335407014149 |
| 14 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_4 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 4 | reml_latent_location | 0.14016411896389744 | 0.14245288114591106 |
| 14 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_4 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 4 | reml_latent_lower | 0.10420760968180406 | 0.10592202924427577 |
| 14 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_4 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 4 | reml_latent_upper | 0.1880507599732369 | 0.19109072419327472 |
| 14 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_4 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 4 | reml_predictive_lower | 0.04174980315383903 | 0.04244557799033877 |
| 14 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_4 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 4 | reml_predictive_upper | 0.4495319570780235 | 0.4563980179072704 |
| 14 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_4 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 4 | reml_typical_within_sd | 0.10197138971053632 | 0.10358768865724917 |
| 14 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_4 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 4 | bayes_latent_location | 0.14012364454012655 | 0.1424295604147628 |
| 14 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_4 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 4 | bayes_latent_lower | 0.11908298560623387 | 0.12112948451202574 |
| 14 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_4 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 4 | bayes_latent_upper | 0.16473946190780892 | 0.1673371895475809 |
| 14 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_4 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 4 | bayes_predictive_lower | 0.07083320840061855 | 0.07220421782467726 |
| 14 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_4 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 4 | bayes_predictive_upper | 0.2734095865882614 | 0.27710037896207895 |
| 14 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_4 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 4 | bayes_tau_mean | 0.0037570904083253486 | 0.0037636131784781856 |
| 14 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_4 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 4 | bayes_interval_scale_mean | 0.2982899028707565 | 0.2960671350263603 |
| 14 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_4 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 4 | bayes_typical_within_sd | 0.05567699717559544 | 0.056355229783321054 |
| 15 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_5 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 5 | pooled_point_estimate | 0.13933333333333334 | 0.14400000000000002 |
| 15 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_5 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 5 | between_run_sd | 0.028158282775923835 | 0.02433930292072201 |
| 15 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_5 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 5 | total_sd | 0.6337201121595839 | 0.6335619096294641 |
| 15 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_5 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 5 | reml_latent_location | 0.1368380118379161 | 0.143582216479177 |
| 15 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_5 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 5 | reml_latent_lower | 0.10197484320998237 | 0.10703859931032506 |
| 15 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_5 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 5 | reml_latent_upper | 0.1831744606659439 | 0.19211218982285488 |
| 15 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_5 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 5 | reml_predictive_lower | 0.04051983505132864 | 0.04255844066321557 |
| 15 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_5 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 5 | reml_predictive_upper | 0.4417185755940596 | 0.4620614453015277 |
| 15 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_5 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 5 | reml_typical_within_sd | 0.1000607844165967 | 0.10484678208364166 |
| 15 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_5 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 5 | bayes_latent_location | 0.1368360731873896 | 0.1435635886930965 |
| 15 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_5 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 5 | bayes_latent_lower | 0.11593429157951093 | 0.12200787559814087 |
| 15 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_5 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 5 | bayes_latent_upper | 0.1613807102690282 | 0.1687874017151269 |
| 15 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_5 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 5 | bayes_predictive_lower | 0.0677221807594998 | 0.07196734515006002 |
| 15 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_5 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 5 | bayes_predictive_upper | 0.2725845043722527 | 0.2822938259793816 |
| 15 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_5 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 5 | bayes_tau_mean | 0.004169760353042458 | 0.004010258792167652 |
| 15 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_5 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 5 | bayes_interval_scale_mean | 0.3138054489854466 | 0.3035804738677562 |
| 15 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_5 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 5 | bayes_typical_within_sd | 0.05605161930055552 | 0.0577613508752366 |
| 16 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_6 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 6 | pooled_point_estimate | 0.156 | 0.14400000000000002 |
| 16 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_6 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 6 | between_run_sd | 0.06770524351924304 | 0.015447887306108318 |
| 16 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_6 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 6 | total_sd | 0.6380775782248843 | 0.634663401383407 |
| 16 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_6 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 6 | reml_latent_location | 0.15386883693104486 | 0.1437978117444172 |
| 16 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_6 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 6 | reml_latent_lower | 0.11080566321459084 | 0.10349301660116758 |
| 16 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_6 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 6 | reml_latent_upper | 0.2129390503514968 | 0.19916065199034444 |
| 16 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_6 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 6 | reml_predictive_lower | 0.039924566990878915 | 0.03725409206053966 |
| 16 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_6 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 6 | reml_predictive_upper | 0.5565217461710259 | 0.522940153490234 |
| 16 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_6 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 6 | reml_typical_within_sd | 0.12442656920465965 | 0.11652425331115725 |
| 16 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_6 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 6 | bayes_latent_location | 0.15363626072005937 | 0.14378516472094643 |
| 16 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_6 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 6 | bayes_latent_lower | 0.12564800034200888 | 0.12024221400658787 |
| 16 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_6 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 6 | bayes_latent_upper | 0.18747754039643438 | 0.17177061646704256 |
| 16 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_6 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 6 | bayes_predictive_lower | 0.06599248517181854 | 0.06769825733823559 |
| 16 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_6 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 6 | bayes_predictive_upper | 0.34920458420380573 | 0.3001750291052919 |
| 16 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_6 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 6 | bayes_tau_mean | 0.007611848725972094 | 0.00412815113404474 |
| 16 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_6 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 6 | bayes_interval_scale_mean | 0.3633872485683715 | 0.2928964934328386 |
| 16 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_6 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 6 | bayes_typical_within_sd | 0.07489655949711446 | 0.06305744183286396 |
| 17 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_7 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 7 | pooled_point_estimate | 0.14066666666666666 | 0.14400000000000002 |
| 17 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_7 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 7 | between_run_sd | 0.01611072796479276 | 0.017544198154629046 |
| 17 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_7 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 7 | total_sd | 0.6323745945069091 | 0.6324127379418533 |
| 17 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_7 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 7 | reml_latent_location | 0.1393549818017516 | 0.14288640323894045 |
| 17 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_7 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 7 | reml_latent_lower | 0.10453217012990593 | 0.1072006022906332 |
| 17 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_7 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 7 | reml_latent_upper | 0.18533913184118084 | 0.1899902981234649 |
| 17 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_7 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 7 | reml_predictive_lower | 0.0426862500964387 | 0.04379004018502751 |
| 17 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_7 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 7 | reml_predictive_upper | 0.43570202551362136 | 0.4460540725796535 |
| 17 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_7 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 7 | reml_typical_within_sd | 0.09906658414618681 | 0.10150325040848783 |
| 17 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_7 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 7 | bayes_latent_location | 0.13935555975713076 | 0.14288762750529266 |
| 17 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_7 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 7 | bayes_latent_lower | 0.11904367352190323 | 0.12207962838975925 |
| 17 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_7 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 7 | bayes_latent_upper | 0.16301771035771687 | 0.1671212442025632 |
| 17 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_7 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 7 | bayes_predictive_lower | 0.07166142597688006 | 0.07351882529038398 |
| 17 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_7 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 7 | bayes_predictive_upper | 0.2675254025532853 | 0.27406893397123233 |
| 17 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_7 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 7 | bayes_tau_mean | 0.003630530090894382 | 0.0037341200751615624 |
| 17 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_7 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 7 | bayes_interval_scale_mean | 0.2973370741768691 | 0.29710821275863547 |
| 17 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_7 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 7 | bayes_typical_within_sd | 0.05401986194449985 | 0.05532747999144893 |
| 18 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_8 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 8 | between_run_sd | 0.016519348924485155 | 0.02090613944913472 |
| 18 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_8 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 8 | total_sd | 0.6325679882212047 | 0.6326977457680721 |
| 19 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_9 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 9 | between_run_sd | 0.014966629547095765 | 0.019549722930687963 |
| 19 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_9 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 9 | total_sd | 0.6334921971807458 | 0.6336170417180678 |
| 20 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.secondary / Secondary-earner substitution elasticity in a tax-benefit simulation | between_run_sd | 0.03741657386773942 | 0.03688975316925946 |
| 20 | gemini-3.5-flash / labor_supply.policy_response.substitution_elasticity.secondary / Secondary-earner substitution elasticity in a tax-benefit simulation | total_sd | 0.6325734981451211 | 0.6325425554414853 |
| 21 | gemini-3.5-flash / macro.tfp_persistence.ar1 / TFP persistence | pooled_point_estimate | 0.9546666666666667 | 0.956 |
| 21 | gemini-3.5-flash / macro.tfp_persistence.ar1 / TFP persistence | between_run_sd | 0.004988876515698593 | 0.0062260875890615954 |
| 21 | gemini-3.5-flash / macro.tfp_persistence.ar1 / TFP persistence | total_sd | 0.1277899304305486 | 0.12784420830535195 |
| 21 | gemini-3.5-flash / macro.tfp_persistence.ar1 / TFP persistence | reml_latent_location | 0.9539919622598294 | 0.9553924451868112 |
| 21 | gemini-3.5-flash / macro.tfp_persistence.ar1 / TFP persistence | reml_latent_lower | 0.935750467440782 | 0.9376699416088118 |
| 21 | gemini-3.5-flash / macro.tfp_persistence.ar1 / TFP persistence | reml_latent_upper | 0.9672357368754639 | 0.968246498268356 |
| 21 | gemini-3.5-flash / macro.tfp_persistence.ar1 / TFP persistence | reml_predictive_lower | 0.8366804351617776 | 0.8410569248569418 |
| 21 | gemini-3.5-flash / macro.tfp_persistence.ar1 / TFP persistence | reml_predictive_upper | 0.9882251524395677 | 0.9885960350430211 |
| 21 | gemini-3.5-flash / macro.tfp_persistence.ar1 / TFP persistence | reml_typical_within_sd | 0.03730707381597933 | 0.036224548448648336 |
| 21 | gemini-3.5-flash / macro.tfp_persistence.ar1 / TFP persistence | bayes_latent_location | 0.9540049670673992 | 0.9554081493575777 |
| 21 | gemini-3.5-flash / macro.tfp_persistence.ar1 / TFP persistence | bayes_latent_lower | 0.9447741703138814 | 0.9463853696593049 |
| 21 | gemini-3.5-flash / macro.tfp_persistence.ar1 / TFP persistence | bayes_latent_upper | 0.9617589465613418 | 0.9629764115471635 |
| 21 | gemini-3.5-flash / macro.tfp_persistence.ar1 / TFP persistence | bayes_predictive_lower | 0.9042950789981498 | 0.906672955181107 |
| 21 | gemini-3.5-flash / macro.tfp_persistence.ar1 / TFP persistence | bayes_predictive_upper | 0.9785107718199425 | 0.9792781156810226 |
| 21 | gemini-3.5-flash / macro.tfp_persistence.ar1 / TFP persistence | bayes_tau_mean | 0.0013564871350610441 | 0.0013560142615332141 |
| 21 | gemini-3.5-flash / macro.tfp_persistence.ar1 / TFP persistence | bayes_interval_scale_mean | 0.29408500223606854 | 0.2974828011552619 |
| 21 | gemini-3.5-flash / macro.tfp_persistence.ar1 / TFP persistence | bayes_typical_within_sd | 0.02022603565365384 | 0.019750956349878675 |
| 22 | gemini-3.5-flash / production.capital_labor_substitution / Elasticity of substitution between capital and labor | pooled_point_estimate | 0.7733333333333333 | 0.74 |
| 22 | gemini-3.5-flash / production.capital_labor_substitution / Elasticity of substitution between capital and labor | between_run_sd | 0.13148721948877348 | 0.03192830510169099 |
| 22 | gemini-3.5-flash / production.capital_labor_substitution / Elasticity of substitution between capital and labor | total_sd | 1.2358066276053603 | 1.2292064711069135 |
| 22 | gemini-3.5-flash / production.capital_labor_substitution / Elasticity of substitution between capital and labor | reml_latent_location | 0.765203651726485 | 0.7392386604312868 |
| 22 | gemini-3.5-flash / production.capital_labor_substitution / Elasticity of substitution between capital and labor | reml_latent_lower | 0.6628802520865464 | 0.6401466328623567 |
| 22 | gemini-3.5-flash / production.capital_labor_substitution / Elasticity of substitution between capital and labor | reml_latent_upper | 0.8818301587304366 | 0.8522730058438805 |
| 22 | gemini-3.5-flash / production.capital_labor_substitution / Elasticity of substitution between capital and labor | reml_predictive_lower | 0.4317867218154452 | 0.4166248707367279 |
| 22 | gemini-3.5-flash / production.capital_labor_substitution / Elasticity of substitution between capital and labor | reml_predictive_upper | 1.320545627584984 | 1.2783452088843303 |
| 22 | gemini-3.5-flash / production.capital_labor_substitution / Elasticity of substitution between capital and labor | reml_typical_within_sd | 0.26106625212827417 | 0.2529168367854927 |
| 22 | gemini-3.5-flash / production.capital_labor_substitution / Elasticity of substitution between capital and labor | bayes_latent_location | 0.7652318726566693 | 0.7392441924450937 |
| 22 | gemini-3.5-flash / production.capital_labor_substitution / Elasticity of substitution between capital and labor | bayes_latent_lower | 0.7028507606923062 | 0.6836255758428317 |
| 22 | gemini-3.5-flash / production.capital_labor_substitution / Elasticity of substitution between capital and labor | bayes_latent_upper | 0.832665779811561 | 0.7990016387034214 |
| 22 | gemini-3.5-flash / production.capital_labor_substitution / Elasticity of substitution between capital and labor | bayes_predictive_lower | 0.5402442351164428 | 0.5368168115504958 |
| 22 | gemini-3.5-flash / production.capital_labor_substitution / Elasticity of substitution between capital and labor | bayes_predictive_upper | 1.0733008540599334 | 1.0098610080707584 |
| 22 | gemini-3.5-flash / production.capital_labor_substitution / Elasticity of substitution between capital and labor | bayes_tau_mean | 0.013225696284992958 | 0.009198669341026137 |
| 22 | gemini-3.5-flash / production.capital_labor_substitution / Elasticity of substitution between capital and labor | bayes_interval_scale_mean | 0.3466446821331856 | 0.29355057044394 |
| 22 | gemini-3.5-flash / production.capital_labor_substitution / Elasticity of substitution between capital and labor | bayes_typical_within_sd | 0.1537119722486391 | 0.1370320631081095 |
| 23 | gemini-3.5-flash / production.capital_share / Capital share in production | between_run_sd | 0.006110100926607784 | 0.0043520110293977995 |
| 23 | gemini-3.5-flash / production.capital_share / Capital share in production | total_sd | 0.1063323145196751 | 0.10624578945905469 |
| 24 | gemini-3.5-flash / tax.capital_gains_realizations.elasticity / Capital gains realizations elasticity | n_quantile_repaired_runs | 9 | 0 |
| 24 | gemini-3.5-flash / tax.capital_gains_realizations.elasticity / Capital gains realizations elasticity | pooled_point_estimate | 0.010000000000000009 | -0.55 |
| 24 | gemini-3.5-flash / tax.capital_gains_realizations.elasticity / Capital gains realizations elasticity | pooled_lower_bound | -1.1389771961917399 | -1.2925836339066685 |
| 24 | gemini-3.5-flash / tax.capital_gains_realizations.elasticity / Capital gains realizations elasticity | pooled_upper_bound | 1.2999999999999998 | -0.026304769590129985 |
| 24 | gemini-3.5-flash / tax.capital_gains_realizations.elasticity / Capital gains realizations elasticity | within_run_sd | 1.3858532394842136 | 1.319867246586228 |
| 24 | gemini-3.5-flash / tax.capital_gains_realizations.elasticity / Capital gains realizations elasticity | between_run_sd | 0.7967015334071683 | 0.14637129348186945 |
| 24 | gemini-3.5-flash / tax.capital_gains_realizations.elasticity / Capital gains realizations elasticity | total_sd | 1.5985376238056528 | 1.3279586229121245 |
| 24 | gemini-3.5-flash / tax.capital_gains_realizations.elasticity / Capital gains realizations elasticity | reml_latent_location | 0.2041663203554105 | -0.4783391880475225 |
| 24 | gemini-3.5-flash / tax.capital_gains_realizations.elasticity / Capital gains realizations elasticity | reml_latent_lower | -0.24212266185561404 | -0.5978705940635614 |
| 24 | gemini-3.5-flash / tax.capital_gains_realizations.elasticity / Capital gains realizations elasticity | reml_latent_upper | 0.5745989953829369 | -0.36292537933476154 |
| 24 | gemini-3.5-flash / tax.capital_gains_realizations.elasticity / Capital gains realizations elasticity | reml_predictive_lower | -1.9705220268034882 | -0.9996871863149828 |
| 24 | gemini-3.5-flash / tax.capital_gains_realizations.elasticity / Capital gains realizations elasticity | reml_predictive_upper | 1.2926831389701068 | -0.02719310647220574 |
| 24 | gemini-3.5-flash / tax.capital_gains_realizations.elasticity / Capital gains realizations elasticity | reml_tau | 0.948531670258146 | 0.0 |
| 24 | gemini-3.5-flash / tax.capital_gains_realizations.elasticity / Capital gains realizations elasticity | reml_typical_within_sd | 0.14222054668419293 | 0.29557310257500247 |
| 24 | gemini-3.5-flash / tax.capital_gains_realizations.elasticity / Capital gains realizations elasticity | bayes_latent_location | 0.202901788811916 | -0.4900897572580387 |
| 24 | gemini-3.5-flash / tax.capital_gains_realizations.elasticity / Capital gains realizations elasticity | bayes_latent_lower | -0.26124141255798605 | -0.5952341036155033 |
| 24 | gemini-3.5-flash / tax.capital_gains_realizations.elasticity / Capital gains realizations elasticity | bayes_latent_upper | 0.5836269493680213 | -0.39279430830544015 |
| 24 | gemini-3.5-flash / tax.capital_gains_realizations.elasticity / Capital gains realizations elasticity | bayes_predictive_lower | -2.164682595116453 | -0.9257370338440527 |
| 24 | gemini-3.5-flash / tax.capital_gains_realizations.elasticity / Capital gains realizations elasticity | bayes_predictive_upper | 1.337222352513571 | -0.10709317676061403 |
| 24 | gemini-3.5-flash / tax.capital_gains_realizations.elasticity / Capital gains realizations elasticity | bayes_tau_mean | 0.9740036107613579 | 0.061796437787488036 |
| 24 | gemini-3.5-flash / tax.capital_gains_realizations.elasticity / Capital gains realizations elasticity | bayes_interval_scale_mean | 0.8011422920923684 | 0.5699426007099081 |
| 24 | gemini-3.5-flash / tax.capital_gains_realizations.elasticity / Capital gains realizations elasticity | bayes_typical_within_sd | 0.12737055766367755 | 0.22392286355798038 |
| 25 | gemini-3.5-flash / tax.capital_gains_realizations.elasticity.net_of_tax_rate / Capital gains realizations elasticity (net-of-tax-rate convention) | between_run_sd | 0.08055363982396382 | 0.08185284899677524 |
| 25 | gemini-3.5-flash / tax.capital_gains_realizations.elasticity.net_of_tax_rate / Capital gains realizations elasticity (net-of-tax-rate convention) | total_sd | 1.3559832430954137 | 1.3560610441847947 |
| 26 | gemini-3.5-flash / tax.elasticity_of_taxable_income.top_earners / Elasticity of taxable income | between_run_sd | 0.01407914138796193 | 0.013186862148871263 |
| 26 | gemini-3.5-flash / tax.elasticity_of_taxable_income.top_earners / Elasticity of taxable income | total_sd | 0.6679912133487319 | 0.667973002614793 |
| 27 | gemini-3.5-flash / trade.armington_elasticity.import_domestic / Armington elasticity | between_run_sd | 0.24184476196289406 | 0.2731032568258549 |
| 27 | gemini-3.5-flash / trade.armington_elasticity.import_domestic / Armington elasticity | total_sd | 2.6529641964749127 | 2.655996146039707 |

## `results/gemini-3.5-flash-ies-clarify-batch15/summary.csv` (2 cells)

| line | row | column | old | new |
|---|---|---|---|---|
| 2 | gemini-3.5-flash / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | between_run_sd | 0.1699673171197595 | 0.13197921764008488 |
| 2 | gemini-3.5-flash / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | total_sd | 0.7535252797499379 | 0.7458753060815342 |

## `results/gemini-3.6-flash-armington-clarify-batch15/summary.csv` (2 cells)

| line | row | column | old | new |
|---|---|---|---|---|
| 2 | gemini-3.6-flash / trade.armington_elasticity.import_domestic / Armington elasticity | between_run_sd | 0.10198039027185571 | 0.10702491921666347 |
| 2 | gemini-3.6-flash / trade.armington_elasticity.import_domestic / Armington elasticity | total_sd | 2.5611418894270144 | 2.5613477138239373 |

## `results/gemini-3.6-flash-elasticities-batch15/summary.csv` (52 cells)

| line | row | column | old | new |
|---|---|---|---|---|
| 2 | gemini-3.6-flash / household.annual_discount_factor / Annual discount factor | between_run_sd | 0.0012472191289246482 | 0.001957251474219234 |
| 2 | gemini-3.6-flash / household.annual_discount_factor / Annual discount factor | total_sd | 0.12565227454058372 | 0.1256613280806788 |
| 3 | gemini-3.6-flash / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | between_run_sd | 0.13063945294843618 | 0.10100831923933569 |
| 3 | gemini-3.6-flash / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | total_sd | 0.7644497158450355 | 0.7599469599547355 |
| 4 | gemini-3.6-flash / household.relative_risk_aversion.crra / Coefficient of relative risk aversion | between_run_sd | 0.0 | 0.25799784667490727 |
| 4 | gemini-3.6-flash / household.relative_risk_aversion.crra / Coefficient of relative risk aversion | total_sd | 6.501636759736394 | 6.506753679404534 |
| 5 | gemini-3.6-flash / labor_supply.extensive_margin.single_mothers / Employment participation elasticity of single mothers | between_run_sd | 0.04422166387140534 | 0.03877863099984606 |
| 5 | gemini-3.6-flash / labor_supply.extensive_margin.single_mothers / Employment participation elasticity of single mothers | total_sd | 0.7026991246061306 | 0.7023775953067473 |
| 6 | gemini-3.6-flash / labor_supply.frisch_elasticity.prime_age / Frisch elasticity of labor supply | between_run_sd | 0.02867441755680877 | 0.027643564651952314 |
| 6 | gemini-3.6-flash / labor_supply.frisch_elasticity.prime_age / Frisch elasticity of labor supply | total_sd | 1.2668127519926184 | 1.2667898377614006 |
| 7 | gemini-3.6-flash / labor_supply.income_elasticity.prime_age / Income elasticity of labor supply | between_run_sd | 0.009092121131323905 | 0.011605715785288255 |
| 7 | gemini-3.6-flash / labor_supply.income_elasticity.prime_age / Income elasticity of labor supply | total_sd | 0.29730164547606824 | 0.2973891295508294 |
| 8 | gemini-3.6-flash / labor_supply.marshallian_wage_elasticity.prime_age / Uncompensated wage elasticity of labor supply | between_run_sd | 0.02 | 0.01585897923014663 |
| 8 | gemini-3.6-flash / labor_supply.marshallian_wage_elasticity.prime_age / Uncompensated wage elasticity of labor supply | total_sd | 0.5979786982920973 | 0.597854523135297 |
| 9 | gemini-3.6-flash / labor_supply.policy_response.substitution_elasticity.all / Substitution elasticity of labor supply in a tax-benefit simulation | between_run_sd | 0.012472191289246468 | 0.010747738780268558 |
| 9 | gemini-3.6-flash / labor_supply.policy_response.substitution_elasticity.all / Substitution elasticity of labor supply in a tax-benefit simulation | total_sd | 0.6376667810158462 | 0.6376353832280988 |
| 10 | gemini-3.6-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_1 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 1 | between_run_sd | 0.026549743668986506 | 0.025250324530367706 |
| 10 | gemini-3.6-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_1 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 1 | total_sd | 0.6366646378676226 | 0.6366117742479408 |
| 11 | gemini-3.6-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_10 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 10 | between_run_sd | 0.01720465053408526 | 0.01699727102279135 |
| 11 | gemini-3.6-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_10 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 10 | total_sd | 0.6327276950719884 | 0.6327220901259363 |
| 12 | gemini-3.6-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_2 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 2 | between_run_sd | 0.016110727964792765 | 0.013620103605414399 |
| 12 | gemini-3.6-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_2 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 2 | total_sd | 0.6339198928536283 | 0.6338614850440294 |
| 13 | gemini-3.6-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_3 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 3 | between_run_sd | 0.016110727964792765 | 0.013741926922944809 |
| 13 | gemini-3.6-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_3 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 3 | total_sd | 0.6334486397228009 | 0.6333928197940569 |
| 14 | gemini-3.6-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_4 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 4 | between_run_sd | 0.014996295838935993 | 0.015883027279317872 |
| 14 | gemini-3.6-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_4 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 4 | total_sd | 0.6316082261884252 | 0.6316299019643984 |
| 15 | gemini-3.6-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_5 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 5 | between_run_sd | 0.0132664991614216 | 0.014391220317340097 |
| 15 | gemini-3.6-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_5 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 5 | total_sd | 0.6335684837577633 | 0.6335930325006213 |
| 16 | gemini-3.6-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_6 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 6 | between_run_sd | 0.018427033281447007 | 0.017342914018891594 |
| 16 | gemini-3.6-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_6 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 6 | total_sd | 0.6325730776843977 | 0.6325424252350369 |
| 17 | gemini-3.6-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_7 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 7 | between_run_sd | 0.022568414506414343 | 0.022044248431028195 |
| 17 | gemini-3.6-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_7 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 7 | total_sd | 0.6320709469232425 | 0.6320524483775061 |
| 18 | gemini-3.6-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_8 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 8 | between_run_sd | 0.011999999999999999 | 0.01501637994546844 |
| 18 | gemini-3.6-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_8 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 8 | total_sd | 0.6325859197242168 | 0.632650327985373 |
| 19 | gemini-3.6-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_9 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 9 | between_run_sd | 0.02467567403109567 | 0.02288064441594443 |
| 19 | gemini-3.6-flash / labor_supply.policy_response.substitution_elasticity.primary.decile_9 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 9 | total_sd | 0.6316940330483493 | 0.6316264611215152 |
| 20 | gemini-3.6-flash / labor_supply.policy_response.substitution_elasticity.secondary / Secondary-earner substitution elasticity in a tax-benefit simulation | between_run_sd | 0.04784233364802442 | 0.04668834615475972 |
| 20 | gemini-3.6-flash / labor_supply.policy_response.substitution_elasticity.secondary / Secondary-earner substitution elasticity in a tax-benefit simulation | total_sd | 0.6373961985208956 | 0.6373106202368407 |
| 21 | gemini-3.6-flash / macro.tfp_persistence.ar1 / TFP persistence | between_run_sd | 0.00464279609239471 | 0.0049387498418122094 |
| 21 | gemini-3.6-flash / macro.tfp_persistence.ar1 / TFP persistence | total_sd | 0.12820776053387373 | 0.128218819038219 |
| 22 | gemini-3.6-flash / production.capital_labor_substitution / Elasticity of substitution between capital and labor | between_run_sd | 0.022110831935702634 | 0.011759747729720488 |
| 22 | gemini-3.6-flash / production.capital_labor_substitution / Elasticity of substitution between capital and labor | total_sd | 1.2347905524149971 | 1.2346485779812455 |
| 23 | gemini-3.6-flash / production.capital_share / Capital share in production | between_run_sd | 0.008692269873603517 | 0.006124041875174361 |
| 23 | gemini-3.6-flash / production.capital_share / Capital share in production | total_sd | 0.10664747874292303 | 0.10646893000098928 |
| 24 | gemini-3.6-flash / tax.capital_gains_realizations.elasticity / Capital gains realizations elasticity | between_run_sd | 0.0644635986860457 | 0.053020567288134104 |
| 24 | gemini-3.6-flash / tax.capital_gains_realizations.elasticity / Capital gains realizations elasticity | total_sd | 1.3208790475790482 | 1.3203700554516273 |
| 25 | gemini-3.6-flash / tax.capital_gains_realizations.elasticity.net_of_tax_rate / Capital gains realizations elasticity (net-of-tax-rate convention) | between_run_sd | 0.04268749491621903 | 0.0518006327717679 |
| 25 | gemini-3.6-flash / tax.capital_gains_realizations.elasticity.net_of_tax_rate / Capital gains realizations elasticity (net-of-tax-rate convention) | total_sd | 1.345199747662447 | 1.3455197673926773 |
| 26 | gemini-3.6-flash / tax.elasticity_of_taxable_income.top_earners / Elasticity of taxable income | between_run_sd | 0.0439696865275764 | 0.035917150035417185 |
| 26 | gemini-3.6-flash / tax.elasticity_of_taxable_income.top_earners / Elasticity of taxable income | total_sd | 0.6729149380782752 | 0.6724367793497187 |
| 27 | gemini-3.6-flash / trade.armington_elasticity.import_domestic / Armington elasticity | between_run_sd | 0.07999999999999997 | 0.1414433534041887 |
| 27 | gemini-3.6-flash / trade.armington_elasticity.import_domestic / Armington elasticity | total_sd | 2.6702687130699037 | 2.672815224107761 |

## `results/gemini-3.6-flash-ies-clarify-batch15/summary.csv` (2 cells)

| line | row | column | old | new |
|---|---|---|---|---|
| 2 | gemini-3.6-flash / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | between_run_sd | 0.04346134936801766 | 0.045357070991069164 |
| 2 | gemini-3.6-flash / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | total_sd | 0.6747255872245809 | 0.6748503486370556 |

## `results/glm-5.2-armington-clarify-batch15/summary.csv` (2 cells)

| line | row | column | old | new |
|---|---|---|---|---|
| 2 | glm-5.2 / trade.armington_elasticity.import_domestic / Armington elasticity | between_run_sd | 0.23513589451397862 | 0.3125439524646449 |
| 2 | glm-5.2 / trade.armington_elasticity.import_domestic / Armington elasticity | total_sd | 2.6002398660721884 | 2.608379227498265 |

## `results/glm-5.2-elasticities-batch15/summary.csv` (67 cells)

| line | row | column | old | new |
|---|---|---|---|---|
| 2 | glm-5.2 / household.annual_discount_factor / Annual discount factor | between_run_sd | 0.0040000000000000036 | 0.003998350354278062 |
| 2 | glm-5.2 / household.annual_discount_factor / Annual discount factor | total_sd | 0.12614876716929632 | 0.12614871487212578 |
| 3 | glm-5.2 / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | between_run_sd | 0.12472191289246472 | 0.10215884961938228 |
| 3 | glm-5.2 / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | total_sd | 0.7274374018505724 | 0.7239102490026723 |
| 4 | glm-5.2 / household.relative_risk_aversion.crra / Coefficient of relative risk aversion | between_run_sd | 0.2 | 0.44274823545667585 |
| 4 | glm-5.2 / household.relative_risk_aversion.crra / Coefficient of relative risk aversion | total_sd | 6.473932215688803 | 6.485971348482303 |
| 5 | glm-5.2 / labor_supply.extensive_margin.single_mothers / Employment participation elasticity of single mothers | between_run_sd | 0.060184900284225976 | 0.05783944732331619 |
| 5 | glm-5.2 / labor_supply.extensive_margin.single_mothers / Employment participation elasticity of single mothers | total_sd | 0.6854033869027624 | 0.685201417265188 |
| 6 | glm-5.2 / labor_supply.frisch_elasticity.prime_age / Frisch elasticity of labor supply | pooled_point_estimate | 0.43666666666666665 | 0.43 |
| 6 | glm-5.2 / labor_supply.frisch_elasticity.prime_age / Frisch elasticity of labor supply | between_run_sd | 0.06944222218666553 | 0.0688728700013454 |
| 6 | glm-5.2 / labor_supply.frisch_elasticity.prime_age / Frisch elasticity of labor supply | total_sd | 1.2759188274207207 | 1.2758879669338787 |
| 6 | glm-5.2 / labor_supply.frisch_elasticity.prime_age / Frisch elasticity of labor supply | reml_latent_location | 0.44535171170138976 | 0.4375846614023625 |
| 6 | glm-5.2 / labor_supply.frisch_elasticity.prime_age / Frisch elasticity of labor supply | reml_latent_lower | 0.3288039819531172 | 0.323000840451511 |
| 6 | glm-5.2 / labor_supply.frisch_elasticity.prime_age / Frisch elasticity of labor supply | reml_latent_upper | 0.6006451889305368 | 0.5903371166343371 |
| 6 | glm-5.2 / labor_supply.frisch_elasticity.prime_age / Frisch elasticity of labor supply | reml_predictive_lower | 0.03161315271670912 | 0.03103837076548106 |
| 6 | glm-5.2 / labor_supply.frisch_elasticity.prime_age / Frisch elasticity of labor supply | reml_predictive_upper | 4.065522691022989 | 4.021190777874326 |
| 6 | glm-5.2 / labor_supply.frisch_elasticity.prime_age / Frisch elasticity of labor supply | reml_typical_within_sd | 0.6952939801112622 | 0.6837232239453926 |
| 6 | glm-5.2 / labor_supply.frisch_elasticity.prime_age / Frisch elasticity of labor supply | bayes_latent_location | 0.4453583913346923 | 0.4376027541009004 |
| 6 | glm-5.2 / labor_supply.frisch_elasticity.prime_age / Frisch elasticity of labor supply | bayes_latent_lower | 0.3772634634918342 | 0.3706725704010987 |
| 6 | glm-5.2 / labor_supply.frisch_elasticity.prime_age / Frisch elasticity of labor supply | bayes_latent_upper | 0.5250777282166276 | 0.5159796520739193 |
| 6 | glm-5.2 / labor_supply.frisch_elasticity.prime_age / Frisch elasticity of labor supply | bayes_predictive_lower | 0.10588235947439084 | 0.10402620269463612 |
| 6 | glm-5.2 / labor_supply.frisch_elasticity.prime_age / Frisch elasticity of labor supply | bayes_predictive_upper | 1.687608599444859 | 1.661289677869119 |
| 6 | glm-5.2 / labor_supply.frisch_elasticity.prime_age / Frisch elasticity of labor supply | bayes_tau_mean | 0.014086374043514956 | 0.013823301570064088 |
| 6 | glm-5.2 / labor_supply.frisch_elasticity.prime_age / Frisch elasticity of labor supply | bayes_interval_scale_mean | 0.2957549888993532 | 0.2955501087059654 |
| 6 | glm-5.2 / labor_supply.frisch_elasticity.prime_age / Frisch elasticity of labor supply | bayes_typical_within_sd | 0.37812963804988164 | 0.3717175174968466 |
| 7 | glm-5.2 / labor_supply.income_elasticity.prime_age / Income elasticity of labor supply | between_run_sd | 0.02215099696778153 | 0.024840189210229454 |
| 7 | glm-5.2 / labor_supply.income_elasticity.prime_age / Income elasticity of labor supply | total_sd | 0.3106514883631209 | 0.3108548142711571 |
| 8 | glm-5.2 / labor_supply.marshallian_wage_elasticity.prime_age / Uncompensated wage elasticity of labor supply | between_run_sd | 0.03944053188733077 | 0.03845771126257458 |
| 8 | glm-5.2 / labor_supply.marshallian_wage_elasticity.prime_age / Uncompensated wage elasticity of labor supply | total_sd | 0.6066986758954839 | 0.6066355770422085 |
| 9 | glm-5.2 / labor_supply.policy_response.substitution_elasticity.all / Substitution elasticity of labor supply in a tax-benefit simulation | between_run_sd | 0.02211083193570266 | 0.019068487675277815 |
| 9 | glm-5.2 / labor_supply.policy_response.substitution_elasticity.all / Substitution elasticity of labor supply in a tax-benefit simulation | total_sd | 0.626456429716651 | 0.626356429412732 |
| 10 | glm-5.2 / labor_supply.policy_response.substitution_elasticity.primary.decile_1 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 1 | between_run_sd | 0.04735680169380811 | 0.04498711543937393 |
| 10 | glm-5.2 / labor_supply.policy_response.substitution_elasticity.primary.decile_1 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 1 | total_sd | 0.635347097830959 | 0.6351748645932954 |
| 11 | glm-5.2 / labor_supply.policy_response.substitution_elasticity.primary.decile_10 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 10 | between_run_sd | 0.05436502143433363 | 0.05192687165620513 |
| 11 | glm-5.2 / labor_supply.policy_response.substitution_elasticity.primary.decile_10 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 10 | total_sd | 0.6310623670534562 | 0.6308570008770257 |
| 12 | glm-5.2 / labor_supply.policy_response.substitution_elasticity.primary.decile_2 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 2 | between_run_sd | 0.04422166387140533 | 0.03985555865316099 |
| 12 | glm-5.2 / labor_supply.policy_response.substitution_elasticity.primary.decile_2 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 2 | total_sd | 0.6330191139382058 | 0.6327290957519743 |
| 13 | glm-5.2 / labor_supply.policy_response.substitution_elasticity.primary.decile_3 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 3 | between_run_sd | 0.02963481436119049 | 0.029578567691263668 |
| 13 | glm-5.2 / labor_supply.policy_response.substitution_elasticity.primary.decile_3 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 3 | total_sd | 0.6323152705643672 | 0.6323126369394599 |
| 14 | glm-5.2 / labor_supply.policy_response.substitution_elasticity.primary.decile_4 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 4 | between_run_sd | 0.03537733109712426 | 0.030505582367093984 |
| 14 | glm-5.2 / labor_supply.policy_response.substitution_elasticity.primary.decile_4 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 4 | total_sd | 0.6313109002526234 | 0.6310566438742071 |
| 15 | glm-5.2 / labor_supply.policy_response.substitution_elasticity.primary.decile_5 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 5 | between_run_sd | 0.02737395355686374 | 0.028078045990892368 |
| 15 | glm-5.2 / labor_supply.policy_response.substitution_elasticity.primary.decile_5 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 5 | total_sd | 0.6298794847252749 | 0.6299104766640344 |
| 16 | glm-5.2 / labor_supply.policy_response.substitution_elasticity.primary.decile_6 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 6 | between_run_sd | 0.043645032808887756 | 0.03616311042423695 |
| 16 | glm-5.2 / labor_supply.policy_response.substitution_elasticity.primary.decile_6 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 6 | total_sd | 0.6297186199230398 | 0.629244326112238 |
| 17 | glm-5.2 / labor_supply.policy_response.substitution_elasticity.primary.decile_7 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 7 | between_run_sd | 0.02958978802822953 | 0.028950167913541065 |
| 17 | glm-5.2 / labor_supply.policy_response.substitution_elasticity.primary.decile_7 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 7 | total_sd | 0.6301776601350871 | 0.6301479508813783 |
| 18 | glm-5.2 / labor_supply.policy_response.substitution_elasticity.primary.decile_8 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 8 | between_run_sd | 0.02893671255228094 | 0.02451181121192167 |
| 18 | glm-5.2 / labor_supply.policy_response.substitution_elasticity.primary.decile_8 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 8 | total_sd | 0.6278956687486652 | 0.6277073094913656 |
| 19 | glm-5.2 / labor_supply.policy_response.substitution_elasticity.primary.decile_9 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 9 | between_run_sd | 0.030912061651652344 | 0.026990348069057743 |
| 19 | glm-5.2 / labor_supply.policy_response.substitution_elasticity.primary.decile_9 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 9 | total_sd | 0.6293970030910538 | 0.6292165849954476 |
| 20 | glm-5.2 / labor_supply.policy_response.substitution_elasticity.secondary / Secondary-earner substitution elasticity in a tax-benefit simulation | between_run_sd | 0.07408703590297623 | 0.06332368347537033 |
| 20 | glm-5.2 / labor_supply.policy_response.substitution_elasticity.secondary / Secondary-earner substitution elasticity in a tax-benefit simulation | total_sd | 0.6456911671482995 | 0.6445448652602341 |
| 21 | glm-5.2 / macro.tfp_persistence.ar1 / TFP persistence | between_run_sd | 0.04161997383735627 | 0.0405319952492952 |
| 21 | glm-5.2 / macro.tfp_persistence.ar1 / TFP persistence | total_sd | 0.13844431542039645 | 0.1381211384578367 |
| 22 | glm-5.2 / production.capital_labor_substitution / Elasticity of substitution between capital and labor | between_run_sd | 0.04830458915396481 | 0.04950897786148375 |
| 22 | glm-5.2 / production.capital_labor_substitution / Elasticity of substitution between capital and labor | total_sd | 1.2570865650162857 | 1.2571334207235125 |
| 23 | glm-5.2 / production.capital_share / Capital share in production | between_run_sd | 0.005734883511361744 | 0.007073424441763224 |
| 23 | glm-5.2 / production.capital_share / Capital share in production | total_sd | 0.1134424474739896 | 0.11351798682734526 |
| 24 | glm-5.2 / tax.capital_gains_realizations.elasticity / Capital gains realizations elasticity | between_run_sd | 0.5434049032617289 | 0.5308476842644121 |
| 24 | glm-5.2 / tax.capital_gains_realizations.elasticity / Capital gains realizations elasticity | total_sd | 1.5041603647144068 | 1.4996695561948898 |
| 25 | glm-5.2 / tax.capital_gains_realizations.elasticity.net_of_tax_rate / Capital gains realizations elasticity (net-of-tax-rate convention) | between_run_sd | 0.7801424371371052 | 0.830638409096682 |
| 25 | glm-5.2 / tax.capital_gains_realizations.elasticity.net_of_tax_rate / Capital gains realizations elasticity (net-of-tax-rate convention) | total_sd | 1.778710402073492 | 1.8014296097513465 |
| 26 | glm-5.2 / tax.elasticity_of_taxable_income.top_earners / Elasticity of taxable income | between_run_sd | 0.0669991708074726 | 0.07807163733107919 |
| 26 | glm-5.2 / tax.elasticity_of_taxable_income.top_earners / Elasticity of taxable income | total_sd | 0.6839292625053494 | 0.6851025673414003 |
| 27 | glm-5.2 / trade.armington_elasticity.import_domestic / Armington elasticity | between_run_sd | 0.3872409528388695 | 0.45237355507736454 |
| 27 | glm-5.2 / trade.armington_elasticity.import_domestic / Armington elasticity | total_sd | 2.739507077519198 | 2.749470004483692 |

## `results/glm-5.2-ies-clarify-batch15/summary.csv` (2 cells)

| line | row | column | old | new |
|---|---|---|---|---|
| 2 | glm-5.2 / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | between_run_sd | 0.04422166387140532 | 0.05393257107001502 |
| 2 | glm-5.2 / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | total_sd | 0.6810744167204573 | 0.6817738098356212 |

## `results/gpt-5.4-armington-clarify-batch15/summary.csv` (2 cells)

| line | row | column | old | new |
|---|---|---|---|---|
| 2 | gpt-5.4 / trade.armington_elasticity.import_domestic / Armington elasticity | between_run_sd | 0.1699673171197595 | 0.11640876255677668 |
| 2 | gpt-5.4 / trade.armington_elasticity.import_domestic / Armington elasticity | total_sd | 2.6591603729164004 | 2.6562748351780168 |

## `results/gpt-5.4-elasticities-batch15/summary.csv` (48 cells)

| line | row | column | old | new |
|---|---|---|---|---|
| 2 | gpt-5.4 / household.annual_discount_factor / Annual discount factor | between_run_sd | 0.0040000000000000036 | 0.003530954387823336 |
| 2 | gpt-5.4 / household.annual_discount_factor / Annual discount factor | total_sd | 0.12800596367400666 | 0.12799216528756752 |
| 3 | gpt-5.4 / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | between_run_sd | 0.0 | 0.010426328852157564 |
| 3 | gpt-5.4 / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | total_sd | 0.6843404417961705 | 0.684419862811645 |
| 4 | gpt-5.4 / household.relative_risk_aversion.crra / Coefficient of relative risk aversion | between_run_sd | 0.0 | 0.2247591303299303 |
| 4 | gpt-5.4 / household.relative_risk_aversion.crra / Coefficient of relative risk aversion | total_sd | 6.639986979153901 | 6.6437898634740105 |
| 5 | gpt-5.4 / labor_supply.extensive_margin.single_mothers / Employment participation elasticity of single mothers | between_run_sd | 0.08055363982396382 | 0.08209115867944207 |
| 5 | gpt-5.4 / labor_supply.extensive_margin.single_mothers / Employment participation elasticity of single mothers | total_sd | 0.7715023673183238 | 0.7716644168433726 |
| 6 | gpt-5.4 / labor_supply.frisch_elasticity.prime_age / Frisch elasticity of labor supply | between_run_sd | 0.0 | 0.01892786012440097 |
| 6 | gpt-5.4 / labor_supply.frisch_elasticity.prime_age / Frisch elasticity of labor supply | total_sd | 1.2877429247632377 | 1.2878820226118022 |
| 7 | gpt-5.4 / labor_supply.income_elasticity.prime_age / Income elasticity of labor supply | between_run_sd | 0.0 | 0.004831148931672468 |
| 7 | gpt-5.4 / labor_supply.income_elasticity.prime_age / Income elasticity of labor supply | total_sd | 0.2967900001123129 | 0.29682931823973635 |
| 8 | gpt-5.4 / labor_supply.marshallian_wage_elasticity.prime_age / Uncompensated wage elasticity of labor supply | between_run_sd | 0.012472191289246471 | 0.011311670472962387 |
| 8 | gpt-5.4 / labor_supply.marshallian_wage_elasticity.prime_age / Uncompensated wage elasticity of labor supply | total_sd | 0.6041131068213413 | 0.604090261605554 |
| 10 | gpt-5.4 / labor_supply.policy_response.substitution_elasticity.primary.decile_1 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 1 | between_run_sd | 0.022271057451320086 | 0.023073397380244342 |
| 10 | gpt-5.4 / labor_supply.policy_response.substitution_elasticity.primary.decile_1 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 1 | total_sd | 0.6369025849985048 | 0.636931145764159 |
| 11 | gpt-5.4 / labor_supply.policy_response.substitution_elasticity.primary.decile_10 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 10 | between_run_sd | 0.028487814158962003 | 0.02705007701775851 |
| 11 | gpt-5.4 / labor_supply.policy_response.substitution_elasticity.primary.decile_10 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 10 | total_sd | 0.6355369241393016 | 0.635474101010856 |
| 12 | gpt-5.4 / labor_supply.policy_response.substitution_elasticity.primary.decile_2 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 2 | between_run_sd | 0.011999999999999999 | 0.01735628288417642 |
| 12 | gpt-5.4 / labor_supply.policy_response.substitution_elasticity.primary.decile_2 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 2 | total_sd | 0.63425848327879 | 0.6343824273785228 |
| 13 | gpt-5.4 / labor_supply.policy_response.substitution_elasticity.primary.decile_3 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 3 | between_run_sd | 0.017204650534085254 | 0.019978738698926912 |
| 13 | gpt-5.4 / labor_supply.policy_response.substitution_elasticity.primary.decile_3 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 3 | total_sd | 0.6359856381589482 | 0.6360667275879508 |
| 14 | gpt-5.4 / labor_supply.policy_response.substitution_elasticity.primary.decile_4 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 4 | between_run_sd | 0.02573367875415838 | 0.027672138013211448 |
| 14 | gpt-5.4 / labor_supply.policy_response.substitution_elasticity.primary.decile_4 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 4 | total_sd | 0.6352819387222233 | 0.6353634130689826 |
| 15 | gpt-5.4 / labor_supply.policy_response.substitution_elasticity.primary.decile_5 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 5 | between_run_sd | 0.02416609194718915 | 0.024450607808850527 |
| 15 | gpt-5.4 / labor_supply.policy_response.substitution_elasticity.primary.decile_5 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 5 | total_sd | 0.6364398679809079 | 0.6364507347609694 |
| 16 | gpt-5.4 / labor_supply.policy_response.substitution_elasticity.primary.decile_6 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 6 | between_run_sd | 0.032 | 0.033674025598374784 |
| 16 | gpt-5.4 / labor_supply.policy_response.substitution_elasticity.primary.decile_6 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 6 | total_sd | 0.6356205924134303 | 0.6357070689397751 |
| 17 | gpt-5.4 / labor_supply.policy_response.substitution_elasticity.primary.decile_7 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 7 | between_run_sd | 0.013564659966250543 | 0.012112482083463433 |
| 17 | gpt-5.4 / labor_supply.policy_response.substitution_elasticity.primary.decile_7 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 7 | total_sd | 0.6358048344421423 | 0.6357755104769468 |
| 18 | gpt-5.4 / labor_supply.policy_response.substitution_elasticity.primary.decile_8 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 8 | between_run_sd | 0.022171052197754528 | 0.0218103186588367 |
| 18 | gpt-5.4 / labor_supply.policy_response.substitution_elasticity.primary.decile_8 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 8 | total_sd | 0.6365826602518587 | 0.6365701986252402 |
| 19 | gpt-5.4 / labor_supply.policy_response.substitution_elasticity.primary.decile_9 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 9 | between_run_sd | 0.02529822128134704 | 0.026510794447210037 |
| 19 | gpt-5.4 / labor_supply.policy_response.substitution_elasticity.primary.decile_9 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 9 | total_sd | 0.6350242646282633 | 0.6350737271285035 |
| 20 | gpt-5.4 / labor_supply.policy_response.substitution_elasticity.secondary / Secondary-earner substitution elasticity in a tax-benefit simulation | between_run_sd | 0.022110831935702683 | 0.028744081516413517 |
| 20 | gpt-5.4 / labor_supply.policy_response.substitution_elasticity.secondary / Secondary-earner substitution elasticity in a tax-benefit simulation | total_sd | 0.6467975597768851 | 0.6470582791887194 |
| 21 | gpt-5.4 / macro.tfp_persistence.ar1 / TFP persistence | between_run_sd | 0.009568466729604892 | 0.008123713573374082 |
| 21 | gpt-5.4 / macro.tfp_persistence.ar1 / TFP persistence | total_sd | 0.12855531667124642 | 0.12845586250191585 |
| 22 | gpt-5.4 / production.capital_labor_substitution / Elasticity of substitution between capital and labor | between_run_sd | 0.0 | 0.003118047822311607 |
| 22 | gpt-5.4 / production.capital_labor_substitution / Elasticity of substitution between capital and labor | total_sd | 1.2301767036577396 | 1.2301806552065613 |
| 24 | gpt-5.4 / tax.capital_gains_realizations.elasticity / Capital gains realizations elasticity | between_run_sd | 0.1309792180292567 | 0.15049861571899364 |
| 24 | gpt-5.4 / tax.capital_gains_realizations.elasticity / Capital gains realizations elasticity | total_sd | 1.4385958624838164 | 1.4405041941394456 |
| 25 | gpt-5.4 / tax.capital_gains_realizations.elasticity.net_of_tax_rate / Capital gains realizations elasticity (net-of-tax-rate convention) | between_run_sd | 0.08055363982396382 | 0.0938429539177023 |
| 25 | gpt-5.4 / tax.capital_gains_realizations.elasticity.net_of_tax_rate / Capital gains realizations elasticity (net-of-tax-rate convention) | total_sd | 1.500952938043769 | 1.5017247861486915 |
| 26 | gpt-5.4 / tax.elasticity_of_taxable_income.top_earners / Elasticity of taxable income | between_run_sd | 0.02357022603955158 | 0.027695015596473097 |
| 26 | gpt-5.4 / tax.elasticity_of_taxable_income.top_earners / Elasticity of taxable income | total_sd | 0.6805049442632042 | 0.6806602952280969 |
| 27 | gpt-5.4 / trade.armington_elasticity.import_domestic / Armington elasticity | between_run_sd | 0.0 | 0.04001735734514324 |
| 27 | gpt-5.4 / trade.armington_elasticity.import_domestic / Armington elasticity | total_sd | 2.7258670893660404 | 2.726160812897467 |

## `results/gpt-5.4-ies-clarify-batch15/summary.csv` (2 cells)

| line | row | column | old | new |
|---|---|---|---|---|
| 2 | gpt-5.4 / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | between_run_sd | 0.0 | 0.004365266951236283 |
| 2 | gpt-5.4 / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | total_sd | 0.6678425827077649 | 0.6678568490577403 |

## `results/gpt-5.4-mini-armington-clarify-batch15/summary.csv` (2 cells)

| line | row | column | old | new |
|---|---|---|---|---|
| 2 | gpt-5.4-mini / trade.armington_elasticity.import_domestic / Armington elasticity | between_run_sd | 0.32659863237109044 | 0.3814492102495429 |
| 2 | gpt-5.4-mini / trade.armington_elasticity.import_domestic / Armington elasticity | total_sd | 2.7412688921170956 | 2.7483434960394275 |

## `results/gpt-5.4-mini-elasticities-batch15/summary.csv` (52 cells)

| line | row | column | old | new |
|---|---|---|---|---|
| 2 | gpt-5.4-mini / household.annual_discount_factor / Annual discount factor | between_run_sd | 0.008653836657164788 | 0.00699640780845588 |
| 2 | gpt-5.4-mini / household.annual_discount_factor / Annual discount factor | total_sd | 0.1259449670380767 | 0.1258419467250708 |
| 3 | gpt-5.4-mini / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | between_run_sd | 0.08 | 0.0896470703493551 |
| 3 | gpt-5.4-mini / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | total_sd | 0.755799360684508 | 0.7568812792197555 |
| 4 | gpt-5.4-mini / household.relative_risk_aversion.crra / Coefficient of relative risk aversion | between_run_sd | 0.0 | 0.2513793061402539 |
| 4 | gpt-5.4-mini / household.relative_risk_aversion.crra / Coefficient of relative risk aversion | total_sd | 6.728169668144029 | 6.732864073994728 |
| 5 | gpt-5.4-mini / labor_supply.extensive_margin.single_mothers / Employment participation elasticity of single mothers | between_run_sd | 0.13999999999999999 | 0.1297384120280326 |
| 5 | gpt-5.4-mini / labor_supply.extensive_margin.single_mothers / Employment participation elasticity of single mothers | total_sd | 0.726922928820136 | 0.7250165515352046 |
| 6 | gpt-5.4-mini / labor_supply.frisch_elasticity.prime_age / Frisch elasticity of labor supply | between_run_sd | 0.05617433182117573 | 0.06188171961267897 |
| 6 | gpt-5.4-mini / labor_supply.frisch_elasticity.prime_age / Frisch elasticity of labor supply | total_sd | 1.2921150565814348 | 1.292375762350529 |
| 7 | gpt-5.4-mini / labor_supply.income_elasticity.prime_age / Income elasticity of labor supply | between_run_sd | 0.01514375558880073 | 0.016786866559572365 |
| 7 | gpt-5.4-mini / labor_supply.income_elasticity.prime_age / Income elasticity of labor supply | total_sd | 0.30224936127126706 | 0.30233614065216297 |
| 8 | gpt-5.4-mini / labor_supply.marshallian_wage_elasticity.prime_age / Uncompensated wage elasticity of labor supply | between_run_sd | 0.034149995932975186 | 0.03941169454193344 |
| 8 | gpt-5.4-mini / labor_supply.marshallian_wage_elasticity.prime_age / Uncompensated wage elasticity of labor supply | total_sd | 0.6018300205299758 | 0.6021515034072036 |
| 9 | gpt-5.4-mini / labor_supply.policy_response.substitution_elasticity.all / Substitution elasticity of labor supply in a tax-benefit simulation | between_run_sd | 0.05617433182117572 | 0.06205419674231014 |
| 9 | gpt-5.4-mini / labor_supply.policy_response.substitution_elasticity.all / Substitution elasticity of labor supply in a tax-benefit simulation | total_sd | 0.6588113707444813 | 0.6593387520842379 |
| 10 | gpt-5.4-mini / labor_supply.policy_response.substitution_elasticity.primary.decile_1 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 1 | between_run_sd | 0.07370813312578801 | 0.07973275501462508 |
| 10 | gpt-5.4-mini / labor_supply.policy_response.substitution_elasticity.primary.decile_1 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 1 | total_sd | 0.6477789832273899 | 0.6484921236564438 |
| 11 | gpt-5.4-mini / labor_supply.policy_response.substitution_elasticity.primary.decile_10 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 10 | between_run_sd | 0.05584104424365847 | 0.05635454728768566 |
| 11 | gpt-5.4-mini / labor_supply.policy_response.substitution_elasticity.primary.decile_10 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 10 | total_sd | 0.6410656514308378 | 0.641110585018078 |
| 12 | gpt-5.4-mini / labor_supply.policy_response.substitution_elasticity.primary.decile_2 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 2 | between_run_sd | 0.04415125517279586 | 0.0448647473586507 |
| 12 | gpt-5.4-mini / labor_supply.policy_response.substitution_elasticity.primary.decile_2 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 2 | total_sd | 0.643136730537657 | 0.6431861055626815 |
| 13 | gpt-5.4-mini / labor_supply.policy_response.substitution_elasticity.primary.decile_3 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 3 | between_run_sd | 0.025157283018817613 | 0.02776470581311621 |
| 13 | gpt-5.4-mini / labor_supply.policy_response.substitution_elasticity.primary.decile_3 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 3 | total_sd | 0.6470422448856541 | 0.6471488674691989 |
| 14 | gpt-5.4-mini / labor_supply.policy_response.substitution_elasticity.primary.decile_4 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 4 | between_run_sd | 0.04959390643572611 | 0.05134835819078238 |
| 14 | gpt-5.4-mini / labor_supply.policy_response.substitution_elasticity.primary.decile_4 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 4 | total_sd | 0.6486145244973234 | 0.6487510306136108 |
| 15 | gpt-5.4-mini / labor_supply.policy_response.substitution_elasticity.primary.decile_5 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 5 | between_run_sd | 0.05344155686354955 | 0.05630820445449214 |
| 15 | gpt-5.4-mini / labor_supply.policy_response.substitution_elasticity.primary.decile_5 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 5 | total_sd | 0.6506323345194445 | 0.650874065093326 |
| 16 | gpt-5.4-mini / labor_supply.policy_response.substitution_elasticity.primary.decile_6 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 6 | between_run_sd | 0.0627375485654325 | 0.05619452820337581 |
| 16 | gpt-5.4-mini / labor_supply.policy_response.substitution_elasticity.primary.decile_6 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 6 | total_sd | 0.6550622118462406 | 0.6544679720115332 |
| 17 | gpt-5.4-mini / labor_supply.policy_response.substitution_elasticity.primary.decile_7 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 7 | between_run_sd | 0.028252826800556123 | 0.03410369807252906 |
| 17 | gpt-5.4-mini / labor_supply.policy_response.substitution_elasticity.primary.decile_7 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 7 | total_sd | 0.6470803616587699 | 0.6473622127097353 |
| 18 | gpt-5.4-mini / labor_supply.policy_response.substitution_elasticity.primary.decile_8 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 8 | between_run_sd | 0.04161196409153929 | 0.04818280006622926 |
| 18 | gpt-5.4-mini / labor_supply.policy_response.substitution_elasticity.primary.decile_8 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 8 | total_sd | 0.6430734492350864 | 0.6435320409876868 |
| 19 | gpt-5.4-mini / labor_supply.policy_response.substitution_elasticity.primary.decile_9 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 9 | between_run_sd | 0.057904135334955906 | 0.058406749039244886 |
| 19 | gpt-5.4-mini / labor_supply.policy_response.substitution_elasticity.primary.decile_9 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 9 | total_sd | 0.6437564551995663 | 0.6438018585368914 |
| 20 | gpt-5.4-mini / labor_supply.policy_response.substitution_elasticity.secondary / Secondary-earner substitution elasticity in a tax-benefit simulation | between_run_sd | 0.06548960901462833 | 0.06290369623480008 |
| 20 | gpt-5.4-mini / labor_supply.policy_response.substitution_elasticity.secondary / Secondary-earner substitution elasticity in a tax-benefit simulation | total_sd | 0.660200990019117 | 0.659949493016953 |
| 21 | gpt-5.4-mini / macro.tfp_persistence.ar1 / TFP persistence | between_run_sd | 0.01959591794226539 | 0.020900049840450942 |
| 21 | gpt-5.4-mini / macro.tfp_persistence.ar1 / TFP persistence | total_sd | 0.13529698557453362 | 0.13549201595994095 |
| 22 | gpt-5.4-mini / production.capital_labor_substitution / Elasticity of substitution between capital and labor | between_run_sd | 0.023570226039551605 | 0.031474857690967716 |
| 22 | gpt-5.4-mini / production.capital_labor_substitution / Elasticity of substitution between capital and labor | total_sd | 1.2348603581647064 | 1.2350365238638807 |
| 23 | gpt-5.4-mini / production.capital_share / Capital share in production | between_run_sd | 0.009092121131323887 | 0.009074139077620533 |
| 23 | gpt-5.4-mini / production.capital_share / Capital share in production | total_sd | 0.11910734537475941 | 0.11910597405485401 |
| 24 | gpt-5.4-mini / tax.capital_gains_realizations.elasticity / Capital gains realizations elasticity | between_run_sd | 0.31612233918743127 | 0.3198178735190112 |
| 24 | gpt-5.4-mini / tax.capital_gains_realizations.elasticity / Capital gains realizations elasticity | total_sd | 1.4715259346640444 | 1.4723242561602312 |
| 25 | gpt-5.4-mini / tax.capital_gains_realizations.elasticity.net_of_tax_rate / Capital gains realizations elasticity (net-of-tax-rate convention) | between_run_sd | 0.29166190472303144 | 0.33865594225145706 |
| 25 | gpt-5.4-mini / tax.capital_gains_realizations.elasticity.net_of_tax_rate / Capital gains realizations elasticity (net-of-tax-rate convention) | total_sd | 1.508636537204667 | 1.5184220039055165 |
| 26 | gpt-5.4-mini / tax.elasticity_of_taxable_income.top_earners / Elasticity of taxable income | between_run_sd | 0.06271629240742262 | 0.06593228007247706 |
| 26 | gpt-5.4-mini / tax.elasticity_of_taxable_income.top_earners / Elasticity of taxable income | total_sd | 0.7118473453315364 | 0.7121378906347968 |
| 27 | gpt-5.4-mini / trade.armington_elasticity.import_domestic / Armington elasticity | between_run_sd | 0.4 | 0.4874500971609528 |
| 27 | gpt-5.4-mini / trade.armington_elasticity.import_domestic / Armington elasticity | total_sd | 2.959341923140271 | 2.972425308612107 |

## `results/gpt-5.4-mini-ies-clarify-batch15/summary.csv` (2 cells)

| line | row | column | old | new |
|---|---|---|---|---|
| 2 | gpt-5.4-mini / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | between_run_sd | 0.0 | 0.01456069671715226 |
| 2 | gpt-5.4-mini / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | total_sd | 0.7239429314908431 | 0.7240893466585767 |

## `results/gpt-5.4-nano-armington-clarify-batch15/summary.csv` (2 cells)

| line | row | column | old | new |
|---|---|---|---|---|
| 2 | gpt-5.4-nano / trade.armington_elasticity.import_domestic / Armington elasticity | between_run_sd | 0.21746008573733452 | 0.22310909140298757 |
| 2 | gpt-5.4-nano / trade.armington_elasticity.import_domestic / Armington elasticity | total_sd | 2.526890491405505 | 2.5273829020022536 |

## `results/gpt-5.4-nano-elasticities-batch15/summary.csv` (52 cells)

| line | row | column | old | new |
|---|---|---|---|---|
| 2 | gpt-5.4-nano / household.annual_discount_factor / Annual discount factor | between_run_sd | 0.0044221663871405375 | 0.003742177025327503 |
| 2 | gpt-5.4-nano / household.annual_discount_factor / Annual discount factor | total_sd | 0.12559574700867326 | 0.12557364373147734 |
| 3 | gpt-5.4-nano / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | between_run_sd | 0.07408703590297626 | 0.07497008662719346 |
| 3 | gpt-5.4-nano / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | total_sd | 0.7249167097750686 | 0.7250074903827622 |
| 4 | gpt-5.4-nano / household.relative_risk_aversion.crra / Coefficient of relative risk aversion | between_run_sd | 0.2280350850198276 | 0.2251429175731125 |
| 4 | gpt-5.4-nano / household.relative_risk_aversion.crra / Coefficient of relative risk aversion | total_sd | 6.351863101571941 | 6.351759928905094 |
| 5 | gpt-5.4-nano / labor_supply.extensive_margin.single_mothers / Employment participation elasticity of single mothers | between_run_sd | 0.0669991708074726 | 0.06893872883462049 |
| 5 | gpt-5.4-nano / labor_supply.extensive_margin.single_mothers / Employment participation elasticity of single mothers | total_sd | 0.674766113800429 | 0.674961456512724 |
| 6 | gpt-5.4-nano / labor_supply.frisch_elasticity.prime_age / Frisch elasticity of labor supply | between_run_sd | 0.1948218559493661 | 0.1859064325586037 |
| 6 | gpt-5.4-nano / labor_supply.frisch_elasticity.prime_age / Frisch elasticity of labor supply | total_sd | 1.2868067135570733 | 1.285487131077813 |
| 7 | gpt-5.4-nano / labor_supply.income_elasticity.prime_age / Income elasticity of labor supply | between_run_sd | 0.04567518168789504 | 0.0472622823542551 |
| 7 | gpt-5.4-nano / labor_supply.income_elasticity.prime_age / Income elasticity of labor supply | total_sd | 0.32015143118357114 | 0.320381709839997 |
| 8 | gpt-5.4-nano / labor_supply.marshallian_wage_elasticity.prime_age / Uncompensated wage elasticity of labor supply | between_run_sd | 0.12931615006126138 | 0.13637808556444186 |
| 8 | gpt-5.4-nano / labor_supply.marshallian_wage_elasticity.prime_age / Uncompensated wage elasticity of labor supply | total_sd | 0.6366159971111139 | 0.6380879589314731 |
| 9 | gpt-5.4-nano / labor_supply.policy_response.substitution_elasticity.all / Substitution elasticity of labor supply in a tax-benefit simulation | between_run_sd | 0.08339997335464537 | 0.08551378381420287 |
| 9 | gpt-5.4-nano / labor_supply.policy_response.substitution_elasticity.all / Substitution elasticity of labor supply in a tax-benefit simulation | total_sd | 0.6421980289080101 | 0.6424759606397737 |
| 10 | gpt-5.4-nano / labor_supply.policy_response.substitution_elasticity.primary.decile_1 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 1 | between_run_sd | 0.20590181047177697 | 0.19715651284082797 |
| 10 | gpt-5.4-nano / labor_supply.policy_response.substitution_elasticity.primary.decile_1 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 1 | total_sd | 0.6696967441810261 | 0.6670598655043389 |
| 11 | gpt-5.4-nano / labor_supply.policy_response.substitution_elasticity.primary.decile_10 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 10 | between_run_sd | 0.21715329966536442 | 0.19369623698518829 |
| 11 | gpt-5.4-nano / labor_supply.policy_response.substitution_elasticity.primary.decile_10 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 10 | total_sd | 0.6805389285950756 | 0.6734210495670595 |
| 12 | gpt-5.4-nano / labor_supply.policy_response.substitution_elasticity.primary.decile_2 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 2 | between_run_sd | 0.1532231488167938 | 0.1509438821402032 |
| 12 | gpt-5.4-nano / labor_supply.policy_response.substitution_elasticity.primary.decile_2 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 2 | total_sd | 0.6607639885852672 | 0.6602391769906821 |
| 13 | gpt-5.4-nano / labor_supply.policy_response.substitution_elasticity.primary.decile_3 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 3 | between_run_sd | 0.30019993337774076 | 0.2830212035637377 |
| 13 | gpt-5.4-nano / labor_supply.policy_response.substitution_elasticity.primary.decile_3 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 3 | total_sd | 0.7072443128477991 | 0.7001253600050653 |
| 14 | gpt-5.4-nano / labor_supply.policy_response.substitution_elasticity.primary.decile_4 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 4 | between_run_sd | 0.27774968746857104 | 0.2643055470893909 |
| 14 | gpt-5.4-nano / labor_supply.policy_response.substitution_elasticity.primary.decile_4 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 4 | total_sd | 0.7000897720213379 | 0.6948656145055835 |
| 15 | gpt-5.4-nano / labor_supply.policy_response.substitution_elasticity.primary.decile_5 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 5 | between_run_sd | 0.16418147141366335 | 0.15126471461940122 |
| 15 | gpt-5.4-nano / labor_supply.policy_response.substitution_elasticity.primary.decile_5 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 5 | total_sd | 0.6640948570548236 | 0.6610199978064204 |
| 16 | gpt-5.4-nano / labor_supply.policy_response.substitution_elasticity.primary.decile_6 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 6 | between_run_sd | 0.15743781841306956 | 0.14492667111335994 |
| 16 | gpt-5.4-nano / labor_supply.policy_response.substitution_elasticity.primary.decile_6 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 6 | total_sd | 0.6571935703344098 | 0.6543091488143982 |
| 17 | gpt-5.4-nano / labor_supply.policy_response.substitution_elasticity.primary.decile_7 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 7 | between_run_sd | 0.23654926665613563 | 0.2132975399660192 |
| 17 | gpt-5.4-nano / labor_supply.policy_response.substitution_elasticity.primary.decile_7 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 7 | total_sd | 0.699633270999092 | 0.6921177637432007 |
| 18 | gpt-5.4-nano / labor_supply.policy_response.substitution_elasticity.primary.decile_8 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 8 | between_run_sd | 0.23061849207921054 | 0.2076959275800403 |
| 18 | gpt-5.4-nano / labor_supply.policy_response.substitution_elasticity.primary.decile_8 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 8 | total_sd | 0.6931362871037701 | 0.6858502912038782 |
| 19 | gpt-5.4-nano / labor_supply.policy_response.substitution_elasticity.primary.decile_9 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 9 | between_run_sd | 0.2418447619628941 | 0.2187980740825253 |
| 19 | gpt-5.4-nano / labor_supply.policy_response.substitution_elasticity.primary.decile_9 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 9 | total_sd | 0.6938484915070917 | 0.6861555490557517 |
| 20 | gpt-5.4-nano / labor_supply.policy_response.substitution_elasticity.secondary / Secondary-earner substitution elasticity in a tax-benefit simulation | between_run_sd | 0.2135935912480106 | 0.19312619363169428 |
| 20 | gpt-5.4-nano / labor_supply.policy_response.substitution_elasticity.secondary / Secondary-earner substitution elasticity in a tax-benefit simulation | total_sd | 0.6905301294818513 | 0.6844759777864134 |
| 21 | gpt-5.4-nano / macro.tfp_persistence.ar1 / TFP persistence | between_run_sd | 0.09601851673274045 | 0.0895693593752288 |
| 21 | gpt-5.4-nano / macro.tfp_persistence.ar1 / TFP persistence | total_sd | 0.17738425901759777 | 0.17397784321733487 |
| 22 | gpt-5.4-nano / production.capital_labor_substitution / Elasticity of substitution between capital and labor | between_run_sd | 0.10241527663824813 | 0.08752459971662571 |
| 22 | gpt-5.4-nano / production.capital_labor_substitution / Elasticity of substitution between capital and labor | total_sd | 1.2430606827951367 | 1.2419225127912683 |
| 23 | gpt-5.4-nano / production.capital_share / Capital share in production | between_run_sd | 0.019933221850301403 | 0.02048630979188026 |
| 23 | gpt-5.4-nano / production.capital_share / Capital share in production | total_sd | 0.12215142583422156 | 0.12224289913483273 |
| 24 | gpt-5.4-nano / tax.capital_gains_realizations.elasticity / Capital gains realizations elasticity | between_run_sd | 0.09809292646374775 | 0.08751407823252717 |
| 24 | gpt-5.4-nano / tax.capital_gains_realizations.elasticity / Capital gains realizations elasticity | total_sd | 1.3047438371402855 | 1.3039911703007128 |
| 25 | gpt-5.4-nano / tax.capital_gains_realizations.elasticity.net_of_tax_rate / Capital gains realizations elasticity (net-of-tax-rate convention) | between_run_sd | 0.2953340857778225 | 0.2854916062202569 |
| 25 | gpt-5.4-nano / tax.capital_gains_realizations.elasticity.net_of_tax_rate / Capital gains realizations elasticity (net-of-tax-rate convention) | total_sd | 1.3913266540727716 | 1.3892707055622147 |
| 26 | gpt-5.4-nano / tax.elasticity_of_taxable_income.top_earners / Elasticity of taxable income | between_run_sd | 0.1012719112093773 | 0.09673443888640004 |
| 26 | gpt-5.4-nano / tax.elasticity_of_taxable_income.top_earners / Elasticity of taxable income | total_sd | 0.7065480963812726 | 0.7059120087990193 |
| 27 | gpt-5.4-nano / trade.armington_elasticity.import_domestic / Armington elasticity | between_run_sd | 0.47842333648024415 | 0.4866761985367912 |
| 27 | gpt-5.4-nano / trade.armington_elasticity.import_domestic / Armington elasticity | total_sd | 2.594380171104887 | 2.5959147338762025 |

## `results/gpt-5.4-nano-ies-clarify-batch15/summary.csv` (2 cells)

| line | row | column | old | new |
|---|---|---|---|---|
| 2 | gpt-5.4-nano / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | between_run_sd | 0.08692269873603535 | 0.0855295595426257 |
| 2 | gpt-5.4-nano / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | total_sd | 0.7146704514436473 | 0.7145023472086475 |

## `results/gpt-5.5-armington-clarify-batch15/summary.csv` (2 cells)

| line | row | column | old | new |
|---|---|---|---|---|
| 2 | gpt-5.5 / trade.armington_elasticity.import_domestic / Armington elasticity | between_run_sd | 0.22744962812309308 | 0.2613150503808679 |
| 2 | gpt-5.5 / trade.armington_elasticity.import_domestic / Armington elasticity | total_sd | 2.713420837041112 | 2.7164691901641573 |

## `results/gpt-5.5-elasticities-batch15/summary.csv` (52 cells)

| line | row | column | old | new |
|---|---|---|---|---|
| 2 | gpt-5.5 / household.annual_discount_factor / Annual discount factor | between_run_sd | 0.0 | 0.001725945795466624 |
| 2 | gpt-5.5 / household.annual_discount_factor / Annual discount factor | total_sd | 0.12749945942151197 | 0.12751114085312965 |
| 3 | gpt-5.5 / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | between_run_sd | 0.018257418583505543 | 0.024691710259833258 |
| 3 | gpt-5.5 / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | total_sd | 0.7382212574831478 | 0.7384084047613639 |
| 4 | gpt-5.5 / household.relative_risk_aversion.crra / Coefficient of relative risk aversion | between_run_sd | 0.0 | 0.07648529270389165 |
| 4 | gpt-5.5 / household.relative_risk_aversion.crra / Coefficient of relative risk aversion | total_sd | 6.8994290725956295 | 6.8998530076935545 |
| 5 | gpt-5.5 / labor_supply.extensive_margin.single_mothers / Employment participation elasticity of single mothers | between_run_sd | 0.06110100926607789 | 0.0573447663019235 |
| 5 | gpt-5.5 / labor_supply.extensive_margin.single_mothers / Employment participation elasticity of single mothers | total_sd | 0.7056726607759909 | 0.7053573513160231 |
| 6 | gpt-5.5 / labor_supply.frisch_elasticity.prime_age / Frisch elasticity of labor supply | between_run_sd | 0.052281290471193745 | 0.05144748131185172 |
| 6 | gpt-5.5 / labor_supply.frisch_elasticity.prime_age / Frisch elasticity of labor supply | total_sd | 1.2862462979106641 | 1.2862126763832213 |
| 7 | gpt-5.5 / labor_supply.income_elasticity.prime_age / Income elasticity of labor supply | between_run_sd | 0.011972189997378648 | 0.01438812203018711 |
| 7 | gpt-5.5 / labor_supply.income_elasticity.prime_age / Income elasticity of labor supply | total_sd | 0.2971813320133387 | 0.29728846062275016 |
| 8 | gpt-5.5 / labor_supply.marshallian_wage_elasticity.prime_age / Uncompensated wage elasticity of labor supply | between_run_sd | 0.0074833147735478825 | 0.0086898727774858 |
| 8 | gpt-5.5 / labor_supply.marshallian_wage_elasticity.prime_age / Uncompensated wage elasticity of labor supply | total_sd | 0.5932162220566048 | 0.5932326693633788 |
| 9 | gpt-5.5 / labor_supply.policy_response.substitution_elasticity.all / Substitution elasticity of labor supply in a tax-benefit simulation | between_run_sd | 0.024494897427831775 | 0.021018338553643 |
| 9 | gpt-5.5 / labor_supply.policy_response.substitution_elasticity.all / Substitution elasticity of labor supply in a tax-benefit simulation | total_sd | 0.6526363778296967 | 0.6525151432895808 |
| 10 | gpt-5.5 / labor_supply.policy_response.substitution_elasticity.primary.decile_1 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 1 | between_run_sd | 0.02022100118413747 | 0.02159780081397178 |
| 10 | gpt-5.5 / labor_supply.policy_response.substitution_elasticity.primary.decile_1 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 1 | total_sd | 0.6406636424659805 | 0.6407085756323923 |
| 11 | gpt-5.5 / labor_supply.policy_response.substitution_elasticity.primary.decile_10 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 10 | between_run_sd | 0.04062839729384691 | 0.04083548973897855 |
| 11 | gpt-5.5 / labor_supply.policy_response.substitution_elasticity.primary.decile_10 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 10 | total_sd | 0.6395059518878616 | 0.6395191420556194 |
| 12 | gpt-5.5 / labor_supply.policy_response.substitution_elasticity.primary.decile_2 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 2 | between_run_sd | 0.04080304999493162 | 0.03780928016594163 |
| 12 | gpt-5.5 / labor_supply.policy_response.substitution_elasticity.primary.decile_2 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 2 | total_sd | 0.6388484920803471 | 0.6386642690890975 |
| 13 | gpt-5.5 / labor_supply.policy_response.substitution_elasticity.primary.decile_3 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 3 | between_run_sd | 0.024729649321321875 | 0.024777476331001365 |
| 13 | gpt-5.5 / labor_supply.policy_response.substitution_elasticity.primary.decile_3 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 3 | total_sd | 0.637116079385155 | 0.6371179375821159 |
| 14 | gpt-5.5 / labor_supply.policy_response.substitution_elasticity.primary.decile_4 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 4 | between_run_sd | 0.021847959477565255 | 0.0231766405388414 |
| 14 | gpt-5.5 / labor_supply.policy_response.substitution_elasticity.primary.decile_4 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 4 | total_sd | 0.6373242066989488 | 0.6373711381744374 |
| 15 | gpt-5.5 / labor_supply.policy_response.substitution_elasticity.primary.decile_5 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 5 | between_run_sd | 0.034615346628659116 | 0.036570647003057274 |
| 15 | gpt-5.5 / labor_supply.policy_response.substitution_elasticity.primary.decile_5 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 5 | total_sd | 0.63812698144213 | 0.6382360334895268 |
| 16 | gpt-5.5 / labor_supply.policy_response.substitution_elasticity.primary.decile_6 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 6 | between_run_sd | 0.023626726862225802 | 0.02396973786534457 |
| 16 | gpt-5.5 / labor_supply.policy_response.substitution_elasticity.primary.decile_6 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 6 | total_sd | 0.6381443258037758 | 0.6381571175397691 |
| 17 | gpt-5.5 / labor_supply.policy_response.substitution_elasticity.primary.decile_7 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 7 | between_run_sd | 0.02305548862105411 | 0.025730602186674313 |
| 17 | gpt-5.5 / labor_supply.policy_response.substitution_elasticity.primary.decile_7 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 7 | total_sd | 0.637688484118835 | 0.6377908051321461 |
| 18 | gpt-5.5 / labor_supply.policy_response.substitution_elasticity.primary.decile_8 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 8 | between_run_sd | 0.034998412662417835 | 0.036009975469768564 |
| 18 | gpt-5.5 / labor_supply.policy_response.substitution_elasticity.primary.decile_8 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 8 | total_sd | 0.638750335942508 | 0.6388065600094532 |
| 19 | gpt-5.5 / labor_supply.policy_response.substitution_elasticity.primary.decile_9 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 9 | between_run_sd | 0.03702251567177286 | 0.03683289592500462 |
| 19 | gpt-5.5 / labor_supply.policy_response.substitution_elasticity.primary.decile_9 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 9 | total_sd | 0.638079126928802 | 0.6380681529255146 |
| 20 | gpt-5.5 / labor_supply.policy_response.substitution_elasticity.secondary / Secondary-earner substitution elasticity in a tax-benefit simulation | between_run_sd | 0.04268749491621899 | 0.048258608903835334 |
| 20 | gpt-5.5 / labor_supply.policy_response.substitution_elasticity.secondary / Secondary-earner substitution elasticity in a tax-benefit simulation | total_sd | 0.6419146360693142 | 0.6423091709691768 |
| 21 | gpt-5.5 / macro.tfp_persistence.ar1 / TFP persistence | between_run_sd | 0.0044221663871405375 | 0.004602867463754434 |
| 21 | gpt-5.5 / macro.tfp_persistence.ar1 / TFP persistence | total_sd | 0.13012206742346033 | 0.13012833382430164 |
| 22 | gpt-5.5 / production.capital_labor_substitution / Elasticity of substitution between capital and labor | between_run_sd | 0.04163331998932265 | 0.03012981174112371 |
| 22 | gpt-5.5 / production.capital_labor_substitution / Elasticity of substitution between capital and labor | total_sd | 1.244845092995733 | 1.2445134703078862 |
| 23 | gpt-5.5 / production.capital_share / Capital share in production | between_run_sd | 0.008793937305515264 | 0.005856477894889844 |
| 23 | gpt-5.5 / production.capital_share / Capital share in production | total_sd | 0.1158816565869393 | 0.11569582245411168 |
| 24 | gpt-5.5 / tax.capital_gains_realizations.elasticity / Capital gains realizations elasticity | between_run_sd | 0.08653836657164779 | 0.07473490185686708 |
| 24 | gpt-5.5 / tax.capital_gains_realizations.elasticity / Capital gains realizations elasticity | total_sd | 1.345222087715548 | 1.344514366581646 |
| 25 | gpt-5.5 / tax.capital_gains_realizations.elasticity.net_of_tax_rate / Capital gains realizations elasticity (net-of-tax-rate convention) | between_run_sd | 0.6611774009715967 | 0.6846916073840998 |
| 25 | gpt-5.5 / tax.capital_gains_realizations.elasticity.net_of_tax_rate / Capital gains realizations elasticity (net-of-tax-rate convention) | total_sd | 1.7390793082196618 | 1.7481544216528597 |
| 26 | gpt-5.5 / tax.elasticity_of_taxable_income.top_earners / Elasticity of taxable income | between_run_sd | 0.023570226039551605 | 0.025045369942477507 |
| 26 | gpt-5.5 / tax.elasticity_of_taxable_income.top_earners / Elasticity of taxable income | total_sd | 0.6822876816677519 | 0.6823402344545979 |
| 27 | gpt-5.5 / trade.armington_elasticity.import_domestic / Armington elasticity | between_run_sd | 0.24997777679003566 | 0.3061966506820231 |
| 27 | gpt-5.5 / trade.armington_elasticity.import_domestic / Armington elasticity | total_sd | 2.8125091110963534 | 2.818062277523334 |

## `results/gpt-5.5-ies-clarify-batch15/summary.csv` (2 cells)

| line | row | column | old | new |
|---|---|---|---|---|
| 2 | gpt-5.5 / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | between_run_sd | 0.06879922480183431 | 0.060117708613094074 |
| 2 | gpt-5.5 / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | total_sd | 0.7037875705384719 | 0.702991998531989 |

## `results/gpt-5.6-luna-armington-clarify-batch15/summary.csv` (2 cells)

| line | row | column | old | new |
|---|---|---|---|---|
| 2 | gpt-5.6-luna / trade.armington_elasticity.import_domestic / Armington elasticity | between_run_sd | 0.5537749241945383 | 0.5931452534301077 |
| 2 | gpt-5.6-luna / trade.armington_elasticity.import_domestic / Armington elasticity | total_sd | 2.9236162028195305 | 2.9313284234948647 |

## `results/gpt-5.6-luna-elasticities-batch15/summary.csv` (52 cells)

| line | row | column | old | new |
|---|---|---|---|---|
| 2 | gpt-5.6-luna / household.annual_discount_factor / Annual discount factor | between_run_sd | 0.0044221663871405375 | 0.0033693471177663028 |
| 2 | gpt-5.6-luna / household.annual_discount_factor / Annual discount factor | total_sd | 0.12858050871816545 | 0.128548606241634 |
| 3 | gpt-5.6-luna / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | between_run_sd | 0.09521904571390467 | 0.10546938734375333 |
| 3 | gpt-5.6-luna / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | total_sd | 0.7796012379914348 | 0.7809194678568192 |
| 4 | gpt-5.6-luna / household.relative_risk_aversion.crra / Coefficient of relative risk aversion | between_run_sd | 0.2449489742783178 | 0.27635102476540396 |
| 4 | gpt-5.6-luna / household.relative_risk_aversion.crra / Coefficient of relative risk aversion | total_sd | 6.483636057628296 | 6.484898335106471 |
| 5 | gpt-5.6-luna / labor_supply.extensive_margin.single_mothers / Employment participation elasticity of single mothers | between_run_sd | 0.05715476066494084 | 0.07029847082262887 |
| 5 | gpt-5.6-luna / labor_supply.extensive_margin.single_mothers / Employment participation elasticity of single mothers | total_sd | 0.7294706271217049 | 0.7306179604736437 |
| 6 | gpt-5.6-luna / labor_supply.frisch_elasticity.prime_age / Frisch elasticity of labor supply | between_run_sd | 0.043969686527576386 | 0.0333797593360607 |
| 6 | gpt-5.6-luna / labor_supply.frisch_elasticity.prime_age / Frisch elasticity of labor supply | total_sd | 1.3137948903420538 | 1.3134831132865352 |
| 7 | gpt-5.6-luna / labor_supply.income_elasticity.prime_age / Income elasticity of labor supply | between_run_sd | 0.016679994670929073 | 0.0219509807424533 |
| 7 | gpt-5.6-luna / labor_supply.income_elasticity.prime_age / Income elasticity of labor supply | total_sd | 0.3431321720561918 | 0.3434287565614349 |
| 8 | gpt-5.6-luna / labor_supply.marshallian_wage_elasticity.prime_age / Uncompensated wage elasticity of labor supply | between_run_sd | 0.021969676071045444 | 0.027153862013021692 |
| 8 | gpt-5.6-luna / labor_supply.marshallian_wage_elasticity.prime_age / Uncompensated wage elasticity of labor supply | total_sd | 0.6175067509752424 | 0.6177129212308543 |
| 9 | gpt-5.6-luna / labor_supply.policy_response.substitution_elasticity.all / Substitution elasticity of labor supply in a tax-benefit simulation | between_run_sd | 0.02211083193570266 | 0.019684314116123584 |
| 9 | gpt-5.6-luna / labor_supply.policy_response.substitution_elasticity.all / Substitution elasticity of labor supply in a tax-benefit simulation | total_sd | 0.6565348588105078 | 0.6564576179515832 |
| 10 | gpt-5.6-luna / labor_supply.policy_response.substitution_elasticity.primary.decile_1 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 1 | between_run_sd | 0.03496029493900505 | 0.041900046406762946 |
| 10 | gpt-5.6-luna / labor_supply.policy_response.substitution_elasticity.primary.decile_1 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 1 | total_sd | 0.6483435228419507 | 0.6487547420079315 |
| 11 | gpt-5.6-luna / labor_supply.policy_response.substitution_elasticity.primary.decile_10 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 10 | between_run_sd | 0.04730985333122712 | 0.052923781673900314 |
| 11 | gpt-5.6-luna / labor_supply.policy_response.substitution_elasticity.primary.decile_10 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 10 | total_sd | 0.6500184217475002 | 0.6504511150390593 |
| 12 | gpt-5.6-luna / labor_supply.policy_response.substitution_elasticity.primary.decile_2 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 2 | between_run_sd | 0.033954217541991585 | 0.036831312161740265 |
| 12 | gpt-5.6-luna / labor_supply.policy_response.substitution_elasticity.primary.decile_2 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 2 | total_sd | 0.649074486394966 | 0.6492313497941666 |
| 13 | gpt-5.6-luna / labor_supply.policy_response.substitution_elasticity.primary.decile_3 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 3 | between_run_sd | 0.04942334131426837 | 0.05329664362999065 |
| 13 | gpt-5.6-luna / labor_supply.policy_response.substitution_elasticity.primary.decile_3 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 3 | total_sd | 0.6513838985831115 | 0.6516892272309623 |
| 14 | gpt-5.6-luna / labor_supply.policy_response.substitution_elasticity.primary.decile_4 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 4 | between_run_sd | 0.04714045207910317 | 0.051701182019584645 |
| 14 | gpt-5.6-luna / labor_supply.policy_response.substitution_elasticity.primary.decile_4 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 4 | total_sd | 0.6478551953690475 | 0.6482030115377949 |
| 15 | gpt-5.6-luna / labor_supply.policy_response.substitution_elasticity.primary.decile_5 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 5 | between_run_sd | 0.04642796092394706 | 0.04683337485170165 |
| 15 | gpt-5.6-luna / labor_supply.policy_response.substitution_elasticity.primary.decile_5 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 5 | total_sd | 0.6511197385188756 | 0.651148772043174 |
| 16 | gpt-5.6-luna / labor_supply.policy_response.substitution_elasticity.primary.decile_6 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 6 | between_run_sd | 0.041633319989322654 | 0.04569493042632483 |
| 16 | gpt-5.6-luna / labor_supply.policy_response.substitution_elasticity.primary.decile_6 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 6 | total_sd | 0.6503708205067834 | 0.6506434488258528 |
| 17 | gpt-5.6-luna / labor_supply.policy_response.substitution_elasticity.primary.decile_7 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 7 | between_run_sd | 0.04422166387140533 | 0.04777477251530236 |
| 17 | gpt-5.6-luna / labor_supply.policy_response.substitution_elasticity.primary.decile_7 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 7 | total_sd | 0.6499205710016503 | 0.6501719941249735 |
| 18 | gpt-5.6-luna / labor_supply.policy_response.substitution_elasticity.primary.decile_8 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 8 | between_run_sd | 0.04707440918375928 | 0.053136652970326326 |
| 18 | gpt-5.6-luna / labor_supply.policy_response.substitution_elasticity.primary.decile_8 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 8 | total_sd | 0.6491754235609629 | 0.649643159314746 |
| 19 | gpt-5.6-luna / labor_supply.policy_response.substitution_elasticity.primary.decile_9 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 9 | between_run_sd | 0.03593821859184948 | 0.03899291246139769 |
| 19 | gpt-5.6-luna / labor_supply.policy_response.substitution_elasticity.primary.decile_9 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 9 | total_sd | 0.6464262794180187 | 0.6466032990859921 |
| 20 | gpt-5.6-luna / labor_supply.policy_response.substitution_elasticity.secondary / Secondary-earner substitution elasticity in a tax-benefit simulation | between_run_sd | 0.08 | 0.09075202783164436 |
| 20 | gpt-5.6-luna / labor_supply.policy_response.substitution_elasticity.secondary / Secondary-earner substitution elasticity in a tax-benefit simulation | total_sd | 0.6996217728172845 | 0.7009326326798857 |
| 21 | gpt-5.6-luna / macro.tfp_persistence.ar1 / TFP persistence | between_run_sd | 0.007180219742846011 | 0.010559934764108252 |
| 21 | gpt-5.6-luna / macro.tfp_persistence.ar1 / TFP persistence | total_sd | 0.13950418527174493 | 0.13971891201623352 |
| 22 | gpt-5.6-luna / production.capital_labor_substitution / Elasticity of substitution between capital and labor | between_run_sd | 0.07408703590297626 | 0.0748852826365472 |
| 22 | gpt-5.6-luna / production.capital_labor_substitution / Elasticity of substitution between capital and labor | total_sd | 1.2905335890415424 | 1.2905796608931628 |
| 23 | gpt-5.6-luna / production.capital_share / Capital share in production | between_run_sd | 0.011469767022723495 | 0.01077793527949064 |
| 23 | gpt-5.6-luna / production.capital_share / Capital share in production | total_sd | 0.12296836201054137 | 0.12290576222817581 |
| 24 | gpt-5.6-luna / tax.capital_gains_realizations.elasticity / Capital gains realizations elasticity | between_run_sd | 0.3352610922848042 | 0.34248382767982233 |
| 24 | gpt-5.6-luna / tax.capital_gains_realizations.elasticity / Capital gains realizations elasticity | total_sd | 1.546859771978917 | 1.5484412570029542 |
| 25 | gpt-5.6-luna / tax.capital_gains_realizations.elasticity.net_of_tax_rate / Capital gains realizations elasticity (net-of-tax-rate convention) | between_run_sd | 0.06548960901462832 | 0.0726963815391721 |
| 25 | gpt-5.6-luna / tax.capital_gains_realizations.elasticity.net_of_tax_rate / Capital gains realizations elasticity (net-of-tax-rate convention) | total_sd | 1.5003383530427767 | 1.50067019981444 |
| 26 | gpt-5.6-luna / tax.elasticity_of_taxable_income.top_earners / Elasticity of taxable income | between_run_sd | 0.05120763831912407 | 0.05741180676094034 |
| 26 | gpt-5.6-luna / tax.elasticity_of_taxable_income.top_earners / Elasticity of taxable income | total_sd | 0.7042388355522579 | 0.7047171282389363 |
| 27 | gpt-5.6-luna / trade.armington_elasticity.import_domestic / Armington elasticity | between_run_sd | 0.46427960923947065 | 0.4756064111566761 |
| 27 | gpt-5.6-luna / trade.armington_elasticity.import_domestic / Armington elasticity | total_sd | 3.238516212240483 | 3.240159434306007 |

## `results/gpt-5.6-luna-ies-clarify-batch15/summary.csv` (2 cells)

| line | row | column | old | new |
|---|---|---|---|---|
| 2 | gpt-5.6-luna / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | between_run_sd | 0.09944289260117534 | 0.0948604237814696 |
| 2 | gpt-5.6-luna / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | total_sd | 0.7705750017573456 | 0.7699970418413595 |

## `results/gpt-5.6-sol-armington-clarify-batch15/summary.csv` (2 cells)

| line | row | column | old | new |
|---|---|---|---|---|
| 2 | gpt-5.6-sol / trade.armington_elasticity.import_domestic / Armington elasticity | between_run_sd | 0.2449489742783178 | 0.26908280427324877 |
| 2 | gpt-5.6-sol / trade.armington_elasticity.import_domestic / Armington elasticity | total_sd | 2.6319648342804447 | 2.6343204900779336 |

## `results/gpt-5.6-sol-elasticities-batch15/summary.csv` (52 cells)

| line | row | column | old | new |
|---|---|---|---|---|
| 2 | gpt-5.6-sol / household.annual_discount_factor / Annual discount factor | between_run_sd | 0.0 | 0.0011022703842524177 |
| 2 | gpt-5.6-sol / household.annual_discount_factor / Annual discount factor | total_sd | 0.12787781033079976 | 0.12788256087129315 |
| 3 | gpt-5.6-sol / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | between_run_sd | 0.07999999999999997 | 0.06091638166827996 |
| 3 | gpt-5.6-sol / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | total_sd | 0.7331468512893958 | 0.7313105435525398 |
| 4 | gpt-5.6-sol / household.relative_risk_aversion.crra / Coefficient of relative risk aversion | between_run_sd | 0.0 | 0.16224124698183934 |
| 4 | gpt-5.6-sol / household.relative_risk_aversion.crra / Coefficient of relative risk aversion | total_sd | 6.865194775500223 | 6.867111585505057 |
| 5 | gpt-5.6-sol / labor_supply.extensive_margin.single_mothers / Employment participation elasticity of single mothers | between_run_sd | 0.04714045207910317 | 0.049947572513586704 |
| 5 | gpt-5.6-sol / labor_supply.extensive_margin.single_mothers / Employment participation elasticity of single mothers | total_sd | 0.6935475310155591 | 0.6937439841581011 |
| 6 | gpt-5.6-sol / labor_supply.frisch_elasticity.prime_age / Frisch elasticity of labor supply | between_run_sd | 0.046427960923947055 | 0.045629199958895736 |
| 6 | gpt-5.6-sol / labor_supply.frisch_elasticity.prime_age / Frisch elasticity of labor supply | total_sd | 1.2866726106296211 | 1.2866440359624638 |
| 7 | gpt-5.6-sol / labor_supply.income_elasticity.prime_age / Income elasticity of labor supply | between_run_sd | 0.017435595774162694 | 0.01785353995399481 |
| 7 | gpt-5.6-sol / labor_supply.income_elasticity.prime_age / Income elasticity of labor supply | total_sd | 0.30660213995049385 | 0.306626191169494 |
| 8 | gpt-5.6-sol / labor_supply.marshallian_wage_elasticity.prime_age / Uncompensated wage elasticity of labor supply | between_run_sd | 0.010198039027185569 | 0.008929290129804389 |
| 8 | gpt-5.6-sol / labor_supply.marshallian_wage_elasticity.prime_age / Uncompensated wage elasticity of labor supply | total_sd | 0.596318118633931 | 0.5962977702736556 |
| 9 | gpt-5.6-sol / labor_supply.policy_response.substitution_elasticity.all / Substitution elasticity of labor supply in a tax-benefit simulation | between_run_sd | 0.024944382578492935 | 0.022930002180549386 |
| 9 | gpt-5.6-sol / labor_supply.policy_response.substitution_elasticity.all / Substitution elasticity of labor supply in a tax-benefit simulation | total_sd | 0.651969748360902 | 0.6518957858090169 |
| 10 | gpt-5.6-sol / labor_supply.policy_response.substitution_elasticity.primary.decile_1 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 1 | between_run_sd | 0.043122564343456606 | 0.040535875742633475 |
| 10 | gpt-5.6-sol / labor_supply.policy_response.substitution_elasticity.primary.decile_1 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 1 | total_sd | 0.6329366619619656 | 0.6327656910122594 |
| 11 | gpt-5.6-sol / labor_supply.policy_response.substitution_elasticity.primary.decile_10 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 10 | between_run_sd | 0.05384752135015646 | 0.05235149366435393 |
| 11 | gpt-5.6-sol / labor_supply.policy_response.substitution_elasticity.primary.decile_10 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 10 | total_sd | 0.6319149380168891 | 0.6317892150252505 |
| 12 | gpt-5.6-sol / labor_supply.policy_response.substitution_elasticity.primary.decile_2 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 2 | between_run_sd | 0.04784233364802442 | 0.04279971443310756 |
| 12 | gpt-5.6-sol / labor_supply.policy_response.substitution_elasticity.primary.decile_2 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 2 | total_sd | 0.628991454631937 | 0.6286280113601896 |
| 13 | gpt-5.6-sol / labor_supply.policy_response.substitution_elasticity.primary.decile_3 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 3 | between_run_sd | 0.040463975747982724 | 0.034954518067530756 |
| 13 | gpt-5.6-sol / labor_supply.policy_response.substitution_elasticity.primary.decile_3 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 3 | total_sd | 0.6294598058829668 | 0.6291296624879662 |
| 14 | gpt-5.6-sol / labor_supply.policy_response.substitution_elasticity.primary.decile_4 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 4 | between_run_sd | 0.042656248728123715 | 0.037165044807662424 |
| 14 | gpt-5.6-sol / labor_supply.policy_response.substitution_elasticity.primary.decile_4 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 4 | total_sd | 0.6283747742744329 | 0.6280259086569951 |
| 15 | gpt-5.6-sol / labor_supply.policy_response.substitution_elasticity.primary.decile_5 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 5 | between_run_sd | 0.04346134936801766 | 0.03960023849535365 |
| 15 | gpt-5.6-sol / labor_supply.policy_response.substitution_elasticity.primary.decile_5 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 5 | total_sd | 0.6288475338532651 | 0.628592483914128 |
| 16 | gpt-5.6-sol / labor_supply.policy_response.substitution_elasticity.primary.decile_6 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 6 | between_run_sd | 0.04134408462323641 | 0.04002910052560373 |
| 16 | gpt-5.6-sol / labor_supply.policy_response.substitution_elasticity.primary.decile_6 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 6 | total_sd | 0.6284759873429268 | 0.6283908514787769 |
| 17 | gpt-5.6-sol / labor_supply.policy_response.substitution_elasticity.primary.decile_7 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 7 | between_run_sd | 0.037676989735852776 | 0.034314938437945655 |
| 17 | gpt-5.6-sol / labor_supply.policy_response.substitution_elasticity.primary.decile_7 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 7 | total_sd | 0.6285382800151829 | 0.6283457081009537 |
| 18 | gpt-5.6-sol / labor_supply.policy_response.substitution_elasticity.primary.decile_8 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 8 | between_run_sd | 0.045587522659410025 | 0.04397844800454979 |
| 18 | gpt-5.6-sol / labor_supply.policy_response.substitution_elasticity.primary.decile_8 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 8 | total_sd | 0.6325727505372186 | 0.6324588258447256 |
| 19 | gpt-5.6-sol / labor_supply.policy_response.substitution_elasticity.primary.decile_9 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 9 | between_run_sd | 0.04644710252893428 | 0.041670419830965096 |
| 19 | gpt-5.6-sol / labor_supply.policy_response.substitution_elasticity.primary.decile_9 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 9 | total_sd | 0.6280089845871811 | 0.627673780938616 |
| 20 | gpt-5.6-sol / labor_supply.policy_response.substitution_elasticity.secondary / Secondary-earner substitution elasticity in a tax-benefit simulation | between_run_sd | 0.08420609637470833 | 0.08084201671573185 |
| 20 | gpt-5.6-sol / labor_supply.policy_response.substitution_elasticity.secondary / Secondary-earner substitution elasticity in a tax-benefit simulation | total_sd | 0.6416461133071892 | 0.6412133028269316 |
| 21 | gpt-5.6-sol / macro.tfp_persistence.ar1 / TFP persistence | between_run_sd | 0.0040000000000000036 | 0.003733705338608773 |
| 21 | gpt-5.6-sol / macro.tfp_persistence.ar1 / TFP persistence | total_sd | 0.13214555710991152 | 0.13213776454687148 |
| 22 | gpt-5.6-sol / production.capital_labor_substitution / Elasticity of substitution between capital and labor | between_run_sd | 0.03590109871423002 | 0.03325657829663177 |
| 22 | gpt-5.6-sol / production.capital_labor_substitution / Elasticity of substitution between capital and labor | total_sd | 1.2553423614474437 | 1.2552695151064395 |
| 23 | gpt-5.6-sol / production.capital_share / Capital share in production | between_run_sd | 0.009568466729604867 | 0.010079875440147502 |
| 23 | gpt-5.6-sol / production.capital_share / Capital share in production | total_sd | 0.11612261838246672 | 0.11616587637225198 |
| 24 | gpt-5.6-sol / tax.capital_gains_realizations.elasticity / Capital gains realizations elasticity | between_run_sd | 0.1206464071390257 | 0.10499399982856163 |
| 24 | gpt-5.6-sol / tax.capital_gains_realizations.elasticity / Capital gains realizations elasticity | total_sd | 1.3278821708729365 | 1.3265516364494323 |
| 25 | gpt-5.6-sol / tax.capital_gains_realizations.elasticity.net_of_tax_rate / Capital gains realizations elasticity (net-of-tax-rate convention) | between_run_sd | 0.29314387821227533 | 0.3482528415773038 |
| 25 | gpt-5.6-sol / tax.capital_gains_realizations.elasticity.net_of_tax_rate / Capital gains realizations elasticity (net-of-tax-rate convention) | total_sd | 1.4867396866409848 | 1.4985798624586768 |
| 26 | gpt-5.6-sol / tax.elasticity_of_taxable_income.top_earners / Elasticity of taxable income | between_run_sd | 0.03559026084010437 | 0.03534007011248782 |
| 26 | gpt-5.6-sol / tax.elasticity_of_taxable_income.top_earners / Elasticity of taxable income | total_sd | 0.687001125059729 | 0.6869882093036402 |
| 27 | gpt-5.6-sol / trade.armington_elasticity.import_domestic / Armington elasticity | between_run_sd | 0.1699673171197595 | 0.22536427302382142 |
| 27 | gpt-5.6-sol / trade.armington_elasticity.import_domestic / Armington elasticity | total_sd | 2.773673982484443 | 2.777619039353269 |

## `results/gpt-5.6-sol-ies-clarify-batch15/summary.csv` (2 cells)

| line | row | column | old | new |
|---|---|---|---|---|
| 2 | gpt-5.6-sol / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | between_run_sd | 0.0 | 0.013985607681549708 |
| 2 | gpt-5.6-sol / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | total_sd | 0.6985400698361309 | 0.6986800601054025 |

## `results/gpt-5.6-terra-armington-clarify-batch15/summary.csv` (2 cells)

| line | row | column | old | new |
|---|---|---|---|---|
| 2 | gpt-5.6-terra / trade.armington_elasticity.import_domestic / Armington elasticity | between_run_sd | 0.2 | 0.2624412103479346 |
| 2 | gpt-5.6-terra / trade.armington_elasticity.import_domestic / Armington elasticity | total_sd | 2.612505768202032 | 2.6180263134234876 |

## `results/gpt-5.6-terra-elasticities-batch15/summary.csv` (52 cells)

| line | row | column | old | new |
|---|---|---|---|---|
| 2 | gpt-5.6-terra / household.annual_discount_factor / Annual discount factor | between_run_sd | 0.013266499161421611 | 0.008512490822315174 |
| 2 | gpt-5.6-terra / household.annual_discount_factor / Annual discount factor | total_sd | 0.1273684820052957 | 0.1269613827442555 |
| 3 | gpt-5.6-terra / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | between_run_sd | 0.0 | 0.011251543104046758 |
| 3 | gpt-5.6-terra / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | total_sd | 0.6543575623804194 | 0.6544542892109935 |
| 4 | gpt-5.6-terra / household.relative_risk_aversion.crra / Coefficient of relative risk aversion | between_run_sd | 0.0 | 0.31856448850010455 |
| 4 | gpt-5.6-terra / household.relative_risk_aversion.crra / Coefficient of relative risk aversion | total_sd | 6.587320258985778 | 6.595018690479792 |
| 5 | gpt-5.6-terra / labor_supply.extensive_margin.single_mothers / Employment participation elasticity of single mothers | between_run_sd | 0.09451631252505216 | 0.08721103077529177 |
| 5 | gpt-5.6-terra / labor_supply.extensive_margin.single_mothers / Employment participation elasticity of single mothers | total_sd | 0.7265537469604174 | 0.7256395646447193 |
| 6 | gpt-5.6-terra / labor_supply.frisch_elasticity.prime_age / Frisch elasticity of labor supply | between_run_sd | 0.04346134936801766 | 0.04861169840915067 |
| 6 | gpt-5.6-terra / labor_supply.frisch_elasticity.prime_age / Frisch elasticity of labor supply | total_sd | 1.2776002488389446 | 1.277785820928792 |
| 7 | gpt-5.6-terra / labor_supply.income_elasticity.prime_age / Income elasticity of labor supply | between_run_sd | 0.014605934866804431 | 0.012866661269428918 |
| 7 | gpt-5.6-terra / labor_supply.income_elasticity.prime_age / Income elasticity of labor supply | total_sd | 0.30498341769585513 | 0.3049050716343258 |
| 8 | gpt-5.6-terra / labor_supply.marshallian_wage_elasticity.prime_age / Uncompensated wage elasticity of labor supply | between_run_sd | 0.013564659966250532 | 0.01869621173749733 |
| 8 | gpt-5.6-terra / labor_supply.marshallian_wage_elasticity.prime_age / Uncompensated wage elasticity of labor supply | total_sd | 0.6106236179331568 | 0.6107591596620645 |
| 9 | gpt-5.6-terra / labor_supply.policy_response.substitution_elasticity.all / Substitution elasticity of labor supply in a tax-benefit simulation | between_run_sd | 0.07788880963698615 | 0.06644421218837149 |
| 9 | gpt-5.6-terra / labor_supply.policy_response.substitution_elasticity.all / Substitution elasticity of labor supply in a tax-benefit simulation | total_sd | 0.6467672816915422 | 0.6454890265010966 |
| 10 | gpt-5.6-terra / labor_supply.policy_response.substitution_elasticity.primary.decile_1 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 1 | between_run_sd | 0.0771722460186015 | 0.07724005869150195 |
| 10 | gpt-5.6-terra / labor_supply.policy_response.substitution_elasticity.primary.decile_1 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 1 | total_sd | 0.6452011604918269 | 0.6452092750504376 |
| 11 | gpt-5.6-terra / labor_supply.policy_response.substitution_elasticity.primary.decile_10 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 10 | between_run_sd | 0.06377042156569664 | 0.06206494358510464 |
| 11 | gpt-5.6-terra / labor_supply.policy_response.substitution_elasticity.primary.decile_10 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 10 | total_sd | 0.6365894608510784 | 0.6364208766392113 |
| 12 | gpt-5.6-terra / labor_supply.policy_response.substitution_elasticity.primary.decile_2 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 2 | between_run_sd | 0.047842333648024406 | 0.04094313129207387 |
| 12 | gpt-5.6-terra / labor_supply.policy_response.substitution_elasticity.primary.decile_2 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 2 | total_sd | 0.6368005836471362 | 0.6363194437108176 |
| 13 | gpt-5.6-terra / labor_supply.policy_response.substitution_elasticity.primary.decile_3 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 3 | between_run_sd | 0.05374838498865699 | 0.05312667252269177 |
| 13 | gpt-5.6-terra / labor_supply.policy_response.substitution_elasticity.primary.decile_3 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 3 | total_sd | 0.6336021348431347 | 0.633549697910292 |
| 14 | gpt-5.6-terra / labor_supply.policy_response.substitution_elasticity.primary.decile_4 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 4 | between_run_sd | 0.04898979485566356 | 0.04468409485861086 |
| 14 | gpt-5.6-terra / labor_supply.policy_response.substitution_elasticity.primary.decile_4 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 4 | total_sd | 0.6353239735669424 | 0.6350064721892386 |
| 15 | gpt-5.6-terra / labor_supply.policy_response.substitution_elasticity.primary.decile_5 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 5 | between_run_sd | 0.04163331998932265 | 0.03858420085417807 |
| 15 | gpt-5.6-terra / labor_supply.policy_response.substitution_elasticity.primary.decile_5 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 5 | total_sd | 0.6291127372030478 | 0.6289183121307037 |
| 16 | gpt-5.6-terra / labor_supply.policy_response.substitution_elasticity.primary.decile_6 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 6 | between_run_sd | 0.03858612300930075 | 0.03176888764533976 |
| 16 | gpt-5.6-terra / labor_supply.policy_response.substitution_elasticity.primary.decile_6 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 6 | total_sd | 0.6290175761543639 | 0.6286362099373886 |
| 17 | gpt-5.6-terra / labor_supply.policy_response.substitution_elasticity.primary.decile_7 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 7 | between_run_sd | 0.03399346342395189 | 0.034122898795709344 |
| 17 | gpt-5.6-terra / labor_supply.policy_response.substitution_elasticity.primary.decile_7 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 7 | total_sd | 0.6292006745775858 | 0.6292076807823912 |
| 18 | gpt-5.6-terra / labor_supply.policy_response.substitution_elasticity.primary.decile_8 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 8 | between_run_sd | 0.02211083193570266 | 0.017084512154450157 |
| 18 | gpt-5.6-terra / labor_supply.policy_response.substitution_elasticity.primary.decile_8 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 8 | total_sd | 0.6271670719282949 | 0.6270099901738231 |
| 19 | gpt-5.6-terra / labor_supply.policy_response.substitution_elasticity.primary.decile_9 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 9 | between_run_sd | 0.037273761995984964 | 0.034042400032900134 |
| 19 | gpt-5.6-terra / labor_supply.policy_response.substitution_elasticity.primary.decile_9 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 9 | total_sd | 0.6308219076464187 | 0.630639223988909 |
| 20 | gpt-5.6-terra / labor_supply.policy_response.substitution_elasticity.secondary / Secondary-earner substitution elasticity in a tax-benefit simulation | between_run_sd | 0.08944271909999159 | 0.08602284903184476 |
| 20 | gpt-5.6-terra / labor_supply.policy_response.substitution_elasticity.secondary / Secondary-earner substitution elasticity in a tax-benefit simulation | total_sd | 0.6322513235344875 | 0.6317765955356899 |
| 21 | gpt-5.6-terra / macro.tfp_persistence.ar1 / TFP persistence | between_run_sd | 0.007118052168020881 | 0.00906793802360822 |
| 21 | gpt-5.6-terra / macro.tfp_persistence.ar1 / TFP persistence | total_sd | 0.1305599253110319 | 0.13068073664682012 |
| 22 | gpt-5.6-terra / production.capital_labor_substitution / Elasticity of substitution between capital and labor | between_run_sd | 0.074535599249993 | 0.06338999658200545 |
| 22 | gpt-5.6-terra / production.capital_labor_substitution / Elasticity of substitution between capital and labor | total_sd | 1.2396652914082182 | 1.2390451044386293 |
| 23 | gpt-5.6-terra / production.capital_share / Capital share in production | between_run_sd | 0.0 | 0.002785179028756005 |
| 23 | gpt-5.6-terra / production.capital_share / Capital share in production | total_sd | 0.1147798012621462 | 0.11481358804601484 |
| 24 | gpt-5.6-terra / tax.capital_gains_realizations.elasticity / Capital gains realizations elasticity | between_run_sd | 0.14375287436739792 | 0.1298989564580443 |
| 24 | gpt-5.6-terra / tax.capital_gains_realizations.elasticity / Capital gains realizations elasticity | total_sd | 1.3404941190968849 | 1.339079285678534 |
| 25 | gpt-5.6-terra / tax.capital_gains_realizations.elasticity.net_of_tax_rate / Capital gains realizations elasticity (net-of-tax-rate convention) | between_run_sd | 0.10677078252031309 | 0.10860945579869595 |
| 25 | gpt-5.6-terra / tax.capital_gains_realizations.elasticity.net_of_tax_rate / Capital gains realizations elasticity (net-of-tax-rate convention) | total_sd | 1.362670185599664 | 1.3628154859008286 |
| 26 | gpt-5.6-terra / tax.elasticity_of_taxable_income.top_earners / Elasticity of taxable income | between_run_sd | 0.04163331998932265 | 0.039430318284284734 |
| 26 | gpt-5.6-terra / tax.elasticity_of_taxable_income.top_earners / Elasticity of taxable income | total_sd | 0.6788512560036828 | 0.6787197097804398 |
| 27 | gpt-5.6-terra / trade.armington_elasticity.import_domestic / Armington elasticity | between_run_sd | 0.0 | 0.023795424396766428 |
| 27 | gpt-5.6-terra / trade.armington_elasticity.import_domestic / Armington elasticity | total_sd | 2.6645713382581198 | 2.6646775862923624 |

## `results/gpt-5.6-terra-ies-clarify-batch15/summary.csv` (2 cells)

| line | row | column | old | new |
|---|---|---|---|---|
| 2 | gpt-5.6-terra / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | between_run_sd | 0.0 | 0.006642665127793207 |
| 2 | gpt-5.6-terra / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | total_sd | 0.6504464545816033 | 0.650480372707569 |

## `results/grok-4.1-fast-armington-clarify-batch15/summary.csv` (2 cells)

| line | row | column | old | new |
|---|---|---|---|---|
| 2 | grok-4.1-fast / trade.armington_elasticity.import_domestic / Armington elasticity | between_run_sd | 0.0 | 0.020579115627256738 |
| 2 | grok-4.1-fast / trade.armington_elasticity.import_domestic / Armington elasticity | total_sd | 2.5004276578661946 | 2.5005123419455906 |

## `results/grok-4.1-fast-elasticities-batch15/summary.csv` (44 cells)

| line | row | column | old | new |
|---|---|---|---|---|
| 2 | grok-4.1-fast / household.annual_discount_factor / Annual discount factor | between_run_sd | 0.0 | 0.0006123724356957815 |
| 2 | grok-4.1-fast / household.annual_discount_factor / Annual discount factor | total_sd | 0.1247449063756379 | 0.12474640943396594 |
| 3 | grok-4.1-fast / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | between_run_sd | 0.0 | 0.047360467574643884 |
| 3 | grok-4.1-fast / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | total_sd | 0.7607549475867887 | 0.7622277246116588 |
| 4 | grok-4.1-fast / household.relative_risk_aversion.crra / Coefficient of relative risk aversion | between_run_sd | 0.0 | 0.06236095644623225 |
| 4 | grok-4.1-fast / household.relative_risk_aversion.crra / Coefficient of relative risk aversion | total_sd | 6.67918486169283 | 6.6794759753707895 |
| 5 | grok-4.1-fast / labor_supply.extensive_margin.single_mothers / Employment participation elasticity of single mothers | between_run_sd | 0.0 | 0.013587678241701179 |
| 5 | grok-4.1-fast / labor_supply.extensive_margin.single_mothers / Employment participation elasticity of single mothers | total_sd | 0.7429422083850129 | 0.7430664505950999 |
| 6 | grok-4.1-fast / labor_supply.frisch_elasticity.prime_age / Frisch elasticity of labor supply | between_run_sd | 0.0 | 0.029933259094191613 |
| 6 | grok-4.1-fast / labor_supply.frisch_elasticity.prime_age / Frisch elasticity of labor supply | total_sd | 1.3195782154410804 | 1.3199176742004277 |
| 7 | grok-4.1-fast / labor_supply.income_elasticity.prime_age / Income elasticity of labor supply | between_run_sd | 0.04 | 0.040497825730388154 |
| 7 | grok-4.1-fast / labor_supply.income_elasticity.prime_age / Income elasticity of labor supply | total_sd | 0.3612808099126096 | 0.361336266516385 |
| 8 | grok-4.1-fast / labor_supply.marshallian_wage_elasticity.prime_age / Uncompensated wage elasticity of labor supply | between_run_sd | 0.0339934634239519 | 0.04097036191633601 |
| 8 | grok-4.1-fast / labor_supply.marshallian_wage_elasticity.prime_age / Uncompensated wage elasticity of labor supply | total_sd | 0.6312354167732424 | 0.63164955979474 |
| 9 | grok-4.1-fast / labor_supply.policy_response.substitution_elasticity.all / Substitution elasticity of labor supply in a tax-benefit simulation | between_run_sd | 0.0 | 0.026941294203013586 |
| 9 | grok-4.1-fast / labor_supply.policy_response.substitution_elasticity.all / Substitution elasticity of labor supply in a tax-benefit simulation | total_sd | 0.686186017053685 | 0.6867147030123452 |
| 10 | grok-4.1-fast / labor_supply.policy_response.substitution_elasticity.primary.decile_1 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 1 | between_run_sd | 0.012472191289246471 | 0.027532384971560703 |
| 10 | grok-4.1-fast / labor_supply.policy_response.substitution_elasticity.primary.decile_1 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 1 | total_sd | 0.6589299648757151 | 0.6593869692963137 |
| 12 | grok-4.1-fast / labor_supply.policy_response.substitution_elasticity.primary.decile_2 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 2 | between_run_sd | 0.024944382578492935 | 0.03710476908550825 |
| 12 | grok-4.1-fast / labor_supply.policy_response.substitution_elasticity.primary.decile_2 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 2 | total_sd | 0.7060009885498273 | 0.7065351636684476 |
| 13 | grok-4.1-fast / labor_supply.policy_response.substitution_elasticity.primary.decile_3 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 3 | between_run_sd | 0.0 | 0.024246420125224443 |
| 13 | grok-4.1-fast / labor_supply.policy_response.substitution_elasticity.primary.decile_3 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 3 | total_sd | 0.700638498482317 | 0.701057910906399 |
| 17 | grok-4.1-fast / labor_supply.policy_response.substitution_elasticity.primary.decile_7 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 7 | between_run_sd | 0.0 | 0.022488268546560494 |
| 17 | grok-4.1-fast / labor_supply.policy_response.substitution_elasticity.primary.decile_7 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 7 | total_sd | 0.7006446436437423 | 0.7010054485443669 |
| 18 | grok-4.1-fast / labor_supply.policy_response.substitution_elasticity.primary.decile_8 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 8 | between_run_sd | 0.04714045207910318 | 0.059369721987633475 |
| 18 | grok-4.1-fast / labor_supply.policy_response.substitution_elasticity.primary.decile_8 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 8 | total_sd | 0.7206867143757943 | 0.7215898294352856 |
| 19 | grok-4.1-fast / labor_supply.policy_response.substitution_elasticity.primary.decile_9 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 9 | between_run_sd | 0.2135415650406262 | 0.20584908846585215 |
| 19 | grok-4.1-fast / labor_supply.policy_response.substitution_elasticity.primary.decile_9 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 9 | total_sd | 0.7600210386342385 | 0.7578956566631643 |
| 20 | grok-4.1-fast / labor_supply.policy_response.substitution_elasticity.secondary / Secondary-earner substitution elasticity in a tax-benefit simulation | between_run_sd | 0.0 | 0.0059895742753554556 |
| 20 | grok-4.1-fast / labor_supply.policy_response.substitution_elasticity.secondary / Secondary-earner substitution elasticity in a tax-benefit simulation | total_sd | 0.709338233261585 | 0.7093635204651185 |
| 21 | grok-4.1-fast / macro.tfp_persistence.ar1 / TFP persistence | between_run_sd | 0.024944382578492935 | 0.02722022328261756 |
| 21 | grok-4.1-fast / macro.tfp_persistence.ar1 / TFP persistence | total_sd | 0.13108172811053584 | 0.13153378949067718 |
| 22 | grok-4.1-fast / production.capital_labor_substitution / Elasticity of substitution between capital and labor | between_run_sd | 0.040000000000000036 | 0.02873804099099307 |
| 22 | grok-4.1-fast / production.capital_labor_substitution / Elasticity of substitution between capital and labor | total_sd | 1.248664536615019 | 1.2483545169542185 |
| 23 | grok-4.1-fast / production.capital_share / Capital share in production | between_run_sd | 0.01019803902718558 | 0.009115676363032826 |
| 23 | grok-4.1-fast / production.capital_share / Capital share in production | total_sd | 0.11279186214734939 | 0.1126991558185873 |
| 24 | grok-4.1-fast / tax.capital_gains_realizations.elasticity / Capital gains realizations elasticity | between_run_sd | 0.1699673171197595 | 0.15649245633221073 |
| 24 | grok-4.1-fast / tax.capital_gains_realizations.elasticity / Capital gains realizations elasticity | total_sd | 1.4173425348556752 | 1.4157898364909642 |
| 25 | grok-4.1-fast / tax.capital_gains_realizations.elasticity.net_of_tax_rate / Capital gains realizations elasticity (net-of-tax-rate convention) | between_run_sd | 0.7009200303093706 | 0.7616589350446388 |
| 25 | grok-4.1-fast / tax.capital_gains_realizations.elasticity.net_of_tax_rate / Capital gains realizations elasticity (net-of-tax-rate convention) | total_sd | 1.8270195826962434 | 1.8511715209563915 |
| 26 | grok-4.1-fast / tax.elasticity_of_taxable_income.top_earners / Elasticity of taxable income | between_run_sd | 0.0 | 0.020933757957476776 |
| 26 | grok-4.1-fast / tax.elasticity_of_taxable_income.top_earners / Elasticity of taxable income | total_sd | 0.702247483283335 | 0.7025594280913181 |
| 27 | grok-4.1-fast / trade.armington_elasticity.import_domestic / Armington elasticity | between_run_sd | 0.0 | 0.0280446073247604 |
| 27 | grok-4.1-fast / trade.armington_elasticity.import_domestic / Armington elasticity | total_sd | 2.5028337828238705 | 2.502990899792575 |

## `results/grok-4.1-fast-ies-clarify-batch15/summary.csv` (2 cells)

| line | row | column | old | new |
|---|---|---|---|---|
| 2 | grok-4.1-fast / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | between_run_sd | 0.0 | 0.019849433241279257 |
| 2 | grok-4.1-fast / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | total_sd | 0.801125315311739 | 0.801371181683827 |

## `results/grok-4.20-armington-clarify-batch15/summary.csv` (2 cells)

| line | row | column | old | new |
|---|---|---|---|---|
| 2 | grok-4.20 / trade.armington_elasticity.import_domestic / Armington elasticity | between_run_sd | 0.46427960923947065 | 0.4520448601140772 |
| 2 | grok-4.20 / trade.armington_elasticity.import_domestic / Armington elasticity | total_sd | 2.897316670453696 | 2.8953813028492275 |

## `results/grok-4.20-elasticities-batch15/summary.csv` (52 cells)

| line | row | column | old | new |
|---|---|---|---|---|
| 2 | grok-4.20 / household.annual_discount_factor / Annual discount factor | between_run_sd | 0.0024944382578492965 | 0.002207782950281922 |
| 2 | grok-4.20 / household.annual_discount_factor / Annual discount factor | total_sd | 0.1269003286157202 | 0.12689501757796132 |
| 3 | grok-4.20 / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | between_run_sd | 0.28674417556808757 | 0.26640424587874384 |
| 3 | grok-4.20 / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | total_sd | 1.0558114803052885 | 1.050469838664797 |
| 4 | grok-4.20 / household.relative_risk_aversion.crra / Coefficient of relative risk aversion | between_run_sd | 0.0 | 0.2156128217172829 |
| 4 | grok-4.20 / household.relative_risk_aversion.crra / Coefficient of relative risk aversion | total_sd | 6.853872334105898 | 6.857262927809543 |
| 5 | grok-4.20 / labor_supply.extensive_margin.single_mothers / Employment participation elasticity of single mothers | between_run_sd | 0.06749485577105527 | 0.07557253689888498 |
| 5 | grok-4.20 / labor_supply.extensive_margin.single_mothers / Employment participation elasticity of single mothers | total_sd | 0.7088792504134019 | 0.7096939089807975 |
| 6 | grok-4.20 / labor_supply.frisch_elasticity.prime_age / Frisch elasticity of labor supply | between_run_sd | 0.05962847939999439 | 0.09226418891181756 |
| 6 | grok-4.20 / labor_supply.frisch_elasticity.prime_age / Frisch elasticity of labor supply | total_sd | 1.3154144625681037 | 1.3172973594953166 |
| 7 | grok-4.20 / labor_supply.income_elasticity.prime_age / Income elasticity of labor supply | between_run_sd | 0.024944382578492942 | 0.02064303756717989 |
| 7 | grok-4.20 / labor_supply.income_elasticity.prime_age / Income elasticity of labor supply | total_sd | 0.3299922515925353 | 0.3296950088928992 |
| 8 | grok-4.20 / labor_supply.marshallian_wage_elasticity.prime_age / Uncompensated wage elasticity of labor supply | between_run_sd | 0.041633319989322654 | 0.0441079798776694 |
| 8 | grok-4.20 / labor_supply.marshallian_wage_elasticity.prime_age / Uncompensated wage elasticity of labor supply | total_sd | 0.6171354355676988 | 0.617307319241307 |
| 9 | grok-4.20 / labor_supply.policy_response.substitution_elasticity.all / Substitution elasticity of labor supply in a tax-benefit simulation | between_run_sd | 0.07498147919467996 | 0.08702639446359554 |
| 9 | grok-4.20 / labor_supply.policy_response.substitution_elasticity.all / Substitution elasticity of labor supply in a tax-benefit simulation | total_sd | 0.6529622330409146 | 0.6544547722256205 |
| 10 | grok-4.20 / labor_supply.policy_response.substitution_elasticity.primary.decile_1 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 1 | between_run_sd | 0.012472191289246468 | 0.011228114514715098 |
| 10 | grok-4.20 / labor_supply.policy_response.substitution_elasticity.primary.decile_1 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 1 | total_sd | 0.6409903210397694 | 0.6409673210598702 |
| 11 | grok-4.20 / labor_supply.policy_response.substitution_elasticity.primary.decile_10 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 10 | between_run_sd | 0.05962847939999439 | 0.05716796888701459 |
| 11 | grok-4.20 / labor_supply.policy_response.substitution_elasticity.primary.decile_10 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 10 | total_sd | 0.6517019417136436 | 0.6514814210278329 |
| 12 | grok-4.20 / labor_supply.policy_response.substitution_elasticity.primary.decile_2 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 2 | between_run_sd | 0.019999999999999993 | 0.020303297488065544 |
| 12 | grok-4.20 / labor_supply.policy_response.substitution_elasticity.primary.decile_2 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 2 | total_sd | 0.6383055748968862 | 0.6383151500891494 |
| 13 | grok-4.20 / labor_supply.policy_response.substitution_elasticity.primary.decile_3 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 3 | between_run_sd | 0.018257418583505533 | 0.021383690565994967 |
| 13 | grok-4.20 / labor_supply.policy_response.substitution_elasticity.primary.decile_3 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 3 | total_sd | 0.6369429243573469 | 0.6370402010688005 |
| 14 | grok-4.20 / labor_supply.policy_response.substitution_elasticity.primary.decile_4 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 4 | between_run_sd | 0.018257418583505533 | 0.022294020124987178 |
| 14 | grok-4.20 / labor_supply.policy_response.substitution_elasticity.primary.decile_4 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 4 | total_sd | 0.6363313678597199 | 0.6364599749569663 |
| 15 | grok-4.20 / labor_supply.policy_response.substitution_elasticity.primary.decile_5 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 5 | between_run_sd | 0.02867441755680875 | 0.03336985499252615 |
| 15 | grok-4.20 / labor_supply.policy_response.substitution_elasticity.primary.decile_5 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 5 | total_sd | 0.6377338361991884 | 0.6379622017277617 |
| 16 | grok-4.20 / labor_supply.policy_response.substitution_elasticity.primary.decile_6 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 6 | between_run_sd | 0.027080128015453196 | 0.032226826299425346 |
| 16 | grok-4.20 / labor_supply.policy_response.substitution_elasticity.primary.decile_6 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 6 | total_sd | 0.6379491032467507 | 0.638188289874809 |
| 17 | grok-4.20 / labor_supply.policy_response.substitution_elasticity.primary.decile_7 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 7 | between_run_sd | 0.02211083193570266 | 0.02195143629823697 |
| 17 | grok-4.20 / labor_supply.policy_response.substitution_elasticity.primary.decile_7 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 7 | total_sd | 0.6363442988403892 | 0.6363387803154333 |
| 18 | grok-4.20 / labor_supply.policy_response.substitution_elasticity.primary.decile_8 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 8 | between_run_sd | 0.019999999999999993 | 0.026969035742660307 |
| 18 | grok-4.20 / labor_supply.policy_response.substitution_elasticity.primary.decile_8 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 8 | total_sd | 0.6395284330400538 | 0.6397842961151481 |
| 19 | grok-4.20 / labor_supply.policy_response.substitution_elasticity.primary.decile_9 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 9 | between_run_sd | 0.035901098714230015 | 0.04194508314451173 |
| 19 | grok-4.20 / labor_supply.policy_response.substitution_elasticity.primary.decile_9 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 9 | total_sd | 0.6426675138307003 | 0.6430334629274316 |
| 20 | grok-4.20 / labor_supply.policy_response.substitution_elasticity.secondary / Secondary-earner substitution elasticity in a tax-benefit simulation | between_run_sd | 0.03399346342395191 | 0.042165843206715736 |
| 20 | grok-4.20 / labor_supply.policy_response.substitution_elasticity.secondary / Secondary-earner substitution elasticity in a tax-benefit simulation | total_sd | 0.6580022638005638 | 0.6584750427650576 |
| 21 | grok-4.20 / macro.tfp_persistence.ar1 / TFP persistence | between_run_sd | 0.022110831935702634 | 0.019647289182536658 |
| 21 | grok-4.20 / macro.tfp_persistence.ar1 / TFP persistence | total_sd | 0.13492789869860947 | 0.1345461442426187 |
| 22 | grok-4.20 / production.capital_labor_substitution / Elasticity of substitution between capital and labor | between_run_sd | 0.0590668171555645 | 0.05489231883120502 |
| 22 | grok-4.20 / production.capital_labor_substitution / Elasticity of substitution between capital and labor | total_sd | 1.2464503349512166 | 1.2462594895437216 |
| 23 | grok-4.20 / production.capital_share / Capital share in production | between_run_sd | 0.0 | 0.0032772786813994943 |
| 23 | grok-4.20 / production.capital_share / Capital share in production | total_sd | 0.11065099035556197 | 0.11069951319776535 |
| 24 | grok-4.20 / tax.capital_gains_realizations.elasticity / Capital gains realizations elasticity | between_run_sd | 0.047842333648024406 | 0.06188272959576218 |
| 24 | grok-4.20 / tax.capital_gains_realizations.elasticity / Capital gains realizations elasticity | total_sd | 1.3605308910699365 | 1.3610969432369207 |
| 25 | grok-4.20 / tax.capital_gains_realizations.elasticity.net_of_tax_rate / Capital gains realizations elasticity (net-of-tax-rate convention) | between_run_sd | 0.07071067811865475 | 0.07594104072678141 |
| 25 | grok-4.20 / tax.capital_gains_realizations.elasticity.net_of_tax_rate / Capital gains realizations elasticity (net-of-tax-rate convention) | total_sd | 1.3586791226530763 | 1.3589613681043329 |
| 26 | grok-4.20 / tax.elasticity_of_taxable_income.top_earners / Elasticity of taxable income | between_run_sd | 0.0 | 0.018679682961858724 |
| 26 | grok-4.20 / tax.elasticity_of_taxable_income.top_earners / Elasticity of taxable income | total_sd | 0.6912781539374083 | 0.6915304886023946 |
| 27 | grok-4.20 / trade.armington_elasticity.import_domestic / Armington elasticity | between_run_sd | 0.18257418583505536 | 0.28672896609864873 |
| 27 | grok-4.20 / trade.armington_elasticity.import_domestic / Armington elasticity | total_sd | 3.0045039801382636 | 3.0126274800136397 |

## `results/grok-4.20-ies-clarify-batch15/summary.csv` (2 cells)

| line | row | column | old | new |
|---|---|---|---|---|
| 2 | grok-4.20 / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | between_run_sd | 0.23570226039551584 | 0.2695624798735083 |
| 2 | grok-4.20 / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | total_sd | 0.9420385143400455 | 0.9510756739082332 |

## `results/grok-4.3-armington-clarify-batch15/summary.csv` (2 cells)

| line | row | column | old | new |
|---|---|---|---|---|
| 2 | grok-4.3 / trade.armington_elasticity.import_domestic / Armington elasticity | between_run_sd | 0.6 | 0.5605404138468124 |
| 2 | grok-4.3 / trade.armington_elasticity.import_domestic / Armington elasticity | total_sd | 2.891301610001973 | 2.8833713870321245 |

## `results/grok-4.3-elasticities-batch15/summary.csv` (52 cells)

| line | row | column | old | new |
|---|---|---|---|---|
| 2 | grok-4.3 / household.annual_discount_factor / Annual discount factor | between_run_sd | 0.0 | 0.001731328969318086 |
| 2 | grok-4.3 / household.annual_discount_factor / Annual discount factor | total_sd | 0.12724993860509323 | 0.12726171606182277 |
| 3 | grok-4.3 / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | between_run_sd | 0.12229290885229427 | 0.1231198602988161 |
| 3 | grok-4.3 / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | total_sd | 0.8159024485534748 | 0.816026807157706 |
| 4 | grok-4.3 / household.relative_risk_aversion.crra / Coefficient of relative risk aversion | between_run_sd | 0.0 | 0.21479486337744055 |
| 4 | grok-4.3 / household.relative_risk_aversion.crra / Coefficient of relative risk aversion | total_sd | 6.412971371022605 | 6.416567512220914 |
| 5 | grok-4.3 / labor_supply.extensive_margin.single_mothers / Employment participation elasticity of single mothers | between_run_sd | 0.05734883511361751 | 0.0594710480448727 |
| 5 | grok-4.3 / labor_supply.extensive_margin.single_mothers / Employment participation elasticity of single mothers | total_sd | 0.679208587663286 | 0.6793910672228641 |
| 6 | grok-4.3 / labor_supply.frisch_elasticity.prime_age / Frisch elasticity of labor supply | between_run_sd | 0.05228129047119374 | 0.061925470437364356 |
| 6 | grok-4.3 / labor_supply.frisch_elasticity.prime_age / Frisch elasticity of labor supply | total_sd | 1.2782631037857581 | 1.2786938621325887 |
| 7 | grok-4.3 / labor_supply.income_elasticity.prime_age / Income elasticity of labor supply | between_run_sd | 0.02 | 0.022232758613261554 |
| 7 | grok-4.3 / labor_supply.income_elasticity.prime_age / Income elasticity of labor supply | total_sd | 0.3094400767694952 | 0.3095924040842518 |
| 8 | grok-4.3 / labor_supply.marshallian_wage_elasticity.prime_age / Uncompensated wage elasticity of labor supply | between_run_sd | 0.035377331097124265 | 0.03582444075705238 |
| 8 | grok-4.3 / labor_supply.marshallian_wage_elasticity.prime_age / Uncompensated wage elasticity of labor supply | total_sd | 0.6113574581753842 | 0.6113834939435858 |
| 9 | grok-4.3 / labor_supply.policy_response.substitution_elasticity.all / Substitution elasticity of labor supply in a tax-benefit simulation | between_run_sd | 0.029814239699997188 | 0.022384890737578614 |
| 9 | grok-4.3 / labor_supply.policy_response.substitution_elasticity.all / Substitution elasticity of labor supply in a tax-benefit simulation | total_sd | 0.6403154333347485 | 0.6400125378546198 |
| 10 | grok-4.3 / labor_supply.policy_response.substitution_elasticity.primary.decile_1 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 1 | between_run_sd | 0.023626726862225795 | 0.029396456702580103 |
| 10 | grok-4.3 / labor_supply.policy_response.substitution_elasticity.primary.decile_1 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 1 | total_sd | 0.6435430929627013 | 0.6437807405821057 |
| 11 | grok-4.3 / labor_supply.policy_response.substitution_elasticity.primary.decile_10 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 10 | between_run_sd | 0.012472191289246468 | 0.01909115560206407 |
| 11 | grok-4.3 / labor_supply.policy_response.substitution_elasticity.primary.decile_10 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 10 | total_sd | 0.6409678012367098 | 0.6411307502287571 |
| 12 | grok-4.3 / labor_supply.policy_response.substitution_elasticity.primary.decile_2 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 2 | between_run_sd | 0.0074833147735478825 | 0.015445387661046263 |
| 12 | grok-4.3 / labor_supply.policy_response.substitution_elasticity.primary.decile_2 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 2 | total_sd | 0.6392797466246247 | 0.6394225163727381 |
| 13 | grok-4.3 / labor_supply.policy_response.substitution_elasticity.primary.decile_3 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 3 | between_run_sd | 0.026195843605851334 | 0.029411373461450063 |
| 13 | grok-4.3 / labor_supply.policy_response.substitution_elasticity.primary.decile_3 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 3 | total_sd | 0.6388238889640173 | 0.6389638235282009 |
| 14 | grok-4.3 / labor_supply.policy_response.substitution_elasticity.primary.decile_4 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 4 | between_run_sd | 0.038620662287893966 | 0.03936862823224716 |
| 14 | grok-4.3 / labor_supply.policy_response.substitution_elasticity.primary.decile_4 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 4 | total_sd | 0.6413943090815682 | 0.641439781316653 |
| 15 | grok-4.3 / labor_supply.policy_response.substitution_elasticity.primary.decile_5 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 5 | between_run_sd | 0.0270801280154532 | 0.025254812522676844 |
| 15 | grok-4.3 / labor_supply.policy_response.substitution_elasticity.primary.decile_5 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 5 | total_sd | 0.6379393638461609 | 0.637864487306408 |
| 16 | grok-4.3 / labor_supply.policy_response.substitution_elasticity.primary.decile_6 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 6 | between_run_sd | 0.0074833147735478825 | 0.013450795102479594 |
| 16 | grok-4.3 / labor_supply.policy_response.substitution_elasticity.primary.decile_6 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 6 | total_sd | 0.6383199878935677 | 0.638417834050188 |
| 17 | grok-4.3 / labor_supply.policy_response.substitution_elasticity.primary.decile_7 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 7 | between_run_sd | 0.0339934634239519 | 0.034513266370419876 |
| 17 | grok-4.3 / labor_supply.policy_response.substitution_elasticity.primary.decile_7 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 7 | total_sd | 0.6406009580854528 | 0.6406287516963316 |
| 18 | grok-4.3 / labor_supply.policy_response.substitution_elasticity.primary.decile_8 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 8 | between_run_sd | 0.027373953556863746 | 0.028814030147366283 |
| 18 | grok-4.3 / labor_supply.policy_response.substitution_elasticity.primary.decile_8 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 8 | total_sd | 0.6402661881332378 | 0.6403293735779007 |
| 19 | grok-4.3 / labor_supply.policy_response.substitution_elasticity.primary.decile_9 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 9 | between_run_sd | 0.016996731711975945 | 0.021614359938604596 |
| 19 | grok-4.3 / labor_supply.policy_response.substitution_elasticity.primary.decile_9 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 9 | total_sd | 0.6387307563963603 | 0.6388703083046928 |
| 20 | grok-4.3 / labor_supply.policy_response.substitution_elasticity.secondary / Secondary-earner substitution elasticity in a tax-benefit simulation | between_run_sd | 0.0725718035235908 | 0.06498311746565838 |
| 20 | grok-4.3 / labor_supply.policy_response.substitution_elasticity.secondary / Secondary-earner substitution elasticity in a tax-benefit simulation | total_sd | 0.6513313022400948 | 0.6505294798598037 |
| 21 | grok-4.3 / macro.tfp_persistence.ar1 / TFP persistence | between_run_sd | 0.009568466729604848 | 0.0112833948792019 |
| 21 | grok-4.3 / macro.tfp_persistence.ar1 / TFP persistence | total_sd | 0.13256749853062275 | 0.13270230258405882 |
| 22 | grok-4.3 / production.capital_labor_substitution / Elasticity of substitution between capital and labor | between_run_sd | 0.04988876515698591 | 0.04911508593768993 |
| 22 | grok-4.3 / production.capital_labor_substitution / Elasticity of substitution between capital and labor | total_sd | 1.254486753173938 | 1.2544562234955299 |
| 23 | grok-4.3 / production.capital_share / Capital share in production | between_run_sd | 0.0 | 0.0034149995932975215 |
| 23 | grok-4.3 / production.capital_share / Capital share in production | total_sd | 0.1084202471865841 | 0.10847401634595366 |
| 24 | grok-4.3 / tax.capital_gains_realizations.elasticity / Capital gains realizations elasticity | between_run_sd | 0.10274023338281628 | 0.10332762080984069 |
| 24 | grok-4.3 / tax.capital_gains_realizations.elasticity / Capital gains realizations elasticity | total_sd | 1.399068005753195 | 1.3991112630484 |
| 25 | grok-4.3 / tax.capital_gains_realizations.elasticity.net_of_tax_rate / Capital gains realizations elasticity (net-of-tax-rate convention) | between_run_sd | 0.09568466729604884 | 0.09799326790935972 |
| 25 | grok-4.3 / tax.capital_gains_realizations.elasticity.net_of_tax_rate / Capital gains realizations elasticity (net-of-tax-rate convention) | total_sd | 1.3922089013506558 | 1.392369473236181 |
| 26 | grok-4.3 / tax.elasticity_of_taxable_income.top_earners / Elasticity of taxable income | between_run_sd | 0.046427960923947055 | 0.045368387182657885 |
| 26 | grok-4.3 / tax.elasticity_of_taxable_income.top_earners / Elasticity of taxable income | total_sd | 0.6812425106621969 | 0.6811711189806372 |
| 27 | grok-4.3 / trade.armington_elasticity.import_domestic / Armington elasticity | between_run_sd | 0.7517091636175965 | 0.7117258757571081 |
| 27 | grok-4.3 / trade.armington_elasticity.import_domestic / Armington elasticity | total_sd | 3.0877900673459 | 3.0783005953862848 |

## `results/grok-4.3-ies-clarify-batch15/summary.csv` (2 cells)

| line | row | column | old | new |
|---|---|---|---|---|
| 2 | grok-4.3 / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | between_run_sd | 0.11323525167642019 | 0.11784064098037936 |
| 2 | grok-4.3 / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | total_sd | 0.7949255511961132 | 0.7955946369784609 |

## `results/grok-4.5-armington-clarify-batch15/summary.csv` (2 cells)

| line | row | column | old | new |
|---|---|---|---|---|
| 2 | grok-4.5 / trade.armington_elasticity.import_domestic / Armington elasticity | between_run_sd | 0.47842333648024415 | 0.4455883750727795 |
| 2 | grok-4.5 / trade.armington_elasticity.import_domestic / Armington elasticity | total_sd | 2.743401274978846 | 2.7378660790233456 |

## `results/grok-4.5-elasticities-batch15/summary.csv` (52 cells)

| line | row | column | old | new |
|---|---|---|---|---|
| 2 | grok-4.5 / household.annual_discount_factor / Annual discount factor | between_run_sd | 0.0 | 0.001524430676970571 |
| 2 | grok-4.5 / household.annual_discount_factor / Annual discount factor | total_sd | 0.12619302207112898 | 0.12620222941110562 |
| 3 | grok-4.5 / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | between_run_sd | 0.1699673171197595 | 0.12152663174062805 |
| 3 | grok-4.5 / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | total_sd | 0.882326548897226 | 0.8742882660897504 |
| 4 | grok-4.5 / household.relative_risk_aversion.crra / Coefficient of relative risk aversion | between_run_sd | 0.0 | 0.3028407172095588 |
| 4 | grok-4.5 / household.relative_risk_aversion.crra / Coefficient of relative risk aversion | total_sd | 6.756828336332563 | 6.763611584550571 |
| 5 | grok-4.5 / labor_supply.extensive_margin.single_mothers / Employment participation elasticity of single mothers | between_run_sd | 0.0649786289653931 | 0.06801021165155191 |
| 5 | grok-4.5 / labor_supply.extensive_margin.single_mothers / Employment participation elasticity of single mothers | total_sd | 0.7003006050975538 | 0.7005883985384476 |
| 6 | grok-4.5 / labor_supply.frisch_elasticity.prime_age / Frisch elasticity of labor supply | between_run_sd | 0.03399346342395189 | 0.040679642738516424 |
| 6 | grok-4.5 / labor_supply.frisch_elasticity.prime_age / Frisch elasticity of labor supply | total_sd | 1.2806453451287754 | 1.2808402623972193 |
| 7 | grok-4.5 / labor_supply.income_elasticity.prime_age / Income elasticity of labor supply | between_run_sd | 0.0 | 0.006916887546673966 |
| 7 | grok-4.5 / labor_supply.income_elasticity.prime_age / Income elasticity of labor supply | total_sd | 0.3093853202543535 | 0.30946263057471446 |
| 8 | grok-4.5 / labor_supply.marshallian_wage_elasticity.prime_age / Uncompensated wage elasticity of labor supply | between_run_sd | 0.03270066258248193 | 0.02885018775213315 |
| 8 | grok-4.5 / labor_supply.marshallian_wage_elasticity.prime_age / Uncompensated wage elasticity of labor supply | total_sd | 0.601179188484321 | 0.6009820435476143 |
| 9 | grok-4.5 / labor_supply.policy_response.substitution_elasticity.all / Substitution elasticity of labor supply in a tax-benefit simulation | between_run_sd | 0.024944382578492935 | 0.023297508212014633 |
| 9 | grok-4.5 / labor_supply.policy_response.substitution_elasticity.all / Substitution elasticity of labor supply in a tax-benefit simulation | total_sd | 0.6392778238849766 | 0.639215681736437 |
| 10 | grok-4.5 / labor_supply.policy_response.substitution_elasticity.primary.decile_1 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 1 | between_run_sd | 0.03858612300930074 | 0.040274564622793316 |
| 10 | grok-4.5 / labor_supply.policy_response.substitution_elasticity.primary.decile_1 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 1 | total_sd | 0.642195186017806 | 0.6422988468081747 |
| 11 | grok-4.5 / labor_supply.policy_response.substitution_elasticity.primary.decile_10 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 10 | between_run_sd | 0.053124591501697425 | 0.05282813854587555 |
| 11 | grok-4.5 / labor_supply.policy_response.substitution_elasticity.primary.decile_10 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 10 | total_sd | 0.6408329638057019 | 0.6408084561707968 |
| 12 | grok-4.5 / labor_supply.policy_response.substitution_elasticity.primary.decile_2 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 2 | between_run_sd | 0.027080128015453196 | 0.03198995502063456 |
| 12 | grok-4.5 / labor_supply.policy_response.substitution_elasticity.primary.decile_2 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 2 | total_sd | 0.6393949939851995 | 0.639621749334888 |
| 13 | grok-4.5 / labor_supply.policy_response.substitution_elasticity.primary.decile_3 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 3 | between_run_sd | 0.025819888974716106 | 0.027117009831878994 |
| 13 | grok-4.5 / labor_supply.policy_response.substitution_elasticity.primary.decile_3 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 3 | total_sd | 0.6374273684114921 | 0.637481227610316 |
| 14 | grok-4.5 / labor_supply.policy_response.substitution_elasticity.primary.decile_4 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 4 | between_run_sd | 0.030912061651652337 | 0.030856234738253822 |
| 14 | grok-4.5 / labor_supply.policy_response.substitution_elasticity.primary.decile_4 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 4 | total_sd | 0.6372669094570099 | 0.6372642038868617 |
| 15 | grok-4.5 / labor_supply.policy_response.substitution_elasticity.primary.decile_5 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 5 | between_run_sd | 0.019999999999999993 | 0.024302206118421057 |
| 15 | grok-4.5 / labor_supply.policy_response.substitution_elasticity.primary.decile_5 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 5 | total_sd | 0.6373891515828894 | 0.6375386480659645 |
| 16 | grok-4.5 / labor_supply.policy_response.substitution_elasticity.primary.decile_6 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 6 | between_run_sd | 0.016996731711975945 | 0.020198941116361082 |
| 16 | grok-4.5 / labor_supply.policy_response.substitution_elasticity.primary.decile_6 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 6 | total_sd | 0.634267859863288 | 0.6343617472616779 |
| 17 | grok-4.5 / labor_supply.policy_response.substitution_elasticity.primary.decile_7 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 7 | between_run_sd | 0.02211083193570266 | 0.020942381271797456 |
| 17 | grok-4.5 / labor_supply.policy_response.substitution_elasticity.primary.decile_7 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 7 | total_sd | 0.6367528301206573 | 0.63671332726048 |
| 18 | grok-4.5 / labor_supply.policy_response.substitution_elasticity.primary.decile_8 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 8 | between_run_sd | 0.02211083193570266 | 0.02333720206022992 |
| 18 | grok-4.5 / labor_supply.policy_response.substitution_elasticity.primary.decile_8 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 8 | total_sd | 0.6362650893211798 | 0.6363088872552386 |
| 19 | grok-4.5 / labor_supply.policy_response.substitution_elasticity.primary.decile_9 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 9 | between_run_sd | 0.02867441755680875 | 0.03211674018327514 |
| 19 | grok-4.5 / labor_supply.policy_response.substitution_elasticity.primary.decile_9 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 9 | total_sd | 0.6370167863652504 | 0.6371810173638954 |
| 20 | grok-4.5 / labor_supply.policy_response.substitution_elasticity.secondary / Secondary-earner substitution elasticity in a tax-benefit simulation | between_run_sd | 0.061101009266077866 | 0.063231057769633 |
| 20 | grok-4.5 / labor_supply.policy_response.substitution_elasticity.secondary / Secondary-earner substitution elasticity in a tax-benefit simulation | total_sd | 0.6563757815966907 | 0.6565774897146567 |
| 21 | grok-4.5 / macro.tfp_persistence.ar1 / TFP persistence | between_run_sd | 0.0 | 0.004620606020859169 |
| 21 | grok-4.5 / macro.tfp_persistence.ar1 / TFP persistence | total_sd | 0.12966606683665888 | 0.12974836757697142 |
| 22 | grok-4.5 / production.capital_labor_substitution / Elasticity of substitution between capital and labor | between_run_sd | 0.053748384988656986 | 0.054799761759417254 |
| 22 | grok-4.5 / production.capital_labor_substitution / Elasticity of substitution between capital and labor | total_sd | 1.2507825467149223 | 1.2508281673222212 |
| 23 | grok-4.5 / production.capital_share / Capital share in production | between_run_sd | 0.0 | 0.004161797154542216 |
| 23 | grok-4.5 / production.capital_share / Capital share in production | total_sd | 0.11239939946458789 | 0.11247642222063946 |
| 24 | grok-4.5 / tax.capital_gains_realizations.elasticity / Capital gains realizations elasticity | between_run_sd | 0.04422166387140532 | 0.043603007031880525 |
| 24 | grok-4.5 / tax.capital_gains_realizations.elasticity / Capital gains realizations elasticity | total_sd | 1.3581382272966345 | 1.35811822427619 |
| 25 | grok-4.5 / tax.capital_gains_realizations.elasticity.net_of_tax_rate / Capital gains realizations elasticity (net-of-tax-rate convention) | between_run_sd | 0.13391539617733778 | 0.16283482599111151 |
| 25 | grok-4.5 / tax.capital_gains_realizations.elasticity.net_of_tax_rate / Capital gains realizations elasticity (net-of-tax-rate convention) | total_sd | 1.3819529005883104 | 1.385054391230419 |
| 26 | grok-4.5 / tax.elasticity_of_taxable_income.top_earners / Elasticity of taxable income | between_run_sd | 0.03741657386773941 | 0.04058649884985017 |
| 26 | grok-4.5 / tax.elasticity_of_taxable_income.top_earners / Elasticity of taxable income | total_sd | 0.6869889514718883 | 0.6871688899632559 |
| 27 | grok-4.5 / trade.armington_elasticity.import_domestic / Armington elasticity | between_run_sd | 0.46427960923947065 | 0.4802314256920535 |
| 27 | grok-4.5 / trade.armington_elasticity.import_domestic / Armington elasticity | total_sd | 2.9060067102468983 | 2.9085978867259508 |

## `results/grok-4.5-ies-clarify-batch15/summary.csv` (2 cells)

| line | row | column | old | new |
|---|---|---|---|---|
| 2 | grok-4.5 / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | between_run_sd | 0.23570226039551584 | 0.17804427508035436 |
| 2 | grok-4.5 / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | total_sd | 0.8681467529872022 | 0.8542967827725653 |

## `results/inkling-armington-clarify-batch15/summary.csv` (3 cells)

| line | row | column | old | new |
|---|---|---|---|---|
| 2 | inkling / trade.armington_elasticity.import_domestic / Armington elasticity | pooled_upper_bound | 5.681443661164893 | 5.70930518578508 |
| 2 | inkling / trade.armington_elasticity.import_domestic / Armington elasticity | between_run_sd | 0.22271057451320087 | 0.3693498980942356 |
| 2 | inkling / trade.armington_elasticity.import_domestic / Armington elasticity | total_sd | 2.5542963776975935 | 2.571234981937915 |

## `results/inkling-elasticities-batch15/summary.csv` (117 cells)

| line | row | column | old | new |
|---|---|---|---|---|
| 2 | inkling / household.annual_discount_factor / Annual discount factor | between_run_sd | 0.007071067811865481 | 0.005359804100897748 |
| 2 | inkling / household.annual_discount_factor / Annual discount factor | total_sd | 0.12533737249697094 | 0.12525248278754575 |
| 3 | inkling / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | between_run_sd | 0.11785113019775792 | 0.12252369385370145 |
| 3 | inkling / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | total_sd | 0.7439442556775041 | 0.744698745951826 |
| 4 | inkling / household.relative_risk_aversion.crra / Coefficient of relative risk aversion | between_run_sd | 0.19955506062794354 | 0.2866892432970275 |
| 4 | inkling / household.relative_risk_aversion.crra / Coefficient of relative risk aversion | total_sd | 6.524590589539784 | 6.527836614155651 |
| 5 | inkling / labor_supply.extensive_margin.single_mothers / Employment participation elasticity of single mothers | between_run_sd | 0.06548960901462833 | 0.06131019944149223 |
| 5 | inkling / labor_supply.extensive_margin.single_mothers / Employment participation elasticity of single mothers | total_sd | 0.676073460217979 | 0.6756814155190135 |
| 6 | inkling / labor_supply.frisch_elasticity.prime_age / Frisch elasticity of labor supply | between_run_sd | 0.05120763831912405 | 0.04324733774722118 |
| 6 | inkling / labor_supply.frisch_elasticity.prime_age / Frisch elasticity of labor supply | total_sd | 1.2678951871332094 | 1.267598641351258 |
| 7 | inkling / labor_supply.income_elasticity.prime_age / Income elasticity of labor supply | between_run_sd | 0.012892719737209143 | 0.01291452670445185 |
| 7 | inkling / labor_supply.income_elasticity.prime_age / Income elasticity of labor supply | total_sd | 0.3058220115978864 | 0.3058229317032252 |
| 8 | inkling / labor_supply.marshallian_wage_elasticity.prime_age / Uncompensated wage elasticity of labor supply | between_run_sd | 0.040933550488023336 | 0.040956467404089224 |
| 8 | inkling / labor_supply.marshallian_wage_elasticity.prime_age / Uncompensated wage elasticity of labor supply | total_sd | 0.6132398286967343 | 0.6132413588194021 |
| 9 | inkling / labor_supply.policy_response.substitution_elasticity.all / Substitution elasticity of labor supply in a tax-benefit simulation | between_run_sd | 0.013266499161421606 | 0.014138658587951922 |
| 9 | inkling / labor_supply.policy_response.substitution_elasticity.all / Substitution elasticity of labor supply in a tax-benefit simulation | total_sd | 0.6314609581491691 | 0.6314798835539683 |
| 10 | inkling / labor_supply.policy_response.substitution_elasticity.primary.decile_1 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 1 | between_run_sd | 0.04237399621885521 | 0.038512104879144464 |
| 10 | inkling / labor_supply.policy_response.substitution_elasticity.primary.decile_1 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 1 | total_sd | 0.6346251857505254 | 0.6343790294891183 |
| 11 | inkling / labor_supply.policy_response.substitution_elasticity.primary.decile_10 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 10 | between_run_sd | 0.043614472623456337 | 0.04033628088403238 |
| 11 | inkling / labor_supply.policy_response.substitution_elasticity.primary.decile_10 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 10 | total_sd | 0.6290090829144591 | 0.6287902827829182 |
| 12 | inkling / labor_supply.policy_response.substitution_elasticity.primary.decile_2 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 2 | between_run_sd | 0.03774770044504551 | 0.037347184930356166 |
| 12 | inkling / labor_supply.policy_response.substitution_elasticity.primary.decile_2 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 2 | total_sd | 0.6312151992607417 | 0.631191374395366 |
| 13 | inkling / labor_supply.policy_response.substitution_elasticity.primary.decile_3 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 3 | between_run_sd | 0.02211083193570267 | 0.021520313401270186 |
| 13 | inkling / labor_supply.policy_response.substitution_elasticity.primary.decile_3 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 3 | total_sd | 0.6286712685409513 | 0.6286507765754282 |
| 14 | inkling / labor_supply.policy_response.substitution_elasticity.primary.decile_4 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 4 | pooled_point_estimate | 0.19266666666666668 | 0.2006666666666667 |
| 14 | inkling / labor_supply.policy_response.substitution_elasticity.primary.decile_4 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 4 | between_run_sd | 0.03492213560989012 | 0.021789230265329605 |
| 14 | inkling / labor_supply.policy_response.substitution_elasticity.primary.decile_4 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 4 | total_sd | 0.6286076114450625 | 0.6280149235222573 |
| 14 | inkling / labor_supply.policy_response.substitution_elasticity.primary.decile_4 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 4 | reml_latent_location | 0.18897735779860206 | 0.20000083231920174 |
| 14 | inkling / labor_supply.policy_response.substitution_elasticity.primary.decile_4 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 4 | reml_latent_lower | 0.1507468811184193 | 0.1596142724553862 |
| 14 | inkling / labor_supply.policy_response.substitution_elasticity.primary.decile_4 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 4 | reml_latent_upper | 0.23643063846075188 | 0.25007828527411247 |
| 14 | inkling / labor_supply.policy_response.substitution_elasticity.primary.decile_4 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 4 | reml_predictive_lower | 0.07643366287202703 | 0.0810027434883086 |
| 14 | inkling / labor_supply.policy_response.substitution_elasticity.primary.decile_4 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 4 | reml_predictive_upper | 0.4520207194843026 | 0.47686722100371737 |
| 14 | inkling / labor_supply.policy_response.substitution_elasticity.primary.decile_4 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 4 | reml_typical_within_sd | 0.10262451297395721 | 0.10836197223342849 |
| 14 | inkling / labor_supply.policy_response.substitution_elasticity.primary.decile_4 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 4 | bayes_latent_location | 0.18897107955401085 | 0.19998655800770337 |
| 14 | inkling / labor_supply.policy_response.substitution_elasticity.primary.decile_4 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 4 | bayes_latent_lower | 0.16524448555740173 | 0.1764228868535928 |
| 14 | inkling / labor_supply.policy_response.substitution_elasticity.primary.decile_4 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 4 | bayes_latent_upper | 0.21594938305084765 | 0.2265435845466135 |
| 14 | inkling / labor_supply.policy_response.substitution_elasticity.primary.decile_4 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 4 | bayes_predictive_lower | 0.10877706003569043 | 0.11934999910210858 |
| 14 | inkling / labor_supply.policy_response.substitution_elasticity.primary.decile_4 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 4 | bayes_predictive_upper | 0.324361970979127 | 0.3313959689297827 |
| 14 | inkling / labor_supply.policy_response.substitution_elasticity.primary.decile_4 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 4 | bayes_tau_mean | 0.0053066238105994165 | 0.004333342217491689 |
| 14 | inkling / labor_supply.policy_response.substitution_elasticity.primary.decile_4 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 4 | bayes_interval_scale_mean | 0.34689409688889883 | 0.30602504065012964 |
| 14 | inkling / labor_supply.policy_response.substitution_elasticity.primary.decile_4 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 4 | bayes_typical_within_sd | 0.06044156517040033 | 0.059941233687210924 |
| 15 | inkling / labor_supply.policy_response.substitution_elasticity.primary.decile_5 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 5 | between_run_sd | 0.02768071932270226 | 0.02553554167995833 |
| 15 | inkling / labor_supply.policy_response.substitution_elasticity.primary.decile_5 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 5 | total_sd | 0.6288518517018845 | 0.6287610778789949 |
| 16 | inkling / labor_supply.policy_response.substitution_elasticity.primary.decile_6 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 6 | between_run_sd | 0.0344222150491349 | 0.03121109133340618 |
| 16 | inkling / labor_supply.policy_response.substitution_elasticity.primary.decile_6 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 6 | total_sd | 0.6282345092488243 | 0.6280667495931022 |
| 17 | inkling / labor_supply.policy_response.substitution_elasticity.primary.decile_7 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 7 | between_run_sd | 0.029992591677871987 | 0.02552137448405857 |
| 17 | inkling / labor_supply.policy_response.substitution_elasticity.primary.decile_7 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 7 | total_sd | 0.6273158085136314 | 0.6271179383585763 |
| 18 | inkling / labor_supply.policy_response.substitution_elasticity.primary.decile_8 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 8 | between_run_sd | 0.03176301133219092 | 0.028969735165436977 |
| 18 | inkling / labor_supply.policy_response.substitution_elasticity.primary.decile_8 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 8 | total_sd | 0.6268679596923813 | 0.6267326348256931 |
| 19 | inkling / labor_supply.policy_response.substitution_elasticity.primary.decile_9 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 9 | between_run_sd | 0.024 | 0.023292249545479485 |
| 19 | inkling / labor_supply.policy_response.substitution_elasticity.primary.decile_9 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 9 | total_sd | 0.6271669490211075 | 0.6271402640823928 |
| 20 | inkling / labor_supply.policy_response.substitution_elasticity.secondary / Secondary-earner substitution elasticity in a tax-benefit simulation | between_run_sd | 0.06236095644623236 | 0.05719106865003777 |
| 20 | inkling / labor_supply.policy_response.substitution_elasticity.secondary / Secondary-earner substitution elasticity in a tax-benefit simulation | total_sd | 0.6283934962355284 | 0.6279015174018577 |
| 21 | inkling / macro.tfp_persistence.ar1 / TFP persistence | pooled_point_estimate | 0.948 | 0.952 |
| 21 | inkling / macro.tfp_persistence.ar1 / TFP persistence | between_run_sd | 0.013266499161421584 | 0.002784954617623464 |
| 21 | inkling / macro.tfp_persistence.ar1 / TFP persistence | total_sd | 0.12733915371732468 | 0.12667681730161467 |
| 21 | inkling / macro.tfp_persistence.ar1 / TFP persistence | reml_latent_location | 0.9491165946302976 | 0.9522990907232616 |
| 21 | inkling / macro.tfp_persistence.ar1 / TFP persistence | reml_latent_lower | 0.9320314946179643 | 0.9362107574804559 |
| 21 | inkling / macro.tfp_persistence.ar1 / TFP persistence | reml_latent_upper | 0.9620817699215162 | 0.9644837051555211 |
| 21 | inkling / macro.tfp_persistence.ar1 / TFP persistence | reml_predictive_lower | 0.8493907917822354 | 0.857876629121495 |
| 21 | inkling / macro.tfp_persistence.ar1 / TFP persistence | reml_predictive_upper | 0.9840490709703504 | 0.9850810628827603 |
| 21 | inkling / macro.tfp_persistence.ar1 / TFP persistence | reml_typical_within_sd | 0.035120376645156756 | 0.033034174347924695 |
| 21 | inkling / macro.tfp_persistence.ar1 / TFP persistence | bayes_latent_location | 0.9491155904766493 | 0.9522969199428465 |
| 21 | inkling / macro.tfp_persistence.ar1 / TFP persistence | bayes_latent_lower | 0.9400785473958913 | 0.9440750907068702 |
| 21 | inkling / macro.tfp_persistence.ar1 / TFP persistence | bayes_latent_upper | 0.9568519855486215 | 0.9593614592980233 |
| 21 | inkling / macro.tfp_persistence.ar1 / TFP persistence | bayes_predictive_lower | 0.9030103581314646 | 0.9105668444029402 |
| 21 | inkling / macro.tfp_persistence.ar1 / TFP persistence | bayes_predictive_upper | 0.9739365287650303 | 0.9750878298422733 |
| 21 | inkling / macro.tfp_persistence.ar1 / TFP persistence | bayes_tau_mean | 0.0014904092122859233 | 0.0012160777203422102 |
| 21 | inkling / macro.tfp_persistence.ar1 / TFP persistence | bayes_interval_scale_mean | 0.3122912982671763 | 0.29383950774407525 |
| 21 | inkling / macro.tfp_persistence.ar1 / TFP persistence | bayes_typical_within_sd | 0.01962669697945505 | 0.01790759748245946 |
| 22 | inkling / production.capital_labor_substitution / Elasticity of substitution between capital and labor | between_run_sd | 0.06782329983125268 | 0.06440994143418824 |
| 22 | inkling / production.capital_labor_substitution / Elasticity of substitution between capital and labor | total_sd | 1.2435580186840232 | 1.2433765263945145 |
| 23 | inkling / production.capital_share / Capital share in production | between_run_sd | 0.009977753031397158 | 0.0094666960093442 |
| 23 | inkling / production.capital_share / Capital share in production | total_sd | 0.10960516259130619 | 0.10955982130527797 |
| 24 | inkling / tax.capital_gains_realizations.elasticity / Capital gains realizations elasticity | n_quantile_repaired_runs | 1 | 0 |
| 24 | inkling / tax.capital_gains_realizations.elasticity / Capital gains realizations elasticity | pooled_point_estimate | -0.36666666666666664 | -0.48000000000000004 |
| 24 | inkling / tax.capital_gains_realizations.elasticity / Capital gains realizations elasticity | pooled_lower_bound | -1.563197737033236 | -1.5974183524180408 |
| 24 | inkling / tax.capital_gains_realizations.elasticity / Capital gains realizations elasticity | pooled_upper_bound | 1.1999999999999997 | -0.05661280494489866 |
| 24 | inkling / tax.capital_gains_realizations.elasticity / Capital gains realizations elasticity | within_run_sd | 1.3250025387816349 | 1.3181789016164183 |
| 24 | inkling / tax.capital_gains_realizations.elasticity / Capital gains realizations elasticity | between_run_sd | 0.42843384034825677 | 0.09279920976675035 |
| 24 | inkling / tax.capital_gains_realizations.elasticity / Capital gains realizations elasticity | total_sd | 1.3925470488760274 | 1.321441375922519 |
| 24 | inkling / tax.capital_gains_realizations.elasticity / Capital gains realizations elasticity | reml_latent_location | -0.2903951747183129 | -0.4611885069820332 |
| 24 | inkling / tax.capital_gains_realizations.elasticity / Capital gains realizations elasticity | reml_latent_lower | -0.6016328523782111 | -0.5715523744025752 |
| 24 | inkling / tax.capital_gains_realizations.elasticity / Capital gains realizations elasticity | reml_latent_upper | -0.008434485314367635 | -0.3543783951893964 |
| 24 | inkling / tax.capital_gains_realizations.elasticity / Capital gains realizations elasticity | reml_predictive_lower | -1.660165560700893 | -0.9390277561861975 |
| 24 | inkling / tax.capital_gains_realizations.elasticity / Capital gains realizations elasticity | reml_predictive_upper | 0.6497509478667052 | -0.04351714938955986 |
| 24 | inkling / tax.capital_gains_realizations.elasticity / Capital gains realizations elasticity | reml_tau | 0.6542964242489785 | 0.0 |
| 24 | inkling / tax.capital_gains_realizations.elasticity / Capital gains realizations elasticity | reml_typical_within_sd | 0.24741010122427767 | 0.2721684540461947 |
| 24 | inkling / tax.capital_gains_realizations.elasticity / Capital gains realizations elasticity | bayes_latent_location | -0.29553216577547126 | -0.4615993515469281 |
| 24 | inkling / tax.capital_gains_realizations.elasticity / Capital gains realizations elasticity | bayes_latent_lower | -0.6000753397671854 | -0.5251067564609038 |
| 24 | inkling / tax.capital_gains_realizations.elasticity / Capital gains realizations elasticity | bayes_latent_upper | -0.02155423477575802 | -0.39946463522578135 |
| 24 | inkling / tax.capital_gains_realizations.elasticity / Capital gains realizations elasticity | bayes_predictive_lower | -1.6759857306395194 | -0.7380745991307158 |
| 24 | inkling / tax.capital_gains_realizations.elasticity / Capital gains realizations elasticity | bayes_predictive_upper | 0.6487313121336769 | -0.20654383464039228 |
| 24 | inkling / tax.capital_gains_realizations.elasticity / Capital gains realizations elasticity | bayes_tau_mean | 0.6438438705711322 | 0.014181868086607772 |
| 24 | inkling / tax.capital_gains_realizations.elasticity / Capital gains realizations elasticity | bayes_interval_scale_mean | 0.6574513787767403 | 0.3266858431699361 |
| 24 | inkling / tax.capital_gains_realizations.elasticity / Capital gains realizations elasticity | bayes_typical_within_sd | 0.20095202173917204 | 0.15558106086426873 |
| 25 | inkling / tax.capital_gains_realizations.elasticity.net_of_tax_rate / Capital gains realizations elasticity (net-of-tax-rate convention) | between_run_sd | 0.2867441755680875 | 0.2985153541556391 |
| 25 | inkling / tax.capital_gains_realizations.elasticity.net_of_tax_rate / Capital gains realizations elasticity (net-of-tax-rate convention) | total_sd | 1.4443455361435427 | 1.446728454901687 |
| 26 | inkling / tax.elasticity_of_taxable_income.top_earners / Elasticity of taxable income | between_run_sd | 0.053124591501697425 | 0.0454844112489836 |
| 26 | inkling / tax.elasticity_of_taxable_income.top_earners / Elasticity of taxable income | total_sd | 0.660863561729819 | 0.6602933110873278 |
| 27 | inkling / trade.armington_elasticity.import_domestic / Armington elasticity | pooled_point_estimate | 1.66 | 1.7133333333333334 |
| 27 | inkling / trade.armington_elasticity.import_domestic / Armington elasticity | between_run_sd | 0.3362538723444931 | 0.21943006985268806 |
| 27 | inkling / trade.armington_elasticity.import_domestic / Armington elasticity | total_sd | 2.6495266872908956 | 2.637247533993644 |
| 27 | inkling / trade.armington_elasticity.import_domestic / Armington elasticity | reml_latent_location | 1.5961500237107011 | 1.6815303959256496 |
| 27 | inkling / trade.armington_elasticity.import_domestic / Armington elasticity | reml_latent_lower | 1.2742445380866239 | 1.343662891510562 |
| 27 | inkling / trade.armington_elasticity.import_domestic / Armington elasticity | reml_latent_upper | 1.9907315008171278 | 2.094816135102083 |
| 27 | inkling / trade.armington_elasticity.import_domestic / Armington elasticity | reml_predictive_lower | 0.6465149941334194 | 0.6829831504010317 |
| 27 | inkling / trade.armington_elasticity.import_domestic / Armington elasticity | reml_predictive_upper | 3.6757354842522982 | 3.8490904879746397 |
| 27 | inkling / trade.armington_elasticity.import_domestic / Armington elasticity | reml_typical_within_sd | 0.8519293174775426 | 0.8933365050427242 |
| 27 | inkling / trade.armington_elasticity.import_domestic / Armington elasticity | bayes_latent_location | 1.5966727256611084 | 1.6818034587403212 |
| 27 | inkling / trade.armington_elasticity.import_domestic / Armington elasticity | bayes_latent_lower | 1.388429938546182 | 1.4857434070096587 |
| 27 | inkling / trade.armington_elasticity.import_domestic / Armington elasticity | bayes_latent_upper | 1.8333549776024372 | 1.9011897575399859 |
| 27 | inkling / trade.armington_elasticity.import_domestic / Armington elasticity | bayes_predictive_lower | 0.8979611983486037 | 1.0096944667408767 |
| 27 | inkling / trade.armington_elasticity.import_domestic / Armington elasticity | bayes_predictive_upper | 2.7608823708783303 | 2.7369768175590714 |
| 27 | inkling / trade.armington_elasticity.import_domestic / Armington elasticity | bayes_tau_mean | 0.050493320529054773 | 0.035395030503823706 |
| 27 | inkling / trade.armington_elasticity.import_domestic / Armington elasticity | bayes_interval_scale_mean | 0.3793624913358289 | 0.30424013440980024 |
| 27 | inkling / trade.armington_elasticity.import_domestic / Armington elasticity | bayes_typical_within_sd | 0.524880721094004 | 0.4928189268357382 |

## `results/inkling-ies-clarify-batch15/summary.csv` (2 cells)

| line | row | column | old | new |
|---|---|---|---|---|
| 2 | inkling / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | between_run_sd | 0.11527744310527055 | 0.10241405610993487 |
| 2 | inkling / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | total_sd | 0.6838485862300872 | 0.6817980924649826 |

## `results/kimi-k2.6-armington-clarify-batch15/summary.csv` (2 cells)

| line | row | column | old | new |
|---|---|---|---|---|
| 2 | kimi-k2.6 / trade.armington_elasticity.import_domestic / Armington elasticity | between_run_sd | 0.17838784213679537 | 0.2198203812206684 |
| 2 | kimi-k2.6 / trade.armington_elasticity.import_domestic / Armington elasticity | total_sd | 2.5500163125839888 | 2.5532492969199505 |

## `results/kimi-k2.6-elasticities-batch15/summary.csv` (72 cells)

| line | row | column | old | new |
|---|---|---|---|---|
| 2 | kimi-k2.6 / household.annual_discount_factor / Annual discount factor | between_run_sd | 0.007180219742846011 | 0.004770962516446066 |
| 2 | kimi-k2.6 / household.annual_discount_factor / Annual discount factor | total_sd | 0.12640748977897717 | 0.12629354694520223 |
| 3 | kimi-k2.6 / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | between_run_sd | 0.21354156504062624 | 0.18228689993767763 |
| 3 | kimi-k2.6 / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | total_sd | 0.8742455676181606 | 0.8671411801943723 |
| 4 | kimi-k2.6 / household.relative_risk_aversion.crra / Coefficient of relative risk aversion | between_run_sd | 0.31622776601683794 | 0.480845493780371 |
| 4 | kimi-k2.6 / household.relative_risk_aversion.crra / Coefficient of relative risk aversion | total_sd | 6.777730261673152 | 6.7874030297963674 |
| 5 | kimi-k2.6 / labor_supply.extensive_margin.single_mothers / Employment participation elasticity of single mothers | between_run_sd | 0.10143416036468626 | 0.10250304873514739 |
| 5 | kimi-k2.6 / labor_supply.extensive_margin.single_mothers / Employment participation elasticity of single mothers | total_sd | 0.7083558084669659 | 0.7085096594260377 |
| 6 | kimi-k2.6 / labor_supply.frisch_elasticity.prime_age / Frisch elasticity of labor supply | between_run_sd | 0.09999999999999999 | 0.1170456345002049 |
| 6 | kimi-k2.6 / labor_supply.frisch_elasticity.prime_age / Frisch elasticity of labor supply | total_sd | 1.2857514285860667 | 1.2871893476356409 |
| 7 | kimi-k2.6 / labor_supply.income_elasticity.prime_age / Income elasticity of labor supply | between_run_sd | 0.01691810338726603 | 0.017304976805018326 |
| 7 | kimi-k2.6 / labor_supply.income_elasticity.prime_age / Income elasticity of labor supply | total_sd | 0.2971776030890918 | 0.2971998784955636 |
| 8 | kimi-k2.6 / labor_supply.marshallian_wage_elasticity.prime_age / Uncompensated wage elasticity of labor supply | between_run_sd | 0.030155154341063042 | 0.028444517144004318 |
| 8 | kimi-k2.6 / labor_supply.marshallian_wage_elasticity.prime_age / Uncompensated wage elasticity of labor supply | total_sd | 0.6071839061053358 | 0.607101353198587 |
| 9 | kimi-k2.6 / labor_supply.policy_response.substitution_elasticity.all / Substitution elasticity of labor supply in a tax-benefit simulation | between_run_sd | 0.035901098714230015 | 0.04298126206719491 |
| 9 | kimi-k2.6 / labor_supply.policy_response.substitution_elasticity.all / Substitution elasticity of labor supply in a tax-benefit simulation | total_sd | 0.6490427513311858 | 0.6494728578282203 |
| 10 | kimi-k2.6 / labor_supply.policy_response.substitution_elasticity.primary.decile_1 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 1 | between_run_sd | 0.03927113726672838 | 0.03757723897373102 |
| 10 | kimi-k2.6 / labor_supply.policy_response.substitution_elasticity.primary.decile_1 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 1 | total_sd | 0.6465768440624655 | 0.6464761727584741 |
| 11 | kimi-k2.6 / labor_supply.policy_response.substitution_elasticity.primary.decile_10 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 10 | between_run_sd | 0.022803508501982758 | 0.021711530474739824 |
| 11 | kimi-k2.6 / labor_supply.policy_response.substitution_elasticity.primary.decile_10 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 10 | total_sd | 0.640403056676028 | 0.6403651033243111 |
| 12 | kimi-k2.6 / labor_supply.policy_response.substitution_elasticity.primary.decile_2 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 2 | between_run_sd | 0.02958978802822953 | 0.031650416883334864 |
| 12 | kimi-k2.6 / labor_supply.policy_response.substitution_elasticity.primary.decile_2 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 2 | total_sd | 0.6431911706051666 | 0.6432892625233051 |
| 13 | kimi-k2.6 / labor_supply.policy_response.substitution_elasticity.primary.decile_3 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 3 | between_run_sd | 0.023999999999999997 | 0.025947896510764294 |
| 13 | kimi-k2.6 / labor_supply.policy_response.substitution_elasticity.primary.decile_3 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 3 | total_sd | 0.6442729008994041 | 0.644348402781187 |
| 14 | kimi-k2.6 / labor_supply.policy_response.substitution_elasticity.primary.decile_4 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 4 | between_run_sd | 0.03399346342395189 | 0.03631550021073034 |
| 14 | kimi-k2.6 / labor_supply.policy_response.substitution_elasticity.primary.decile_4 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 4 | total_sd | 0.641536094940192 | 0.6416633238008163 |
| 15 | kimi-k2.6 / labor_supply.policy_response.substitution_elasticity.primary.decile_5 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 5 | between_run_sd | 0.043461349368017654 | 0.04553409589405383 |
| 15 | kimi-k2.6 / labor_supply.policy_response.substitution_elasticity.primary.decile_5 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 5 | total_sd | 0.64158232454352 | 0.6417260662982818 |
| 16 | kimi-k2.6 / labor_supply.policy_response.substitution_elasticity.primary.decile_6 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 6 | between_run_sd | 0.032550814975289874 | 0.037491754649078064 |
| 16 | kimi-k2.6 / labor_supply.policy_response.substitution_elasticity.primary.decile_6 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 6 | total_sd | 0.6419291779039527 | 0.6421986807488439 |
| 17 | kimi-k2.6 / labor_supply.policy_response.substitution_elasticity.primary.decile_7 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 7 | between_run_sd | 0.029544693074880442 | 0.02994173044802558 |
| 17 | kimi-k2.6 / labor_supply.policy_response.substitution_elasticity.primary.decile_7 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 7 | total_sd | 0.6396893929435163 | 0.6397078534595131 |
| 18 | kimi-k2.6 / labor_supply.policy_response.substitution_elasticity.primary.decile_8 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 8 | between_run_sd | 0.04607240678178932 | 0.04855424801188873 |
| 18 | kimi-k2.6 / labor_supply.policy_response.substitution_elasticity.primary.decile_8 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 8 | total_sd | 0.6412583690162128 | 0.6414414580978273 |
| 19 | kimi-k2.6 / labor_supply.policy_response.substitution_elasticity.primary.decile_9 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 9 | between_run_sd | 0.05487764167268447 | 0.05305323322433381 |
| 19 | kimi-k2.6 / labor_supply.policy_response.substitution_elasticity.primary.decile_9 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 9 | total_sd | 0.6422004273502852 | 0.6420471002106379 |
| 20 | kimi-k2.6 / labor_supply.policy_response.substitution_elasticity.secondary / Secondary-earner substitution elasticity in a tax-benefit simulation | between_run_sd | 0.05312459150169743 | 0.055169561857563776 |
| 20 | kimi-k2.6 / labor_supply.policy_response.substitution_elasticity.secondary / Secondary-earner substitution elasticity in a tax-benefit simulation | total_sd | 0.6471856004183723 | 0.6473566711807505 |
| 21 | kimi-k2.6 / macro.tfp_persistence.ar1 / TFP persistence | between_run_sd | 0.010456258094238741 | 0.010473378951735978 |
| 21 | kimi-k2.6 / macro.tfp_persistence.ar1 / TFP persistence | total_sd | 0.13336121974005619 | 0.13336256320230533 |
| 22 | kimi-k2.6 / production.capital_labor_substitution / Elasticity of substitution between capital and labor | between_run_sd | 0.12064640713902573 | 0.12464772583386975 |
| 22 | kimi-k2.6 / production.capital_labor_substitution / Elasticity of substitution between capital and labor | total_sd | 1.2756861987878436 | 1.276070835721034 |
| 23 | kimi-k2.6 / production.capital_share / Capital share in production | between_run_sd | 0.012543258481484505 | 0.011015771521878177 |
| 23 | kimi-k2.6 / production.capital_share / Capital share in production | total_sd | 0.11519563673256995 | 0.11503933506027889 |
| 24 | kimi-k2.6 / tax.capital_gains_realizations.elasticity / Capital gains realizations elasticity | n_quantile_repaired_runs | 1 | 0 |
| 24 | kimi-k2.6 / tax.capital_gains_realizations.elasticity / Capital gains realizations elasticity | pooled_point_estimate | -0.38999999999999996 | -0.4533333333333333 |
| 24 | kimi-k2.6 / tax.capital_gains_realizations.elasticity / Capital gains realizations elasticity | pooled_lower_bound | -1.4994679479156283 | -1.5128235664553396 |
| 24 | kimi-k2.6 / tax.capital_gains_realizations.elasticity / Capital gains realizations elasticity | pooled_upper_bound | 0.7 | 0.0691073019310226 |
| 24 | kimi-k2.6 / tax.capital_gains_realizations.elasticity / Capital gains realizations elasticity | within_run_sd | 1.3440515036427898 | 1.3407763738678506 |
| 24 | kimi-k2.6 / tax.capital_gains_realizations.elasticity / Capital gains realizations elasticity | between_run_sd | 0.3210399767422535 | 0.14398992055773285 |
| 24 | kimi-k2.6 / tax.capital_gains_realizations.elasticity / Capital gains realizations elasticity | total_sd | 1.3818614659621677 | 1.348485959120244 |
| 24 | kimi-k2.6 / tax.capital_gains_realizations.elasticity / Capital gains realizations elasticity | reml_latent_location | -0.3109711417523613 | -0.40156058260904537 |
| 24 | kimi-k2.6 / tax.capital_gains_realizations.elasticity / Capital gains realizations elasticity | reml_latent_lower | -0.5367655652504268 | -0.5326845545152992 |
| 24 | kimi-k2.6 / tax.capital_gains_realizations.elasticity / Capital gains realizations elasticity | reml_latent_upper | -0.10081277282852952 | -0.2755935156846441 |
| 24 | kimi-k2.6 / tax.capital_gains_realizations.elasticity / Capital gains realizations elasticity | reml_predictive_lower | -1.2889978163010483 | -0.9892016015121339 |
| 24 | kimi-k2.6 / tax.capital_gains_realizations.elasticity / Capital gains realizations elasticity | reml_predictive_upper | 0.42868696049348465 | 0.09498063598481998 |
| 24 | kimi-k2.6 / tax.capital_gains_realizations.elasticity / Capital gains realizations elasticity | reml_tau | 0.4147186176382311 | 0.0 |
| 24 | kimi-k2.6 / tax.capital_gains_realizations.elasticity / Capital gains realizations elasticity | reml_typical_within_sd | 0.31544762750477345 | 0.32940785811239753 |
| 24 | kimi-k2.6 / tax.capital_gains_realizations.elasticity / Capital gains realizations elasticity | bayes_latent_location | -0.33302203650001516 | -0.40337265008804657 |
| 24 | kimi-k2.6 / tax.capital_gains_realizations.elasticity / Capital gains realizations elasticity | bayes_latent_lower | -0.5468597814249687 | -0.48681160112625577 |
| 24 | kimi-k2.6 / tax.capital_gains_realizations.elasticity / Capital gains realizations elasticity | bayes_latent_upper | -0.13640685583656698 | -0.3230727487264371 |
| 24 | kimi-k2.6 / tax.capital_gains_realizations.elasticity / Capital gains realizations elasticity | bayes_predictive_lower | -1.261800206957739 | -0.7744522235962492 |
| 24 | kimi-k2.6 / tax.capital_gains_realizations.elasticity / Capital gains realizations elasticity | bayes_predictive_upper | 0.3776104203653894 | -0.07156333602153175 |
| 24 | kimi-k2.6 / tax.capital_gains_realizations.elasticity / Capital gains realizations elasticity | bayes_tau_mean | 0.41797392961911817 | 0.022795655121271283 |
| 24 | kimi-k2.6 / tax.capital_gains_realizations.elasticity / Capital gains realizations elasticity | bayes_interval_scale_mean | 0.5180232472285452 | 0.38599415470115334 |
| 24 | kimi-k2.6 / tax.capital_gains_realizations.elasticity / Capital gains realizations elasticity | bayes_typical_within_sd | 0.22868447821675836 | 0.2047716783448458 |
| 25 | kimi-k2.6 / tax.capital_gains_realizations.elasticity.net_of_tax_rate / Capital gains realizations elasticity (net-of-tax-rate convention) | between_run_sd | 0.2965355515504563 | 0.3233708096837987 |
| 25 | kimi-k2.6 / tax.capital_gains_realizations.elasticity.net_of_tax_rate / Capital gains realizations elasticity (net-of-tax-rate convention) | total_sd | 1.449385609778617 | 1.455113051640853 |
| 26 | kimi-k2.6 / tax.elasticity_of_taxable_income.top_earners / Elasticity of taxable income | between_run_sd | 0.07302967433402215 | 0.07396389134045221 |
| 26 | kimi-k2.6 / tax.elasticity_of_taxable_income.top_earners / Elasticity of taxable income | total_sd | 0.6887086275131967 | 0.688808316950369 |
| 27 | kimi-k2.6 / trade.armington_elasticity.import_domestic / Armington elasticity | between_run_sd | 0.3438345855527367 | 0.38701945113334485 |
| 27 | kimi-k2.6 / trade.armington_elasticity.import_domestic / Armington elasticity | total_sd | 2.6926296007187225 | 2.6984840188520667 |

## `results/kimi-k2.6-ies-clarify-batch15/summary.csv` (2 cells)

| line | row | column | old | new |
|---|---|---|---|---|
| 2 | kimi-k2.6 / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | between_run_sd | 0.10561986345169906 | 0.06793175905928601 |
| 2 | kimi-k2.6 / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | total_sd | 0.7255297422879674 | 0.7210080271937184 |

## `results/kimi-k3-armington-clarify-batch15/summary.csv` (2 cells)

| line | row | column | old | new |
|---|---|---|---|---|
| 2 | kimi-k3 / trade.armington_elasticity.import_domestic / Armington elasticity | between_run_sd | 0.408248290463863 | 0.39988317738504026 |
| 2 | kimi-k3 / trade.armington_elasticity.import_domestic / Armington elasticity | total_sd | 2.849822704036945 | 2.848636398934292 |

## `results/kimi-k3-elasticities-batch15/summary.csv` (67 cells)

| line | row | column | old | new |
|---|---|---|---|---|
| 2 | kimi-k3 / household.annual_discount_factor / Annual discount factor | between_run_sd | 0.0 | 0.002413446129960693 |
| 2 | kimi-k3 / household.annual_discount_factor / Annual discount factor | total_sd | 0.12573705892103215 | 0.12576021910100718 |
| 3 | kimi-k3 / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | between_run_sd | 0.03399346342395189 | 0.05781291666516517 |
| 3 | kimi-k3 / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | total_sd | 0.7282210773522008 | 0.7297209845398293 |
| 4 | kimi-k3 / household.relative_risk_aversion.crra / Coefficient of relative risk aversion | between_run_sd | 0.0 | 0.3356290735320765 |
| 4 | kimi-k3 / household.relative_risk_aversion.crra / Coefficient of relative risk aversion | total_sd | 6.6639127775612765 | 6.672359431411384 |
| 5 | kimi-k3 / labor_supply.extensive_margin.single_mothers / Employment participation elasticity of single mothers | between_run_sd | 0.09285592184789412 | 0.08003315285277444 |
| 5 | kimi-k3 / labor_supply.extensive_margin.single_mothers / Employment participation elasticity of single mothers | total_sd | 0.732147146716044 | 0.7306315951132812 |
| 6 | kimi-k3 / labor_supply.frisch_elasticity.prime_age / Frisch elasticity of labor supply | between_run_sd | 0.03399346342395189 | 0.046647764028824444 |
| 6 | kimi-k3 / labor_supply.frisch_elasticity.prime_age / Frisch elasticity of labor supply | total_sd | 1.2949455426130219 | 1.29533949861288 |
| 7 | kimi-k3 / labor_supply.income_elasticity.prime_age / Income elasticity of labor supply | between_run_sd | 0.02719477073916152 | 0.025284184780213898 |
| 7 | kimi-k3 / labor_supply.income_elasticity.prime_age / Income elasticity of labor supply | total_sd | 0.3089855713999172 | 0.3088232792031355 |
| 8 | kimi-k3 / labor_supply.marshallian_wage_elasticity.prime_age / Uncompensated wage elasticity of labor supply | between_run_sd | 0.024494897427831775 | 0.026440152546206446 |
| 8 | kimi-k3 / labor_supply.marshallian_wage_elasticity.prime_age / Uncompensated wage elasticity of labor supply | total_sd | 0.6071604972694159 | 0.6072420860835579 |
| 9 | kimi-k3 / labor_supply.policy_response.substitution_elasticity.all / Substitution elasticity of labor supply in a tax-benefit simulation | between_run_sd | 0.0024944382578492965 | 0.014309573330078327 |
| 9 | kimi-k3 / labor_supply.policy_response.substitution_elasticity.all / Substitution elasticity of labor supply in a tax-benefit simulation | total_sd | 0.6365047841750899 | 0.6366607275028392 |
| 10 | kimi-k3 / labor_supply.policy_response.substitution_elasticity.primary.decile_1 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 1 | between_run_sd | 0.0402768199119819 | 0.04349069504567104 |
| 10 | kimi-k3 / labor_supply.policy_response.substitution_elasticity.primary.decile_1 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 1 | total_sd | 0.6434656362231008 | 0.6436747962545476 |
| 11 | kimi-k3 / labor_supply.policy_response.substitution_elasticity.primary.decile_10 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 10 | between_run_sd | 0.03265986323710904 | 0.031291967375386004 |
| 11 | kimi-k3 / labor_supply.policy_response.substitution_elasticity.primary.decile_10 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 10 | total_sd | 0.6427594180130264 | 0.6426913644977658 |
| 12 | kimi-k3 / labor_supply.policy_response.substitution_elasticity.primary.decile_2 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 2 | between_run_sd | 0.04019950248448356 | 0.038088128800921106 |
| 12 | kimi-k3 / labor_supply.policy_response.substitution_elasticity.primary.decile_2 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 2 | total_sd | 0.6387513068044907 | 0.6386219049641189 |
| 13 | kimi-k3 / labor_supply.policy_response.substitution_elasticity.primary.decile_3 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 3 | between_run_sd | 0.04173993557999608 | 0.03917778565576275 |
| 13 | kimi-k3 / labor_supply.policy_response.substitution_elasticity.primary.decile_3 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 3 | total_sd | 0.6389231522213329 | 0.638760887274034 |
| 14 | kimi-k3 / labor_supply.policy_response.substitution_elasticity.primary.decile_4 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 4 | between_run_sd | 0.03461534662865912 | 0.0314766844929174 |
| 14 | kimi-k3 / labor_supply.policy_response.substitution_elasticity.primary.decile_4 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 4 | total_sd | 0.6379541574003923 | 0.6377915540275592 |
| 15 | kimi-k3 / labor_supply.policy_response.substitution_elasticity.primary.decile_5 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 5 | between_run_sd | 0.027080128015453207 | 0.026823165775542272 |
| 15 | kimi-k3 / labor_supply.policy_response.substitution_elasticity.primary.decile_5 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 5 | total_sd | 0.6396531992242185 | 0.6396423720851103 |
| 16 | kimi-k3 / labor_supply.policy_response.substitution_elasticity.primary.decile_6 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 6 | between_run_sd | 0.03641733408999377 | 0.033971785679034035 |
| 16 | kimi-k3 / labor_supply.policy_response.substitution_elasticity.primary.decile_6 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 6 | total_sd | 0.6373901343238169 | 0.6372550849803659 |
| 17 | kimi-k3 / labor_supply.policy_response.substitution_elasticity.primary.decile_7 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 7 | between_run_sd | 0.035251477510406096 | 0.030261205454435485 |
| 17 | kimi-k3 / labor_supply.policy_response.substitution_elasticity.primary.decile_7 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 7 | total_sd | 0.6388157109057353 | 0.6385597751102781 |
| 18 | kimi-k3 / labor_supply.policy_response.substitution_elasticity.primary.decile_8 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 8 | between_run_sd | 0.03858612300930075 | 0.03339197342010335 |
| 18 | kimi-k3 / labor_supply.policy_response.substitution_elasticity.primary.decile_8 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 8 | total_sd | 0.6367621536160718 | 0.6364685186855497 |
| 19 | kimi-k3 / labor_supply.policy_response.substitution_elasticity.primary.decile_9 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 9 | between_run_sd | 0.057904135334955906 | 0.05564878455296416 |
| 19 | kimi-k3 / labor_supply.policy_response.substitution_elasticity.primary.decile_9 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 9 | total_sd | 0.639094326632097 | 0.6388939322506254 |
| 20 | kimi-k3 / labor_supply.policy_response.substitution_elasticity.secondary / Secondary-earner substitution elasticity in a tax-benefit simulation | between_run_sd | 0.07526545614615572 | 0.06541660509551243 |
| 20 | kimi-k3 / labor_supply.policy_response.substitution_elasticity.secondary / Secondary-earner substitution elasticity in a tax-benefit simulation | total_sd | 0.6416172145446224 | 0.6405365667417695 |
| 21 | kimi-k3 / macro.tfp_persistence.ar1 / TFP persistence | between_run_sd | 0.012543258481484503 | 0.013685852386883156 |
| 21 | kimi-k3 / macro.tfp_persistence.ar1 / TFP persistence | total_sd | 0.13352735341910701 | 0.13363952758571596 |
| 22 | kimi-k3 / production.capital_labor_substitution / Elasticity of substitution between capital and labor | between_run_sd | 0.05830951894845301 | 0.04768924290538578 |
| 22 | kimi-k3 / production.capital_labor_substitution / Elasticity of substitution between capital and labor | total_sd | 1.247669410674692 | 1.2472181935099496 |
| 23 | kimi-k3 / production.capital_share / Capital share in production | between_run_sd | 0.007999999999999995 | 0.0065438690560113005 |
| 23 | kimi-k3 / production.capital_share / Capital share in production | total_sd | 0.11469117955041995 | 0.11459881713564452 |
| 24 | kimi-k3 / tax.capital_gains_realizations.elasticity / Capital gains realizations elasticity | between_run_sd | 0.14005713120009278 | 0.1274967145546199 |
| 24 | kimi-k3 / tax.capital_gains_realizations.elasticity / Capital gains realizations elasticity | total_sd | 1.3325857675128374 | 1.3313242430001793 |
| 25 | kimi-k3 / tax.capital_gains_realizations.elasticity.net_of_tax_rate / Capital gains realizations elasticity (net-of-tax-rate convention) | pooled_point_estimate | 0.85 | 0.7166666666666667 |
| 25 | kimi-k3 / tax.capital_gains_realizations.elasticity.net_of_tax_rate / Capital gains realizations elasticity (net-of-tax-rate convention) | between_run_sd | 0.6814200858012136 | 0.376348187631259 |
| 25 | kimi-k3 / tax.capital_gains_realizations.elasticity.net_of_tax_rate / Capital gains realizations elasticity (net-of-tax-rate convention) | total_sd | 1.557591545820377 | 1.4503089493660002 |
| 25 | kimi-k3 / tax.capital_gains_realizations.elasticity.net_of_tax_rate / Capital gains realizations elasticity (net-of-tax-rate convention) | reml_latent_location | 0.6249207421039267 | 0.5784884704695532 |
| 25 | kimi-k3 / tax.capital_gains_realizations.elasticity.net_of_tax_rate / Capital gains realizations elasticity (net-of-tax-rate convention) | reml_latent_lower | 0.44478490713635965 | 0.4007230976645326 |
| 25 | kimi-k3 / tax.capital_gains_realizations.elasticity.net_of_tax_rate / Capital gains realizations elasticity (net-of-tax-rate convention) | reml_latent_upper | 0.8144199051793999 | 0.7656244267648327 |
| 25 | kimi-k3 / tax.capital_gains_realizations.elasticity.net_of_tax_rate / Capital gains realizations elasticity (net-of-tax-rate convention) | reml_predictive_lower | -0.11437904247018094 | -0.15031399092713738 |
| 25 | kimi-k3 / tax.capital_gains_realizations.elasticity.net_of_tax_rate / Capital gains realizations elasticity (net-of-tax-rate convention) | reml_predictive_upper | 1.55227793867805 | 1.4955579786374185 |
| 25 | kimi-k3 / tax.capital_gains_realizations.elasticity.net_of_tax_rate / Capital gains realizations elasticity (net-of-tax-rate convention) | reml_typical_within_sd | 0.5070527556947971 | 0.5005503650276235 |
| 25 | kimi-k3 / tax.capital_gains_realizations.elasticity.net_of_tax_rate / Capital gains realizations elasticity (net-of-tax-rate convention) | bayes_latent_location | 0.628188594682066 | 0.5798058927816561 |
| 25 | kimi-k3 / tax.capital_gains_realizations.elasticity.net_of_tax_rate / Capital gains realizations elasticity (net-of-tax-rate convention) | bayes_latent_lower | 0.4554931820631678 | 0.4663728897090924 |
| 25 | kimi-k3 / tax.capital_gains_realizations.elasticity.net_of_tax_rate / Capital gains realizations elasticity (net-of-tax-rate convention) | bayes_latent_upper | 0.8118751564714835 | 0.6977146761653379 |
| 25 | kimi-k3 / tax.capital_gains_realizations.elasticity.net_of_tax_rate / Capital gains realizations elasticity (net-of-tax-rate convention) | bayes_predictive_lower | -0.09545282013054202 | 0.08824320684783249 |
| 25 | kimi-k3 / tax.capital_gains_realizations.elasticity.net_of_tax_rate / Capital gains realizations elasticity (net-of-tax-rate convention) | bayes_predictive_upper | 1.5326417035010858 | 1.150950433123188 |
| 25 | kimi-k3 / tax.capital_gains_realizations.elasticity.net_of_tax_rate / Capital gains realizations elasticity (net-of-tax-rate convention) | bayes_tau_mean | 0.039838945839323466 | 0.0219486008116392 |
| 25 | kimi-k3 / tax.capital_gains_realizations.elasticity.net_of_tax_rate / Capital gains realizations elasticity (net-of-tax-rate convention) | bayes_interval_scale_mean | 0.8904219365550567 | 0.3942180702915216 |
| 25 | kimi-k3 / tax.capital_gains_realizations.elasticity.net_of_tax_rate / Capital gains realizations elasticity (net-of-tax-rate convention) | bayes_typical_within_sd | 0.47889466265373015 | 0.3143961004213812 |
| 26 | kimi-k3 / tax.elasticity_of_taxable_income.top_earners / Elasticity of taxable income | between_run_sd | 0.04760952285695235 | 0.04803817926052847 |
| 26 | kimi-k3 / tax.elasticity_of_taxable_income.top_earners / Elasticity of taxable income | total_sd | 0.6844572819638443 | 0.6844872320455169 |
| 27 | kimi-k3 / trade.armington_elasticity.import_domestic / Armington elasticity | between_run_sd | 0.4472135954999579 | 0.4530515668466695 |
| 27 | kimi-k3 / trade.armington_elasticity.import_domestic / Armington elasticity | total_sd | 2.935844308807188 | 2.9367392679258706 |

## `results/kimi-k3-ies-clarify-batch15/summary.csv` (2 cells)

| line | row | column | old | new |
|---|---|---|---|---|
| 2 | kimi-k3 / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | between_run_sd | 0.054772255750516606 | 0.07946496432740377 |
| 2 | kimi-k3 / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | total_sd | 0.7119349855226327 | 0.7142591295648006 |

## `results/minimax-m3-armington-clarify-batch15/summary.csv` (2 cells)

| line | row | column | old | new |
|---|---|---|---|---|
| 2 | minimax-m3 / trade.armington_elasticity.import_domestic / Armington elasticity | between_run_sd | 0.24997777679003566 | 0.2765896479142583 |
| 2 | minimax-m3 / trade.armington_elasticity.import_domestic / Armington elasticity | total_sd | 2.6228712267708114 | 2.625541166439153 |

## `results/minimax-m3-elasticities-batch15/summary.csv` (67 cells)

| line | row | column | old | new |
|---|---|---|---|---|
| 2 | minimax-m3 / household.annual_discount_factor / Annual discount factor | between_run_sd | 0.0060184900284226015 | 0.005442247289085244 |
| 2 | minimax-m3 / household.annual_discount_factor / Annual discount factor | total_sd | 0.12567592251501478 | 0.12564964517790464 |
| 3 | minimax-m3 / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | between_run_sd | 0.043461349368017654 | 0.049719770268531555 |
| 3 | minimax-m3 / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | total_sd | 0.6894992144061273 | 0.6899219762649493 |
| 4 | minimax-m3 / household.relative_risk_aversion.crra / Coefficient of relative risk aversion | between_run_sd | 0.1699673171197595 | 0.23811213511471635 |
| 4 | minimax-m3 / household.relative_risk_aversion.crra / Coefficient of relative risk aversion | total_sd | 6.405563922611862 | 6.4077342069304555 |
| 5 | minimax-m3 / labor_supply.extensive_margin.single_mothers / Employment participation elasticity of single mothers | between_run_sd | 0.1755625877635159 | 0.16529321589896612 |
| 5 | minimax-m3 / labor_supply.extensive_margin.single_mothers / Employment participation elasticity of single mothers | total_sd | 0.7160329077633234 | 0.7135844378908498 |
| 6 | minimax-m3 / labor_supply.frisch_elasticity.prime_age / Frisch elasticity of labor supply | between_run_sd | 0.1299572579307862 | 0.13604548871609085 |
| 6 | minimax-m3 / labor_supply.frisch_elasticity.prime_age / Frisch elasticity of labor supply | total_sd | 1.2832151731317534 | 1.2838460447680893 |
| 7 | minimax-m3 / labor_supply.income_elasticity.prime_age / Income elasticity of labor supply | between_run_sd | 0.04192055979269997 | 0.04913030859074897 |
| 7 | minimax-m3 / labor_supply.income_elasticity.prime_age / Income elasticity of labor supply | total_sd | 0.32617347548675857 | 0.3271782236029776 |
| 8 | minimax-m3 / labor_supply.marshallian_wage_elasticity.prime_age / Uncompensated wage elasticity of labor supply | between_run_sd | 0.01720465053408525 | 0.020363543132001585 |
| 8 | minimax-m3 / labor_supply.marshallian_wage_elasticity.prime_age / Uncompensated wage elasticity of labor supply | total_sd | 0.5975178577061758 | 0.5976171551810295 |
| 9 | minimax-m3 / labor_supply.policy_response.substitution_elasticity.all / Substitution elasticity of labor supply in a tax-benefit simulation | between_run_sd | 0.03323986896618109 | 0.04057610818641378 |
| 9 | minimax-m3 / labor_supply.policy_response.substitution_elasticity.all / Substitution elasticity of labor supply in a tax-benefit simulation | total_sd | 0.6409652248323964 | 0.6413875202333695 |
| 10 | minimax-m3 / labor_supply.policy_response.substitution_elasticity.primary.decile_1 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 1 | between_run_sd | 0.058133944950911044 | 0.05949424808799215 |
| 10 | minimax-m3 / labor_supply.policy_response.substitution_elasticity.primary.decile_1 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 1 | total_sd | 0.6415286388341868 | 0.6416533366580778 |
| 11 | minimax-m3 / labor_supply.policy_response.substitution_elasticity.primary.decile_10 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 10 | between_run_sd | 0.07066037707859256 | 0.07604569167429685 |
| 11 | minimax-m3 / labor_supply.policy_response.substitution_elasticity.primary.decile_10 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 10 | total_sd | 0.6436391522688263 | 0.6442526031508655 |
| 12 | minimax-m3 / labor_supply.policy_response.substitution_elasticity.primary.decile_2 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 2 | between_run_sd | 0.02963481436119049 | 0.03285348789195245 |
| 12 | minimax-m3 / labor_supply.policy_response.substitution_elasticity.primary.decile_2 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 2 | total_sd | 0.6376678058013872 | 0.6378254933757352 |
| 13 | minimax-m3 / labor_supply.policy_response.substitution_elasticity.primary.decile_3 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 3 | between_run_sd | 0.035714920629277 | 0.03764269148483172 |
| 13 | minimax-m3 / labor_supply.policy_response.substitution_elasticity.primary.decile_3 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 3 | total_sd | 0.6342129856058697 | 0.6343244656938417 |
| 14 | minimax-m3 / labor_supply.policy_response.substitution_elasticity.primary.decile_4 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 4 | between_run_sd | 0.04611097724210823 | 0.03787024630967635 |
| 14 | minimax-m3 / labor_supply.policy_response.substitution_elasticity.primary.decile_4 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 4 | total_sd | 0.6346393857932235 | 0.6340939073460123 |
| 15 | minimax-m3 / labor_supply.policy_response.substitution_elasticity.primary.decile_5 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 5 | between_run_sd | 0.035377331097124265 | 0.03571818708849721 |
| 15 | minimax-m3 / labor_supply.policy_response.substitution_elasticity.primary.decile_5 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 5 | total_sd | 0.6382194545939682 | 0.638238439421785 |
| 16 | minimax-m3 / labor_supply.policy_response.substitution_elasticity.primary.decile_6 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 6 | between_run_sd | 0.04882622246293481 | 0.05078597794229778 |
| 16 | minimax-m3 / labor_supply.policy_response.substitution_elasticity.primary.decile_6 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 6 | total_sd | 0.6383730307499597 | 0.6385259132912653 |
| 17 | minimax-m3 / labor_supply.policy_response.substitution_elasticity.primary.decile_7 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 7 | between_run_sd | 0.052179178478265316 | 0.05046564838250536 |
| 17 | minimax-m3 / labor_supply.policy_response.substitution_elasticity.primary.decile_7 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 7 | total_sd | 0.6373601001178394 | 0.637222105880063 |
| 18 | minimax-m3 / labor_supply.policy_response.substitution_elasticity.primary.decile_8 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 8 | between_run_sd | 0.051751543186867595 | 0.049442278354550874 |
| 18 | minimax-m3 / labor_supply.policy_response.substitution_elasticity.primary.decile_8 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 8 | total_sd | 0.6392032497136138 | 0.6390204309027303 |
| 19 | minimax-m3 / labor_supply.policy_response.substitution_elasticity.primary.decile_9 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 9 | between_run_sd | 0.04939635614091387 | 0.04500044444224968 |
| 19 | minimax-m3 / labor_supply.policy_response.substitution_elasticity.primary.decile_9 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 9 | total_sd | 0.6376102388345616 | 0.6372847532043009 |
| 20 | minimax-m3 / labor_supply.policy_response.substitution_elasticity.secondary / Secondary-earner substitution elasticity in a tax-benefit simulation | pooled_point_estimate | 0.36000000000000004 | 0.38 |
| 20 | minimax-m3 / labor_supply.policy_response.substitution_elasticity.secondary / Secondary-earner substitution elasticity in a tax-benefit simulation | between_run_sd | 0.1818424226264781 | 0.16724661597639442 |
| 20 | minimax-m3 / labor_supply.policy_response.substitution_elasticity.secondary / Secondary-earner substitution elasticity in a tax-benefit simulation | total_sd | 0.7001731184738053 | 0.6965250603691314 |
| 20 | minimax-m3 / labor_supply.policy_response.substitution_elasticity.secondary / Secondary-earner substitution elasticity in a tax-benefit simulation | reml_latent_location | 0.346895044309479 | 0.3714932956712552 |
| 20 | minimax-m3 / labor_supply.policy_response.substitution_elasticity.secondary / Secondary-earner substitution elasticity in a tax-benefit simulation | reml_latent_lower | 0.24396111893113004 | 0.2616708141906382 |
| 20 | minimax-m3 / labor_supply.policy_response.substitution_elasticity.secondary / Secondary-earner substitution elasticity in a tax-benefit simulation | reml_latent_upper | 0.4887960986943517 | 0.5223270092155561 |
| 20 | minimax-m3 / labor_supply.policy_response.substitution_elasticity.secondary / Secondary-earner substitution elasticity in a tax-benefit simulation | reml_predictive_lower | 0.08447195991071679 | 0.09082506912048023 |
| 20 | minimax-m3 / labor_supply.policy_response.substitution_elasticity.secondary / Secondary-earner substitution elasticity in a tax-benefit simulation | reml_predictive_upper | 1.2219125114485236 | 1.2913385749350987 |
| 20 | minimax-m3 / labor_supply.policy_response.substitution_elasticity.secondary / Secondary-earner substitution elasticity in a tax-benefit simulation | reml_typical_within_sd | 0.28801297270938997 | 0.3068053885968461 |
| 20 | minimax-m3 / labor_supply.policy_response.substitution_elasticity.secondary / Secondary-earner substitution elasticity in a tax-benefit simulation | bayes_latent_location | 0.3460717798501298 | 0.37102562785957033 |
| 20 | minimax-m3 / labor_supply.policy_response.substitution_elasticity.secondary / Secondary-earner substitution elasticity in a tax-benefit simulation | bayes_latent_lower | 0.2725345711373811 | 0.2994788562355831 |
| 20 | minimax-m3 / labor_supply.policy_response.substitution_elasticity.secondary / Secondary-earner substitution elasticity in a tax-benefit simulation | bayes_latent_upper | 0.437152183441033 | 0.4577413388797156 |
| 20 | minimax-m3 / labor_supply.policy_response.substitution_elasticity.secondary / Secondary-earner substitution elasticity in a tax-benefit simulation | bayes_predictive_lower | 0.12954475682381617 | 0.15352205218523252 |
| 20 | minimax-m3 / labor_supply.policy_response.substitution_elasticity.secondary / Secondary-earner substitution elasticity in a tax-benefit simulation | bayes_predictive_upper | 0.859773037398631 | 0.8426512332600183 |
| 20 | minimax-m3 / labor_supply.policy_response.substitution_elasticity.secondary / Secondary-earner substitution elasticity in a tax-benefit simulation | bayes_tau_mean | 0.022108296991117708 | 0.01848575902904385 |
| 20 | minimax-m3 / labor_supply.policy_response.substitution_elasticity.secondary / Secondary-earner substitution elasticity in a tax-benefit simulation | bayes_interval_scale_mean | 0.4450395277548748 | 0.3667468208365754 |
| 20 | minimax-m3 / labor_supply.policy_response.substitution_elasticity.secondary / Secondary-earner substitution elasticity in a tax-benefit simulation | bayes_typical_within_sd | 0.19171507585871642 | 0.1855850419734866 |
| 21 | minimax-m3 / macro.tfp_persistence.ar1 / TFP persistence | between_run_sd | 0.11523116862299983 | 0.10553729790931735 |
| 21 | minimax-m3 / macro.tfp_persistence.ar1 / TFP persistence | total_sd | 0.18951555381785656 | 0.18378260028268906 |
| 22 | minimax-m3 / production.capital_labor_substitution / Elasticity of substitution between capital and labor | between_run_sd | 0.04422166387140533 | 0.04652239604033024 |
| 22 | minimax-m3 / production.capital_labor_substitution / Elasticity of substitution between capital and labor | total_sd | 1.2318075584729584 | 1.2318923000363664 |
| 23 | minimax-m3 / production.capital_share / Capital share in production | between_run_sd | 0.017435595774162687 | 0.016736487086602136 |
| 23 | minimax-m3 / production.capital_share / Capital share in production | total_sd | 0.1182374200496611 | 0.1181363513064459 |
| 24 | minimax-m3 / tax.capital_gains_realizations.elasticity / Capital gains realizations elasticity | between_run_sd | 0.1794609211561732 | 0.1988438248140149 |
| 24 | minimax-m3 / tax.capital_gains_realizations.elasticity / Capital gains realizations elasticity | total_sd | 1.3381553072752388 | 1.3408923412538882 |
| 25 | minimax-m3 / tax.capital_gains_realizations.elasticity.net_of_tax_rate / Capital gains realizations elasticity (net-of-tax-rate convention) | between_run_sd | 1.1332647038044064 | 1.1921102496087441 |
| 25 | minimax-m3 / tax.capital_gains_realizations.elasticity.net_of_tax_rate / Capital gains realizations elasticity (net-of-tax-rate convention) | total_sd | 1.936736605879993 | 1.9717471031775067 |
| 26 | minimax-m3 / tax.elasticity_of_taxable_income.top_earners / Elasticity of taxable income | between_run_sd | 0.06182412330330469 | 0.07064268460986523 |
| 26 | minimax-m3 / tax.elasticity_of_taxable_income.top_earners / Elasticity of taxable income | total_sd | 0.6943114844938114 | 0.6951522165444535 |
| 27 | minimax-m3 / trade.armington_elasticity.import_domestic / Armington elasticity | between_run_sd | 0.2729265265394496 | 0.2864242434261148 |
| 27 | minimax-m3 / trade.armington_elasticity.import_domestic / Armington elasticity | total_sd | 2.5858212616540657 | 2.58728072608203 |

## `results/minimax-m3-ies-clarify-batch15/summary.csv` (2 cells)

| line | row | column | old | new |
|---|---|---|---|---|
| 2 | minimax-m3 / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | between_run_sd | 0.032659863237109045 | 0.039569208006001604 |
| 2 | minimax-m3 / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | total_sd | 0.6914962390433596 | 0.691856996905189 |

## `results/qwen-3.7-max-armington-clarify-batch15/summary.csv` (2 cells)

| line | row | column | old | new |
|---|---|---|---|---|
| 2 | qwen-3.7-max / trade.armington_elasticity.import_domestic / Armington elasticity | between_run_sd | 0.12472191289246472 | 0.16633454408376983 |
| 2 | qwen-3.7-max / trade.armington_elasticity.import_domestic / Armington elasticity | total_sd | 2.542699414500267 | 2.5450799471725833 |

## `results/qwen-3.7-max-elasticities-batch15/summary.csv` (52 cells)

| line | row | column | old | new |
|---|---|---|---|---|
| 2 | qwen-3.7-max / household.annual_discount_factor / Annual discount factor | between_run_sd | 0.008793937305515287 | 0.008306606139426359 |
| 2 | qwen-3.7-max / household.annual_discount_factor / Annual discount factor | total_sd | 0.12639829475379272 | 0.12636532470930817 |
| 3 | qwen-3.7-max / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | between_run_sd | 0.20725722075613084 | 0.1831005340122075 |
| 3 | qwen-3.7-max / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | total_sd | 0.7565038141565006 | 0.7502454737173249 |
| 4 | qwen-3.7-max / household.relative_risk_aversion.crra / Coefficient of relative risk aversion | between_run_sd | 0.0 | 0.26198579265974625 |
| 4 | qwen-3.7-max / household.relative_risk_aversion.crra / Coefficient of relative risk aversion | total_sd | 6.4450231445149475 | 6.450345718555626 |
| 5 | qwen-3.7-max / labor_supply.extensive_margin.single_mothers / Employment participation elasticity of single mothers | between_run_sd | 0.056764621219754695 | 0.062426401110071666 |
| 5 | qwen-3.7-max / labor_supply.extensive_margin.single_mothers / Employment participation elasticity of single mothers | total_sd | 0.7362138502726863 | 0.7366720210966795 |
| 6 | qwen-3.7-max / labor_supply.frisch_elasticity.prime_age / Frisch elasticity of labor supply | between_run_sd | 0.12015915371798447 | 0.12790178089282242 |
| 6 | qwen-3.7-max / labor_supply.frisch_elasticity.prime_age / Frisch elasticity of labor supply | total_sd | 1.304671897877436 | 1.3054077540923543 |
| 7 | qwen-3.7-max / labor_supply.income_elasticity.prime_age / Income elasticity of labor supply | between_run_sd | 0.014079141387961918 | 0.013144327039956561 |
| 7 | qwen-3.7-max / labor_supply.income_elasticity.prime_age / Income elasticity of labor supply | total_sd | 0.3036669296559417 | 0.3036250241297278 |
| 8 | qwen-3.7-max / labor_supply.marshallian_wage_elasticity.prime_age / Uncompensated wage elasticity of labor supply | between_run_sd | 0.029484459183327975 | 0.03261822939536862 |
| 8 | qwen-3.7-max / labor_supply.marshallian_wage_elasticity.prime_age / Uncompensated wage elasticity of labor supply | total_sd | 0.5984505224141573 | 0.5986130998677972 |
| 9 | qwen-3.7-max / labor_supply.policy_response.substitution_elasticity.all / Substitution elasticity of labor supply in a tax-benefit simulation | between_run_sd | 0.017461067804945062 | 0.01722969013715054 |
| 9 | qwen-3.7-max / labor_supply.policy_response.substitution_elasticity.all / Substitution elasticity of labor supply in a tax-benefit simulation | total_sd | 0.6437916113843741 | 0.6437853774529384 |
| 10 | qwen-3.7-max / labor_supply.policy_response.substitution_elasticity.primary.decile_1 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 1 | between_run_sd | 0.02954469307488045 | 0.0312298201510458 |
| 10 | qwen-3.7-max / labor_supply.policy_response.substitution_elasticity.primary.decile_1 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 1 | total_sd | 0.6421081046487075 | 0.6421878469990951 |
| 11 | qwen-3.7-max / labor_supply.policy_response.substitution_elasticity.primary.decile_10 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 10 | between_run_sd | 0.05521674464226309 | 0.054226290261786825 |
| 11 | qwen-3.7-max / labor_supply.policy_response.substitution_elasticity.primary.decile_10 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 10 | total_sd | 0.6373400245900491 | 0.6372549792752593 |
| 12 | qwen-3.7-max / labor_supply.policy_response.substitution_elasticity.primary.decile_2 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 2 | between_run_sd | 0.0496655480858378 | 0.052737041588958665 |
| 12 | qwen-3.7-max / labor_supply.policy_response.substitution_elasticity.primary.decile_2 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 2 | total_sd | 0.6405418398599042 | 0.6407873106577564 |
| 13 | qwen-3.7-max / labor_supply.policy_response.substitution_elasticity.primary.decile_3 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 3 | between_run_sd | 0.05148462553682086 | 0.0480446551542301 |
| 13 | qwen-3.7-max / labor_supply.policy_response.substitution_elasticity.primary.decile_3 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 3 | total_sd | 0.6354574325720891 | 0.6351879807059745 |
| 14 | qwen-3.7-max / labor_supply.policy_response.substitution_elasticity.primary.decile_4 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 4 | between_run_sd | 0.07858753081755401 | 0.07955390555396315 |
| 14 | qwen-3.7-max / labor_supply.policy_response.substitution_elasticity.primary.decile_4 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 4 | total_sd | 0.6361565124506181 | 0.6362766161208678 |
| 15 | qwen-3.7-max / labor_supply.policy_response.substitution_elasticity.primary.decile_5 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 5 | between_run_sd | 0.06447738621666772 | 0.0671826986656535 |
| 15 | qwen-3.7-max / labor_supply.policy_response.substitution_elasticity.primary.decile_5 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 5 | total_sd | 0.6412633591850804 | 0.6415410177845218 |
| 16 | qwen-3.7-max / labor_supply.policy_response.substitution_elasticity.primary.decile_6 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 6 | between_run_sd | 0.04062839729384691 | 0.03844181750819456 |
| 16 | qwen-3.7-max / labor_supply.policy_response.substitution_elasticity.primary.decile_6 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 6 | total_sd | 0.6379991118071143 | 0.6378636008844942 |
| 17 | qwen-3.7-max / labor_supply.policy_response.substitution_elasticity.primary.decile_7 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 7 | between_run_sd | 0.11298770827936207 | 0.1063141884541601 |
| 17 | qwen-3.7-max / labor_supply.policy_response.substitution_elasticity.primary.decile_7 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 7 | total_sd | 0.6414946728366323 | 0.6403529493351477 |
| 18 | qwen-3.7-max / labor_supply.policy_response.substitution_elasticity.primary.decile_8 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 8 | between_run_sd | 0.05264556539306569 | 0.04810299713462074 |
| 18 | qwen-3.7-max / labor_supply.policy_response.substitution_elasticity.primary.decile_8 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 8 | total_sd | 0.6356922582682774 | 0.6353321887013124 |
| 19 | qwen-3.7-max / labor_supply.policy_response.substitution_elasticity.primary.decile_9 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 9 | between_run_sd | 0.04654269246855216 | 0.042516611132852794 |
| 19 | qwen-3.7-max / labor_supply.policy_response.substitution_elasticity.primary.decile_9 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 9 | total_sd | 0.6367313786920754 | 0.6364497534064344 |
| 20 | qwen-3.7-max / labor_supply.policy_response.substitution_elasticity.secondary / Secondary-earner substitution elasticity in a tax-benefit simulation | between_run_sd | 0.06344201201797504 | 0.06179175151713662 |
| 20 | qwen-3.7-max / labor_supply.policy_response.substitution_elasticity.secondary / Secondary-earner substitution elasticity in a tax-benefit simulation | total_sd | 0.6843368251656328 | 0.6841858095170086 |
| 21 | qwen-3.7-max / macro.tfp_persistence.ar1 / TFP persistence | between_run_sd | 0.06236095644623236 | 0.057802459338297675 |
| 21 | qwen-3.7-max / macro.tfp_persistence.ar1 / TFP persistence | total_sd | 0.1477557540240725 | 0.14589036384864112 |
| 22 | qwen-3.7-max / production.capital_labor_substitution / Elasticity of substitution between capital and labor | between_run_sd | 0.04422166387140532 | 0.03758287139405694 |
| 22 | qwen-3.7-max / production.capital_labor_substitution / Elasticity of substitution between capital and labor | total_sd | 1.2504170276573954 | 1.2501998479132135 |
| 23 | qwen-3.7-max / production.capital_share / Capital share in production | between_run_sd | 0.010624918300339467 | 0.009944624455229865 |
| 23 | qwen-3.7-max / production.capital_share / Capital share in production | total_sd | 0.11106736569407874 | 0.1110043530177483 |
| 24 | qwen-3.7-max / tax.capital_gains_realizations.elasticity / Capital gains realizations elasticity | between_run_sd | 0.07483314773547883 | 0.0812649986156402 |
| 24 | qwen-3.7-max / tax.capital_gains_realizations.elasticity / Capital gains realizations elasticity | total_sd | 1.3520780302926307 | 1.35244925967668 |
| 25 | qwen-3.7-max / tax.capital_gains_realizations.elasticity.net_of_tax_rate / Capital gains realizations elasticity (net-of-tax-rate convention) | between_run_sd | 0.08055363982396382 | 0.09190899786685136 |
| 25 | qwen-3.7-max / tax.capital_gains_realizations.elasticity.net_of_tax_rate / Capital gains realizations elasticity (net-of-tax-rate convention) | total_sd | 1.3571540509667854 | 1.3578753599117837 |
| 26 | qwen-3.7-max / tax.elasticity_of_taxable_income.top_earners / Elasticity of taxable income | between_run_sd | 0.04827697864061778 | 0.0455142712661522 |
| 26 | qwen-3.7-max / tax.elasticity_of_taxable_income.top_earners / Elasticity of taxable income | total_sd | 0.6947945369755804 | 0.6946080411522266 |
| 27 | qwen-3.7-max / trade.armington_elasticity.import_domestic / Armington elasticity | between_run_sd | 0.1699673171197595 | 0.19329374594699705 |
| 27 | qwen-3.7-max / trade.armington_elasticity.import_domestic / Armington elasticity | total_sd | 2.589095126948581 | 2.590731008754522 |

## `results/qwen-3.7-max-ies-clarify-batch15/summary.csv` (2 cells)

| line | row | column | old | new |
|---|---|---|---|---|
| 2 | qwen-3.7-max / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | between_run_sd | 0.03118047822311618 | 0.044563924124041546 |
| 2 | qwen-3.7-max / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | total_sd | 0.7123118689247787 | 0.7130230849854878 |

## `results/qwen3.8-max-armington-clarify-batch15/summary.csv` (2 cells)

| line | row | column | old | new |
|---|---|---|---|---|
| 2 | qwen3.8-max / trade.armington_elasticity.import_domestic / Armington elasticity | between_run_sd | 0.1876758434701233 | 0.21621722616130498 |
| 2 | qwen3.8-max / trade.armington_elasticity.import_domestic / Armington elasticity | total_sd | 2.5362674893981074 | 2.5385390374080217 |

## `results/qwen3.8-max-elasticities-batch15/summary.csv` (52 cells)

| line | row | column | old | new |
|---|---|---|---|---|
| 2 | qwen3.8-max / household.annual_discount_factor / Annual discount factor | between_run_sd | 0.007483314773547889 | 0.00774489078898685 |
| 2 | qwen3.8-max / household.annual_discount_factor / Annual discount factor | total_sd | 0.12781410519231087 | 0.1278296867689366 |
| 3 | qwen3.8-max / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | between_run_sd | 0.1829996964174774 | 0.18957269200904323 |
| 3 | qwen3.8-max / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | total_sd | 0.7469524890067194 | 0.7485899662031278 |
| 4 | qwen3.8-max / household.relative_risk_aversion.crra / Coefficient of relative risk aversion | between_run_sd | 0.0 | 0.13273443620837652 |
| 4 | qwen3.8-max / household.relative_risk_aversion.crra / Coefficient of relative risk aversion | total_sd | 6.365117386213531 | 6.366501218945405 |
| 5 | qwen3.8-max / labor_supply.extensive_margin.single_mothers / Employment participation elasticity of single mothers | between_run_sd | 0.060184900284225976 | 0.05888851519797575 |
| 5 | qwen3.8-max / labor_supply.extensive_margin.single_mothers / Employment participation elasticity of single mothers | total_sd | 0.7161606091202976 | 0.716052828397148 |
| 6 | qwen3.8-max / labor_supply.frisch_elasticity.prime_age / Frisch elasticity of labor supply | between_run_sd | 0.06944222218666551 | 0.08170381808023963 |
| 6 | qwen3.8-max / labor_supply.frisch_elasticity.prime_age / Frisch elasticity of labor supply | total_sd | 1.3458876924006533 | 1.3465760179886699 |
| 7 | qwen3.8-max / labor_supply.income_elasticity.prime_age / Income elasticity of labor supply | between_run_sd | 0.011352924243950934 | 0.011909193460889318 |
| 7 | qwen3.8-max / labor_supply.income_elasticity.prime_age / Income elasticity of labor supply | total_sd | 0.30302938068041446 | 0.30305073099327046 |
| 8 | qwen3.8-max / labor_supply.marshallian_wage_elasticity.prime_age / Uncompensated wage elasticity of labor supply | between_run_sd | 0.03496029493900505 | 0.03884300308792935 |
| 8 | qwen3.8-max / labor_supply.marshallian_wage_elasticity.prime_age / Uncompensated wage elasticity of labor supply | total_sd | 0.6229318571169009 | 0.6231618211008901 |
| 9 | qwen3.8-max / labor_supply.policy_response.substitution_elasticity.all / Substitution elasticity of labor supply in a tax-benefit simulation | between_run_sd | 0.016996731711975945 | 0.022086320552675953 |
| 9 | qwen3.8-max / labor_supply.policy_response.substitution_elasticity.all / Substitution elasticity of labor supply in a tax-benefit simulation | total_sd | 0.6743162946850519 | 0.6744637736338731 |
| 10 | qwen3.8-max / labor_supply.policy_response.substitution_elasticity.primary.decile_1 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 1 | between_run_sd | 0.040144184579532255 | 0.048423261168804216 |
| 10 | qwen3.8-max / labor_supply.policy_response.substitution_elasticity.primary.decile_1 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 1 | total_sd | 0.6491188215145548 | 0.6496833852817163 |
| 11 | qwen3.8-max / labor_supply.policy_response.substitution_elasticity.primary.decile_10 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 10 | between_run_sd | 0.0590893861497609 | 0.06979818924744553 |
| 11 | qwen3.8-max / labor_supply.policy_response.substitution_elasticity.primary.decile_10 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 10 | total_sd | 0.6512649753023385 | 0.6523237690918691 |
| 12 | qwen3.8-max / labor_supply.policy_response.substitution_elasticity.primary.decile_2 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 2 | between_run_sd | 0.05450382249591919 | 0.06643546158156466 |
| 12 | qwen3.8-max / labor_supply.policy_response.substitution_elasticity.primary.decile_2 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 2 | total_sd | 0.6523973801807198 | 0.6535023684391323 |
| 13 | qwen3.8-max / labor_supply.policy_response.substitution_elasticity.primary.decile_3 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 3 | between_run_sd | 0.05339163480046913 | 0.05301615057906621 |
| 13 | qwen3.8-max / labor_supply.policy_response.substitution_elasticity.primary.decile_3 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 3 | total_sd | 0.6554035133242557 | 0.6553730318172494 |
| 14 | qwen3.8-max / labor_supply.policy_response.substitution_elasticity.primary.decile_4 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 4 | between_run_sd | 0.05706137047074842 | 0.061295246326466636 |
| 14 | qwen3.8-max / labor_supply.policy_response.substitution_elasticity.primary.decile_4 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 4 | total_sd | 0.6598921302842694 | 0.6602717098538551 |
| 15 | qwen3.8-max / labor_supply.policy_response.substitution_elasticity.primary.decile_5 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 5 | between_run_sd | 0.04730985333122713 | 0.05574044512041703 |
| 15 | qwen3.8-max / labor_supply.policy_response.substitution_elasticity.primary.decile_5 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 5 | total_sd | 0.6582394679918717 | 0.6588990607234331 |
| 16 | qwen3.8-max / labor_supply.policy_response.substitution_elasticity.primary.decile_6 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 6 | between_run_sd | 0.05838569078883018 | 0.06786717828883775 |
| 16 | qwen3.8-max / labor_supply.policy_response.substitution_elasticity.primary.decile_6 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 6 | total_sd | 0.6603828119608606 | 0.661288532588713 |
| 17 | qwen3.8-max / labor_supply.policy_response.substitution_elasticity.primary.decile_7 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 7 | between_run_sd | 0.05748043145279966 | 0.05022282570925519 |
| 17 | qwen3.8-max / labor_supply.policy_response.substitution_elasticity.primary.decile_7 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 7 | total_sd | 0.6525470513048593 | 0.6519478402363865 |
| 18 | qwen3.8-max / labor_supply.policy_response.substitution_elasticity.primary.decile_8 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 8 | between_run_sd | 0.04127953488110059 | 0.04721332792054945 |
| 18 | qwen3.8-max / labor_supply.policy_response.substitution_elasticity.primary.decile_8 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 8 | total_sd | 0.6575089617048746 | 0.6579081494065533 |
| 19 | qwen3.8-max / labor_supply.policy_response.substitution_elasticity.primary.decile_9 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 9 | between_run_sd | 0.04753478258660237 | 0.05052936439998694 |
| 19 | qwen3.8-max / labor_supply.policy_response.substitution_elasticity.primary.decile_9 / Primary-earner substitution elasticity in a tax-benefit simulation, decile 9 | total_sd | 0.6553207855275495 | 0.6555448062913439 |
| 20 | qwen3.8-max / labor_supply.policy_response.substitution_elasticity.secondary / Secondary-earner substitution elasticity in a tax-benefit simulation | between_run_sd | 0.10132456102380442 | 0.09423537316504646 |
| 20 | qwen3.8-max / labor_supply.policy_response.substitution_elasticity.secondary / Secondary-earner substitution elasticity in a tax-benefit simulation | total_sd | 0.6918221712742854 | 0.6908194811638968 |
| 21 | qwen3.8-max / macro.tfp_persistence.ar1 / TFP persistence | between_run_sd | 0.0699205898780101 | 0.07051341775388098 |
| 21 | qwen3.8-max / macro.tfp_persistence.ar1 / TFP persistence | total_sd | 0.17947922543044115 | 0.17971100566063158 |
| 22 | qwen3.8-max / production.capital_labor_substitution / Elasticity of substitution between capital and labor | between_run_sd | 0.10561986345169908 | 0.10115774260475019 |
| 22 | qwen3.8-max / production.capital_labor_substitution / Elasticity of substitution between capital and labor | total_sd | 1.2482887592175493 | 1.2479191318840426 |
| 23 | qwen3.8-max / production.capital_share / Capital share in production | between_run_sd | 0.004988876515698579 | 0.004404227766842024 |
| 23 | qwen3.8-max / production.capital_share / Capital share in production | total_sd | 0.11310705965785002 | 0.11308278064222589 |
| 24 | qwen3.8-max / tax.capital_gains_realizations.elasticity / Capital gains realizations elasticity | between_run_sd | 0.09467136138593692 | 0.09188639725225928 |
| 24 | qwen3.8-max / tax.capital_gains_realizations.elasticity / Capital gains realizations elasticity | total_sd | 1.3313618461101315 | 1.3311667095488495 |
| 25 | qwen3.8-max / tax.capital_gains_realizations.elasticity.net_of_tax_rate / Capital gains realizations elasticity (net-of-tax-rate convention) | between_run_sd | 0.09092121131323905 | 0.08333399999733336 |
| 25 | qwen3.8-max / tax.capital_gains_realizations.elasticity.net_of_tax_rate / Capital gains realizations elasticity (net-of-tax-rate convention) | total_sd | 1.354081830675926 | 1.3535935479513619 |
| 26 | qwen3.8-max / tax.elasticity_of_taxable_income.top_earners / Elasticity of taxable income | between_run_sd | 0.04349201714746692 | 0.04746386344718826 |
| 26 | qwen3.8-max / tax.elasticity_of_taxable_income.top_earners / Elasticity of taxable income | total_sd | 0.6864438817396349 | 0.6867069721180611 |
| 27 | qwen3.8-max / trade.armington_elasticity.import_domestic / Armington elasticity | between_run_sd | 0.12036980056845191 | 0.13454155698354156 |
| 27 | qwen3.8-max / trade.armington_elasticity.import_domestic / Armington elasticity | total_sd | 2.5446196848012037 | 2.5453294250341045 |

## `results/qwen3.8-max-ies-clarify-batch15/summary.csv` (2 cells)

| line | row | column | old | new |
|---|---|---|---|---|
| 2 | qwen3.8-max / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | between_run_sd | 0.17869900204906947 | 0.1849067437626029 |
| 2 | qwen3.8-max / household.intertemporal_elasticity_of_substitution / Intertemporal elasticity of substitution | total_sd | 0.7390938342547131 | 0.7406192452190862 |

## `paper/tables/armington-clarify-delta.md` (Markdown)

```diff
@@ -21 +21 @@
-| Gemini 3 Flash | 1.633 | 1.573 | -0.061 | [0.6512, 5.783] | [0, 5.903] |
+| Gemini 3 Flash | 1.633 | 1.573 | -0.061 | [0.6512, 5.783] | [0, 5.923] |
@@ -23,2 +23,2 @@
-| Gemini 3.1 Pro | 1.653 | 1.444 | -0.209 | [0.5471, 4.933] | [0, 5.592] |
-| Gemini 3.5 Flash | 1.753 | 1.387 | -0.367 | [0.6111, 5.062] | [0.5137, 3.815] |
+| Gemini 3.1 Pro | 1.653 | 1.444 | -0.209 | [0.5471, 4.933] | [0, 5.625] |
+| Gemini 3.5 Flash | 1.753 | 1.453 | -0.3 | [0.6111, 5.062] | [0.5137, 3.815] |
@@ -30 +30 @@
-| Inkling | 1.66 | 1.48 | -0.18 | [0.7158, 5.05] | [0, 5.681] |
+| Inkling | 1.713 | 1.48 | -0.233 | [0.7158, 5.05] | [0, 5.709] |
```

## `paper/tables/benchmark-comparison-labor-tax.md` (Markdown)

```diff
@@ -5 +5 @@
-| Capital gains realizations elasticity | [-1, -0.2] | 30 / 31 | -0.93 | 0.01 | Dowd, McClelland, and Muthitacharoen 2015; Burman and Randolph 1994; CBO/JCT medium-run convention |
+| Capital gains realizations elasticity | [-1, -0.2] | 31 / 31 | -0.93 | -0.327 | Dowd, McClelland, and Muthitacharoen 2015; Burman and Randolph 1994; CBO/JCT medium-run convention |
@@ -9 +9 @@
-| Income elasticity of labor supply | [-0.15, -0.05] | 26 / 31 | -0.107 | 0.011 | CBO 2012; Blundell and MaCurdy 1999; Imbens, Rubin, and Sacerdote 2001 (marginal propensity to earn, converted to an elasticity) |
+| Income elasticity of labor supply | [-0.15, -0.05] | 26 / 31 | -0.107 | -0.001 | CBO 2012; Blundell and MaCurdy 1999; Imbens, Rubin, and Sacerdote 2001 (marginal propensity to earn, converted to an elasticity) |
```

## `paper/tables/cap-gains-convention-audit.md` (Markdown)

```diff
@@ -24 +24 @@
-| Gemini 3.5 Flash | Google | -0.4 | 0.8 | 0.452 [-0.889, 3.250] | 65% | sign-consistent (tax<0, net>0) | uninformative (pole-straddling) |
+| Gemini 3.5 Flash | Google | -0.6 | 0.8 | 0.429 [0.200, 0.500] | 100% | sign-consistent (tax<0, net>0) | ordinary-income-rate consistent |
@@ -30,3 +30,3 @@
-| Inkling | Thinking Machines | -0.5 | 1 | 0.333 [0.200, 0.500] | 94% | sign-consistent (tax<0, net>0) | LTCG-rate consistent |
-| Kimi K2.6 | Moonshot AI | -0.5 | 0.65 | 0.400 [0.185, 0.560] | 94% | sign-consistent (tax<0, net>0) | ordinary-income-rate consistent |
-| Kimi K3 | Moonshot AI | -0.5 | 0.5 | 0.444 [0.143, 0.545] | 100% | sign-consistent (tax<0, net>0) | ordinary-income-rate consistent |
+| Inkling | Thinking Machines | -0.5 | 1 | 0.333 [0.211, 0.476] | 100% | sign-consistent (tax<0, net>0) | LTCG-rate consistent |
+| Kimi K2.6 | Moonshot AI | -0.5 | 0.65 | 0.381 [0.200, 0.542] | 100% | sign-consistent (tax<0, net>0) | ordinary-income-rate consistent |
+| Kimi K3 | Moonshot AI | -0.5 | 0.5 | 0.444 [0.190, 0.545] | 100% | sign-consistent (tax<0, net>0) | ordinary-income-rate consistent |
```

## `paper/tables/correlates-country.md` (Markdown)

```diff
@@ -5,5 +5,5 @@
-| Implied optimal top rate (%) | 35.843 (24) | 32.942 (7) | -2.901 | 0.126 | 0.209* | 0.139* |
-| ETI pooled median | 0.421 (24) | 0.479 (7) | +0.058 | 0.105 | 0.209 | 0.139 |
-| Avg interval-width rank (1 = tightest) | 13.789 (24) | 20.308 (7) | +6.519 | 0.029 | 0.107 | 0.057 |
-| Mean |center|, labor-and-tax | 0.368 (24) | 0.324 (7) | -0.044 | 0.027 | 0.107 | 0.057 |
-| Mean |center|, macro-and-trade | 1.162 (24) | 1.038 (7) | -0.124 | 0.169 | 0.209 | 0.169 |
+| Implied optimal top rate (%) | 35.843 (24) | 32.942 (7) | -2.901 | 0.126 | 0.237* | 0.139* |
+| ETI pooled median | 0.421 (24) | 0.479 (7) | +0.058 | 0.105 | 0.237 | 0.139 |
+| Avg interval-width rank (1 = tightest) | 13.865 (24) | 20.462 (7) | +6.596 | 0.055 | 0.222 | 0.139 |
+| Mean |center|, labor-and-tax | 0.368 (24) | 0.334 (7) | -0.034 | 0.079 | 0.237 | 0.139 |
+| Mean |center|, macro-and-trade | 1.162 (24) | 1.038 (7) | -0.124 | 0.168 | 0.237 | 0.168 |
```

## `paper/tables/correlates-model-summary.md` (Markdown)

```diff
@@ -5 +5 @@
-| Claude Opus 5 | Anthropic | July 2026 late | 79.8 | 0.337 | 41.2% | 13.0 |
+| Claude Opus 5 | Anthropic | July 2026 late | 79.8 | 0.337 | 41.2% | 13.1 |
@@ -7,2 +7,2 @@
-| Gemini 3.5 Flash | Google | July 2026 frontier | 76.2 | 0.357 | 39.8% | 13.3 |
-| GPT-5.5 | OpenAI | July 2026 frontier | 83.5 | 0.369 | 39.0% | 15.1 |
+| Gemini 3.5 Flash | Google | July 2026 frontier | 76.2 | 0.357 | 39.8% | 11.1 |
+| GPT-5.5 | OpenAI | July 2026 frontier | 83.5 | 0.369 | 39.0% | 15.3 |
@@ -10 +10 @@
-| Qwen 3.8 Max | Alibaba | August 2026 | 71.5 | 0.372 | 38.7% | 19.4 |
+| Qwen 3.8 Max | Alibaba | August 2026 | 71.5 | 0.372 | 38.7% | 19.5 |
@@ -12,4 +12,4 @@
-| Claude Opus 4.8 | Anthropic | July 2026 frontier | 72.6 | 0.383 | 38.0% | 11.0 |
-| Gemini 3.1 Flash-Lite | Google | April 2026 | 76.1 | 0.389 | 37.7% | 13.9 |
-| Claude Opus 4.7 | Anthropic | April 2026 | 77.4 | 0.400 | 37.0% | 9.5 |
-| Gemini 3 Flash | Google | April 2026 | 76.9 | 0.400 | 37.0% | 12.9 |
+| Claude Opus 4.8 | Anthropic | July 2026 frontier | 72.6 | 0.383 | 38.0% | 11.2 |
+| Gemini 3.1 Flash-Lite | Google | April 2026 | 76.1 | 0.389 | 37.7% | 14.2 |
+| Claude Opus 4.7 | Anthropic | April 2026 | 77.4 | 0.400 | 37.0% | 9.6 |
+| Gemini 3 Flash | Google | April 2026 | 76.9 | 0.400 | 37.0% | 13.0 |
@@ -17,4 +17,4 @@
-| Grok 4.5 | xAI | July 2026 late | 80.9 | 0.410 | 36.5% | 18.8 |
-| GPT-5.4 | OpenAI | April 2026 | — | 0.420 | 35.9% | 15.3 |
-| Gemini 3.6 Flash | Google | July 2026 late | 79.0 | 0.423 | 35.8% | 7.5 |
-| GPT-5.6 Sol | OpenAI | July 2026 GPT-5.6 | 88.7 | 0.431 | 35.3% | 17.4 |
+| Grok 4.5 | xAI | July 2026 late | 80.9 | 0.410 | 36.5% | 19.0 |
+| GPT-5.4 | OpenAI | April 2026 | — | 0.420 | 35.9% | 15.4 |
+| Gemini 3.6 Flash | Google | July 2026 late | 79.0 | 0.423 | 35.8% | 7.6 |
+| GPT-5.6 Sol | OpenAI | July 2026 GPT-5.6 | 88.7 | 0.431 | 35.3% | 17.5 |
@@ -22,7 +22,7 @@
-| Claude Fable 5 | Anthropic | July 2026 frontier | 79.9 | 0.437 | 35.0% | 6.8 |
-| Grok 4.3 | xAI | July 2026 frontier | 77.2 | 0.439 | 34.9% | 18.7 |
-| MiniMax M3 | MiniMax | July 2026 independent labs | 72.4 | 0.438 | 34.9% | 18.8 |
-| Inkling | Thinking Machines | August 2026 | 83.8 | 0.443 | 34.7% | 12.7 |
-| Claude Sonnet 5 | Anthropic | July 2026 frontier | 69.4 | 0.471 | 33.3% | 9.8 |
-| DeepSeek V4 Pro | DeepSeek | July 2026 independent labs | 76.1 | 0.479 | 32.9% | 20.4 |
-| GPT-5.6 Terra | OpenAI | July 2026 GPT-5.6 | 83.4 | 0.492 | 32.4% | 13.8 |
+| Claude Fable 5 | Anthropic | July 2026 frontier | 79.9 | 0.437 | 35.0% | 6.9 |
+| Grok 4.3 | xAI | July 2026 frontier | 77.2 | 0.439 | 34.9% | 18.8 |
+| MiniMax M3 | MiniMax | July 2026 independent labs | 72.4 | 0.438 | 34.9% | 19.0 |
+| Inkling | Thinking Machines | August 2026 | 83.8 | 0.443 | 34.7% | 12.1 |
+| Claude Sonnet 5 | Anthropic | July 2026 frontier | 69.4 | 0.471 | 33.3% | 10.0 |
+| DeepSeek V4 Pro | DeepSeek | July 2026 independent labs | 76.1 | 0.479 | 32.9% | 20.5 |
+| GPT-5.6 Terra | OpenAI | July 2026 GPT-5.6 | 83.4 | 0.492 | 32.4% | 13.9 |
@@ -30,4 +30,4 @@
-| Kimi K2.6 | Moonshot AI | July 2026 independent labs | 64.6 | 0.499 | 32.1% | 22.7 |
-| Claude Sonnet 4.6 | Anthropic | April 2026 | 77.1 | 0.500 | 32.0% | 13.7 |
-| Grok 4.20 | xAI | April 2026 | — | 0.500 | 32.0% | 23.8 |
-| Claude Haiku 4.5 | Anthropic | April 2026 | 71.7 | 0.502 | 31.9% | 9.3 |
+| Kimi K2.6 | Moonshot AI | July 2026 independent labs | 64.6 | 0.499 | 32.1% | 22.5 |
+| Claude Sonnet 4.6 | Anthropic | April 2026 | 77.1 | 0.500 | 32.0% | 13.8 |
+| Grok 4.20 | xAI | April 2026 | — | 0.500 | 32.0% | 24.0 |
+| Claude Haiku 4.5 | Anthropic | April 2026 | 71.7 | 0.502 | 31.9% | 9.4 |
@@ -35 +35 @@
-| Qwen 3.7 Max | Alibaba | July 2026 independent labs | 73.6 | 0.555 | 29.8% | 20.3 |
+| Qwen 3.7 Max | Alibaba | July 2026 independent labs | 73.6 | 0.555 | 29.8% | 20.5 |
```

## `paper/tables/ies-clarify-delta.md` (Markdown)

```diff
@@ -21 +21 @@
-| Gemini 3 Flash | 0.5 | 0.478 | -0.022 | [0.1, 1.979] | [0, 1.667] |
+| Gemini 3 Flash | 0.5 | 0.478 | -0.022 | [0.1, 1.979] | [0, 1.671] |
@@ -23,2 +23,2 @@
-| Gemini 3.1 Pro | 1.467 | 0.625 | -0.842 | [0.2857, 2.499] | [0, 1.767] |
-| Gemini 3.5 Flash | 0.933 | 0.567 | -0.367 | [0.07895, 2.11] | [0.1037, 1.899] |
+| Gemini 3.1 Pro | 1.467 | 0.625 | -0.842 | [0.2857, 2.499] | [0, 1.754] |
+| Gemini 3.5 Flash | 0.987 | 0.567 | -0.42 | [0.07895, 2.11] | [0.1037, 1.899] |
```

## `paper/tables/leave-one-organization-out-appendix.md` (Markdown)

```diff
@@ -5,2 +5,2 @@
-| Labor/tax | Alibaba | 0.999 | Claude Sonnet 4.6 | Claude Sonnet 4.6 | 1.833 |
-| Labor/tax | Anthropic | 0.994 | Grok 4.20 | Grok 4.20 | 6.167 |
+| Labor/tax | Alibaba | 0.999 | Claude Sonnet 4.6 | Claude Sonnet 4.6 | 1.667 |
+| Labor/tax | Anthropic | 0.993 | Grok 4.5 | Grok 4.5 | 6.167 |
@@ -9,4 +9,4 @@
-| Labor/tax | MiniMax | 1 | Claude Sonnet 4.6 | Claude Sonnet 4.6 | 0.833 |
-| Labor/tax | Moonshot AI | 0.999 | Claude Sonnet 4.6 | Claude Sonnet 4.6 | 2 |
-| Labor/tax | OpenAI | 0.997 | Claude Sonnet 4.6 | Claude Sonnet 4.6 | 5.667 |
-| Labor/tax | Thinking Machines | 0.999 | Claude Sonnet 4.6 | Claude Sonnet 4.6 | 1 |
+| Labor/tax | MiniMax | 1 | Claude Sonnet 4.6 | Claude Sonnet 4.6 | 0.5 |
+| Labor/tax | Moonshot AI | 0.999 | Claude Sonnet 4.6 | Claude Sonnet 4.6 | 1.667 |
+| Labor/tax | OpenAI | 0.997 | Claude Sonnet 4.6 | Claude Sonnet 4.6 | 5.583 |
+| Labor/tax | Thinking Machines | 1 | Claude Sonnet 4.6 | Claude Sonnet 4.6 | 0.917 |
@@ -14 +14 @@
-| Labor/tax | xAI | 0.998 | Claude Sonnet 4.6 | Claude Sonnet 4.6 | 3.5 |
+| Labor/tax | xAI | 0.998 | Claude Sonnet 4.6 | Claude Sonnet 4.6 | 3.333 |
@@ -21 +21 @@
-| Macro/trade | OpenAI | 0.995 | Grok 4.3 | Grok 4.20 | 7 |
+| Macro/trade | OpenAI | 0.995 | Grok 4.3 | Grok 4.3 | 7 |
@@ -24 +24 @@
-| Macro/trade | xAI | 0.999 | GPT-5.6 Luna | GPT-5.4 nano | 3.667 |
+| Macro/trade | xAI | 0.999 | GPT-5.6 Luna | GPT-5.6 Luna | 3.667 |
```

## `paper/tables/leave-one-provider-out-appendix.md` (Markdown)

```diff
@@ -5,2 +5,2 @@
-| Labor/tax | Alibaba | 0.999 | Claude Sonnet 4.6 | Claude Sonnet 4.6 | 1.833 |
-| Labor/tax | Anthropic | 0.994 | Grok 4.20 | Grok 4.20 | 6.167 |
+| Labor/tax | Alibaba | 0.999 | Claude Sonnet 4.6 | Claude Sonnet 4.6 | 1.667 |
+| Labor/tax | Anthropic | 0.993 | Grok 4.5 | Grok 4.5 | 6.167 |
@@ -9,4 +9,4 @@
-| Labor/tax | MiniMax | 1 | Claude Sonnet 4.6 | Claude Sonnet 4.6 | 0.833 |
-| Labor/tax | Moonshot AI | 0.999 | Claude Sonnet 4.6 | Claude Sonnet 4.6 | 2 |
-| Labor/tax | OpenAI | 0.997 | Claude Sonnet 4.6 | Claude Sonnet 4.6 | 5.667 |
-| Labor/tax | Thinking Machines | 0.999 | Claude Sonnet 4.6 | Claude Sonnet 4.6 | 1 |
+| Labor/tax | MiniMax | 1 | Claude Sonnet 4.6 | Claude Sonnet 4.6 | 0.5 |
+| Labor/tax | Moonshot AI | 0.999 | Claude Sonnet 4.6 | Claude Sonnet 4.6 | 1.667 |
+| Labor/tax | OpenAI | 0.997 | Claude Sonnet 4.6 | Claude Sonnet 4.6 | 5.583 |
+| Labor/tax | Thinking Machines | 1 | Claude Sonnet 4.6 | Claude Sonnet 4.6 | 0.917 |
@@ -14 +14 @@
-| Labor/tax | xAI | 0.998 | Claude Sonnet 4.6 | Claude Sonnet 4.6 | 3.5 |
+| Labor/tax | xAI | 0.998 | Claude Sonnet 4.6 | Claude Sonnet 4.6 | 3.333 |
@@ -21 +21 @@
-| Macro/trade | OpenAI | 0.995 | Grok 4.3 | Grok 4.20 | 7 |
+| Macro/trade | OpenAI | 0.995 | Grok 4.3 | Grok 4.3 | 7 |
@@ -24 +24 @@
-| Macro/trade | xAI | 0.999 | GPT-5.6 Luna | GPT-5.4 nano | 3.667 |
+| Macro/trade | xAI | 0.999 | GPT-5.6 Luna | GPT-5.6 Luna | 3.667 |
```

## `paper/tables/model-overview-labor-tax.md` (Markdown)

```diff
@@ -5,13 +5,13 @@
-| Claude Sonnet 4.6 | Anthropic | 8.25 | 15.83 | 0.428 | 0.978 | 100.0% | $0.0112 |
-| Grok 4.20 | xAI | 9.83 | 23.83 | 0.362 | 1.245 | 100.0% | $0.0092 |
-| Grok 4.5 | xAI | 10 | 17.17 | 0.387 | 1.049 | 100.0% | $0.0066 |
-| Qwen 3.7 Max | Alibaba | 10.83 | 23.83 | 0.429 | 1.262 | 100.0% | — |
-| GPT-5.6 Terra | OpenAI | 12.33 | 17.33 | 0.361 | 1.02 | 100.0% | — |
-| GLM-5.2 | Zhipu AI | 12.58 | 21 | 0.37 | 1.406 | 100.0% | — |
-| Grok 4.3 | xAI | 12.83 | 17.67 | 0.37 | 1.125 | 100.0% | $0.0018 |
-| Claude Haiku 4.5 | Anthropic | 13.33 | 11.67 | 0.369 | 0.911 | 100.0% | $0.0031 |
-| Inkling | Thinking Machines | 13.42 | 13.83 | 0.341 | 1.125 | 100.0% | — |
-| Kimi K3 | Moonshot AI | 14.58 | 18.5 | 0.357 | 1.035 | 100.0% | — |
-| Gemini 3 Flash | Google | 14.83 | 10 | 0.382 | 0.892 | 100.0% | $0.0009 |
-| GPT-5.4 | OpenAI | 15.08 | 16.33 | 0.411 | 1.243 | 100.0% | $0.0036 |
-| Claude Fable 5 | Anthropic | 15.5 | 6.17 | 0.376 | 0.812 | 100.0% | $0.0403 |
+| Claude Sonnet 4.6 | Anthropic | 8.25 | 16 | 0.428 | 0.978 | 100.0% | $0.0112 |
+| Grok 4.5 | xAI | 10 | 17.67 | 0.387 | 1.049 | 100.0% | $0.0066 |
+| Grok 4.20 | xAI | 10.17 | 24.33 | 0.362 | 1.245 | 100.0% | $0.0092 |
+| Qwen 3.7 Max | Alibaba | 10.83 | 24.33 | 0.429 | 1.262 | 100.0% | — |
+| Inkling | Thinking Machines | 12.42 | 12.5 | 0.36 | 0.921 | 100.0% | — |
+| GLM-5.2 | Zhipu AI | 12.58 | 21 | 0.369 | 1.406 | 100.0% | — |
+| GPT-5.6 Terra | OpenAI | 12.67 | 17.5 | 0.361 | 1.02 | 100.0% | — |
+| Grok 4.3 | xAI | 12.83 | 18 | 0.37 | 1.125 | 100.0% | $0.0018 |
+| Claude Haiku 4.5 | Anthropic | 13.33 | 11.83 | 0.369 | 0.911 | 100.0% | $0.0031 |
+| Gemini 3 Flash | Google | 14.83 | 10.17 | 0.382 | 0.892 | 100.0% | $0.0009 |
+| Kimi K3 | Moonshot AI | 15.08 | 18.5 | 0.357 | 1.035 | 100.0% | — |
+| GPT-5.4 | OpenAI | 15.17 | 16.5 | 0.411 | 1.243 | 100.0% | $0.0036 |
+| Claude Fable 5 | Anthropic | 15.5 | 6.33 | 0.376 | 0.812 | 100.0% | $0.0403 |
@@ -19,7 +19,7 @@
-| Claude Opus 4.7 | Anthropic | 15.75 | 9.83 | 0.394 | 0.93 | 100.0% | $0.0221 |
-| Claude Opus 4.8 | Anthropic | 15.83 | 10.5 | 0.391 | 0.902 | 100.0% | $0.0146 |
-| GPT-5.4 nano | OpenAI | 16.17 | 19.5 | 0.313 | 1.086 | 100.0% | $0.0003 |
-| Qwen 3.8 Max | Alibaba | 16.58 | 19.5 | 0.321 | 1.129 | 100.0% | — |
-| Claude Opus 5 | Anthropic | 16.83 | 14.5 | 0.381 | 0.986 | 100.0% | — |
-| Kimi K2.6 | Moonshot AI | 16.92 | 20.33 | 0.324 | 1.205 | 100.0% | — |
-| DeepSeek V4 Pro | DeepSeek | 17 | 20.67 | 0.312 | 1.158 | 100.0% | — |
+| Claude Opus 4.7 | Anthropic | 15.75 | 10.17 | 0.394 | 0.93 | 100.0% | $0.0221 |
+| Claude Opus 4.8 | Anthropic | 15.83 | 10.83 | 0.391 | 0.902 | 100.0% | $0.0146 |
+| GPT-5.4 nano | OpenAI | 16.5 | 19.5 | 0.313 | 1.086 | 100.0% | $0.0003 |
+| Claude Opus 5 | Anthropic | 16.83 | 14.67 | 0.381 | 0.986 | 100.0% | — |
+| Kimi K2.6 | Moonshot AI | 17 | 20 | 0.334 | 1.102 | 100.0% | — |
+| Qwen 3.8 Max | Alibaba | 17.08 | 19.67 | 0.321 | 1.129 | 100.0% | — |
+| DeepSeek V4 Pro | DeepSeek | 17.33 | 20.83 | 0.312 | 1.158 | 100.0% | — |
@@ -27 +27 @@
-| GPT-5.6 Sol | OpenAI | 17.75 | 12.83 | 0.339 | 0.938 | 100.0% | — |
+| GPT-5.6 Sol | OpenAI | 17.58 | 13 | 0.339 | 0.938 | 100.0% | — |
@@ -29,7 +29,7 @@
-| Claude Sonnet 5 | Anthropic | 18.08 | 8.67 | 0.367 | 0.893 | 100.0% | $0.0068 |
-| Gemini 3.1 Flash-Lite | Google | 18.42 | 11.33 | 0.367 | 1.022 | 100.0% | $0.0007 |
-| GPT-5.6 Luna | OpenAI | 19.92 | 26.83 | 0.318 | 1.554 | 100.0% | — |
-| Gemini 3.6 Flash | Google | 21.17 | 6.5 | 0.348 | 0.819 | 100.0% | $0.0080 |
-| MiniMax M3 | MiniMax | 21.42 | 22.67 | 0.3 | 1.154 | 100.0% | — |
-| GPT-5.5 | OpenAI | 23.17 | 9.5 | 0.328 | 0.917 | 100.0% | $0.0159 |
-| Gemini 3.5 Flash | Google | 26.5 | 11.67 | 0.218 | 1.059 | 100.0% | $0.0126 |
+| Claude Sonnet 5 | Anthropic | 18.08 | 9 | 0.367 | 0.893 | 100.0% | $0.0068 |
+| Gemini 3.1 Flash-Lite | Google | 18.42 | 12 | 0.367 | 1.022 | 100.0% | $0.0007 |
+| GPT-5.6 Luna | OpenAI | 19.75 | 26.83 | 0.318 | 1.554 | 100.0% | — |
+| Gemini 3.6 Flash | Google | 21 | 6.83 | 0.348 | 0.819 | 100.0% | $0.0080 |
+| MiniMax M3 | MiniMax | 21.75 | 23.17 | 0.3 | 1.154 | 100.0% | — |
+| GPT-5.5 | OpenAI | 23.17 | 10 | 0.328 | 0.917 | 100.0% | $0.0159 |
+| Gemini 3.5 Flash | Google | 25.17 | 6.83 | 0.309 | 0.841 | 100.0% | $0.0126 |
```

## `paper/tables/model-overview-macro-trade.md` (Markdown)

```diff
@@ -6,2 +6,2 @@
-| Grok 4.20 | xAI | 6.83 | 28.33 | 1.257 | 3.986 | 100.0% | $0.0089 |
-| GPT-5.6 Luna | OpenAI | 7.5 | 29 | 1.291 | 4.144 | 100.0% | — |
+| Grok 4.20 | xAI | 7.17 | 28.33 | 1.257 | 3.986 | 100.0% | $0.0089 |
+| GPT-5.6 Luna | OpenAI | 7.17 | 29 | 1.291 | 4.144 | 100.0% | — |
@@ -12,3 +12,3 @@
-| Gemini 3.5 Flash | Google | 10.5 | 15 | 1.153 | 2.473 | 100.0% | $0.0104 |
-| Grok 4.5 | xAI | 11.33 | 24.67 | 1.344 | 3.446 | 100.0% | $0.0065 |
-| Kimi K2.6 | Moonshot AI | 12 | 26 | 1.11 | 3.23 | 100.0% | — |
+| Gemini 3.5 Flash | Google | 10.67 | 15 | 1.16 | 2.473 | 100.0% | $0.0104 |
+| Grok 4.5 | xAI | 11.5 | 24.67 | 1.344 | 3.446 | 100.0% | $0.0065 |
+| Kimi K2.6 | Moonshot AI | 11.67 | 26 | 1.11 | 3.23 | 100.0% | — |
@@ -20 +20 @@
-| Inkling | Thinking Machines | 16 | 17 | 1.069 | 2.457 | 100.0% | — |
+| Inkling | Thinking Machines | 16 | 17 | 1.087 | 2.457 | 100.0% | — |
```

## `paper/tables/model-overview-simulation.md` (Markdown)

```diff
@@ -16 +16 @@
-| Claude Haiku 4.5 | Anthropic | 12.5 | 21.08 | 0.247 | 0.678 | 100.0% | $0.0031 |
+| Claude Haiku 4.5 | Anthropic | 12.58 | 21.08 | 0.247 | 0.678 | 100.0% | $0.0031 |
@@ -18 +18,2 @@
-| Kimi K2.6 | Moonshot AI | 13.5 | 22.25 | 0.24 | 0.707 | 100.0% | — |
+| Kimi K2.6 | Moonshot AI | 13.58 | 22.25 | 0.24 | 0.707 | 100.0% | — |
+| Inkling | Thinking Machines | 16.5 | 6.33 | 0.224 | 0.473 | 100.0% | — |
@@ -20 +20,0 @@
-| Inkling | Thinking Machines | 16.71 | 6.33 | 0.224 | 0.473 | 100.0% | — |
@@ -23,2 +23,2 @@
-| Claude Fable 5 | Anthropic | 17.83 | 3.25 | 0.222 | 0.42 | 100.0% | $0.0468 |
-| Gemini 3.1 Pro | Google | 18.79 | 3.75 | 0.216 | 0.432 | 100.0% | $0.0078 |
+| Claude Fable 5 | Anthropic | 17.88 | 3.25 | 0.222 | 0.42 | 100.0% | $0.0468 |
+| Gemini 3.1 Pro | Google | 18.88 | 3.75 | 0.216 | 0.432 | 100.0% | $0.0078 |
@@ -26 +26 @@
-| GPT-5.6 Sol | OpenAI | 19.25 | 11.67 | 0.211 | 0.536 | 100.0% | — |
+| GPT-5.6 Sol | OpenAI | 19.38 | 11.67 | 0.211 | 0.536 | 100.0% | — |
@@ -28 +28 @@
-| Qwen 3.8 Max | Alibaba | 21.92 | 26.92 | 0.196 | 0.872 | 100.0% | — |
+| Qwen 3.8 Max | Alibaba | 22.08 | 26.92 | 0.196 | 0.872 | 100.0% | — |
@@ -31 +31 @@
-| MiniMax M3 | MiniMax | 25.08 | 17 | 0.173 | 0.657 | 100.0% | — |
+| MiniMax M3 | MiniMax | 24.71 | 17 | 0.174 | 0.657 | 100.0% | — |
@@ -33,3 +33,3 @@
-| Gemini 3 Flash | Google | 27.17 | 8.58 | 0.163 | 0.503 | 100.0% | $0.0010 |
-| Gemini 3.5 Flash | Google | 27.46 | 4.25 | 0.165 | 0.446 | 100.0% | $0.0100 |
-| Gemini 3.1 Flash-Lite | Google | 28.75 | 6.17 | 0.13 | 0.456 | 100.0% | $0.0008 |
+| Gemini 3 Flash | Google | 27.25 | 8.58 | 0.163 | 0.503 | 100.0% | $0.0010 |
+| Gemini 3.5 Flash | Google | 27.29 | 4.25 | 0.167 | 0.446 | 100.0% | $0.0100 |
+| Gemini 3.1 Flash-Lite | Google | 28.83 | 6.17 | 0.13 | 0.456 | 100.0% | $0.0008 |
```

## `paper/tables/policybench-correlates.md` (Markdown)

```diff
@@ -5,3 +5,3 @@
-| Tax within-$1 (domain-matched) | Mean |center|, labor-and-tax | 28 | 0.085 | 0.665 | 1.000 | 0.760 | 8 | no |
-| Tax within-$1 (domain-matched) | Mean |center|, macro-and-trade | 28 | 0.236 | 0.227 | 1.000 | 0.453 | 8 | no |
-| Tax within-$1 (domain-matched) | Avg interval-width rank (1 = tightest) | 28 | -0.274 | 0.158 | 0.949 | 0.422 | 8 | no |
+| Tax within-$1 (domain-matched) | Mean |center|, labor-and-tax | 28 | 0.074 | 0.704 | 1.000 | 0.805 | 8 | no |
+| Tax within-$1 (domain-matched) | Mean |center|, macro-and-trade | 28 | 0.237 | 0.223 | 1.000 | 0.446 | 8 | no |
+| Tax within-$1 (domain-matched) | Avg interval-width rank (1 = tightest) | 28 | -0.254 | 0.193 | 1.000 | 0.446 | 8 | no |
@@ -10,3 +10,3 @@
-| Overall within-$1 (leaderboard headline) | Mean |center|, labor-and-tax | 28 | 0.021 | 0.915 | 1.000 | 0.915 | 8 | no |
-| Overall within-$1 (leaderboard headline) | Mean |center|, macro-and-trade | 28 | 0.115 | 0.555 | 1.000 | 0.739 | 8 | no |
-| Overall within-$1 (leaderboard headline) | Avg interval-width rank (1 = tightest) | 28 | -0.180 | 0.357 | 1.000 | 0.571 | 8 | no |
+| Overall within-$1 (leaderboard headline) | Mean |center|, labor-and-tax | 28 | 0.014 | 0.942 | 1.000 | 0.942 | 8 | no |
+| Overall within-$1 (leaderboard headline) | Mean |center|, macro-and-trade | 28 | 0.118 | 0.546 | 1.000 | 0.728 | 8 | no |
+| Overall within-$1 (leaderboard headline) | Avg interval-width rank (1 = tightest) | 28 | -0.167 | 0.394 | 1.000 | 0.630 | 8 | no |
```

## `paper/tables/pooling-robustness-appendix.md` (Markdown)

```diff
@@ -5,31 +5,31 @@
-| Claude Fable 5 | 6.85 | 7.73 | 7 | 0.88 |
-| Gemini 3.6 Flash | 7.46 | 10.23 | 9.12 | 2.77 |
-| Claude Haiku 4.5 | 9.31 | 8.38 | 8.23 | 1.08 |
-| Claude Opus 4.7 | 9.46 | 13.15 | 11.77 | 3.69 |
-| Claude Sonnet 5 | 9.77 | 12.15 | 11.46 | 2.38 |
-| Claude Opus 4.8 | 11.04 | 14.42 | 13.77 | 3.38 |
-| Gemini 3.1 Pro | 11.19 | 9.85 | 10.15 | 1.35 |
-| Inkling | 12.69 | 11 | 12.15 | 1.69 |
-| Gemini 3 Flash | 12.92 | 13 | 12 | 1 |
-| Claude Opus 5 | 13 | 14.15 | 13.08 | 1.15 |
-| Gemini 3.5 Flash | 13.31 | 15.69 | 17.15 | 3.85 |
-| Claude Sonnet 4.6 | 13.77 | 18.31 | 17.23 | 4.54 |
-| GPT-5.6 Terra | 13.85 | 14.46 | 15.38 | 1.54 |
-| Gemini 3.1 Flash-Lite | 13.92 | 14.12 | 13.69 | 0.42 |
-| GPT-5.5 | 15.08 | 17.77 | 16.77 | 2.69 |
-| GPT-5.4 | 15.31 | 18.38 | 17.38 | 3.08 |
-| GPT-5.6 Sol | 17.38 | 19.46 | 19 | 2.08 |
-| Grok 4.3 | 18.69 | 18.19 | 17.69 | 1 |
-| GPT-5.4 nano | 18.77 | 16.23 | 18.15 | 2.54 |
-| Kimi K3 | 18.77 | 18.31 | 18.69 | 0.46 |
-| MiniMax M3 | 18.77 | 14.31 | 17.38 | 4.46 |
-| Grok 4.5 | 18.85 | 19.46 | 18.04 | 1.42 |
-| Grok 4.1 Fast | 19.19 | 17.92 | 17.5 | 1.69 |
-| Qwen 3.8 Max | 19.38 | 18.19 | 18.46 | 1.19 |
-| Qwen 3.7 Max | 20.31 | 18.42 | 18.81 | 1.88 |
-| DeepSeek V4 Pro | 20.38 | 16.23 | 18.31 | 4.15 |
-| GLM-5.2 | 20.85 | 17 | 18.5 | 3.85 |
-| Kimi K2.6 | 22.69 | 19.31 | 20.08 | 3.38 |
-| GPT-5.4 mini | 23.12 | 21.31 | 21.27 | 1.85 |
-| Grok 4.20 | 23.77 | 23 | 22.23 | 1.54 |
-| GPT-5.6 Luna | 26.15 | 25.85 | 25.54 | 0.62 |
+| Claude Fable 5 | 6.92 | 7.81 | 7.23 | 0.88 |
+| Gemini 3.6 Flash | 7.62 | 10.46 | 9.27 | 2.85 |
+| Claude Haiku 4.5 | 9.38 | 8.62 | 8.46 | 0.92 |
+| Claude Opus 4.7 | 9.62 | 13.38 | 11.92 | 3.77 |
+| Claude Sonnet 5 | 9.92 | 12.46 | 11.62 | 2.54 |
+| Gemini 3.5 Flash | 11.08 | 13.31 | 14 | 2.92 |
+| Claude Opus 4.8 | 11.19 | 14.73 | 13.92 | 3.54 |
+| Gemini 3.1 Pro | 11.19 | 10 | 10.31 | 1.19 |
+| Inkling | 12.08 | 9.23 | 9.85 | 2.85 |
+| Gemini 3 Flash | 13 | 13.31 | 12.23 | 1.08 |
+| Claude Opus 5 | 13.08 | 14.38 | 13.23 | 1.31 |
+| Claude Sonnet 4.6 | 13.85 | 18.38 | 17.54 | 4.54 |
+| GPT-5.6 Terra | 13.92 | 14.62 | 15.62 | 1.69 |
+| Gemini 3.1 Flash-Lite | 14.23 | 14.42 | 14 | 0.42 |
+| GPT-5.5 | 15.31 | 18.08 | 17 | 2.77 |
+| GPT-5.4 | 15.38 | 18.62 | 17.77 | 3.23 |
+| GPT-5.6 Sol | 17.46 | 19.62 | 19.15 | 2.15 |
+| GPT-5.4 nano | 18.77 | 16.23 | 18.23 | 2.54 |
+| Kimi K3 | 18.77 | 18.38 | 19 | 0.62 |
+| Grok 4.3 | 18.85 | 18.35 | 18 | 0.85 |
+| MiniMax M3 | 19 | 14.15 | 17.69 | 4.85 |
+| Grok 4.5 | 19.08 | 19.69 | 18.27 | 1.42 |
+| Grok 4.1 Fast | 19.19 | 18.08 | 17.73 | 1.46 |
+| Qwen 3.8 Max | 19.46 | 18.35 | 18.62 | 1.12 |
+| DeepSeek V4 Pro | 20.46 | 16.23 | 18.69 | 4.23 |
+| Qwen 3.7 Max | 20.54 | 18.58 | 19.12 | 1.96 |
+| GLM-5.2 | 20.85 | 17.23 | 18.81 | 3.62 |
+| Kimi K2.6 | 22.54 | 18.54 | 19 | 4 |
+| GPT-5.4 mini | 23.12 | 21.54 | 21.58 | 1.58 |
+| Grok 4.20 | 24 | 23.23 | 22.38 | 1.62 |
+| GPT-5.6 Luna | 26.15 | 26 | 25.77 | 0.38 |
```

## `paper/tables/quantile-rule-appendix.md` (Markdown)

```diff
@@ -5,6 +5,6 @@
-| Claude Fable 5 | 6.85 | 8.15 | 1.31 |
-| Gemini 3.6 Flash | 7.46 | 9.31 | 1.85 |
-| Claude Haiku 4.5 | 9.31 | 8.23 | -1.08 |
-| Claude Opus 4.7 | 9.46 | 13.38 | 3.92 |
-| Claude Sonnet 5 | 9.77 | 12.08 | 2.31 |
-| Claude Opus 4.8 | 11.04 | 14.42 | 3.38 |
+| Claude Fable 5 | 6.92 | 8.23 | 1.31 |
+| Gemini 3.6 Flash | 7.62 | 9.46 | 1.85 |
+| Claude Haiku 4.5 | 9.38 | 8.46 | -0.92 |
+| Claude Opus 4.7 | 9.62 | 13.62 | 4 |
+| Claude Sonnet 5 | 9.92 | 12.31 | 2.38 |
+| Gemini 3.5 Flash | 11.08 | 13 | 1.92 |
@@ -12,11 +12,10 @@
-| Inkling | 12.69 | 11.69 | -1 |
-| Gemini 3 Flash | 12.92 | 12.62 | -0.31 |
-| Claude Opus 5 | 13 | 14.38 | 1.38 |
-| Gemini 3.5 Flash | 13.31 | 14.46 | 1.15 |
-| Claude Sonnet 4.6 | 13.77 | 18.19 | 4.42 |
-| GPT-5.6 Terra | 13.85 | 14.08 | 0.23 |
-| Gemini 3.1 Flash-Lite | 13.92 | 13.77 | -0.15 |
-| GPT-5.5 | 15.08 | 17.38 | 2.31 |
-| GPT-5.4 | 15.31 | 16.77 | 1.46 |
-| GPT-5.6 Sol | 17.38 | 19.62 | 2.23 |
-| Grok 4.3 | 18.69 | 18.15 | -0.54 |
+| Claude Opus 4.8 | 11.19 | 14.73 | 3.54 |
+| Inkling | 12.08 | 9.77 | -2.31 |
+| Gemini 3 Flash | 13 | 12.77 | -0.23 |
+| Claude Opus 5 | 13.08 | 14.62 | 1.54 |
+| Claude Sonnet 4.6 | 13.85 | 18.35 | 4.5 |
+| GPT-5.6 Terra | 13.92 | 14.15 | 0.23 |
+| Gemini 3.1 Flash-Lite | 14.23 | 14.08 | -0.15 |
+| GPT-5.5 | 15.31 | 17.69 | 2.38 |
+| GPT-5.4 | 15.38 | 17 | 1.62 |
+| GPT-5.6 Sol | 17.46 | 19.69 | 2.23 |
@@ -24,7 +23,8 @@
-| MiniMax M3 | 18.77 | 13.85 | -4.92 |
-| Kimi K3 | 18.77 | 18.46 | -0.31 |
-| Grok 4.5 | 18.85 | 19.08 | 0.23 |
-| Grok 4.1 Fast | 19.19 | 17.31 | -1.88 |
-| Qwen 3.8 Max | 19.38 | 18.15 | -1.23 |
-| Qwen 3.7 Max | 20.31 | 17.85 | -2.46 |
-| DeepSeek V4 Pro | 20.38 | 16.62 | -3.77 |
+| Kimi K3 | 18.77 | 18.54 | -0.23 |
+| Grok 4.3 | 18.85 | 18.38 | -0.46 |
+| MiniMax M3 | 19 | 13.85 | -5.15 |
+| Grok 4.5 | 19.08 | 19.31 | 0.23 |
+| Grok 4.1 Fast | 19.19 | 17.46 | -1.73 |
+| Qwen 3.8 Max | 19.46 | 18.23 | -1.23 |
+| DeepSeek V4 Pro | 20.46 | 16.69 | -3.77 |
+| Qwen 3.7 Max | 20.54 | 18 | -2.54 |
@@ -32 +32 @@
-| Kimi K2.6 | 22.69 | 19.31 | -3.38 |
+| Kimi K2.6 | 22.54 | 18.69 | -3.85 |
@@ -34 +34 @@
-| Grok 4.20 | 23.77 | 23.08 | -0.69 |
+| Grok 4.20 | 24 | 23.31 | -0.69 |
```

## `paper/tables/quantity-disagreement.md` (Markdown)

```diff
@@ -7 +7 @@
-| Capital gains realizations elasticity | GPT-5.4 mini | -0.93 | Gemini 3.5 Flash | 0.01 | 0.94 | 1.894 | 0.496 |
+| Capital gains realizations elasticity | GPT-5.4 mini | -0.93 | MiniMax M3 | -0.327 | 0.603 | 1.797 | 0.335 |
@@ -15 +15 @@
-| Income elasticity of labor supply | Grok 4.20 | -0.107 | Gemini 3.5 Flash | 0.011 | 0.118 | 0.377 | 0.312 |
+| Income elasticity of labor supply | Grok 4.20 | -0.107 | GPT-5.4 nano | -0.001 | 0.106 | 0.373 | 0.284 |
```

## `paper/tables/resampling-stability.md` (Markdown)

```diff
@@ -5,19 +5,19 @@
-| Claude Fable 5 | 0.003 | 3% | 7.44 | [6.62, 8.08] |
-| Gemini 3.6 Flash | 0.006 | 2% | 7.83 | [7.08, 8.54] |
-| Claude Haiku 4.5 | 0.005 | 5% | 9.2 | [8.31, 10.00] |
-| Claude Opus 4.7 | 0 | 2% | 10.07 | [9.15, 10.85] |
-| Claude Sonnet 5 | 0.003 | 2% | 10.34 | [9.69, 11.08] |
-| Gemini 3.1 Pro | 0.006 | 2% | 11.06 | [10.30, 11.69] |
-| Claude Opus 4.8 | 0 | 1% | 11.4 | [10.69, 12.08] |
-| Inkling | 0.014 | 4% | 12.37 | [10.85, 13.39] |
-| Gemini 3 Flash | 0 | 1% | 13.11 | [12.38, 13.77] |
-| Gemini 3.5 Flash | 0.01 | 3% | 13.48 | [12.84, 14.08] |
-| Claude Opus 5 | 0.008 | 3% | 13.67 | [12.85, 14.46] |
-| GPT-5.6 Terra | 0.004 | 3% | 13.73 | [12.69, 14.69] |
-| Gemini 3.1 Flash-Lite | 0.006 | 5% | 13.94 | [12.92, 14.85] |
-| Claude Sonnet 4.6 | 0 | 1% | 14.27 | [13.46, 15.23] |
-| GPT-5.5 | 0.005 | 2% | 15.4 | [14.85, 16.00] |
-| GPT-5.4 | 0 | 3% | 15.49 | [14.54, 16.23] |
-| GPT-5.6 Sol | 0.008 | 3% | 17.57 | [16.69, 18.31] |
-| MiniMax M3 | 0.016 | 9% | 18.04 | [16.38, 19.38] |
-| Kimi K3 | 0.008 | 3% | 18.69 | [17.69, 19.62] |
+| Claude Fable 5 | 0.003 | 3% | 7.53 | [6.77, 8.16] |
+| Gemini 3.6 Flash | 0.006 | 2% | 8 | [7.30, 8.69] |
+| Claude Haiku 4.5 | 0.005 | 5% | 9.3 | [8.38, 10.08] |
+| Claude Opus 4.7 | 0 | 2% | 10.25 | [9.31, 11.08] |
+| Claude Sonnet 5 | 0.003 | 2% | 10.52 | [9.84, 11.31] |
+| Gemini 3.1 Pro | 0.006 | 2% | 11.05 | [10.30, 11.69] |
+| Gemini 3.5 Flash | 0.004 | 2% | 11.25 | [10.54, 11.85] |
+| Claude Opus 4.8 | 0 | 1% | 11.57 | [10.92, 12.23] |
+| Inkling | 0.014 | 4% | 11.71 | [10.46, 12.85] |
+| Gemini 3 Flash | 0 | 1% | 13.21 | [12.46, 13.92] |
+| Claude Opus 5 | 0.008 | 3% | 13.78 | [13.00, 14.62] |
+| GPT-5.6 Terra | 0.004 | 3% | 13.82 | [12.77, 14.85] |
+| Gemini 3.1 Flash-Lite | 0.006 | 5% | 14.16 | [13.08, 15.08] |
+| Claude Sonnet 4.6 | 0 | 1% | 14.36 | [13.53, 15.38] |
+| GPT-5.4 | 0 | 3% | 15.58 | [14.62, 16.31] |
+| GPT-5.5 | 0.005 | 2% | 15.59 | [15.07, 16.23] |
+| GPT-5.6 Sol | 0.008 | 3% | 17.67 | [16.77, 18.38] |
+| MiniMax M3 | 0.016 | 9% | 18.18 | [16.38, 19.62] |
+| Kimi K3 | 0.008 | 3% | 18.74 | [17.77, 19.69] |
@@ -25,10 +25,10 @@
-| Grok 4.1 Fast | 0 | 2% | 18.83 | [17.38, 20.15] |
-| Qwen 3.8 Max | 0.016 | 7% | 19.04 | [17.76, 20.16] |
-| Grok 4.5 | 0.009 | 3% | 19.05 | [18.08, 19.92] |
-| Grok 4.3 | 0.012 | 5% | 19.24 | [18.31, 20.23] |
-| Qwen 3.7 Max | 0.012 | 8% | 19.35 | [17.60, 20.77] |
-| GLM-5.2 | 0.017 | 7% | 19.83 | [18.46, 21.31] |
-| DeepSeek V4 Pro | 0.014 | 7% | 19.88 | [18.62, 21.08] |
-| Kimi K2.6 | 0.027 | 5% | 21.69 | [20.15, 22.92] |
-| GPT-5.4 mini | 0.009 | 4% | 22.98 | [22.07, 23.77] |
-| Grok 4.20 | 0.011 | 3% | 24.1 | [23.30, 24.77] |
+| Grok 4.1 Fast | 0 | 2% | 18.87 | [17.38, 20.16] |
+| Qwen 3.8 Max | 0.016 | 7% | 19.13 | [17.84, 20.23] |
+| Grok 4.5 | 0.009 | 3% | 19.21 | [18.23, 20.00] |
+| Grok 4.3 | 0.012 | 5% | 19.38 | [18.46, 20.38] |
+| Qwen 3.7 Max | 0.012 | 8% | 19.5 | [17.76, 20.93] |
+| GLM-5.2 | 0.017 | 7% | 19.87 | [18.46, 21.31] |
+| DeepSeek V4 Pro | 0.014 | 7% | 19.98 | [18.69, 21.15] |
+| Kimi K2.6 | 0.027 | 4% | 21.6 | [20.15, 22.77] |
+| GPT-5.4 mini | 0.009 | 4% | 22.99 | [22.07, 23.77] |
+| Grok 4.20 | 0.011 | 3% | 24.27 | [23.46, 25.00] |
```

## `paper/tables/stability-appendix.md` (Markdown)

```diff
@@ -5,2 +5,2 @@
-| 5 | 403 | 0.006 | 0.048 | 0.028 | 0.269 |
-| 10 | 403 | 0.003 | 0.025 | 0.01 | 0.134 |
+| 5 | 403 | 0.006 | 0.043 | 0.028 | 0.249 |
+| 10 | 403 | 0.002 | 0.023 | 0.01 | 0.13 |
```

## `paper/tables/variance-decomposition.md` (Markdown)

```diff
@@ -5,31 +5,31 @@
-| Claude Fable 5 | 13 | 0.679 | 0.012 | 0% | 1% |
-| Claude Haiku 4.5 | 13 | 0.672 | 0.018 | 0% | 4% |
-| Claude Opus 4.7 | 13 | 0.704 | 0 | 0% | 0% |
-| Claude Opus 4.8 | 13 | 0.72 | 0 | 0% | 1% |
-| Claude Opus 5 | 13 | 0.733 | 0.029 | 0% | 1% |
-| Claude Sonnet 4.6 | 13 | 0.726 | 0 | 0% | 1% |
-| Claude Sonnet 5 | 13 | 0.699 | 0.01 | 0% | 1% |
-| DeepSeek V4 Pro | 13 | 0.738 | 0.054 | 1% | 4% |
-| GLM-5.2 | 13 | 0.683 | 0.06 | 1% | 13% |
-| GPT-5.4 | 13 | 0.684 | 0 | 0% | 1% |
-| GPT-5.4 mini | 13 | 0.713 | 0.034 | 1% | 5% |
-| GPT-5.4 nano | 13 | 0.699 | 0.098 | 2% | 29% |
-| GPT-5.5 | 13 | 0.703 | 0.018 | 0% | 1% |
-| GPT-5.6 Luna | 13 | 0.727 | 0.051 | 0% | 5% |
-| GPT-5.6 Sol | 13 | 0.692 | 0.036 | 0% | 1% |
-| GPT-5.6 Terra | 13 | 0.678 | 0.014 | 0% | 2% |
-| Gemini 3 Flash | 13 | 0.677 | 0 | 0% | 1% |
-| Gemini 3.1 Flash-Lite | 13 | 0.687 | 0.025 | 0% | 3% |
-| Gemini 3.1 Pro | 13 | 0.689 | 0.025 | 0% | 3% |
-| Gemini 3.5 Flash | 13 | 0.683 | 0.041 | 0% | 25% |
-| Gemini 3.6 Flash | 13 | 0.701 | 0.022 | 0% | 3% |
-| Grok 4.1 Fast | 13 | 0.743 | 0 | 0% | 4% |
-| Grok 4.20 | 13 | 0.706 | 0.042 | 0% | 7% |
-| Grok 4.3 | 13 | 0.68 | 0.046 | 0% | 6% |
-| Grok 4.5 | 13 | 0.697 | 0.034 | 0% | 4% |
-| Inkling | 13 | 0.673 | 0.053 | 1% | 9% |
-| Kimi K2.6 | 13 | 0.701 | 0.1 | 1% | 6% |
-| Kimi K3 | 13 | 0.726 | 0.034 | 0% | 2% |
-| MiniMax M3 | 13 | 0.692 | 0.062 | 1% | 37% |
-| Qwen 3.7 Max | 13 | 0.728 | 0.048 | 0% | 18% |
-| Qwen 3.8 Max | 13 | 0.714 | 0.06 | 0% | 15% |
+| Claude Fable 5 | 13 | 0.679 | 0.014 | 0% | 0% |
+| Claude Haiku 4.5 | 13 | 0.672 | 0.026 | 0% | 3% |
+| Claude Opus 4.7 | 13 | 0.704 | 0.008 | 0% | 0% |
+| Claude Opus 4.8 | 13 | 0.72 | 0.015 | 0% | 1% |
+| Claude Opus 5 | 13 | 0.733 | 0.031 | 0% | 1% |
+| Claude Sonnet 4.6 | 13 | 0.726 | 0.004 | 0% | 1% |
+| Claude Sonnet 5 | 13 | 0.699 | 0.026 | 0% | 1% |
+| DeepSeek V4 Pro | 13 | 0.738 | 0.069 | 1% | 5% |
+| GLM-5.2 | 13 | 0.683 | 0.058 | 1% | 13% |
+| GPT-5.4 | 13 | 0.684 | 0.011 | 0% | 1% |
+| GPT-5.4 mini | 13 | 0.713 | 0.062 | 1% | 5% |
+| GPT-5.4 nano | 13 | 0.699 | 0.088 | 2% | 27% |
+| GPT-5.5 | 13 | 0.703 | 0.025 | 0% | 1% |
+| GPT-5.6 Luna | 13 | 0.727 | 0.057 | 1% | 5% |
+| GPT-5.6 Sol | 13 | 0.692 | 0.035 | 0% | 1% |
+| GPT-5.6 Terra | 13 | 0.678 | 0.024 | 0% | 1% |
+| Gemini 3 Flash | 13 | 0.677 | 0.011 | 0% | 1% |
+| Gemini 3.1 Flash-Lite | 13 | 0.687 | 0.035 | 0% | 3% |
+| Gemini 3.1 Pro | 13 | 0.689 | 0.026 | 0% | 3% |
+| Gemini 3.5 Flash | 13 | 0.683 | 0.032 | 0% | 1% |
+| Gemini 3.6 Flash | 13 | 0.701 | 0.028 | 0% | 2% |
+| Grok 4.1 Fast | 13 | 0.743 | 0.029 | 0% | 4% |
+| Grok 4.20 | 13 | 0.706 | 0.055 | 0% | 6% |
+| Grok 4.3 | 13 | 0.68 | 0.049 | 0% | 5% |
+| Grok 4.5 | 13 | 0.697 | 0.041 | 0% | 3% |
+| Inkling | 13 | 0.673 | 0.045 | 0% | 3% |
+| Kimi K2.6 | 13 | 0.701 | 0.103 | 1% | 4% |
+| Kimi K3 | 13 | 0.726 | 0.048 | 0% | 2% |
+| MiniMax M3 | 13 | 0.692 | 0.071 | 1% | 33% |
+| Qwen 3.7 Max | 13 | 0.728 | 0.058 | 0% | 16% |
+| Qwen 3.8 Max | 13 | 0.714 | 0.071 | 0% | 15% |
```

## `paper/tables/wording-comparison.md` (Markdown)

```diff
@@ -13 +13 @@
-| Gemini 3.1 Pro | Capital gains realizations elasticity (net-of-tax-rate convention) | 0.373 | 2.077 | 1.703 | 4.832 | 4.598 |
+| Gemini 3.1 Pro | Capital gains realizations elasticity (net-of-tax-rate convention) | 0.373 | 2.077 | 1.703 | 4.793 | 4.598 |
```

