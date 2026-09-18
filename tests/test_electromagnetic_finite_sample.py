from __future__ import annotations

import math
from statistics import NormalDist

import numpy as np
import pytest

from consciousness_measurement.electromagnetic_finite_sample import (
    gaussian_equal_covariance_bayes_error,
    gaussian_two_sided_interval_half_width,
    gls_amplitude_estimate,
    gls_amplitude_information,
    gls_amplitude_variance,
    independent_two_sided_fwer,
    independent_two_sided_fwer_threshold,
    inverse_sample_covariance_bias_factor,
    nominal_weighted_amplitude_variance,
    weighted_amplitude_variance,
)


def test_gls_scalar_amplitude_is_unbiased_linear_estimator() -> None:
    topography = np.asarray([1.0, 0.5])
    covariance = np.asarray([[1.0, 0.2], [0.2, 0.8]])
    true_amplitude = 1.7
    measurement = true_amplitude * topography
    assert gls_amplitude_estimate(topography, measurement, covariance) == pytest.approx(
        true_amplitude
    )


def test_gls_variance_is_reciprocal_fisher_information() -> None:
    topography = np.asarray([1.0, 0.5, -0.2])
    covariance = np.asarray(
        [[1.0, 0.3, 0.1], [0.3, 0.8, 0.2], [0.1, 0.2, 0.6]]
    )
    information = gls_amplitude_information(topography, covariance)
    variance = gls_amplitude_variance(topography, covariance)
    assert information == pytest.approx(1.2766666666666668)
    assert variance == pytest.approx(0.7832898172323759)
    assert information * variance == pytest.approx(1.0)


def test_known_variance_gaussian_interval_has_standard_normal_quantile() -> None:
    variance = 4.0
    half_width = gaussian_two_sided_interval_half_width(variance, 0.95)
    expected = NormalDist().inv_cdf(0.975) * 2.0
    assert half_width == pytest.approx(expected)


def test_inverse_sample_covariance_bias_factor_matches_wishart_identity() -> None:
    assert inverse_sample_covariance_bias_factor(4, 6) == pytest.approx(6.0)
    assert inverse_sample_covariance_bias_factor(4, 10) == pytest.approx(2.0)
    assert inverse_sample_covariance_bias_factor(4, 20) == pytest.approx(4.0 / 3.0)
    assert inverse_sample_covariance_bias_factor(4, 50) == pytest.approx(10.0 / 9.0)


def test_gaussian_equal_covariance_bayes_error_has_closed_form_limits() -> None:
    assert gaussian_equal_covariance_bayes_error(0.0) == pytest.approx(0.5)
    assert gaussian_equal_covariance_bayes_error(4.0) == pytest.approx(
        NormalDist().cdf(-1.0)
    )
    assert gaussian_equal_covariance_bayes_error(9.0) == pytest.approx(
        NormalDist().cdf(-1.5)
    )


def test_independent_two_sided_fwer_threshold_is_exact() -> None:
    alpha = 0.05
    for comparisons in (1, 10, 100, 1000):
        threshold = independent_two_sided_fwer_threshold(alpha, comparisons)
        realized = independent_two_sided_fwer(threshold, comparisons)
        assert realized == pytest.approx(alpha, abs=1e-12)


def test_single_comparison_fwer_threshold_matches_standard_normal() -> None:
    threshold = independent_two_sided_fwer_threshold(0.05, 1)
    assert threshold == pytest.approx(NormalDist().inv_cdf(0.975))


def test_sandwich_variance_reduces_to_nominal_for_oracle_precision() -> None:
    topography = np.asarray([1.0, 0.4, -0.3])
    covariance = np.asarray(
        [[1.0, 0.6, 0.0], [0.6, 1.0, 0.2], [0.0, 0.2, 0.8]]
    )
    weight = np.linalg.inv(covariance)
    exact = weighted_amplitude_variance(topography, covariance, weight)
    nominal = nominal_weighted_amplitude_variance(topography, weight)
    assert exact == pytest.approx(nominal)
    assert exact == pytest.approx(0.8779761904761904)


def test_identity_weight_can_understate_true_variance_when_covariance_is_correlated() -> None:
    topography = np.asarray([1.0, 0.4, -0.3])
    covariance = np.asarray(
        [[1.0, 0.6, 0.0], [0.6, 1.0, 0.2], [0.0, 0.2, 0.8]]
    )
    weight = np.eye(3)
    exact = weighted_amplitude_variance(topography, covariance, weight)
    nominal = nominal_weighted_amplitude_variance(topography, weight)
    assert exact == pytest.approx(1.06496)
    assert nominal == pytest.approx(0.8)
    assert exact / nominal == pytest.approx(1.3312)


def test_two_sided_fwer_increases_with_comparison_count_at_fixed_threshold() -> None:
    threshold = 2.0
    one = independent_two_sided_fwer(threshold, 1)
    many = independent_two_sided_fwer(threshold, 100)
    assert 0.0 < one < many < 1.0
    assert math.isfinite(many)
