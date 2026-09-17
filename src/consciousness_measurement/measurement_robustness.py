"""Advanced robustness mathematics for Research III measurement science.

The latent target is abstract and declared. These functions validate statistical
measurement logic under explicit assumptions; they do not establish that a
particular biological or artificial system is conscious.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import isfinite

from .latent_measurement import (
    CalibrationBox,
    RateInterval,
    calibration_box_prevalence_outer_interval,
    hoeffding_rate_interval,
    proxy_rate_from_latent_prevalence,
    youden_index,
)


@dataclass(frozen=True)
class LocalInversionSensitivity:
    """Local derivatives of the calibrated binary-channel inverse."""

    d_prevalence_d_proxy_rate: float
    d_prevalence_d_sensitivity: float
    d_prevalence_d_specificity: float


@dataclass(frozen=True)
class TwoSiteIdentifiedSet:
    """Sharp interval for population-average prevalence from one pooled proxy rate."""

    lower: float
    upper: float

    def __post_init__(self) -> None:
        if not 0.0 <= self.lower <= self.upper <= 1.0:
            raise ValueError("identified set must lie inside [0,1]")

    @property
    def width(self) -> float:
        return self.upper - self.lower


def joint_finite_sample_prevalence_outer_interval(
    *,
    proxy_successes: int,
    proxy_trials: int,
    sensitivity_successes: int,
    sensitivity_trials: int,
    specificity_successes: int,
    specificity_trials: int,
    delta: float = 0.05,
    minimum_youden: float = 1e-6,
) -> RateInterval:
    """Simultaneous finite-sample interval including calibration-sample uncertainty.

    Three independent Bernoulli means are estimated: deployment proxy rate,
    sensitivity on a declared target-positive calibration sample, and specificity
    on a declared target-negative calibration sample. Giving each Hoeffding event
    failure probability delta/3 and applying the union bound yields simultaneous
    coverage at least 1-delta before the outer identification map is applied.
    """
    if not 0.0 < delta < 1.0:
        raise ValueError("delta must lie strictly between zero and one")
    local_delta = delta / 3.0
    q_interval = hoeffding_rate_interval(proxy_successes, proxy_trials, local_delta)
    sensitivity_interval = hoeffding_rate_interval(
        sensitivity_successes,
        sensitivity_trials,
        local_delta,
    )
    specificity_interval = hoeffding_rate_interval(
        specificity_successes,
        specificity_trials,
        local_delta,
    )
    calibration = CalibrationBox(sensitivity_interval, specificity_interval)
    return calibration_box_prevalence_outer_interval(
        q_interval,
        calibration,
        minimum_youden=minimum_youden,
    )


def missingness_proxy_rate_bounds(
    *,
    observed_positives: int,
    observed_trials: int,
    total_trials: int,
) -> RateInterval:
    """Sharp proxy-rate bounds under arbitrary outcomes among missing trials.

    If no assumption is made about the missing outcomes, the smallest possible
    full-sample positive count equals the observed positives, and the largest
    equals observed positives plus the number missing.
    """
    if total_trials <= 0:
        raise ValueError("total_trials must be positive")
    if not 0 <= observed_trials <= total_trials:
        raise ValueError("observed_trials must lie between zero and total_trials")
    if not 0 <= observed_positives <= observed_trials:
        raise ValueError("observed_positives must lie between zero and observed_trials")
    missing = total_trials - observed_trials
    return RateInterval(
        observed_positives / total_trials,
        (observed_positives + missing) / total_trials,
    )


def missingness_robust_prevalence_outer_interval(
    *,
    observed_positives: int,
    observed_trials: int,
    total_trials: int,
    calibration: CalibrationBox,
    minimum_youden: float = 1e-6,
) -> RateInterval:
    """Propagate arbitrary-missingness uncertainty through calibration uncertainty."""
    q_interval = missingness_proxy_rate_bounds(
        observed_positives=observed_positives,
        observed_trials=observed_trials,
        total_trials=total_trials,
    )
    return calibration_box_prevalence_outer_interval(
        q_interval,
        calibration,
        minimum_youden=minimum_youden,
    )


def inverse_slope_amplification(sensitivity: float, specificity: float) -> float:
    """Absolute amplification of proxy-rate error into latent-prevalence error.

    For fixed calibration, pi=(q+Sp-1)/J, so |d pi/d q|=1/J.
    """
    j = youden_index(sensitivity, specificity)
    if j <= 0.0:
        raise ValueError("measurement channel is not positively informative")
    return 1.0 / j


def local_inversion_sensitivities(
    prevalence: float,
    sensitivity: float,
    specificity: float,
) -> LocalInversionSensitivity:
    """Return exact first derivatives of the point-identified inverse."""
    if not isfinite(prevalence) or not 0.0 <= prevalence <= 1.0:
        raise ValueError("prevalence must lie in [0,1]")
    j = youden_index(sensitivity, specificity)
    if j <= 0.0:
        raise ValueError("measurement channel is not positively informative")
    return LocalInversionSensitivity(
        d_prevalence_d_proxy_rate=1.0 / j,
        d_prevalence_d_sensitivity=-prevalence / j,
        d_prevalence_d_specificity=(1.0 - prevalence) / j,
    )


def pooled_two_site_proxy_rate(
    *,
    site1_weight: float,
    site1_prevalence: float,
    site2_prevalence: float,
    site1_sensitivity: float,
    site1_specificity: float,
    site2_sensitivity: float,
    site2_specificity: float,
) -> float:
    """Observable pooled proxy rate for two sites with site-specific calibration."""
    if not 0.0 < site1_weight < 1.0:
        raise ValueError("site1_weight must lie strictly between zero and one")
    q1 = proxy_rate_from_latent_prevalence(
        site1_prevalence,
        site1_sensitivity,
        site1_specificity,
    )
    q2 = proxy_rate_from_latent_prevalence(
        site2_prevalence,
        site2_sensitivity,
        site2_specificity,
    )
    return site1_weight * q1 + (1.0 - site1_weight) * q2


def two_site_average_prevalence_identified_interval(
    *,
    pooled_proxy_rate: float,
    site1_weight: float,
    site1_sensitivity: float,
    site1_specificity: float,
    site2_sensitivity: float,
    site2_specificity: float,
    tolerance: float = 1e-12,
) -> TwoSiteIdentifiedSet:
    """Sharp average-prevalence set from one pooled proxy rate and two calibrations.

    With w=site1_weight,

        q_bar = c + a*pi1 + b*pi2,

    where a=w*J1, b=(1-w)*J2 and c is the weighted false-positive
    intercept. One scalar pooled observation does not generally identify the two
    site prevalences. Because both the feasibility equation and target average are
    linear, extrema occur at endpoints of the feasible line segment in [0,1]^2.
    """
    if not 0.0 <= pooled_proxy_rate <= 1.0:
        raise ValueError("pooled_proxy_rate must lie in [0,1]")
    if not 0.0 < site1_weight < 1.0:
        raise ValueError("site1_weight must lie strictly between zero and one")

    j1 = youden_index(site1_sensitivity, site1_specificity)
    j2 = youden_index(site2_sensitivity, site2_specificity)
    if j1 <= 0.0 or j2 <= 0.0:
        raise ValueError("both site channels must be positively informative")

    w = site1_weight
    a = w * j1
    b = (1.0 - w) * j2
    intercept = w * (1.0 - site1_specificity) + (1.0 - w) * (
        1.0 - site2_specificity
    )
    rhs = pooled_proxy_rate - intercept

    p1_lower = max(0.0, (rhs - b) / a)
    p1_upper = min(1.0, rhs / a)
    if p1_lower > p1_upper + tolerance:
        raise ValueError("pooled proxy rate is incompatible with site calibrations")
    p1_lower = min(1.0, max(0.0, p1_lower))
    p1_upper = min(1.0, max(0.0, p1_upper))

    def average_at(p1: float) -> float:
        p2 = (rhs - a * p1) / b
        if p2 < -tolerance or p2 > 1.0 + tolerance:
            raise ValueError("internal feasibility calculation left [0,1]")
        p2 = min(1.0, max(0.0, p2))
        return w * p1 + (1.0 - w) * p2

    values = (average_at(p1_lower), average_at(p1_upper))
    return TwoSiteIdentifiedSet(min(values), max(values))
