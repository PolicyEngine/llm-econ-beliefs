"""Property tests for empirical PIT recalibration.

Invariants:

1. Distribution axioms: the calibrated CDF is nondecreasing, lies in [0, 1],
   and has ``cdf(-inf) == 0`` and ``cdf(+inf) == 1`` even when calibration
   outcomes fall outside the base support.
2. Generalized inverse (exact, no tolerance): for every ``p`` in (0, 1] and
   every ``x``, ``quantile(p) <= x`` if and only if ``p <= cdf(x)``. In
   particular ``cdf(quantile(p)) >= p``.
3. The same Galois connection holds for the PIT map itself:
   ``inverse_probability(p) <= u`` iff ``p <= map_probability(u)``.
4. Composition: inside the base support the calibrated CDF equals the
   documented forward map ``G(F(x))``.
"""

from __future__ import annotations

import math

import pytest
from hypothesis import given, settings, strategies as st

from llm_econ_beliefs import (
    CalibrationExample,
    EmpiricalCDFCalibrator,
    PiecewiseDistribution,
    evaluate_calibration,
    fit_pit_calibrator,
    mixture_distribution,
    piecewise_distribution_from_quantiles,
)

QUANTILES = ("p05", "p25", "p50", "p75", "p95")
invariant_settings = settings(max_examples=300, deadline=None, derandomize=True, database=None)

ordered_quantiles = st.lists(
    st.floats(-100, 100, allow_nan=False, allow_infinity=False), min_size=5, max_size=5
).map(sorted)
probabilities = st.floats(0.0, 1.0, exclude_min=True)


@st.composite
def base_distributions(draw):
    runs = draw(st.lists(ordered_quantiles, min_size=1, max_size=4))
    components = [piecewise_distribution_from_quantiles(dict(zip(QUANTILES, run))) for run in runs]
    return components[0] if len(components) == 1 else mixture_distribution(components)


@st.composite
def calibrated_cases(draw):
    base = draw(base_distributions())
    observations = draw(
        st.lists(st.floats(-300, 300, allow_nan=False), min_size=1, max_size=12)
    )
    calibrator = fit_pit_calibrator(
        [CalibrationExample(base, observed) for observed in observations]
    )
    return base, calibrator, calibrator.calibrate_distribution(base)


def _probe_points(base, calibrated):
    atoms = list(calibrated._atoms)
    points = [-math.inf, math.inf, base.lower_support, base.upper_support, *atoms]
    points += [math.nextafter(atom, -math.inf) for atom in atoms]
    points += [math.nextafter(atom, math.inf) for atom in atoms]
    return points


@invariant_settings
@given(calibrated_cases())
def test_calibrated_cdf_is_a_distribution_function(case):
    base, _, calibrated = case
    assert calibrated.cdf(-math.inf) == 0.0
    assert calibrated.cdf(math.inf) == 1.0
    points = sorted(_probe_points(base, calibrated))
    values = [calibrated.cdf(point) for point in points]
    assert all(0.0 <= value <= 1.0 for value in values)
    assert values == sorted(values)


@invariant_settings
@given(calibrated_cases(), st.lists(probabilities, min_size=1, max_size=8))
def test_calibrated_quantile_is_the_exact_generalized_inverse(case, levels):
    base, _, calibrated = case
    for probability in levels:
        quantile = calibrated.quantile(probability)
        assert calibrated.cdf(quantile) >= probability
        for point in _probe_points(base, calibrated):
            assert (quantile <= point) == (probability <= calibrated.cdf(point))


@invariant_settings
@given(calibrated_cases(), st.lists(probabilities, min_size=2, max_size=8))
def test_calibrated_quantile_is_monotone(case, levels):
    _, _, calibrated = case
    ordered = sorted(levels)
    values = [calibrated.quantile(level) for level in ordered]
    assert values == sorted(values)


@invariant_settings
@given(
    st.lists(st.floats(0.0, 1.0), min_size=1, max_size=20),
    probabilities,
    st.floats(0.0, 1.0),
)
def test_pit_map_and_inverse_form_a_galois_connection(pits, probability, level):
    calibrator = EmpiricalCDFCalibrator(tuple(pits))
    inverse = calibrator.inverse_probability(probability)
    assert (inverse <= level) == (probability <= calibrator.map_probability(level))


@invariant_settings
@given(
    st.lists(st.integers(-2, 12), min_size=1, max_size=12),
    st.integers(0, 9),
)
def test_calibrated_cdf_is_pit_map_composed_with_base_cdf(observations, cell):
    # Uniform base on [0, 10]; probing at half-integers keeps every PIT and
    # every probe exactly representable, so composition must match exactly.
    base = PiecewiseDistribution(((0.0, 10.0, 1.0),))
    calibrator = fit_pit_calibrator(
        [CalibrationExample(base, float(observed)) for observed in observations]
    )
    calibrated = calibrator.calibrate_distribution(base)
    point = cell + 0.5
    assert calibrated.cdf(point) == calibrator.map_probability(base.cdf(point))


def test_audit_counterexample_quantile_reaches_its_level():
    base = PiecewiseDistribution(((0.0, 10.0, 1.0),))
    calibrated = fit_pit_calibrator(
        [CalibrationExample(base, 1.0), CalibrationExample(base, 2.0)]
    ).calibrate_distribution(base)
    quantile = calibrated.quantile(0.75)
    # Before the fix: quantile 1.75 with cdf 0.5 < 0.75.
    assert quantile == 2.0
    assert calibrated.cdf(quantile) >= 0.75


def test_audit_counterexample_lower_tail_starts_at_zero():
    base = PiecewiseDistribution(((0.0, 1.0, 1.0),))
    calibrated = fit_pit_calibrator([CalibrationExample(base, -1.0)]).calibrate_distribution(base)
    # Before the fix: cdf(-inf) == 1.0. The outcome below the support now
    # places its mass at the support's lower edge.
    assert calibrated.cdf(-math.inf) == 0.0
    assert calibrated.cdf(math.nextafter(0.0, -1.0)) == 0.0
    assert calibrated.cdf(0.0) == 1.0


def test_rank_is_not_pushed_past_its_order_statistic_by_float_rounding():
    # 0.7 * 10 == 7.000000000000001 in floating point; the 0.7 quantile of ten
    # PITs is the seventh, not the eighth.
    calibrator = EmpiricalCDFCalibrator(tuple(i / 10 for i in range(1, 11)))
    assert calibrator.inverse_probability(0.7) == 0.7


@pytest.mark.parametrize("pits", [(), (float("nan"),)])
def test_calibrator_rejects_empty_or_nan_pits(pits):
    with pytest.raises(ValueError):
        EmpiricalCDFCalibrator(pits)


def test_calibrated_distribution_evaluates_like_any_distribution():
    base = piecewise_distribution_from_quantiles(dict(zip(QUANTILES, (-1, -0.5, 0, 0.5, 1))))
    calibrated = fit_pit_calibrator(
        [CalibrationExample(base, value) for value in (-0.2, 0.1, 0.4, 0.9)]
    ).calibrate_distribution(base)
    metrics = evaluate_calibration(
        [CalibrationExample(calibrated, 0.3), CalibrationExample(calibrated, -0.4)]
    )
    assert metrics.n_examples == 2
    assert 0.0 <= metrics.pit_mean <= 1.0
    lower, upper = calibrated.central_interval(0.9)
    assert lower <= upper
