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
import json
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
    sentence = sentence_with("sit on the high-response side")
    check(
        "high-response-side naming",
        names_present(sentence, labor_high, roster),
        f"expected {labor_high}",
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
    width_col = next(c for c in rows[0] if "width" in c.lower())
    widths = sorted(float(r[width_col]) for r in rows)
    check(
        "top-rate interval-width range prose",
        f"roughly `{round(widths[0])}` to `{round(widths[-1])}` percentage points wide" in PAPER,
        f"expected roughly {round(widths[0])}..{round(widths[-1])} (table {widths[0]}..{widths[-1]})",
    )


def verify_stability() -> None:
    note = (TABLES / "stability-appendix.md").read_text()
    rows = read_rows("stability-appendix")
    cells = {r[next(iter(r))] for r in rows}
    check(
        "stability note says 13-quantity",
        "13-quantity canonical subpanel" in note and "9-quantity" not in note,
    )
    with (REPO_ROOT / "results" / "model-registry.csv").open() as handle:
        n_models = len(list(csv.DictReader(handle)))
    expected_cells = str(13 * n_models)
    counts = {
        r["Cells compared"] for r in rows if "Cells compared" in r
    } if "Cells compared" in rows[0] else set()
    if counts:
        check(
            f"stability cell count is {expected_cells}",
            counts == {expected_cells},
            f"got {counts}",
        )
    check(
        "A1 prose cell count",
        f"({expected_cells} cells at every prefix length)" in PAPER,
        f"expected {expected_cells}",
    )
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
    sys.path.insert(0, str(REPO_ROOT))
    from llm_econ_beliefs.providers import (  # noqa: E402
        ANTHROPIC_MAX_OUTPUT_TOKENS,
        LITELLM_MAX_COMPLETION_TOKENS_BY_MODEL,
        OPENAI_MAX_COMPLETION_TOKENS_BY_MODEL,
    )

    rows = read_rows("harness-disclosure")
    budget_col = next(c for c in rows[0] if "budget" in c.lower())
    model_col = next(iter(rows[0]))

    def row_for(model_id: str) -> dict[str, str] | None:
        # Compare hyphen-insensitively: PolicyBench-style ids drop the
        # hyphen between family and version (qwen3.8-max), while display
        # labels space everything (Qwen 3.8 Max).
        def canon(value: str) -> str:
            return value.strip("`").lower().replace(" ", "").replace("-", "")

        for row in rows:
            if canon(row[model_col]) == canon(model_id):
                return row
        return None

    gpt55 = row_for("gpt-5.5")
    check(
        "gpt-5.5 budget discloses 1200 base",
        gpt55 is not None
        and "1200" in gpt55[budget_col]
        and "8000" in gpt55[budget_col],
        f"got {gpt55 and gpt55[budget_col]!r}",
    )

    # Every model with a canonical budget in providers.py must disclose that
    # budget in A16 (rows may also document historical protocols, so the
    # check is membership, not equality). Catches drift like the GLM-5.2
    # 16000-token rerun landing in providers.py but not the table.
    canonical = dict(LITELLM_MAX_COMPLETION_TOKENS_BY_MODEL)
    canonical.update(OPENAI_MAX_COMPLETION_TOKENS_BY_MODEL)
    canonical.update(
        {
            model_id: ANTHROPIC_MAX_OUTPUT_TOKENS
            for model_id in ("claude-fable-5", "claude-opus-4.8", "claude-sonnet-5")
        }
    )
    for model_id, budget in sorted(canonical.items()):
        row = row_for(model_id)
        disclosed = set(re.findall(r"\d+", row[budget_col])) if row else set()
        check(
            f"A16 budget for {model_id} includes {budget}",
            row is not None and str(budget) in disclosed,
            f"got {sorted(disclosed)}",
        )


def verify_resampling_range() -> None:
    rows = read_rows("resampling-stability")
    ses = [
        float(r["Median relative width MC SE"].rstrip("%").strip())
        for r in rows
    ]
    low, high = min(ses), max(ses)
    claim = f"run `{low:.0f}` to `{high:.0f}` percent"
    count = PAPER.count(claim)
    check(
        "A14 width-SE range in both prose mentions",
        count == 2,
        f"expected 2 occurrences of {claim!r}, found {count}",
    )


def verify_rank_spread_tie() -> None:
    rows = read_rows("pooling-robustness-appendix")
    col = "Max rank spread"
    top = max(float(r[col]) for r in rows)
    tied = [r["Model"] for r in rows if float(r[col]) == top]
    sentence = sentence_with("largest rank spread is")
    roster = [r["Model"] for r in rows]
    check(
        "A2 largest rank spread names every tied model",
        f"`{top}` positions" in sentence
        and names_present(sentence, tied, roster),
        f"expected {top} for {tied}",
    )


def verify_correlates() -> None:
    """Pin the correlates-and-country section to results/correlates-*.csv."""
    results = REPO_ROOT / "results"

    with (results / "correlates-spearman.csv").open() as handle:
        spearman = list(csv.DictReader(handle))
    eti_rows = {
        r["predictor"]: r for r in spearman if r["outcome"] == "ETI pooled median"
    }
    overall = next(v for k, v in eti_rows.items() if k.startswith("Overall"))
    tax = next(v for k, v in eti_rows.items() if k.startswith("Tax"))
    rho_claim = (
        f"$\\rho = {float(overall['spearman_rho']):.2f}$"
        f" and ${float(tax['spearman_rho']):.2f}$"
    )
    p_claim = (
        f"raw $p$ of `{float(overall['raw_p']):.3f}`"
        f" and `{float(tax['raw_p']):.3f}`"
    )
    n_values = {r["n_models"] for r in eti_rows.values()}
    check(
        "capability rho per predictor in prose",
        len(eti_rows) == 2
        and rho_claim in PAPER
        and p_claim in PAPER
        and "$\\rho \\approx -0.5$" in PAPER
        and len(n_values) == 1
        and f"$n = {next(iter(n_values))}$" in PAPER,
        f"expected {rho_claim!r} and {p_claim!r}; got "
        f"{[(r['spearman_rho'], r['raw_p'], r['n_models']) for r in eti_rows.values()]}",
    )
    min_holm = min(float(r["holm_adjusted_p"]) for r in spearman)
    min_bh = min(float(r["bh_adjusted_p"]) for r in spearman)
    check(
        "Holm and BH minima in prose",
        f"`{min_holm:.3f}`" in PAPER and f"`{min_bh:.3f}`" in PAPER,
        f"expected {min_holm:.3f} and {min_bh:.3f}",
    )

    sys.path.insert(0, str(REPO_ROOT))
    from llm_econ_beliefs.model_registry import (  # noqa: E402
        MODEL_REGISTRY,
        ORGANIZATIONS,
        ORGANIZATION_COUNTRY,
    )

    with (results / "correlates-sensitivity.csv").open() as handle:
        sensitivity = list(csv.DictReader(handle))
    loo = [
        float(r["spearman_rho"])
        for r in sensitivity
        if r["analysis"] == "leave_one_organization_out"
        and r["predictor"].startswith("Overall")
    ]
    check(
        "LOO-organization rho range in prose",
        len(loo) == len(ORGANIZATIONS)
        and f"between `{max(loo):.2f}` and `{min(loo):.2f}`" in PAPER,
        f"expected between {max(loo):.2f} and {min(loo):.2f} over {len(loo)}",
    )

    with (results / "correlates-country.csv").open() as handle:
        country = {r["outcome"]: r for r in csv.DictReader(handle)}
    with (REPO_ROOT / "results" / "model-registry.csv").open() as handle:
        n_models = len(list(csv.DictReader(handle)))
    tau = country["Implied optimal top rate (%)"]
    eti = country["ETI pooled median"]
    width = country["Avg interval-width rank (1 = tightest)"]

    china_models = sum(
        1
        for model in MODEL_REGISTRY
        if ORGANIZATION_COUNTRY[model.organization] == "china"
    )
    check(
        "country top-rate medians and p",
        f"`{float(tau['china_median']):.1f}%` versus `{float(tau['us_median']):.1f}%`" in PAPER
        and f"$p = {float(tau['permutation_p']):.3f}$" in PAPER
        and int(tau["china_n"]) == china_models
        and int(tau["us_n"]) + int(tau["china_n"]) == n_models,
        f"got {tau['china_median']} vs {tau['us_median']}, p {tau['permutation_p']}",
    )
    check(
        "country ETI medians and p",
        f"`{float(eti['china_median']):.3f}` versus `{float(eti['us_median']):.3f}`" in PAPER
        and f"$p = {float(eti['permutation_p']):.3f}$" in PAPER,
        f"got {eti['china_median']} vs {eti['us_median']}, p {eti['permutation_p']}",
    )
    check(
        "country width-rank medians and p",
        f"`{float(width['china_median']):.1f}` versus `{float(width['us_median']):.1f}`" in PAPER
        and f"$p = {float(width['permutation_p']):.3f}$" in PAPER,
        f"got {width['china_median']} vs {width['us_median']}, p {width['permutation_p']}",
    )
    labor_center = country["Mean |center|, labor-and-tax"]
    check(
        "country labor-and-tax center medians and p",
        f"`{float(labor_center['china_median']):.3f}` versus "
        f"`{float(labor_center['us_median']):.3f}`, "
        f"$p = {float(labor_center['permutation_p']):.3f}$" in PAPER
        and f"centers $p = {float(labor_center['permutation_p']):.3f}$" in PAPER,
        f"got {labor_center['china_median']} vs {labor_center['us_median']}, "
        f"p {labor_center['permutation_p']}",
    )
    check(
        "country rows disclose the confound",
        all("confounded" in r["disclosure"] for r in country.values()),
    )


# Cover 1-99 so panel growth can never KeyError a check mid-run (a crash
# here hides every later check, which happened at 26, again at 18, and
# again at 31 when the cap was 30).
_ONES = (
    "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
    "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
    "seventeen", "eighteen", "nineteen", "twenty",
)
_TENS = {
    20: "twenty", 30: "thirty", 40: "forty", 50: "fifty",
    60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety",
}
NUMBER_WORDS = {i + 1: word for i, word in enumerate(_ONES)}
NUMBER_WORDS.update(
    {
        tens + unit: (f"{word}-{_ONES[unit - 1]}" if unit else word)
        for tens, word in _TENS.items()
        for unit in range(10)
    }
)


def verify_cap_gains_audit() -> None:
    """Pin the A9 sign-consistency and band counts (the round-4 regression)."""
    rows = read_rows("cap-gains-convention-audit")
    coherence_col = next(c for c in rows[0] if "coherence" in c.lower())
    band_col = next(c for c in rows[0] if c.startswith("Band"))
    consistent = sum(
        1 for r in rows if r[coherence_col].startswith("sign-consistent")
    )
    ordinary = sum(1 for r in rows if r[band_col].startswith("ordinary-income"))
    ltcg = sum(1 for r in rows if r[band_col].startswith("LTCG"))
    uninformative = sum(1 for r in rows if r[band_col].startswith("uninformative"))
    informative = consistent - uninformative
    check(
        "A9 sign-consistency count",
        f"{NUMBER_WORDS[consistent].capitalize()} of {NUMBER_WORDS[len(rows)]} models are sign-consistent"
        in PAPER
        and f"{consistent} of {len(rows)} models return a negative" in PAPER,
        f"expected {consistent}/{len(rows)}",
    )
    check(
        "A9 band split",
        f"the remaining {NUMBER_WORDS[informative]}: {NUMBER_WORDS[ordinary]} cluster in the ordinary-income-rate window and {NUMBER_WORDS[ltcg]} in the LTCG window"
        in PAPER,
        f"expected {informative}: {ordinary} ordinary / {ltcg} LTCG",
    )


def verify_top_rate_robustness() -> None:
    rows = read_rows("top-rate-robustness")

    def pct(cell: str) -> float:
        return float(cell.replace("%", "").strip())

    base = "Baseline top rate (a=1.621, gamma=1)"
    shift13 = [pct(r["Top rate (a=1.3, gamma=1)"]) - pct(r[base]) for r in rows]
    shift17 = [pct(r["Top rate (a=1.7, gamma=1)"]) - pct(r[base]) for r in rows]
    shiftg2 = [pct(r["Top rate (a=1.621, gamma=2)"]) - pct(r[base]) for r in rows]
    check(
        "A13 a=1.3 shift range",
        f"up by `{min(shift13):.1f}` to `{max(shift13):.1f}` percentage points" in PAPER,
        f"expected {min(shift13):.1f}..{max(shift13):.1f}",
    )
    check(
        "A13 a=1.7 shift range",
        f"down by `{abs(max(shift17)):.1f}` to `{abs(min(shift17)):.1f}` percentage points"
        in PAPER,
        f"expected {abs(max(shift17)):.1f}..{abs(min(shift17)):.1f}",
    )
    check(
        "A13 gamma=2 shift range",
        f"by `{min(shiftg2):.1f}` to `{max(shiftg2):.1f}` percentage points" in PAPER,
        f"expected {min(shiftg2):.1f}..{max(shiftg2):.1f}",
    )


def verify_benchmark_counts() -> None:
    rows = read_rows("benchmark-comparison-labor-tax")
    counts = {r["Quantity"]: r["Models in range"].replace(" ", "") for r in rows}

    def count_for(keyword: str) -> str:
        return next(v for k, v in counts.items() if keyword.lower() in k.lower())

    def spaced(count: str) -> str:
        inside, total = count.split("/")
        return f"`{inside} / {total}`"

    frisch = count_for("frisch")
    check(
        "Frisch in-range count",
        frisch.split("/")[0] == frisch.split("/")[1]
        and f"Every one of the {frisch.split('/')[1]} models falls inside the rough benchmark range for the Frisch"
        in PAPER,
        f"got {frisch}",
    )
    capital_gains = count_for("capital gains")
    check(
        "capital-gains in-range count",
        capital_gains == frisch
        and "benchmark range for the Frisch elasticity and for capital gains realizations"
        in PAPER,
        f"got {capital_gains}",
    )
    pair = {count_for("wage"), count_for("single mother")}
    check(
        "wage/single-mother in-range counts",
        len(pair) == 1
        and f"{spaced(next(iter(pair)))} lie inside for the uncompensated wage elasticity"
        in PAPER,
        f"got {pair}",
    )
    check(
        "income-elasticity in-range count",
        f"{spaced(count_for('income elasticity'))} for the canonical income elasticity" in PAPER,
        f"got {count_for('income elasticity')}",
    )
    check(
        "ETI in-range count",
        f"{spaced(count_for('taxable income'))} models fall inside" in PAPER,
        f"got {count_for('taxable income')}",
    )


def verify_eti_outliers() -> None:
    comparison = REPO_ROOT / "results" / "elasticity-all-model-comparison.csv"
    with comparison.open() as handle:
        records = [
            r
            for r in csv.DictReader(handle)
            if r["quantity_id"] == "tax.elasticity_of_taxable_income.top_earners"
        ]
    over = {
        r["model_name"]: float(r["pooled_point_estimate"])
        for r in records
        if float(r["pooled_point_estimate"]) > 0.5
    }
    sentence = sentence_with("just above the review band's upper anchor")
    named = all(
        model in sentence and f"`{value:.3f}`" in sentence
        for model, value in over.items()
    )
    with (REPO_ROOT / "results" / "model-registry.csv").open() as handle:
        n_models = len(list(csv.DictReader(handle)))
    check(
        "ETI out-of-band models all named with centers",
        len(records) == n_models
        and named
        and f"{NUMBER_WORDS[len(over)]} models just above" in sentence,
        f"expected {sorted(over)} over {n_models} models",
    )


def verify_quantile_rule() -> None:
    rows = read_rows("quantile-rule-appendix")
    shifts = {r["Model"]: float(r["Rank shift"]) for r in rows}
    top_model = max(shifts, key=lambda m: abs(shifts[m]))
    small = sum(1 for v in shifts.values() if abs(v) < 1)
    check(
        "A4 largest rank change and small-move count",
        f"rank change is `{abs(shifts[top_model]):.2f}` positions for `{top_model}`" in PAPER
        and f"only {small} of {len(rows)} models move by less than one rank" in PAPER,
        f"expected {abs(shifts[top_model]):.2f} for {top_model}; {small}/{len(rows)}",
    )


def verify_armington_delta() -> None:
    rows = read_rows("armington-clarify-delta")
    increases = {r["Model"]: float(r["Change"]) for r in rows if float(r["Change"]) > 0}
    sentence = sentence_with("the only increases are small")
    check(
        "A7 increases list",
        len(increases) == 3
        and all(
            f"`+{value:.3f}` for `{model}`" in sentence
            for model, value in increases.items()
        ),
        f"expected {increases}",
    )
    check(
        "A7 rerun model count in prose",
        f"Across all {len(rows)} model reruns" in PAPER
        and f"a {len(rows)}-model follow-up on the Armington elasticity" in PAPER,
        f"expected {len(rows)}",
    )


def verify_variance_median_range() -> None:
    rows = read_rows("variance-decomposition")
    col = "Median between-run variance share"
    shares = [int(r[col].rstrip("%")) for r in rows]
    check(
        "A15 median between-run share range",
        f"median of `{min(shares)}` to `{max(shares)}` percent" in PAPER,
        f"expected {min(shares)}..{max(shares)}",
    )


def verify_resampling_panel_median() -> None:
    rows = read_rows("resampling-stability")
    values = sorted(float(r["Median center MC SE"]) for r in rows)
    mid = len(values) // 2
    median = (
        values[mid]
        if len(values) % 2 == 1
        else (values[mid - 1] + values[mid]) / 2
    )
    check(
        "A14 panel-median center SE",
        f"median center standard error is `{median:.3f}`" in PAPER,
        f"expected {median:.3f}",
    )


def verify_policybench_release_pin() -> None:
    """The release named in prose must match the scores CSV's source."""
    with (REPO_ROOT / "results" / "policybench-scores.csv").open() as handle:
        releases = {r["source_release"] for r in csv.DictReader(handle)}
    check("scores CSV pins a single release", len(releases) == 1, f"got {releases}")
    release_tag = next(iter(releases)).split()[-1]
    check(
        "prose release pin matches scores CSV",
        f"pinned release `{release_tag}`" in PAPER,
        f"expected {release_tag}",
    )


def verify_posthoc_consistency() -> None:
    """Pin the post-hoc run-consistency cut to its artifact and raw data."""
    sys.path.insert(0, str(REPO_ROOT / "scripts"))
    from build_correlates import load_consistency_metrics  # noqa: E402

    with (REPO_ROOT / "results" / "correlates-posthoc.csv").open() as handle:
        rows = list(csv.DictReader(handle))
    check(
        "posthoc rows carry the post-hoc note",
        len(rows) == 4 and all("Post hoc" in r["note"] for r in rows),
        f"got {len(rows)} rows",
    )
    by_key = {(r["predictor"], r["outcome"]): r for r in rows}
    overall = by_key[
        ("Overall within-$1 (leaderboard headline)", "Max between-run variance share")
    ]
    tax = by_key[
        ("Tax within-$1 (domain-matched)", "Max between-run variance share")
    ]
    check(
        "posthoc consistency rhos and ps in prose",
        f"is `{float(overall['spearman_rho']):.2f}` (raw permutation $p = {float(overall['raw_p']):.3f}$, $n = {overall['n_models']}$)"
        in PAPER
        and f"it is `{float(tax['spearman_rho']):.2f}` ($p = {float(tax['raw_p']):.3f}$)" in PAPER,
        f"got overall {overall['spearman_rho']}/{overall['raw_p']}, tax {tax['spearman_rho']}/{tax['raw_p']}",
    )

    from llm_econ_beliefs.model_registry import MODEL_REGISTRY  # noqa: E402

    metrics = load_consistency_metrics([m.model_id for m in MODEL_REGISTRY])
    claude_max = max(
        metrics[m.model_id]["max_between_run_share"]
        for m in MODEL_REGISTRY
        if m.organization == "anthropic"
    )
    check(
        "Claude worst-case share claim",
        claude_max < 0.04 and "worst-case share stays below `4%`" in PAPER,
        f"claude max {claude_max:.3f}",
    )
    top5 = sorted(
        (metrics[m.model_id]["max_between_run_share"] for m in MODEL_REGISTRY),
        reverse=True,
    )[:5]
    claim = ", ".join(f"`{share:.0%}`" for share in top5[:4])
    claim += f", and `{top5[4]:.0%}`"
    check(
        "top-5 instability shares in prose",
        claim in PAPER,
        f"expected {claim!r}",
    )


def verify_country_family() -> None:
    """The country cut carries the same multiplicity treatment as Table 6."""
    sys.path.insert(0, str(REPO_ROOT))
    from llm_econ_beliefs.model_registry import (  # noqa: E402
        MODEL_REGISTRY,
        ORGANIZATION_COUNTRY,
    )

    with (REPO_ROOT / "results" / "correlates-country.csv").open() as handle:
        rows = list(csv.DictReader(handle))
    tested = [r for r in rows if r["is_derived"].strip().lower() != "true"]
    derived = [r for r in rows if r["is_derived"].strip().lower() == "true"]
    min_holm = min(float(r["holm_adjusted_p"]) for r in tested)
    eti = next(r for r in tested if r["outcome"] == "ETI pooled median")
    check(
        "country Holm minimum in prose",
        f"smallest Holm-adjusted p-value is `{min_holm:.3f}`" in PAPER
        and all(r["family_size"] == str(len(tested)) for r in tested),
        f"expected {min_holm:.3f} over family of {len(tested)}",
    )
    check(
        "country derived top-rate row mirrors ETI",
        len(derived) == 1
        and derived[0]["holm_adjusted_p"] == eti["holm_adjusted_p"]
        and derived[0]["bh_adjusted_p"] == eti["bh_adjusted_p"],
    )
    check(
        "country budget confound in disclosure",
        all("completion budget" in r["disclosure"] for r in rows),
    )
    us_organizations = {
        model.organization
        for model in MODEL_REGISTRY
        if ORGANIZATION_COUNTRY[model.organization] == "us"
    }
    us_models = sum(
        1
        for model in MODEL_REGISTRY
        if ORGANIZATION_COUNTRY[model.organization] == "us"
    )
    check(
        "US model and organization counts in prose",
        f"{NUMBER_WORDS[us_models]} models from "
        f"{NUMBER_WORDS[len(us_organizations)]} US organizations" in PAPER,
        f"got {us_models} models across {sorted(us_organizations)}",
    )


def verify_income_sign_counts() -> None:
    comparison = REPO_ROOT / "results" / "elasticity-all-model-comparison.csv"
    with comparison.open() as handle:
        records = [
            r
            for r in csv.DictReader(handle)
            if r["quantity_id"] == "labor_supply.income_elasticity.prime_age"
        ]
    with (REPO_ROOT / "results" / "model-registry.csv").open() as handle:
        n_models = len(list(csv.DictReader(handle)))
    centers = [float(r["pooled_point_estimate"]) for r in records]
    negative = sum(1 for c in centers if c < 0)
    check(
        "income-elasticity sign count in CSV",
        negative == len(centers) and len(centers) == n_models,
        f"{negative} negative of {len(centers)}",
    )
    check(
        "income-elasticity sign prose",
        f"negative for {negative} of {len(centers)} models" in PAPER,
        f"expected 'negative for {negative} of {len(centers)} models'",
    )


SIGN_CLARIFIED_QUANTITIES = (
    "labor_supply.income_elasticity.prime_age",
    "tax.capital_gains_realizations.elasticity",
    "tax.capital_gains_realizations.elasticity.net_of_tax_rate",
)
ORIGINAL_WORDING_MODELS = frozenset(
    {
        "claude-haiku-4.5",
        "gemini-3-flash-preview",
        "gemini-3.1-flash-lite-preview",
        "gpt-5.4",
        "gpt-5.4-mini",
        "gpt-5.4-nano",
        "grok-4.1-fast",
    }
)


def verify_prompt_identity() -> None:
    """Pin the prompt-wording disclosure to the archived request logs.

    Recomputes the per-quantity prompt census from every
    ``results/*-elasticities-batch15/runs.jsonl``: which models received
    byte-identical prompt text, quantity by quantity. Fails if the archives
    stop matching the paper's claims (23 of 26 quantities uniform across all
    28 models, the three sign-clarified quantities split 21/7 on the same
    seven April models, every cell internally uniform), if any archived
    wording other than the disclosed original stops matching what the
    current prompt builder produces, or if the prose fragments carrying the
    disclosure numbers drift.
    """
    sys.path.insert(0, str(REPO_ROOT))
    from llm_econ_beliefs.model_registry import MODEL_REGISTRY  # noqa: E402
    from llm_econ_beliefs.prompts import create_belief_prompt  # noqa: E402
    from llm_econ_beliefs.registry import get_quantity  # noqa: E402

    dirs = sorted((REPO_ROOT / "results").glob("*-elasticities-batch15"))
    check(
        f"main-panel archive count is {len(MODEL_REGISTRY)}",
        len(dirs) == len(MODEL_REGISTRY),
        f"got {len(dirs)}",
    )

    variants: dict[str, dict[str, set[str]]] = {}
    mixed: list[str] = []
    for directory in dirs:
        model = directory.name.removesuffix("-elasticities-batch15")
        cell_texts: dict[str, set[str]] = {}
        with (directory / "runs.jsonl").open() as handle:
            for line in handle:
                record = json.loads(line)
                cell_texts.setdefault(record["quantity_id"], set()).add(
                    record["prompt"]
                )
        for quantity_id, texts in cell_texts.items():
            if len(texts) > 1:
                mixed.append(f"{model}:{quantity_id}")
            for text in texts:
                variants.setdefault(quantity_id, {}).setdefault(text, set()).add(model)

    check(
        "every model-quantity cell carries one prompt text",
        not mixed,
        f"mixed cells: {mixed[:5]}",
    )
    check("archive quantity count is 26", len(variants) == 26, f"got {len(variants)}")

    split = {q: texts for q, texts in variants.items() if len(texts) > 1}
    check(
        "23 quantities byte-identical across all models",
        len(variants) - len(split) == 23
        and all(
            len(next(iter(texts.values()))) == len(MODEL_REGISTRY)
            for q, texts in variants.items()
            if q not in split
        ),
        f"got {len(variants) - len(split)} uniform",
    )
    check(
        "split quantities are exactly the three sign-clarified ones",
        set(split) == set(SIGN_CLARIFIED_QUANTITIES),
        f"got {sorted(split)}",
    )

    for quantity_id in SIGN_CLARIFIED_QUANTITIES:
        texts = variants.get(quantity_id, {})
        if len(texts) != 2:
            check(f"{quantity_id} carries two wordings", False, f"got {len(texts)}")
            continue
        (majority_text, majority), (minority_text, minority) = sorted(
            texts.items(), key=lambda item: -len(item[1])
        )
        expected_majority = len(MODEL_REGISTRY) - 7
        check(
            f"{quantity_id} splits {expected_majority}/7",
            (len(majority), len(minority)) == (expected_majority, 7),
            f"got {len(majority)}/{len(minority)}",
        )
        check(
            f"{quantity_id} original-wording membership",
            minority == ORIGINAL_WORDING_MODELS,
            f"got {sorted(minority)}",
        )
        check(
            f"{quantity_id} revised wording matches current prompt builder",
            majority_text == create_belief_prompt(get_quantity(quantity_id)),
        )
        check(
            f"{quantity_id} wording forms (iff revised, conditional original)",
            "if and only if" in majority_text and "if and only if" not in minority_text,
        )

    sibling = "tax.capital_gains_realizations.elasticity.net_of_tax_rate"
    if len(variants.get(sibling, {})) == 2:
        by_size = sorted(variants[sibling].items(), key=lambda item: -len(item[1]))
        check(
            "sibling identity backwards in original, corrected in revised",
            "minus epsilon_taxrate times tau / (1 - tau)" in by_size[1][0]
            and "epsilon_taxrate = -(tau / (1 - tau)) * epsilon_netoftax"
            in by_size[0][0],
        )

    stale = [
        quantity_id
        for quantity_id, texts in variants.items()
        if quantity_id not in split
        and next(iter(texts)) != create_belief_prompt(get_quantity(quantity_id))
    ]
    check(
        "uniform quantities match current prompt builder",
        not stale,
        f"stale: {stale[:5]}",
    )

    # prose fragments carrying the disclosure numbers
    majority_count = len(MODEL_REGISTRY) - 7
    check(
        f"abstract discloses the {majority_count}/7 wording split",
        f"{majority_count} models carry the revised text and seven April models the original" in PAPER,
    )
    check(
        "design discloses the byte-identical census",
        f"23 of the 26 quantities are byte-identical across all {len(MODEL_REGISTRY)} models" in PAPER
        and f"split {majority_count}/7 on the same seven models" in PAPER,
    )
    sentence = sentence_with("were elicited before the revision and never re-elicited")
    check(
        "design names the seven original-wording models",
        all(f"`{model_id}`" in sentence for model_id in ORIGINAL_WORDING_MODELS),
        f"sentence: {sentence[:120]!r}",
    )
    check(
        f"results section scopes the iff clarifier to {majority_count} models",
        f"revised wording that {majority_count} of the {len(MODEL_REGISTRY)} models received" in PAPER,
    )
    check(
        "A16 prose scopes prompt identity to 23 of 26 quantities",
        "byte-identical across models on 23 of the 26 quantities" in PAPER,
    )

    # A9 caveat: band counts by wording group, recomputed from the audit table
    display_to_id = {model.display_label: model.model_id for model in MODEL_REGISTRY}
    banded = {"LTCG-rate consistent", "ordinary-income-rate consistent"}
    band_col = "Band (LTCG [0.15, 0.37], ordinary-income [0.37, 0.55])"
    original_banded = original_ordinary = revised_banded = revised_ordinary = 0
    for row in read_rows("cap-gains-convention-audit"):
        band = row[band_col].strip()
        if band not in banded:
            continue
        original = display_to_id[row["Model"].strip("`")] in ORIGINAL_WORDING_MODELS
        original_banded += original
        revised_banded += not original
        if band == "ordinary-income-rate consistent":
            original_ordinary += original
            revised_ordinary += not original
    check(
        "A9 band counts by wording group",
        (revised_ordinary, revised_banded, original_ordinary, original_banded)
        == (15, 24, 5, 6),
        f"got revised {revised_ordinary}/{revised_banded}, "
        f"original {original_ordinary}/{original_banded}",
    )
    check(
        "A9 caveat prose carries the per-group band counts",
        f"{revised_ordinary} of its {revised_banded} banded models" in PAPER
        and f"{original_ordinary} of the {original_banded} banded original-wording"
        in PAPER,
    )


WORDING_SIBLING_LABEL = "Capital gains realizations elasticity (net-of-tax-rate convention)"
WORDING_DUAL_LABELS = ("Claude Opus 4.7", "Claude Sonnet 4.6", "Gemini 3.1 Pro", "Grok 4.20")


def _tau_median(cell: str) -> float:
    """Leading number of an 'x.xxx [p05, p95]' implied-tau cell."""
    return float(cell.split(" ", 1)[0])


def verify_wording_comparison_prose() -> None:
    """Pin the clarifier-wording-ablation prose (Design, A9 caveat, A18-A19)
    to the committed tables. Hermetic: reads only in-tree files, so the
    pytest wrapper can gate it in CI; the archive recomputation lives in
    ``verify_wording_comparison_tables()``.
    """
    sys.path.insert(0, str(REPO_ROOT))
    from llm_econ_beliefs.model_registry import MODEL_REGISTRY  # noqa: E402

    rows = read_rows("wording-comparison")
    tau_rows = read_rows("wording-comparison-tau")
    check(
        "A18 is 4 models x 3 quantities and A19 is 4 models",
        len(rows) == 12
        and len(tau_rows) == 4
        and [row["Model"] for row in tau_rows] == list(WORDING_DUAL_LABELS),
        f"got {len(rows)} and {[row['Model'] for row in tau_rows]}",
    )

    headline = [row for row in rows if row["Quantity"] != WORDING_SIBLING_LABEL]
    sibling = {
        row["Model"]: row for row in rows if row["Quantity"] == WORDING_SIBLING_LABEL
    }
    check("A18 has 8 headline rows and 4 sibling rows", len(headline) == 8 and len(sibling) == 4)

    max_center = max(abs(float(row["Center change"])) for row in headline)
    max_width = max(
        abs(float(row["Revised 90% width"]) - float(row["Original 90% width"]))
        for row in headline
    )
    check(
        "design and appendix quote the max headline center move",
        f"pooled centers move by at most `{max_center:.2f}`" in PAPER
        and f"pooled center moves by at most `{max_center:.2f}`" in PAPER,
        f"max headline |center change| is {max_center:.3f}",
    )
    check(
        "appendix quotes the max headline width move",
        f"width by at most `{max_width:.2f}`" in PAPER,
        f"max headline |width change| is {max_width:.3f}",
    )

    sonnet_row, gemini_row = sibling["Claude Sonnet 4.6"], sibling["Gemini 3.1 Pro"]
    check(
        "design quotes the two sibling center changes",
        f"`{float(sonnet_row['Center change']):.2f}` and "
        f"`{float(gemini_row['Center change']):+.2f}`" in PAPER,
    )
    check(
        "appendix quotes the sibling center moves",
        f"`{float(sonnet_row['Original center']):.2f}` to "
        f"`{float(sonnet_row['Revised center']):.2f}`" in PAPER
        and f"`{float(gemini_row['Original center']):.2f}` to "
        f"`{float(gemini_row['Revised center']):.2f}`" in PAPER,
    )
    check(
        "opus and grok sibling centers are the effectively-unmoved ones",
        all(
            abs(float(sibling[label]["Center change"])) <= 0.02
            for label in ("Claude Opus 4.7", "Grok 4.20")
        ),
    )

    tau = {row["Model"]: row for row in tau_rows}
    audit = {row["Model"]: row for row in read_rows("cap-gains-convention-audit")}
    check(
        "A19 revised implied-tau cells equal the published A9 cells",
        all(
            tau[label]["Revised implied tau median [90%]"]
            == audit[label]["Implied tau median [90%]"]
            for label in WORDING_DUAL_LABELS
        ),
    )
    sonnet_tau, gemini_tau = tau["Claude Sonnet 4.6"], tau["Gemini 3.1 Pro"]
    check(
        "A9 caveat quotes the two implied-tau moves",
        f"implied-tau median `{_tau_median(sonnet_tau['Original implied tau median [90%]']):.3f}` "
        f"to `{_tau_median(sonnet_tau['Revised implied tau median [90%]']):.3f}`" in PAPER
        and f"(`{_tau_median(gemini_tau['Original implied tau median [90%]']):.3f}` "
        f"to `{_tau_median(gemini_tau['Revised implied tau median [90%]']):.3f}`)" in PAPER,
    )
    check(
        "the two movers cross into the LTCG band",
        sonnet_tau["Original band"] == "plausible sign, outside bands"
        and _tau_median(sonnet_tau["Original implied tau median [90%]"]) < 0.15
        and sonnet_tau["Revised band"] == "LTCG-rate consistent"
        and gemini_tau["Original band"] == "ordinary-income-rate consistent"
        and gemini_tau["Revised band"] == "LTCG-rate consistent",
    )
    check(
        "opus and grok stay in their bands",
        all(
            tau[label]["Original band"] == tau[label]["Revised band"]
            and abs(float(tau[label]["Tau median change"])) <= 0.04
            for label in ("Claude Opus 4.7", "Grok 4.20")
        ),
    )

    # the extreme-flip parity claim in the A9 caveat, from the audit table
    display_to_id = {model.display_label: model.model_id for model in MODEL_REGISTRY}
    band_col = "Band (LTCG [0.15, 0.37], ordinary-income [0.37, 0.55])"
    ordinary_total = ltcg_total = original_ordinary = 0
    for row in read_rows("cap-gains-convention-audit"):
        band = row[band_col].strip()
        if band == "ordinary-income-rate consistent":
            ordinary_total += 1
            if display_to_id[row["Model"].strip("`")] in ORIGINAL_WORDING_MODELS:
                original_ordinary += 1
        elif band == "LTCG-rate consistent":
            ltcg_total += 1
    worst_ordinary = ordinary_total - original_ordinary
    worst_ltcg = ltcg_total + original_ordinary
    check(
        "extreme-flip split arithmetic",
        (ordinary_total, ltcg_total, original_ordinary) == (20, 10, 5)
        and (worst_ordinary, worst_ltcg) == (15, 15),
        f"got {ordinary_total}/{ltcg_total}/{original_ordinary}",
    )
    check(
        "A9 caveat carries the extreme-flip sentence",
        f"{NUMBER_WORDS[ordinary_total]}-to-{NUMBER_WORDS[ltcg_total]} ordinary-income majority" in PAPER
        and f"{NUMBER_WORDS[worst_ordinary]}-to-{NUMBER_WORDS[worst_ltcg]}" in PAPER,
    )

    check(
        "wording-ablation captions and includes are present",
        "**Appendix Table A18. Same model, two clarifier wordings: sign-clarified quantities.**"
        in PAPER
        and "**Appendix Table A19. Same model, two clarifier wordings: implied tau.**"
        in PAPER
        and "{{< include tables/wording-comparison.md >}}" in PAPER
        and "{{< include tables/wording-comparison-tau.md >}}" in PAPER,
    )
    check(
        "support-bounds table renumbered to A20",
        "**Appendix Table A20. Registry support bounds.**" in PAPER
        and "Appendix Table A20 tabulates" in PAPER
        and "Appendix Table A18. Registry support bounds" not in PAPER,
    )
    check(
        "the design section no longer defers the comparison",
        "this paper does not run it" not in PAPER
        and "Appendix Tables A18-A19 run it" in PAPER,
    )
    check(
        "appendix discloses the harness-path confound",
        "wording is confounded with harness path and time" in PAPER,
    )


def verify_wording_comparison_tables() -> None:
    """Rebuild the A18-A19 tables from the ``ddca237`` archives and diff them
    against the committed CSVs, then pin the appendix's median-pair prose to
    the same archives. Needs full git history, so this stays in the local
    gate and out of the pytest wrapper (CI clones are shallow).
    """
    import importlib.util
    from statistics import median

    spec = importlib.util.spec_from_file_location(
        "paper_build_tables", REPO_ROOT / "paper" / "build_tables.py"
    )
    build_tables = importlib.util.module_from_spec(spec)
    sys.modules["paper_build_tables"] = build_tables
    try:
        spec.loader.exec_module(build_tables)
        rebuilt_rows, rebuilt_tau = build_tables.build_wording_comparison_tables()
    except Exception as error:  # noqa: BLE001 - report any rebuild failure
        check("wording tables rebuild from the archives", False, str(error))
        return

    check(
        "A18 CSV matches the archive recomputation",
        [{key: str(value) for key, value in row.items()} for row in rebuilt_rows]
        == read_rows("wording-comparison"),
    )
    check(
        "A19 CSV matches the archive recomputation",
        [{key: str(value) for key, value in row.items()} for row in rebuilt_tau]
        == read_rows("wording-comparison-tau"),
    )

    cells: dict[tuple[str, str, str], float] = {}
    for model_name in ("claude-sonnet-4.6", "gemini-3.1-pro-preview"):
        archived = build_tables._read_archived_runs_jsonl(
            build_tables.WORDING_ARCHIVE_COMMIT,
            f"results/{model_name}-elasticities-batch15/runs.jsonl",
        )
        current = build_tables._read_runs_jsonl_records(
            (
                REPO_ROOT / "results" / f"{model_name}-elasticities-batch15" / "runs.jsonl"
            ).read_text()
        )
        for wording, records in (("original", archived), ("revised", current)):
            for quantity_id in (
                build_tables.CAP_GAINS_TAX_RATE_ID,
                build_tables.CAP_GAINS_NET_OF_TAX_RATE_ID,
            ):
                estimates, _ = build_tables._wording_cell(records, quantity_id)
                cells[(model_name, wording, quantity_id)] = median(
                    estimate.point_estimate for estimate in estimates
                )

    tax_id = build_tables.CAP_GAINS_TAX_RATE_ID
    net_id = build_tables.CAP_GAINS_NET_OF_TAX_RATE_ID
    gemini = "gemini-3.1-pro-preview"
    gem_tax_o = cells[(gemini, "original", tax_id)]
    gem_net_o = cells[(gemini, "original", net_id)]
    gem_tax_r = cells[(gemini, "revised", tax_id)]
    gem_net_r = cells[(gemini, "revised", net_id)]
    check(
        "appendix quotes Gemini's median pairs",
        f"$({gem_tax_o:.2f}, {gem_net_o:.2f})$" in PAPER
        and f"$({gem_tax_r:.2f}, {gem_net_r:.1f})$" in PAPER,
        f"pairs ({gem_tax_o}, {gem_net_o}) and ({gem_tax_r}, {gem_net_r})",
    )
    # internal tax rates implied by the identity stated in each wording
    backwards_rate = gem_net_o / (gem_net_o + abs(gem_tax_o))
    corrected_rate = (abs(gem_tax_r) / gem_net_r) / (1 + abs(gem_tax_r) / gem_net_r)
    rho = gem_tax_o / gem_net_o
    plug_in = -rho / (1 - rho)
    check(
        "appendix quotes Gemini's internal rates and the plug-in complement",
        f"near `{backwards_rate:.2f}`" in PAPER
        and f"(`{corrected_rate:.2f}`)" in PAPER
        and f"plug-in `{plug_in:.2f}`" in PAPER,
        f"rates {backwards_rate:.3f}, {corrected_rate:.3f}, plug-in {plug_in:.3f}",
    )

    sonnet = "claude-sonnet-4.6"
    son_net_o = cells[(sonnet, "original", net_id)]
    son_net_r = cells[(sonnet, "revised", net_id)]
    son_rate_o = (abs(cells[(sonnet, "original", tax_id)]) / son_net_o) / (
        1 + abs(cells[(sonnet, "original", tax_id)]) / son_net_o
    )
    son_rate_r = (abs(cells[(sonnet, "revised", tax_id)]) / son_net_r) / (
        1 + abs(cells[(sonnet, "revised", tax_id)]) / son_net_r
    )
    check(
        "appendix quotes Sonnet's sibling medians and corrected-identity rates",
        f"median `{son_net_o:.1f}` to `{son_net_r:.1f}`" in PAPER
        and f"(`{son_rate_o:.2f}` to `{son_rate_r:.2f}`)" in PAPER,
        f"medians {son_net_o}, {son_net_r}; rates {son_rate_o:.3f}, {son_rate_r:.3f}",
    )


PRE_CORRECTION_COMMIT = "22b4ceee3183ebd6aa73c159405c1539e2c0424d"  # origin/main before the d339 correction
QUANTILE_KEYS = ("p05", "p25", "p50", "p75", "p95")


def _correction_note() -> str:
    start = PAPER.find("## Correction (")
    end = PAPER.find("\n## ", start + 1)
    return PAPER[start:end] if start >= 0 else ""


def _git_show(path: str) -> str | None:
    import subprocess

    result = subprocess.run(
        ["git", "-C", str(REPO_ROOT), "show", f"{PRE_CORRECTION_COMMIT}:{path}"],
        capture_output=True,
    )
    return result.stdout.decode("utf-8") if result.returncode == 0 else None


def _build_tables_module():
    import importlib.util

    if "paper_build_tables" in sys.modules:
        return sys.modules["paper_build_tables"]
    spec = importlib.util.spec_from_file_location(
        "paper_build_tables", REPO_ROOT / "paper" / "build_tables.py"
    )
    module = importlib.util.module_from_spec(spec)
    sys.modules["paper_build_tables"] = module
    spec.loader.exec_module(module)
    return module


def _pooled_center(rows: list[dict], skip: int | None = None) -> float:
    from statistics import fmean

    return fmean(
        row["point_estimate"]
        for index, row in enumerate(rows, 1)
        if row.get("parsed_ok") and row.get("run_index", index) != skip
    )


def verify_correction_note() -> None:
    """Recompute most counts and quoted numbers in the dated correction note.

    Covers the run census, the moved and quoted centers, the sample counts, the
    between-run item's scope, the downstream table effects, each open item's
    effects and the ledger's header counts. Most checks match a sentence
    fragment built from recomputed values, so wording outside those fragments
    (some labels and descriptions) is not checked. The run census compares each
    runs.jsonl with the pre-correction commit, so this needs git history and
    stays in the local gate (CI clones are shallow).
    """
    from collections import Counter

    sys.path.insert(0, str(REPO_ROOT))
    from llm_econ_beliefs.model_registry import MODEL_REGISTRY_BY_ID, PANEL_MODEL_IDS

    note = _correction_note()
    check("correction note present", bool(note))
    if not note:
        return
    results = REPO_ROOT / "results"
    kinds: dict[tuple[bool, str], list[tuple[str, str, float | None, float | None]]] = {}
    old_repairs = new_repairs = sign_with_prose_estimate = 0
    for path in sorted(results.glob("*/runs.jsonl")):
        relative = path.relative_to(REPO_ROOT).as_posix()
        old_text = _git_show(relative)
        if old_text is None:
            check("pre-correction runs readable from git", False, relative)
            return
        main_panel = path.parent.name.endswith("-elasticities-batch15")
        new_lines = path.read_bytes().decode("utf-8").split("\n")
        for old_line, new_line in zip(old_text.split("\n"), new_lines):
            if not new_line.strip():
                continue
            new = json.loads(new_line)
            old = json.loads(old_line)
            if main_panel:
                old_repairs += bool(old.get("quantiles_repaired"))
                new_repairs += bool(new.get("quantiles_repaired"))
            if old_line == new_line:
                continue
            old_q, new_q = old.get("quantiles") or {}, new.get("quantiles") or {}
            old_p, new_p = old.get("point_estimate"), new.get("point_estimate")
            if old_q == new_q and old_p == new_p:
                continue  # text fields only
            if old_q == new_q:
                kind = "prose"
            elif any(
                old_q.get(k) is not None and old_q.get(k) == -new_q.get(k, 0) != 0
                for k in QUANTILE_KEYS
            ):
                kind = "sign"
            else:
                kind = "other"
            if main_panel and kind == "sign" and old_p != old_q.get("p50"):
                sign_with_prose_estimate += 1
            kinds.setdefault((main_panel, kind), []).append(
                (new["model_name"], new["quantity_id"], old_p, new_p)
            )
    sign = kinds.get((True, "sign"), [])
    prose = kinds.get((True, "prose"), [])
    changed = sign + prose + kinds.get((True, "other"), [])
    flips = sum(1 for _, _, a, b in changed if a and b and (a < 0) != (b < 0))
    by_model = Counter(model for model, *_ in changed)
    labels = {m: MODEL_REGISTRY_BY_ID[m].display_label for m in by_model}
    singles = sorted(labels[m] for m, n in by_model.items() if n == 1)
    multi = [(labels[m], n) for m, n in by_model.most_common() if n > 1]
    breakdown = ", ".join(f"{n} for `{name}`" for name, n in multi)
    singles_text = ", ".join(f"`{name}`" for name in singles[:-1]) + f", and `{singles[-1]}`"
    check(
        "correction run census",
        f"changes {len(changed)} main-panel runs ({breakdown}, and 1 each for {singles_text})"
        in note
        and f"{len(sign)} had lost a minus sign, {flips} of which change the sign of their point estimate" in note
        and f"({sign_with_prose_estimate} of the {len(sign)} also took their point estimate from "
        f"prose), and {len(prose)} more carried a point estimate read from prose" in note
        and not kinds.get((True, "other")),
        f"got {len(changed)} changed ({dict(by_model)}), sign {len(sign)}, flips {flips}, "
        f"sign with prose estimate {sign_with_prose_estimate}, prose {len(prose)}, other {len(kinds.get((True, 'other'), []))}",
    )
    check(
        "correction quantile-repair counts",
        "Panel-wide quantile repairs, in which each of a run's quantiles is raised to the largest value "
        f"before it, fall from {old_repairs} to {new_repairs}" in note,
        f"got {old_repairs} -> {new_repairs}",
    )
    clarify_prose = kinds.get((False, "prose"), [])
    check(
        "correction clarify-probe prose runs",
        len(clarify_prose) == 2
        and {model for model, *_ in clarify_prose} == {"gemini-3.5-flash"}
        and "changed two `Gemini 3.5 Flash` Armington clarify-probe runs" in note
        and not kinds.get((False, "sign"))
        and not kinds.get((False, "other")),
        f"got {[(m, q) for m, q, *_ in clarify_prose]}",
    )

    # Centers: which moved, through which defect, and the ones the note quotes.
    sign_cells = {(m, q) for m, q, *_ in sign}
    moved: list[tuple[str, str, float, float]] = []
    for path in sorted(results.glob("*-elasticities-batch15/summary.csv")):
        old_text = _git_show(path.relative_to(REPO_ROOT).as_posix()) or ""
        old_rows = {
            (r["model_name"], r["quantity_id"]): r
            for r in csv.DictReader(old_text.splitlines())
        }
        with path.open() as handle:
            for row in csv.DictReader(handle):
                old = old_rows[(row["model_name"], row["quantity_id"])]
                a, b = float(old["pooled_point_estimate"]), float(row["pooled_point_estimate"])
                if a != b:
                    moved.append((row["model_name"], row["quantity_id"], a, b))
    through_sign = [c for c in moved if (c[0], c[1]) in sign_cells]
    k3 = next(
        (c for c in moved if c[0] == "kimi-k3" and c[1].endswith("net_of_tax_rate")), None
    )
    rest = [c for c in moved if (c[0], c[1]) not in sign_cells and c is not k3]
    largest_rest = max(abs(b - a) for _, _, a, b in rest)
    cell_kinds: dict[tuple[str, str], set[str]] = {}
    for (is_main, kind), rows in kinds.items():
        if is_main:
            for model, quantity, *_ in rows:
                cell_kinds.setdefault((model, quantity), set()).add(kind)
    prose_only = all(
        cell_kinds.get((m, q)) == {"prose"} for m, q, *_ in ([k3] if k3 else []) + rest
    )
    check(
        "correction moved-center counts",
        f"{len(moved)} main-panel centers move, {len(through_sign)} of them through a lost sign"
        in note
        and k3 is not None
        and prose_only
        and f"The prose defect moves `{MODEL_REGISTRY_BY_ID['kimi-k3'].display_label}`'s "
        f"net-of-tax-rate capital-gains center from `{k3[2]:.3f}` to `{k3[3]:.3f}` and "
        f"{len(rest)} other centers, the largest by `{largest_rest:.3f}`" in note,
        f"got {len(moved)} moved, {len(through_sign)} via sign, K3 {k3}, prose only {prose_only}, "
        f"{len(rest)} others max {largest_rest:.4f}",
    )
    quoted = {
        ("gemini-3.5-flash", "tax.capital_gains_realizations.elasticity"): "`{b:.2f}` for capital gains",
        ("gemini-3.5-flash", "labor_supply.income_elasticity.prime_age"): "`{b:.3f}` for the income elasticity",
        ("inkling", "tax.capital_gains_realizations.elasticity"): "`Inkling` from `{a:.3f}` to `{b:.3f}`",
        ("kimi-k2.6", "tax.capital_gains_realizations.elasticity"): "`Kimi K2.6` from `{a:.3f}` to `{b:.3f}`",
        ("gemini-3.5-flash", "labor_supply.marshallian_wage_elasticity.prime_age"): (
            "`Gemini 3.5 Flash`'s Marshallian wage elasticity, from `{a:.3f}` to `{b:.3f}`"
        ),
    }
    centers = {(m, q): (a, b) for m, q, a, b in moved}
    for cell, template in quoted.items():
        a, b = centers.get(cell, (float("nan"), float("nan")))
        check(f"correction quotes {cell[0]} {cell[1].split('.')[1]}", template.format(a=a, b=b) in note, f"got {a} -> {b}")
    check(
        "correction names every center moved through a lost sign",
        {(m, q) for m, q, *_ in through_sign} == set(quoted)
        and "Two other capital-gains centers move through a lost sign" in note,
        f"got {sorted((m, q) for m, q, *_ in through_sign)}",
    )
    gem_cg = centers.get(("gemini-3.5-flash", "tax.capital_gains_realizations.elasticity"), (0, 0))
    gem_inc = centers.get(("gemini-3.5-flash", "labor_supply.income_elasticity.prime_age"), (0, 0))
    check(
        "correction quotes Gemini 3.5 Flash's published centers",
        f"(published: `{gem_cg[0]:+.3f}` and `{gem_inc[0]:+.3f}`)" in note,
        f"got {gem_cg[0]}, {gem_inc[0]}",
    )
    sign_sensitive = [
        row["point_estimate"]
        for row in (
            json.loads(line)
            for line in (results / "gemini-3.5-flash-elasticities-batch15" / "runs.jsonl")
            .read_text()
            .splitlines()
            if line.strip()
        )
        if row["quantity_id"]
        in ("tax.capital_gains_realizations.elasticity", "labor_supply.income_elasticity.prime_age")
    ]
    check(
        "Gemini 3.5 Flash sign-sensitive runs all negative",
        len(sign_sensitive) == 30
        and all(value < 0 for value in sign_sensitive)
        and "The Gemini 3.5 Flash bimodality finding is withdrawn: all "
        f"{len(sign_sensitive)} of its runs on the two sign-sensitive quantities are negative" in note,
        f"got {len(sign_sensitive)} runs, {sum(v < 0 for v in sign_sensitive)} negative",
    )

    # Clarify-probe center in Table A7, before and after.
    old_clarify = [
        json.loads(line)
        for line in (_git_show("results/gemini-3.5-flash-armington-clarify-batch15/runs.jsonl") or "").splitlines()
        if line.strip()
    ]
    new_clarify = [
        json.loads(line)
        for line in (results / "gemini-3.5-flash-armington-clarify-batch15" / "runs.jsonl").read_text().splitlines()
        if line.strip()
    ]
    check(
        "correction A7 clarified center",
        "moving that model's clarified center in Appendix Table A7 from "
        f"`{_pooled_center(old_clarify):.3f}` to `{_pooled_center(new_clarify):.3f}`" in note,
    )

    # Table 7 contrasts before and after.
    def country_p(text: str, outcome: str) -> float:
        return float(next(r for r in csv.DictReader(text.splitlines()) if r["outcome"] == outcome)["permutation_p"])

    old_country = _git_show("results/correlates-country.csv") or ""
    new_country = (results / "correlates-country.csv").read_text()
    width, center = "Avg interval-width rank (1 = tightest)", "Mean |center|, labor-and-tax"
    check(
        "correction Table 7 p-values",
        "the US-lab versus Chinese-lab width and center contrasts in Table 7 move "
        f"from raw $p = {country_p(old_country, width):.3f}$ and ${country_p(old_country, center):.3f}$ "
        f"to ${country_p(new_country, width):.3f}$ and ${country_p(new_country, center):.3f}$"
        in note,
    )

    # Between-run variance: what the fix moved, and what it left alone.
    parser_cells = {
        (is_main, model, quantity)
        for (is_main, _), rows in kinds.items()
        for model, quantity, *_ in rows
    }
    stale_dirs = {
        key.split("/")[1]
        for key in json.loads((REPO_ROOT / "tests" / "fixtures" / "stale_cached_rows.json").read_text())
    }

    def summary_moves(pattern: str, is_main: bool):
        centers_moved, bounds_moved, between_moved, bound_steps = [], [], [], {}
        for path in sorted(results.glob(pattern)):
            old_rows = {
                r["quantity_id"]: r
                for r in csv.DictReader((_git_show(path.relative_to(REPO_ROOT).as_posix()) or "").splitlines())
            }
            with path.open() as handle:
                for row in csv.DictReader(handle):
                    old = old_rows[row["quantity_id"]]
                    cell = (is_main, row["model_name"], row["quantity_id"], path.parent.name)
                    differs = lambda col: abs(float(old[col]) - float(row[col])) > 1e-12  # noqa: E731
                    if differs("pooled_point_estimate"):
                        centers_moved.append(cell)
                    if differs("pooled_lower_bound") or differs("pooled_upper_bound"):
                        bounds_moved.append(cell)
                        bound_steps[cell] = max(
                            abs(float(old[c]) - float(row[c]))
                            for c in ("pooled_lower_bound", "pooled_upper_bound")
                        )
                    if differs("between_run_sd"):
                        between_moved.append(cell)
        return centers_moved, bounds_moved, between_moved, bound_steps

    main_c, main_b, main_between, _ = summary_moves("*-elasticities-batch15/summary.csv", True)
    clar_c, clar_b, _, clar_steps = summary_moves("*-clarify-batch15/summary.csv", False)
    in_parser = lambda cell: cell[:3] in parser_cells  # noqa: E731
    fallback_moves = [cell for cell in clar_b if not in_parser(cell)]
    old_a18 = list(csv.DictReader((_git_show("paper/tables/wording-comparison.csv") or "").splitlines()))
    new_a18 = read_rows("wording-comparison")
    a18_changes = [
        (index, column)
        for index, (old, new) in enumerate(zip(old_a18, new_a18))
        for column in new
        if old.get(column) != new[column]
    ]
    check(
        "correction between-run variance scope",
        all(in_parser(cell) for cell in main_c + main_b + clar_c)
        and sum(1 for cell in main_between if not in_parser(cell)) > 100
        and all(cell[3] in stale_dirs for cell in fallback_moves)
        and 0 < len(fallback_moves) <= 5
        and max(clar_steps[cell] for cell in fallback_moves) < 0.05
        and len(old_a18) == len(new_a18)
        and len(a18_changes) == 1
        and "width" in a18_changes[0][1]
        and "used the variance of run medians in place of the variance of run means. Both now use "
        "run means. The reported center, the mean of run medians, is unchanged, and the headline "
        "pooled intervals do not depend on this term." in note
        and "a few clarify-probe intervals in Appendix Tables A7 and A8 move slightly, as does one "
        "interval in Appendix Table A18." in note,
        f"main centers {len(main_c)}, bounds {len(main_b)}, between {len(main_between)}; clarify "
        f"fallback moves {[(c[3], round(clar_steps[c], 4)) for c in fallback_moves]}; A18 {a18_changes}",
    )

    cap_gains_row = next(
        r for r in read_rows("benchmark-comparison-labor-tax")
        if r["Quantity"] == "Capital gains realizations elasticity"
    )
    in_band, total_models = cap_gains_row["Models in range"].split(" / ")
    check(
        "correction Table 3 capital-gains band count",
        f"inside the review band for {in_band} of {total_models} models (Table 3)" in note,
        f"Table 3 says {cap_gains_row['Models in range']}",
    )

    def a9_band(text: str) -> str:
        row = next(r for r in csv.DictReader(text.splitlines()) if r["Model"] == "Gemini 3.5 Flash")
        return list(row.values())[-1]

    old_band = a9_band(_git_show("paper/tables/cap-gains-convention-audit.csv") or "Model\nGemini 3.5 Flash")
    new_band = a9_band((TABLES / "cap-gains-convention-audit.csv").read_text())
    check(
        "correction A9 band for Gemini 3.5 Flash",
        old_band.startswith("uninformative")
        and new_band.endswith("consistent")
        and "Gemini 3.5 Flash's implied-tau row in Appendix Table A9 receives a band" in note,
        f"band {old_band!r} -> {new_band!r}",
    )

    # Sample counts, open items and the changed-numbers ledger.
    main_rows = [
        json.loads(line)
        for path in sorted(results.glob("*-elasticities-batch15/runs.jsonl"))
        for line in path.read_text().splitlines()
        if line.strip()
    ]
    quantities = len({row["quantity_id"] for row in main_rows})
    n_models = len(PANEL_MODEL_IDS)
    n_runs = sum(1 for row in main_rows if row.get("parsed_ok"))
    cell_sizes = Counter((row["model_name"], row["quantity_id"]) for row in main_rows if row.get("parsed_ok"))
    old_paper = _git_show("paper/paper.qmd") or ""
    old_data = old_paper[old_paper.find("## Data"):]
    old_count = re.search(r"\n- ([\d,]+) successful main-panel runs", old_data)
    check(
        "correction sample counts",
        n_runs == n_models * quantities * 15
        and old_count is not None
        and int(old_count[1].replace(",", "")) == 29 * quantities * 15
        and f"contains {n_runs:,} successful runs across {n_models} models" in old_paper
        and f"The Data section stated {old_count[1]} successful main-panel runs, the count for the "
        f"29-model panel (29 × {quantities} × 15)" in note
        and f"The {n_models}-model panel holds {n_runs:,} ({n_models} × {quantities} × 15), "
        "as the abstract already stated" in note
        and f"contains {n_runs:,} successful runs across {n_models} models" in PAPER
        and f"\n- {n_runs:,} successful main-panel runs, every one accepted as parsed at collection"
        in PAPER
        and set(cell_sizes.values()) == {15}
        and f"every cell holds exactly {next(iter(set(cell_sizes.values())))} parsed runs" in PAPER
        and f"Every model-quantity cell holds {next(iter(set(cell_sizes.values())))} runs that were accepted"
        in PAPER
        and f"\n- {n_models} models from ten organizations" in PAPER
        and f"\n- {quantities} quantities (" in PAPER
        and "\n- 15 runs per model-quantity cell" in PAPER,
        f"got {n_runs} runs, {n_models} models, {quantities} quantities, old {old_count and old_count[1]}",
    )
    stale = json.loads((REPO_ROOT / "tests" / "fixtures" / "stale_cached_rows.json").read_text())
    main_stale = [key for key in stale if "-elasticities-batch15/" in key]
    check(
        "correction open-item row counts",
        len(stale) == 9 and len(main_stale) == 1
        and "Nine retained rows do not reparse" in note
        and "One is a main-panel run" in note
        and "machine-parseable" not in PAPER
        and "A run counts as successful if the parser in use at collection accepted its output as an "
        "estimate; failed runs stay missing and drop out of the pooled summaries. The correction note "
        "lists the retained runs that the corrected parser would reject." in PAPER
        and "The other eight are clarify-probe rows" in note
        and f"the other {len(PANEL_MODEL_IDS) * quantities * 15 - len(main_stale):,} main-panel runs reparse "
        "to their stored values" in note,
        f"got {len(stale)} stale rows, {len(main_stale)} main-panel",
    )

    def cell_rows(directory: str, quantity: str | None = None) -> list[dict]:
        rows = [
            json.loads(line)
            for line in (results / directory / "runs.jsonl").read_text().splitlines()
            if line.strip()
        ]
        return [r for r in rows if quantity is None or r["quantity_id"] == quantity]

    ies = cell_rows("gemini-3.5-flash-elasticities-batch15", "household.intertemporal_elasticity_of_substitution")
    inkling = cell_rows("inkling-armington-clarify-batch15")
    pro_ies = cell_rows("gemini-3.1-pro-preview-ies-clarify-batch15")
    check(
        "correction open-item effects",
        f"Dropping it would move that cell's center from `{_pooled_center(ies):.3f}` to "
        f"`{_pooled_center(ies, skip=2):.3f}`" in note
        and f"`Inkling`'s clarified center in Appendix Table A7 from `{_pooled_center(inkling):.3f}` to "
        f"`{_pooled_center(inkling, skip=13):.3f}`" in note
        and "`Gemini 3.1 Pro`'s clarified IES center in Appendix Table A8, which " + f"rests on {sum(1 for r in pro_ies if r.get('parsed_ok'))} parsed runs, from "
        f"`{_pooled_center(pro_ies):.3f}` to `{_pooled_center(pro_ies, skip=15):.3f}`".replace("rests on 4", "rests on four")
        in note
        and "point_estimate" not in next(r for r in inkling if r["run_index"] == 13)["raw_response"]
        and "point_estimate" not in next(r for r in pro_ies if r["run_index"] == 15)["raw_response"],
    )
    open_items = note[note.find("**Open items.**"):]
    bullets = [line for line in open_items.splitlines() if line.startswith("- *")]
    check(
        "correction open-item count",
        len(bullets) == 3
        and "flags three open items" in note
        and "Three groups of retained answers" in note,
        f"got {len(bullets)} bullets",
    )
    check(
        "Data section reparse count",
        f"under the corrected parser {len(PANEL_MODEL_IDS) * quantities * 15 - len(main_stale):,} reparse"
        in PAPER,
    )

    def stale_row(key: str) -> dict:
        path, line = key.rsplit(":", 1)
        return json.loads((REPO_ROOT / path).read_text().splitlines()[int(line) - 1])

    main_row = stale_row(main_stale[0]) if main_stale else {}
    check(
        "correction describes the main-panel stale row",
        main_row.get("model_name") == "gemini-3.5-flash"
        and main_row.get("quantity_id") == "household.intertemporal_elasticity_of_substitution"
        and main_row.get("run_index") == 2
        and [main_row["quantiles"][k] for k in QUANTILE_KEYS] == [0, 0, 1, 1, 2]
        and all(
            f'"{key}": {value}' in main_row["raw_response"]
            for key, value in zip(QUANTILE_KEYS, ("0 .1", "0 .5", "1 .0"))
        )
        and "`Gemini 3.5 Flash` on the intertemporal elasticity of substitution (run 2)" in note
        and 'which wrote its numbers with spaces inside them ("0 .1", "0 .5", "1 .0") and is stored '
        "with quantiles `[0, 0, 1, 1, 2]`" in note,
        f"got {main_stale} {main_row.get('run_index')} {main_row.get('quantiles')}",
    )
    clarify_stale = {key: stale_row(key) for key in stale if key not in main_stale}
    clarify_labels = sorted({MODEL_REGISTRY_BY_ID[r["model_name"]].display_label for r in clarify_stale.values()})
    no_estimate = sorted(
        (key.split("/")[1], row["run_index"])
        for key, row in clarify_stale.items()
        if "point_estimate" not in row["raw_response"]
    )
    check(
        "correction names the clarify rows without a point estimate",
        "clarify-probe rows (" + ", ".join(f"`{label}`" for label in clarify_labels) + ")" in note
        and no_estimate
        == [("gemini-3.1-pro-preview-ies-clarify-batch15", 15), ("inkling-armington-clarify-batch15", 13)]
        and "Two of them state no point estimate at all" in note
        and "`Inkling`'s Armington run 13 and `Gemini 3.1 Pro`'s IES run 15" in note,
        f"got {clarify_labels}, {no_estimate}",
    )
    truncated_key = "results/gemini-3.1-pro-preview-armington-clarify-batch15/runs.jsonl:12"
    truncated = clarify_stale.get(truncated_key, {})
    pro_armington = cell_rows("gemini-3.1-pro-preview-armington-clarify-batch15")
    check(
        "correction describes the truncated Armington run",
        truncated.get("run_index") == 12
        and truncated["raw_response"].rstrip().endswith('"point_estimate": 1.')
        and truncated["point_estimate"] == 1.0
        and "A third, `Gemini 3.1 Pro`'s Armington run 12, is cut off at `\"point_estimate\": 1.` and stored as `1.0`"
        in note
        and f"`Gemini 3.1 Pro`'s from `{_pooled_center(pro_armington):.3f}` to "
        f"`{_pooled_center(pro_armington, skip=12):.3f}`" in note,
    )

    words = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 7: "Seven", 8: "eight"}
    fallback_dirs = {key.split("/")[1] for key in clarify_stale}
    clarify_lower = {}
    for path in sorted(results.glob("*-clarify-batch15/summary.csv")):
        with path.open() as handle:
            for row in csv.DictReader(handle):
                clarify_lower[path.parent.name] = float(row["pooled_lower_bound"])

    def cell_labels(kind: str) -> str:
        labels = sorted(
            MODEL_REGISTRY_BY_ID[d.split(f"-{kind}-clarify")[0]].display_label
            for d in fallback_dirs
            if f"-{kind}-clarify" in d
        )
        names = [f"`{label}`" for label in labels]
        return names[0] if len(names) == 1 else (
            " and ".join(names) if len(names) == 2 else ", ".join(names[:-1]) + f", and {names[-1]}"
        )

    check(
        "correction describes the clarify fallback cells",
        all(set(row.get("quantiles") or {}) != set(QUANTILE_KEYS) for row in clarify_stale.values())
        and all(clarify_lower[d] == 0.0 for d in fallback_dirs)
        and all(value > 0 for d, value in clarify_lower.items() if d not in fallback_dirs)
        and "Dropping those three rows would move" in note
        and f"Because all {words.get(len(clarify_stale), len(clarify_stale))} clarify-probe rows lack "
        f"full quantiles, the {words.get(len(fallback_dirs), len(fallback_dirs))} clarify cells that "
        f"hold them (the Armington cells of {cell_labels('armington')}, and the IES cells of "
        f"{cell_labels('ies')}) use the normal approximation described above, and their lower ends in "
        "Appendix Tables A7 and A8 sit at the support floor of `0`; no other clarify cell does." in note,
        f"fallback cells {sorted(fallback_dirs)}",
    )

    # Descending quantiles: the repair keeps the stated p05 as the point estimate.
    from collections import defaultdict
    from statistics import fmean, median

    stated_number = r"\s*:\s*(-?[\d.]+)"
    repaired: dict[tuple[str, str], list[tuple[float, float]]] = defaultdict(list)
    shapes_ok, example_seen = True, False
    for path in sorted(results.glob("*-elasticities-batch15/runs.jsonl")):
        for row in (json.loads(line) for line in path.read_text().splitlines() if line.strip()):
            if not row.get("quantiles_repaired"):
                continue
            raw = row["raw_response"]
            stated = [float(re.search(f'"{key}"' + stated_number, raw)[1]) for key in QUANTILE_KEYS]
            stated_estimate = float(re.search('"point_estimate"' + stated_number, raw)[1])
            shapes_ok &= (
                stated == sorted(stated, reverse=True) != sorted(stated)
                and row["point_estimate"] == stated[0]
                and stated_estimate == stated[2]
            )
            example_seen |= stated == [-0.1, -0.4, -0.7, -1.0, -1.5] and stated_estimate == -0.7
            repaired[(row["model_name"], row["quantity_id"])].append((row["point_estimate"], stated[2]))
    per_model = Counter()
    for (model, _), runs in repaired.items():
        per_model[model] += len(runs)
    model_text = ", ".join(
        f"{words[n]} `{MODEL_REGISTRY_BY_ID[m].display_label}`" for m, n in per_model.most_common()
    )
    check(
        "correction descending-quantile rows",
        sum(per_model.values()) == new_repairs
        and shapes_ok
        and example_seen
        and f"{words.get(new_repairs)} main-panel runs ({model_text}) list their quantiles in descending order"
        in note
        and "`-0.1, -0.4, -0.7, -1.0, -1.5` with a stated point estimate of `-0.7`" in note
        and "collapses each run to its first value, so the stored point estimate is the stated p05 rather "
        "than the stated median. Using the stated medians would move" in note,
        f"got {dict(per_model)}, shapes ok {shapes_ok}, example {example_seen}",
    )
    band_low, band_high = (
        float(x) for x in cap_gains_row["Rough review range"].strip("[]").split(",")
    )
    cap_gains_id = "tax.capital_gains_realizations.elasticity"
    effects_ok = True
    for (model, quantity), runs in repaired.items():
        cell = cell_rows(f"{model}-elasticities-batch15", quantity)
        stored_center = fmean(r["point_estimate"] for r in cell)
        stated_center = (
            stored_center * len(cell) - sum(a for a, _ in runs) + sum(b for _, b in runs)
        ) / len(cell)
        with (results / f"{model}-elasticities-batch15" / "summary.csv").open() as handle:
            published = next(
                float(r["pooled_point_estimate"]) for r in csv.DictReader(handle) if r["quantity_id"] == quantity
            )
        label = MODEL_REGISTRY_BY_ID[model].display_label
        if quantity == cap_gains_id:
            text = f"`{label}` from `{stored_center:.3f}` to `{stated_center:.3f}`"
            effects_ok &= band_low <= stated_center <= band_high
        else:
            text = f"`{label}`'s income-elasticity center from `{stored_center:.3f}` to `{stated_center:.3f}`"
            effects_ok &= quantity == "labor_supply.income_elasticity.prime_age"
        effects_ok &= text in note and abs(published - stored_center) < 1e-9
    check(
        "correction descending-quantile effects",
        effects_ok
        and sum(1 for _, q in repaired if q == cap_gains_id) == 3
        and "All three capital-gains centers stay inside the Table 3 band" in note,
        f"cells {sorted(repaired)}",
    )

    # The same runs read at their stated medians, through the Table A9 bootstrap.
    tables = _build_tables_module()
    a9_rows = {r["Model"]: r for r in read_rows("cap-gains-convention-audit")}
    band_column = list(next(iter(a9_rows.values())))[-1]
    a9_counts = Counter(r[band_column] for r in a9_rows.values())
    ordinary, ltcg = "ordinary-income-rate consistent", "LTCG-rate consistent"
    a9_ok, a9_detail, moved_counts = True, [], Counter(a9_counts)
    for model in sorted({m for m, q in repaired if q == cap_gains_id}):
        directory = f"{model}-elasticities-batch15"
        tax_points, net_points = tables._load_cap_gains_run_points(f"results/{directory}")
        stated_tax = []
        for row in cell_rows(directory, cap_gains_id):
            if not row.get("parsed_ok") or row.get("point_estimate") is None:
                continue
            value = float(row["point_estimate"])
            if row.get("quantiles_repaired"):
                value = float(re.search('"p50"' + stated_number, row["raw_response"])[1])
            stated_tax.append(value)
        old = tables._bootstrap_implied_tau_quantiles(tax_points, net_points)
        new = tables._bootstrap_implied_tau_quantiles(stated_tax, net_points)
        old_band = tables._implied_tau_band_flag(old[1], old[3])
        new_band = tables._implied_tau_band_flag(new[1], new[3])
        pairs = [
            -(x / y) / (1 - x / y) for x in stated_tax for y in net_points if y != 0 and x / y != 1
        ]
        pair_median = median(pairs)
        pair_band = tables._implied_tau_band_flag(pair_median, sum(0 < v < 1 for v in pairs) / len(pairs))
        label = MODEL_REGISTRY_BY_ID[model].display_label
        a9_ok &= a9_rows[label]["Implied tau median [90%]"] == f"{old[1]:.3f} [{old[0]:.3f}, {old[2]:.3f}]"
        a9_ok &= a9_rows[label][band_column] == old_band
        a9_detail.append((label, round(old[1], 3), round(new[1], 3), new_band, round(pair_median, 4), pair_band))
        if new_band == old_band:
            continue
        moved_counts[old_band] -= 1
        moved_counts[new_band] += 1
        if (old_band, new_band) != (ltcg, ordinary):
            a9_ok = False
        elif pair_band == new_band:
            a9_ok &= (
                f"`{label}`'s implied tau from `{old[1]:.3f}` to `{new[1]:.3f}`, from the LTCG window "
                "into the ordinary-income window" in note
            )
        else:
            a9_ok &= pair_band == old_band and (
                f"`{label}`'s from `{old[1]:.3f}` to `{new[1]:.3f}`, though over all {len(pairs)} run "
                f"pairs its median is `{pair_median:.3f}`, inside the LTCG window" in note
            )
    check(
        "correction descending-quantile A9 effects",
        a9_ok
        and sum(1 for d in a9_detail if d[3] != a9_rows[d[0]][band_column]) == 2
        and f"Table A9 would hold {moved_counts[ordinary]} ordinary-income-window rows and "
        f"{moved_counts[ltcg]} LTCG-window rows rather than {a9_counts[ordinary]} and {a9_counts[ltcg]}"
        in note,
        f"got {a9_detail}, counts {dict(a9_counts)} -> {dict(moved_counts)}",
    )

    # April 19 archive behind Tables A18 and A19, reparsed.
    from llm_econ_beliefs import parse_belief_response

    build_tables = _build_tables_module()
    tax_id = build_tables.CAP_GAINS_TAX_RATE_ID
    net_id = build_tables.CAP_GAINS_NET_OF_TAX_RATE_ID
    archive: dict[tuple[str, str], tuple[list[float], list[float], int, int]] = {}
    for model in build_tables.DUAL_WORDING_MODELS:
        rows = build_tables._read_archived_runs_jsonl(
            build_tables.WORDING_ARCHIVE_COMMIT, f"results/{model}-elasticities-batch15/runs.jsonl"
        )
        for quantity in build_tables.SIGN_CLARIFIED_QUANTITY_IDS:
            stored_values, reparsed_values, changed_runs, rejected_runs = [], [], 0, 0
            for row in rows:
                if row["quantity_id"] != quantity or not row.get("parsed_ok"):
                    continue
                stored_values.append(row["point_estimate"])
                try:
                    estimate = parse_belief_response(row["raw_response"], quantity_id=quantity)
                except ValueError:
                    rejected_runs += 1
                    continue
                reparsed_values.append(estimate.point_estimate)
                changed_runs += (
                    estimate.point_estimate != row["point_estimate"]
                    or estimate.quantiles != row["quantiles"]
                )
            archive[(model, quantity)] = (stored_values, reparsed_values, changed_runs, rejected_runs)
    gemini_pro = "gemini-3.1-pro-preview"
    moved_cells = {cell: (c, r) for cell, (_, _, c, r) in archive.items() if c or r}
    stored_net, reparsed_net, _, _ = archive[(gemini_pro, net_id)]
    stored_tax = archive[(gemini_pro, tax_id)][0]
    check(
        "correction April 19 reparse counts",
        moved_cells == {(gemini_pro, net_id): (3, 5)}
        and len(stored_net) == 15
        and "changes 3 and rejects 5 of the 15 `Gemini 3.1 Pro` net-of-tax-rate runs there; "
        f"the other {len(archive) - 1} sign-clarified April 19 cells reparse unchanged" in note,
        f"got {moved_cells}, {len(archive)} cells",
    )
    a18 = next(
        r for r in read_rows("wording-comparison")
        if r["Model"] == "Gemini 3.1 Pro" and "net-of-tax" in r["Quantity"]
    )
    revised_center = float(a18["Revised center"])
    tax_median = median(stored_tax)
    check(
        "correction April 19 A18 effects",
        f"{fmean(stored_net):.3f}" == a18["Original center"]
        and f"parse {len(reparsed_net)} of {len(stored_net)} runs rather than all {len(stored_net)}" in note
        and f"$({tax_median:.2f}, {median(reparsed_net):.3f})$ rather than "
        f"$({tax_median:.2f}, {median(stored_net):.2f})$" in note
        and f"its Table A18 center would move from `{fmean(stored_net):.3f}` to `{fmean(reparsed_net):.3f}`, shrinking its wording change "
        f"from `{float(a18['Center change']):+.2f}` to `{revised_center - fmean(reparsed_net):+.2f}`" in note,
        f"centers {fmean(stored_net):.4f} -> {fmean(reparsed_net):.4f}",
    )
    a19 = next(r for r in read_rows("wording-comparison-tau") if r["Model"] == "Gemini 3.1 Pro")
    old_tau = build_tables._bootstrap_implied_tau_quantiles(stored_tax, stored_net)
    new_tau = build_tables._bootstrap_implied_tau_quantiles(stored_tax, reparsed_net)
    old_flag = build_tables._implied_tau_band_flag(old_tau[1], old_tau[3])
    new_flag = build_tables._implied_tau_band_flag(new_tau[1], new_tau[3])
    rho = tax_median / median(reparsed_net)
    check(
        "correction April 19 A19 effects",
        f"{old_tau[1]:.3f} [{old_tau[0]:.3f}, {old_tau[2]:.3f}]" == a19["Original implied tau median [90%]"]
        and old_flag == a19["Original band"]
        and new_flag == "plausible sign, outside bands"
        and f"Its Table A19 implied tau would move from `{old_tau[1]:.3f}` [{old_tau[0]:.3f}, "
        f"{old_tau[2]:.3f}], {old_flag}, to "
        f"`{new_tau[1]:.3f}` [{new_tau[0]:.3f}, {new_tau[2]:.3f}], a plausible sign outside both bands, "
        f"against a reparsed plug-in of `{-rho / (1 - rho):.2f}`" in note,
        f"tau {old_tau} {old_flag} -> {new_tau} {new_flag}",
    )

    ledger = (REPO_ROOT / "paper" / "corrections" / "2026-09-25-changed-numbers.md").read_text()
    match = re.search(r"(\d+) cells changed across (\d+) CSV files; (\d+) Markdown tables", ledger)
    check(
        "correction ledger counts",
        match is not None
        and f"({int(match[1]):,} cells across {match[2]} CSV files, plus line diffs for {match[3]} Markdown tables)"
        in note,
        f"ledger says {match.groups() if match else None}",
    )


def main() -> int:
    verify_correction_note()
    verify_superlatives()
    verify_top_rate()
    verify_stability()
    verify_loo()
    verify_variance_decomposition()
    verify_ablation()
    verify_harness_disclosure()
    verify_resampling_range()
    verify_rank_spread_tie()
    verify_correlates()
    verify_cap_gains_audit()
    verify_top_rate_robustness()
    verify_benchmark_counts()
    verify_eti_outliers()
    verify_quantile_rule()
    verify_armington_delta()
    verify_variance_median_range()
    verify_resampling_panel_median()
    verify_policybench_release_pin()
    verify_posthoc_consistency()
    verify_country_family()
    verify_income_sign_counts()
    verify_prompt_identity()
    verify_wording_comparison_prose()
    verify_wording_comparison_tables()
    if FAILURES:
        print(f"\n{len(FAILURES)} check(s) failed")
        return 1
    print("\nall prose checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
