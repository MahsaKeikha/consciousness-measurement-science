"""Simple tools for phenomenal-neural relational structure comparison."""

from __future__ import annotations

import numpy as np


def distance_matrix(features: np.ndarray) -> np.ndarray:
    """Euclidean pairwise distance matrix for rows of a feature matrix."""
    x = np.asarray(features, dtype=float)
    if x.ndim != 2:
        raise ValueError("features must be a 2D array")
    diff = x[:, None, :] - x[None, :, :]
    return np.sqrt(np.sum(diff * diff, axis=-1))


def _upper_triangle(matrix: np.ndarray) -> np.ndarray:
    m = np.asarray(matrix, dtype=float)
    if m.ndim != 2 or m.shape[0] != m.shape[1]:
        raise ValueError("distance matrix must be square")
    idx = np.triu_indices(m.shape[0], k=1)
    return m[idx]


def _normalize_distances(matrix: np.ndarray) -> np.ndarray:
    m = np.asarray(matrix, dtype=float)
    scale = np.mean(_upper_triangle(m))
    if scale <= 0:
        raise ValueError("distance matrix must contain positive off-diagonal distances")
    return m / scale


def matrix_alignment(a: np.ndarray, b: np.ndarray) -> float:
    """Pearson correlation between upper triangles of two distance matrices."""
    va = _upper_triangle(a)
    vb = _upper_triangle(b)
    if va.shape != vb.shape:
        raise ValueError("distance matrices must have matching shape")
    if np.std(va) == 0 or np.std(vb) == 0:
        raise ValueError("alignment undefined for constant distance vectors")
    return float(np.corrcoef(va, vb)[0, 1])


def normalized_distortion(a: np.ndarray, b: np.ndarray) -> float:
    """Mean absolute difference after scale normalization."""
    na = _normalize_distances(a)
    nb = _normalize_distances(b)
    if na.shape != nb.shape:
        raise ValueError("distance matrices must have matching shape")
    return float(np.mean(np.abs(_upper_triangle(na) - _upper_triangle(nb))))


def permutation_alignment_test(
    phenomenal: np.ndarray,
    neural: np.ndarray,
    permutations: int = 1000,
    seed: int = 0,
) -> tuple[float, float]:
    """Permutation test for cross-domain distance-matrix alignment.

    Labels of the neural matrix are permuted while preserving its internal geometry.
    Returns (observed_alignment, one-sided_p_value).
    """
    p = np.asarray(phenomenal, dtype=float)
    n = np.asarray(neural, dtype=float)
    if p.shape != n.shape:
        raise ValueError("distance matrices must have matching shape")
    if permutations < 1:
        raise ValueError("permutations must be positive")

    observed = matrix_alignment(p, n)
    rng = np.random.default_rng(seed)
    exceed = 0
    for _ in range(permutations):
        order = rng.permutation(n.shape[0])
        permuted = n[np.ix_(order, order)]
        if matrix_alignment(p, permuted) >= observed:
            exceed += 1
    p_value = (exceed + 1) / (permutations + 1)
    return observed, p_value
