"""Rebuild the cross-model comparison artifacts under results/.

Regenerates:

- ``results/elasticity-all-model-comparison.csv`` — one row per
  (model, quantity) stacked from every ``*-elasticities-batch15``
  summary via ``llm_econ_beliefs.compare``.
- ``results/elasticity-model-rollup.csv`` — one row per model with run
  counts, tracked cost, and mean pooled interval geometry.

Usage:
    .venv/bin/python scripts/build_comparison_artifacts.py
"""

from __future__ import annotations

import csv
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))

from llm_econ_beliefs import list_quantities
from llm_econ_beliefs.compare import (
    build_comparison_rows,
    read_summary_rows,
    write_comparison_csv,
)

RESULTS_DIR = REPO_ROOT / "results"
COMPARISON_PATH = RESULTS_DIR / "elasticity-all-model-comparison.csv"
ROLLUP_PATH = RESULTS_DIR / "elasticity-model-rollup.csv"
RUNS_PER_QUANTITY = 15


def elasticities_dirs() -> list[Path]:
    return sorted(
        path
        for path in RESULTS_DIR.iterdir()
        if path.is_dir()
        and path.name.endswith("-elasticities-batch15")
        and (path / "summary.csv").exists()
    )


def build_rollup_rows(result_dirs: list[Path]) -> list[dict[str, object]]:
    expected_per_model = len(list_quantities()) * RUNS_PER_QUANTITY
    rollup_rows: list[dict[str, object]] = []
    for result_dir in result_dirs:
        rows = read_summary_rows(result_dir)
        model_name = rows[0]["model_name"]
        successful_runs = sum(int(row["n_successful_runs"]) for row in rows)
        total_cost = sum(
            float(row["usage_estimated_total_cost_usd_total"])
            for row in rows
            if row.get("usage_estimated_total_cost_usd_total") not in (None, "")
        )
        widths = [
            float(row["pooled_upper_bound"]) - float(row["pooled_lower_bound"])
            for row in rows
            if row.get("pooled_upper_bound") not in (None, "")
            and row.get("pooled_lower_bound") not in (None, "")
        ]
        points = [
            float(row["pooled_point_estimate"])
            for row in rows
            if row.get("pooled_point_estimate") not in (None, "")
        ]
        rollup_rows.append(
            {
                "model_name": model_name,
                "quantities": len(rows),
                "successful_runs": successful_runs,
                "expected_runs": expected_per_model,
                "success_rate": successful_runs / expected_per_model,
                "total_cost_usd": total_cost,
                "cost_per_successful_run_usd": (
                    total_cost / successful_runs if successful_runs else None
                ),
                "mean_pooled_interval_width": (
                    sum(widths) / len(widths) if widths else None
                ),
                "mean_pooled_point_estimate": (
                    sum(points) / len(points) if points else None
                ),
            }
        )
    return rollup_rows


def main() -> int:
    result_dirs = elasticities_dirs()
    if not result_dirs:
        print("No *-elasticities-batch15 result directories found.")
        return 1

    comparison_rows = build_comparison_rows(result_dirs)
    write_comparison_csv(COMPARISON_PATH, comparison_rows)
    print(f"Wrote {len(comparison_rows)} rows to {COMPARISON_PATH}")

    rollup_rows = build_rollup_rows(result_dirs)
    with ROLLUP_PATH.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rollup_rows[0].keys()))
        writer.writeheader()
        writer.writerows(rollup_rows)
    print(f"Wrote {len(rollup_rows)} models to {ROLLUP_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
