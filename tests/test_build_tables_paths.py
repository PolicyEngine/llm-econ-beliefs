"""The table build reads run data from its own checkout.

``results/elasticity-all-model-comparison.csv`` records each model's run
directory as an absolute path into the checkout that generated it. Read as
written, a build from a worktree, CI or a fresh clone would load another
checkout's runs (or none), and the run-level tables (Appendix A9 and A15)
would silently come out different from the committed ones.
"""

from __future__ import annotations

import csv
import io
from pathlib import Path

import pytest

from paper import build_tables

REPO_ROOT = Path(__file__).resolve().parents[1]


def _as_csv(rows: list[dict[str, object]]) -> str:
    buffer = io.StringIO(newline="")
    writer = csv.DictWriter(buffer, fieldnames=list(rows[0].keys()))
    writer.writeheader()
    writer.writerows(rows)
    return buffer.getvalue()


def _committed(stem: str) -> str:
    with (REPO_ROOT / "paper" / "tables" / f"{stem}.csv").open(newline="") as handle:
        return handle.read()


def test_resolve_source_dir_points_into_this_checkout() -> None:
    results = build_tables.REPO_ROOT / "results"
    for recorded in (
        "/elsewhere/llm-econ-beliefs/results/gpt-5.4-elasticities-batch15",
        "C:\\elsewhere\\llm-econ-beliefs\\results\\gpt-5.4-elasticities-batch15",
        "results/gpt-5.4-elasticities-batch15",
        "results/gpt-5.4-elasticities-batch15/",
        # A "results" substring elsewhere, or a results/ directory above the
        # checkout, must not move the anchor.
        "/elsewhere/old-results/llm-econ-beliefs/results/gpt-5.4-elasticities-batch15",
        "/ci/results/llm-econ-beliefs/results/gpt-5.4-elasticities-batch15",
    ):
        assert build_tables.resolve_source_dir(recorded) == str(results / "gpt-5.4-elasticities-batch15")
    assert build_tables.resolve_source_dir(
        "/elsewhere/llm-econ-beliefs/results/glm-5.2-8k-pilot-archive/elasticities-batch15"
    ) == str(results / "glm-5.2-8k-pilot-archive" / "elasticities-batch15")
    assert build_tables.resolve_source_dir("/elsewhere/llm-econ-beliefs/results/x-results/y") == str(
        results / "x-results" / "y"
    )


@pytest.mark.parametrize(
    "recorded",
    [
        "/elsewhere/llm-econ-beliefs/gpt-5.4-elasticities-batch15",
        "C:\\elsewhere\\llm-econ-beliefs\\gpt-5.4-elasticities-batch15",
    ],
)
def test_resolve_source_dir_refuses_paths_it_cannot_place(recorded: str) -> None:
    with pytest.raises(ValueError):
        build_tables.resolve_source_dir(recorded)


def test_comparison_rows_resolve_to_existing_run_directories() -> None:
    rows = build_tables.read_comparison_rows(build_tables.MAIN_COMPARISON_PATH)
    assert rows
    for row in rows:
        path = Path(row.source_dir)
        assert path.is_relative_to(build_tables.REPO_ROOT / "results"), row.source_dir
        assert (path / "runs.jsonl").exists(), row.source_dir


def test_run_level_tables_rebuild_to_the_committed_csvs() -> None:
    comparison = build_tables.read_comparison_rows(build_tables.MAIN_COMPARISON_PATH)
    canonical = [row for row in comparison if build_tables.quantity_panel(row.quantity_id) == "canonical"]
    assert _as_csv(build_tables.build_cap_gains_convention_audit_table(comparison)) == _committed(
        "cap-gains-convention-audit"
    )
    assert _as_csv(build_tables.build_variance_decomposition_table(canonical)) == _committed(
        "variance-decomposition"
    )
