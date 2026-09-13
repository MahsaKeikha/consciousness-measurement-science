"""Transparent evidence-fusion scaffolds.

These functions are pedagogical/research tools, not clinical classifiers.
Conditional independence of channels is a strong explicit assumption.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import prod


@dataclass(frozen=True)
class EvidenceChannel:
    """Binary-test calibration for a declared validation context."""

    name: str
    sensitivity: float
    specificity: float

    def __post_init__(self) -> None:
        if not 0 < self.sensitivity < 1:
            raise ValueError("sensitivity must lie strictly between 0 and 1")
        if not 0 < self.specificity < 1:
            raise ValueError("specificity must lie strictly between 0 and 1")

    def likelihood_ratio(self, positive: bool) -> float:
        """Return LR+ for positive evidence or LR- for negative evidence."""
        if positive:
            return self.sensitivity / (1.0 - self.specificity)
        return (1.0 - self.sensitivity) / self.specificity


def posterior_from_lr(prior: float, likelihood_ratio: float) -> float:
    """Bayes update from prior probability and a likelihood ratio."""
    if not 0 < prior < 1:
        raise ValueError("prior must lie strictly between 0 and 1")
    if likelihood_ratio <= 0:
        raise ValueError("likelihood ratio must be positive")
    prior_odds = prior / (1.0 - prior)
    posterior_odds = prior_odds * likelihood_ratio
    return posterior_odds / (1.0 + posterior_odds)


def fuse_independent_channels(
    prior: float,
    observations: list[tuple[EvidenceChannel, bool]],
) -> tuple[float, float]:
    """Fuse calibrated binary channels under conditional independence.

    Returns (combined_likelihood_ratio, posterior_probability).
    The result is assumption-bound and should not be called a direct
    probability of consciousness unless the latent model has been validated.
    """
    combined_lr = prod(channel.likelihood_ratio(value) for channel, value in observations)
    return combined_lr, posterior_from_lr(prior, combined_lr)
