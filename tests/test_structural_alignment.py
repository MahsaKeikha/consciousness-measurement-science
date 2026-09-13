import numpy as np
import pytest

from consciousness_measurement.structural_alignment import (
    distance_matrix,
    matrix_alignment,
    normalized_distortion,
    permutation_alignment_test,
)


def test_distance_matrix_is_symmetric_with_zero_diagonal():
    features = np.array([[0.0], [1.0], [3.0]])
    distances = distance_matrix(features)
    assert distances.shape == (3, 3)
    assert np.allclose(distances, distances.T)
    assert np.allclose(np.diag(distances), 0.0)


def test_identical_relational_structures_have_unit_alignment_and_zero_distortion():
    distances = distance_matrix(np.array([[0.0], [1.0], [3.0], [5.0]]))
    assert matrix_alignment(distances, distances) == pytest.approx(1.0)
    assert normalized_distortion(distances, distances) == pytest.approx(0.0)


def test_scale_change_is_removed_by_normalized_distortion():
    first = distance_matrix(np.array([[0.0], [1.0], [2.5], [4.0]]))
    second = first * 7.0
    assert normalized_distortion(first, second) == pytest.approx(0.0)


def test_permutation_test_is_reproducible():
    phenomenal = distance_matrix(np.array([[0.0], [1.0], [3.0], [7.0], [9.0]]))
    neural = distance_matrix(np.array([[0.0], [1.1], [2.9], [7.2], [9.1]]))
    first = permutation_alignment_test(phenomenal, neural, permutations=99, seed=17)
    second = permutation_alignment_test(phenomenal, neural, permutations=99, seed=17)
    assert first == second
    observed, p_value = first
    assert -1.0 <= observed <= 1.0
    assert 0.0 < p_value <= 1.0


def test_invalid_shapes_are_rejected():
    with pytest.raises(ValueError):
        distance_matrix(np.array([1.0, 2.0, 3.0]))
    with pytest.raises(ValueError):
        matrix_alignment(np.eye(3), np.eye(4))
    with pytest.raises(ValueError):
        permutation_alignment_test(np.eye(3), np.eye(4), permutations=10)
