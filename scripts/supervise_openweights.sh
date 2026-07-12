#!/bin/bash
# Run resume_openweights.sh repeatedly until every open-weights cell is
# fully parsed (or attempts run out), keeping the machine awake via the
# caller's caffeinate wrapper. Prints a machine-greppable final line.
set -euo pipefail
cd "$(dirname "$0")/.."

# Single-instance lock: concurrent recovery pipelines can interleave
# staging deletes with canonical merges (Codex hardening review, finding 1).
LOCK_DIR="results/.supervisor.lock"
if ! mkdir "$LOCK_DIR" 2>/dev/null; then
  holder=$(cat "$LOCK_DIR/pid" 2>/dev/null || echo "unknown")
  if [ "$holder" != "unknown" ] && kill -0 "$holder" 2>/dev/null; then
    echo "SUPERVISOR: another instance (pid $holder) holds the lock; exiting"
    exit 3
  fi
  echo "SUPERVISOR: clearing stale lock from pid $holder"
  rm -rf "$LOCK_DIR"
  mkdir "$LOCK_DIR" || exit 3
fi
echo $$ > "$LOCK_DIR/pid"
trap 'rm -rf "$LOCK_DIR"' EXIT

check_complete() {
  .venv/bin/python scripts/check_panel_grid.py \
    --models deepseek-v4-pro,qwen-3.7-max,kimi-k2.6,glm-5.2,minimax-m3 \
    --require-parsed
}

for attempt in 1 2 3 4; do
  echo "=== supervisor attempt $attempt $(date '+%H:%M:%S') ==="
  if remaining=$(check_complete 2>&1); then
    echo "SUPERVISOR: ALL COMPLETE before attempt $attempt"
    exit 0
  fi
  echo "remaining grid failures:"
  echo "$remaining"
  if bash scripts/resume_openweights.sh; then
    :
  else
    rc=$?
    echo "SUPERVISOR: resume attempt $attempt exited $rc; will recheck" >&2
  fi
done

if remaining=$(check_complete 2>&1); then
  echo "SUPERVISOR: ALL COMPLETE"
  exit 0
fi
echo "SUPERVISOR: INCOMPLETE after 4 attempts — $remaining"
exit 1
