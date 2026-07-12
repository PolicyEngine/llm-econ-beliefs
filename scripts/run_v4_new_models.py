"""Extend the v4 panel with models released after the April 2026 rerun.

Runs the July 2026 additions (gpt-5.5, claude-sonnet-5, claude-opus-4.8,
claude-fable-5, gemini-3.5-flash, grok-4.3) through the per-quantity fallback
path, which persists results incrementally and survives hung provider calls.
Prompts are unchanged (`v4` plus the two clarify probes), so the new rows pool
directly with the existing panel.

Usage:
    .venv/bin/python scripts/run_v4_new_models.py [--only-model M] [--only-batch B] [--dry-run]
"""

from __future__ import annotations

import argparse
import subprocess
import sys
import time
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from llm_econ_beliefs import list_quantities
from check_panel_grid import check_batch_directory
from run_v4_full_panel import NEW_MODELS_JULY_2026, count_records
from run_v4_per_quantity import PROVIDER_FOR_MODEL

BATCHES = {
    "elasticities-batch15": {"per_quantity_batch": "main", "prompt_version": "v4"},
    "armington-clarify-batch15": {
        "per_quantity_batch": "armington-clarify",
        "prompt_version": "armington-clarify",
    },
    "ies-clarify-batch15": {
        "per_quantity_batch": "ies-clarify",
        "prompt_version": "ies-clarify",
    },
}

RUNS_PER_QUANTITY = 15


def expected_runs(batch_key: str) -> int:
    if batch_key == "elasticities-batch15":
        return len(list_quantities()) * RUNS_PER_QUANTITY
    return RUNS_PER_QUANTITY


def parse_models_argument(raw: str | None) -> list[str]:
    """Return a nonempty, unique list of registered model names."""
    if raw is None:
        models = [model_name for _, model_name in NEW_MODELS_JULY_2026]
    else:
        models = [
            model_name.strip() for model_name in raw.split(",") if model_name.strip()
        ]
        if not models:
            raise ValueError("--models must contain at least one model")
    if len(models) != len(set(models)):
        raise ValueError("--models must not contain duplicates")
    unknown = sorted(set(models) - set(PROVIDER_FOR_MODEL))
    if unknown:
        raise ValueError(f"unknown models: {', '.join(unknown)}")
    return models


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--only-model", help="run a single model")
    parser.add_argument("--only-batch", choices=list(BATCHES.keys()))
    parser.add_argument(
        "--models",
        help="comma-separated model list (default: the July 2026 additions)",
    )
    parser.add_argument("--per-quantity-timeout", type=int, default=1800)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    try:
        models = parse_models_argument(args.models)
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 2
    if args.only_model:
        if args.only_model not in models:
            print(f"No such new model: {args.only_model}")
            return 2
        models = [args.only_model]

    batches = BATCHES
    if args.only_batch:
        batches = {args.only_batch: BATCHES[args.only_batch]}

    start = time.time()
    first_failure = 0
    for model_name in models:
        for batch_key, spec in batches.items():
            target_dir = REPO_ROOT / "results" / f"{model_name}-{batch_key}"
            ok, total = count_records(target_dir, spec["prompt_version"])
            needed = expected_runs(batch_key)
            grid_result = check_batch_directory(
                REPO_ROOT / "results",
                model_name=model_name,
                batch=batch_key,
            )
            if grid_result.ok:
                parsed_grid = check_batch_directory(
                    REPO_ROOT / "results",
                    model_name=model_name,
                    batch=batch_key,
                    require_parsed=True,
                )
                status = "complete" if parsed_grid.ok else "unresolved"
                print(
                    f"[{time.strftime('%H:%M:%S')}] {model_name} / {batch_key} "
                    f"SKIP ({ok}/{total} runs on exact grid; {status})"
                )
                if not parsed_grid.ok and first_failure == 0:
                    first_failure = 1
                continue

            print(
                f"\n[{time.strftime('%H:%M:%S')}] {model_name} / {batch_key} "
                f"(have {total}/{needed} runs)"
            )
            if args.dry_run:
                continue

            cmd = [
                sys.executable,
                "-u",
                str(REPO_ROOT / "scripts" / "run_v4_per_quantity.py"),
                "--model",
                model_name,
                "--batch",
                spec["per_quantity_batch"],
                "--prompt-version",
                spec["prompt_version"],
                "--per-quantity-timeout",
                str(args.per_quantity_timeout),
            ]
            proc = subprocess.run(cmd)
            if proc.returncode != 0 and first_failure == 0:
                first_failure = proc.returncode
            ok, total = count_records(target_dir, spec["prompt_version"])
            status = "OK" if proc.returncode == 0 else f"EXIT {proc.returncode}"
            print(
                f"[{time.strftime('%H:%M:%S')}] {model_name} / {batch_key} {status}: "
                f"{ok}/{total} parsed, elapsed {time.time() - start:.0f}s"
            )
            grid_result = check_batch_directory(
                REPO_ROOT / "results",
                model_name=model_name,
                batch=batch_key,
                require_parsed=True,
            )
            if not grid_result.ok:
                if first_failure == 0:
                    first_failure = 1
                print(f"  INVALID OR UNRESOLVED GRID for {model_name} / {batch_key}")
                for error in grid_result.errors:
                    print(f"    {error}")

    print(f"\nAll new-model cells processed in {time.time() - start:.0f}s")
    return first_failure


if __name__ == "__main__":
    raise SystemExit(main())
