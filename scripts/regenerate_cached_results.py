"""Bring cached run artifacts in line with the current parser and pooling code.

For every ``results/**/runs.jsonl`` this script:

1. re-parses each successful row's retained ``raw_response`` and, where any
   parsed field differs from the stored one, rewrites that row's parsed
   fields in ``runs.jsonl`` and ``runs.csv`` (all other rows keep their exact
   bytes);
2. recomputes each ``summary.csv`` row's scientific fields (counts, pooled
   center and interval, SDs, REML and Bayes columns) with
   ``summarize_run_results``, keeping usage and cost columns and any
   committed value that the recomputation matches to 1e-12.

Rows that the current parser now *rejects* are never flipped to failed: that
would drop a slot from an exact 15-run grid, and whether to exclude,
re-elicit or hand-correct such a slot is a methodology decision. They are
listed as kept-as-stored instead. No provider is called; failed-run archives
are not touched.

Usage:
    python scripts/regenerate_cached_results.py [--check]

``--check`` reports what would change without writing and exits 1 if
anything would.
"""

from __future__ import annotations

import argparse
import csv
import io
import json
import math
import sys
from dataclasses import fields
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))

from llm_econ_beliefs import parse_belief_response  # noqa: E402
from llm_econ_beliefs.experiment import summarize_run_results  # noqa: E402
from llm_econ_beliefs.models import RequestLog, RunResult  # noqa: E402

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
SUMMARY_SCIENTIFIC_FIELDS = (
    "n_successful_runs",
    "n_quantile_repaired_runs",
    "pooled_point_estimate",
    "pooled_lower_bound",
    "pooled_upper_bound",
    "within_run_sd",
    "between_run_sd",
    "total_sd",
    "pool_transform",
    "reml_latent_location",
    "reml_latent_lower",
    "reml_latent_upper",
    "reml_predictive_lower",
    "reml_predictive_upper",
    "reml_tau",
    "reml_typical_within_sd",
    "bayes_latent_location",
    "bayes_latent_lower",
    "bayes_latent_upper",
    "bayes_predictive_lower",
    "bayes_predictive_upper",
    "bayes_tau_mean",
    "bayes_interval_scale_mean",
    "bayes_typical_within_sd",
)
RUN_FIELDS = {field.name for field in fields(RunResult)}
REQUEST_FIELDS = {field.name for field in fields(RequestLog)}


def _read(path: Path) -> str:
    # Exact bytes: the CSVs are CRLF, which read_text() would translate.
    return path.read_bytes().decode("utf-8")


def _read_jsonl(path: Path) -> list[str]:
    # Split on "\n" only: JSON strings may hold U+2028 and similar.
    return _read(path).split("\n")


def reparse_rows(lines: list[str]) -> tuple[list[str], list[int], list[tuple[int, str]]]:
    """Return updated lines, changed line numbers and kept rejections."""
    updated = list(lines)
    changed: list[int] = []
    rejected: list[tuple[int, str]] = []
    for index, line in enumerate(lines):
        if not line.strip():
            continue
        row = json.loads(line)
        raw = row.get("raw_response")
        if not row.get("parsed_ok") or not raw:
            continue
        try:
            parsed = parse_belief_response(raw, quantity_id=row.get("quantity_id"))
        except ValueError as exc:
            rejected.append((index + 1, str(exc)))
            continue
        new_values = {
            "point_estimate": parsed.point_estimate,
            "lower_bound": parsed.lower_bound,
            "upper_bound": parsed.upper_bound,
            "confidence_level": parsed.confidence_level,
            "quantiles": dict(parsed.quantiles),
            "quantiles_repaired": parsed.quantiles_repaired,
            "interpretation": parsed.interpretation,
            "citations": list(parsed.citations),
            "reasoning_summary": parsed.reasoning_summary,
        }
        stored = {name: row.get(name) for name in PARSED_FIELDS}
        stored["quantiles_repaired"] = bool(stored["quantiles_repaired"])
        if stored == new_values:
            continue
        if "quantiles_repaired" not in row and not new_values["quantiles_repaired"]:
            del new_values["quantiles_repaired"]  # keep the legacy schema
        row.update(new_values)
        updated[index] = json.dumps(row)
        changed.append(index + 1)
    return updated, changed, rejected


def patch_runs_csv(path: Path, jsonl_lines: list[str], changed: list[int]) -> str:
    """Rewrite only the runs.csv rows for changed records, in the file's schema."""
    text = _read(path)
    rows = list(csv.reader(io.StringIO(text, newline="")))
    header = rows[0]
    record_lines = [line for line in jsonl_lines if line.strip()]
    changed_records = {
        sum(1 for line in jsonl_lines[: number - 1] if line.strip()) for number in changed
    }
    if len(rows) - 1 != len(record_lines):
        raise RuntimeError(f"{path}: {len(rows) - 1} CSV rows vs {len(record_lines)} records")
    output = io.StringIO(newline="")
    writer = csv.writer(output)
    for position, row in enumerate(rows):
        record_index = position - 1
        if record_index in changed_records:
            record = json.loads(record_lines[record_index])
            values = dict(record)
            values["quantiles"] = json.dumps(record.get("quantiles") or {}, sort_keys=True)
            values["citations"] = " | ".join(record.get("citations") or [])
            row = ["" if values.get(name) is None else str(values[name]) for name in header]
        writer.writerow(row)
    return output.getvalue()


def _same_number(committed: str, value: object) -> bool:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return False
    try:
        old = float(committed)
    except ValueError:
        return False
    return math.isclose(old, float(value), rel_tol=1e-12, abs_tol=1e-15)


def patch_summary_csv(path: Path, jsonl_lines: list[str], requests_path: Path) -> str | None:
    if not path.exists() or not _read(path).strip():
        return None
    records = [
        RunResult(**{k: v for k, v in json.loads(line).items() if k in RUN_FIELDS})
        for line in jsonl_lines
        if line.strip()
    ]
    request_logs = []
    if requests_path.exists():
        request_logs = [
            RequestLog(**{k: v for k, v in json.loads(line).items() if k in REQUEST_FIELDS})
            for line in _read_jsonl(requests_path)
            if line.strip()
        ]
    fresh = {
        (row["model_name"], row["quantity_id"]): row
        for row in summarize_run_results(records, request_logs=request_logs)
    }
    text = _read(path)
    rows = list(csv.reader(io.StringIO(text, newline="")))
    header = rows[0]
    output = io.StringIO(newline="")
    writer = csv.writer(output)
    writer.writerow(header)
    for row in rows[1:]:
        values = dict(zip(header, row))
        new = fresh.get((values["model_name"], values["quantity_id"]))
        if new is None:
            raise RuntimeError(f"{path}: no recomputed row for {values['quantity_id']}")
        for name in SUMMARY_SCIENTIFIC_FIELDS:
            if name not in values:
                continue
            value = new.get(name)
            committed = values[name]
            if _same_number(committed, value):
                continue
            rendered = "" if value is None else str(value)
            if rendered != committed:
                values[name] = rendered
        writer.writerow([values[name] for name in header])
    return output.getvalue()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--results", type=Path, default=REPO_ROOT / "results")
    args = parser.parse_args(argv)

    changed_files: list[str] = []
    kept_rejections: list[str] = []
    changed_rows = 0
    for runs_path in sorted(args.results.rglob("runs.jsonl")):
        directory = runs_path.parent
        lines = _read_jsonl(runs_path)
        updated, changed, rejected = reparse_rows(lines)
        for number, message in rejected:
            kept_rejections.append(
                f"{runs_path.relative_to(args.results.parent)}:{number}: {message}"
            )
        outputs: dict[Path, str] = {}
        if changed:
            changed_rows += len(changed)
            outputs[runs_path] = "\n".join(updated)
            runs_csv = directory / "runs.csv"
            if runs_csv.exists():
                outputs[runs_csv] = patch_runs_csv(runs_csv, updated, changed)
        summary = patch_summary_csv(directory / "summary.csv", updated, directory / "requests.jsonl")
        if summary is not None:
            outputs[directory / "summary.csv"] = summary
        for path, text in outputs.items():
            if _read(path) == text:
                continue
            changed_files.append(str(path.relative_to(args.results.parent)))
            if not args.check:
                path.write_bytes(text.encode("utf-8"))

    print(f"re-parsed rows changed: {changed_rows}")
    print(f"files {'to change' if args.check else 'changed'}: {len(changed_files)}")
    for name in changed_files:
        print(f"  {name}")
    print(f"rows the current parser rejects, kept as stored: {len(kept_rejections)}")
    for entry in kept_rejections:
        print(f"  {entry}")
    return 1 if args.check and changed_files else 0


if __name__ == "__main__":
    raise SystemExit(main())
