"""Property and regression tests for the parser's numeric contract.

Invariants (each holds for every input the strategies generate):

1. Numeric preservation: a quantile written as a literal numeric token is
   parsed to exactly ``float(token)`` — sign, leading decimal point, and
   exponent included — on both the JSON path and the free-text fallback.
2. Point = p50: every accepted response has ``point_estimate == p50``, and
   ``p05 <= point <= p95``, whatever narrative numbers surround it.
3. Finite: every accepted number is finite.
4. Refusals stay refusals: a quantile that is not a bare number ("N/A (0)",
   "1%", NaN, infinity) is missing, so the response fails to parse.
5. Label integrity: a text quantile comes only from its own label on its own
   line — never from the prefix of another label ("p5" in "p50"), a later
   line, or a digit inside a refusal annotation.
6. Truncated-JSON completion only appends closers; it never alters a value.

The regression fixtures at the bottom are verbatim Gemini 3.5 Flash answers
from results/gemini-3.5-flash-elasticities-batch15/runs.jsonl, whose missing
final brace previously routed them to a text fallback that dropped every
minus sign (audit 2026-09-25).
"""

from __future__ import annotations

import itertools
import json
import math
from pathlib import Path

import pytest
from hypothesis import given, settings, strategies as st

from llm_econ_beliefs import parse_belief_response
from llm_econ_beliefs.parse import QUANTILE_ORDER, _coerce_float

settings.register_profile("parse_invariants", max_examples=300, derandomize=True, database=None)
settings.load_profile("parse_invariants")

finite_floats = st.floats(allow_nan=False, allow_infinity=False, width=64)


def _structured(values, **extra) -> str:
    payload = {"quantiles": dict(zip(QUANTILE_ORDER, values, strict=True))}
    payload.update(extra)
    return json.dumps(payload)


def _text(tokens, *, template="{key}={value}", joiner="\n") -> str:
    return joiner.join(
        template.format(key=key, value=value)
        for key, value in zip(QUANTILE_ORDER, tokens, strict=True)
    )


@st.composite
def numeric_tokens(draw):
    """Literal numeric tokens in the forms models write, with their value."""
    sign = draw(st.sampled_from(["", "-", "+", "\u2212"]))
    form = draw(st.sampled_from(["int", "decimal", "leading_decimal", "exponent"]))
    whole = draw(st.integers(0, 10_000))
    fraction = draw(st.integers(0, 999))
    if form == "int":
        body = str(whole)
    elif form == "decimal":
        body = f"{whole}.{fraction:03d}"
    elif form == "leading_decimal":
        body = f".{fraction:03d}"
    else:
        exponent = draw(st.integers(-12, 12))
        marker = draw(st.sampled_from(["e", "E"]))
        body = f"{whole}.{fraction:03d}{marker}{exponent}"
    token = sign + body
    return token, float(token.replace("\u2212", "-"))


# --- 1. Numeric preservation -------------------------------------------------


@given(st.lists(numeric_tokens(), min_size=5, max_size=5))
def test_text_quantiles_preserve_every_literal_token(tokens):
    parsed = parse_belief_response(_text([token for token, _ in tokens]))
    expected = [value for _, value in tokens]
    running = list(itertools.accumulate(expected, max))
    assert list(parsed.quantiles.values()) == running
    assert parsed.quantiles_repaired == (expected != running)


@given(st.lists(numeric_tokens(), min_size=5, max_size=5))
def test_text_and_json_agree_on_every_token(tokens):
    text = parse_belief_response(_text([token for token, _ in tokens]))
    structured = parse_belief_response(_structured([value for _, value in tokens]))
    assert text.quantiles == structured.quantiles
    assert text.point_estimate == structured.point_estimate
    assert text.quantiles_repaired == structured.quantiles_repaired


@given(
    numeric_tokens(),
    st.sampled_from(
        [
            "{key}={value}",
            "{key}: {value}",
            '"{key}": {value},',
            "- {key} = {value}",
            "**{key}**: {value}",
            "{key} ≈ {value}",
            "{key} is {value}",
            "| {key} | {value} |",
            "{key}: {value}.",
        ]
    ),
)
def test_text_separator_forms_never_swallow_the_sign(token_and_value, template):
    token, value = token_and_value
    parsed = parse_belief_response(_text([token] * 5, template=template))
    assert parsed.quantiles == dict.fromkeys(QUANTILE_ORDER, value)


@given(st.lists(numeric_tokens(), min_size=5, max_size=5))
def test_string_json_quantiles_preserve_every_literal_token(tokens):
    parsed = parse_belief_response(_structured([token for token, _ in tokens]))
    expected = list(itertools.accumulate([value for _, value in tokens], max))
    assert list(parsed.quantiles.values()) == expected


@given(finite_floats)
def test_json_numbers_round_trip_exactly(value):
    parsed = parse_belief_response(_structured([value] * 5))
    assert parsed.point_estimate == value
    assert parsed.quantiles == dict.fromkeys(QUANTILE_ORDER, value)


# --- 2. Point = p50 ------------------------------------------------------------


@given(
    st.lists(st.integers(-1000, 1000), min_size=5, max_size=5),
    st.sampled_from(
        [
            "Past work reported around {n}.",
            "Prior study: beta = {n}.",
            "Earlier estimate approximately -{n}.",
            "Central estimates typically fall between -{n} and {n}.",
            "Point estimate: {n}",
        ]
    ),
    st.integers(1, 99),
    st.booleans(),
)
def test_point_estimate_is_p50_whatever_the_narrative(values, narrative, n, before):
    body = _text(values)
    sentence = narrative.format(n=n)
    text = f"{sentence}\n{body}" if before else f"{body}\n{sentence}"
    parsed = parse_belief_response(text)
    assert parsed.point_estimate == parsed.quantiles["p50"]
    assert parsed.lower_bound == parsed.quantiles["p05"]
    assert parsed.upper_bound == parsed.quantiles["p95"]
    assert parsed.lower_bound <= parsed.point_estimate <= parsed.upper_bound


@given(st.lists(st.integers(-10_000, 10_000), min_size=5, max_size=5), finite_floats)
def test_structured_point_is_p50_even_when_stated_point_differs(values, stated):
    parsed = parse_belief_response(_structured(values, point_estimate=stated))
    assert parsed.point_estimate == parsed.quantiles["p50"]
    assert list(parsed.quantiles.values()) == sorted(parsed.quantiles.values())


# --- 3/4. Finite values; refusals stay refusals --------------------------------


@given(st.sampled_from([float("nan"), float("inf"), float("-inf")]), st.integers(0, 4))
def test_nonfinite_quantile_fails_the_run(bad, position):
    values = [0.1, 0.2, 0.3, 0.4, 0.5]
    values[position] = bad
    with pytest.raises(ValueError, match="missing"):
        parse_belief_response(_structured(values))


@pytest.mark.parametrize("literal", ["NaN", "Infinity", "-Infinity", "1e999", "-1e999"])
def test_nonfinite_json_literals_fail_the_run(literal):
    raw = '{"quantiles": {"p05": %s, "p25": 1, "p50": 2, "p75": 3, "p95": 4}}' % literal
    with pytest.raises(ValueError, match="missing quantiles: p05"):
        parse_belief_response(raw)


@given(
    st.sampled_from(
        [
            "N/A ({n})",
            "N/A [{n}]",
            "{n}%",
            "~{n}",
            "about {n}",
            "{n} (approx.)",
            "-{n} to {n}",
            "unknown ({n})",
            "{n}-{n}",
        ]
    ),
    st.integers(0, 2026),
)
def test_annotated_or_refused_string_values_are_missing_not_rewritten(template, n):
    annotated = template.format(n=n)
    assert _coerce_float(annotated) is None
    with pytest.raises(ValueError, match="missing"):
        parse_belief_response(_structured([annotated] * 5))


@given(st.integers(1, 100))
def test_repeated_percent_strings_fail_instead_of_losing_scale(percent):
    with pytest.raises(ValueError):
        parse_belief_response(
            _structured([f"{percent}%"] * 5), quantity_id="production.capital_share"
        )


@given(st.integers(0, 2026))
def test_text_percent_values_fail_instead_of_losing_scale(n):
    with pytest.raises(ValueError, match="missing quantiles"):
        parse_belief_response(_text([f"{n}%"] * 5))


@pytest.mark.parametrize(
    "refusal",
    [
        "I cannot answer.",
        "I refuse to provide a number.",
        "N/A",
        "Unknown (2026).",
        "\n".join(f"{key}=N/A" for key in QUANTILE_ORDER[:-1]) + "\np95=N/A (2026)",
        "\n".join(f"{key}=unknown" for key in QUANTILE_ORDER[:-1]) + "\np95=unknown (17)",
    ],
)
def test_plain_and_annotated_refusals_fail(refusal):
    with pytest.raises(ValueError):
        parse_belief_response(refusal)


@pytest.mark.parametrize("present", [p for p in itertools.product([False, True], repeat=5) if not all(p)])
def test_every_incomplete_quantile_set_fails_on_both_paths(present):
    keys = [key for key, include in zip(QUANTILE_ORDER, present) if include]
    with pytest.raises(ValueError):
        parse_belief_response(json.dumps({"point_estimate": 0, "quantiles": dict.fromkeys(keys, 1)}))
    with pytest.raises(ValueError):
        parse_belief_response("\n".join(f"{key}=1" for key in keys))


# --- 5. Label integrity ----------------------------------------------------------


def test_missing_p05_is_not_invented_from_the_p50_label():
    with pytest.raises(ValueError, match="missing quantiles: p05"):
        parse_belief_response("p25=1\np50=2\np75=3\np95=4")


def test_percentile_labels_do_not_match_inside_longer_labels():
    parsed = parse_belief_response(
        "25th percentile: 0.2\n95th percentile: 0.9\n5th percentile: 0.1\n"
        "75th percentile: 0.7\n50th percentile: 0.5"
    )
    assert parsed.quantiles == {"p05": 0.1, "p25": 0.2, "p50": 0.5, "p75": 0.7, "p95": 0.9}


def test_value_on_a_later_line_is_not_attributed_to_an_empty_label():
    with pytest.raises(ValueError, match="missing quantiles: p05"):
        parse_belief_response("p05:\n0.3\np25=1\np50=2\np75=3\np95=4")


def test_canonical_label_wins_over_earlier_median_prose():
    parsed = parse_belief_response(
        "The median is 9 in older work.\np05=1\np25=2\np50=3\np75=4\np95=5"
    )
    assert parsed.quantiles["p50"] == 3.0


# --- 6. Truncated-JSON completion -------------------------------------------------


@given(st.lists(st.integers(-1000, 1000), min_size=5, max_size=5), st.booleans())
def test_truncated_object_completion_never_changes_values(values, cut_inside_list):
    payload = {
        "interpretation": "x",
        "quantiles": dict(zip(QUANTILE_ORDER, (v / 100 for v in values))),
        "reasoning_summary": "between -0.10 and 0.00",
        "citations": ["a", "b"],
    }
    complete = json.dumps(payload, indent=2)
    # Drop the final "}" (one missing closer) or the final "]" and "}" (two).
    truncated = complete.rstrip()[:-1].rstrip()
    if cut_inside_list:
        truncated = truncated[:-1].rstrip()
    parsed = parse_belief_response(truncated)
    reference = parse_belief_response(complete)
    assert parsed.quantiles == reference.quantiles
    assert parsed.point_estimate == reference.point_estimate
    assert parsed.interpretation == "x"
    assert parsed.citations == ["a", "b"]


def test_number_cut_off_at_the_end_of_an_unclosed_object_is_rejected():
    # "1.2" may be the start of "1.25"; neither completion nor the text
    # fallback may accept it.
    cut = '{"quantiles": {"p05": -1, "p25": -0.5, "p50": 0, "p75": 0.5, "p95": 1.2'
    with pytest.raises(ValueError, match="missing quantiles: p95"):
        parse_belief_response(cut)


def test_answer_cut_inside_a_later_string_keeps_its_complete_quantiles():
    cut = (
        '{"quantiles": {"p05": -1, "p25": -0.5, "p50": 0, "p75": 0.5, "p95": 1}, '
        '"reasoning_summary": "trunc'
    )
    parsed = parse_belief_response(cut)
    assert parsed.interpretation is None  # text path
    assert list(parsed.quantiles.values()) == [-1.0, -0.5, 0.0, 0.5, 1.0]


@pytest.mark.parametrize(
    "text",
    [
        "\n".join(
            f"| {key} | {label} | {value} |"
            for key, label, value in zip(
                QUANTILE_ORDER,
                ("5th percentile", "25th percentile", "50th percentile", "75th percentile", "95th percentile"),
                ("-0.40", "-0.20", "-0.10", "0.00", "0.10"),
            )
        ),
        "p05: -0.4.\np25: -0.2.\np50: -0.1.\np75: 0.0.\np95: 0.1.",
        "p05 (5th percentile): -0.4\np25: -0.2\np50: -0.1\np75: 0\np95: 0.1",
    ],
    ids=["label-column-table", "sentence-periods", "parenthetical-label"],
)
def test_ordinal_labels_and_full_stops_do_not_change_values(text):
    parsed = parse_belief_response(text)
    assert list(parsed.quantiles.values()) == [-0.4, -0.2, -0.1, 0.0, 0.1]


def test_thousands_grouped_text_value_is_rejected_not_truncated():
    with pytest.raises(ValueError, match="missing quantiles: p95"):
        parse_belief_response("p05: 1\np25: 2\np50: 3\np75: 4\np95: 12,500")


# --- Scalar coercion unit contract --------------------------------------------


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        ("0.5", 0.5),
        (" -0.5 ", -0.5),
        ("\u22120.5", -0.5),
        (".5", 0.5),
        ("1e-1", 0.1),
        ("-2.5E3", -2500.0),
        ("1,000.5", 1000.5),
        (3, 3.0),
        (-0.0, -0.0),
        (True, None),
        (None, None),
        ([1], None),
        ("1,5", None),
        ("", None),
        (10**400, None),
    ],
)
def test_coerce_float_contract(value, expected):
    result = _coerce_float(value)
    if expected is None:
        assert result is None
    else:
        assert result == expected and math.copysign(1, result) == math.copysign(1, expected)


# --- Regression: verbatim Gemini 3.5 Flash answers -------------------------------

GEMINI_INCOME_RUN_5 = (
    '{\n  "interpretation": "Intensive-margin annual-hours elasticity with respect to non-labor '
    'income conditional on employment for prime-age US workers.",\n  "point_estimate": -0.04,\n'
    '  "quantiles": {\n    "p05": -0.15,\n    "p25": -0.08,\n    "p50": -0.04,\n    "p75": -0.01,\n'
    '    "p95": 0.01\n  },\n  "citations": [\n    "Imbens, Rubin, and Sacerdote (2001)",\n'
    '    "Cesarini, Lindqvist, Östling, and Wallace (2017)",\n    "Blundell and MaCurdy (1999)"\n  ],\n'
    '  "reasoning_summary": "Microeconomic empirical research, particularly studies exploiting '
    "lottery wealth shocks (e.g., Imbens et al., 2001; Cesarini et al., 2017), consistently finds "
    "small, negative income effects on the intensive margin of labor supply. This indicates that "
    "while leisure is a normal good, the intensive-margin hours response to non-labor income is "
    "highly inelastic, with central estimates typically falling between -0.10 and 0.00.\""
)

GEMINI_CAPITAL_GAINS_RUN_2 = (
    '{\n  "interpretation": "The medium-run elasticity of long-term capital gains realizations '
    'with respect to the capital gains marginal tax rate for U.S. taxpayers.",\n'
    '  "point_estimate": -0.65,\n  "quantiles": {\n    "p05": -1.3,\n    "p25": -0.9,\n'
    '    "p50": -0.65,\n    "p75": -0.4,\n    "p95": -0.15\n  },\n  "citations": [\n'
    '    "Dowd, McClelland, and Lu (2015). An Analysis of the Elasticity of Capital Gains '
    'Realizations with Respect to Marginal Tax Rates. National Tax Journal.",\n'
    '    "Congressional Budget Office (2012). How CBO Analyzes the Effects of the Tax on Capital '
    'Gains Realizations.",\n    "Slemrod (1998). Methodological Issues in Measuring the Response '
    'of Realizations to Tax Rates."\n  ],\n  "reasoning_summary": "Empirical estimates from the '
    "CBO, JCT, and academic literature indicate a negative medium-run realization elasticity with "
    "respect to the marginal tax rate. While short-run timing elasticities are very high, "
    "medium-run behavioral responses are more moderate, typically estimated to lie between -0.5 "
    "and -0.8, with substantial uncertainty regarding the extent of permanent tax and permanence "
    'of avoidance can mitigate the long-run impact."'
)


@pytest.mark.parametrize(
    ("raw", "quantiles", "citations"),
    [
        (GEMINI_INCOME_RUN_5, [-0.15, -0.08, -0.04, -0.01, 0.01], 3),
        (GEMINI_CAPITAL_GAINS_RUN_2, [-1.3, -0.9, -0.65, -0.4, -0.15], 3),
    ],
)
def test_gemini_answers_missing_their_final_brace_keep_their_signs(raw, quantiles, citations):
    # Before the fix these parsed as point 0.1 / quantiles all 0.15 and
    # point 1.3 / quantiles all 1.3 (signs dropped, then "repaired").
    parsed = parse_belief_response(raw)
    assert list(parsed.quantiles.values()) == quantiles
    assert parsed.point_estimate == quantiles[2]
    assert parsed.quantiles_repaired is False
    assert parsed.interpretation is not None
    assert len(parsed.citations) == citations


@pytest.mark.parametrize("raw", [GEMINI_INCOME_RUN_5, GEMINI_CAPITAL_GAINS_RUN_2])
def test_gemini_answers_text_fallback_alone_also_keeps_signs(raw):
    # Even with completion unavailable (a string cut short), the text path
    # must read the same literal quantiles.
    cut = raw[: raw.index('"reasoning_summary"') + 40]
    parsed = parse_belief_response(cut)
    assert parsed.interpretation is None  # text path
    assert parsed.quantiles == parse_belief_response(raw).quantiles
    assert parsed.point_estimate == parsed.quantiles["p50"]


# --- Regression: salvage paths on committed raw answers ---------------------------

RESULTS = Path(__file__).resolve().parents[1] / "results"


def _cached_raw(experiment: str, line: int) -> str:
    rows = (RESULTS / experiment / "runs.jsonl").read_text().splitlines()
    return json.loads(rows[line - 1])["raw_response"]


@pytest.mark.parametrize(
    ("experiment", "line", "quantiles"),
    [
        # Escaped JSON inside a string literal, e.g. "<<answer>>\n{\"p05\": ...}".
        ("inkling-elasticities-batch15", 142, [0.7, 1.1, 1.5, 2.2, 3.8]),
        ("inkling-elasticities-batch15", 236, [0.08, 0.16, 0.22, 0.3, 0.45]),
        # A {"They want ...": {<answer>}} wrapper whose outer brace never closes.
        ("inkling-elasticities-batch15", 356, [-1.2, -0.75, -0.5, -0.35, -0.1]),
        # Answer cut inside the reasoning string; signs were dropped before.
        ("kimi-k2.6-elasticities-batch15", 344, [-0.7, -0.4, -0.25, -0.1, 0.05]),
    ],
)
def test_salvaged_answers_keep_their_literal_values(experiment, line, quantiles):
    parsed = parse_belief_response(_cached_raw(experiment, line))
    assert list(parsed.quantiles.values()) == quantiles
    assert parsed.point_estimate == quantiles[2]


def test_space_split_numeric_tokens_are_rejected_not_misread():
    # Gemini 3.5 Flash IES run 2 wrote "p05": 0 .1 ... "p95": 2 .0 (tokens
    # split by spaces). Reading "0 .1" as 0 would invent a quantile.
    raw = _cached_raw("gemini-3.5-flash-elasticities-batch15", 17)
    assert '"p05": 0 .1' in raw
    with pytest.raises(ValueError, match="missing quantiles"):
        parse_belief_response(raw)
