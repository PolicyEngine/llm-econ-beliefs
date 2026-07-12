#!/bin/bash
# Resume the July 2026 open-weights wave after an OpenRouter credit top-up.
#
# Two recovery layers, both idempotent:
#  1. run_v4_new_models fills cells that never reached full run counts
#     (per-quantity staging resume skips completed quantities).
#  2. rerun_failed_runs re-elicits failed slots in place (credit-exhaustion
#     records, GLM empty-content records), archiving what it replaces.
#
# Usage: bash scripts/resume_openweights.sh
set -euo pipefail
cd "$(dirname "$0")/.."

MODELS=(deepseek-v4-pro qwen-3.7-max kimi-k2.6 glm-5.2 minimax-m3)
BATCHES=(elasticities-batch15 armington-clarify-batch15 ies-clarify-batch15)

echo "== Layer 1: fill cells that never completed =="
status=0
pids=()
job_models=()
for model in "${MODELS[@]}"; do
  .venv/bin/python -u scripts/run_v4_new_models.py --models "$model" &
  pids+=("$!")
  job_models+=("$model")
done
for i in "${!pids[@]}"; do
  if wait "${pids[$i]}"; then
    echo "layer 1 ${job_models[$i]}: OK"
  else
    rc=$?
    echo "layer 1 ${job_models[$i]}: EXIT $rc" >&2
    if (( status == 0 )); then
      status=$rc
    fi
  fi
done

echo "== Layer 2: re-elicit failed slots in place =="
for model in "${MODELS[@]}"; do
  for batch in "${BATCHES[@]}"; do
    if .venv/bin/python -u scripts/rerun_failed_runs.py \
      --model "$model" --batch "$batch" --attempts 3; then
      :
    else
      rc=$?
      echo "layer 2 $model/$batch: EXIT $rc" >&2
      if (( status == 0 )); then
        status=$rc
      fi
    fi
  done
done

echo "== Authoritative exact-grid check =="
models_csv=$(IFS=,; echo "${MODELS[*]}")
if .venv/bin/python scripts/check_panel_grid.py \
  --models "$models_csv" --require-parsed; then
  if (( status != 0 )); then
    echo "Earlier job failures were resolved; authoritative grid is complete."
  fi
  exit 0
else
  rc=$?
  if (( status == 0 )); then
    status=$rc
  fi
fi
exit "$status"
