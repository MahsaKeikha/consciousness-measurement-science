"""Deterministic electromagnetic resolution experiments for V26-V30."""

from __future__ import annotations

import numpy as np

from .electromagnetic_resolution import (
    cosine_aliasing_error,
    covariance_inverse_sqrt,
    off_diagonal_leakage_fraction,
    pseudoinverse_noise_amplification,
    pseudoinverse_operator_norm,
    resolution_identity_error,
    resolution_matrix,
    scalar_amplitude_crlb,
    scalar_amplitude_fisher_information,
    weighted_residual_energy,
)


def v26_correlated_noise_whitening() -> dict[str, float]:
    lead_field = np.asarray(
        [
            [1.0, 0.2],
            [0.3, 1.0],
            [0.7, -0.2],
        ]
    )
    source = np.asarray([1.0, -0.4])
    residual = np.asarray([0.10, -0.05, 0.08])
    measurement = lead_field @ source + residual
    covariance = np.asarray(
        [
            [1.0, 0.4, 0.2],
            [0.4, 1.0, 0.3],
            [0.2, 0.3, 1.0],
        ]
    )
    direct = weighted_residual_energy(
        lead_field,
        source,
        measurement,
        covariance,
    )
    whitener = covariance_inverse_sqrt(covariance)
    whitened = float(np.linalg.norm(whitener @ residual) ** 2)
    return {
        "weighted_residual_energy": direct,
        "whitened_residual_energy": whitened,
        "absolute_identity_error": abs(direct - whitened),
    }


def v27_resolution_leakage_path() -> list[dict[str, float]]:
    lead_field = np.asarray(
        [
            [1.0, 0.2, 0.0, 0.9, 0.1, 0.0],
            [0.0, 0.7, 0.2, 0.1, 0.6, 0.0],
            [0.1, 0.0, 0.5, 0.0, 0.2, 0.4],
        ]
    )
    rows: list[dict[str, float]] = []
    for regularization in (1e-4, 1e-2, 1e-1, 1.0):
        resolution = resolution_matrix(
            lead_field,
            regularization=regularization,
        )
        rows.append(
            {
                "regularization": regularization,
                "resolution_trace": float(np.trace(resolution)),
                "off_diagonal_leakage_fraction": off_diagonal_leakage_fraction(
                    resolution
                ),
                "identity_error": resolution_identity_error(resolution),
            }
        )
    return rows


def v28_correlated_noise_fisher_information() -> list[dict[str, float]]:
    topography = np.ones(4)
    identity = np.eye(4)
    common = np.ones((4, 4))
    rows: list[dict[str, float]] = []
    for correlation in (0.0, 0.3, 0.6, 0.9):
        covariance = (1.0 - correlation) * identity + correlation * common
        rows.append(
            {
                "common_noise_correlation": correlation,
                "fisher_information": scalar_amplitude_fisher_information(
                    topography,
                    covariance,
                ),
                "crlb_variance": scalar_amplitude_crlb(
                    topography,
                    covariance,
                ),
            }
        )
    return rows


def v29_temporal_aliasing() -> dict[str, float]:
    sample_rate_hz = 100.0
    frequency_hz = 17.0
    alias_frequency_hz = sample_rate_hz - frequency_hz
    return {
        "sample_rate_hz": sample_rate_hz,
        "frequency_hz": frequency_hz,
        "alias_frequency_hz": alias_frequency_hz,
        "max_sample_difference": cosine_aliasing_error(
            sample_rate_hz=sample_rate_hz,
            frequency_hz=frequency_hz,
            n_samples=200,
        ),
    }


def v30_inverse_noise_amplification() -> list[dict[str, float]]:
    rows: list[dict[str, float]] = []
    for smallest_singular_value in (1.0, 0.3, 0.1, 0.03, 0.01):
        lead_field = np.diag([1.0, 0.5, smallest_singular_value])
        noise = np.asarray([0.0, 0.0, 1e-3])
        rows.append(
            {
                "smallest_singular_value": smallest_singular_value,
                "pseudoinverse_norm": pseudoinverse_operator_norm(lead_field),
                "realized_noise_amplification": pseudoinverse_noise_amplification(
                    lead_field,
                    noise,
                ),
            }
        )
    return rows
