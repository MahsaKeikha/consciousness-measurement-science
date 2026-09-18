from __future__ import annotations

import numpy as np


def _vector(values: np.ndarray | list[float], *, name: str) -> np.ndarray:
    vector = np.asarray(values, dtype=float)
    if vector.ndim != 1 or vector.size == 0:
        raise ValueError(f"{name} must be a nonempty one-dimensional vector")
    if not np.all(np.isfinite(vector)):
        raise ValueError(f"{name} must contain only finite values")
    return vector


def inverse_variance_weights(standard_errors: np.ndarray | list[float]) -> np.ndarray:
    """Return inverse-variance weights from positive standard errors."""
    standard_errors = _vector(standard_errors, name="standard_errors")
    if np.any(standard_errors <= 0.0):
        raise ValueError("standard_errors must be strictly positive")
    return 1.0 / np.square(standard_errors)


def common_effect_estimate(
    estimates: np.ndarray | list[float],
    standard_errors: np.ndarray | list[float],
) -> tuple[float, float]:
    """Inverse-variance common-effect estimate and its known-variance standard error."""
    estimates = _vector(estimates, name="estimates")
    weights = inverse_variance_weights(standard_errors)
    if estimates.shape != weights.shape:
        raise ValueError("estimates and standard_errors must have matching shapes")
    total_weight = float(np.sum(weights))
    estimate = float(np.dot(weights, estimates) / total_weight)
    standard_error = float(np.sqrt(1.0 / total_weight))
    return estimate, standard_error


def cochran_q_known_variance(
    estimates: np.ndarray | list[float],
    standard_errors: np.ndarray | list[float],
) -> float:
    """Weighted residual sum of squares around the common-effect estimate."""
    estimates = _vector(estimates, name="estimates")
    weights = inverse_variance_weights(standard_errors)
    if estimates.shape != weights.shape:
        raise ValueError("estimates and standard_errors must have matching shapes")
    pooled, _ = common_effect_estimate(estimates, standard_errors)
    return float(np.dot(weights, np.square(estimates - pooled)))


def leave_one_site_out_estimates(
    estimates: np.ndarray | list[float],
    standard_errors: np.ndarray | list[float],
) -> np.ndarray:
    """Return inverse-variance pooled estimates after deleting each site once."""
    estimates = _vector(estimates, name="estimates")
    weights = inverse_variance_weights(standard_errors)
    if estimates.shape != weights.shape:
        raise ValueError("estimates and standard_errors must have matching shapes")
    if estimates.size < 2:
        raise ValueError("at least two sites are required")
    weighted_sum = float(np.dot(weights, estimates))
    total_weight = float(np.sum(weights))
    denominator = total_weight - weights
    return (weighted_sum - weights * estimates) / denominator


def leave_one_site_out_shift_identity(
    estimates: np.ndarray | list[float],
    standard_errors: np.ndarray | list[float],
) -> np.ndarray:
    """Exact delete-one shift relative to the full pooled estimate."""
    estimates = _vector(estimates, name="estimates")
    weights = inverse_variance_weights(standard_errors)
    if estimates.shape != weights.shape:
        raise ValueError("estimates and standard_errors must have matching shapes")
    pooled, _ = common_effect_estimate(estimates, standard_errors)
    total_weight = float(np.sum(weights))
    return weights * (pooled - estimates) / (total_weight - weights)


def bonferroni_partial_conjunction_pvalue(
    p_values: np.ndarray | list[float],
    required_nonnulls: int,
) -> float:
    """Union-bound partial-conjunction p-value valid under arbitrary dependence."""
    p_values = _vector(p_values, name="p_values")
    if np.any((p_values < 0.0) | (p_values > 1.0)):
        raise ValueError("p_values must lie in [0, 1]")
    k = int(p_values.size)
    r = int(required_nonnulls)
    if not 1 <= r <= k:
        raise ValueError("required_nonnulls must lie between 1 and the number of tests")
    ordered = np.sort(p_values)
    return float(min(1.0, (k - r + 1) * ordered[r - 1]))


def normalized_site_weights(standard_errors: np.ndarray | list[float]) -> np.ndarray:
    """Normalize inverse-variance weights to sum to one."""
    weights = inverse_variance_weights(standard_errors)
    return weights / np.sum(weights)


def effective_site_count(standard_errors: np.ndarray | list[float]) -> float:
    """Kish-style effective count induced by normalized inverse-variance weights."""
    normalized = normalized_site_weights(standard_errors)
    return float(1.0 / np.dot(normalized, normalized))


def delete_site_variance_inflation(
    standard_errors: np.ndarray | list[float],
) -> np.ndarray:
    """Exact variance inflation after deleting each site under known variances."""
    normalized = normalized_site_weights(standard_errors)
    return 1.0 / (1.0 - normalized)
