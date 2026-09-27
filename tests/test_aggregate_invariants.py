"""Property tests for run pooling (aggregate_beliefs).

Invariants:

1. Mixture identity (differential): with full quantiles on every run,
   ``total_sd ** 2`` equals the variance of the equal-weight mixture of the
   reconstructed run distributions — the same mixture the headline interval
   comes from — for any supports.
2. Law of total variance, term by term: ``within_run_sd ** 2`` is the mean of
   the run variances and ``between_run_sd ** 2`` is the population variance of
   the run *means* (not of the run medians).
3. Intended center: ``point_estimate`` stays the mean of the run point
   estimates (the elicited medians).
4. Permutation invariance of every reported field.
5. The headline interval is the mixture's central interval.
"""

from __future__ import annotations

from dataclasses import asdict
from statistics import fmean, pvariance

import pytest
from hypothesis import given, settings, strategies as st

from llm_econ_beliefs import (
    BeliefEstimate,
    aggregate_beliefs,
    mixture_distribution,
    piecewise_distribution_from_quantiles,
)

QUANTILES = ("p05", "p25", "p50", "p75", "p95")
invariant_settings = settings(max_examples=300, deadline=None, derandomize=True, database=None)

ordered_quantiles = st.lists(
    st.floats(-1e3, 1e3, allow_nan=False, allow_infinity=False), min_size=5, max_size=5
).map(sorted)


def _estimate(values) -> BeliefEstimate:
    return BeliefEstimate(point_estimate=values[2], quantiles=dict(zip(QUANTILES, values)))


@st.composite
def pooled_inputs(draw):
    runs = draw(st.lists(ordered_quantiles, min_size=1, max_size=15))
    lowest = min(run[0] for run in runs)
    highest = max(run[-1] for run in runs)
    lower = draw(st.one_of(st.none(), st.floats(lowest - 100, lowest)))
    upper = draw(st.one_of(st.none(), st.floats(highest, highest + 100)))
    return [_estimate(run) for run in runs], lower, upper


def _components(estimates, lower, upper):
    return [
        piecewise_distribution_from_quantiles(
            estimate.quantiles, lower_support=lower, upper_support=upper
        )
        for estimate in estimates
    ]


@invariant_settings
@given(pooled_inputs())
def test_total_variance_is_the_mixture_variance(inputs):
    estimates, lower, upper = inputs
    pooled = aggregate_beliefs(estimates, lower_support=lower, upper_support=upper)
    mixture = mixture_distribution(_components(estimates, lower, upper))
    assert pooled.total_sd**2 == pytest.approx(mixture.variance(), rel=1e-9, abs=1e-9)


@invariant_settings
@given(pooled_inputs())
def test_variance_terms_use_run_means(inputs):
    estimates, lower, upper = inputs
    pooled = aggregate_beliefs(estimates, lower_support=lower, upper_support=upper)
    components = _components(estimates, lower, upper)
    means = [component.mean() for component in components]
    variances = [component.variance() for component in components]
    expected_between = pvariance(means) if len(means) > 1 else 0.0
    assert pooled.between_run_sd**2 == pytest.approx(expected_between, rel=1e-9, abs=1e-9)
    assert pooled.within_run_sd**2 == pytest.approx(fmean(variances), rel=1e-9, abs=1e-9)
    assert pooled.total_sd**2 == pytest.approx(
        pooled.within_run_sd**2 + pooled.between_run_sd**2, rel=1e-9, abs=1e-9
    )


@invariant_settings
@given(pooled_inputs())
def test_center_stays_the_mean_of_run_medians(inputs):
    estimates, lower, upper = inputs
    pooled = aggregate_beliefs(estimates, lower_support=lower, upper_support=upper)
    assert pooled.point_estimate == fmean(estimate.quantiles["p50"] for estimate in estimates)


@invariant_settings
@given(pooled_inputs())
def test_pooling_is_permutation_invariant(inputs):
    estimates, lower, upper = inputs
    forward = aggregate_beliefs(estimates, lower_support=lower, upper_support=upper)
    backward = aggregate_beliefs(
        list(reversed(estimates)), lower_support=lower, upper_support=upper
    )
    for key, value in asdict(forward).items():
        if isinstance(value, float):
            assert value == pytest.approx(getattr(backward, key), rel=1e-9, abs=1e-9)
        else:
            assert value == getattr(backward, key)


@invariant_settings
@given(pooled_inputs())
def test_headline_interval_is_the_mixture_central_interval(inputs):
    estimates, lower, upper = inputs
    pooled = aggregate_beliefs(estimates, lower_support=lower, upper_support=upper)
    mixture = mixture_distribution(_components(estimates, lower, upper))
    assert (pooled.lower_bound, pooled.upper_bound) == mixture.central_interval(0.9)


def test_minimized_audit_counterexample():
    # Two runs with equal medians but one right-skewed: the medians agree, so
    # the old median-based between-run term was 0 and understated the
    # mixture variance (0.0554166... vs 0.0610416...).
    estimates = [_estimate([0, 0, 0, 0, 0]), _estimate([0, 0, 0, 0, 1])]
    pooled = aggregate_beliefs(estimates)
    assert pooled.point_estimate == 0.0
    assert pooled.total_sd**2 == pytest.approx(0.06104166666666667, rel=1e-12)
    assert pooled.between_run_sd**2 == pytest.approx(pvariance([0.0, 0.15]), rel=1e-12)


def test_symmetric_runs_leave_the_between_term_unchanged():
    # When every run distribution is symmetric its mean is its median, so the
    # corrected between-run term coincides with the variance of the points.
    estimates = [_estimate([c - 2, c - 1, c, c + 1, c + 2]) for c in (0.0, 1.0, 5.0)]
    pooled = aggregate_beliefs(estimates)
    assert pooled.between_run_sd**2 == pytest.approx(pvariance([0.0, 1.0, 5.0]))
