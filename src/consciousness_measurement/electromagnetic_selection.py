from __future__ import annotations

from math import erfc, sqrt
from statistics import NormalDist

import numpy as np


def _validate_alpha(alpha: float) -> float:
    alpha = float(alpha)
    if not 0.0 < alpha < 1.0:
        raise ValueError("alpha must lie strictly between zero and one")
    return alpha


def _validate_comparisons(comparisons: int) -> int:
    if comparisons < 1:
        raise ValueError("comparisons must be positive")
    return int(comparisons)


def two_sided_standard_normal_tail(threshold: float) -> float:
    """Two-sided standard-normal exceedance probability at a nonnegative threshold."""
    threshold = float(threshold)
    if not np.isfinite(threshold) or threshold < 0.0:
        raise ValueError("threshold must be finite and nonnegative")
    return float(erfc(threshold / sqrt(2.0)))


def bonferroni_two_sided_z_threshold(alpha: float, comparisons: int) -> float:
    """Two-sided Bonferroni z threshold valid under arbitrary dependence."""
    alpha = _validate_alpha(alpha)
    comparisons = _validate_comparisons(comparisons)
    upper_probability = 1.0 - alpha / (2.0 * comparisons)
    return float(NormalDist().inv_cdf(upper_probability))


def bonferroni_fwer_union_bound(threshold: float, comparisons: int) -> float:
    """Union-bound FWER upper bound for K marginal standard-normal tests."""
    comparisons = _validate_comparisons(comparisons)
    single = two_sided_standard_normal_tail(threshold)
    return float(min(comparisons * single, 1.0))


def holm_adjusted_pvalues(pvalues: np.ndarray | list[float]) -> np.ndarray:
    """Holm step-down adjusted p-values in the original hypothesis order."""
    values = np.asarray(pvalues, dtype=float)
    if values.ndim != 1 or values.size == 0:
        raise ValueError("pvalues must be a nonempty one-dimensional sequence")
    if not np.all(np.isfinite(values)):
        raise ValueError("pvalues must be finite")
    if np.any(values < 0.0) or np.any(values > 1.0):
        raise ValueError("pvalues must lie between zero and one")

    order = np.argsort(values, kind="stable")
    sorted_values = values[order]
    adjusted_sorted = np.empty_like(sorted_values)
    running = 0.0
    total = values.size
    for index, value in enumerate(sorted_values):
        candidate = float((total - index) * value)
        running = max(running, candidate)
        adjusted_sorted[index] = min(running, 1.0)

    adjusted = np.empty_like(adjusted_sorted)
    adjusted[order] = adjusted_sorted
    return adjusted


def holm_rejections(
    pvalues: np.ndarray | list[float],
    alpha: float,
) -> np.ndarray:
    """Boolean rejection mask for Holm-adjusted p-values."""
    alpha = _validate_alpha(alpha)
    return holm_adjusted_pvalues(pvalues) <= alpha


def sign_flip_max_statistic_distribution(
    observations: np.ndarray | list[list[float]],
) -> np.ndarray:
    """Enumerate the row-wise sign-flip orbit of a max-absolute-mean statistic."""
    data = np.asarray(observations, dtype=float)
    if data.ndim != 2 or data.shape[0] < 1 or data.shape[1] < 1:
        raise ValueError("observations must be a nonempty two-dimensional matrix")
    if not np.all(np.isfinite(data)):
        raise ValueError("observations must contain only finite values")
    rows = data.shape[0]
    if rows > 20:
        raise ValueError("exact sign-flip enumeration is limited to at most 20 rows")

    statistics = np.empty(1 << rows, dtype=float)
    for mask in range(1 << rows):
        signs = np.fromiter(
            (1.0 if (mask >> index) & 1 else -1.0 for index in range(rows)),
            dtype=float,
            count=rows,
        )
        flipped = data * signs[:, None]
        statistics[mask] = float(np.max(np.abs(np.mean(flipped, axis=0))))
    return statistics


def sign_flip_max_statistic_pvalue(
    observations: np.ndarray | list[list[float]],
) -> float:
    """Exact orbit p-value for the observed max-absolute-mean statistic."""
    data = np.asarray(observations, dtype=float)
    distribution = sign_flip_max_statistic_distribution(data)
    observed = float(np.max(np.abs(np.mean(data, axis=0))))
    exceedances = int(np.sum(distribution >= observed - 1e-15))
    return float(exceedances / distribution.size)


def selected_max_abs_naive_null_coverage(
    marginal_coverage: float,
    comparisons: int,
) -> float:
    """Exact naive coverage after selecting max |Z| among independent null coordinates."""
    marginal_coverage = float(marginal_coverage)
    if not 0.0 < marginal_coverage < 1.0:
        raise ValueError("marginal_coverage must lie strictly between zero and one")
    comparisons = _validate_comparisons(comparisons)
    return float(marginal_coverage**comparisons)


def selected_max_abs_naive_false_positive(
    marginal_coverage: float,
    comparisons: int,
) -> float:
    """Exact false-positive probability after max-|Z| selection and naive reuse."""
    return 1.0 - selected_max_abs_naive_null_coverage(
        marginal_coverage,
        comparisons,
    )


def independent_holdout_selected_type1(alpha: float) -> float:
    """Exact conditional and unconditional Type I error after independent selection."""
    return _validate_alpha(alpha)
