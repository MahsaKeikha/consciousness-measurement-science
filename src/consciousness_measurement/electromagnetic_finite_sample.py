from __future__ import annotations

from math import erf, erfc, sqrt
from statistics import NormalDist

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
    if np.min(np.linalg.eigvalsh(covariance)) <= 0.0:
        raise ValueError("covariance must be positive definite")
    return covariance


def gls_amplitude_estimate(
    topography: np.ndarray,
    measurement: np.ndarray,
    covariance: np.ndarray,
) -> float:
    """Generalized least-squares estimate for a scalar source amplitude."""
    topography = _as_vector(topography)
    measurement = _as_vector(measurement)
    if measurement.shape != topography.shape:
        raise ValueError("measurement and topography must have the same shape")
    covariance = _validate_covariance(covariance, topography.size)
    precision_topography = np.linalg.solve(covariance, topography)
    information = float(topography @ precision_topography)
    if information <= 0.0:
        raise ValueError("topography must carry positive information")
    return float(precision_topography @ measurement / information)


def gls_amplitude_information(
    topography: np.ndarray,
    covariance: np.ndarray,
) -> float:
    """Fisher information for scalar amplitude in a Gaussian linear mean model."""
    topography = _as_vector(topography)
    covariance = _validate_covariance(covariance, topography.size)
    return float(topography @ np.linalg.solve(covariance, topography))


def gls_amplitude_variance(
    topography: np.ndarray,
    covariance: np.ndarray,
) -> float:
    """Exact variance and CRLB of the scalar-amplitude GLS estimator."""
    information = gls_amplitude_information(topography, covariance)
    return 1.0 / information


def gaussian_two_sided_interval_half_width(
    variance: float,
    coverage: float = 0.95,
) -> float:
    """Normal-theory symmetric interval half-width for a known variance."""
    variance = float(variance)
    coverage = float(coverage)
    if not np.isfinite(variance) or variance <= 0.0:
        raise ValueError("variance must be finite and positive")
    if not 0.0 < coverage < 1.0:
        raise ValueError("coverage must lie strictly between zero and one")
    probability = 0.5 * (1.0 + coverage)
    z = NormalDist().inv_cdf(probability)
    return float(z * sqrt(variance))


def inverse_sample_covariance_bias_factor(
    dimension: int,
    degrees_of_freedom: int,
) -> float:
    """E[S^-1] multiplier when S = W / nu and W ~ Wishart(C, nu)."""
    if dimension < 1:
        raise ValueError("dimension must be positive")
    if degrees_of_freedom <= dimension + 1:
        raise ValueError("degrees_of_freedom must exceed dimension + one")
    return float(degrees_of_freedom / (degrees_of_freedom - dimension - 1))


def gaussian_equal_covariance_bayes_error(
    mahalanobis_squared: float,
) -> float:
    """Equal-prior Bayes error for two Gaussian means with common covariance."""
    mahalanobis_squared = float(mahalanobis_squared)
    if not np.isfinite(mahalanobis_squared) or mahalanobis_squared < 0.0:
        raise ValueError("mahalanobis_squared must be finite and nonnegative")
    distance = sqrt(mahalanobis_squared)
    return float(0.5 * erfc(distance / (2.0 * sqrt(2.0))))


def independent_two_sided_fwer(
    threshold: float,
    comparisons: int,
) -> float:
    """Family-wise error for K independent two-sided standard-normal tests."""
    threshold = float(threshold)
    if not np.isfinite(threshold) or threshold < 0.0:
        raise ValueError("threshold must be finite and nonnegative")
    if comparisons < 1:
        raise ValueError("comparisons must be positive")
    single_acceptance = erf(threshold / sqrt(2.0))
    return float(1.0 - single_acceptance**comparisons)


def independent_two_sided_fwer_threshold(
    alpha: float,
    comparisons: int,
) -> float:
    """Exact independent-test threshold that controls two-sided FWER at alpha."""
    alpha = float(alpha)
    if not 0.0 < alpha < 1.0:
        raise ValueError("alpha must lie strictly between zero and one")
    if comparisons < 1:
        raise ValueError("comparisons must be positive")
    single_acceptance = (1.0 - alpha) ** (1.0 / comparisons)
    upper_probability = 0.5 * (1.0 + single_acceptance)
    return float(NormalDist().inv_cdf(upper_probability))


def weighted_amplitude_variance(
    topography: np.ndarray,
    true_covariance: np.ndarray,
    weight_matrix: np.ndarray,
) -> float:
    """Exact sandwich variance for a weighted scalar-amplitude estimator."""
    topography = _as_vector(topography)
    true_covariance = _validate_covariance(true_covariance, topography.size)
    weight_matrix = _as_matrix(weight_matrix)
    if weight_matrix.shape != true_covariance.shape:
        raise ValueError("weight_matrix shape does not match covariance")
    if not np.allclose(weight_matrix, weight_matrix.T, atol=1e-12):
        raise ValueError("weight_matrix must be symmetric")
    denominator = float(topography @ weight_matrix @ topography)
    if denominator <= 0.0:
        raise ValueError("weight_matrix must give positive target information")
    numerator = float(
        topography @ weight_matrix @ true_covariance @ weight_matrix @ topography
    )
    return numerator / denominator**2


def nominal_weighted_amplitude_variance(
    topography: np.ndarray,
    weight_matrix: np.ndarray,
) -> float:
    """Variance reported if the weighting matrix is treated as exact precision."""
    topography = _as_vector(topography)
    weight_matrix = _as_matrix(weight_matrix)
    if weight_matrix.shape != (topography.size, topography.size):
        raise ValueError("weight_matrix shape does not match topography")
    if not np.allclose(weight_matrix, weight_matrix.T, atol=1e-12):
        raise ValueError("weight_matrix must be symmetric")
    information = float(topography @ weight_matrix @ topography)
    if information <= 0.0:
        raise ValueError("weight_matrix must give positive target information")
    return 1.0 / information
