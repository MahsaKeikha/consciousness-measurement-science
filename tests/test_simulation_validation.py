from consciousness_measurement.evidence import EvidenceChannel
from consciousness_measurement.partial_identification import fuse_unknown_dependence
from consciousness_measurement.simulation_validation import (
    ChannelCalibration,
    dependence_stress_experiment,
    exact_all_positive_posterior_with_shared_uniform_dependence,
    finite_sample_coverage_experiment,
    naive_independence_all_positive_posterior,
    structural_alignment_power_experiment,
    transport_stress_experiment,
)


def test_dependence_zero_matches_naive_independence() -> None:
    channels = (
        ChannelCalibration(0.80, 0.90),
        ChannelCalibration(0.85, 0.88),
        ChannelCalibration(0.78, 0.92),
    )
    exact = exact_all_positive_posterior_with_shared_uniform_dependence(0.35, channels, 0.0)
    naive = naive_independence_all_positive_posterior(0.35, channels)
    assert abs(exact - naive) < 1e-12


def test_positive_dependence_exposes_naive_overconfidence_for_example_channels() -> None:
    channels = (
        ChannelCalibration(0.80, 0.90),
        ChannelCalibration(0.85, 0.88),
        ChannelCalibration(0.78, 0.92),
    )
    rows = dependence_stress_experiment(
        prior=0.35,
        channels=channels,
        dependence_grid=(0.0, 0.25, 0.50, 0.75, 1.0),
    )
    assert rows[-1]["absolute_error"] > rows[1]["absolute_error"]


def test_coverage_experiment_is_reproducible_and_conservative() -> None:
    kwargs = dict(
        prevalence=0.40,
        sensitivity=0.84,
        specificity=0.91,
        calibration_half_width=0.02,
        sample_sizes=(100, 500),
        repetitions=400,
        delta=0.05,
        seed=20260917,
    )
    a = finite_sample_coverage_experiment(**kwargs)
    b = finite_sample_coverage_experiment(**kwargs)
    assert a == b
    assert all(row["coverage"] >= 0.94 for row in a)
    assert a[1]["mean_width"] < a[0]["mean_width"]


def test_transport_grid_has_zero_bias_at_zero_shift() -> None:
    rows = transport_stress_experiment(
        latent_prevalence_after=0.55,
        baseline_sensitivity=0.84,
        baseline_specificity=0.91,
        sensitivity_shifts=(-0.05, 0.0, 0.05),
        specificity_shifts=(-0.05, 0.0, 0.05),
    )
    zero = next(
        row for row in rows
        if row["sensitivity_shift"] == 0.0 and row["specificity_shift"] == 0.0
    )
    assert abs(zero["bias"]) < 1e-12


def test_structural_alignment_battery_separates_null_and_signal() -> None:
    rows = structural_alignment_power_experiment(
        signal_levels=(0.0, 0.5, 0.9),
        replicates=30,
        items=18,
        dimensions=3,
        permutations=99,
        alpha=0.05,
        seed=20260917,
    )
    assert rows[0]["rejection_rate"] <= 0.20
    assert rows[-1]["rejection_rate"] >= 0.80
    assert rows[-1]["mean_alignment"] > rows[1]["mean_alignment"] > rows[0]["mean_alignment"]


def test_exact_dependence_family_stays_inside_frechet_robust_posterior_interval() -> None:
    channels = (
        ChannelCalibration(0.80, 0.90),
        ChannelCalibration(0.85, 0.88),
        ChannelCalibration(0.78, 0.92),
    )
    evidence_channels = tuple(
        EvidenceChannel(f"channel_{index}", channel.sensitivity, channel.specificity)
        for index, channel in enumerate(channels)
    )
    robust = fuse_unknown_dependence(
        0.35,
        [(channel, True) for channel in evidence_channels],
    )
    for dependence in (0.0, 0.25, 0.50, 0.75, 1.0):
        exact = exact_all_positive_posterior_with_shared_uniform_dependence(
            0.35,
            channels,
            dependence,
        )
        assert robust.posterior.lower <= exact <= robust.posterior.upper
