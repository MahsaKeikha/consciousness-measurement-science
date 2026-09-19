from __future__ import annotations

import numpy as np

from . import transportability

COVARIANCE = np.asarray(
    [
        [2.0, 0.6, 0.2],
        [0.6, 1.5, 0.3],
        [0.2, 0.3, 1.0],
    ]
)
TOPOGRAPHY = np.asarray([1.0, 0.4, -0.2])
OBSERVATION = np.asarray([0.8, 0.3, -0.1])


def v51_invertible_sensor_coordinate_invariance() -> dict[str, float]:
    transform = np.asarray(
        [
            [1.0, 1.0, 0.0],
            [0.0, 1.0, 0.5],
            [0.2, 0.0, 1.0],
        ]
    )
    transformed_observation, transformed_topography, transformed_covariance = (
        transportability.transformed_sensor_model(
            OBSERVATION,
            TOPOGRAPHY,
            COVARIANCE,
            transform,
        )
    )
    original_information = transportability.scalar_amplitude_information(
        TOPOGRAPHY,
        COVARIANCE,
    )
    transformed_information = transportability.scalar_amplitude_information(
        transformed_topography,
        transformed_covariance,
    )
    original_estimate = transportability.gls_scalar_amplitude_estimate(
        OBSERVATION,
        TOPOGRAPHY,
        COVARIANCE,
    )
    transformed_estimate = transportability.gls_scalar_amplitude_estimate(
        transformed_observation,
        transformed_topography,
        transformed_covariance,
    )
    return {
        "transform_determinant": float(np.linalg.det(transform)),
        "original_information": original_information,
        "transformed_information": transformed_information,
        "absolute_information_difference": abs(
            transformed_information - original_information
        ),
        "original_gls_estimate": original_estimate,
        "transformed_gls_estimate": transformed_estimate,
        "absolute_estimate_difference": abs(transformed_estimate - original_estimate),
    }


def v52_projection_information_monotonicity() -> list[dict[str, float | str]]:
    baseline = transportability.scalar_amplitude_information(TOPOGRAPHY, COVARIANCE)
    projections = {
        "all_sensors": np.eye(3),
        "drop_sensor_3": np.asarray(
            [
                [1.0, 0.0, 0.0],
                [0.0, 1.0, 0.0],
            ]
        ),
        "single_mixed_channel": np.asarray([[1.0, 1.0, 0.0]]),
    }
    rows: list[dict[str, float | str]] = []
    for name, projection in projections.items():
        information = transportability.projected_scalar_information(
            TOPOGRAPHY,
            COVARIANCE,
            projection,
        )
        rows.append(
            {
                "projection": name,
                "retained_information": information,
                "information_fraction": information / baseline,
                "information_loss": baseline - information,
            }
        )
    return rows


def v53_cross_hardware_topography_mismatch() -> list[dict[str, float]]:
    weight = np.linalg.inv(COVARIANCE)
    mismatch_direction = np.asarray([0.2, -0.6, 0.7])
    mismatch_direction /= np.sqrt(mismatch_direction @ weight @ mismatch_direction)
    rows: list[dict[str, float]] = []
    for mismatch_norm in (0.0, 0.05, 0.10, 0.20, 0.40):
        true_topography = TOPOGRAPHY + mismatch_norm * mismatch_direction
        gain = transportability.mismatched_topography_gain(
            TOPOGRAPHY,
            true_topography,
            weight,
        )
        bound = transportability.mismatched_topography_relative_bias_bound(
            TOPOGRAPHY,
            true_topography,
            weight,
        )
        rows.append(
            {
                "whitened_mismatch_norm": mismatch_norm,
                "expected_amplitude_gain": gain,
                "relative_bias": gain - 1.0,
                "absolute_relative_bias": abs(gain - 1.0),
                "cauchy_schwarz_bias_bound": bound,
            }
        )
    return rows


def _shifted_target(alpha: float) -> np.ndarray:
    return np.asarray([0.5 - alpha, 0.3, 0.2 + alpha])


def v54_importance_weighted_transport() -> list[dict[str, float]]:
    source = np.asarray([0.5, 0.3, 0.2])
    values = np.asarray([0.0, 0.4, 1.0])
    rows: list[dict[str, float]] = []
    for alpha in (0.0, 0.10, 0.20, 0.30, 0.40):
        target = _shifted_target(alpha)
        target_expectation = float(np.dot(target, values))
        weighted_expectation = transportability.importance_weighted_expectation(
            values,
            source,
            target,
        )
        weights = transportability.importance_weights(source, target)
        rows.append(
            {
                "shift_alpha": alpha,
                "target_expectation": target_expectation,
                "importance_weighted_source_expectation": weighted_expectation,
                "absolute_transport_identity_error": abs(
                    weighted_expectation - target_expectation
                ),
                "maximum_importance_weight": float(np.max(weights)),
                "effective_sample_fraction": (
                    transportability.population_effective_sample_fraction(
                        source,
                        target,
                    )
                ),
            }
        )
    return rows


def v55_total_variation_transport_budget() -> list[dict[str, float]]:
    source = np.asarray([0.5, 0.3, 0.2])
    values = np.asarray([0.0, 0.4, 1.0])
    source_expectation = float(np.dot(source, values))
    rows: list[dict[str, float]] = []
    for alpha in (0.0, 0.10, 0.20, 0.30, 0.40):
        target = _shifted_target(alpha)
        target_expectation = float(np.dot(target, values))
        actual_shift = abs(target_expectation - source_expectation)
        tv = transportability.total_variation_distance(source, target)
        bound = transportability.bounded_expectation_shift_bound(
            0.0,
            1.0,
            source,
            target,
        )
        rows.append(
            {
                "shift_alpha": alpha,
                "total_variation": tv,
                "actual_expectation_shift": actual_shift,
                "sharp_tv_bound": bound,
                "bound_slack": bound - actual_shift,
            }
        )
    return rows
