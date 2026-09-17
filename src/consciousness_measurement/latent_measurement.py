"""Identification and finite-sample bounds for an imperfect binary evidence channel.

The latent target in this module is an abstract declared binary measurement target.
The mathematics does not identify consciousness by itself. Scientific interpretation
requires an independently justified target definition, calibration domain, and assumptions.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import isfinite, log, sqrt


@dataclass(frozen=True)
class RateInterval:
    """Closed interval contained in [0, 1]."""

    lower: float
    upper: float

    def __post_init__(self) -> None:
        if not (isfinite(self.lower) and isfinite(self.upper)):
            raise ValueError("rate bounds must be finite")
        if not 0.0 <= self.lower <= self.upper <= 1.0:
            raise ValueError("rate bounds must satisfy 0 <= lower <= upper <= 1")

    @property
    def width(self) -> float:
        return self.upper - self.lower


@dataclass(frozen=True)
class CalibrationBox:
    """Sensitivity/specificity uncertainty set for one binary evidence channel."""

    sensitivity: RateInterval
    specificity: RateInterval

    @property
    def minimum_youden(self) -> float:
        return self.sensitivity.lower + self.specificity.lower - 1.0

    def validate_informative(self, margin: float = 0.0) -> None:
        if self.minimum_youden <= margin:
            raise ValueError(
                "calibration box must satisfy sensitivity + specificity - 1 > margin"
            )


def youden_index(sensitivity: float, specificity: float) -> float:
    """Return J = sensitivity + specificity - 1."""
    _validate_unit_rate("sensitivity", sensitivity)
    _validate_unit_rate("specificity", specificity)
    return sensitivity + specificity - 1.0


def proxy_rate_from_latent_prevalence(
    prevalence: float,
    sensitivity: float,
    specificity: float,
) -> float:
    """Map latent prevalence to the observable positive proxy rate.

    q = (1 - specificity) + J * prevalence,
    where J = sensitivity + specificity - 1.
    """
    _validate_unit_rate("prevalence", prevalence)
    j = youden_index(sensitivity, specificity)
    return (1.0 - specificity) + j * prevalence


def latent_prevalence_from_proxy_rate(
    proxy_rate: float,
    sensitivity: float,
    specificity: float,
    *,
    minimum_youden: float = 1e-12,
) -> float:
    """Invert the binary measurement channel when calibration is point-known."""
    _validate_unit_rate("proxy_rate", proxy_rate)
    j = youden_index(sensitivity, specificity)
    if j <= minimum_youden:
        raise ValueError("measurement channel is not sufficiently informative to invert")
    prevalence = (proxy_rate + specificity - 1.0) / j
    if prevalence < -1e-12 or prevalence > 1.0 + 1e-12:
        raise ValueError("proxy rate is incompatible with the declared calibration")
    return min(1.0, max(0.0, prevalence))


def hoeffding_rate_interval(successes: int, trials: int, delta: float = 0.05) -> RateInterval:
    """Distribution-free two-sided Hoeffding interval for a Bernoulli mean.

    With probability at least 1-delta,
    |q_hat - q| <= sqrt(log(2/delta)/(2n)).
    """
    if trials <= 0:
        raise ValueError("trials must be positive")
    if not 0 <= successes <= trials:
        raise ValueError("successes must lie between zero and trials")
    if not 0.0 < delta < 1.0:
        raise ValueError("delta must lie strictly between zero and one")
    q_hat = successes / trials
    epsilon = sqrt(log(2.0 / delta) / (2.0 * trials))
    return RateInterval(max(0.0, q_hat - epsilon), min(1.0, q_hat + epsilon))


def calibration_box_prevalence_outer_interval(
    proxy_rate: RateInterval,
    calibration: CalibrationBox,
    *,
    minimum_youden: float = 1e-6,
) -> RateInterval:
    """Guaranteed outer identification interval under box calibration uncertainty.

    For q in [qL,qU], Se in [sL,sU], Sp in [cL,cU] and
    J = Se + Sp - 1 >= kappa > 0,

        prevalence = (q + Sp - 1) / J.

    The interval below is obtained by valid interval arithmetic. It is deliberately
    conservative because specificity appears in both numerator and denominator.
    The returned interval contains the exact identified set whenever the declared
    calibration box contains the true sensitivity/specificity.
    """
    calibration.validate_informative(minimum_youden)
    numerator_lower = proxy_rate.lower + calibration.specificity.lower - 1.0
    numerator_upper = proxy_rate.upper + calibration.specificity.upper - 1.0
    denominator_lower = calibration.minimum_youden
    denominator_upper = calibration.sensitivity.upper + calibration.specificity.upper - 1.0

    lower = numerator_lower / denominator_upper
    upper = numerator_upper / denominator_lower
    return RateInterval(max(0.0, lower), min(1.0, upper))


def finite_sample_prevalence_outer_interval(
    successes: int,
    trials: int,
    calibration: CalibrationBox,
    *,
    delta: float = 0.05,
    minimum_youden: float = 1e-6,
) -> RateInterval:
    """Finite-sample prevalence interval from proxy counts and calibration uncertainty.

    Conditional on the true calibration lying in ``calibration`` and independent
    Bernoulli sampling of the observed proxy, this interval contains the true
    prevalence with probability at least 1-delta.
    """
    q_interval = hoeffding_rate_interval(successes, trials, delta)
    return calibration_box_prevalence_outer_interval(
        q_interval,
        calibration,
        minimum_youden=minimum_youden,
    )


def latent_effect_from_proxy_effect(
    proxy_effect: float,
    sensitivity: float,
    specificity: float,
    *,
    minimum_youden: float = 1e-12,
) -> float:
    """Recover a latent prevalence contrast when calibration is invariant.

    If q_z = (1-Sp) + J*pi_z in both conditions z=0,1, then
    delta_pi = delta_q / J.
    """
    if not isfinite(proxy_effect):
        raise ValueError("proxy effect must be finite")
    j = youden_index(sensitivity, specificity)
    if j <= minimum_youden:
        raise ValueError("measurement channel is not sufficiently informative")
    return proxy_effect / j


def transport_bias_from_calibration_shift(
    latent_prevalence_after: float,
    baseline_sensitivity: float,
    baseline_specificity: float,
    shifted_sensitivity: float,
    shifted_specificity: float,
    *,
    minimum_youden: float = 1e-12,
) -> float:
    """Exact bias in a contrast corrected with stale baseline calibration.

    Let condition 0 use baseline calibration and condition 1 use shifted calibration.
    If both observed proxy rates are corrected using baseline J0, the bias in the
    estimated latent prevalence contrast is

        ((J1-J0)*pi1 + (FPR1-FPR0)) / J0.

    This isolates the price of violating measurement invariance across conditions.
    """
    _validate_unit_rate("latent_prevalence_after", latent_prevalence_after)
    j0 = youden_index(baseline_sensitivity, baseline_specificity)
    j1 = youden_index(shifted_sensitivity, shifted_specificity)
    if j0 <= minimum_youden:
        raise ValueError("baseline measurement channel is not sufficiently informative")
    fpr0 = 1.0 - baseline_specificity
    fpr1 = 1.0 - shifted_specificity
    return ((j1 - j0) * latent_prevalence_after + (fpr1 - fpr0)) / j0


def _validate_unit_rate(name: str, value: float) -> None:
    if not isfinite(value) or not 0.0 <= value <= 1.0:
        raise ValueError(f"{name} must be finite and lie in [0, 1]")
