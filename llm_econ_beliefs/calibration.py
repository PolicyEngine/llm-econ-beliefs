"""Evaluate and recalibrate elicited predictive distributions."""

from __future__ import annotations

import math
from bisect import bisect_right
from dataclasses import dataclass, field
from statistics import fmean, pvariance
from typing import Sequence

from .distributions import (
    MixtureDistribution,
    PiecewiseDistribution,
    empirical_cdf,
)


@dataclass(frozen=True)
class CalibrationExample:
    """One resolved outcome paired with a predictive distribution."""

    distribution: PiecewiseDistribution | MixtureDistribution | CalibratedDistribution
    observed_value: float
    label: str | None = None


@dataclass(frozen=True)
class CalibrationMetrics:
    """Summary metrics for predictive calibration on resolved tasks."""

    n_examples: int
    quantile_levels: tuple[float, ...]
    interval_levels: tuple[float, ...]
    mean_pinball_loss: float
    weighted_interval_score: float
    pit_mean: float
    pit_variance: float
    coverage_by_interval: dict[float, float]


@dataclass(frozen=True)
class EmpiricalCDFCalibrator:
    """Empirical PIT recalibrator."""

    sorted_pits: tuple[float, ...]
    method: str = "empirical_pit"

    def __post_init__(self) -> None:
        if not self.sorted_pits:
            raise ValueError("At least one PIT value is required")
        pits = tuple(float(pit) for pit in self.sorted_pits)
        if any(math.isnan(pit) for pit in pits):
            raise ValueError("PIT values must not be NaN")
        object.__setattr__(
            self,
            "sorted_pits",
            tuple(sorted(min(max(pit, 0.0), 1.0) for pit in pits)),
        )

    @classmethod
    def fit(cls, examples: Sequence[CalibrationExample]) -> "EmpiricalCDFCalibrator":
        if not examples:
            raise ValueError("At least one calibration example is required")
        return cls(
            tuple(
                example.distribution.cdf(example.observed_value) for example in examples
            )
        )

    def map_probability(self, probability: float) -> float:
        """Map an uncalibrated CDF value through the empirical PIT CDF.

        This is the step function ``G(u) = #{PIT <= u} / n``.
        """
        probability = min(max(probability, 0.0), 1.0)
        return empirical_cdf(self.sorted_pits, probability)

    def inverse_probability(self, probability: float) -> float:
        """Map a target quantile level back to the uncalibrated probability scale.

        Returns the generalized inverse of :meth:`map_probability`,
        ``inf{u in [0, 1] : G(u) >= p}``: the ``k``-th smallest PIT for the
        smallest ``k`` with ``k / n >= p``. Interpolating between PITs instead
        would return a level whose calibrated CDF can fall short of ``p``.
        """
        probability = min(max(probability, 0.0), 1.0)
        if probability <= 0.0:
            return 0.0
        return self.sorted_pits[_minimal_rank(probability, len(self.sorted_pits)) - 1]

    def calibrate_distribution(
        self,
        distribution: PiecewiseDistribution | MixtureDistribution,
    ) -> "CalibratedDistribution":
        return CalibratedDistribution(
            base_distribution=distribution,
            calibrator=self,
        )


@dataclass(frozen=True)
class CalibratedDistribution:
    """Distribution wrapper produced by empirical PIT recalibration.

    Composing the step PIT CDF ``G`` with the base CDF ``F`` gives
    ``P(X <= x) = #{i : PIT_i <= F(x)} / n = #{i : F^-1(PIT_i) <= x} / n``,
    so the calibrated distribution is the empirical distribution of the ``n``
    base quantiles ``F^-1(PIT_i)``. Both :meth:`cdf` and :meth:`quantile` are
    computed from those same atoms, which makes them an exact
    generalized-inverse pair (``quantile(p) <= x`` iff ``p <= cdf(x)``) free of
    floating-point round trips through ``F``. A PIT of 0 (an outcome below the
    base support) places its atom at the support's lower edge, so the CDF
    still starts at 0.
    """

    base_distribution: PiecewiseDistribution | MixtureDistribution
    calibrator: EmpiricalCDFCalibrator
    _atoms: tuple[float, ...] = field(init=False, repr=False, compare=False)

    def __post_init__(self) -> None:
        atoms = sorted(
            self.base_distribution.quantile(pit) for pit in self.calibrator.sorted_pits
        )
        object.__setattr__(self, "_atoms", tuple(atoms))

    def cdf(self, value: float) -> float:
        return bisect_right(self._atoms, value) / len(self._atoms)

    def quantile(self, probability: float) -> float:
        probability = min(max(probability, 0.0), 1.0)
        if probability <= 0.0:
            return self._atoms[0]
        return self._atoms[_minimal_rank(probability, len(self._atoms)) - 1]

    def central_interval(self, confidence_level: float) -> tuple[float, float]:
        lower_prob = (1.0 - confidence_level) / 2.0
        upper_prob = 1.0 - lower_prob
        return self.quantile(lower_prob), self.quantile(upper_prob)


def fit_pit_calibrator(examples: Sequence[CalibrationExample]) -> EmpiricalCDFCalibrator:
    """Fit an empirical PIT calibrator on resolved examples."""
    return EmpiricalCDFCalibrator.fit(examples)


def _minimal_rank(probability: float, n: int) -> int:
    """Smallest ``k`` in ``1..n`` with ``k / n >= probability``, for ``0 < p <= 1``.

    Computed with the same ``k / n`` division the empirical CDF uses, so a
    float such as ``0.7 * 10 == 7.000000000000001`` cannot push the rank past
    the order statistic the CDF actually reaches.
    """
    rank = min(max(math.ceil(probability * n), 1), n)
    while rank > 1 and (rank - 1) / n >= probability:
        rank -= 1
    while rank < n and rank / n < probability:
        rank += 1
    return rank


def evaluate_calibration(
    examples: Sequence[CalibrationExample],
    *,
    quantile_levels: Sequence[float] = (0.05, 0.25, 0.50, 0.75, 0.95),
    interval_levels: Sequence[float] = (0.5, 0.9),
) -> CalibrationMetrics:
    """Evaluate predictive calibration on resolved numeric targets."""
    if not examples:
        raise ValueError("At least one calibration example is required")

    quantile_levels = tuple(quantile_levels)
    interval_levels = tuple(interval_levels)

    pinball_losses = []
    wis_scores = []
    pits = []
    coverage_by_interval = {level: 0.0 for level in interval_levels}

    for example in examples:
        pits.append(example.distribution.cdf(example.observed_value))
        for level in quantile_levels:
            predicted_quantile = example.distribution.quantile(level)
            pinball_losses.append(
                _pinball_loss(
                    example.observed_value,
                    predicted_quantile,
                    level,
                )
            )

        wis_scores.append(
            _weighted_interval_score(
                example.distribution,
                example.observed_value,
                interval_levels,
            )
        )

        for level in interval_levels:
            lower, upper = example.distribution.central_interval(level)
            if lower <= example.observed_value <= upper:
                coverage_by_interval[level] += 1.0

    n_examples = len(examples)
    return CalibrationMetrics(
        n_examples=n_examples,
        quantile_levels=quantile_levels,
        interval_levels=interval_levels,
        mean_pinball_loss=fmean(pinball_losses),
        weighted_interval_score=fmean(wis_scores),
        pit_mean=fmean(pits),
        pit_variance=pvariance(pits) if len(pits) > 1 else 0.0,
        coverage_by_interval={
            level: covered / n_examples
            for level, covered in coverage_by_interval.items()
        },
    )


def _pinball_loss(observed_value: float, predicted_quantile: float, level: float) -> float:
    error = observed_value - predicted_quantile
    return max(level * error, (level - 1.0) * error)


def _interval_score(
    observed_value: float,
    lower: float,
    upper: float,
    alpha: float,
) -> float:
    score = upper - lower
    if observed_value < lower:
        score += (2.0 / alpha) * (lower - observed_value)
    elif observed_value > upper:
        score += (2.0 / alpha) * (observed_value - upper)
    return score


def _weighted_interval_score(
    distribution: PiecewiseDistribution | MixtureDistribution | CalibratedDistribution,
    observed_value: float,
    interval_levels: Sequence[float],
) -> float:
    median = distribution.quantile(0.5)
    total = 0.5 * abs(observed_value - median)
    normalizer = 0.5

    for level in interval_levels:
        alpha = 1.0 - level
        lower, upper = distribution.central_interval(level)
        total += (alpha / 2.0) * _interval_score(
            observed_value,
            lower,
            upper,
            alpha,
        )
        normalizer += alpha / 2.0

    return total / normalizer
