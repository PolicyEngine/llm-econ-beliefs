"""Run cells written by the real prompt builder and experiment writer.

Nothing here calls a provider: the OpenAI batch hook is a stub returning one
fixed, parseable belief per requested draw.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Sequence

from llm_econ_beliefs.experiment import run_openai_experiment
from llm_econ_beliefs.models import ProviderBatchResult


MODEL = "gpt-5.4"
RUNNER = "openai"
PROVIDER_TAG = "openai_chat_completions"
STUB_ANSWER = json.dumps(
    {
        "interpretation": "stub",
        "point_estimate": 0.5,
        "quantiles": {"p05": 0.1, "p25": 0.3, "p50": 0.5, "p75": 0.7, "p95": 0.9},
        "citations": [],
        "reasoning_summary": "stub",
    }
)


def stub_openai_batch(prompt: str, model_name: str, n: int) -> ProviderBatchResult:
    return ProviderBatchResult(
        outputs=[STUB_ANSWER] * n,
        request_id="stub",
        usage={"prompt_tokens": 5, "completion_tokens": 5, "total_tokens": 10},
    )


def elicit_cell(
    output_dir: Path,
    quantity_ids: Sequence[str],
    *,
    prompt_version: str = "v4",
    n_runs: int = 15,
    model_name: str = MODEL,
) -> list[dict]:
    """Write a cell the way run_v4_full_panel.exec_cell's OpenAI branch does."""
    run_openai_experiment(
        quantity_ids=quantity_ids,
        n_runs=n_runs,
        output_dir=output_dir,
        model_name=model_name,
        prompt_version=prompt_version,
        tool_regime="none",
        batch_size=5,
        invoke_batch=stub_openai_batch,
    )
    return read_rows(Path(output_dir) / "runs.jsonl")


def read_rows(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]


def write_rows(path: Path, rows: Sequence[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("".join(json.dumps(row) + "\n" for row in rows))
