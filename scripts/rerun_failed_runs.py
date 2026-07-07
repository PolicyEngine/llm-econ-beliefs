"""Re-elicit failed runs in a merged batch directory, in place.

Failed runs are infrastructure artifacts (empty responses from exhausted
completion budgets, missing forced tool calls, transient 4xx errors), not
content, so replacing them with fresh independent draws does not select on
elicited values. Each failed run slot gets up to ``--attempts`` fresh draws;
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

    provider = PROVIDER_FOR_MODEL[args.model]
    target_dir = REPO_ROOT / "results" / f"{args.model}-{args.batch}"
    runs_path = target_dir / "runs.jsonl"
    records = load_jsonl(runs_path, RunResult)
    request_logs = load_jsonl(target_dir / "requests.jsonl", RequestLog)
    next_request_index = max(
        (log.request_index for log in request_logs), default=0
    ) + 1

    failed_positions = [
        index for index, record in enumerate(records) if not record.parsed_ok
    ]
    if not failed_positions:
        print(f"{args.model} / {args.batch}: no failed runs.")
        return 0
    print(f"{args.model} / {args.batch}: re-eliciting {len(failed_positions)} failed runs")

    fixed = 0
    for index in failed_positions:
        failed = records[index]
        replacement = None
        last_error = failed.error
        for attempt in range(1, args.attempts + 1):
            try:
                batch_result = invoke_once(provider, failed.model_name, failed.prompt)
                raw_response = batch_result.outputs[0]
                parsed = parse_belief_response(
                    raw_response, quantity_id=failed.quantity_id
                )
                if batch_result.request_id is not None or batch_result.usage:
                    request_logs.append(
                        _request_log_from_batch_result(
                            provider=provider,
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
                    run_like, parsed, raw_response, provider=provider
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
                provider=provider,
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
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
