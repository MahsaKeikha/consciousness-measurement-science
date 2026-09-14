from math import inf

import pytest

from consciousness_measurement.evidence import (
    EvidenceChannel,
    fuse_independent_channels,
    posterior_from_lr,
)
from consciousness_measurement.partial_identification import (
    LikelihoodRatioInterval,
    ProbabilityInterval,
    conditional_pattern_probability_bounds,
    frechet_intersection_bounds,
    fuse_unknown_dependence,
    likelihood_ratio_bounds,
    posterior_interval_from_lr_bounds,
)


def test_frechet_intersection_bounds_are_sharp_from_marginals():
    interval = frechet_intersection_bounds([0.8, 0.75, 0.9])
    assert interval.lower == pytest.approx(0.45)
    assert interval.upper == pytest.approx(0.75)


def test_empty_intersection_has_probability_one():
    assert frechet_intersection_bounds([]) == ProbabilityInterval(1.0, 1.0)


def test_conditional_pattern_bounds_use_observed_signs():
    first = EvidenceChannel("first", sensitivity=0.8, specificity=0.9)
    second = EvidenceChannel("second", sensitivity=0.75, specificity=0.8)

    target, nontarget = conditional_pattern_probability_bounds(
        [(first, True), (second, False)]
    )

    assert target.lower == pytest.approx(0.05)
    assert target.upper == pytest.approx(0.25)
    assert nontarget.lower == pytest.approx(0.0)
    assert nontarget.upper == pytest.approx(0.1)


def test_single_channel_robust_fusion_matches_ordinary_bayes_update():
    channel = EvidenceChannel("test", sensitivity=0.8, specificity=0.9)
    result = fuse_unknown_dependence(0.25, [(channel, True)])
    expected = posterior_from_lr(0.25, channel.likelihood_ratio(True))

    assert result.posterior.lower == pytest.approx(expected)
    assert result.posterior.upper == pytest.approx(expected)
    assert not result.is_vacuous


def test_independence_result_lies_inside_unknown_dependence_interval():
    first = EvidenceChannel("first", sensitivity=0.8, specificity=0.9)
    second = EvidenceChannel("second", sensitivity=0.75, specificity=0.8)
    observations = [(first, True), (second, True)]

    _, independent_posterior = fuse_independent_channels(0.25, observations)
    robust = fuse_unknown_dependence(0.25, observations)

    assert robust.likelihood_ratio.lower == pytest.approx(5.5)
    assert robust.likelihood_ratio.upper == inf
    assert robust.posterior.lower < independent_posterior < robust.posterior.upper


def test_unknown_dependence_can_make_marginal_evidence_nonidentifying():
    channels = [
        EvidenceChannel(f"channel-{index}", sensitivity=0.5, specificity=0.5)
        for index in range(3)
    ]
    result = fuse_unknown_dependence(0.4, [(channel, True) for channel in channels])

    assert result.likelihood_ratio == LikelihoodRatioInterval(0.0, inf)
    assert result.posterior == ProbabilityInterval(0.0, 1.0)
    assert result.is_vacuous


def test_posterior_interval_maps_zero_and_infinite_likelihood_ratio_bounds():
    posterior = posterior_interval_from_lr_bounds(
        0.3,
        LikelihoodRatioInterval(0.0, inf),
    )
    assert posterior == ProbabilityInterval(0.0, 1.0)


def test_likelihood_ratio_bounds_reject_impossible_nontarget_pattern():
    with pytest.raises(ValueError, match="identically zero"):
        likelihood_ratio_bounds(
            ProbabilityInterval(0.2, 0.4),
            ProbabilityInterval(0.0, 0.0),
        )


@pytest.mark.parametrize(
    "probabilities",
    [
        [-0.1, 0.5],
        [0.4, 1.1],
        [0.4, float("nan")],
    ],
)
def test_frechet_bounds_reject_invalid_marginals(probabilities):
    with pytest.raises(ValueError):
        frechet_intersection_bounds(probabilities)
