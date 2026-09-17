from __future__ import annotations

from math import log, sqrt

import pytest

from consciousness_measurement.identification_design import (
    hoeffding_resolution_sample_size,
    independent_gate_preserves_conditional_coverage,
    interior_missingness_width,
    missingness_resolution_interval_known_calibration,
    multisite_average_prevalence_identified_interval,
    pooled_average_is_point_identified,
    pooled_average_prevalence_if_identified,
)
from consciousness_measurement.measurement_robustness import (
    two_site_average_prevalence_identified_interval,
)


def test_v11_missingness_width_is_exact_in_the_interior() -> None:
    interval = missingness_resolution_interval_known_calibration(
        observed_positives=400,
        observed_trials=800,
        total_trials=1000,
        sensitivity=0.9,
        specificity=0.9,
    )
    assert interval.lower == pytest.approx(0.375)
    assert interval.upper == pytest.approx(0.625)
    assert interval.width == pytest.approx(
        interior_missingness_width(
            missing_trials=200,
            total_trials=1000,
            sensitivity=0.9,
            specificity=0.9,
        )
    )
    assert interval.width == pytest.approx(0.20 / 0.80)


def test_v11_clips_only_at_the_latent_parameter_boundary() -> None:
    interval = missingness_resolution_interval_known_calibration(
        observed_positives=0,
        observed_trials=800,
        total_trials=1000,
        sensitivity=0.9,
        specificity=0.9,
    )
    assert interval.lower == pytest.approx(0.0)
    assert interval.upper == pytest.approx(0.125)


def test_v12_equal_youden_margins_are_sufficient_for_pooled_average_identification() -> None:
    weights = (0.4, 0.6)
    sensitivities = (0.9, 0.8)
    specificities = (0.8, 0.9)
    assert pooled_average_is_point_identified(
        weights=weights,
        sensitivities=sensitivities,
        specificities=specificities,
    )

    prevalence = (0.25, 0.75)
    j = 0.7
    intercept = 0.4 * 0.2 + 0.6 * 0.1
    average = 0.4 * prevalence[0] + 0.6 * prevalence[1]
    pooled_q = intercept + j * average
    recovered = pooled_average_prevalence_if_identified(
        pooled_proxy_rate=pooled_q,
        weights=weights,
        sensitivities=sensitivities,
        specificities=specificities,
    )
    assert recovered == pytest.approx(average)


def test_v12_unequal_youden_margins_are_not_point_identified() -> None:
    assert not pooled_average_is_point_identified(
        weights=(0.5, 0.5),
        sensitivities=(0.9, 0.7),
        specificities=(0.9, 0.8),
    )
    with pytest.raises(ValueError, match="not point-identified"):
        pooled_average_prevalence_if_identified(
            pooled_proxy_rate=0.45,
            weights=(0.5, 0.5),
            sensitivities=(0.9, 0.7),
            specificities=(0.9, 0.8),
        )


def test_v13_multisite_interval_matches_existing_two_site_sharp_result() -> None:
    old = two_site_average_prevalence_identified_interval(
        pooled_proxy_rate=0.45,
        site1_weight=0.5,
        site1_sensitivity=0.9,
        site1_specificity=0.9,
        site2_sensitivity=0.7,
        site2_specificity=0.8,
    )
    new = multisite_average_prevalence_identified_interval(
        pooled_proxy_rate=0.45,
        weights=(0.5, 0.5),
        sensitivities=(0.9, 0.7),
        specificities=(0.9, 0.8),
    )
    assert new.lower == pytest.approx(old.lower)
    assert new.upper == pytest.approx(old.upper)


def test_v13_three_site_fractional_knapsack_solution_is_sharp() -> None:
    identified = multisite_average_prevalence_identified_interval(
        pooled_proxy_rate=0.30,
        weights=(0.2, 0.3, 0.5),
        sensitivities=(0.9, 0.6, 0.3),
        specificities=(0.9, 0.9, 0.9),
    )
    assert identified.lower == pytest.approx(0.28)
    assert identified.upper == pytest.approx(0.70)


def test_v13_equal_margins_collapse_the_identified_set_to_a_point() -> None:
    identified = multisite_average_prevalence_identified_interval(
        pooled_proxy_rate=0.45,
        weights=(0.2, 0.3, 0.5),
        sensitivities=(0.9, 0.8, 0.75),
        specificities=(0.8, 0.9, 0.95),
    )
    assert identified.width == pytest.approx(0.0, abs=1e-12)
    recovered = pooled_average_prevalence_if_identified(
        pooled_proxy_rate=0.45,
        weights=(0.2, 0.3, 0.5),
        sensitivities=(0.9, 0.8, 0.75),
        specificities=(0.8, 0.9, 0.95),
    )
    assert identified.lower == pytest.approx(recovered)


def test_v14_sample_size_formula_meets_predeclared_width() -> None:
    sensitivity = 0.84
    specificity = 0.91
    maximum_width = 0.10
    delta = 0.05
    n = hoeffding_resolution_sample_size(
        sensitivity=sensitivity,
        specificity=specificity,
        maximum_width=maximum_width,
        delta=delta,
    )
    j = sensitivity + specificity - 1.0
    epsilon = sqrt(log(2.0 / delta) / (2.0 * n))
    assert 2.0 * epsilon / j <= maximum_width
    if n > 1:
        previous_epsilon = sqrt(log(2.0 / delta) / (2.0 * (n - 1)))
        assert 2.0 * previous_epsilon / j > maximum_width


def test_v14_required_sample_size_grows_quadratically_as_information_weakens() -> None:
    n_strong = hoeffding_resolution_sample_size(
        sensitivity=0.9,
        specificity=0.9,
        maximum_width=0.10,
    )
    n_weak = hoeffding_resolution_sample_size(
        sensitivity=0.7,
        specificity=0.7,
        maximum_width=0.10,
    )
    assert n_weak > n_strong
    assert n_weak / n_strong == pytest.approx((0.8 / 0.4) ** 2, rel=0.01)


def test_v15_independent_pilot_gate_preserves_confirmatory_coverage() -> None:
    assert independent_gate_preserves_conditional_coverage(
        marginal_coverage=0.95,
        release_probability=0.42,
    ) == pytest.approx(0.95)


def test_v15_requires_positive_release_probability() -> None:
    with pytest.raises(ValueError, match="release_probability"):
        independent_gate_preserves_conditional_coverage(
            marginal_coverage=0.95,
            release_probability=0.0,
        )
