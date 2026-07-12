"""Focused regression tests for panel runner integrity hardening."""

from __future__ import annotations

import json
import os
import sys
from dataclasses import asdict
from pathlib import Path
from types import SimpleNamespace

import pytest

from llm_econ_beliefs.models import ProviderBatchResult, RunResult
from llm_econ_beliefs.provider_tags import provider_tag_for_runner


REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPTS_DIR = REPO_ROOT / "scripts"
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

import check_panel_grid
import rerun_failed_runs
import run_v4_new_models
import run_v4_per_quantity


MODEL = "gpt-5.4"
QUANTITY = "trade.armington_elasticity.import_domestic"
PROMPT_VERSION = "armington-clarify"


def _run(
    run_index: int,
    *,
    parsed_ok: bool = True,
    model_name: str = MODEL,
    quantity_id: str = QUANTITY,
    prompt_version: str = PROMPT_VERSION,
) -> RunResult:
    return RunResult(
        provider="openai_chat_completions",
        model_name=model_name,
        quantity_id=quantity_id,
        run_index=run_index,
        prompt_version=prompt_version,
        tool_regime="none",
        prompt="prompt",
        raw_response="{}" if parsed_ok else None,
        parsed_ok=parsed_ok,
        point_estimate=1.0 if parsed_ok else None,
        error=None if parsed_ok else "failed",
    )


def _write_runs(path: Path, records: list[RunResult]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("".join(json.dumps(asdict(record)) + "\n" for record in records))


def _grid_rows(*, parsed_value: object = True) -> list[dict[str, object]]:
    return [
        {
            "model_name": MODEL,
            "prompt_version": PROMPT_VERSION,
            "quantity_id": QUANTITY,
            "run_index": run_index,
            "parsed_ok": parsed_value,
        }
        for run_index in (1, 2)
    ]


def test_grid_checker_rejects_gaps_duplicates_and_non_boolean_parsed_ok():
    complete = check_panel_grid.validate_grid_rows(
        _grid_rows(),
        model_name=MODEL,
        prompt_version=PROMPT_VERSION,
        quantity_ids=[QUANTITY],
        n_runs=2,
        require_parsed=True,
    )
    assert complete.ok

    missing = check_panel_grid.validate_grid_rows(
        _grid_rows()[:1],
        model_name=MODEL,
        prompt_version=PROMPT_VERSION,
        quantity_ids=[QUANTITY],
        n_runs=2,
    )
    assert not missing.ok
    assert any(error.startswith("missing:") for error in missing.errors)

    duplicate = check_panel_grid.validate_grid_rows(
        [_grid_rows()[0], _grid_rows()[0]],
        model_name=MODEL,
        prompt_version=PROMPT_VERSION,
        quantity_ids=[QUANTITY],
        n_runs=2,
    )
    assert not duplicate.ok
    assert any(error.startswith("duplicate:") for error in duplicate.errors)

    integer_true = check_panel_grid.validate_grid_rows(
        _grid_rows(parsed_value=1),
        model_name=MODEL,
        prompt_version=PROMPT_VERSION,
        quantity_ids=[QUANTITY],
        n_runs=2,
        require_parsed=True,
    )
    assert not integer_true.ok
    assert any(error.startswith("unparsed:") for error in integer_true.errors)


def test_grid_checker_cli_is_runnable_standalone(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
):
    results_root = tmp_path / "results"
    _write_runs(
        results_root / f"{MODEL}-armington-clarify-batch15" / "runs.jsonl",
        [_run(run_index) for run_index in range(1, 16)],
    )
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "check_panel_grid.py",
            "--results-root",
            str(results_root),
            "--models",
            MODEL,
            "--batches",
            "armington-clarify-batch15",
            "--require-parsed",
        ],
    )

    assert check_panel_grid.main() == 0


@pytest.mark.parametrize(
    "staged_runs",
    [
        [_run(1)],
        [_run(1), _run(1)],
    ],
    ids=["missing", "duplicate"],
)
def test_invalid_staging_preserves_staging_and_existing_target(
    tmp_path: Path, staged_runs: list[RunResult]
):
    staging_root = tmp_path / "staging"
    _write_runs(staging_root / "quantity" / "runs.jsonl", staged_runs)
    target_dir = tmp_path / "canonical"
    target_dir.mkdir()
    snapshots = {
        "runs.jsonl": "canonical runs sentinel\n",
        "runs.csv": "canonical csv sentinel\n",
        "summary.csv": "canonical summary sentinel\n",
    }
    for filename, contents in snapshots.items():
        (target_dir / filename).write_text(contents)

    published = run_v4_per_quantity.merge_per_quantity(
        staging_root,
        target_dir,
        MODEL,
        PROMPT_VERSION,
        expected_quantity_ids=[QUANTITY],
        n_runs=2,
    )

    assert not published
    assert staging_root.exists()
    assert (staging_root / "quantity" / "runs.jsonl").exists()
    assert {
        filename: (target_dir / filename).read_text() for filename in snapshots
    } == snapshots
    assert not list(tmp_path.glob(".canonical.publish-*"))


def test_valid_staging_publishes_temp_files_with_os_replace(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
):
    staging_root = tmp_path / "staging"
    _write_runs(staging_root / "quantity" / "runs.jsonl", [_run(1), _run(2)])
    target_dir = tmp_path / "canonical"
    target_dir.mkdir()
    (target_dir / "runs.jsonl").write_text("old canonical contents\n")

    real_replace = os.replace
    replacements: list[tuple[Path, Path]] = []

    def recording_replace(source, target):
        replacements.append((Path(source), Path(target)))
        real_replace(source, target)

    monkeypatch.setattr(run_v4_per_quantity.os, "replace", recording_replace)
    published = run_v4_per_quantity.merge_per_quantity(
        staging_root,
        target_dir,
        MODEL,
        PROMPT_VERSION,
        expected_quantity_ids=[QUANTITY],
        n_runs=2,
    )

    assert published
    assert {target.name for _, target in replacements} == {
        "prompt_grid.csv",
        "runs.jsonl",
        "runs.csv",
        "requests.jsonl",
        "requests.csv",
        "summary.csv",
    }
    assert all(
        source.parent.name.startswith(".canonical.publish-")
        for source, _ in replacements
    )
    assert replacements[-1][1].name == "runs.jsonl"
    published_rows = [
        json.loads(line)
        for line in (target_dir / "runs.jsonl").read_text().splitlines()
    ]
    assert [row["run_index"] for row in published_rows] == [1, 2]
    assert staging_root.exists()
    assert not list(tmp_path.glob(".canonical.publish-*"))


def test_publication_failure_rolls_back_every_replaced_artifact(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
):
    staging_root = tmp_path / "staging"
    _write_runs(staging_root / "quantity" / "runs.jsonl", [_run(1), _run(2)])
    target_dir = tmp_path / "canonical"
    target_dir.mkdir()
    snapshots = {
        filename: f"old {filename}\n"
        for filename in (
            "prompt_grid.csv",
            "runs.csv",
            "requests.jsonl",
            "requests.csv",
            "summary.csv",
            "runs.jsonl",
        )
    }
    for filename, contents in snapshots.items():
        (target_dir / filename).write_text(contents)

    real_replace = os.replace
    publication_calls = 0

    def fail_third_publication(source, target):
        nonlocal publication_calls
        source_path = Path(source)
        if source_path.parent.name.startswith(".canonical.publish-"):
            publication_calls += 1
            if publication_calls == 3:
                raise OSError("injected publication failure")
        real_replace(source, target)

    monkeypatch.setattr(
        run_v4_per_quantity.os,
        "replace",
        fail_third_publication,
    )

    published = run_v4_per_quantity.merge_per_quantity(
        staging_root,
        target_dir,
        MODEL,
        PROMPT_VERSION,
        expected_quantity_ids=[QUANTITY],
        n_runs=2,
    )

    assert not published
    assert staging_root.exists()
    assert {
        filename: (target_dir / filename).read_text() for filename in snapshots
    } == snapshots
    assert not list(tmp_path.glob(".canonical.publish-*"))


def test_rerun_logs_returned_request_before_parse_failure(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
):
    monkeypatch.setattr(rerun_failed_runs, "REPO_ROOT", tmp_path)
    monkeypatch.setitem(
        rerun_failed_runs.PROVIDER_FOR_MODEL,
        "test-litellm-model",
        "litellm",
    )
    target_dir = tmp_path / "results" / "test-litellm-model-armington-clarify-batch15"
    _write_runs(
        target_dir / "runs.jsonl",
        [
            _run(
                1,
                parsed_ok=False,
                model_name="test-litellm-model",
            )
        ],
    )
    monkeypatch.setattr(
        rerun_failed_runs,
        "invoke_once",
        lambda *args: ProviderBatchResult(
            outputs=["not valid JSON"],
            request_id="req_parse_failure",
            usage={"prompt_tokens": 7, "completion_tokens": 5, "total_tokens": 12},
        ),
    )
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "rerun_failed_runs.py",
            "--model",
            "test-litellm-model",
            "--batch",
            "armington-clarify-batch15",
            "--attempts",
            "1",
        ],
    )

    assert rerun_failed_runs.main() == 1
    request_rows = [
        json.loads(line)
        for line in (target_dir / "requests.jsonl").read_text().splitlines()
    ]
    assert len(request_rows) == 1
    assert request_rows[0]["provider"] == "litellm_completion"
    assert request_rows[0]["request_id"] == "req_parse_failure"
    assert request_rows[0]["usage"]["total_tokens"] == 12


@pytest.mark.parametrize("raw", ["", " , ", "unknown-model"])
def test_models_argument_rejects_empty_and_unknown_values(raw: str):
    with pytest.raises(ValueError):
        run_v4_new_models.parse_models_argument(raw)


def test_run_v4_new_models_propagates_child_exit_status(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
):
    monkeypatch.setattr(run_v4_new_models, "REPO_ROOT", tmp_path)
    monkeypatch.setattr(
        run_v4_new_models.subprocess,
        "run",
        lambda command: SimpleNamespace(returncode=7),
    )
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "run_v4_new_models.py",
            "--models",
            MODEL,
            "--only-batch",
            "armington-clarify-batch15",
        ],
    )

    assert run_v4_new_models.main() == 7


def test_run_v4_new_models_rejects_exact_but_unparsed_grid(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
):
    monkeypatch.setattr(run_v4_new_models, "REPO_ROOT", tmp_path)

    def fake_check(*args, require_parsed=False, **kwargs):
        return SimpleNamespace(
            ok=not require_parsed,
            errors=() if not require_parsed else ("unparsed slots",),
        )

    monkeypatch.setattr(
        run_v4_new_models,
        "check_batch_directory",
        fake_check,
    )
    monkeypatch.setattr(
        run_v4_new_models.subprocess,
        "run",
        lambda command: pytest.fail("an exact structural grid should be skipped"),
    )
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "run_v4_new_models.py",
            "--models",
            MODEL,
            "--only-batch",
            "armington-clarify-batch15",
        ],
    )

    assert run_v4_new_models.main() == 1


def test_provider_runner_tags_are_canonical():
    assert provider_tag_for_runner("litellm") == "litellm_completion"
    assert provider_tag_for_runner("openai") == "openai_chat_completions"
    assert provider_tag_for_runner("anthropic") == "anthropic"
    with pytest.raises(ValueError):
        provider_tag_for_runner("unknown")
