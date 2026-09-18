from __future__ import annotations

import numpy as np
import pytest

from consciousness_measurement.electromagnetic_observables import (
    EPSILON_0,
    MU_0,
    common_mode_fraction,
    covariance_effective_rank,
    field_energy_density,
    normalized_spectral_entropy,
    poynting_vector,
    remove_common_mode,
    spatial_phase_concentration,
    spatiotemporal_singular_entropy,
)


def test_field_energy_density_matches_vacuum_formula() -> None:
    e = np.array([[2.0, 0.0, 0.0]])
    b = np.array([[0.0, 3e-6, 0.0]])
    expected = 0.5 * (EPSILON_0 * 4.0 + 9e-12 / MU_0)
    assert field_energy_density(e, b)[0] == pytest.approx(expected)


def test_poynting_vector_has_expected_direction_and_magnitude() -> None:
    e = np.array([[2.0, 0.0, 0.0]])
    b = np.array([[0.0, 3e-6, 0.0]])
    result = poynting_vector(e, b)[0]
    assert result[0] == pytest.approx(0.0)
    assert result[1] == pytest.approx(0.0)
    assert result[2] == pytest.approx(6e-6 / MU_0)


def test_spectral_entropy_separates_tone_from_broadband_impulse() -> None:
    n = 2560
    fs = 256.0
    time = np.arange(n) / fs
    tone = np.sin(2.0 * np.pi * 10.0 * time)
    impulse = np.zeros(n)
    impulse[0] = 1.0
    assert normalized_spectral_entropy(tone) < 1e-10
    assert normalized_spectral_entropy(impulse) > 0.99


def test_phase_concentration_detects_phase_balanced_array() -> None:
    n_sensors = 8
    n = 2560
    fs = 256.0
    time = np.arange(n) / fs
    coherent = np.array([np.sin(2.0 * np.pi * 10.0 * time) for _ in range(n_sensors)])
    phases = 2.0 * np.pi * np.arange(n_sensors) / n_sensors
    balanced = np.array(
        [np.sin(2.0 * np.pi * 10.0 * time + phase) for phase in phases]
    )
    assert spatial_phase_concentration(
        coherent, sample_rate_hz=fs, frequency_hz=10.0
    ) > 0.999999
    assert spatial_phase_concentration(
        balanced, sample_rate_hz=fs, frequency_hz=10.0
    ) < 1e-12


def test_normalized_organization_metrics_are_gain_invariant() -> None:
    n = 2048
    time = np.arange(n) / 256.0
    signals = np.array(
        [
            np.sin(2 * np.pi * 10 * time),
            np.sin(2 * np.pi * 10 * time + 0.4),
            0.6 * np.sin(2 * np.pi * 17 * time + 1.2),
        ]
    )
    assert covariance_effective_rank(signals * 7.0) == pytest.approx(
        covariance_effective_rank(signals)
    )
    assert spatiotemporal_singular_entropy(signals * 7.0) == pytest.approx(
        spatiotemporal_singular_entropy(signals)
    )


def test_common_mode_removal_eliminates_shared_component() -> None:
    n = 1024
    time = np.arange(n) / 256.0
    phases = 2.0 * np.pi * np.arange(8) / 8
    balanced = np.array([np.sin(2 * np.pi * 10 * time + p) for p in phases])
    common = 3.0 * np.sin(2 * np.pi * 10 * time)
    contaminated = balanced + common[None, :]
    assert common_mode_fraction(contaminated) > 0.8
    cleaned = remove_common_mode(contaminated)
    assert common_mode_fraction(cleaned) < 1e-28
