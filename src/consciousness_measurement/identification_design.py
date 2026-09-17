"""Identification and release-design theorems for Research III V11-V15.

These utilities formalize what can be identified from imperfect proxy channels,
what resolution a finite design can guarantee, and how to preserve coverage when
a release decision is made before an independent confirmatory analysis.

The latent target is abstract and declared. None of these results establishes that
a particular biological, behavioral, neural, or artificial-system proxy measures
consciousness.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import ceil, log
from typing import Sequence

from .latent_measurement import RateInterval, latent_prevalence_from_proxy_rate, youden_index
from .measurement_robustness import missingness_proxy_rate_bounds


@dataclass(frozen=True)
class MultiSiteIdentifiedSet:
    """Sharp interval for a weighted average prevalence from one pooled proxy rate."""

    lower: float
    upper: float

    def __post_init__(self) -> None:
        if not 0.0 <= self.lower <= self.upper <= 1.0:
            raise ValueError("identified set must lie inside [0,1]")

    @property
    def width(self) -> float:
        return self.upper - self.lower


def missingness_resolution_interval_known_calibration(
    *,
    observed_positives: int,
    observed_trials: int,
    total_trials: int,
    sensitivity: float,
    specificity: float,
    minimum_youden: float = 1e-12,
) -> RateInterval:
    """Sharp latent interval under arbitrary missing outcomes and known calibration.

    V11. The observable positive rate is sharply bounded by assigning every missing
    outcome either zero or one. When calibration is point-known and positively
    informative, the inverse map is monotone, so the sharp latent identified set is
    obtained by applying the inverse to the compatible proxy-rate endpoints and
    clipping only where the latent parameter space [0,1] requires it.
    """
    q_bounds = missingness_proxy_rate_bounds(
        observed_positives=observed_positives,
        observed_trials=observed_trials,
        total_trials=total_trials,
    )
    j = youden_index(sensitivity, specificity)
    if j <= minimum_youden:
        raise ValueError("measurement channel is not sufficiently informative")

    q_min = max(q_bounds.lower, 1.0 - specificity)
    q_max = min(q_bounds.upper, sensitivity)
    if q_min > q_max:
        raise ValueError("missingness bounds are incompatible with the declared calibration")

    lower = latent_prevalence_from_proxy_rate(
        q_min,
        sensitivity,
        specificity,
        minimum_youden=minimum_youden,
    )
    upper = latent_prevalence_from_proxy_rate(
        q_max,
        sensitivity,
        specificity,
        minimum_youden=minimum_youden,
    )
    return RateInterval(lower, upper)


def interior_missingness_width(
    *,
    missing_trials: int,
    total_trials: int,
    sensitivity: float,
    specificity: float,
) -> float:
    """Exact V11 width law before [0,1] clipping: missing_fraction / Youden.

    This identity applies when both sharp proxy-rate endpoints are compatible with
    interior latent prevalences, so no clipping at prevalence zero or one occurs.
    """
    if total_trials <= 0:
        raise ValueError("total_trials must be positive")
    if not 0 <= missing_trials <= total_trials:
        raise ValueError("missing_trials must lie between zero and total_trials")
    j = youden_index(sensitivity, specificity)
    if j <= 0.0:
        raise ValueError("measurement channel must be positively informative")
    return (missing_trials / total_trials) / j


def pooled_average_is_point_identified(
    *,
    weights: Sequence[float],
    sensitivities: Sequence[float],
    specificities: Sequence[float],
    tolerance: float = 1e-12,
) -> bool:
    """Return the V12 necessary-and-sufficient condition for pooled identification.

    With positive site weights and known site calibration, one pooled proxy rate
    identifies the weighted average latent prevalence for every feasible site
    prevalence vector if and only if all site Youden information margins are equal.
    """
    _validate_multisite_inputs(weights, sensitivities, specificities)
    margins = [youden_index(se, sp) for se, sp in zip(sensitivities, specificities, strict=True)]
    if any(j <= 0.0 for j in margins):
        raise ValueError("all site channels must be positively informative")
    return max(margins) - min(margins) <= tolerance


def pooled_average_prevalence_if_identified(
    *,
    pooled_proxy_rate: float,
    weights: Sequence[float],
    sensitivities: Sequence[float],
    specificities: Sequence[float],
    tolerance: float = 1e-12,
) -> float:
    """Recover the pooled average when the V12 equal-Youden condition holds."""
    if not 0.0 <= pooled_proxy_rate <= 1.0:
        raise ValueError("pooled_proxy_rate must lie in [0,1]")
    if not pooled_average_is_point_identified(
        weights=weights,
        sensitivities=sensitivities,
        specificities=specificities,
        tolerance=tolerance,
    ):
        raise ValueError("pooled average prevalence is not point-identified")
    margins = [youden_index(se, sp) for se, sp in zip(sensitivities, specificities, strict=True)]
    j = sum(w * margin for w, margin in zip(weights, margins, strict=True))
    intercept = sum(
        w * (1.0 - sp) for w, sp in zip(weights, specificities, strict=True)
    )
    value = (pooled_proxy_rate - intercept) / j
    if value < -tolerance or value > 1.0 + tolerance:
        raise ValueError("pooled proxy rate is incompatible with the site calibrations")
    return min(1.0, max(0.0, value))


def multisite_average_prevalence_identified_interval(
    *,
    pooled_proxy_rate: float,
    weights: Sequence[float],
    sensitivities: Sequence[float],
    specificities: Sequence[float],
    tolerance: float = 1e-12,
) -> MultiSiteIdentifiedSet:
    """Sharp V13 interval for weighted average prevalence across K sites.

    The pooled observation imposes one equality

        sum_i w_i J_i pi_i = pooled_proxy_rate - sum_i w_i(1-Sp_i),

    with 0 <= pi_i <= 1. Minimizing or maximizing sum_i w_i pi_i is a
    one-constraint linear program. Its exact solution is fractional-knapsack:
    to maximize the target average, allocate latent prevalence first to sites with
    the smallest J_i; to minimize it, allocate first to sites with the largest J_i.
    """
    if not 0.0 <= pooled_proxy_rate <= 1.0:
        raise ValueError("pooled_proxy_rate must lie in [0,1]")
    _validate_multisite_inputs(weights, sensitivities, specificities)

    margins = [youden_index(se, sp) for se, sp in zip(sensitivities, specificities, strict=True)]
    if any(j <= 0.0 for j in margins):
        raise ValueError("all site channels must be positively informative")

    intercept = sum(
        w * (1.0 - sp) for w, sp in zip(weights, specificities, strict=True)
    )
    rhs = pooled_proxy_rate - intercept
    capacities = [w * j for w, j in zip(weights, margins, strict=True)]
    total_capacity = sum(capacities)
    if rhs < -tolerance or rhs > total_capacity + tolerance:
        raise ValueError("pooled proxy rate is incompatible with site calibrations")
    rhs = min(total_capacity, max(0.0, rhs))

    lower = _fractional_extreme(
        rhs=rhs,
        weights=weights,
        margins=margins,
        maximize=False,
    )
    upper = _fractional_extreme(
        rhs=rhs,
        weights=weights,
        margins=margins,
        maximize=True,
    )
    return MultiSiteIdentifiedSet(lower, upper)


def hoeffding_resolution_sample_size(
    *,
    sensitivity: float,
    specificity: float,
    maximum_width: float,
    delta: float = 0.05,
) -> int:
    """V14 sufficient deployment size for a target latent interval width.

    For point-known calibration, a two-sided Hoeffding proxy-rate interval has
    width at most 2*sqrt(log(2/delta)/(2n)). The positively informative inverse
    amplifies this by 1/J. Therefore

        n >= 2 log(2/delta) / (J^2 * maximum_width^2)

    is sufficient to make the resulting latent interval width no larger than the
    predeclared maximum, with clipping only making the interval narrower.
    """
    if not 0.0 < maximum_width <= 1.0:
        raise ValueError("maximum_width must lie in (0,1]")
    if not 0.0 < delta < 1.0:
        raise ValueError("delta must lie strictly between zero and one")
    j = youden_index(sensitivity, specificity)
    if j <= 0.0:
        raise ValueError("measurement channel must be positively informative")
    return ceil(2.0 * log(2.0 / delta) / (j * j * maximum_width * maximum_width))


def independent_gate_preserves_conditional_coverage(
    *,
    marginal_coverage: float,
    release_probability: float,
) -> float:
    """V15 conditional coverage under an independent pilot-gated release design.

    If the release event is measurable with respect to pilot data that are
    independent of the confirmatory data used to construct the interval, then the
    confirmatory interval and release event are independent. Thus conditional
    coverage among released cases equals marginal confirmatory coverage whenever
    the release probability is positive.

    This function returns that guaranteed conditional coverage after validating
    the probability inputs; the theorem is the independence statement above.
    """
    if not 0.0 <= marginal_coverage <= 1.0:
        raise ValueError("marginal_coverage must lie in [0,1]")
    if not 0.0 < release_probability <= 1.0:
        raise ValueError("release_probability must lie in (0,1]")
    return marginal_coverage


def _fractional_extreme(
    *,
    rhs: float,
    weights: Sequence[float],
    margins: Sequence[float],
    maximize: bool,
) -> float:
    order = sorted(
        range(len(weights)),
        key=lambda index: margins[index],
        reverse=not maximize,
    )
    remaining = rhs
    target = 0.0
    for index in order:
        capacity = weights[index] * margins[index]
        take = min(capacity, remaining)
        if capacity > 0.0:
            prevalence = take / capacity
            target += weights[index] * prevalence
        remaining -= take
        if remaining <= 1e-15:
            break
    if remaining > 1e-10:
        raise ValueError("internal multisite optimization did not satisfy the constraint")
    return min(1.0, max(0.0, target))


def _validate_multisite_inputs(
    weights: Sequence[float],
    sensitivities: Sequence[float],
    specificities: Sequence[float],
) -> None:
    if len(weights) < 2:
        raise ValueError("at least two sites are required")
    if len(weights) != len(sensitivities) or len(weights) != len(specificities):
        raise ValueError("weights and calibration vectors must have equal length")
    if any(w <= 0.0 for w in weights):
        raise ValueError("all site weights must be positive")
    if abs(sum(weights) - 1.0) > 1e-12:
        raise ValueError("site weights must sum to one")
    for name, values in (("sensitivity", sensitivities), ("specificity", specificities)):
        if any(value < 0.0 or value > 1.0 for value in values):
            raise ValueError(f"all {name} values must lie in [0,1]")
