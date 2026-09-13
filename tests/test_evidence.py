import pytest

from consciousness_measurement.evidence import (
    EvidenceChannel,
    fuse_independent_channels,
    posterior_from_lr,
)


def test_likelihood_ratios_are_computed_from_calibration():
    channel = EvidenceChannel("test", sensitivity=0.8, specificity=0.9)
    assert channel.likelihood_ratio(True) == pytest.approx(8.0)
    assert channel.likelihood_ratio(False) == pytest.approx(2.0 / 9.0)


def test_posterior_from_lr_updates_odds():
    posterior = posterior_from_lr(prior=0.5, likelihood_ratio=4.0)
    assert posterior == pytest.approx(0.8)


def test_fusion_multiplies_likelihood_ratios_under_declared_assumption():
    first = EvidenceChannel("first", sensitivity=0.8, specificity=0.9)
    second = EvidenceChannel("second", sensitivity=0.75, specificity=0.8)
    combined_lr, posterior = fuse_independent_channels(
        prior=0.25,
        observations=[(first, True), (second, False)],
    )
    expected_lr = first.likelihood_ratio(True) * second.likelihood_ratio(False)
    assert combined_lr == pytest.approx(expected_lr)
    assert 0.0 < posterior < 1.0


@pytest.mark.parametrize(
    ("sensitivity", "specificity"),
    [
        (0.0, 0.9),
        (1.0, 0.9),
        (0.8, 0.0),
        (0.8, 1.0),
    ],
)
def test_channel_rejects_degenerate_calibration(sensitivity, specificity):
    with pytest.raises(ValueError):
        EvidenceChannel("bad", sensitivity=sensitivity, specificity=specificity)


def test_posterior_rejects_invalid_inputs():
    with pytest.raises(ValueError):
        posterior_from_lr(0.0, 2.0)
    with pytest.raises(ValueError):
        posterior_from_lr(0.5, 0.0)
