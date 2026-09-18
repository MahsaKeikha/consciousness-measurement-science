from __future__ import annotations

import numpy as np
import pytest

from consciousness_measurement.electromagnetic_inverse import (
    common_reference_invariance_error,
    forward_model_mismatch,
    forward_model_perturbation_bound,
    nullspace_alternative,
    pairwise_sensor_differences,
    rank_nullity,
    right_nullspace,
    stacked_rank_nullity,
    tikhonov_filter_factors,
    tikhonov_source_estimate,
)


def test_pairwise_sensor_differences_are_common_reference_invariant() -> None:
    time = np.arange(1024) / 256.0
    signals = np.asarray(
        [
            np.sin(2.0 * np.pi * 10.0 * time + phase)
            for phase in (0.0, 0.4, 0.9, 1.3)
        ]
    )
    reference = 12.0 * np.sin(2.0 * np.pi * 1.0 * time)
    assert common_reference_invariance_error(signals, reference) < 5e-15
    assert pairwise_sensor_differences(signals).shape == (6, 1024)


def test_rank_nullity_and_right_nullspace_are_consistent() -> None:
    operator = np.asarray(
        [
            [1.0, 0.0, 1.0, 0.0],
            [0.0, 1.0, 0.0, 1.0],
        ]
    )
    geometry = rank_nullity(operator)
    basis = right_nullspace(operator)
    assert geometry.rank == 2
    assert geometry.nullity == 2
    assert basis.shape == (4, 2)
    assert np.linalg.norm(operator @ basis) < 1e-12


def test_nullspace_alternative_has_same_sensor_measurement() -> None:
    operator = np.asarray(
        [
            [1.0, 0.0, 1.0, 0.0],
            [0.0, 1.0, 0.0, 1.0],
        ]
    )
    source = np.asarray([1.0, 2.0, 0.0, 0.0])
    result = nullspace_alternative(operator, source, scale=2.0)
    assert result.sensor_residual < 1e-12
    assert result.source_separation == pytest.approx(2.0)


def test_tikhonov_filter_factors_match_singular_value_formula() -> None:
    operator = np.diag([2.0, 0.5])
    factors = tikhonov_filter_factors(operator, regularization=0.25)
    expected = np.asarray([2.0 / 4.25, 0.5 / 0.5])
    assert factors == pytest.approx(expected)


def test_tikhonov_regularization_changes_source_estimate() -> None:
    operator = np.asarray(
        [
            [1.0, 0.0, 0.9, 0.0],
            [0.0, 0.2, 0.0, 0.1],
        ]
    )
    source = np.asarray([1.0, 1.0, 0.2, 0.2])
    measurement = operator @ source
    weak = tikhonov_source_estimate(operator, measurement, regularization=1e-6)
    strong = tikhonov_source_estimate(operator, measurement, regularization=1.0)
    assert np.linalg.norm(strong) < np.linalg.norm(weak)
    assert np.linalg.norm(operator @ strong - measurement) > np.linalg.norm(
        operator @ weak - measurement
    )


def test_stacked_modalities_can_reduce_but_not_remove_nullity() -> None:
    eeg = np.asarray(
        [
            [1.0, 0.0, 0.0, 0.0],
            [0.0, 1.0, 0.0, 0.0],
        ]
    )
    meg = np.asarray(
        [
            [0.0, 0.0, 1.0, 0.0],
            [1.0, 1.0, 0.0, 0.0],
        ]
    )
    assert rank_nullity(eeg).nullity == 2
    assert rank_nullity(meg).nullity == 2
    combined = stacked_rank_nullity(eeg, meg)
    assert combined.rank == 3
    assert combined.nullity == 1


def test_forward_model_mismatch_obeys_operator_norm_bound() -> None:
    lead_field = np.asarray(
        [
            [1.0, 0.2, 0.0],
            [0.0, 0.8, 0.1],
        ]
    )
    perturbation = np.asarray(
        [
            [0.01, -0.02, 0.0],
            [0.0, 0.01, 0.02],
        ]
    )
    source = np.asarray([1.0, -0.5, 0.8])
    mismatch = forward_model_mismatch(lead_field, perturbation, source)
    bound = forward_model_perturbation_bound(perturbation, source)
    assert mismatch <= bound + 1e-15
