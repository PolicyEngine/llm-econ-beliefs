"""Parse structured or semi-structured LLM belief responses.

Numeric contract: every accepted number is a literal numeric token the model
wrote, with its sign, decimal point, and exponent intact. A value that is not
a bare finite number (a refusal such as ``"N/A (0)"``, a unit-annotated
``"1%"``, NaN, or infinity) is treated as missing, never coerced into a
different number, so a refusal stays a failed run under the quantile-complete
contract below.
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

# One numeric token: optional sign (ASCII or U+2212 minus), digits with an
# optional fraction or a bare leading-decimal fraction, optional exponent.
_NUMBER = r"[-+\u2212]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?"
_NUMBER_RE = re.compile(_NUMBER)
_JSON_DECODER = json.JSONDecoder()
_THOUSANDS_RE = re.compile(r"[-+\u2212]?\d{1,3}(?:,\d{3})+(?:\.\d*)?")
# What may sit between a quantile label and its value on the same line:
# quoting/markup filler, one short parenthetical such as "(5th percentile)",
# and one assignment marker. Digits, signs, decimal points, and newlines are
# excluded, so the separator can never swallow a minus sign or reach a number
# on another line or inside another label.
_FILLER = r"[ \t\"'`*_|\\]*"
_SEPARATOR = (
    rf"{_FILLER}(?:\([^()\n]{{0,40}}\))?{_FILLER}"
    rf"(?::=|->|=>|[:=≈~]|\bis\b)?{_FILLER}"
)
# A value must end the numeric token. Rejected continuations: a letter or
# digit ("5th" is a label, not 5), a decimal fraction (".5"), a digit or
# decimal point after a space ("0 .1" is a token split in two, not 0), a
# thousands group ("12,500" is not 12), and a percent sign (which changes the
# number's meaning). A sentence-ending full stop is fine.
_VALUE_END = r"(?![\w%]|\.\d|[ \t]+[\d.]|,\d{3}(?!\d)|\s*%)"


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
    # all five is a failed run, not a parsed one.
    missing_quantiles = [key for key in QUANTILE_ORDER if quantiles.get(key) is None]
    if missing_quantiles:
        raise ValueError(
            "Response text is missing quantiles: " + ", ".join(missing_quantiles)
        )

    # The prompt asks for point_estimate == p50, and the structured path
    # enforces it; the text path does too, so an unrelated narrative number
    # ("around 1", "central estimates between -0.10 and 0") can never stand
    # in for the elicited median.
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
    """Return the answer object, preferring one that carries a quantiles dict.

    The whole text, a fenced block, and the first balanced block are tried
    first, as before. When none of them is an answer (an object with a
    ``quantiles`` dict), salvage paths look for one: a truncated object closed
    up, any complete object embedded in surrounding text, and escaped JSON
    inside a string literal. Salvaged objects are only accepted when they are
    answer-shaped, and every number still has to pass the strict structured
    contract, so salvage can recover a literal answer but never invent one.
    """
    stripped = response_text.strip()
    if stripped.startswith("```"):
        match = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", stripped, re.S)
        if match:
            stripped = match.group(1)

    legacy = [_decode_object(stripped), _decode_object(_first_braced_block(stripped))]
    for candidate in legacy:
        answer = _answer_object(candidate)
        if answer is not None:
            return answer
    for candidate in _salvaged_objects(stripped):
        answer = _answer_object(candidate)
        if answer is not None:
            return answer
    return next((candidate for candidate in legacy if candidate is not None), None)


def _decode_object(text: str | None) -> dict[str, Any] | None:
    if not text:
        return None
    try:
        parsed = json.loads(text)
    except json.JSONDecodeError:
        try:
            parsed = ast.literal_eval(text)
        except (ValueError, SyntaxError, TypeError, MemoryError, RecursionError):
            return None
    return parsed if isinstance(parsed, dict) else None


def _answer_object(payload: Any, depth: int = 0) -> dict[str, Any] | None:
    """Return ``payload`` if it holds a quantiles dict, unwrapping one level.

    A wrapper such as ``{"They want ...": {<answer>}}`` holds the answer as
    its only object value.
    """
    if not isinstance(payload, dict):
        return None
    if isinstance(payload.get("quantiles"), dict):
        return payload
    nested = [value for value in payload.values() if isinstance(value, dict)]
    if depth < 2 and len(nested) == 1:
        return _answer_object(nested[0], depth + 1)
    return None


def _salvaged_objects(text: str, depth: int = 0):
    completed = _complete_truncated_object(text)
    if completed is not None:
        try:
            yield json.loads(completed)
        except json.JSONDecodeError:
            pass
    for match in re.finditer(r"\{", text):
        try:
            candidate, _ = _JSON_DECODER.raw_decode(text, match.start())
        except json.JSONDecodeError:
            continue
        yield candidate
    if depth == 0:
        # Escaped JSON inside a string literal: decode the literal, then look
        # for the answer in the decoded text.
        for literal in re.finditer(r'"(?:[^"\\]|\\.)*"', text, re.S):
            if "quantiles" not in literal.group(0):
                continue
            try:
                decoded = json.loads(literal.group(0))
            except json.JSONDecodeError:
                continue
            if isinstance(decoded, str) and "{" in decoded:
                yield _decode_object(_first_braced_block(decoded))
                yield from _salvaged_objects(decoded, depth + 1)


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
    missing_quantiles = [
        key for key in ("p05", "p25", "p50", "p75", "p95") if quantiles.get(key) is None
    ]
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
        if isinstance(value, str) and value.endswith("%"):
            value = value[:-1]
        try:
            numeric = float(value)
        except (TypeError, ValueError):
            continue
        if numeric > 1:
            numeric /= 100
        if 0 < numeric < 1:
            return numeric
    return None


def _coerce_float(value: Any) -> float | None:
    """Return a finite number only when the value *is* one bare number.

    JSON numbers pass through. A string must be exactly one numeric token
    (surrounding whitespace and thousands separators allowed); anything else
    — ``"N/A (0)"``, ``"1%"``, ``"~0.3"``, ``"0.1-0.3"`` — is missing, not
    rewritten. NaN and infinities are missing too.
    """
    if value is None or isinstance(value, bool):
        return None
    if isinstance(value, (int, float)):
        try:
            number = float(value)
        except OverflowError:
            return None
    elif isinstance(value, str):
        text = value.strip()
        if _THOUSANDS_RE.fullmatch(text):
            text = text.replace(",", "")
        if not _NUMBER_RE.fullmatch(text):
            return None
        number = _to_float(text)
    else:
        return None
    return number if math.isfinite(number) else None


def _to_float(token: str) -> float:
    return float(token.replace("\u2212", "-"))


def _extract_quantiles_from_text(response_text: str) -> tuple[dict[str, float], bool]:
    quantiles: dict[str, float] = {}
    # In an object cut off mid-answer, a number running into the end of the
    # text may itself be cut ("1.2" of "1.25"); completion refuses it, and so
    # does this fallback.
    cut_object = "{" in response_text and _first_braced_block(response_text) is None
    for key, aliases in QUANTILE_ALIASES.items():
        # Aliases are tried in priority order, so the canonical label ("p50")
        # wins over a looser one ("median") that prose may use earlier.
        for alias in aliases:
            pattern = (
                rf"(?i)(?<![A-Za-z0-9_]){re.escape(alias)}(?![A-Za-z0-9_])"
                rf"{_SEPARATOR}(?P<value>{_NUMBER}){_VALUE_END}"
            )
            match = re.search(pattern, response_text)
            if match:
                value = _to_float(match.group("value"))
                runs_to_end = not response_text[match.end() :].strip()
                if math.isfinite(value) and not (cut_object and runs_to_end):
                    quantiles[key] = value
                break
    return _sorted_quantiles(quantiles)


def _first_braced_block(text: str) -> str | None:
    """Return the first balanced ``{...}`` block, ignoring braces inside strings."""
    start = text.find("{")
    if start == -1:
        return None

    depth = 0
    in_string = False
    escaped = False
    for index in range(start, len(text)):
        char = text[index]
        if in_string:
            if escaped:
                escaped = False
            elif char == "\\":
                escaped = True
            elif char == '"':
                in_string = False
        elif char == '"':
            in_string = True
        elif char == "{":
            depth += 1
        elif char == "}":
            depth -= 1
            if depth == 0:
                return text[start : index + 1]
    return None


def _complete_truncated_object(text: str) -> str | None:
    """Close a JSON object whose only defect is missing trailing closers.

    Some responses (e.g. Gemini 3.5 Flash) end one ``}`` short of a complete
    object. Closing the still-open ``{``/``[`` containers recovers the literal
    answer without inventing any value. Completion is refused whenever the
    text could have been cut mid-value — inside a string, or right after a
    bare number, literal, or separator — because appending closers there
    could silently change or truncate a number. (A dangling key still fails
    to decode after completion.)
    """
    start = text.find("{")
    if start == -1:
        return None

    stack: list[str] = []
    in_string = False
    escaped = False
    for char in text[start:]:
        if in_string:
            if escaped:
                escaped = False
            elif char == "\\":
                escaped = True
            elif char == '"':
                in_string = False
        elif char == '"':
            in_string = True
        elif char in "{[":
            stack.append("}" if char == "{" else "]")
        elif char in "}]":
            if not stack or stack.pop() != char:
                return None
            if not stack:
                return None  # a complete block exists; nothing to complete
    if in_string or not stack:
        return None

    body = text[start:].rstrip()
    if not body or body[-1] not in "\"}]":
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
