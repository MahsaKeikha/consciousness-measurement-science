"""Deterministic simulation experiments for Research III measurement validation."""

from __future__ import annotations

from dataclasses import dataclass
from math import prod

import numpy as np

from .latent_measurement import (
    CalibrationBox,
    RateInterval,
    finite_sample_prevalence_outer_interval,
    proxy_rate_from_latent_prevalence,
    transport_bias_from_calibration_shift,
)


@dataclass(frozen=True)
class ChannelCalibration:
    sensitivity: float
    specificity: float


def exact_all_positive_posterior_with_shared_uniform_dependence(
    prior: float,
    channels: tuple[ChannelCalibration, ...],
    dependence: float,
) -> float:
    """Exact posterior for the all-positive pattern under a dependence mixture.

    With probability ``dependence``, all channels use a shared U~Uniform(0,1),
    and otherwise use independent uniforms. This preserves every channel marginal
    exactly while increasing positive conditional dependence.
    """
    if not 0.0 < prior < 1.0:
        raise ValueError("prior must lie strictly between zero and one")
    if not 0.0 <= dependence <= 1.0:
        raise ValueError("dependence must lie in [0, 1]")
    if not channels:
        raise ValueError("at least one channel is required")

    p_target = tuple(channel.sensitivity for channel in channels)
    p_nontarget = tuple(1.0 - channel.specificity for channel in channels)

    target_pattern = dependence * min(p_target) + (1.0 - dependence) * prod(p_target)
    nontarget_pattern = dependence * min(p_nontarget) + (1.0 - dependence) * prod(p_nontarget)
    numerator = prior * target_pattern
    denominator = numerator + (1.0 - prior) * nontarget_pattern
    return numerator / denominator


def naive_independence_all_positive_posterior(
    prior: float,
    channels: tuple[ChannelCalibration, ...],
) -> float:
    """Posterior obtained by multiplying channel likelihood ratios."""
    target_pattern = prod(channel.sensitivity for channel in channels)
    nontarget_pattern = prod(1.0 - channel.specificity for channel in channels)
    numerator = prior * target_pattern
    denominator = numerator + (1.0 - prior) * nontarget_pattern
    return numerator / denominator


def finite_sample_coverage_experiment(
    *,
    prevalence: float,
    sensitivity: float,
    specificity: float,
    calibration_half_width: float,
    sample_sizes: tuple[int, ...],
    repetitions: int,
    delta: float,
    seed: int,
) -> list[dict[str, float]]:
    """Monte Carlo coverage and width of the finite-sample outer interval."""
    rng = np.random.default_rng(seed)
    q = proxy_rate_from_latent_prevalence(prevalence, sensitivity, specificity)
    calibration = CalibrationBox(
        sensitivity=RateInterval(
            max(0.0, sensitivity - calibration_half_width),
            min(1.0, sensitivity + calibration_half_width),
        ),
        specificity=RateInterval(
            max(0.0, specificity - calibration_half_width),
            min(1.0, specificity + calibration_half_width),
        ),
    )
    rows: list[dict[str, float]] = []
    for n in sample_sizes:
        hits = 0
        widths: list[float] = []
        for _ in range(repetitions):
            successes = int(rng.binomial(n, q))
            interval = finite_sample_prevalence_outer_interval(
                successes,
                n,
                calibration,
                delta=delta,
            )
            hits += int(interval.lower <= prevalence <= interval.upper)
            widths.append(interval.width)
        rows.append(
            {
                "n": float(n),
                "coverage": hits / repetitions,
                "mean_width": float(np.mean(widths)),
                "median_width": float(np.median(widths)),
            }
        )
    return rows


def dependence_stress_experiment(
    *,
    prior: float,
    channels: tuple[ChannelCalibration, ...],
    dependence_grid: tuple[float, ...],
) -> list[dict[str, float]]:
    """Quantify overconfidence induced by a false conditional-independence assumption."""
    naive = naive_independence_all_positive_posterior(prior, channels)
    rows: list[dict[str, float]] = []
    for rho in dependence_grid:
        truth = exact_all_positive_posterior_with_shared_uniform_dependence(
            prior,
            channels,
            rho,
        )
        rows.append(
            {
                "dependence": rho,
                "true_posterior": truth,
                "naive_independence_posterior": naive,
                "absolute_error": abs(naive - truth),
            }
        )
    return rows


def transport_stress_experiment(
    *,
    latent_prevalence_after: float,
    baseline_sensitivity: float,
    baseline_specificity: float,
    sensitivity_shifts: tuple[float, ...],
    specificity_shifts: tuple[float, ...],
) -> list[dict[str, float]]:
    """Evaluate exact contrast bias under calibration transport failure."""
    rows: list[dict[str, float]] = []
    for ds in sensitivity_shifts:
        for dc in specificity_shifts:
            shifted_sensitivity = min(1.0, max(0.0, baseline_sensitivity + ds))
            shifted_specificity = min(1.0, max(0.0, baseline_specificity + dc))
            bias = transport_bias_from_calibration_shift(
                latent_prevalence_after,
                baseline_sensitivity,
                baseline_specificity,
                shifted_sensitivity,
                shifted_specificity,
            )
            rows.append(
                {
                    "sensitivity_shift": ds,
                    "specificity_shift": dc,
                    "bias": bias,
                    "absolute_bias": abs(bias),
                }
            )
    return rows


def structural_alignment_power_experiment(
    *,
    signal_levels: tuple[float, ...],
    replicates: int,
    items: int,
    dimensions: int,
    permutations: int,
    alpha: float,
    seed: int,
) -> list[dict[str, float]]:
    """Permutation-test null/power experiment for relational-geometry alignment."""
    if not 0.0 < alpha < 1.0:
        raise ValueError("alpha must lie strictly between zero and one")
    rng = np.random.default_rng(seed)
    rows: list[dict[str, float]] = []
    for signal in signal_levels:
        if not 0.0 <= signal <= 1.0:
            raise ValueError("signal levels must lie in [0,1]")
        rejections = 0
        observed_alignments: list[float] = []
        for _ in range(replicates):
            latent = rng.normal(size=(items, dimensions))
            independent = rng.normal(size=(items, dimensions))
            neural = signal * latent + np.sqrt(max(0.0, 1.0 - signal**2)) * independent
            phenomenal_distances = _distance_matrix(latent)
            neural_distances = _distance_matrix(neural)
            observed = _matrix_alignment(phenomenal_distances, neural_distances)
            observed_alignments.append(observed)

            exceed = 0
            for _ in range(permutations):
                order = rng.permutation(items)
                permuted = neural_distances[np.ix_(order, order)]
                if _matrix_alignment(phenomenal_distances, permuted) >= observed:
                    exceed += 1
            p_value = (exceed + 1) / (permutations + 1)
            rejections += int(p_value <= alpha)

        rows.append(
            {
                "signal": signal,
                "rejection_rate": rejections / replicates,
                "mean_alignment": float(np.mean(observed_alignments)),
            }
        )
    return rows


def _distance_matrix(features: np.ndarray) -> np.ndarray:
    diff = features[:, None, :] - features[None, :, :]
    return np.sqrt(np.sum(diff * diff, axis=-1))


def _matrix_alignment(a: np.ndarray, b: np.ndarray) -> float:
    idx = np.triu_indices(a.shape[0], k=1)
    return float(np.corrcoef(a[idx], b[idx])[0, 1])
