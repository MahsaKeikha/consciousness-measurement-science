"""Synthetic robustness experiments for Research III formal validation V6-V10."""

from __future__ import annotations

import numpy as np

from .latent_measurement import (
    CalibrationBox,
    RateInterval,
    proxy_rate_from_latent_prevalence,
)
from .measurement_robustness import (
    inverse_slope_amplification,
    joint_finite_sample_prevalence_outer_interval,
    missingness_robust_prevalence_outer_interval,
    pooled_two_site_proxy_rate,
    two_site_average_prevalence_identified_interval,
)


def calibration_sample_coverage_experiment(
    *,
    prevalence: float,
    sensitivity: float,
    specificity: float,
    deployment_n: int,
    calibration_sizes: tuple[int, ...],
    repetitions: int,
    delta: float,
    seed: int,
) -> list[dict[str, float]]:
    """Coverage/width when q, sensitivity, and specificity are all estimated."""
    rng = np.random.default_rng(seed)
    q = proxy_rate_from_latent_prevalence(prevalence, sensitivity, specificity)
    rows: list[dict[str, float]] = []
    for n_cal in calibration_sizes:
        hits = 0
        widths: list[float] = []
        identified = 0
        for _ in range(repetitions):
            proxy_successes = int(rng.binomial(deployment_n, q))
            sensitivity_successes = int(rng.binomial(n_cal, sensitivity))
            specificity_successes = int(rng.binomial(n_cal, specificity))
            try:
                interval = joint_finite_sample_prevalence_outer_interval(
                    proxy_successes=proxy_successes,
                    proxy_trials=deployment_n,
                    sensitivity_successes=sensitivity_successes,
                    sensitivity_trials=n_cal,
                    specificity_successes=specificity_successes,
                    specificity_trials=n_cal,
                    delta=delta,
                )
            except ValueError:
                continue
            identified += 1
            widths.append(interval.width)
            hits += int(interval.lower <= prevalence <= interval.upper)
        rows.append(
            {
                "calibration_n_per_class": float(n_cal),
                "identified_rate": identified / repetitions,
                "conditional_coverage": hits / identified if identified else float("nan"),
                "mean_width": float(np.mean(widths)) if widths else float("nan"),
            }
        )
    return rows


def missingness_stress_experiment(
    *,
    prevalence: float,
    sensitivity: float,
    specificity: float,
    total_trials: int,
    missing_fractions: tuple[float, ...],
) -> list[dict[str, float]]:
    """Worst-case interval width as arbitrary missingness increases."""
    q = proxy_rate_from_latent_prevalence(prevalence, sensitivity, specificity)
    calibration = CalibrationBox(
        RateInterval(sensitivity, sensitivity),
        RateInterval(specificity, specificity),
    )
    rows: list[dict[str, float]] = []
    for missing_fraction in missing_fractions:
        observed_trials = round(total_trials * (1.0 - missing_fraction))
        observed_positives = round(observed_trials * q)
        interval = missingness_robust_prevalence_outer_interval(
            observed_positives=observed_positives,
            observed_trials=observed_trials,
            total_trials=total_trials,
            calibration=calibration,
        )
        rows.append(
            {
                "missing_fraction": missing_fraction,
                "lower": interval.lower,
                "upper": interval.upper,
                "width": interval.width,
            }
        )
    return rows


def conditioning_experiment(
    *,
    youden_values: tuple[float, ...],
    proxy_rate_error: float,
) -> list[dict[str, float]]:
    """Exact error amplification versus the Youden identifiability margin."""
    rows: list[dict[str, float]] = []
    for j in youden_values:
        if not 0.0 < j <= 1.0:
            raise ValueError("Youden values must lie in (0,1]")
        sensitivity = (1.0 + j) / 2.0
        specificity = sensitivity
        amplification = inverse_slope_amplification(sensitivity, specificity)
        rows.append(
            {
                "youden": j,
                "amplification": amplification,
                "latent_error_from_proxy_error": amplification * proxy_rate_error,
            }
        )
    return rows


def two_site_nonidentifiability_experiment(
    *,
    pooled_proxy_rates: tuple[float, ...],
    site1_weight: float,
    site1_sensitivity: float,
    site1_specificity: float,
    site2_sensitivity: float,
    site2_specificity: float,
) -> list[dict[str, float]]:
    """Width of the sharp population-average identified set from pooled data only."""
    rows: list[dict[str, float]] = []
    for q_bar in pooled_proxy_rates:
        try:
            identified = two_site_average_prevalence_identified_interval(
                pooled_proxy_rate=q_bar,
                site1_weight=site1_weight,
                site1_sensitivity=site1_sensitivity,
                site1_specificity=site1_specificity,
                site2_sensitivity=site2_sensitivity,
                site2_specificity=site2_specificity,
            )
        except ValueError:
            continue
        rows.append(
            {
                "pooled_proxy_rate": q_bar,
                "average_prevalence_lower": identified.lower,
                "average_prevalence_upper": identified.upper,
                "identified_width": identified.width,
            }
        )
    return rows


def resolution_abstention_frontier(
    *,
    prevalence: float,
    sensitivity: float,
    specificity: float,
    deployment_sizes: tuple[int, ...],
    calibration_n_per_class: int,
    repetitions: int,
    delta: float,
    maximum_width: float,
    seed: int,
) -> list[dict[str, float]]:
    """Rate at which finite-sample evidence licenses a predeclared resolution target."""
    rng = np.random.default_rng(seed)
    q = proxy_rate_from_latent_prevalence(prevalence, sensitivity, specificity)
    rows: list[dict[str, float]] = []
    for deployment_n in deployment_sizes:
        identifiable = 0
        claims = 0
        covered_claims = 0
        widths: list[float] = []
        for _ in range(repetitions):
            proxy_successes = int(rng.binomial(deployment_n, q))
            sensitivity_successes = int(
                rng.binomial(calibration_n_per_class, sensitivity)
            )
            specificity_successes = int(
                rng.binomial(calibration_n_per_class, specificity)
            )
            try:
                interval = joint_finite_sample_prevalence_outer_interval(
                    proxy_successes=proxy_successes,
                    proxy_trials=deployment_n,
                    sensitivity_successes=sensitivity_successes,
                    sensitivity_trials=calibration_n_per_class,
                    specificity_successes=specificity_successes,
                    specificity_trials=calibration_n_per_class,
                    delta=delta,
                )
            except ValueError:
                continue
            identifiable += 1
            widths.append(interval.width)
            if interval.width <= maximum_width:
                claims += 1
                covered_claims += int(interval.lower <= prevalence <= interval.upper)
        rows.append(
            {
                "deployment_n": float(deployment_n),
                "identifiable_rate": identifiable / repetitions,
                "resolution_claim_rate": claims / repetitions,
                "conditional_claim_coverage": (
                    covered_claims / claims if claims else float("nan")
                ),
                "mean_width_when_identified": (
                    float(np.mean(widths)) if widths else float("nan")
                ),
            }
        )
    return rows


def canonical_two_site_counterexample() -> dict[str, float]:
    """Two latent populations with identical pooled proxy rate but different averages."""
    common = {
        "site1_weight": 0.5,
        "site1_sensitivity": 0.9,
        "site1_specificity": 0.9,
        "site2_sensitivity": 0.7,
        "site2_specificity": 0.8,
    }
    q_a = pooled_two_site_proxy_rate(
        site1_prevalence=0.75,
        site2_prevalence=0.0,
        **common,
    )
    q_b = pooled_two_site_proxy_rate(
        site1_prevalence=0.125,
        site2_prevalence=1.0,
        **common,
    )
    return {
        "pooled_proxy_rate_a": q_a,
        "pooled_proxy_rate_b": q_b,
        "average_prevalence_a": 0.375,
        "average_prevalence_b": 0.5625,
        "average_prevalence_gap": 0.1875,
    }
