from __future__ import annotations

import numpy as np
import pytest

from consciousness_measurement.electromagnetic_design import (
    cross_talk_function,
    d_optimal_log_information,
    e_optimal_information,
    fisher_information_matrix,
    mahalanobis_topography_distance,
    orthogonal_complement_projector,
    point_spread_function,
    retained_target_information_fraction,
    robust_whitened_information_lower_bound,
    worst_case_whitened_perturbation,
)


def test_point_spread_and_cross_talk_are_resolution_column_and_row() -> None:
    resolution = np.asarray(
        [
            [0.8, 0.1, 0.0],
            [0.2, 0.7, 0.3],
            [0.0, 0.4, 0.6],
        ]
    )
    assert point_spread_function(resolution, 1) == pytest.approx([0.1, 0.7, 0.4])
    assert cross_talk_function(resolution, 1) == pytest.approx([0.2, 0.7, 0.3])


def test_mahalanobis_topography_distance_uses_noise_geometry() -> None:
    first = np.asarray([1.0, 0.0])
    second = np.asarray([0.0, 1.0])
    covariance = np.asarray([[1.0, 0.5], [0.5, 1.0]])
    expected = float((first - second) @ np.linalg.solve(covariance, first - second))
    assert mahalanobis_topography_distance(first, second, covariance) == pytest.approx(expected)
    assert mahalanobis_topography_distance(first, first, covariance) == pytest.approx(0.0)


def test_fisher_information_supports_d_and_e_optimality() -> None:
    sensitivity = np.asarray([[1.0, 0.0], [0.0, 1.0], [1.0, 1.0]])
    information = fisher_information_matrix(sensitivity, np.eye(3))
    assert information == pytest.approx(np.asarray([[2.0, 1.0], [1.0, 2.0]]))
    assert d_optimal_log_information(information) == pytest.approx(np.log(3.0))
    assert e_optimal_information(information) == pytest.approx(1.0)


def test_nuisance_projection_has_exact_aligned_and_orthogonal_limits() -> None:
    target = np.asarray([1.0, 0.0, 0.0])
    aligned = np.asarray([[1.0], [0.0], [0.0]])
    orthogonal = np.asarray([[0.0], [1.0], [0.0]])
    aligned_projector = orthogonal_complement_projector(aligned)
    assert aligned_projector @ target == pytest.approx(np.zeros(3))
    assert retained_target_information_fraction(target, aligned) == pytest.approx(0.0)
    assert retained_target_information_fraction(target, orthogonal) == pytest.approx(1.0)


def test_robust_information_bound_is_attained_by_anti_aligned_perturbation() -> None:
    topography = np.asarray([1.0, 0.5, -0.2])
    radius = 0.5
    perturbation = worst_case_whitened_perturbation(topography, radius)
    realized = topography + perturbation
    bound = robust_whitened_information_lower_bound(topography, radius)
    assert np.linalg.norm(perturbation) == pytest.approx(radius)
    assert float(realized @ realized) == pytest.approx(bound)


def test_robust_information_collapses_when_uncertainty_covers_nominal_vector() -> None:
    topography = np.asarray([1.0, 0.5, -0.2])
    radius = float(np.linalg.norm(topography)) + 0.1
    assert robust_whitened_information_lower_bound(topography, radius) == pytest.approx(0.0)
    perturbation = worst_case_whitened_perturbation(topography, radius)
    assert topography + perturbation == pytest.approx(np.zeros(3))
