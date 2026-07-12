"""Re-elicit failed runs in a merged batch directory, in place.

Failed runs are infrastructure artifacts (empty responses from exhausted
completion budgets, missing forced tool calls, transient 4xx errors). The
replacement policy conditions only on failure status, but truncation-type
failures correlate with response length, so replacement is not provably
independent of elicited values; see results/failure-manifest.csv and the
paper's harness-disclosure appendix. Each failed run slot gets up to
``--attempts`` fresh draws;
slots that still fail keep an error record. Request logs from reruns are
appended and the summary artifacts are rewritten.

Usage:
    .venv/bin/python scripts/rerun_failed_runs.py --model gpt-5.5 --batch elasticities-batch15
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from run_v4_per_quantity import PROVIDER_FOR_MODEL
from check_panel_grid import check_batch_directory

from llm_econ_beliefs.experiment import (
    _record_from_parsed,
    _request_log_from_batch_result,
    _write_jsonl,
    _write_requests_csv,
    _write_runs_csv,
    _write_summary_csv,
    summarize_run_results,
)
from llm_econ_beliefs.models import RequestLog, RunResult
from llm_econ_beliefs.parse import parse_belief_response
from llm_econ_beliefs.provider_tags import provider_tag_for_runner
from llm_econ_beliefs.providers import (
    run_anthropic_prompt_logged,
    run_litellm_prompt_logged,
    run_openai_prompt_batch_logged,
)


def load_jsonl(path: Path, cls):
    records = []
    if not path.exists():
        return records
    with path.open() as handle:
        for line in handle:
            line = line.strip()
            if line:
                records.append(cls(**json.loads(line)))
    return records


def invoke_once(provider: str, model_name: str, prompt: str):
    if provider == "openai":
        return run_openai_prompt_batch_logged(prompt, model_name=model_name, n=1)
    if provider == "anthropic":
        return run_anthropic_prompt_logged(prompt, model_name=model_name)
    return run_litellm_prompt_logged(prompt, model_name=model_name)


def report_grid_errors(model_name: str, batch: str, errors: tuple[str, ...]) -> None:
    print(f"{model_name} / {batch}: unresolved panel grid:")
    for error in errors:
        print(f"  {error}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", required=True)
    parser.add_argument(
        "--batch",
        default="elasticities-batch15",
        choices=[
            "elasticities-batch15",
            "armington-clarify-batch15",
            "ies-clarify-batch15",
        ],
    )
    parser.add_argument("--attempts", type=int, default=3)
    args = parser.parse_args()

    if args.model not in PROVIDER_FOR_MODEL:
        print(f"Unknown model: {args.model}", file=sys.stderr)
        return 2
    if args.attempts <= 0:
        print("--attempts must be positive", file=sys.stderr)
        return 2

    provider = PROVIDER_FOR_MODEL[args.model]
    # Tag records with the same provider label the main experiment driver
    # writes, so log filters see one consistent value per path.
    log_provider = provider_tag_for_runner(provider)
    target_dir = REPO_ROOT / "results" / f"{args.model}-{args.batch}"
    runs_path = target_dir / "runs.jsonl"
    records = load_jsonl(runs_path, RunResult)
    request_logs = load_jsonl(target_dir / "requests.jsonl", RequestLog)
    next_request_index = max((log.request_index for log in request_logs), default=0) + 1

    failed_positions = [
        index for index, record in enumerate(records) if not record.parsed_ok
    ]
    if not failed_positions:
        grid_result = check_batch_directory(
            REPO_ROOT / "results",
            model_name=args.model,
            batch=args.batch,
            require_parsed=True,
        )
        if grid_result.ok:
            print(f"{args.model} / {args.batch}: no failed runs; grid complete.")
            return 0
        report_grid_errors(args.model, args.batch, grid_result.errors)
        return 1
    print(
        f"{args.model} / {args.batch}: re-eliciting {len(failed_positions)} failed runs"
    )

    # Archive the failed records before replacing them so the replacement
    # policy stays auditable (see results/failure-manifest.csv).
    archive_path = target_dir / "failed-runs-archive.jsonl"
    with archive_path.open("a") as handle:
        from dataclasses import asdict

        for index in failed_positions:
            handle.write(json.dumps(asdict(records[index])) + "\n")
    print(f"archived {len(failed_positions)} failed records to {archive_path}")

    fixed = 0
    for index in failed_positions:
        failed = records[index]
        replacement = None
        last_error = failed.error
        for attempt in range(1, args.attempts + 1):
            try:
                batch_result = invoke_once(provider, failed.model_name, failed.prompt)
                # Record every completed provider request before inspecting or
                # parsing its output.  Invalid response content must not erase
                # the request id, usage, or cost of a paid request.
                request_logs.append(
                    _request_log_from_batch_result(
                        provider=log_provider,
                        model_name=failed.model_name,
                        quantity_id=failed.quantity_id,
                        prompt_version=failed.prompt_version,
                        tool_regime=failed.tool_regime,
                        batch_size=1,
                        request_index=next_request_index,
                        batch_result=batch_result,
                    )
                )
                next_request_index += 1
                raw_response = batch_result.outputs[0]
                parsed = parse_belief_response(
                    raw_response, quantity_id=failed.quantity_id
                )
                run_like = type(
                    "RunLike",
                    (),
                    {
                        "model_name": failed.model_name,
                        "quantity_id": failed.quantity_id,
                        "run_index": failed.run_index,
                        "prompt_version": failed.prompt_version,
                        "tool_regime": failed.tool_regime,
                        "prompt": failed.prompt,
                    },
                )()
                replacement = _record_from_parsed(
                    run_like, parsed, raw_response, provider=log_provider
                )
                break
            except Exception as exc:
                last_error = str(exc)
                print(
                    f"  {failed.quantity_id} run {failed.run_index} "
                    f"attempt {attempt}: {last_error[:90]}"
                )
        if replacement is not None:
            records[index] = replacement
            fixed += 1
        else:
            records[index] = RunResult(
                provider=log_provider,
                model_name=failed.model_name,
                quantity_id=failed.quantity_id,
                run_index=failed.run_index,
                prompt_version=failed.prompt_version,
                tool_regime=failed.tool_regime,
                prompt=failed.prompt,
                raw_response=None,
                parsed_ok=False,
                error=last_error,
            )

    _write_jsonl(runs_path, records)
    _write_runs_csv(target_dir / "runs.csv", records)
    if request_logs:
        _write_jsonl(target_dir / "requests.jsonl", request_logs)
        _write_requests_csv(target_dir / "requests.csv", request_logs)
    summaries = summarize_run_results(records, request_logs=request_logs)
    _write_summary_csv(target_dir / "summary.csv", summaries)

    ok = sum(1 for record in records if record.parsed_ok)
    print(
        f"Fixed {fixed}/{len(failed_positions)}; directory now {ok}/{len(records)} parsed"
    )
    grid_result = check_batch_directory(
        REPO_ROOT / "results",
        model_name=args.model,
        batch=args.batch,
        require_parsed=True,
    )
    if not grid_result.ok:
        report_grid_errors(args.model, args.batch, grid_result.errors)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
