"""Electromagnetic resolution utilities for Research III V26-V30."""

from __future__ import annotations

import numpy as np


def covariance_inverse_sqrt(covariance: np.ndarray) -> np.ndarray:
    cov = _validate_covariance(covariance)
    eigenvalues, eigenvectors = np.linalg.eigh(cov)
    if np.min(eigenvalues) <= np.finfo(float).eps:
        raise ValueError("covariance must be positive definite")
    return (eigenvectors * (1.0 / np.sqrt(eigenvalues))) @ eigenvectors.T


def weighted_residual_energy(
    lead_field: np.ndarray,
    source: np.ndarray,
    measurement: np.ndarray,
    noise_covariance: np.ndarray,
) -> float:
    operator = _validate_matrix(lead_field)
    j = _validate_vector(source, operator.shape[1], "source")
    y = _validate_vector(measurement, operator.shape[0], "measurement")
    covariance = _validate_covariance(noise_covariance, operator.shape[0])
    residual = y - operator @ j
    return float(residual @ np.linalg.solve(covariance, residual))


def tikhonov_inverse_operator(
    lead_field: np.ndarray,
    *,
    regularization: float,
) -> np.ndarray:
    operator = _validate_matrix(lead_field)
    if regularization <= 0.0 or not np.isfinite(regularization):
        raise ValueError("regularization must be finite and positive")
    gram = operator.T @ operator
    return np.linalg.solve(
        gram + regularization * np.eye(operator.shape[1]),
        operator.T,
    )


def resolution_matrix(
    lead_field: np.ndarray,
    *,
    regularization: float,
) -> np.ndarray:
    operator = _validate_matrix(lead_field)
    return tikhonov_inverse_operator(
        operator,
        regularization=regularization,
    ) @ operator


def off_diagonal_leakage_fraction(resolution: np.ndarray) -> float:
    matrix = _validate_square_matrix(resolution, "resolution")
    total = float(np.sum(matrix**2))
    if total <= np.finfo(float).eps:
        return 0.0
    diagonal = np.diag(np.diag(matrix))
    return float(np.sum((matrix - diagonal) ** 2) / total)


def resolution_identity_error(resolution: np.ndarray) -> float:
    matrix = _validate_square_matrix(resolution, "resolution")
    identity = np.eye(matrix.shape[0])
    return float(
        np.linalg.norm(matrix - identity, ord="fro") / np.sqrt(matrix.shape[0])
    )


def rank_limited_identity_error_lower_bound(
    *,
    source_dimension: int,
    operator_rank: int,
) -> float:
    """Minimum normalized Frobenius distance from identity at a declared rank."""
    if source_dimension < 1:
        raise ValueError("source_dimension must be positive")
    if not 0 <= operator_rank <= source_dimension:
        raise ValueError("operator_rank must lie between zero and source_dimension")
    return float(np.sqrt((source_dimension - operator_rank) / source_dimension))


def scalar_amplitude_fisher_information(
    topography: np.ndarray,
    noise_covariance: np.ndarray,
) -> float:
    lead = np.asarray(topography, dtype=float)
    if lead.ndim != 1 or lead.size < 1 or not np.all(np.isfinite(lead)):
        raise ValueError("topography must be a finite nonempty vector")
    covariance = _validate_covariance(noise_covariance, lead.size)
    return float(lead @ np.linalg.solve(covariance, lead))


def scalar_amplitude_crlb(
    topography: np.ndarray,
    noise_covariance: np.ndarray,
) -> float:
    information = scalar_amplitude_fisher_information(topography, noise_covariance)
    if information <= 0.0:
        raise ValueError("Fisher information must be positive")
    return 1.0 / information


def sampled_cosine(
    *,
    sample_rate_hz: float,
    frequency_hz: float,
    n_samples: int,
) -> np.ndarray:
    if sample_rate_hz <= 0.0 or not np.isfinite(sample_rate_hz):
        raise ValueError("sample_rate_hz must be finite and positive")
    if frequency_hz < 0.0 or not np.isfinite(frequency_hz):
        raise ValueError("frequency_hz must be finite and nonnegative")
    if n_samples < 2:
        raise ValueError("n_samples must be at least two")
    index = np.arange(n_samples, dtype=float)
    return np.cos(2.0 * np.pi * frequency_hz * index / sample_rate_hz)


def cosine_aliasing_error(
    *,
    sample_rate_hz: float,
    frequency_hz: float,
    n_samples: int,
) -> float:
    if not 0.0 < frequency_hz < sample_rate_hz:
        raise ValueError(
            "frequency_hz must lie strictly between 0 and sample_rate_hz"
        )
    alias_frequency = sample_rate_hz - frequency_hz
    first = sampled_cosine(
        sample_rate_hz=sample_rate_hz,
        frequency_hz=frequency_hz,
        n_samples=n_samples,
    )
    alias = sampled_cosine(
        sample_rate_hz=sample_rate_hz,
        frequency_hz=alias_frequency,
        n_samples=n_samples,
    )
    return float(np.max(np.abs(first - alias)))


def pseudoinverse_noise_amplification(
    lead_field: np.ndarray,
    noise: np.ndarray,
) -> float:
    operator = _validate_matrix(lead_field)
    eta = _validate_vector(noise, operator.shape[0], "noise")
    denominator = float(np.linalg.norm(eta))
    if denominator <= np.finfo(float).eps:
        raise ValueError("noise must be nonzero")
    source_error = np.linalg.pinv(operator) @ eta
    return float(np.linalg.norm(source_error) / denominator)


def pseudoinverse_operator_norm(lead_field: np.ndarray) -> float:
    operator = _validate_matrix(lead_field)
    return float(np.linalg.norm(np.linalg.pinv(operator), 2))


def _validate_matrix(matrix: np.ndarray) -> np.ndarray:
    operator = np.asarray(matrix, dtype=float)
    if operator.ndim != 2 or min(operator.shape) < 1:
        raise ValueError("matrix must be a nonempty two-dimensional array")
    if not np.all(np.isfinite(operator)):
        raise ValueError("matrix must contain only finite values")
    return operator


def _validate_square_matrix(matrix: np.ndarray, name: str) -> np.ndarray:
    value = _validate_matrix(matrix)
    if value.shape[0] != value.shape[1]:
        raise ValueError(f"{name} must be square")
    return value


def _validate_vector(vector: np.ndarray, length: int, name: str) -> np.ndarray:
    value = np.asarray(vector, dtype=float)
    if value.ndim != 1 or value.shape[0] != length:
        raise ValueError(f"{name} must have length {length}")
    if not np.all(np.isfinite(value)):
        raise ValueError(f"{name} must contain only finite values")
    return value


def _validate_covariance(
    covariance: np.ndarray,
    dimension: int | None = None,
) -> np.ndarray:
    cov = _validate_square_matrix(covariance, "covariance")
    if dimension is not None and cov.shape != (dimension, dimension):
        raise ValueError("covariance dimension does not match sensor dimension")
    if not np.allclose(cov, cov.T, atol=1e-12, rtol=1e-12):
        raise ValueError("covariance must be symmetric")
    if np.min(np.linalg.eigvalsh(cov)) <= np.finfo(float).eps:
        raise ValueError("covariance must be positive definite")
    return cov
