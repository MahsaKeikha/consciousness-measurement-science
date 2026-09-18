from __future__ import annotations

import math

import numpy as np

from .electromagnetic_design import (
    cross_talk_function,
    d_optimal_log_information,
    e_optimal_information,
    fisher_information_matrix,
    mahalanobis_topography_distance,
    point_spread_function,
    retained_target_information_fraction,
    robust_whitened_information_lower_bound,
    worst_case_whitened_perturbation,
)


def v31_point_spread_cross_talk() -> dict[str, float | list[float]]:
    resolution = np.asarray(
        [
            [0.80, 0.10, 0.00, 0.00],
            [0.20, 0.70, 0.20, 0.00],
            [0.00, 0.10, 0.75, 0.15],
            [0.05, 0.00, 0.25, 0.70],
        ]
    )
    source_index = 1
    point_spread = point_spread_function(resolution, source_index)
    cross_talk = cross_talk_function(resolution, source_index)
    point_spread_off_diagonal = point_spread.copy()
    point_spread_off_diagonal[source_index] = 0.0
    cross_talk_off_diagonal = cross_talk.copy()
    cross_talk_off_diagonal[source_index] = 0.0
    return {
        "source_index": float(source_index),
        "point_spread": point_spread.tolist(),
        "cross_talk": cross_talk.tolist(),
        "point_spread_leakage_norm": float(np.linalg.norm(point_spread_off_diagonal)),
        "cross_talk_leakage_norm": float(np.linalg.norm(cross_talk_off_diagonal)),
    }


def v32_noise_aware_source_distinguishability() -> list[dict[str, float | str]]:
    reference = np.asarray([1.0, 0.2, 0.1])
    close = np.asarray([0.95, 0.18, 0.12])
    distinct = np.asarray([0.1, 1.0, -0.3])
    covariance = np.asarray(
        [
            [1.0, 0.3, 0.1],
            [0.3, 1.0, 0.2],
            [0.1, 0.2, 1.0],
        ]
    )
    return [
        {
            "comparison": "close",
            "mahalanobis_distance_squared": mahalanobis_topography_distance(
                reference,
                close,
                covariance,
            ),
        },
        {
            "comparison": "distinct",
            "mahalanobis_distance_squared": mahalanobis_topography_distance(
                reference,
                distinct,
                covariance,
            ),
        },
    ]


def v33_sensor_design_information() -> list[dict[str, float | str]]:
    candidate_designs = {
        "redundant": np.asarray(
            [
                [1.0, 0.0],
                [1.0, 0.02],
                [1.0, -0.02],
            ]
        ),
        "complementary": np.asarray(
            [
                [1.0, 0.0],
                [0.0, 1.0],
                [2.0**-0.5, 2.0**-0.5],
            ]
        ),
    }
    covariance = np.eye(3)
    rows: list[dict[str, float | str]] = []
    for name, sensitivity in candidate_designs.items():
        information = fisher_information_matrix(sensitivity, covariance)
        rows.append(
            {
                "design": name,
                "determinant": float(np.linalg.det(information)),
                "log_determinant": d_optimal_log_information(information),
                "minimum_eigenvalue": e_optimal_information(information),
                "trace": float(np.trace(information)),
            }
        )
    return rows


def v34_nuisance_subspace_information_loss() -> list[dict[str, float]]:
    target = np.asarray([1.0, 0.0, 0.0])
    rows: list[dict[str, float]] = []
    for angle_degrees in (0.0, 15.0, 30.0, 45.0, 60.0, 90.0):
        angle = math.radians(angle_degrees)
        nuisance = np.asarray(
            [
                [math.cos(angle)],
                [math.sin(angle)],
                [0.0],
            ]
        )
        rows.append(
            {
                "angle_degrees": angle_degrees,
                "retained_information_fraction": retained_target_information_fraction(
                    target,
                    nuisance,
                ),
                "sin_squared_angle": math.sin(angle) ** 2,
            }
        )
    return rows


def v35_robust_information_under_model_uncertainty() -> list[dict[str, float]]:
    topography = np.asarray([1.0, 0.5, -0.2])
    nominal_information = float(topography @ topography)
    rows: list[dict[str, float]] = []
    for radius in (0.0, 0.2, 0.5, 1.0, 1.2):
        perturbation = worst_case_whitened_perturbation(topography, radius)
        realized = topography + perturbation
        rows.append(
            {
                "uncertainty_radius": radius,
                "nominal_information": nominal_information,
                "robust_information_lower_bound": robust_whitened_information_lower_bound(
                    topography,
                    radius,
                ),
                "realized_worst_case_information": float(realized @ realized),
                "realized_perturbation_norm": float(np.linalg.norm(perturbation)),
            }
        )
    return rows
