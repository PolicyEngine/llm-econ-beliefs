"""End-to-end resume and publish checks for the per-quantity and full-panel runners.

These port the audit's executed repros (2026-09-25): a staged cell whose
prompt, provider or tool regime differs from today's elicitation used to be
skipped and republished with no provider call.
"""

from __future__ import annotations

import csv
import sys
from pathlib import Path
from types import SimpleNamespace

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]
for path in (REPO_ROOT / "scripts", Path(__file__).resolve().parent):
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))

import check_panel_grid  # noqa: E402
import run_v4_full_panel  # noqa: E402
import run_v4_per_quantity  # noqa: E402
from cell_fixtures import MODEL, RUNNER, elicit_cell, read_rows, write_rows  # noqa: E402

QID = "household.annual_discount_factor"


def _staged_cell(tmp_path: Path) -> Path:
    return tmp_path / "results" / f"_perquantity_{MODEL}_main" / QID.replace(".", "_")


def _run_main(tmp_path, monkeypatch, staged_rows=None):
    """Run run_v4_per_quantity.main() on one quantity with a stub child."""
    if staged_rows is not None:
        write_rows(_staged_cell(tmp_path) / "runs.jsonl", staged_rows)
    calls = []

    def fake_child(model_name, quantity_id, prompt_version, target_dir, **kwargs):
        calls.append((model_name, quantity_id, prompt_version))
        elicit_cell(target_dir, [quantity_id], prompt_version=prompt_version)
        return True

    monkeypatch.setattr(run_v4_per_quantity, "REPO_ROOT", tmp_path)
    monkeypatch.setattr(
        run_v4_per_quantity, "list_quantities", lambda: [SimpleNamespace(id=QID)]
    )
    monkeypatch.setattr(run_v4_per_quantity, "run_one_quantity", fake_child)
    monkeypatch.setattr(sys, "argv", ["run_v4_per_quantity.py", "--model", MODEL])
    status = run_v4_per_quantity.main()
    return status, calls


@pytest.mark.parametrize(
    "mutate",
    [
        pytest.param(lambda row: row.update(prompt=row["prompt"].replace("Annual", "Monthly")), id="prompt-text"),
        pytest.param(lambda row: row.update(prompt=row["prompt"] + "x"), id="one-byte-suffix"),
        pytest.param(lambda row: row.update(provider="litellm_completion"), id="provider"),
        pytest.param(lambda row: row.update(tool_regime="full"), id="tool-regime"),
    ],
)
def test_stale_staged_cell_is_quarantined_and_re_elicited(tmp_path, monkeypatch, mutate):
    rows = elicit_cell(tmp_path / "fresh", [QID])
    for row in rows:
        mutate(row)

    status, calls = _run_main(tmp_path, monkeypatch, rows)

    assert status == 0
    assert calls == [(MODEL, QID, "v4")]
    published = tmp_path / "results" / f"{MODEL}-elasticities-batch15"
    identity = check_panel_grid.expected_cell_identity(
        model_name=MODEL, runner=RUNNER, prompt_version="v4", quantity_ids=[QID]
    )
    published_rows = read_rows(published / "runs.jsonl")
    assert check_panel_grid.validate_cell_identity(
        published_rows, identity, require_parsed=True
    ).ok
    with (published / "prompt_grid.csv").open() as handle:
        grid_prompts = {row["prompt"] for row in csv.DictReader(handle)}
    assert grid_prompts == {row["prompt"] for row in published_rows}
    quarantine = tmp_path / "results" / f"_perquantity_{MODEL}_main.quarantine"
    (kept,) = list(quarantine.iterdir())
    assert read_rows(kept / "runs.jsonl") == rows  # evidence retained, not deleted


def test_matching_staged_cell_is_reused_without_a_provider_call(tmp_path, monkeypatch):
    rows = elicit_cell(tmp_path / "fresh", [QID])
    status, calls = _run_main(tmp_path, monkeypatch, rows)
    assert status == 0
    assert calls == []


def test_partially_written_staged_cell_is_re_elicited_not_a_crash(tmp_path, monkeypatch):
    staged = _staged_cell(tmp_path)
    write_rows(staged / "runs.jsonl", elicit_cell(tmp_path / "fresh", [QID]))
    with (staged / "runs.jsonl").open("a") as handle:
        handle.write('{"model_name": "gpt-5.4", "trunc')  # child killed mid-write
    status, calls = _run_main(tmp_path, monkeypatch)
    assert status == 0
    assert len(calls) == 1


def test_prompt_version_that_disagrees_with_the_batch_is_refused(monkeypatch):
    monkeypatch.setattr(
        sys,
        "argv",
        ["run_v4_per_quantity.py", "--model", MODEL, "--batch", "armington-clarify", "--prompt-version", "v4"],
    )
    assert run_v4_per_quantity.main() == 2


def test_merge_refuses_one_row_with_a_changed_prompt(tmp_path):
    staging = tmp_path / "staging"
    rows = elicit_cell(staging / "cell", [QID])
    rows[7]["prompt"] += "x"
    write_rows(staging / "cell" / "runs.jsonl", rows)
    identity = check_panel_grid.expected_cell_identity(
        model_name=MODEL, runner=RUNNER, prompt_version="v4", quantity_ids=[QID]
    )
    target = tmp_path / "published"
    assert not run_v4_per_quantity.merge_per_quantity(
        staging, target, MODEL, "v4", identity=identity
    )
    assert not target.exists()


@pytest.mark.parametrize(
    "corrupt",
    [
        pytest.param(lambda rows: [dict(rows[0], run_index=1) for _ in rows], id="duplicate-run-1"),
        pytest.param(lambda rows: [dict(row, model_name="gpt-5.4-mini") for row in rows], id="wrong-model"),
    ],
)
def test_skip_complete_never_skips_a_cell_that_fails_the_exact_grid(tmp_path, corrupt):
    output_dir = tmp_path / f"{MODEL}-elasticities-batch15"
    rows = corrupt(elicit_cell(tmp_path / "fresh", [QID]))
    write_rows(output_dir / "runs.jsonl", rows)
    identity = check_panel_grid.expected_cell_identity(
        model_name=MODEL, runner=RUNNER, prompt_version="v4", quantity_ids=[QID]
    )
    complete, _ = run_v4_full_panel.cell_already_complete(output_dir, identity)
    grid = check_panel_grid.check_run_files(
        [output_dir / "runs.jsonl"],
        model_name=MODEL,
        prompt_version="v4",
        quantity_ids=[QID],
        require_parsed=True,
    )
    assert not grid.ok
    assert not complete.ok


def test_skip_complete_flags_unparsed_slots_without_overwriting_the_archive(
    tmp_path, monkeypatch, capsys
):
    # Four April clarify cells hold disclosed unparsed slots. --skip-complete
    # must neither call them complete (exit 0) nor re-elicit them in place.
    results = tmp_path / "results"
    output_dir = results / f"{MODEL}-elasticities-batch15"
    rows = elicit_cell(tmp_path / "fresh", [QID])
    rows[3] = dict(rows[3], parsed_ok=False, point_estimate=None)
    write_rows(output_dir / "runs.jsonl", rows)
    before = (output_dir / "runs.jsonl").read_bytes()
    children = []
    monkeypatch.setattr(run_v4_full_panel, "REPO_ROOT", tmp_path)
    monkeypatch.setattr(
        run_v4_full_panel, "list_quantities", lambda: [SimpleNamespace(id=QID)]
    )
    monkeypatch.setattr(
        run_v4_full_panel, "run_cell_in_subprocess", lambda **kw: children.append(kw) or (0, 0)
    )
    monkeypatch.setattr(
        sys,
        "argv",
        ["run_v4_full_panel.py", "--skip-complete", "--only-model", MODEL, "--only-batch", "elasticities-batch15"],
    )
    assert run_v4_full_panel.main() == 1
    assert children == []
    assert (output_dir / "runs.jsonl").read_bytes() == before
    assert "UNRESOLVED: 1 unparsed slots" in capsys.readouterr().out
