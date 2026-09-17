from math import isclose

import pytest

from consciousness_measurement.latent_measurement import (
    CalibrationBox,
    RateInterval,
    calibration_box_prevalence_outer_interval,
    finite_sample_prevalence_outer_interval,
    latent_effect_from_proxy_effect,
    latent_prevalence_from_proxy_rate,
    proxy_rate_from_latent_prevalence,
    transport_bias_from_calibration_shift,
)


def test_point_identification_inverts_measurement_channel() -> None:
    prevalence = 0.37
    sensitivity = 0.84
    specificity = 0.91
    q = proxy_rate_from_latent_prevalence(prevalence, sensitivity, specificity)
    recovered = latent_prevalence_from_proxy_rate(q, sensitivity, specificity)
    assert isclose(recovered, prevalence, rel_tol=0.0, abs_tol=1e-12)


def test_calibration_outer_interval_contains_every_grid_consistent_point() -> None:
    q_box = RateInterval(0.31, 0.37)
    cal = CalibrationBox(RateInterval(0.78, 0.86), RateInterval(0.84, 0.92))
    outer = calibration_box_prevalence_outer_interval(q_box, cal)

    for q in (0.31, 0.33, 0.35, 0.37):
        for sensitivity in (0.78, 0.80, 0.83, 0.86):
            for specificity in (0.84, 0.87, 0.90, 0.92):
                j = sensitivity + specificity - 1.0
                prevalence = (q + specificity - 1.0) / j
                if 0.0 <= prevalence <= 1.0:
                    assert outer.lower <= prevalence <= outer.upper


def test_finite_sample_interval_contains_truth_for_expected_count() -> None:
    prevalence = 0.40
    sensitivity = 0.85
    specificity = 0.90
    q = proxy_rate_from_latent_prevalence(prevalence, sensitivity, specificity)
    n = 10_000
    successes = round(q * n)
    cal = CalibrationBox(RateInterval(0.83, 0.87), RateInterval(0.88, 0.92))
    interval = finite_sample_prevalence_outer_interval(successes, n, cal, delta=0.05)
    assert interval.lower <= prevalence <= interval.upper


def test_invariant_calibration_recovers_latent_contrast() -> None:
    sensitivity = 0.82
    specificity = 0.93
    latent_delta = 0.18
    j = sensitivity + specificity - 1.0
    proxy_delta = j * latent_delta
    assert isclose(
        latent_effect_from_proxy_effect(proxy_delta, sensitivity, specificity),
        latent_delta,
        abs_tol=1e-12,
    )


def test_transport_bias_formula_matches_direct_two_condition_calculation() -> None:
    pi0 = 0.25
    pi1 = 0.55
    se0, sp0 = 0.84, 0.91
    se1, sp1 = 0.78, 0.88
    q0 = proxy_rate_from_latent_prevalence(pi0, se0, sp0)
    q1 = proxy_rate_from_latent_prevalence(pi1, se1, sp1)
    estimated_delta = latent_effect_from_proxy_effect(q1 - q0, se0, sp0)
    true_delta = pi1 - pi0
    direct_bias = estimated_delta - true_delta
    analytic_bias = transport_bias_from_calibration_shift(pi1, se0, sp0, se1, sp1)
    assert isclose(direct_bias, analytic_bias, abs_tol=1e-12)


def test_noninformative_calibration_is_rejected() -> None:
    with pytest.raises(ValueError):
        latent_prevalence_from_proxy_rate(0.5, 0.5, 0.5)
