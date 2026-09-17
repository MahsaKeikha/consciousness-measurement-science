"""Deterministic and fixed-seed experiments for Research III V11-V15."""

from __future__ import annotations

import numpy as np

from .identification_design import (
    hoeffding_resolution_sample_size,
    interior_missingness_width,
    multisite_average_prevalence_identified_interval,
)
from .latent_measurement import (
    CalibrationBox,
    RateInterval,
    finite_sample_prevalence_outer_interval,
    proxy_rate_from_latent_prevalence,
)
from .measurement_robustness import joint_finite_sample_prevalence_outer_interval


def missingness_information_design_grid(
    *,
    missing_fractions: tuple[float, ...],
    youden_values: tuple[float, ...],
) -> list[dict[str, float]]:
    """V11 exact interior resolution law across missingness and channel strength."""
    rows: list[dict[str, float]] = []
    total = 10_000
    for j in youden_values:
        sensitivity = (1.0 + j) / 2.0
        specificity = sensitivity
        for missing_fraction in missing_fractions:
            missing = round(total * missing_fraction)
            rows.append(
                {
                    "youden": j,
                    "missing_fraction": missing_fraction,
                    "interior_latent_width": interior_missingness_width(
                        missing_trials=missing,
                        total_trials=total,
                        sensitivity=sensitivity,
                        specificity=specificity,
                    ),
                }
            )
    return rows


def multisite_heterogeneity_design_grid(
    *,
    spreads: tuple[float, ...],
) -> list[dict[str, float]]:
    """V12-V13 width induced by heterogeneous site information margins."""
    weights = (0.3, 0.3, 0.4)
    specificities = (0.9, 0.9, 0.9)
    prevalence = (0.2, 0.5, 0.8)
    rows: list[dict[str, float]] = []
    for spread in spreads:
        margins = (0.6 + spread, 0.6, 0.6 - spread)
        sensitivities = tuple(j + 0.1 for j in margins)
        pooled_q = sum(
            w * proxy_rate_from_latent_prevalence(pi, se, sp)
            for w, pi, se, sp in zip(
                weights,
                prevalence,
                sensitivities,
                specificities,
                strict=True,
            )
        )
        identified = multisite_average_prevalence_identified_interval(
            pooled_proxy_rate=pooled_q,
            weights=weights,
            sensitivities=sensitivities,
            specificities=specificities,
        )
        rows.append(
            {
                "youden_spread": spread,
                "pooled_proxy_rate": pooled_q,
                "true_average_prevalence": sum(
                    w * pi for w, pi in zip(weights, prevalence, strict=True)
                ),
                "identified_lower": identified.lower,
                "identified_upper": identified.upper,
                "identified_width": identified.width,
            }
        )
    return rows


def resolution_sample_size_design_grid(
    *,
    youden_values: tuple[float, ...],
    maximum_widths: tuple[float, ...],
    delta: float,
) -> list[dict[str, float]]:
    """V14 sufficient deployment sample sizes for declared resolution targets."""
    rows: list[dict[str, float]] = []
    for j in youden_values:
        sensitivity = (1.0 + j) / 2.0
        specificity = sensitivity
        for maximum_width in maximum_widths:
            rows.append(
                {
                    "youden": j,
                    "maximum_width": maximum_width,
                    "required_n": float(
                        hoeffding_resolution_sample_size(
                            sensitivity=sensitivity,
                            specificity=specificity,
                            maximum_width=maximum_width,
                            delta=delta,
                        )
                    ),
                }
            )
    return rows


def independent_pilot_gate_experiment(
    *,
    prevalence: float,
    sensitivity: float,
    specificity: float,
    pilot_calibration_n_per_class: int,
    confirm_deployment_n: int,
    confirm_calibration_n_per_class: int,
    maximum_width: float,
    repetitions: int,
    delta: float,
    seed: int,
) -> dict[str, float]:
    """V15 fixed-seed check of conditional coverage under an independent pilot gate.

    The pilot data are used only to decide whether the planned confirmatory design
    appears capable of meeting the resolution target. All data entering the final
    confirmatory interval are generated independently after the gate decision.
    """
    rng = np.random.default_rng(seed)
    q = proxy_rate_from_latent_prevalence(prevalence, sensitivity, specificity)
    released = 0
    confirm_identified = 0
    covered = 0

    for _ in range(repetitions):
        pilot_se = int(rng.binomial(pilot_calibration_n_per_class, sensitivity))
        pilot_sp = int(rng.binomial(pilot_calibration_n_per_class, specificity))
        se_hat = pilot_se / pilot_calibration_n_per_class
        sp_hat = pilot_sp / pilot_calibration_n_per_class
        pilot_j = se_hat + sp_hat - 1.0
        if pilot_j <= 0.0:
            continue
        try:
            required_n = hoeffding_resolution_sample_size(
                sensitivity=se_hat,
                specificity=sp_hat,
                maximum_width=maximum_width,
                delta=delta,
            )
        except ValueError:
            continue
        if required_n > confirm_deployment_n:
            continue
        released += 1

        proxy_successes = int(rng.binomial(confirm_deployment_n, q))
        confirm_se = int(rng.binomial(confirm_calibration_n_per_class, sensitivity))
        confirm_sp = int(rng.binomial(confirm_calibration_n_per_class, specificity))
        try:
            interval = joint_finite_sample_prevalence_outer_interval(
                proxy_successes=proxy_successes,
                proxy_trials=confirm_deployment_n,
                sensitivity_successes=confirm_se,
                sensitivity_trials=confirm_calibration_n_per_class,
                specificity_successes=confirm_sp,
                specificity_trials=confirm_calibration_n_per_class,
                delta=delta,
            )
        except ValueError:
            continue
        confirm_identified += 1
        covered += int(interval.lower <= prevalence <= interval.upper)

    return {
        "release_rate": released / repetitions,
        "confirm_identified_rate": confirm_identified / repetitions,
        "conditional_coverage_given_release_and_identification": (
            covered / confirm_identified if confirm_identified else float("nan")
        ),
        "released_runs": float(released),
        "identified_confirmatory_runs": float(confirm_identified),
    }


def point_calibration_coverage_experiment(
    *,
    prevalence: float,
    sensitivity: float,
    specificity: float,
    deployment_n: int,
    repetitions: int,
    delta: float,
    seed: int,
) -> float:
    """Reference coverage check for V14 under point-known calibration."""
    rng = np.random.default_rng(seed)
    q = proxy_rate_from_latent_prevalence(prevalence, sensitivity, specificity)
    calibration = CalibrationBox(
        RateInterval(sensitivity, sensitivity),
        RateInterval(specificity, specificity),
    )
    hits = 0
    for _ in range(repetitions):
        successes = int(rng.binomial(deployment_n, q))
        interval = finite_sample_prevalence_outer_interval(
            successes,
            deployment_n,
            calibration,
            delta=delta,
        )
        hits += int(interval.lower <= prevalence <= interval.upper)
    return hits / repetitions
