from __future__ import annotations

import numpy as np
import pytest

from consciousness_measurement.electromagnetic_resolution import (
    cosine_aliasing_error,
    covariance_inverse_sqrt,
    off_diagonal_leakage_fraction,
    pseudoinverse_noise_amplification,
    pseudoinverse_operator_norm,
    rank_limited_identity_error_lower_bound,
    resolution_identity_error,
    resolution_matrix,
    scalar_amplitude_crlb,
    scalar_amplitude_fisher_information,
    sampled_cosine,
    weighted_residual_energy,
)


def test_covariance_inverse_sqrt_whitens_positive_definite_covariance() -> None:
    covariance = np.asarray(
        [
            [1.0, 0.4, 0.2],
            [0.4, 1.0, 0.3],
            [0.2, 0.3, 1.0],
        ]
    )
    whitener = covariance_inverse_sqrt(covariance)
    assert whitener @ covariance @ whitener.T == pytest.approx(np.eye(3), abs=1e-12)


def test_weighted_residual_energy_matches_whitened_norm() -> None:
    lead_field = np.asarray([[1.0, 0.2], [0.3, 1.0], [0.7, -0.2]])
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
    assert direct == pytest.approx(whitened, abs=1e-14)


def test_underdetermined_resolution_matrix_cannot_be_identity() -> None:
    lead_field = np.asarray(
        [
            [1.0, 0.0, 1.0, 0.0],
            [0.0, 1.0, 0.0, 1.0],
        ]
    )
    resolution = resolution_matrix(lead_field, regularization=1e-6)
    assert resolution.shape == (4, 4)
    assert resolution_identity_error(resolution) > 0.7
    assert off_diagonal_leakage_fraction(resolution) > 0.4


def test_rank_limited_resolution_error_has_closed_form_lower_bound() -> None:
    bound = rank_limited_identity_error_lower_bound(
        source_dimension=6,
        operator_rank=3,
    )
    assert bound == pytest.approx(np.sqrt(0.5))


def test_scalar_fisher_information_and_crlb_are_reciprocal() -> None:
    topography = np.ones(4)
    covariance = np.eye(4)
    information = scalar_amplitude_fisher_information(topography, covariance)
    bound = scalar_amplitude_crlb(topography, covariance)
    assert information == pytest.approx(4.0)
    assert bound == pytest.approx(0.25)
    assert information * bound == pytest.approx(1.0)


def test_cosine_alias_pair_is_indistinguishable_after_sampling() -> None:
    error = cosine_aliasing_error(
        sample_rate_hz=100.0,
        frequency_hz=17.0,
        n_samples=200,
    )
    assert error < 2e-13
    first = sampled_cosine(
        sample_rate_hz=100.0,
        frequency_hz=17.0,
        n_samples=200,
    )
    alias = sampled_cosine(
        sample_rate_hz=100.0,
        frequency_hz=83.0,
        n_samples=200,
    )
    assert first == pytest.approx(alias, abs=2e-13)


def test_pseudoinverse_noise_amplification_hits_spectral_bound() -> None:
    lead_field = np.diag([1.0, 1.0, 0.01])
    noise = np.asarray([0.0, 0.0, 1e-3])
    amplification = pseudoinverse_noise_amplification(lead_field, noise)
    operator_norm = pseudoinverse_operator_norm(lead_field)
    assert amplification == pytest.approx(100.0)
    assert operator_norm == pytest.approx(100.0)
    assert amplification == pytest.approx(operator_norm)
