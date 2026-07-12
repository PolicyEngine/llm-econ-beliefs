from pathlib import Path

import pytest

from llm_econ_beliefs.experiment import summarize_run_results
from llm_econ_beliefs.models import RequestLog, RunResult
from llm_econ_beliefs.pricing import lookup_model_pricing
from paper.build_tables import (
    ComparisonRow,
    build_income_delta_table,
    build_model_overview_table,
)
from scripts import build_comparison_artifacts


def comparison_row(
    quantity_id: str,
    cost_per_run_usd: float | None,
) -> ComparisonRow:
    return ComparisonRow(
        model_name="gpt-5.6-sol",
        quantity_id=quantity_id,
        n_successful_runs=15,
        pooled_point_estimate=0.5,
        pooled_lower=0.25,
        pooled_upper=0.75,
        pooled_width=0.5,
        cost_per_run_usd=cost_per_run_usd,
        source_dir="unused",
    )


def test_gpt_56_pricing_remains_untracked_without_authoritative_rates():
    assert lookup_model_pricing("openai_chat_completions", "gpt-5.6-sol") is None


def test_model_overview_does_not_turn_a_missing_cost_into_zero():
    table = build_model_overview_table(
        [
            comparison_row("quantity.a", 0.25),
            comparison_row("quantity.b", None),
        ]
    )

    assert table[0]["Cost / successful run"] == "—"


def test_model_overview_preserves_a_tracked_zero_cost():
    table = build_model_overview_table([comparison_row("quantity.a", 0.0)])

    assert table[0]["Cost / successful run"] == 0.0


def test_income_delta_renders_an_untracked_cost_as_a_dash():
    table = build_income_delta_table(
        [
            {
                "model_name": "gpt-5.6-sol",
                "old_pooled_point_estimate": "0.4",
                "new_pooled_point_estimate": "0.5",
                "point_estimate_change": "0.1",
                "new_pooled_90_interval": "[0.25, 0.75]",
                "new_cost_per_run_usd": "",
            }
        ]
    )

    assert table[0]["Cost / successful run"] == "—"


@pytest.mark.parametrize(
    ("cost_cells", "expected_total"),
    [(["0.25", ""], None), (["0", "0"], 0.0)],
)
def test_model_rollup_propagates_untracked_costs(
    monkeypatch: pytest.MonkeyPatch,
    cost_cells: list[str],
    expected_total: float | None,
):
    rows = [
        {
            "model_name": "gpt-5.6-sol",
            "n_successful_runs": 15,
            "usage_estimated_total_cost_usd_total": cost,
            "pooled_lower_bound": "0.25",
            "pooled_upper_bound": "0.75",
            "pooled_point_estimate": "0.5",
        }
        for cost in cost_cells
    ]
    monkeypatch.setattr(build_comparison_artifacts, "read_summary_rows", lambda _: rows)

    rollup = build_comparison_artifacts.build_rollup_rows([Path("unused")])[0]

    assert rollup["total_cost_usd"] == expected_total
    if expected_total is None:
        assert rollup["cost_per_successful_run_usd"] is None


def test_experiment_summary_does_not_report_partial_request_costs():
    quantity_id = "household.annual_discount_factor"
    records = [
        RunResult(
            provider="openai_chat_completions",
            model_name="gpt-5.6-sol",
            quantity_id=quantity_id,
            run_index=run_index,
            prompt_version="v4",
            tool_regime="none",
            prompt="prompt",
            raw_response="{}",
            parsed_ok=True,
            point_estimate=0.96,
            quantiles={
                "p05": 0.94,
                "p25": 0.95,
                "p50": 0.96,
                "p75": 0.97,
                "p95": 0.98,
            },
        )
        for run_index in (1, 2)
    ]
    request_logs = [
        RequestLog(
            provider="openai_chat_completions",
            model_name="gpt-5.6-sol",
            quantity_id=quantity_id,
            request_index=1,
            prompt_version="v4",
            tool_regime="none",
            batch_size=1,
            estimated_input_cost_usd=0.10,
            estimated_cached_input_cost_usd=0.01,
            estimated_output_cost_usd=0.20,
            estimated_tool_cost_usd=0.0,
            estimated_total_cost_usd=0.31,
        ),
        RequestLog(
            provider="openai_chat_completions",
            model_name="gpt-5.6-sol",
            quantity_id=quantity_id,
            request_index=2,
            prompt_version="v4",
            tool_regime="none",
            batch_size=1,
        ),
    ]

    summary = summarize_run_results(records, request_logs=request_logs)[0]

    for field in (
        "usage_estimated_input_cost_usd_total",
        "usage_estimated_cached_input_cost_usd_total",
        "usage_estimated_output_cost_usd_total",
        "usage_estimated_tool_cost_usd_total",
        "usage_estimated_total_cost_usd_total",
        "usage_estimated_total_cost_usd_per_successful_run",
    ):
        assert summary[field] is None
