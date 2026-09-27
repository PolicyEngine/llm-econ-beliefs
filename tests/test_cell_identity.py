"""Properties of the cell-identity check that guards every resume path.

A stored cell may stand in for a fresh elicitation only when it is the exact
grid and every row carries the provider tag, tool regime and prompt text the
elicitation would send.  Valid cells here come from the real prompt builder
and experiment writer, so the accepting side of each property is exercised
on the artifact shape the runners actually produce.
"""

from __future__ import annotations

import sys
from copy import deepcopy
from pathlib import Path

import pytest
from hypothesis import given, settings, strategies as st

from llm_econ_beliefs import list_quantities
from llm_econ_beliefs.model_registry import PANEL_MODEL_IDS
from llm_econ_beliefs.models import RunResult
from llm_econ_beliefs.runner import build_run_grid


REPO_ROOT = Path(__file__).resolve().parents[1]
for path in (REPO_ROOT / "scripts", Path(__file__).resolve().parent):
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))

import check_panel_grid  # noqa: E402
from cell_fixtures import MODEL, PROVIDER_TAG, RUNNER, elicit_cell  # noqa: E402
from run_v4_per_quantity import PROVIDER_FOR_MODEL  # noqa: E402
from verify_paper_prose import (  # noqa: E402
    ORIGINAL_WORDING_MODELS,
    SIGN_CLARIFIED_QUANTITIES,
)


QUANTITY_IDS = [quantity.id for quantity in list_quantities()]
IDENTITY = check_panel_grid.expected_cell_identity(
    model_name=MODEL,
    runner=RUNNER,
    prompt_version="v4",
    quantity_ids=QUANTITY_IDS,
)
PROPERTY_SETTINGS = settings(
    max_examples=150, derandomize=True, database=None, deadline=None
)


@pytest.fixture(scope="module")
def valid_rows(tmp_path_factory) -> list[dict]:
    return elicit_cell(tmp_path_factory.mktemp("cell"), QUANTITY_IDS)


def _check(rows, *, canonical: bool = False, require_parsed: bool = True):
    return check_panel_grid.validate_cell_identity(
        rows,
        IDENTITY,
        require_parsed=require_parsed,
        exact_prompts=not canonical,
        accept_legacy_provider_tags=canonical,
    )


def test_identity_matches_what_the_experiment_writer_records(valid_rows):
    assert len(valid_rows) == len(QUANTITY_IDS) * 15
    assert IDENTITY.quantity_ids == tuple(QUANTITY_IDS)
    assert {row["provider"] for row in valid_rows} == {IDENTITY.provider}
    assert {
        (row["quantity_id"], row["prompt"]) for row in valid_rows
    } == set(IDENTITY.prompts.items())
    assert _check(valid_rows).ok
    assert _check(valid_rows, canonical=True).ok


def test_run_results_are_accepted_like_mappings(valid_rows):
    records = [RunResult(**row) for row in valid_rows]
    assert _check(records).ok


@PROPERTY_SETTINGS
@given(order=st.permutations(range(len(QUANTITY_IDS) * 15)))
def test_valid_cell_is_accepted_in_any_row_order(valid_rows, order):
    shuffled = [valid_rows[index] for index in order]
    assert _check(shuffled).ok
    assert _check(shuffled, canonical=True).ok


def _mutation(draw, row: dict):
    """Change exactly one identity field of one row; return (field, value)."""
    field = draw(
        st.sampled_from(
            [
                "prompt",
                "provider",
                "tool_regime",
                "model_name",
                "prompt_version",
                "quantity_id",
                "run_index_duplicate",
                "run_index_out_of_range",
            ]
        )
    )
    if field == "prompt":
        prompt = row["prompt"]
        position = draw(st.integers(0, len(prompt) - 1))
        operation = draw(st.sampled_from(["insert", "replace", "delete"]))
        if operation == "delete":
            return field, prompt[:position] + prompt[position + 1 :]
        char = draw(st.characters(codec="utf-8").filter(lambda c: c != prompt[position]))
        if operation == "insert":
            return field, prompt[:position] + char + prompt[position:]
        return field, prompt[:position] + char + prompt[position + 1 :]
    if field == "provider":
        return field, draw(
            st.sampled_from(
                ["openai", "litellm", "litellm_completion", "anthropic", "openai_responses", ""]
            )
            | st.text(max_size=20).filter(lambda value: value != PROVIDER_TAG)
        )
    if field == "tool_regime":
        return field, draw(st.text(max_size=10).filter(lambda value: value != "none"))
    if field == "model_name":
        return field, draw(st.text(max_size=20).filter(lambda value: value != MODEL))
    if field == "prompt_version":
        return field, draw(
            st.sampled_from(["v2", "v3", "armington-clarify", "ies-clarify"])
            | st.text(max_size=10).filter(lambda value: value != "v4")
        )
    if field == "quantity_id":
        return field, draw(
            st.sampled_from(QUANTITY_IDS).filter(lambda value: value != row["quantity_id"])
            | st.text(max_size=20).filter(lambda value: value not in QUANTITY_IDS)
        )
    if field == "run_index_duplicate":
        return "run_index", draw(
            st.integers(1, 15).filter(lambda value: value != row["run_index"])
        )
    return "run_index", draw(st.integers(max_value=0) | st.integers(min_value=16))


@PROPERTY_SETTINGS
@given(data=st.data())
def test_any_single_field_mutation_of_one_row_is_rejected(valid_rows, data):
    rows = deepcopy(valid_rows)
    index = data.draw(st.integers(0, len(rows) - 1), label="row")
    field, value = _mutation(data.draw, rows[index])
    rows[index][field] = value

    assert not _check(rows).ok
    assert not _check(rows, require_parsed=False).ok
    # The canonical mode forgives only a legacy alias of the right tag; a
    # one-row prompt change still splits the quantity into two texts.
    legacy_alias = (
        field == "provider"
        and check_panel_grid.LEGACY_PROVIDER_TAGS.get(value) == PROVIDER_TAG
    )
    assert _check(rows, canonical=True).ok is legacy_alias


def test_uniform_prompt_drift_passes_only_the_canonical_check(valid_rows):
    rows = deepcopy(valid_rows)
    drifted = "labor_supply.income_elasticity.prime_age"
    for row in rows:
        if row["quantity_id"] == drifted:
            row["prompt"] = row["prompt"] + " (original wording)"

    strict = _check(rows)
    assert not strict.ok
    assert any("differs from the current builder" in error for error in strict.errors)
    assert _check(rows, canonical=True).ok
    assert check_panel_grid.drifted_prompt_quantities(rows, IDENTITY) == [drifted]


@pytest.mark.parametrize("prompt", ["", "   ", None, 7])
def test_missing_or_empty_prompts_are_rejected_in_every_mode(valid_rows, prompt):
    rows = deepcopy(valid_rows)
    for row in rows:
        if row["quantity_id"] == QUANTITY_IDS[0]:
            row["prompt"] = prompt
    for canonical in (False, True):
        result = _check(rows, canonical=canonical)
        assert any("prompt is missing or empty" in error for error in result.errors)


def test_legacy_provider_tags_are_normalized_only_when_allowed(valid_rows):
    legacy = [dict(row, provider="openai") for row in valid_rows]
    assert not _check(legacy).ok
    assert _check(legacy, canonical=True).ok

    # "litellm" is a legacy alias, but of another serving path.
    other_path = [dict(row, provider="litellm") for row in valid_rows]
    assert not _check(other_path, canonical=True).ok


def test_unparsed_rows_fail_only_when_parsing_is_required(valid_rows):
    rows = [dict(row, parsed_ok=False) for row in valid_rows]
    assert _check(rows, require_parsed=False).ok
    assert not _check(rows).ok


def test_changed_prompt_version_is_rejected_even_with_identical_text(valid_rows):
    quantity_id = "household.annual_discount_factor"
    same_text = build_run_grid(
        model_names=[MODEL],
        quantity_ids=[quantity_id],
        n_runs=1,
        prompt_version="armington-clarify",
    )[0].prompt
    assert same_text == IDENTITY.prompts[quantity_id]
    rows = [
        dict(row, prompt_version="armington-clarify")
        if row["quantity_id"] == quantity_id
        else row
        for row in valid_rows
    ]
    assert not _check(rows).ok
    assert not _check(rows, canonical=True).ok


def test_restricted_identity_keeps_prompts_and_rejects_unknown_quantities():
    quantity_id = QUANTITY_IDS[3]
    restricted = IDENTITY.restricted_to([quantity_id])
    assert restricted.quantity_ids == (quantity_id,)
    assert restricted.prompts[quantity_id] == IDENTITY.prompts[quantity_id]
    assert (restricted.provider, restricted.tool_regime, restricted.n_runs) == (
        IDENTITY.provider,
        IDENTITY.tool_regime,
        IDENTITY.n_runs,
    )
    with pytest.raises(KeyError):
        IDENTITY.restricted_to(["not.a.quantity"])
    with pytest.raises(ValueError):
        check_panel_grid.CellIdentity(
            model_name=MODEL, provider=PROVIDER_TAG, prompt_version="v4",
            tool_regime="none", prompts={},
        )
    with pytest.raises(TypeError):
        IDENTITY.prompts[quantity_id] = "edited"  # type: ignore[index]


def test_unreadable_run_files_are_reported_not_raised(tmp_path: Path):
    runs = tmp_path / "runs.jsonl"
    runs.write_bytes(b'{"model_name": "\xff\xfe"}\n')
    rows, errors = check_panel_grid.load_jsonl_rows([runs])
    assert rows == []
    assert errors and errors[0].startswith("unreadable file:")


# Committed archives: the canonical check must accept every published main
# cell as it stands, or --skip-complete would re-elicit the panel.
@pytest.mark.parametrize("model_name", PANEL_MODEL_IDS)
def test_committed_main_cells_pass_the_canonical_identity_check(model_name: str):
    identity = check_panel_grid.expected_cell_identity(
        model_name=model_name,
        runner=PROVIDER_FOR_MODEL[model_name],
        prompt_version="v4",
        quantity_ids=check_panel_grid.quantity_ids_for_batch("elasticities-batch15"),
    )
    result, drifted = check_panel_grid.check_canonical_cell(
        REPO_ROOT / "results" / f"{model_name}-elasticities-batch15",
        identity,
        require_parsed=True,
    )
    assert result.ok, result.errors
    # exact_prompts=False exists for exactly this disclosed wording split.
    expected_drift = (
        sorted(SIGN_CLARIFIED_QUANTITIES) if model_name in ORIGINAL_WORDING_MODELS else []
    )
    assert drifted == expected_drift


def test_committed_legacy_provider_tags_are_confined_to_three_models():
    needs_legacy = set()
    for model_name in PANEL_MODEL_IDS:
        identity = check_panel_grid.expected_cell_identity(
            model_name=model_name,
            runner=PROVIDER_FOR_MODEL[model_name],
            prompt_version="v4",
            quantity_ids=check_panel_grid.quantity_ids_for_batch("elasticities-batch15"),
        )
        rows, errors = check_panel_grid.load_jsonl_rows(
            [REPO_ROOT / "results" / f"{model_name}-elasticities-batch15" / "runs.jsonl"]
        )
        assert not errors
        strict_tags = check_panel_grid.validate_cell_identity(
            rows, identity, require_parsed=True, exact_prompts=False
        )
        if not strict_tags.ok:
            needs_legacy.add(model_name)
    assert needs_legacy == {"gpt-5.5", "grok-4.3", "qwen-3.7-max"}
