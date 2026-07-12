import math

import pytest

from scripts.build_correlates import (
    kruskal_wallis,
    parse_estimate_interval_cell,
    parse_interval_cell,
    parse_percentage_cell,
    parse_percentage_interval_cell,
    permutation_p,
    spearman,
)


def test_kruskal_wallis_matches_known_tie_corrected_values() -> None:
    # Independently checked against R's stats::kruskal.test.
    groups = [[1, 2, 2, 3], [2, 3, 4], [1, 1, 2, 4]]

    h, p = kruskal_wallis(groups)

    assert h == pytest.approx(1.9260620915032711, abs=1e-12)
    assert p == pytest.approx(0.3817340772081283, abs=1e-12)


@pytest.mark.parametrize(
    ("xs", "ys"),
    [
        ([1.0, 2.0, 3.0], [1.0, 2.0]),
        ([1.0, 2.0], [1.0, 2.0]),
        ([1.0, math.nan, 3.0], [1.0, 2.0, 3.0]),
        ([1.0, 2.0, 3.0], [1.0, math.inf, 3.0]),
        ([1.0, 1.0, 1.0], [1.0, 2.0, 3.0]),
        ([1.0, 2.0, 3.0], [1.0, 1.0, 1.0]),
    ],
)
def test_degenerate_correlations_surface_nan(
    xs: list[float], ys: list[float]
) -> None:
    assert math.isnan(spearman(xs, ys))
    assert math.isnan(permutation_p(xs, ys))


def test_valid_permutation_p_is_not_zero() -> None:
    p = permutation_p([1.0, 2.0, 3.0], [3.0, 1.0, 2.0])

    assert 0 < p <= 1


def test_strict_interval_parsers_accept_well_formed_cells() -> None:
    assert parse_interval_cell("[-1.2e-3, 4]") == (-0.0012, 4.0)
    assert parse_estimate_interval_cell("0.351 [0.103, 0.868]") == (
        0.351,
        0.103,
        0.868,
    )
    assert parse_percentage_cell("63.8%") == 63.8
    assert parse_percentage_interval_cell("40.2% [21.3%, 69.5%]") == (
        40.2,
        21.3,
        69.5,
    )


@pytest.mark.parametrize(
    "cell",
    [
        "1, 2",
        "[1, 2, 3]",
        "[2, 1]",
        "[nan, 2]",
        "[1, inf]",
        "[1, 2] trailing",
    ],
)
def test_strict_interval_parser_rejects_malformed_cells(cell: str) -> None:
    with pytest.raises(ValueError):
        parse_interval_cell(cell)


@pytest.mark.parametrize(
    "cell",
    [
        "40.2 [21.3%, 69.5%]",
        "40.2% [21.3, 69.5%]",
        "40.2% [21.3%, 69.5]",
        "40.2% [69.5%, 21.3%]",
        "40.2% [21.3%, 69.5%, 80%]",
        "nan% [21.3%, 69.5%]",
        "40.2% [21.3%, inf%]",
    ],
)
def test_percentage_interval_parser_rejects_malformed_cells(cell: str) -> None:
    with pytest.raises(ValueError):
        parse_percentage_interval_cell(cell)


@pytest.mark.parametrize("cell", ["63.8", "63.8%%", "nan%", "inf%"])
def test_percentage_parser_requires_finite_explicit_units(cell: str) -> None:
    with pytest.raises(ValueError):
        parse_percentage_cell(cell)
