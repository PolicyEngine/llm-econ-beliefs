"""Whole-cache checks tying the parser to every retained raw answer.

1. Differential oracle: an independent, key-anchored decoder reads each
   quantile value straight from the raw text (``"p05": <JSON value>``) with
   ``json.JSONDecoder.raw_decode`` — no object extraction, no regex numbers.
   Wherever it finds all five quantiles unambiguously, the parser must either
   agree exactly (after the intended running-max repair) or have a recorded
   reason to reject the answer.
2. Cache agreement: re-parsing each successful cached row reproduces every
   stored parsed field (numbers and text), except the rows pinned in
   ``fixtures/stale_cached_rows.json``. That file is the exact list of rows
   whose stored values came from the pre-2026-09-25 parser, with the values
   the current parser reads; regenerating the cache empties it. Any other
   drift between parser and cache fails here.
"""

from __future__ import annotations

import itertools
import json
import math
from functools import lru_cache
from pathlib import Path

import pytest

from llm_econ_beliefs import parse_belief_response

ROOT = Path(__file__).resolve().parents[1]
QUANTILES = ("p05", "p25", "p50", "p75", "p95")
STALE_ROWS_PATH = Path(__file__).parent / "fixtures" / "stale_cached_rows.json"
_DECODER = json.JSONDecoder()


def _run_files() -> list[Path]:
    return sorted(
        path
        for pattern in ("runs.jsonl", "failed-runs-archive.jsonl")
        for path in (ROOT / "results").rglob(pattern)
    )


@lru_cache(maxsize=1)
def _cached_records() -> tuple[tuple[str, dict], ...]:
    records = []
    for path in _run_files():
        for line_number, line in enumerate(path.read_text(encoding="utf-8").split("\n"), 1):
            if line.strip():
                location = f"{path.relative_to(ROOT)}:{line_number}"
                records.append((location, json.loads(line)))
    return tuple(records)


def _oracle_quantiles(raw: str) -> list[float] | None:
    """Decode each ``"pXX": value`` pair directly; None if absent or ambiguous."""
    values = []
    for key in QUANTILES:
        found = set()
        marker = f'"{key}"'
        start = raw.find(marker)
        while start != -1:
            colon = start + len(marker)
            while colon < len(raw) and raw[colon] in " \t\r\n":
                colon += 1
            if colon < len(raw) and raw[colon] == ":":
                position = colon + 1
                while position < len(raw) and raw[position] in " \t\r\n":
                    position += 1
                try:
                    value, end = _DECODER.raw_decode(raw, position)
                except json.JSONDecodeError:
                    value, end = None, position
                # The value must end where JSON allows ("0 .1" is not 0).
                rest = raw[end:].lstrip(" \t\r\n")
                if rest and rest[0] not in ",}]":
                    value = None
                found.add(json.dumps(value))
            start = raw.find(marker, start + 1)
        if len(found) != 1:
            return None
        value = json.loads(found.pop())
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            return None
        if not math.isfinite(value):
            return None
        values.append(float(value))
    return list(itertools.accumulate(values, max))


@lru_cache(maxsize=1)
def _reparsed() -> dict[str, tuple[str, object]]:
    outcomes: dict[str, tuple[str, object]] = {}
    for location, record in _cached_records():
        raw = record.get("raw_response")
        if not raw:
            continue
        try:
            parsed = parse_belief_response(raw, quantity_id=record.get("quantity_id"))
        except ValueError as exc:
            outcomes[location] = ("rejected", str(exc))
        else:
            outcomes[location] = ("parsed", parsed)
    return outcomes


def test_parser_agrees_with_key_anchored_oracle_on_every_cached_answer():
    disagreements = []
    oracle_rows = 0
    for location, record in _cached_records():
        raw = record.get("raw_response")
        if not raw:
            continue
        expected = _oracle_quantiles(raw)
        if expected is None:
            continue
        oracle_rows += 1
        status, value = _reparsed()[location]
        if status == "rejected":
            disagreements.append((location, "rejected", value))
            continue
        actual = [value.quantiles[key] for key in QUANTILES]
        if actual != expected or value.point_estimate != expected[2]:
            disagreements.append((location, actual, expected))
    assert oracle_rows > 13_000
    assert disagreements == []


PARSED_FIELDS = (
    "point_estimate",
    "lower_bound",
    "upper_bound",
    "confidence_level",
    "quantiles",
    "quantiles_repaired",
    "interpretation",
    "citations",
    "reasoning_summary",
)


def _stored(record: dict, field: str):
    value = record.get(field)
    if field == "quantiles":
        return [(value or {}).get(key) for key in QUANTILES]
    if field == "quantiles_repaired":
        return bool(value)
    return value


def _current(parsed, field: str):
    if field == "quantiles":
        return [parsed.quantiles.get(key) for key in QUANTILES]
    return getattr(parsed, field)


def current_stale_rows() -> dict[str, dict]:
    """Successful cached rows whose stored parse differs from the current parser.

    Each entry names the differing fields and gives the current numeric
    reading, or the current rejection message.
    """
    stale: dict[str, dict] = {}
    for location, record in _cached_records():
        if not record.get("parsed_ok") or location not in _reparsed():
            continue
        status, value = _reparsed()[location]
        if status == "rejected":
            stale[location] = {"rejected": value}
            continue
        changed = [
            field
            for field in PARSED_FIELDS
            if _current(value, field) != _stored(record, field)
        ]
        if changed:
            stale[location] = {
                "changed_fields": changed,
                "point_estimate": value.point_estimate,
                "quantiles": _current(value, "quantiles"),
                "quantiles_repaired": value.quantiles_repaired,
            }
    return stale


def test_cached_rows_match_the_current_parser_except_pinned_stale_rows():
    pinned = json.loads(STALE_ROWS_PATH.read_text())
    assert current_stale_rows() == pinned


if __name__ == "__main__":  # regenerate the pinned fixture
    STALE_ROWS_PATH.parent.mkdir(exist_ok=True)
    STALE_ROWS_PATH.write_text(json.dumps(current_stale_rows(), indent=2, sort_keys=True) + "\n")
