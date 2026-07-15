"""Build results/policybench-scores.csv from a PolicyBench dashboard release.

The join key for the correlates analysis is the leaderboard headline:
the household-weighted share of predictions within one dollar of the
reference answer (`exact` in the dashboard data), US, no-tools. The
domain-matched tax predictor n-weights the same rate over the
benchmark's seven tax variables from the per-model heatmap.

Usage:
    gh release download <TAG> -R PolicyEngine/policybench -D <DIR>
    .venv/bin/python scripts/build_policybench_scores.py \
        --dashboard-json <DIR>/dashboard-data.json --release <TAG>
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))

CONDITION = "no_tools"
COUNTRY = "us"

# The benchmark's tax-domain variables (all money-valued tax outputs).
TAX_VARIABLES = (
    "federal_income_tax_before_refundable_credits",
    "federal_refundable_credits",
    "local_income_tax",
    "payroll_tax",
    "self_employment_tax",
    "state_income_tax_before_refundable_credits",
    "state_refundable_credits",
)
FEDERAL_TAX_VARIABLE = "federal_income_tax_before_refundable_credits"


def build_rows(dashboard: dict, release: str) -> list[dict[str, object]]:
    country = dashboard["countries"][COUNTRY]
    stats = [m for m in country["modelStats"] if m["condition"] == CONDITION]
    heatmap = [h for h in country["heatmap"] if h["condition"] == CONDITION]

    heatmap_variables = {h["variable"] for h in heatmap}
    missing = sorted(set(TAX_VARIABLES) - heatmap_variables)
    if missing:
        raise ValueError(f"heatmap lacks expected tax variables: {missing}")

    rows: list[dict[str, object]] = []
    for model in sorted(stats, key=lambda m: -m["exact"]):
        cells = [
            h
            for h in heatmap
            if h["model"] == model["model"] and h["variable"] in TAX_VARIABLES
        ]
        if len(cells) != len(TAX_VARIABLES):
            raise ValueError(
                f"{model['model']}: expected {len(TAX_VARIABLES)} tax cells, "
                f"got {len(cells)}"
            )
        weighted = sum(h["exact"] * h["n"] for h in cells)
        total_n = sum(h["n"] for h in cells)
        federal = next(
            h["exact"] for h in cells if h["variable"] == FEDERAL_TAX_VARIABLE
        )
        rows.append(
            {
                "model": model["model"],
                "policybench_within_dollar": round(model["exact"], 4),
                "policybench_tax_within_dollar": round(weighted / total_n, 4),
                "policybench_fedtax_within_dollar": round(federal, 4),
                "policybench_composite_score": round(model["score"], 4),
                "output_group_score": round(model["outputGroupScore"], 4),
                "condition": CONDITION,
                "country": COUNTRY,
                "source_release": f"PolicyEngine/policybench {release}",
            }
        )
    return rows


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dashboard-json", required=True, type=Path)
    parser.add_argument("--release", required=True, help="e.g. dashboard-data-20260710")
    parser.add_argument(
        "--output",
        type=Path,
        default=REPO_ROOT / "results" / "policybench-scores.csv",
    )
    args = parser.parse_args()

    dashboard = json.loads(args.dashboard_json.read_text())
    rows = build_rows(dashboard, args.release)

    temporary = args.output.with_name(f".{args.output.name}.tmp")
    with temporary.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    os.replace(temporary, args.output)
    print(f"Wrote {len(rows)} models to {args.output} ({args.release})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
