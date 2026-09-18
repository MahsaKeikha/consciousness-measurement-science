"""Electromagnetic observable utilities for Research III V16-V20.

This module treats electromagnetic recordings as one possible evidence channel.
It computes physical field quantities and dimensionless descriptors of
multichannel field organization. None of the functions maps an electromagnetic
quantity directly to consciousness.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

EPSILON_0 = 8.8541878128e-12
MU_0 = 1.25663706212e-6


@dataclass(frozen=True)
class ElectromagneticFeatureProfile:
    """Dimensionless organization features for a multichannel field window."""

    spectral_entropy: float
    spatial_phase_concentration: float
    covariance_effective_rank: float
    spatiotemporal_singular_entropy: float
    common_mode_fraction: float


def field_energy_density(
    electric_field_v_per_m: np.ndarray,
    magnetic_field_t: np.ndarray,
) -> np.ndarray:
    """Return vacuum electromagnetic energy density in J/m^3.

    Inputs must have identical shape (..., 3), with the final axis representing
    Cartesian vector components.
    """
    e = np.asarray(electric_field_v_per_m, dtype=float)
    b = np.asarray(magnetic_field_t, dtype=float)
    if e.shape != b.shape or e.ndim < 1 or e.shape[-1] != 3:
        raise ValueError("electric and magnetic fields must have identical shape (..., 3)")
    e2 = np.sum(e * e, axis=-1)
    b2 = np.sum(b * b, axis=-1)
    return 0.5 * (EPSILON_0 * e2 + b2 / MU_0)


def poynting_vector(
    electric_field_v_per_m: np.ndarray,
    magnetic_field_t: np.ndarray,
) -> np.ndarray:
    """Return the vacuum Poynting vector E x B / mu0 in W/m^2."""
    e = np.asarray(electric_field_v_per_m, dtype=float)
    b = np.asarray(magnetic_field_t, dtype=float)
    if e.shape != b.shape or e.ndim < 1 or e.shape[-1] != 3:
        raise ValueError("electric and magnetic fields must have identical shape (..., 3)")
    return np.cross(e, b) / MU_0


def normalized_spectral_entropy(signal: np.ndarray) -> float:
    """Return Shannon entropy of positive-frequency power, normalized to [0, 1]."""
    x = np.asarray(signal, dtype=float)
    if x.ndim != 1 or x.size < 4:
        raise ValueError("signal must be one-dimensional with at least four samples")
    x = x - np.mean(x)
    power = np.abs(np.fft.rfft(x)) ** 2
    if power.size <= 1:
        raise ValueError("signal does not contain positive-frequency bins")
    power = power[1:]
    total = float(np.sum(power))
    if not np.isfinite(total) or total <= 0.0:
        raise ValueError("signal must contain nonzero finite variation")
    probabilities = power / total
    positive = probabilities > 0.0
    entropy = -float(np.sum(probabilities[positive] * np.log(probabilities[positive])))
    return entropy / float(np.log(probabilities.size))


def spatial_phase_concentration(
    signals: np.ndarray,
    *,
    sample_rate_hz: float,
    frequency_hz: float,
) -> float:
    """Return concentration of sensor phases at one declared frequency.

    The statistic is |mean(exp(i*phi_k))| over sensors, where phi_k is the phase
    of the Fourier coefficient nearest the declared frequency. It equals one
    when all measured channels have the same phase and approaches zero for
    phase-balanced sensor arrays.

    This is a sensor-level descriptor, not a connectivity estimator. Shared
    sources, reference choices, field spread, or environmental interference can
    inflate it.
    """
    x = _validate_signals(signals)
    if sample_rate_hz <= 0.0:
        raise ValueError("sample_rate_hz must be positive")
    nyquist = sample_rate_hz / 2.0
    if not 0.0 < frequency_hz < nyquist:
        raise ValueError("frequency_hz must lie strictly between zero and Nyquist")

    centered = x - np.mean(x, axis=1, keepdims=True)
    n = centered.shape[1]
    frequencies = np.fft.rfftfreq(n, d=1.0 / sample_rate_hz)
    index = int(np.argmin(np.abs(frequencies - frequency_hz)))
    coefficients = np.fft.rfft(centered, axis=1)[:, index]
    magnitudes = np.abs(coefficients)
    if np.any(magnitudes <= np.finfo(float).eps):
        raise ValueError("declared frequency has negligible amplitude in at least one channel")
    unit_phases = coefficients / magnitudes
    return float(np.abs(np.mean(unit_phases)))


def frequency_power_per_channel(
    signals: np.ndarray,
    *,
    sample_rate_hz: float,
    frequency_hz: float,
) -> np.ndarray:
    """Return Fourier power at the nearest declared frequency for each channel."""
    x = _validate_signals(signals)
    if sample_rate_hz <= 0.0:
        raise ValueError("sample_rate_hz must be positive")
    if not 0.0 < frequency_hz < sample_rate_hz / 2.0:
        raise ValueError("frequency_hz must lie strictly between zero and Nyquist")
    centered = x - np.mean(x, axis=1, keepdims=True)
    frequencies = np.fft.rfftfreq(centered.shape[1], d=1.0 / sample_rate_hz)
    index = int(np.argmin(np.abs(frequencies - frequency_hz)))
    coefficients = np.fft.rfft(centered, axis=1)[:, index]
    return np.abs(coefficients) ** 2


def covariance_effective_rank(signals: np.ndarray) -> float:
    """Return exp(entropy) of normalized covariance eigenvalues."""
    x = _validate_signals(signals)
    centered = x - np.mean(x, axis=1, keepdims=True)
    covariance = centered @ centered.T / centered.shape[1]
    eigenvalues = np.linalg.eigvalsh(covariance)
    eigenvalues = np.clip(eigenvalues, 0.0, None)
    total = float(np.sum(eigenvalues))
    if total <= np.finfo(float).eps:
        raise ValueError("signals must contain nonzero variance")
    probabilities = eigenvalues / total
    positive = probabilities > np.finfo(float).eps
    entropy = -float(np.sum(probabilities[positive] * np.log(probabilities[positive])))
    return float(np.exp(entropy))


def spatiotemporal_singular_entropy(signals: np.ndarray) -> float:
    """Return normalized entropy of singular-value energy in a sensor-time window."""
    x = _validate_signals(signals)
    centered = x - np.mean(x, axis=1, keepdims=True)
    singular_values = np.linalg.svd(centered, compute_uv=False)
    energy = singular_values**2
    total = float(np.sum(energy))
    if total <= np.finfo(float).eps:
        raise ValueError("signals must contain nonzero variance")
    probabilities = energy / total
    positive = probabilities > np.finfo(float).eps
    entropy = -float(np.sum(probabilities[positive] * np.log(probabilities[positive])))
    denominator = np.log(min(centered.shape))
    if denominator <= 0.0:
        return 0.0
    return entropy / float(denominator)


def common_mode_fraction(signals: np.ndarray) -> float:
    """Return variance of the sensor mean divided by mean channel variance."""
    x = _validate_signals(signals)
    centered = x - np.mean(x, axis=1, keepdims=True)
    channel_variance = np.mean(centered**2, axis=1)
    denominator = float(np.mean(channel_variance))
    if denominator <= np.finfo(float).eps:
        raise ValueError("signals must contain nonzero variance")
    common = np.mean(centered, axis=0)
    return float(np.mean(common**2) / denominator)


def remove_common_mode(signals: np.ndarray) -> np.ndarray:
    """Subtract the instantaneous sensor average from every channel."""
    x = _validate_signals(signals)
    return x - np.mean(x, axis=0, keepdims=True)


def electromagnetic_feature_profile(
    signals: np.ndarray,
    *,
    sample_rate_hz: float,
    reference_frequency_hz: float,
) -> ElectromagneticFeatureProfile:
    """Compute a compact field-organization profile for a declared time window."""
    x = _validate_signals(signals)
    mean_spectral_entropy = float(
        np.mean([normalized_spectral_entropy(channel) for channel in x])
    )
    return ElectromagneticFeatureProfile(
        spectral_entropy=mean_spectral_entropy,
        spatial_phase_concentration=spatial_phase_concentration(
            x,
            sample_rate_hz=sample_rate_hz,
            frequency_hz=reference_frequency_hz,
        ),
        covariance_effective_rank=covariance_effective_rank(x),
        spatiotemporal_singular_entropy=spatiotemporal_singular_entropy(x),
        common_mode_fraction=common_mode_fraction(x),
    )


def _validate_signals(signals: np.ndarray) -> np.ndarray:
    x = np.asarray(signals, dtype=float)
    if x.ndim != 2:
        raise ValueError("signals must have shape (channels, samples)")
    if x.shape[0] < 2 or x.shape[1] < 4:
        raise ValueError("signals require at least two channels and four samples")
    if not np.all(np.isfinite(x)):
        raise ValueError("signals must contain only finite values")
    return x
