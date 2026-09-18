"""Deterministic electromagnetic validation experiments for Research III V16-V20."""

from __future__ import annotations

import numpy as np

from .electromagnetic_observables import (
    electromagnetic_feature_profile,
    field_energy_density,
    frequency_power_per_channel,
    poynting_vector,
    remove_common_mode,
    spatial_phase_concentration,
)


def phase_structured_fields(
    *,
    n_sensors: int = 8,
    n_samples: int = 2560,
    sample_rate_hz: float = 256.0,
    frequency_hz: float = 10.0,
) -> tuple[np.ndarray, np.ndarray]:
    """Construct matched-power coherent and phase-balanced sensor fields."""
    if n_sensors < 4:
        raise ValueError("n_sensors must be at least four")
    time = np.arange(n_samples) / sample_rate_hz
    coherent_phases = np.zeros(n_sensors)
    balanced_phases = 2.0 * np.pi * np.arange(n_sensors) / n_sensors
    coherent = np.array(
        [np.sin(2.0 * np.pi * frequency_hz * time + phase) for phase in coherent_phases]
    )
    balanced = np.array(
        [np.sin(2.0 * np.pi * frequency_hz * time + phase) for phase in balanced_phases]
    )
    return coherent, balanced


def v16_field_identity() -> dict[str, float]:
    """Exact physical sanity check for vacuum field energy and flux."""
    e = np.array([[2.0, 0.0, 0.0]])
    b = np.array([[0.0, 3e-6, 0.0]])
    energy = field_energy_density(e, b)[0]
    flux = poynting_vector(e, b)[0]
    return {
        "energy_density_j_m3": float(energy),
        "poynting_x_w_m2": float(flux[0]),
        "poynting_y_w_m2": float(flux[1]),
        "poynting_z_w_m2": float(flux[2]),
    }


def v17_scale_invariance() -> list[dict[str, float]]:
    """Show normalized organization features are invariant to global gain."""
    coherent, _ = phase_structured_fields()
    rows: list[dict[str, float]] = []
    for scale in (0.1, 1.0, 10.0):
        profile = electromagnetic_feature_profile(
            coherent * scale,
            sample_rate_hz=256.0,
            reference_frequency_hz=10.0,
        )
        rows.append(
            {
                "scale": scale,
                "spectral_entropy": profile.spectral_entropy,
                "phase_concentration": profile.spatial_phase_concentration,
                "effective_rank": profile.covariance_effective_rank,
                "singular_entropy": profile.spatiotemporal_singular_entropy,
                "common_mode_fraction": profile.common_mode_fraction,
            }
        )
    return rows


def v18_power_nonidentifiability() -> dict[str, float]:
    """Matched channel power can hide radically different spatial phase structure."""
    coherent, balanced = phase_structured_fields()
    p_coherent = frequency_power_per_channel(
        coherent, sample_rate_hz=256.0, frequency_hz=10.0
    )
    p_balanced = frequency_power_per_channel(
        balanced, sample_rate_hz=256.0, frequency_hz=10.0
    )
    coherent_profile = electromagnetic_feature_profile(
        coherent, sample_rate_hz=256.0, reference_frequency_hz=10.0
    )
    balanced_profile = electromagnetic_feature_profile(
        balanced, sample_rate_hz=256.0, reference_frequency_hz=10.0
    )
    return {
        "max_relative_channel_power_difference": float(
            np.max(np.abs(p_coherent - p_balanced) / np.maximum(p_coherent, 1e-30))
        ),
        "coherent_phase_concentration": coherent_profile.spatial_phase_concentration,
        "balanced_phase_concentration": balanced_profile.spatial_phase_concentration,
        "coherent_effective_rank": coherent_profile.covariance_effective_rank,
        "balanced_effective_rank": balanced_profile.covariance_effective_rank,
    }


def v19_common_mode_confound() -> list[dict[str, float]]:
    """Quantify how a shared contaminant can mimic sensor-wide phase organization."""
    _, balanced = phase_structured_fields()
    time = np.arange(balanced.shape[1]) / 256.0
    common = np.sin(2.0 * np.pi * 10.0 * time)
    rows: list[dict[str, float]] = []
    for amplitude in (0.0, 0.25, 0.5, 1.0, 2.0):
        contaminated = balanced + amplitude * common[None, :]
        before = spatial_phase_concentration(
            contaminated, sample_rate_hz=256.0, frequency_hz=10.0
        )
        cleaned = remove_common_mode(contaminated)
        after = spatial_phase_concentration(
            cleaned, sample_rate_hz=256.0, frequency_hz=10.0
        )
        rows.append(
            {
                "common_mode_amplitude": amplitude,
                "phase_concentration_raw": before,
                "phase_concentration_after_common_mode_removal": after,
            }
        )
    return rows


def v20_frequency_specific_structure() -> list[dict[str, float]]:
    """Show that field organization must be declared frequency-by-frequency."""
    n_sensors = 8
    n_samples = 2560
    sample_rate = 256.0
    time = np.arange(n_samples) / sample_rate
    balanced_phases = 2.0 * np.pi * np.arange(n_sensors) / n_sensors
    signals = np.array(
        [
            np.sin(2.0 * np.pi * 10.0 * time)
            + 0.8 * np.sin(2.0 * np.pi * 17.0 * time + phase)
            for phase in balanced_phases
        ]
    )
    return [
        {
            "frequency_hz": frequency,
            "phase_concentration": spatial_phase_concentration(
                signals,
                sample_rate_hz=sample_rate,
                frequency_hz=frequency,
            ),
        }
        for frequency in (10.0, 17.0)
    ]
