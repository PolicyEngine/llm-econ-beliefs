import inspect

import pytest
from hypothesis import given, settings, strategies as st

from llm_econ_beliefs import RequestLog, estimate_request_cost, lookup_model_pricing
from llm_econ_beliefs.experiment import run_anthropic_experiment


def test_lookup_model_pricing_supports_snapshot_names():
    pricing = lookup_model_pricing("openai_chat_completions", "gpt-5.4-mini-2026-03-17")

    assert pricing is not None
    assert pricing.input_per_million_usd == 0.75
    assert pricing.cached_input_per_million_usd == 0.075
    assert pricing.output_per_million_usd == 4.5


def test_estimate_request_cost_uses_cached_and_uncached_prompt_rates():
    request_log = RequestLog(
        provider="openai_chat_completions",
        model_name="gpt-5.4-mini",
        quantity_id="labor_supply.frisch_elasticity.prime_age",
        request_index=1,
        prompt_version="v1",
        tool_regime="none",
        batch_size=5,
        prompt_tokens=1000,
        completion_tokens=500,
        total_tokens=1500,
        cached_prompt_tokens=200,
    )

    enriched = estimate_request_cost(request_log)

    assert enriched.estimated_input_cost_usd == 800 * 0.75 / 1_000_000
    assert enriched.estimated_cached_input_cost_usd == 200 * 0.075 / 1_000_000
    assert enriched.estimated_output_cost_usd == 500 * 4.5 / 1_000_000
    assert enriched.estimated_total_cost_usd == (
        enriched.estimated_input_cost_usd
        + enriched.estimated_cached_input_cost_usd
        + enriched.estimated_output_cost_usd
    )


def test_estimate_request_cost_includes_openai_response_tool_costs():
    request_log = RequestLog(
        provider="openai_responses",
        model_name="gpt-5.4-mini",
        quantity_id="labor_supply.frisch_elasticity.prime_age",
        request_index=1,
        prompt_version="v3",
        tool_regime="full",
        batch_size=1,
        prompt_tokens=100,
        completion_tokens=100,
        total_tokens=200,
        web_search_call_count=2,
        code_interpreter_call_count=1,
    )

    enriched = estimate_request_cost(request_log)

    assert enriched.estimated_tool_cost_usd == 0.05
    assert enriched.estimated_total_cost_usd == (
        enriched.estimated_input_cost_usd
        + enriched.estimated_cached_input_cost_usd
        + enriched.estimated_output_cost_usd
        + enriched.estimated_tool_cost_usd
    )


def test_estimate_request_cost_preserves_precomputed_total():
    request_log = RequestLog(
        provider="litellm_completion",
        model_name="claude-haiku-4.5",
        quantity_id="labor_supply.frisch_elasticity.prime_age",
        request_index=1,
        prompt_version="v2",
        tool_regime="none",
        batch_size=1,
        prompt_tokens=100,
        completion_tokens=200,
        total_tokens=300,
        estimated_total_cost_usd=0.123,
    )

    enriched = estimate_request_cost(request_log)

    assert enriched.estimated_total_cost_usd == 0.123
    assert enriched.estimated_input_cost_usd is None


def test_lookup_model_pricing_supports_gpt_55():
    pricing = lookup_model_pricing("openai_chat_completions", "gpt-5.5")

    assert pricing is not None
    assert pricing.input_per_million_usd == 5.00
    assert pricing.cached_input_per_million_usd == 0.50
    assert pricing.output_per_million_usd == 30.00


def test_lookup_model_pricing_supports_anthropic_panel_names():
    fable = lookup_model_pricing("anthropic", "claude-fable-5")
    opus = lookup_model_pricing("anthropic", "claude-opus-4.8")
    sonnet = lookup_model_pricing("anthropic", "claude-sonnet-5")

    assert fable is not None and fable.input_per_million_usd == 10.00
    assert fable.output_per_million_usd == 50.00
    assert opus is not None and opus.output_per_million_usd == 25.00
    assert sonnet is not None and sonnet.output_per_million_usd == 10.00
    assert lookup_model_pricing("anthropic", "unknown-model") is None


def test_lookup_model_pricing_supports_claude_sonnet_55():
    pricing = lookup_model_pricing("anthropic", "claude-sonnet-5-5")

    assert pricing is not None
    assert pricing.input_per_million_usd == 2.00
    assert pricing.cached_input_per_million_usd == 0.20
    assert pricing.output_per_million_usd == 10.00


def test_anthropic_experiment_default_model_has_pricing():
    default = inspect.signature(run_anthropic_experiment).parameters["model_name"].default

    assert lookup_model_pricing("anthropic", default) is not None


@settings(max_examples=200, derandomize=True, database=None)
@given(
    prompt_tokens=st.integers(min_value=0, max_value=10_000_000),
    cached_tokens=st.integers(min_value=0, max_value=10_000_000),
    completion_tokens=st.integers(min_value=0, max_value=10_000_000),
)
def test_claude_sonnet_55_cost_is_the_sum_of_its_priced_parts(
    prompt_tokens: int, cached_tokens: int, completion_tokens: int
):
    enriched = estimate_request_cost(
        RequestLog(
            provider="anthropic",
            model_name="claude-sonnet-5-5",
            quantity_id="household.annual_discount_factor",
            request_index=1,
            prompt_version="v4",
            tool_regime="none",
            batch_size=1,
            prompt_tokens=prompt_tokens,
            cached_prompt_tokens=cached_tokens,
            completion_tokens=completion_tokens,
        )
    )

    cached = min(cached_tokens, prompt_tokens)
    assert enriched.estimated_input_cost_usd == pytest.approx(
        (prompt_tokens - cached) * 2.00 / 1_000_000
    )
    assert enriched.estimated_cached_input_cost_usd == pytest.approx(
        cached * 0.20 / 1_000_000
    )
    assert enriched.estimated_output_cost_usd == pytest.approx(
        completion_tokens * 10.00 / 1_000_000
    )
    assert enriched.estimated_tool_cost_usd == 0.0
    assert enriched.estimated_total_cost_usd == pytest.approx(
        enriched.estimated_input_cost_usd
        + enriched.estimated_cached_input_cost_usd
        + enriched.estimated_output_cost_usd
    )
    assert enriched.estimated_total_cost_usd >= 0.0


def test_estimate_request_cost_fills_anthropic_costs():
    request_log = RequestLog(
        provider="anthropic",
        model_name="claude-fable-5",
        quantity_id="labor_supply.frisch_elasticity.prime_age",
        request_index=1,
        prompt_version="v4",
        tool_regime="none",
        batch_size=1,
        prompt_tokens=700,
        completion_tokens=350,
        total_tokens=1050,
    )

    enriched = estimate_request_cost(request_log)

    assert enriched.estimated_input_cost_usd == 700 * 10.00 / 1_000_000
    assert enriched.estimated_output_cost_usd == 350 * 50.00 / 1_000_000
    assert enriched.estimated_total_cost_usd == (
        enriched.estimated_input_cost_usd
        + enriched.estimated_cached_input_cost_usd
        + enriched.estimated_output_cost_usd
        + enriched.estimated_tool_cost_usd
    )
