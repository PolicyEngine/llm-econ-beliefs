"""List every published number that differs between two checkouts.

Compares, cell by cell, every CSV under ``results/`` (top-level artifacts and
each experiment's ``summary.csv``) and ``paper/tables/``, and line by line
every Markdown table under ``paper/tables/``. Rows are matched by position;
a changed header or row count is reported as a structural change. Numeric
cells are compared as floats (so ``0.10`` and ``0.1`` are equal); everything
else is compared as text.

Usage:
    python scripts/diff_published_numbers.py OLD_ROOT NEW_ROOT --output diff.md
"""

from __future__ import annotations

import argparse
import csv
import difflib
import math
import sys
from pathlib import Path


def published_csvs(root: Path) -> list[Path]:
    paths = set((root / "results").glob("*.csv"))
    paths |= set((root / "results").glob("*/summary.csv"))
    paths |= set((root / "paper" / "tables").glob("*.csv"))
    return sorted(path.relative_to(root) for path in paths)


def published_markdown(root: Path) -> list[Path]:
    return sorted(
        path.relative_to(root) for path in (root / "paper" / "tables").glob("*.md")
    )


def _as_float(value: str) -> float | None:
    try:
        number = float(value)
    except ValueError:
        return None
    return number if math.isfinite(number) else None


def _read_csv(path: Path) -> tuple[list[str], list[list[str]]]:
    with path.open(newline="") as handle:
        rows = list(csv.reader(handle))
    return (rows[0], rows[1:]) if rows else ([], [])


def _row_label(header: list[str], row: list[str]) -> str:
    """A readable identity for a row: its leading non-numeric cells."""
    parts = []
    for name, value in zip(header, row):
        if _as_float(value) is not None or not value:
            continue
        parts.append(value)
        if len(parts) == 3:
            break
    return " / ".join(parts) or "(row)"


def diff_csv(old: Path, new: Path) -> tuple[list[str], list[tuple[str, str, str, str, str]]]:
    notes: list[str] = []
    changes: list[tuple[str, str, str, str, str]] = []
    old_header, old_rows = _read_csv(old)
    new_header, new_rows = _read_csv(new)
    if old_header != new_header:
        notes.append(f"header changed: {old_header} -> {new_header}")
        return notes, changes
    if len(old_rows) != len(new_rows):
        notes.append(f"row count changed: {len(old_rows)} -> {len(new_rows)}")
    old_labels = [_row_label(old_header, row) for row in old_rows]
    new_labels = [_row_label(new_header, row) for row in new_rows]
    if (
        len(set(old_labels)) == len(old_labels)
        and set(old_labels) == set(new_labels)
        and old_labels != new_labels
    ):
        # Same rows in a new order (tables sorted by a value that moved):
        # match by row identity, and say the order changed.
        notes.append("row order changed; rows matched by identity")
        by_label = dict(zip(new_labels, new_rows))
        new_rows = [by_label[label] for label in old_labels]
    for index, (old_row, new_row) in enumerate(zip(old_rows, new_rows), 2):
        for column, old_value, new_value in zip(old_header, old_row, new_row):
            if old_value == new_value:
                continue
            old_number, new_number = _as_float(old_value), _as_float(new_value)
            if old_number is not None and new_number is not None and old_number == new_number:
                continue
            changes.append(
                (f"{index}", _row_label(old_header, old_row), column, old_value, new_value)
            )
    return notes, changes


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("old_root", type=Path)
    parser.add_argument("new_root", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args(argv)

    lines = [
        "# Changed published numbers",
        "",
        f"Old: `{args.old_root}`  ",
        f"New: `{args.new_root}`",
        "",
    ]
    total_cells = 0
    changed_files = 0
    for relative in sorted(set(published_csvs(args.old_root)) | set(published_csvs(args.new_root))):
        old, new = args.old_root / relative, args.new_root / relative
        if not old.exists() or not new.exists():
            lines += [f"## `{relative}`", "", "only in " + ("new" if new.exists() else "old"), ""]
            changed_files += 1
            continue
        notes, changes = diff_csv(old, new)
        if not notes and not changes:
            continue
        changed_files += 1
        total_cells += len(changes)
        lines += [f"## `{relative}` ({len(changes)} cells)", ""]
        lines += [f"- {note}" for note in notes]
        if changes:
            lines += ["| line | row | column | old | new |", "|---|---|---|---|---|"]
            lines += [
                f"| {line} | {label} | {column} | {old_value} | {new_value} |"
                for line, label, column, old_value, new_value in changes
            ]
        lines.append("")

    for relative in sorted(set(published_markdown(args.old_root)) | set(published_markdown(args.new_root))):
        old, new = args.old_root / relative, args.new_root / relative
        old_lines = old.read_text().splitlines() if old.exists() else []
        new_lines = new.read_text().splitlines() if new.exists() else []
        if old_lines == new_lines:
            continue
        changed_files += 1
        lines += [f"## `{relative}` (Markdown)", "", "```diff"]
        lines += [
            line
            for line in difflib.unified_diff(old_lines, new_lines, lineterm="", n=0)
            if not line.startswith(("---", "+++"))
        ]
        lines += ["```", ""]

    lines.insert(5, f"{changed_files} files changed; {total_cells} CSV cells changed.\n")
    report = "\n".join(lines) + "\n"
    if args.output:
        args.output.write_text(report)
    else:
        sys.stdout.write(report)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
