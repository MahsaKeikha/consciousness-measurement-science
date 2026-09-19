from __future__ import annotations

import numpy as np
import pytest

from consciousness_measurement.transportability import (
    bounded_expectation_shift_bound,
    gls_scalar_amplitude_estimate,
    importance_weighted_expectation,
    population_effective_sample_fraction,
    projected_scalar_information,
    scalar_amplitude_information,
    total_variation_distance,
    transformed_sensor_model,
)


def _canonical_model() -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    covariance = np.asarray(
        [
            [2.0, 0.6, 0.2],
            [0.6, 1.5, 0.3],
            [0.2, 0.3, 1.0],
        ]
    )
    topography = np.asarray([1.0, 0.4, -0.2])
    observation = np.asarray([0.8, 0.3, -0.1])
    return observation, topography, covariance


def test_invertible_sensor_transform_preserves_gls_estimate_and_information() -> None:
    observation, topography, covariance = _canonical_model()
    transform = np.asarray(
        [
            [1.0, 1.0, 0.0],
            [0.0, 1.0, 0.5],
            [0.2, 0.0, 1.0],
        ]
    )
    transformed_observation, transformed_topography, transformed_covariance = (
        transformed_sensor_model(
            observation,
            topography,
            covariance,
            transform,
        )
    )
    assert gls_scalar_amplitude_estimate(
        transformed_observation,
        transformed_topography,
        transformed_covariance,
    ) == pytest.approx(gls_scalar_amplitude_estimate(observation, topography, covariance))
    assert scalar_amplitude_information(
        transformed_topography,
        transformed_covariance,
    ) == pytest.approx(scalar_amplitude_information(topography, covariance))


def test_lossy_projection_cannot_increase_scalar_fisher_information() -> None:
    _, topography, covariance = _canonical_model()
    full_information = scalar_amplitude_information(topography, covariance)
    projections = (
        np.asarray([[1.0, 0.0, 0.0], [0.0, 1.0, 0.0]]),
        np.asarray([[1.0, 1.0, 0.0]]),
    )
    for projection in projections:
        assert projected_scalar_information(
            topography,
            covariance,
            projection,
        ) <= full_information + 1e-12


def test_importance_weighting_recovers_target_expectation_under_covariate_shift() -> None:
    source = np.asarray([0.5, 0.3, 0.2])
    target = np.asarray([0.2, 0.3, 0.5])
    values = np.asarray([0.0, 0.4, 1.0])
    assert importance_weighted_expectation(values, source, target) == pytest.approx(
        float(np.dot(target, values))
    )


def test_importance_weight_concentration_reduces_effective_sample_fraction() -> None:
    source = np.asarray([0.5, 0.3, 0.2])
    mild = np.asarray([0.4, 0.3, 0.3])
    severe = np.asarray([0.1, 0.3, 0.6])
    assert population_effective_sample_fraction(source, mild) == pytest.approx(
        0.9345794392523362
    )
    assert population_effective_sample_fraction(source, severe) == pytest.approx(
        0.47169811320754707
    )


def test_total_variation_bound_is_sharp_for_declared_bounded_outcome() -> None:
    source = np.asarray([0.5, 0.3, 0.2])
    target = np.asarray([0.2, 0.3, 0.5])
    values = np.asarray([0.0, 0.4, 1.0])
    actual_shift = abs(float(np.dot(target - source, values)))
    assert total_variation_distance(source, target) == pytest.approx(0.3)
    assert bounded_expectation_shift_bound(0.0, 1.0, source, target) == pytest.approx(
        actual_shift
    )
