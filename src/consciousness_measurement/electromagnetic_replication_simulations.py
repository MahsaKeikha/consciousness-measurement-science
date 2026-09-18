from __future__ import annotations

import numpy as np

from . import electromagnetic_replication as replication


ESTIMATES = np.asarray([0.42, 0.55, 0.37, 0.48])
STANDARD_ERRORS = np.asarray([0.12, 0.18, 0.10, 0.15])


def v46_common_effect_pooling() -> dict[str, float]:
    pooled, pooled_se = replication.common_effect_estimate(ESTIMATES, STANDARD_ERRORS)
    return {
        "pooled_estimate": pooled,
        "pooled_standard_error": pooled_se,
        "pooled_variance": pooled_se**2,
        "site_count": float(ESTIMATES.size),
    }


def v47_common_effect_heterogeneity(
    *,
    seed: int = 20260918,
    simulations: int = 50000,
) -> dict[str, float]:
    pooled, _ = replication.common_effect_estimate(ESTIMATES, STANDARD_ERRORS)
    observed_q = replication.cochran_q_known_variance(ESTIMATES, STANDARD_ERRORS)

    rng = np.random.default_rng(seed)
    samples = rng.normal(
        loc=pooled,
        scale=STANDARD_ERRORS,
        size=(simulations, ESTIMATES.size),
    )
    weights = 1.0 / np.square(STANDARD_ERRORS)
    total_weight = float(np.sum(weights))
    simulated_pooled = (samples * weights).sum(axis=1) / total_weight
    simulated_q = (
        np.square(samples - simulated_pooled[:, None]) * weights
    ).sum(axis=1)

    degrees_of_freedom = ESTIMATES.size - 1
    return {
        "observed_q": observed_q,
        "degrees_of_freedom": float(degrees_of_freedom),
        "simulated_mean_q": float(np.mean(simulated_q)),
        "theoretical_mean_q": float(degrees_of_freedom),
        "simulated_variance_q": float(np.var(simulated_q)),
        "theoretical_variance_q": float(2 * degrees_of_freedom),
        "seed": float(seed),
        "simulations": float(simulations),
    }


def v48_leave_one_site_out_influence() -> list[dict[str, float]]:
    pooled, _ = replication.common_effect_estimate(ESTIMATES, STANDARD_ERRORS)
    delete_estimates = replication.leave_one_site_out_estimates(ESTIMATES, STANDARD_ERRORS)
    identity_shifts = replication.leave_one_site_out_shift_identity(ESTIMATES, STANDARD_ERRORS)
    return [
        {
            "site_index": float(index),
            "site_estimate": float(ESTIMATES[index]),
            "leave_one_out_estimate": float(delete_estimates[index]),
            "leave_one_out_shift": float(delete_estimates[index] - pooled),
            "identity_shift": float(identity_shifts[index]),
        }
        for index in range(ESTIMATES.size)
    ]


def v49_partial_conjunction_replicability() -> list[dict[str, float]]:
    p_values = np.asarray([0.001, 0.012, 0.04, 0.21, 0.45])
    ordered = np.sort(p_values)
    return [
        {
            "required_nonnulls": float(required),
            "ordered_p_value": float(ordered[required - 1]),
            "partial_conjunction_p_value": replication.bonferroni_partial_conjunction_pvalue(
                p_values,
                required,
            ),
        }
        for required in range(1, p_values.size + 1)
    ]


def v50_site_weight_concentration() -> list[dict[str, float | str]]:
    designs = {
        "balanced": np.asarray([0.10, 0.10, 0.10, 0.10]),
        "dominant_site": np.asarray([0.05, 0.20, 0.20, 0.20]),
    }
    rows: list[dict[str, float | str]] = []
    for name, standard_errors in designs.items():
        weights = replication.normalized_site_weights(standard_errors)
        inflations = replication.delete_site_variance_inflation(standard_errors)
        rows.append(
            {
                "design": name,
                "effective_site_count": replication.effective_site_count(standard_errors),
                "maximum_normalized_weight": float(np.max(weights)),
                "maximum_delete_variance_inflation": float(np.max(inflations)),
            }
        )
    return rows
