from __future__ import annotations

import math
from collections.abc import Sequence

import numpy as np


def _as_matrix(values: np.ndarray | list[list[float]]) -> np.ndarray:
    matrix = np.asarray(values, dtype=float)
    if matrix.ndim != 2:
        raise ValueError("expected a two-dimensional matrix")
    if not np.all(np.isfinite(matrix)):
        raise ValueError("matrix must contain only finite values")
    return matrix


def _as_vector(values: np.ndarray | list[float]) -> np.ndarray:
    vector = np.asarray(values, dtype=float)
    if vector.ndim != 1:
        raise ValueError("expected a one-dimensional vector")
    if not np.all(np.isfinite(vector)):
        raise ValueError("vector must contain only finite values")
    return vector


def normalize_columns(matrix: np.ndarray) -> np.ndarray:
    """Return a copy with unit-L2 columns."""
    matrix = _as_matrix(matrix)
    norms = np.linalg.norm(matrix, axis=0)
    if np.any(norms <= 0.0):
        raise ValueError("all columns must have nonzero norm")
    return matrix / norms


def mutual_coherence(matrix: np.ndarray) -> float:
    """Maximum absolute inner product between distinct normalized columns."""
    normalized = normalize_columns(matrix)
    gram = normalized.T @ normalized
    np.fill_diagonal(gram, 0.0)
    return float(np.max(np.abs(gram), initial=0.0))


def welch_coherence_lower_bound(sensor_dimension: int, source_count: int) -> float:
    """Welch lower bound for source_count unit vectors in sensor_dimension dimensions."""
    if sensor_dimension < 1:
        raise ValueError("sensor_dimension must be positive")
    if source_count < 1:
        raise ValueError("source_count must be positive")
    if source_count <= sensor_dimension:
        return 0.0
    return math.sqrt(
        (source_count - sensor_dimension)
        / (sensor_dimension * (source_count - 1))
    )


def sparse_uniqueness_threshold(coherence: float) -> float:
    """Classical coherence-based sufficient threshold k < (1 + 1/mu) / 2."""
    coherence = float(coherence)
    if not np.isfinite(coherence) or coherence < 0.0 or coherence > 1.0:
        raise ValueError("coherence must lie in [0, 1]")
    if coherence == 0.0:
        return float("inf")
    return 0.5 * (1.0 + 1.0 / coherence)


def largest_guaranteed_integer_sparsity(coherence: float) -> int | None:
    """Largest positive integer k satisfying the strict coherence uniqueness bound."""
    threshold = sparse_uniqueness_threshold(coherence)
    if math.isinf(threshold):
        return None
    return max(int(math.ceil(threshold) - 1), 0)


def coherence_gram_eigenvalue_bounds(
    sparsity: int,
    coherence: float,
) -> tuple[float, float]:
    """Gershgorin bounds for a normalized k-column Gram matrix."""
    if sparsity < 1:
        raise ValueError("sparsity must be positive")
    coherence = float(coherence)
    if not np.isfinite(coherence) or coherence < 0.0 or coherence > 1.0:
        raise ValueError("coherence must lie in [0, 1]")
    radius = (sparsity - 1) * coherence
    return max(1.0 - radius, 0.0), 1.0 + radius


def subdictionary_gram_spectrum(
    matrix: np.ndarray,
    indices: Sequence[int],
) -> np.ndarray:
    """Eigenvalues of the normalized Gram matrix on a selected source support."""
    normalized = normalize_columns(matrix)
    support = tuple(int(index) for index in indices)
    if not support:
        raise ValueError("indices must not be empty")
    if len(set(support)) != len(support):
        raise ValueError("indices must be unique")
    if min(support) < 0 or max(support) >= normalized.shape[1]:
        raise IndexError("support index is out of range")
    subdictionary = normalized[:, support]
    gram = subdictionary.T @ subdictionary
    return np.linalg.eigvalsh(0.5 * (gram + gram.T))


def nuisance_adjusted_fisher_information(
    target_sensitivity: np.ndarray,
    nuisance_sensitivity: np.ndarray,
    covariance: np.ndarray,
) -> np.ndarray:
    """Efficient Fisher information for target parameters after nuisance adjustment."""
    target_sensitivity = _as_matrix(target_sensitivity)
    nuisance_sensitivity = _as_matrix(nuisance_sensitivity)
    covariance = _as_matrix(covariance)
    measurement_dimension = target_sensitivity.shape[0]
    if nuisance_sensitivity.shape[0] != measurement_dimension:
        raise ValueError("target and nuisance sensitivities must share measurement rows")
    if covariance.shape != (measurement_dimension, measurement_dimension):
        raise ValueError("covariance shape does not match measurement dimension")
    if not np.allclose(covariance, covariance.T, atol=1e-12):
        raise ValueError("covariance must be symmetric")
    if np.min(np.linalg.eigvalsh(covariance)) <= 0.0:
        raise ValueError("covariance must be positive definite")

    weighted_target = np.linalg.solve(covariance, target_sensitivity)
    fisher_target = target_sensitivity.T @ weighted_target
    if nuisance_sensitivity.shape[1] == 0:
        return fisher_target

    weighted_nuisance = np.linalg.solve(covariance, nuisance_sensitivity)
    fisher_cross = target_sensitivity.T @ weighted_nuisance
    fisher_nuisance = nuisance_sensitivity.T @ weighted_nuisance
    efficient = (
        fisher_target
        - fisher_cross @ np.linalg.pinv(fisher_nuisance) @ fisher_cross.T
    )
    return 0.5 * (efficient + efficient.T)


def sequential_logdet_information_gain(
    prior_information: np.ndarray,
    sensitivity: np.ndarray,
    noise_variance: float,
) -> float:
    """Exact log-determinant gain from one scalar linear measurement."""
    prior_information = _as_matrix(prior_information)
    sensitivity = _as_vector(sensitivity)
    if prior_information.shape[0] != prior_information.shape[1]:
        raise ValueError("prior_information must be square")
    if sensitivity.size != prior_information.shape[0]:
        raise ValueError("sensitivity dimension does not match information matrix")
    if np.min(np.linalg.eigvalsh(0.5 * (prior_information + prior_information.T))) <= 0.0:
        raise ValueError("prior_information must be positive definite")
    noise_variance = float(noise_variance)
    if not np.isfinite(noise_variance) or noise_variance <= 0.0:
        raise ValueError("noise_variance must be positive and finite")
    leverage = float(
        sensitivity @ np.linalg.solve(prior_information, sensitivity)
        / noise_variance
    )
    return math.log1p(leverage)


def updated_information_matrix(
    prior_information: np.ndarray,
    sensitivity: np.ndarray,
    noise_variance: float,
) -> np.ndarray:
    """F_new = F + a a^T / sigma^2 for one scalar linear measurement."""
    prior_information = _as_matrix(prior_information)
    sensitivity = _as_vector(sensitivity)
    if prior_information.shape[0] != prior_information.shape[1]:
        raise ValueError("prior_information must be square")
    if sensitivity.size != prior_information.shape[0]:
        raise ValueError("sensitivity dimension does not match information matrix")
    noise_variance = float(noise_variance)
    if not np.isfinite(noise_variance) or noise_variance <= 0.0:
        raise ValueError("noise_variance must be positive and finite")
    return prior_information + np.outer(sensitivity, sensitivity) / noise_variance
