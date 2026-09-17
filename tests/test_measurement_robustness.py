from math import isclose

import pytest

from consciousness_measurement.latent_measurement import CalibrationBox, RateInterval
from consciousness_measurement.measurement_robustness import (
    inverse_slope_amplification,
    joint_finite_sample_prevalence_outer_interval,
    local_inversion_sensitivities,
    missingness_proxy_rate_bounds,
    missingness_robust_prevalence_outer_interval,
    pooled_two_site_proxy_rate,
    two_site_average_prevalence_identified_interval,
)


def test_joint_finite_sample_interval_contains_canonical_truth() -> None:
    interval = joint_finite_sample_prevalence_outer_interval(
        proxy_successes=419,
        proxy_trials=1000,
        sensitivity_successes=840,
        sensitivity_trials=1000,
        specificity_successes=910,
        specificity_trials=1000,
        delta=0.05,
    )
    assert interval.lower <= 0.40 <= interval.upper


def test_missingness_proxy_bounds_are_sharp_extremes() -> None:
    bounds = missingness_proxy_rate_bounds(
        observed_positives=30,
        observed_trials=80,
        total_trials=100,
    )
    assert bounds.lower == 0.30
    assert bounds.upper == 0.50


def test_missingness_robust_interval_contains_complete_case_truth() -> None:
    calibration = CalibrationBox(RateInterval(0.84, 0.84), RateInterval(0.91, 0.91))
    interval = missingness_robust_prevalence_outer_interval(
        observed_positives=34,
        observed_trials=80,
        total_trials=100,
        calibration=calibration,
    )
    assert interval.lower <= 0.40 <= interval.upper


def test_inverse_slope_is_exact_error_amplification() -> None:
    amplification = inverse_slope_amplification(0.84, 0.91)
    assert isclose(amplification, 1.0 / 0.75, abs_tol=1e-12)


def test_local_sensitivity_derivatives_match_closed_form() -> None:
    sens = local_inversion_sensitivities(0.4, 0.84, 0.91)
    j = 0.75
    assert isclose(sens.d_prevalence_d_proxy_rate, 1 / j, abs_tol=1e-12)
    assert isclose(sens.d_prevalence_d_sensitivity, -0.4 / j, abs_tol=1e-12)
    assert isclose(sens.d_prevalence_d_specificity, 0.6 / j, abs_tol=1e-12)


def test_two_site_counterexample_has_same_pooled_proxy_rate() -> None:
    common = {
        "site1_weight": 0.5,
        "site1_sensitivity": 0.9,
        "site1_specificity": 0.9,
        "site2_sensitivity": 0.7,
        "site2_specificity": 0.8,
    }
    q_a = pooled_two_site_proxy_rate(
        site1_prevalence=0.75,
        site2_prevalence=0.0,
        **common,
    )
    q_b = pooled_two_site_proxy_rate(
        site1_prevalence=0.125,
        site2_prevalence=1.0,
        **common,
    )
    assert isclose(q_a, q_b, abs_tol=1e-12)
    assert not isclose(0.375, 0.5625, abs_tol=1e-12)


def test_two_site_identified_set_contains_both_counterexample_averages() -> None:
    identified = two_site_average_prevalence_identified_interval(
        pooled_proxy_rate=0.45,
        site1_weight=0.5,
        site1_sensitivity=0.9,
        site1_specificity=0.9,
        site2_sensitivity=0.7,
        site2_specificity=0.8,
    )
    assert identified.lower - 1e-12 <= 0.375 <= identified.upper + 1e-12
    assert identified.lower - 1e-12 <= 0.5625 <= identified.upper + 1e-12
    assert identified.width > 0.18


def test_incompatible_two_site_proxy_rate_is_rejected() -> None:
    with pytest.raises(ValueError):
        two_site_average_prevalence_identified_interval(
            pooled_proxy_rate=0.99,
            site1_weight=0.5,
            site1_sensitivity=0.9,
            site1_specificity=0.9,
            site2_sensitivity=0.7,
            site2_specificity=0.8,
        )
