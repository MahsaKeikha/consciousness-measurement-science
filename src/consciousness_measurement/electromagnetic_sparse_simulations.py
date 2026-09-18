from __future__ import annotations

import itertools
import math

import numpy as np

from .electromagnetic_sparse import (
    coherence_gram_eigenvalue_bounds,
    largest_guaranteed_integer_sparsity,
    mutual_coherence,
    nuisance_adjusted_fisher_information,
    sequential_logdet_information_gain,
    sparse_uniqueness_threshold,
    subdictionary_gram_spectrum,
    updated_information_matrix,
    welch_coherence_lower_bound,
)


def regular_simplex_dictionary(dimension: int) -> np.ndarray:
    """Return d+1 normalized regular-simplex columns in R^d."""
    if dimension < 1:
        raise ValueError("dimension must be positive")
    helmert = np.zeros((dimension, dimension + 1))
    for k in range(1, dimension + 1):
        denominator = math.sqrt(k * (k + 1))
        helmert[k - 1, :k] = 1.0 / denominator
        helmert[k - 1, k] = -k / denominator
    return helmert / np.linalg.norm(helmert, axis=0)


def coherent_comparison_dictionary() -> np.ndarray:
    """Four orthogonal columns plus one nearly duplicated first direction."""
    extra = np.asarray([0.99, 0.10, 0.0, 0.0])
    extra = extra / np.linalg.norm(extra)
    return np.column_stack((np.eye(4), extra))


def v36_coherence_and_welch_bound() -> list[dict[str, float | str]]:
    simplex = regular_simplex_dictionary(4)
    coherent = coherent_comparison_dictionary()
    rows: list[dict[str, float | str]] = []
    for name, matrix in (("regular_simplex", simplex), ("coherent", coherent)):
        rows.append(
            {
                "dictionary": name,
                "sensor_dimension": float(matrix.shape[0]),
                "source_count": float(matrix.shape[1]),
                "rank": float(np.linalg.matrix_rank(matrix)),
                "mutual_coherence": mutual_coherence(matrix),
                "welch_lower_bound": welch_coherence_lower_bound(
                    matrix.shape[0],
                    matrix.shape[1],
                ),
            }
        )
    return rows


def v37_sparse_uniqueness_guarantee() -> list[dict[str, float | str]]:
    rows: list[dict[str, float | str]] = []
    for name, matrix in (
        ("regular_simplex", regular_simplex_dictionary(4)),
        ("coherent", coherent_comparison_dictionary()),
    ):
        coherence = mutual_coherence(matrix)
        rows.append(
            {
                "dictionary": name,
                "mutual_coherence": coherence,
                "strict_sparsity_threshold": sparse_uniqueness_threshold(coherence),
                "largest_guaranteed_integer_sparsity": float(
                    largest_guaranteed_integer_sparsity(coherence) or 0
                ),
            }
        )
    return rows


def v38_restricted_gram_conditioning() -> list[dict[str, float]]:
    matrix = regular_simplex_dictionary(4)
    coherence = mutual_coherence(matrix)
    rows: list[dict[str, float]] = []
    for sparsity in (2, 3):
        minimums: list[float] = []
        maximums: list[float] = []
        for support in itertools.combinations(range(matrix.shape[1]), sparsity):
            spectrum = subdictionary_gram_spectrum(matrix, support)
            minimums.append(float(spectrum[0]))
            maximums.append(float(spectrum[-1]))
        lower, upper = coherence_gram_eigenvalue_bounds(sparsity, coherence)
        rows.append(
            {
                "sparsity": float(sparsity),
                "mutual_coherence": coherence,
                "gershgorin_lower_bound": lower,
                "observed_minimum_eigenvalue": min(minimums),
                "observed_maximum_eigenvalue": max(maximums),
                "gershgorin_upper_bound": upper,
            }
        )
    return rows


def v39_nuisance_adjusted_fisher_information() -> list[dict[str, float | str]]:
    target = np.asarray([[1.0], [0.0], [0.0], [0.0]])
    covariance = np.eye(4)
    nuisance_cases = {
        "orthogonal": np.column_stack(
            (np.asarray([0.0, 1.0, 0.0, 0.0]), np.asarray([0.0, 0.0, 1.0, 0.0]))
        ),
        "partial_30deg": np.column_stack(
            (
                np.asarray([math.cos(math.pi / 6), math.sin(math.pi / 6), 0.0, 0.0]),
                np.asarray([0.0, 0.0, 1.0, 0.0]),
            )
        ),
        "contains_target": np.column_stack(
            (np.asarray([1.0, 0.0, 0.0, 0.0]), np.asarray([0.0, 1.0, 0.0, 0.0]))
        ),
    }
    rows: list[dict[str, float | str]] = []
    for name, nuisance in nuisance_cases.items():
        efficient = nuisance_adjusted_fisher_information(
            target,
            nuisance,
            covariance,
        )
        rows.append(
            {
                "nuisance_case": name,
                "nominal_target_information": 1.0,
                "nuisance_adjusted_information": float(efficient[0, 0]),
            }
        )
    return rows


def v40_sequential_sensor_information_gain() -> list[dict[str, float | str]]:
    prior = np.diag([10.0, 1.0])
    candidates = {
        "strong_direction": np.asarray([1.0, 0.0]),
        "weak_direction": np.asarray([0.0, 1.0]),
        "mixed_direction": np.asarray([2.0**-0.5, 2.0**-0.5]),
    }
    rows: list[dict[str, float | str]] = []
    prior_logdet = float(np.linalg.slogdet(prior)[1])
    for name, sensitivity in candidates.items():
        updated = updated_information_matrix(prior, sensitivity, 1.0)
        exact_gain = float(np.linalg.slogdet(updated)[1] - prior_logdet)
        rows.append(
            {
                "candidate": name,
                "determinant_lemma_gain": sequential_logdet_information_gain(
                    prior,
                    sensitivity,
                    1.0,
                ),
                "direct_logdet_gain": exact_gain,
                "updated_determinant": float(np.linalg.det(updated)),
            }
        )
    return rows
