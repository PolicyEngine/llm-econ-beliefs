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
        for row in rows:
            label = row[model_col].strip("`").lower().replace(" ", "-")
            if label == model_id:
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
    claim = (
        f"$\\rho = {float(overall['spearman_rho']):.2f}$"
        f" and ${float(tax['spearman_rho']):.2f}$"
    )
    check(
        "capability rho per predictor in prose",
        len(eti_rows) == 2
        and claim in PAPER
        and "$\\rho \\approx -0.5$" in PAPER
        and all(r["n_models"] == "22" for r in eti_rows.values())
        and all(0.015 <= float(r["raw_p"]) < 0.025 for r in eti_rows.values()),
        f"expected {claim!r}; got "
        f"{[(r['spearman_rho'], r['raw_p'], r['n_models']) for r in eti_rows.values()]}",
    )
    min_holm = min(float(r["holm_adjusted_p"]) for r in spearman)
    min_bh = min(float(r["bh_adjusted_p"]) for r in spearman)
    check(
        "Holm and BH minima in prose",
        f"`{min_holm:.3f}`" in PAPER and f"`{min_bh:.3f}`" in PAPER,
        f"expected {min_holm:.3f} and {min_bh:.3f}",
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
        len(loo) == 9
        and f"between `{max(loo):.2f}` and `{min(loo):.2f}`" in PAPER,
        f"expected between {max(loo):.2f} and {min(loo):.2f} over {len(loo)}",
    )

    with (results / "correlates-country.csv").open() as handle:
        country = {r["outcome"]: r for r in csv.DictReader(handle)}
    tau = country["Implied optimal top rate (%)"]
    eti = country["ETI pooled median"]
    width = country["Avg interval-width rank (1 = tightest)"]
    check(
        "country top-rate medians and p",
        f"`{float(tau['china_median']):.1f}%` versus `{float(tau['us_median']):.1f}%`" in PAPER
        and f"$p = {float(tau['permutation_p']):.3f}$" in PAPER
        and tau["us_n"] == "20"
        and tau["china_n"] == "5",
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
    check(
        "country rows disclose the confound",
        all("confounded" in r["disclosure"] for r in country.values()),
    )


NUMBER_WORDS = {
    3: "three",
    8: "eight",
    15: "fifteen",
    23: "twenty-three",
    24: "twenty-four",
    25: "twenty-five",
}


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

    check(
        "Frisch in-range count",
        count_for("frisch") == "25/25"
        and "Every one of the 25 models falls inside the rough benchmark range for the Frisch"
        in PAPER,
        f"got {count_for('frisch')}",
    )
    trio = {count_for("capital gains"), count_for("wage"), count_for("single mother")}
    check(
        "capital-gains/wage/single-mother in-range counts",
        trio == {"24/25"} and "`24 / 25` lie inside for capital gains realizations" in PAPER,
        f"got {trio}",
    )
    check(
        "income-elasticity in-range count",
        count_for("income elasticity") == "21/25"
        and "`21 / 25` for the canonical income elasticity" in PAPER,
        f"got {count_for('income elasticity')}",
    )
    check(
        "ETI in-range count",
        count_for("taxable income") == "22/25" and "`22 / 25` models fall inside" in PAPER,
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
    check(
        "ETI out-of-band models all named with centers",
        len(records) == 25
        and named
        and f"{NUMBER_WORDS[len(over)]} models just above" in sentence,
        f"expected {sorted(over)}",
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
    check(
        "US organization count in prose",
        len(us_organizations) == 4
        and "twenty models from four US organizations" in PAPER,
        f"got {sorted(us_organizations)}",
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
    verify_country_family()
    verify_income_sign_counts()
    if FAILURES:
        print(f"\n{len(FAILURES)} check(s) failed")
        return 1
    print("\nall prose checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
