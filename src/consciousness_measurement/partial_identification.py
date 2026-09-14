"""Dependence-robust partial identification for binary evidence channels.

The functions in this module answer a narrow question: what can calibrated
marginal channel performance alone imply about a jointly observed evidence
pattern when conditional dependence between channels is unknown?

They use sharp Frechet-Hoeffding bounds for intersections. The resulting
likelihood-ratio and posterior intervals are assumption-bound research objects,
not direct probabilities of consciousness and not clinical classifiers.
"""

from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass
from math import inf, isfinite

from .evidence import EvidenceChannel


@dataclass(frozen=True)
class ProbabilityInterval:
    """Closed interval contained in the probability unit interval."""

    lower: float
    upper: float

    def __post_init__(self) -> None:
        if not (isfinite(self.lower) and isfinite(self.upper)):
            raise ValueError("probability bounds must be finite")
        if not 0.0 <= self.lower <= self.upper <= 1.0:
            raise ValueError("probability bounds must satisfy 0 <= lower <= upper <= 1")


@dataclass(frozen=True)
class LikelihoodRatioInterval:
    """Closed likelihood-ratio interval with an optionally infinite upper end."""

    lower: float
    upper: float

    def __post_init__(self) -> None:
        if not isfinite(self.lower) or self.lower < 0.0:
            raise ValueError("likelihood-ratio lower bound must be finite and nonnegative")
        if self.upper < self.lower:
            raise ValueError("likelihood-ratio upper bound must be at least the lower bound")
        if not (isfinite(self.upper) or self.upper == inf):
            raise ValueError("likelihood-ratio upper bound must be finite or positive infinity")


@dataclass(frozen=True)
class DependenceRobustFusion:
    """Partial-identification result under unrestricted conditional dependence."""

    target_pattern_probability: ProbabilityInterval
    nontarget_pattern_probability: ProbabilityInterval
    likelihood_ratio: LikelihoodRatioInterval
    posterior: ProbabilityInterval

    @property
    def is_vacuous(self) -> bool:
        """Return whether the posterior interval spans the full unit interval."""
        return self.posterior.lower == 0.0 and self.posterior.upper == 1.0


def frechet_intersection_bounds(probabilities: Sequence[float]) -> ProbabilityInterval:
    """Return sharp bounds for an intersection from marginal probabilities.

    For events A_1, ..., A_n with known marginals p_i and otherwise unrestricted
    dependence,

        max(0, sum_i p_i - (n - 1)) <= P(intersection_i A_i) <= min_i p_i.

    The empty intersection has probability one.
    """
    values = tuple(float(value) for value in probabilities)
    if not values:
        return ProbabilityInterval(1.0, 1.0)
    if any(not isfinite(value) or not 0.0 <= value <= 1.0 for value in values):
        raise ValueError("marginal probabilities must be finite and lie in [0, 1]")

    lower = max(0.0, sum(values) - (len(values) - 1))
    upper = min(values)
    return ProbabilityInterval(lower, upper)


def conditional_pattern_probability_bounds(
    observations: Sequence[tuple[EvidenceChannel, bool]],
) -> tuple[ProbabilityInterval, ProbabilityInterval]:
    """Bound an observed binary pattern under target and non-target conditions.

    ``EvidenceChannel.sensitivity`` is P(positive | target) and specificity is
    P(negative | non-target). For each observed sign, this function converts the
    channel calibration into the corresponding marginal pattern probability and
    then applies Frechet-Hoeffding bounds separately under target and non-target.
    """
    target_marginals: list[float] = []
    nontarget_marginals: list[float] = []

    for channel, positive in observations:
        if positive:
            target_marginals.append(channel.sensitivity)
            nontarget_marginals.append(1.0 - channel.specificity)
        else:
            target_marginals.append(1.0 - channel.sensitivity)
            nontarget_marginals.append(channel.specificity)

    return (
        frechet_intersection_bounds(target_marginals),
        frechet_intersection_bounds(nontarget_marginals),
    )


def likelihood_ratio_bounds(
    target_probability: ProbabilityInterval,
    nontarget_probability: ProbabilityInterval,
) -> LikelihoodRatioInterval:
    """Map conditional pattern-probability intervals to sharp LR bounds.

    The numerator and denominator dependence structures are allowed to vary
    independently within their admissible Frechet classes. A zero lower bound on
    the non-target pattern probability therefore permits an infinite LR upper
    bound. If the pattern is impossible under every non-target distribution, the
    ordinary likelihood ratio is not identified by this helper and an error is
    raised rather than inventing a finite value.
    """
    if nontarget_probability.upper == 0.0:
        raise ValueError("non-target pattern probability is identically zero")

    lower = target_probability.lower / nontarget_probability.upper
    if nontarget_probability.lower == 0.0:
        upper = inf if target_probability.upper > 0.0 else 0.0
    else:
        upper = target_probability.upper / nontarget_probability.lower
    return LikelihoodRatioInterval(lower, upper)


def posterior_interval_from_lr_bounds(
    prior: float,
    likelihood_ratio: LikelihoodRatioInterval,
) -> ProbabilityInterval:
    """Transform likelihood-ratio bounds into posterior-probability bounds."""
    if not 0.0 < prior < 1.0:
        raise ValueError("prior must lie strictly between 0 and 1")

    prior_odds = prior / (1.0 - prior)

    def update(lr: float) -> float:
        if lr == 0.0:
            return 0.0
        if lr == inf:
            return 1.0
        posterior_odds = prior_odds * lr
        return posterior_odds / (1.0 + posterior_odds)

    return ProbabilityInterval(update(likelihood_ratio.lower), update(likelihood_ratio.upper))


def fuse_unknown_dependence(
    prior: float,
    observations: Sequence[tuple[EvidenceChannel, bool]],
) -> DependenceRobustFusion:
    """Fuse calibrated binary channels without assuming conditional independence.

    Only each channel's sensitivity and specificity are used. Dependence among
    channels is otherwise unrestricted under both target-present and
    target-absent conditions. The output can therefore be broad or fully vacuous;
    that width is an identification result, not a software failure.
    """
    target_probability, nontarget_probability = conditional_pattern_probability_bounds(
        observations
    )
    lr = likelihood_ratio_bounds(target_probability, nontarget_probability)
    posterior = posterior_interval_from_lr_bounds(prior, lr)
    return DependenceRobustFusion(
        target_pattern_probability=target_probability,
        nontarget_pattern_probability=nontarget_probability,
        likelihood_ratio=lr,
        posterior=posterior,
    )
