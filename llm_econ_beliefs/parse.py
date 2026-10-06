"""Parse structured or semi-structured LLM belief responses.

Parsing contract (enforced by ``tests/test_parse.py`` and
``tests/test_parse_properties.py``):

- A successful parse carries all five elicited quantiles, and its point
  estimate is the elicited median (``p50``) on both the JSON and the text path.
- Every accepted number is finite and is read exactly as written, including
  its sign and exponent. A value with an annotation (``"1%"``, ``"N/A (0)"``,
  ``"~0.3"``) is not a number: it is treated as missing, so a refusal or a
  unit-ambiguous answer fails the run instead of becoming a belief.
- JSON cut off after a complete value but before its closing brackets is read
  structurally once the missing brackets are appended; nothing else is
  repaired.

The one intended transformation is the running-max repair that makes
disordered quantiles monotone, flagged on the result as ``quantiles_repaired``.
"""

from __future__ import annotations

import ast
import json
import math
import re
from typing import Any, Sequence

from .models import BeliefEstimate


POINT_KEYS = (
    "point_estimate",
    "best_estimate",
    "central_estimate",
    "estimate",
    "median",
    "p50",
)
LOWER_KEYS = ("lower_bound", "lower_90", "p05", "p10", "lower")
UPPER_KEYS = ("upper_bound", "upper_90", "p95", "p90", "upper")
CONFIDENCE_KEYS = ("confidence_level", "interval_probability", "coverage")
INTERPRETATION_KEYS = ("interpretation", "definition", "quantity_interpretation")
REASONING_KEYS = ("reasoning_summary", "reasoning", "summary", "notes")
CITATION_KEYS = ("citations", "references", "literature_anchors")
QUANTILE_ORDER = ("p05", "p25", "p50", "p75", "p95")
QUANTILE_ALIASES = {
    "p05": ("p05", "p5", "q05", "q5", "5th percentile", "5th quantile"),
    "p25": ("p25", "q25", "25th percentile", "first quartile", "q1"),
    "p50": ("p50", "q50", "50th percentile", "median"),
    "p75": ("p75", "q75", "75th percentile", "third quartile", "q3"),
    "p95": ("p95", "q95", "95th percentile", "95th quantile"),
}

# A decimal literal with an optional sign and exponent. Leading-dot (".1") and
# trailing-dot ("1.") forms are both accepted, as Python's float() does.
NUMBER_PATTERN = r"[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?"
_STRICT_NUMBER = re.compile(rf"{NUMBER_PATTERN}")
_THOUSANDS_NUMBER = re.compile(r"[-+]?\d{1,3}(?:,\d{3})+(?:\.\d*)?")
# U+2212 MINUS SIGN is the typographic minus some models emit in prose.
_UNICODE_MINUS = "−"
# Text-path labels must stand alone ("p5" must not match inside "p50", nor
# "5th percentile" inside "95th percentile"), and the separator between a
# label and its value may not contain a digit, sign, decimal point, letter, or
# newline, so it can never swallow part of the number or reach another line.
_LABEL_LEFT = r"(?<![A-Za-z0-9_])"
_LABEL_RIGHT = r"(?![A-Za-z0-9_])"
_TEXT_SEPARATOR = r"[ \t\"'*`|:=≈~]{0,12}"
# A value must end the token: "0.5%" (unit-ambiguous) and "5th" (a label) are
# not values. A following period is allowed only as punctuation ("0.3."), not
# as the start of more digits.
_VALUE_END = r"(?![A-Za-z0-9_%]|\.\d)"


def parse_belief_response(
    response_text: str,
    *,
    quantity_id: str | None = None,
) -> BeliefEstimate:
    """Parse either JSON-first output or a free-form fallback."""
    if not response_text or not response_text.strip():
        raise ValueError("Response text is empty")

    payload = _extract_payload(response_text)
    if payload is not None:
        return _parse_structured_payload(
            payload,
            raw_response=response_text,
            quantity_id=quantity_id,
        )

    quantiles, quantiles_repaired = _extract_quantiles_from_text(response_text)
    # Same quantile-complete contract as the structured path: the pooled
    # analysis is a mixture over the five quantiles, so a response without
    # all five is a failed run, not a parsed one. The point estimate is the
    # elicited median, as on the structured path; narrative numbers elsewhere
    # in the text never override it.
    missing_quantiles = [key for key in QUANTILE_ORDER if quantiles.get(key) is None]
    if missing_quantiles:
        raise ValueError(
            "Response text is missing quantiles: " + ", ".join(missing_quantiles)
        )

    return BeliefEstimate(
        quantity_id=quantity_id,
        point_estimate=quantiles["p50"],
        lower_bound=quantiles["p05"],
        upper_bound=quantiles["p95"],
        confidence_level=0.9,
        quantiles=quantiles,
        reasoning_summary=response_text.strip(),
        raw_response=response_text,
        quantiles_repaired=quantiles_repaired,
    )


def _extract_payload(response_text: str) -> dict[str, Any] | None:
    stripped = response_text.strip()
    if stripped.startswith("```"):
        match = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", stripped, re.S)
        if match:
            stripped = match.group(1)

    fallback: dict[str, Any] | None = None
    for candidate in _payload_candidates(stripped):
        parsed = _load_object(candidate)
        if parsed is not None:
            parsed = _unwrap_payload(parsed)
            if _has_belief_keys(parsed):
                return parsed
            fallback = fallback if fallback is not None else parsed

    # Some responses deliver the JSON answer as an escaped string literal
    # (``"{\n  \"point_estimate\": ...}"``), sometimes inside a malformed
    # outer object. Decode each string literal and read the object inside it.
    if '\\"' in stripped:
        for decoded in _decoded_string_literals(stripped):
            for candidate in _payload_candidates(decoded):
                parsed = _load_object(candidate)
                if parsed is not None:
                    parsed = _unwrap_payload(parsed)
                    if _has_belief_keys(parsed):
                        return parsed

    # An object without belief fields still routes to the structured path,
    # which rejects it; it is never mined as free text.
    return fallback


def _payload_candidates(text: str) -> tuple[str | None, ...]:
    return (text, _first_braced_block(text), _close_truncated_json(text))


def _load_object(candidate: str | None) -> dict[str, Any] | None:
    if not candidate:
        return None
    try:
        parsed = json.loads(candidate)
    except json.JSONDecodeError:
        try:
            parsed = ast.literal_eval(candidate)
        except (ValueError, SyntaxError, TypeError, MemoryError, RecursionError):
            return None
    return parsed if isinstance(parsed, dict) else None


def _has_belief_keys(payload: dict[str, Any]) -> bool:
    return any(key in payload for key in ("quantiles", *POINT_KEYS, *QUANTILE_ORDER))


def _unwrap_payload(payload: dict[str, Any]) -> dict[str, Any]:
    """Descend into a single wrapper key (``{"answer": {...}}``) when the top
    level carries no belief fields but exactly one nested object does."""
    if _has_belief_keys(payload):
        return payload
    nested = [
        value
        for value in payload.values()
        if isinstance(value, dict) and _has_belief_keys(value)
    ]
    return nested[0] if len(nested) == 1 else payload


def _decoded_string_literals(text: str):
    decoder = json.JSONDecoder()
    for match in re.finditer(r'(?<!\\)"', text):
        try:
            value, _ = decoder.raw_decode(text, match.start())
        except json.JSONDecodeError:
            continue
        if isinstance(value, str) and "{" in value:
            yield value


def _parse_structured_payload(
    payload: dict[str, Any],
    *,
    raw_response: str,
    quantity_id: str | None,
) -> BeliefEstimate:
    quantiles, quantiles_repaired = _lookup_quantiles(payload)
    point_estimate = _lookup_numeric(payload, POINT_KEYS)
    if "p50" in quantiles:
        point_estimate = quantiles["p50"]
    if point_estimate is None:
        raise ValueError("Structured response is missing a point estimate")
    # The pooled analysis is a mixture over the five elicited quantiles, so
    # a run without all five contributes nothing valid — the same failure
    # class as a missing point estimate. Inkling is the only panel model
    # that ever omitted them (9 runs); every such slot re-ran as a fresh
    # draw under the standard replacement policy.
    missing_quantiles = [key for key in QUANTILE_ORDER if quantiles.get(key) is None]
    if missing_quantiles:
        raise ValueError(
            "Structured response is missing quantiles: " + ", ".join(missing_quantiles)
        )

    lower_bound = _lookup_numeric(payload, LOWER_KEYS)
    upper_bound = _lookup_numeric(payload, UPPER_KEYS)
    if lower_bound is None:
        lower_bound = quantiles.get("p05")
    if upper_bound is None:
        upper_bound = quantiles.get("p95")
    if lower_bound is not None and upper_bound is not None and lower_bound > upper_bound:
        lower_bound, upper_bound = upper_bound, lower_bound

    confidence_level = _lookup_confidence(payload)
    if confidence_level is None and lower_bound is not None and upper_bound is not None:
        confidence_level = 0.9

    return BeliefEstimate(
        quantity_id=quantity_id,
        point_estimate=point_estimate,
        interpretation=_lookup_string(payload, INTERPRETATION_KEYS),
        lower_bound=lower_bound,
        upper_bound=upper_bound,
        confidence_level=confidence_level,
        quantiles=quantiles,
        citations=_lookup_string_list(payload, CITATION_KEYS),
        reasoning_summary=_lookup_string(payload, REASONING_KEYS),
        raw_response=raw_response,
        quantiles_repaired=quantiles_repaired,
    )


def _lookup_quantiles(payload: dict[str, Any]) -> tuple[dict[str, float], bool]:
    quantiles: dict[str, float] = {}
    candidate = payload.get("quantiles")
    if isinstance(candidate, dict):
        for key in QUANTILE_ORDER:
            if key in candidate:
                value = _coerce_float(candidate[key])
                if value is not None:
                    quantiles[key] = value

    for key in QUANTILE_ORDER:
        value = _lookup_numeric(payload, (key,))
        if value is not None:
            quantiles[key] = value

    return _sorted_quantiles(quantiles)


def _lookup_numeric(payload: dict[str, Any], keys: Sequence[str]) -> float | None:
    for key in keys:
        if key in payload:
            value = _coerce_float(payload[key])
            if value is not None:
                return value
    return None


def _lookup_string(payload: dict[str, Any], keys: Sequence[str]) -> str | None:
    for key in keys:
        if key in payload and payload[key] is not None:
            return str(payload[key]).strip()
    return None


def _lookup_string_list(payload: dict[str, Any], keys: Sequence[str]) -> list[str]:
    for key in keys:
        if key not in payload or payload[key] is None:
            continue
        value = payload[key]
        if isinstance(value, list):
            return [str(item).strip() for item in value if str(item).strip()]
        if isinstance(value, str):
            parts = re.split(r"\n|;|, (?=[A-Z])", value)
            return [part.strip(" -") for part in parts if part.strip()]
    return []


def _lookup_confidence(payload: dict[str, Any]) -> float | None:
    for key in CONFIDENCE_KEYS:
        if key not in payload:
            continue
        value = payload[key]
        if isinstance(value, str) and value.strip().endswith("%"):
            value = value.strip()[:-1]
        numeric = _coerce_float(value)
        if numeric is None:
            continue
        if numeric > 1:
            numeric /= 100
        if 0 < numeric < 1:
            return numeric
    return None


def _coerce_float(value: Any) -> float | None:
    """Return a finite float for a bare numeric value, else None.

    Strings must be a complete numeric literal (optionally with standard
    thousands separators); any other content — a unit, an annotation, a
    refusal — makes the value missing rather than silently changing its
    meaning.
    """
    if value is None or isinstance(value, bool):
        return None
    if isinstance(value, (int, float)):
        try:
            numeric = float(value)
        except OverflowError:
            return None
        return numeric if math.isfinite(numeric) else None
    if not isinstance(value, str):
        return None

    text = value.strip().replace(_UNICODE_MINUS, "-")
    if _THOUSANDS_NUMBER.fullmatch(text):
        text = text.replace(",", "")
    if not _STRICT_NUMBER.fullmatch(text):
        return None
    numeric = float(text)
    return numeric if math.isfinite(numeric) else None


def _extract_quantiles_from_text(response_text: str) -> tuple[dict[str, float], bool]:
    text = response_text.replace(_UNICODE_MINUS, "-")
    quantiles: dict[str, float] = {}
    for key, aliases in QUANTILE_ALIASES.items():
        patterns = [
            # A JSON-style quoted key is the most specific anchor, so it wins
            # over a bare label that may appear earlier in prose.
            rf'"{re.escape(key)}"\s*:\s*"?\s*({NUMBER_PATTERN}){_VALUE_END}',
            rf"(?i){_LABEL_LEFT}(?:{'|'.join(re.escape(alias) for alias in aliases)})"
            rf"{_LABEL_RIGHT}{_TEXT_SEPARATOR}({NUMBER_PATTERN}){_VALUE_END}",
        ]
        for pattern in patterns:
            match = re.search(pattern, text)
            if match:
                value = _coerce_float(match.group(1))
                if value is not None:
                    quantiles[key] = value
                    break
    return _sorted_quantiles(quantiles)


def _scan_json_brackets(text: str, start: int) -> tuple[int | None, list[str], bool, str | None]:
    """Scan JSON-like text from ``start``, respecting string literals.

    Returns ``(end, open_stack, in_string, last_token_char)`` where ``end`` is
    the index just past the bracket that closes the opening one (None when the
    text ends first), ``open_stack`` lists the closers still owed, and
    ``last_token_char`` is the last non-whitespace character outside a string
    (a closing quote counts).
    """
    stack: list[str] = []
    in_string = False
    escaped = False
    last_token_char: str | None = None
    for index in range(start, len(text)):
        char = text[index]
        if in_string:
            if escaped:
                escaped = False
            elif char == "\\":
                escaped = True
            elif char == '"':
                in_string = False
                last_token_char = '"'
            continue
        if char == '"':
            in_string = True
        elif char in "{[":
            stack.append("}" if char == "{" else "]")
        elif char in "}]":
            if not stack or stack[-1] != char:
                # Mismatched brackets: not JSON, and nothing to complete.
                return None, [], False, char
            stack.pop()
            if not stack:
                return index + 1, stack, False, char
        if not char.isspace():
            last_token_char = char
    return None, stack, in_string, last_token_char


def _first_braced_block(text: str) -> str | None:
    start = text.find("{")
    if start == -1:
        return None
    end, _, _, _ = _scan_json_brackets(text, start)
    if end is None:
        return None
    return text[start:end]


def _close_truncated_json(text: str) -> str | None:
    """Append the closing brackets owed by JSON cut off after a complete value.

    Only text that stops outside a string, right after a closed string, a
    closed object/array, or a ``true``/``false``/``null`` literal is completed.
    Text that stops inside a string, after a separator, or after a bare number
    (which may itself be truncated) is left alone and fails structured parsing.
    """
    start = text.find("{")
    if start == -1:
        return None
    end, stack, in_string, last_token_char = _scan_json_brackets(text, start)
    if end is not None or not stack or in_string:
        return None
    body = text[start:].rstrip()
    if last_token_char not in ('"', "}", "]") and not body.endswith(("true", "false", "null")):
        return None
    return body + "".join(reversed(stack))


def _sorted_quantiles(quantiles: dict[str, float]) -> tuple[dict[str, float], bool]:
    if not quantiles:
        return {}, False

    sorted_values = []
    running_max = None
    repaired = False
    for key in QUANTILE_ORDER:
        if key not in quantiles:
            continue
        value = quantiles[key]
        if running_max is None:
            running_max = value
        else:
            if value < running_max:
                repaired = True
            running_max = max(running_max, value)
        sorted_values.append((key, running_max))

    return dict(sorted_values), repaired
