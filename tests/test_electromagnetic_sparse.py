from __future__ import annotations

import math

import numpy as np
import pytest

from consciousness_measurement.electromagnetic_sparse import (
    coherence_gram_eigenvalue_bounds,
    largest_guaranteed_integer_sparsity,
    mutual_coherence,
    normalize_columns,
    nuisance_adjusted_fisher_information,
    sequential_logdet_information_gain,
    sparse_uniqueness_threshold,
    subdictionary_gram_spectrum,
    updated_information_matrix,
    welch_coherence_lower_bound,
)


def test_mutual_coherence_uses_normalized_columns() -> None:
    matrix = np.asarray([[2.0, 0.0, 1.0], [0.0, 3.0, 1.0]])
    normalized = normalize_columns(matrix)
    assert np.linalg.norm(normalized, axis=0) == pytest.approx(np.ones(3))
    assert mutual_coherence(matrix) == pytest.approx(2.0**-0.5)


def test_welch_bound_for_four_by_five_dictionary_is_one_quarter() -> None:
    assert welch_coherence_lower_bound(4, 5) == pytest.approx(0.25)
    assert welch_coherence_lower_bound(5, 4) == pytest.approx(0.0)


def test_sparse_uniqueness_threshold_is_strict() -> None:
    assert sparse_uniqueness_threshold(0.25) == pytest.approx(2.5)
    assert largest_guaranteed_integer_sparsity(0.25) == 2
    assert math.isinf(sparse_uniqueness_threshold(0.0))
    assert largest_guaranteed_integer_sparsity(0.0) is None


def test_coherence_bounds_contain_selected_gram_spectrum() -> None:
    matrix = np.asarray(
        [
            [1.0, 0.0, 0.5],
            [0.0, 1.0, math.sqrt(3.0) / 2.0],
        ]
    )
    coherence = mutual_coherence(matrix)
    spectrum = subdictionary_gram_spectrum(matrix, [0, 2])
    lower, upper = coherence_gram_eigenvalue_bounds(2, coherence)
    assert spectrum[0] >= lower - 1e-12
    assert spectrum[-1] <= upper + 1e-12


def test_nuisance_adjusted_information_is_schur_complement() -> None:
    target = np.asarray([[1.0], [0.0], [0.0]])
    nuisance = np.asarray([[0.5], [math.sqrt(3.0) / 2.0], [0.0]])
    efficient = nuisance_adjusted_fisher_information(target, nuisance, np.eye(3))
    assert efficient[0, 0] == pytest.approx(0.75)


def test_sequential_logdet_gain_matches_direct_determinant_update() -> None:
    prior = np.diag([10.0, 1.0])
    sensitivity = np.asarray([0.0, 1.0])
    updated = updated_information_matrix(prior, sensitivity, 1.0)
    direct = np.linalg.slogdet(updated)[1] - np.linalg.slogdet(prior)[1]
    assert sequential_logdet_information_gain(prior, sensitivity, 1.0) == pytest.approx(direct)
