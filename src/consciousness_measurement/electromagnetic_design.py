from __future__ import annotations

import numpy as np


def _as_vector(values: np.ndarray | list[float]) -> np.ndarray:
    vector = np.asarray(values, dtype=float)
    if vector.ndim != 1:
        raise ValueError("expected a one-dimensional vector")
    if not np.all(np.isfinite(vector)):
        raise ValueError("vector must contain only finite values")
    return vector


def _as_matrix(values: np.ndarray | list[list[float]]) -> np.ndarray:
    matrix = np.asarray(values, dtype=float)
    if matrix.ndim != 2:
        raise ValueError("expected a two-dimensional matrix")
    if not np.all(np.isfinite(matrix)):
        raise ValueError("matrix must contain only finite values")
    return matrix


def _validate_covariance(covariance: np.ndarray, dimension: int) -> np.ndarray:
    covariance = _as_matrix(covariance)
    if covariance.shape != (dimension, dimension):
        raise ValueError("covariance shape does not match measurement dimension")
    if not np.allclose(covariance, covariance.T, atol=1e-12):
        raise ValueError("covariance must be symmetric")
    eigenvalues = np.linalg.eigvalsh(covariance)
    if np.min(eigenvalues) <= 0.0:
        raise ValueError("covariance must be positive definite")
    return covariance


def point_spread_function(
    resolution: np.ndarray,
    source_index: int,
) -> np.ndarray:
    """Return the source-index column of a linear inverse resolution matrix."""
    resolution = _as_matrix(resolution)
    if resolution.shape[0] != resolution.shape[1]:
        raise ValueError("resolution matrix must be square")
    if not 0 <= source_index < resolution.shape[1]:
        raise IndexError("source_index is out of range")
    return resolution[:, source_index].copy()


def cross_talk_function(
    resolution: np.ndarray,
    estimate_index: int,
) -> np.ndarray:
    """Return the estimate-index row of a linear inverse resolution matrix."""
    resolution = _as_matrix(resolution)
    if resolution.shape[0] != resolution.shape[1]:
        raise ValueError("resolution matrix must be square")
    if not 0 <= estimate_index < resolution.shape[0]:
        raise IndexError("estimate_index is out of range")
    return resolution[estimate_index, :].copy()


def mahalanobis_topography_distance(
    first: np.ndarray,
    second: np.ndarray,
    covariance: np.ndarray,
) -> float:
    """Noise-aware distance between two sensor topographies."""
    first = _as_vector(first)
    second = _as_vector(second)
    if first.shape != second.shape:
        raise ValueError("topographies must have the same shape")
    covariance = _validate_covariance(covariance, first.size)
    difference = first - second
    return float(difference @ np.linalg.solve(covariance, difference))


def fisher_information_matrix(
    sensitivity_matrix: np.ndarray,
    covariance: np.ndarray,
) -> np.ndarray:
    """Gaussian Fisher information for a linear mean model."""
    sensitivity_matrix = _as_matrix(sensitivity_matrix)
    covariance = _validate_covariance(covariance, sensitivity_matrix.shape[0])
    return sensitivity_matrix.T @ np.linalg.solve(covariance, sensitivity_matrix)


def d_optimal_log_information(fisher_information: np.ndarray) -> float:
    """Return log det(F) for positive-definite Fisher information, else -inf."""
    fisher_information = _as_matrix(fisher_information)
    if fisher_information.shape[0] != fisher_information.shape[1]:
        raise ValueError("Fisher information matrix must be square")
    sign, logdet = np.linalg.slogdet(fisher_information)
    if sign <= 0.0:
        return float("-inf")
    return float(logdet)


def e_optimal_information(fisher_information: np.ndarray) -> float:
    """Return the smallest eigenvalue of a symmetric Fisher information matrix."""
    fisher_information = _as_matrix(fisher_information)
    if fisher_information.shape[0] != fisher_information.shape[1]:
        raise ValueError("Fisher information matrix must be square")
    symmetric = 0.5 * (fisher_information + fisher_information.T)
    return float(np.min(np.linalg.eigvalsh(symmetric)))


def orthogonal_complement_projector(nuisance_basis: np.ndarray) -> np.ndarray:
    """Project onto the Euclidean orthogonal complement of nuisance columns."""
    nuisance_basis = _as_matrix(nuisance_basis)
    dimension = nuisance_basis.shape[0]
    if nuisance_basis.shape[1] == 0:
        return np.eye(dimension)
    nuisance_projector = nuisance_basis @ np.linalg.pinv(nuisance_basis)
    complement = np.eye(dimension) - nuisance_projector
    return 0.5 * (complement + complement.T)


def retained_target_information(
    whitened_target: np.ndarray,
    nuisance_basis: np.ndarray,
) -> float:
    """Squared target norm retained after projecting out a whitened nuisance subspace."""
    whitened_target = _as_vector(whitened_target)
    nuisance_basis = _as_matrix(nuisance_basis)
    if nuisance_basis.shape[0] != whitened_target.size:
        raise ValueError("nuisance basis and target dimension do not match")
    projector = orthogonal_complement_projector(nuisance_basis)
    retained = projector @ whitened_target
    return float(retained @ retained)


def retained_target_information_fraction(
    whitened_target: np.ndarray,
    nuisance_basis: np.ndarray,
) -> float:
    """Fraction of whitened target information retained after nuisance projection."""
    whitened_target = _as_vector(whitened_target)
    total = float(whitened_target @ whitened_target)
    if total <= 0.0:
        raise ValueError("whitened_target must have nonzero norm")
    return retained_target_information(whitened_target, nuisance_basis) / total


def robust_whitened_information_lower_bound(
    whitened_topography: np.ndarray,
    uncertainty_radius: float,
) -> float:
    """Exact worst-case information under an L2-bounded whitened perturbation."""
    whitened_topography = _as_vector(whitened_topography)
    uncertainty_radius = float(uncertainty_radius)
    if not np.isfinite(uncertainty_radius) or uncertainty_radius < 0.0:
        raise ValueError("uncertainty_radius must be a finite nonnegative value")
    remaining_norm = max(float(np.linalg.norm(whitened_topography)) - uncertainty_radius, 0.0)
    return remaining_norm**2


def worst_case_whitened_perturbation(
    whitened_topography: np.ndarray,
    uncertainty_radius: float,
) -> np.ndarray:
    """Construct a perturbation attaining the robust information lower bound."""
    whitened_topography = _as_vector(whitened_topography)
    uncertainty_radius = float(uncertainty_radius)
    if not np.isfinite(uncertainty_radius) or uncertainty_radius < 0.0:
        raise ValueError("uncertainty_radius must be a finite nonnegative value")
    norm = float(np.linalg.norm(whitened_topography))
    if norm == 0.0 or uncertainty_radius == 0.0:
        return np.zeros_like(whitened_topography)
    scale = min(uncertainty_radius / norm, 1.0)
    return -scale * whitened_topography
