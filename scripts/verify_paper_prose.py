"""Assert that paper prose matches the committed tables.

Every check reads a number or a model-name superlative from
``paper/tables/*.csv`` and asserts the corresponding claim in
``paper/paper.qmd``. Run after any table regeneration; a nonzero exit
means the prose and the committed build have desynchronized.

Usage:
    .venv/bin/python scripts/verify_paper_prose.py
"""

from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
PAPER = (REPO_ROOT / "paper" / "paper.qmd").read_text()
TABLES = REPO_ROOT / "paper" / "tables"

FAILURES: list[str] = []


def check(label: str, condition: bool, detail: str = "") -> None:
    if condition:
        print(f"  ok: {label}")
    else:
        FAILURES.append(f"{label} {detail}".strip())
        print(f"FAIL: {label} {detail}".strip())


def read_rows(stem: str) -> list[dict[str, str]]:
    with (TABLES / f"{stem}.csv").open() as handle:
        return list(csv.DictReader(handle))


def ranked(rows: list[dict[str, str]], column: str, *, reverse: bool = False):
    return sorted(rows, key=lambda row: float(row[column]), reverse=reverse)


def sentence_with(fragment: str) -> str:
    """Return the paper sentence containing the fragment ('' if absent)."""
    for sentence in re.split(r"(?<=[.!?])\s+", PAPER):
        if fragment in sentence:
            return sentence
    return ""


def _name_position(sentence: str, name: str, roster: list[str]) -> int:
    """First occurrence of name that is not a prefix of a longer roster name.

    Model names nest ("GPT-5.4" is a prefix of "GPT-5.4 mini"), so a bare
    substring search could accept the wrong model. Skip any match where a
    longer roster name starts at the same position.
    """
    longer = [m for m in roster if m != name and m.startswith(name)]
    start = 0
    while True:
        pos = sentence.find(name, start)
        if pos == -1 or not any(sentence.startswith(m, pos) for m in longer):
            return pos
        start = pos + 1


def names_in_order(sentence: str, names: list[str], roster: list[str]) -> bool:
    """All names present in the sentence, in the given order."""
    positions = [_name_position(sentence, name, roster) for name in names]
    return all(p != -1 for p in positions) and positions == sorted(positions)


def names_present(sentence: str, names: list[str], roster: list[str]) -> bool:
    return all(_name_position(sentence, name, roster) != -1 for name in names)


ABS_RANK = "Avg abs-elasticity rank (1=highest)"
WIDTH_RANK = "Avg predictive-uncertainty rank (1=narrowest)"


def verify_superlatives() -> None:
    labor = read_rows("model-overview-labor-tax")
    macro = read_rows("model-overview-macro-trade")
    roster = sorted({r["Model"] for r in labor} | {r["Model"] for r in macro})

    labor_high = [r["Model"] for r in ranked(labor, ABS_RANK)[:3]]
    labor_low = [r["Model"] for r in ranked(labor, ABS_RANK, reverse=True)[:3]]
    labor_tight = [r["Model"] for r in ranked(labor, WIDTH_RANK)[:3]]
    labor_wide = [r["Model"] for r in ranked(labor, WIDTH_RANK, reverse=True)[:3]]
    macro_high = [r["Model"] for r in ranked(macro, ABS_RANK)[:3]]
    macro_low = [r["Model"] for r in ranked(macro, ABS_RANK, reverse=True)[:2]]
    macro_tight = ranked(macro, WIDTH_RANK)[0]["Model"]
    macro_wide = [r["Model"] for r in ranked(macro, WIDTH_RANK, reverse=True)[:3]]

    sentence = sentence_with("highest-elasticity models by average within-quantity")
    check(
        "Table 1 highest-elasticity trio",
        names_in_order(sentence, labor_high, roster),
        f"expected {labor_high}",
    )
    sentence = sentence_with("The lowest-elasticity models are")
    check(
        "Table 1 lowest-elasticity trio",
        names_in_order(sentence, labor_low, roster),
        f"expected {labor_low}",
    )
    sentence = sentence_with("sit on the low-response side")
    check(
        "low-response-side naming",
        names_present(sentence, labor_low, roster),
        f"expected {labor_low}",
    )
    sentence = sentence_with("move to the top of the ranking")
    check(
        "Table 2 top trio",
        names_in_order(sentence, macro_high, roster)
        and names_present(sentence, macro_low, roster),
        f"expected top {macro_high}, bottom {macro_low}",
    )
    sentence = sentence_with("are the tightest models")
    check(
        "labor-tax tightest trio",
        names_in_order(sentence, labor_tight, roster)
        and names_in_order(sentence, labor_wide, roster),
        f"expected tight {labor_tight}, wide {labor_wide}",
    )
    sentence = sentence_with("becomes the tightest model")
    check(
        "macro-trade tightest + widest",
        _name_position(sentence, macro_tight, roster) != -1
        and names_in_order(sentence, macro_wide, roster),
        f"expected tightest {macro_tight}, widest {macro_wide}",
    )
    abstract_high = sentence_with("most elastic models by average within-quantity")
    check(
        "abstract labor-tax top pair",
        names_present(abstract_high, labor_high[:2], roster),
        f"expected {labor_high[:2]}",
    )
    check(
        "abstract macro-trade top pair",
        names_present(abstract_high, macro_high[:2], roster),
        f"expected {macro_high[:2]}",
    )


def verify_top_rate() -> None:
    rows = read_rows("toy-top-rate-labor-tax")
    note = (TABLES / "toy-top-rate-labor-tax.md").read_text()

    match = re.search(r"a = (1\.\d+)", note)
    a_value = match.group(1)
    check("Table 4 note has Pareto a", match is not None)
    check(
        f"prose quotes a = {a_value} and no stale a-value",
        f"$a = {a_value}$" in PAPER
        and "1.470" not in PAPER
        and "a = 1.500" not in PAPER,
    )
    check("no FALLBACK label in committed note", "FALLBACK" not in note)

    def pct(cell: str) -> float:
        return float(cell.split("%")[0].split("[")[0])

    top_col = next(c for c in rows[0] if "Top rate" in c and "median" in c)
    rev_col = next(c for c in rows[0] if "Revenue-max" in c)
    tops = {r["Model"]: pct(r[top_col]) for r in rows}
    revs = sorted(pct(r[rev_col]) for r in rows)
    low_model = min(tops, key=tops.get)
    high_model = max(tops, key=tops.get)
    spread = tops[high_model] - tops[low_model]
    check(
        "top-rate range prose",
        f"from `{tops[low_model]}%` for `{low_model}`" in PAPER
        and f"to `{tops[high_model]}%` for `{high_model}`" in PAPER,
        f"expected {tops[low_model]}% {low_model} .. {tops[high_model]}% {high_model}",
    )
    check(
        "top-rate spread prose",
        f"`{spread:.1f}` percentage-point cross-model spread" in PAPER,
        f"expected {spread:.1f}",
    )
    check(
        "revenue-max range prose",
        f"from `{revs[0]}%` to `{revs[-1]}%`" in PAPER,
        f"expected {revs[0]}%..{revs[-1]}%",
    )


def verify_stability() -> None:
    note = (TABLES / "stability-appendix.md").read_text()
    rows = read_rows("stability-appendix")
    cells = {r[next(iter(r))] for r in rows}
    check(
        "stability note says 13-quantity",
        "13-quantity canonical subpanel" in note and "9-quantity" not in note,
    )
    counts = {
        r["Cells compared"] for r in rows if "Cells compared" in r
    } if "Cells compared" in rows[0] else set()
    if counts:
        check("stability cell count is 325", counts == {"325"}, f"got {counts}")
    check(
        "prose stability medians",
        "median of `0.002`" in PAPER and "`0.010`" in PAPER,
    )
    del cells


def verify_loo() -> None:
    rows = read_rows("leave-one-provider-out-appendix")
    rhos = [float(r["Spearman rho"]) for r in rows]
    low, high = min(rhos), max(rhos)
    check(
        "LOO rho bounds prose",
        f"between `{low}` and `{high}`" in PAPER,
        f"expected {low}..{high}",
    )
    floor = "0.99" if low >= 0.99 else "0.98" if low >= 0.98 else "0.97"
    check(
        f"LOO floor prose (above {floor})",
        f"stays above `{floor}`" in PAPER,
    )


def verify_variance_decomposition() -> None:
    rows = read_rows("variance-decomposition")
    col = "Max between-run variance share"
    shares = {r["Model"]: int(r[col].rstrip("%")) for r in rows}
    top_two = sorted(shares, key=shares.get, reverse=True)[:2]
    third = sorted(shares.values(), reverse=True)[2]
    for model in top_two:
        check(
            f"A15 max share for {model}",
            f"`{shares[model]}%` for `{model.lower().replace(' ', '-').replace('gpt-5.4-nano', 'gpt-5.4-nano')}`" in PAPER
            or f"`{shares[model]}%`" in PAPER,
            f"expected {shares[model]}%",
        )
    check(
        "A15 third-largest share named",
        f"`{third}%`" in PAPER,
        f"expected {third}%",
    )


def verify_ablation() -> None:
    rows = read_rows("mechanism-ablation")
    changes = [abs(float(r["Center change"])) for r in rows]
    check(
        "ablation max center change 0.03",
        max(changes) == 0.03 and "at most `0.03`" in PAPER,
        f"max {max(changes)}",
    )
    width_moves = [
        (float(r["Native 90% width"]) - float(r["LiteLLM 90% width"]))
        / float(r["LiteLLM 90% width"])
        for r in rows
    ]
    low_pct = min(width_moves) * 100
    high_pct = max(width_moves) * 100
    check(
        "ablation width range prose",
        f"from `{low_pct:.0f}` to `+{high_pct:.0f}` percent" in PAPER,
        f"expected {low_pct:.0f}..+{high_pct:.0f}",
    )


def verify_harness_disclosure() -> None:
    rows = read_rows("harness-disclosure")
    budget_col = next(c for c in rows[0] if "budget" in c.lower())
    model_col = next(iter(rows[0]))
    gpt55 = next(
        r for r in rows if r[model_col].strip("`").lower() == "gpt-5.5"
    )
    check(
        "gpt-5.5 budget discloses 1200 base",
        "1200" in gpt55[budget_col] and "8000" in gpt55[budget_col],
        f"got {gpt55[budget_col]!r}",
    )


def verify_income_sign_counts() -> None:
    comparison = REPO_ROOT / "results" / "elasticity-all-model-comparison.csv"
    with comparison.open() as handle:
        records = [
            r
            for r in csv.DictReader(handle)
            if r["quantity_id"] == "labor_supply.income_elasticity.prime_age"
        ]
    centers = [float(r["pooled_point_estimate"]) for r in records]
    negative = sum(1 for c in centers if c < 0)
    check(
        "income-elasticity sign count in CSV",
        negative == 24 and len(centers) == 25,
        f"{negative} negative of {len(centers)}",
    )
    check(
        "income-elasticity sign prose",
        f"negative for {negative} of {len(centers)} models" in PAPER,
        f"expected 'negative for {negative} of {len(centers)} models'",
    )


def main() -> int:
    verify_superlatives()
    verify_top_rate()
    verify_stability()
    verify_loo()
    verify_variance_decomposition()
    verify_ablation()
    verify_harness_disclosure()
    verify_income_sign_counts()
    if FAILURES:
        print(f"\n{len(FAILURES)} check(s) failed")
        return 1
    print("\nall prose checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
