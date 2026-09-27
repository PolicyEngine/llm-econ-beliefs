"""Per-quantity rerun fallback for models where multi-quantity cells hang.

For a given model, spawns one subprocess per quantity (each doing 15 runs),
then merges all per-quantity outputs into a single canonical batch dir
matching what a normal cell run would produce.

Reruns resume from the staging directory by default: a quantity is skipped
only when its staged `runs.jsonl` is the exact, fully parsed cell today's
run would produce (same model, provider, prompt version, tool regime and
prompt text), so an interrupted panel run picks up where it left off. Any
other staged cell is moved to `<staging>.quarantine/` (keeping its paid
request logs and raw answers) and re-elicited. Pass `--fresh` to discard
staged results and re-elicit everything.

Usage:
    python3 scripts/run_v4_per_quantity.py --model claude-sonnet-4.6
"""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path
from typing import Sequence

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from check_panel_grid import (
    BATCH_PROMPT_VERSIONS,
    CellIdentity,
    expected_cell_identity,
    load_jsonl_rows,
    validate_cell_identity,
    validate_grid_rows,
)

from llm_econ_beliefs import list_quantities
from llm_econ_beliefs.experiment import (
    _write_jsonl,
    _write_requests_csv,
    _write_runs_csv,
    _write_summary_csv,
    summarize_run_results,
)
from llm_econ_beliefs.models import RequestLog, RunResult
from llm_econ_beliefs.runner import build_run_grid, write_run_grid_csv

PROVIDER_FOR_MODEL = {
    "claude-sonnet-4.6": "litellm",
    "claude-opus-4.7": "litellm",
    "gemini-3.1-pro-preview": "litellm",
    "grok-4.20": "litellm",
    "claude-haiku-4.5": "litellm",
    "gemini-3-flash-preview": "litellm",
    "gemini-3.1-flash-lite-preview": "litellm",
    "grok-4.1-fast": "litellm",
    "gpt-5.4": "openai",
    "gpt-5.4-mini": "openai",
    "gpt-5.4-nano": "openai",
    "gpt-5.5": "openai",
    "claude-sonnet-5": "anthropic",
    "claude-opus-4.8": "anthropic",
    "claude-opus-5": "anthropic",
    "claude-fable-5": "anthropic",
    "gemini-3.5-flash": "litellm",
    "gemini-3.6-flash": "litellm",
    "grok-4.3": "litellm",
    "grok-4.5": "litellm",
    "deepseek-v4-pro": "litellm",
    "qwen-3.7-max": "litellm",
    "kimi-k2.6": "litellm",
    "kimi-k3": "litellm",
    "glm-5.2": "litellm",
    "minimax-m3": "litellm",
    "qwen3.8-max": "litellm",
    "inkling": "litellm",
    "gpt-5.6-sol": "openai",
    "gpt-5.6-luna": "openai",
    "gpt-5.6-terra": "openai",
}


def run_one_quantity(
    model_name: str,
    quantity_id: str,
    prompt_version: str,
    target_dir: Path,
    per_quantity_timeout: int = 900,
) -> bool:
    """Spawn subprocess for a single quantity, return True on success."""
    target_dir.mkdir(parents=True, exist_ok=True)
    provider = PROVIDER_FOR_MODEL[model_name]
    cmd = [
        sys.executable,
        "-u",
        str(REPO_ROOT / "scripts" / "run_v4_full_panel.py"),
        "--exec-cell",
        "--provider",
        provider,
        "--model",
        model_name,
        "--prompt-version",
        prompt_version,
        "--output-dir",
        str(target_dir),
        "--quantity-ids",
        quantity_id,
    ]
    try:
        proc = subprocess.run(
            cmd,
            timeout=per_quantity_timeout,
            capture_output=True,
            text=True,
            env={**os.environ, "PYTHONUNBUFFERED": "1"},
        )
        if proc.returncode != 0:
            print(f"  FAIL {quantity_id}: exit {proc.returncode}")
            return False
        return True
    except subprocess.TimeoutExpired:
        print(f"  TIMEOUT {quantity_id}")
        return False


def load_runs(path: Path) -> list[RunResult]:
    if not path.exists():
        return []
    records = []
    with path.open() as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            data = json.loads(line)
            records.append(RunResult(**data))
    return records


def load_requests(path: Path) -> list[RequestLog]:
    if not path.exists():
        return []
    records = []
    with path.open() as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            data = json.loads(line)
            records.append(RequestLog(**data))
    return records


def merge_per_quantity(
    staging_root: Path,
    target_dir: Path,
    model_name: str,
    prompt_version: str,
    *,
    expected_quantity_ids: Sequence[str] | None = None,
    n_runs: int = 15,
    identity: CellIdentity | None = None,
) -> bool:
    """Validate staging and atomically publish canonical batch artifacts.

    Production callers pass ``identity`` so every staged row is checked
    against the exact grid, provider, tool regime and prompt text before any
    target artifact is touched; the published prompt grid then describes the
    prompts that were actually sent.  ``expected_quantity_ids`` alone checks
    only the grid.  Returning ``False`` leaves both the staging tree and the
    canonical target unchanged.
    """
    tool_regime = "none"
    if identity is not None:
        if (
            identity.model_name != model_name
            or identity.prompt_version != prompt_version
            or identity.n_runs != n_runs
        ):
            raise ValueError("identity disagrees with model, prompt version or n_runs")
        if expected_quantity_ids is not None and tuple(
            expected_quantity_ids
        ) != identity.quantity_ids:
            raise ValueError("identity disagrees with expected_quantity_ids")
        expected_quantity_ids = identity.quantity_ids
        tool_regime = identity.tool_regime

    all_records: list[RunResult] = []
    all_request_logs: list[RequestLog] = []
    next_request_index = 1
    for sub in sorted(staging_root.iterdir()):
        if not sub.is_dir():
            continue
        runs_path = sub / "runs.jsonl"
        if runs_path.exists():
            all_records.extend(load_runs(runs_path))
        requests_path = sub / "requests.jsonl"
        for log in load_requests(requests_path):
            log.request_index = next_request_index
            all_request_logs.append(log)
            next_request_index += 1

    if not all_records:
        print("No records to merge.")
        return False

    quantity_ids = (
        list(expected_quantity_ids)
        if expected_quantity_ids is not None
        else sorted({record.quantity_id for record in all_records})
    )
    if identity is not None:
        identity_result = validate_cell_identity(
            all_records, identity, require_parsed=False
        )
        if not identity_result.ok:
            print("Staging does not match the expected cell; publication refused.")
            for error in identity_result.errors:
                print(f"  {error}")
            return False
    elif expected_quantity_ids is not None:
        grid_result = validate_grid_rows(
            (
                {
                    "model_name": record.model_name,
                    "prompt_version": record.prompt_version,
                    "quantity_id": record.quantity_id,
                    "run_index": record.run_index,
                    "parsed_ok": record.parsed_ok,
                }
                for record in all_records
            ),
            model_name=model_name,
            prompt_version=prompt_version,
            quantity_ids=quantity_ids,
            n_runs=n_runs,
        )
        if not grid_result.ok:
            print("Staging grid is incomplete or invalid; publication refused.")
            for error in grid_result.errors:
                print(f"  {error}")
            return False

    quantity_order = {
        quantity_id: index for index, quantity_id in enumerate(quantity_ids)
    }
    all_records.sort(
        key=lambda record: (
            quantity_order.get(record.quantity_id, len(quantity_order)),
            record.run_index,
        )
    )
    runs = build_run_grid(
        model_names=[model_name],
        quantity_ids=quantity_ids,
        n_runs=n_runs,
        prompt_version=prompt_version,
        tool_regime=tool_regime,
    )
    summaries = summarize_run_results(all_records, request_logs=all_request_logs)

    # Materialize every artifact away from the canonical directory first.
    # Each final os.replace is atomic. Existing artifacts are backed up before
    # publication so an I/O failure partway through can roll the whole set back
    # instead of leaving a mixed old/new canonical batch.
    target_dir.parent.mkdir(parents=True, exist_ok=True)
    temp_dir = Path(
        tempfile.mkdtemp(
            prefix=f".{target_dir.name}.publish-",
            dir=target_dir.parent,
        )
    )
    try:
        artifacts = (
            "prompt_grid.csv",
            "runs.csv",
            "requests.jsonl",
            "requests.csv",
            "summary.csv",
            # Publish runs.jsonl last: it is the authoritative completeness
            # artifact consumed by the exact-grid checker.
            "runs.jsonl",
        )
        write_run_grid_csv(temp_dir / "prompt_grid.csv", runs)
        _write_jsonl(temp_dir / "runs.jsonl", all_records)
        _write_runs_csv(temp_dir / "runs.csv", all_records)
        _write_jsonl(temp_dir / "requests.jsonl", all_request_logs)
        _write_requests_csv(temp_dir / "requests.csv", all_request_logs)
        _write_summary_csv(temp_dir / "summary.csv", summaries)
        if not (temp_dir / "summary.csv").exists():
            (temp_dir / "summary.csv").touch()

        target_existed = target_dir.exists()
        backup_dir = temp_dir / "backup"
        backup_dir.mkdir()
        if target_existed:
            if not target_dir.is_dir():
                print(f"Canonical target is not a directory: {target_dir}")
                return False
            for artifact in artifacts:
                existing = target_dir / artifact
                if existing.exists():
                    shutil.copy2(existing, backup_dir / artifact)

        target_dir.mkdir(parents=True, exist_ok=True)
        published: list[str] = []
        try:
            for artifact in artifacts:
                os.replace(temp_dir / artifact, target_dir / artifact)
                published.append(artifact)
        except OSError as exc:
            rollback_errors: list[str] = []
            for artifact in reversed(published):
                target = target_dir / artifact
                backup = backup_dir / artifact
                try:
                    if backup.exists():
                        os.replace(backup, target)
                    else:
                        target.unlink(missing_ok=True)
                except OSError as rollback_exc:
                    rollback_errors.append(f"{artifact}: {rollback_exc}")
            if not target_existed:
                try:
                    target_dir.rmdir()
                except OSError as rollback_exc:
                    rollback_errors.append(f"target directory: {rollback_exc}")
            if rollback_errors:
                details = "; ".join(rollback_errors)
                raise RuntimeError(
                    f"Publication failed ({exc}); rollback also failed: {details}"
                ) from exc
            print(f"Publication failed and was rolled back: {exc}")
            return False
    finally:
        shutil.rmtree(temp_dir, ignore_errors=True)
    print(
        f"Merged {len(all_records)} records and {len(all_request_logs)} "
        f"request logs into {target_dir}"
    )
    return True


CANONICAL_BATCH_FOR = {
    "main": "elasticities-batch15",
    "armington-clarify": "armington-clarify-batch15",
    "ies-clarify": "ies-clarify-batch15",
}


def quarantine_cell(cell_dir: Path, staging_root: Path) -> Path:
    """Move a stale staged cell out of staging without deleting it.

    The cell holds paid request logs and raw answers, so it is kept, but as a
    sibling of ``staging_root``: merge_per_quantity reads every subdirectory
    of staging_root and must never publish it.
    """
    quarantine_root = staging_root.with_name(f"{staging_root.name}.quarantine")
    quarantine_root.mkdir(parents=True, exist_ok=True)
    stem = f"{cell_dir.name}-{time.strftime('%Y%m%dT%H%M%S')}"
    destination = quarantine_root / stem
    suffix = 1
    while destination.exists():
        suffix += 1
        destination = quarantine_root / f"{stem}-{suffix}"
    shutil.move(str(cell_dir), str(destination))
    return destination


def cell_problems(
    cell_dir: Path, identity: CellIdentity, *, require_parsed: bool
) -> tuple[str, ...]:
    """Return why the runs in ``cell_dir`` do not match ``identity``."""
    rows, read_errors = load_jsonl_rows([cell_dir / "runs.jsonl"])
    result = validate_cell_identity(rows, identity, require_parsed=require_parsed)
    return tuple(read_errors) + result.errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", required=True)
    parser.add_argument(
        "--prompt-version",
        default=None,
        help="optional; must equal the version implied by --batch",
    )
    parser.add_argument(
        "--batch",
        choices=list(CANONICAL_BATCH_FOR),
        default="main",
    )
    parser.add_argument("--per-quantity-timeout", type=int, default=900)
    parser.add_argument(
        "--fresh",
        action="store_true",
        help="discard any staged per-quantity results instead of resuming",
    )
    args = parser.parse_args()

    if args.model not in PROVIDER_FOR_MODEL:
        print(f"Unknown model: {args.model}", file=sys.stderr)
        return 2

    canonical_batch = CANONICAL_BATCH_FOR[args.batch]
    prompt_version = BATCH_PROMPT_VERSIONS[canonical_batch]
    # A mismatched override is how claude-opus-4.7's armington-clarify
    # cell came to hold v4-tagged rows; the batch alone decides the version.
    if args.prompt_version is not None and args.prompt_version != prompt_version:
        print(
            f"--prompt-version {args.prompt_version!r} disagrees with --batch "
            f"{args.batch!r}, which elicits {prompt_version!r}",
            file=sys.stderr,
        )
        return 2

    if args.batch == "main":
        qids = [q.id for q in list_quantities()]
    elif args.batch == "armington-clarify":
        qids = ["trade.armington_elasticity.import_domestic"]
    else:
        qids = ["household.intertemporal_elasticity_of_substitution"]
    target_dir = REPO_ROOT / "results" / f"{args.model}-{canonical_batch}"
    identity = expected_cell_identity(
        model_name=args.model,
        runner=PROVIDER_FOR_MODEL[args.model],
        prompt_version=prompt_version,
        quantity_ids=qids,
    )

    staging_root = REPO_ROOT / "results" / f"_perquantity_{args.model}_{args.batch}"
    if staging_root.exists() and args.fresh:
        shutil.rmtree(staging_root)
    staging_root.mkdir(parents=True, exist_ok=True)

    print(f"Running {args.model} / {args.batch} per-quantity ({len(qids)} quantities)")
    start = time.time()
    successes = 0
    for i, qid in enumerate(qids, 1):
        sub = staging_root / qid.replace(".", "_")
        cell_identity = identity.restricted_to([qid])
        if sub.exists():
            # A cell full of provider failures (e.g. upstream 429s) must
            # redo on resume, not skip as staged.
            stale = cell_problems(sub, cell_identity, require_parsed=True)
            if not stale:
                print(
                    f"[{time.strftime('%H:%M:%S')}] {i}/{len(qids)} {qid} "
                    "SKIP (staged cell matches the expected identity)"
                )
                successes += 1
                continue
            moved_to = quarantine_cell(sub, staging_root)
            print(f"  staged {qid} is not reusable; quarantined to {moved_to}:")
            for error in stale:
                print(f"    {error}")
        print(f"[{time.strftime('%H:%M:%S')}] {i}/{len(qids)} {qid}")
        if not run_one_quantity(
            args.model,
            qid,
            prompt_version,
            sub,
            per_quantity_timeout=args.per_quantity_timeout,
        ):
            continue
        produced = cell_problems(sub, cell_identity, require_parsed=False)
        if produced:
            print(f"  child output for {qid} does not match the expected cell:")
            for error in produced:
                print(f"    {error}")
            continue
        successes += 1

    elapsed = time.time() - start
    print(f"\nPer-quantity phase done: {successes}/{len(qids)} in {elapsed:.0f}s")

    if successes != len(qids):
        print(
            "One or more quantity children failed; preserving staging and "
            "leaving the canonical target untouched."
        )
        return 1

    published = merge_per_quantity(
        staging_root,
        target_dir,
        args.model,
        prompt_version,
        n_runs=identity.n_runs,
        identity=identity,
    )
    if not published:
        print("Preserved staging; canonical target was not published.")
        return 1
    shutil.rmtree(staging_root, ignore_errors=True)
    unresolved = cell_problems(target_dir, identity, require_parsed=True)
    if unresolved:
        print("Canonical grid contains unresolved runs.")
        for error in unresolved:
            print(f"  {error}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
