from __future__ import annotations

from statistics import NormalDist

import numpy as np

from .electromagnetic_finite_sample import independent_two_sided_fwer
from .electromagnetic_selection import (
    bonferroni_fwer_union_bound,
    bonferroni_two_sided_z_threshold,
    holm_adjusted_pvalues,
    holm_rejections,
    independent_holdout_selected_type1,
    selected_max_abs_naive_false_positive,
    selected_max_abs_naive_null_coverage,
    sign_flip_max_statistic_distribution,
    sign_flip_max_statistic_pvalue,
)


def v41_arbitrary_dependence_bonferroni(
    *,
    alpha: float = 0.05,
) -> list[dict[str, float]]:
    rows: list[dict[str, float]] = []
    for comparisons in (1, 10, 100, 1000):
        threshold = bonferroni_two_sided_z_threshold(alpha, comparisons)
        rows.append(
            {
                "comparisons": float(comparisons),
                "target_fwer": alpha,
                "two_sided_z_threshold": threshold,
                "union_bound_fwer": bonferroni_fwer_union_bound(
                    threshold,
                    comparisons,
                ),
                "independent_exact_fwer": independent_two_sided_fwer(
                    threshold,
                    comparisons,
                ),
            }
        )
    return rows


def v42_holm_step_down_gain() -> list[dict[str, float]]:
    pvalues = np.asarray([0.001, 0.016, 0.017, 0.5])
    adjusted = holm_adjusted_pvalues(pvalues)
    rejections = holm_rejections(pvalues, 0.05)
    bonferroni_cutoff = 0.05 / pvalues.size
    rows: list[dict[str, float]] = []
    for index, pvalue in enumerate(pvalues):
        rows.append(
            {
                "hypothesis_index": float(index),
                "raw_pvalue": float(pvalue),
                "holm_adjusted_pvalue": float(adjusted[index]),
                "holm_reject": float(rejections[index]),
                "bonferroni_reject": float(pvalue <= bonferroni_cutoff),
            }
        )
    return rows


def v43_exact_sign_flip_max_statistic() -> dict[str, float]:
    observations = np.asarray(
        [
            [1.0, 0.8],
            [1.1, 0.7],
            [0.9, 0.9],
            [1.2, 0.6],
            [0.8, 1.0],
            [1.05, 0.85],
        ]
    )
    distribution = sign_flip_max_statistic_distribution(observations)
    observed = float(np.max(np.abs(np.mean(observations, axis=0))))
    pvalue = sign_flip_max_statistic_pvalue(observations)
    exceedances = int(np.sum(distribution >= observed - 1e-15))
    return {
        "rows": float(observations.shape[0]),
        "sources": float(observations.shape[1]),
        "orbit_size": float(distribution.size),
        "observed_max_abs_mean": observed,
        "exceedances": float(exceedances),
        "exact_randomization_pvalue": pvalue,
    }


def v44_post_selection_coverage_collapse(
    *,
    marginal_coverage: float = 0.95,
) -> list[dict[str, float]]:
    rows: list[dict[str, float]] = []
    for comparisons in (1, 10, 100, 1000):
        coverage = selected_max_abs_naive_null_coverage(
            marginal_coverage,
            comparisons,
        )
        rows.append(
            {
                "comparisons": float(comparisons),
                "marginal_coverage": marginal_coverage,
                "selected_naive_coverage": coverage,
                "selected_false_positive": 1.0 - coverage,
            }
        )
    return rows


def v45_independent_holdout_confirmation(
    *,
    seed: int = 20260918,
    trials: int = 50_000,
    comparisons: int = 100,
    alpha: float = 0.05,
) -> dict[str, float]:
    rng = np.random.default_rng(seed)
    discovery = rng.standard_normal((trials, comparisons))
    selected = np.argmax(np.abs(discovery), axis=1)
    confirmation = rng.standard_normal((trials, comparisons))
    selected_confirmation = confirmation[np.arange(trials), selected]

    threshold = NormalDist().inv_cdf(1.0 - alpha / 2.0)
    reuse_false_positive = float(
        np.mean(np.max(np.abs(discovery), axis=1) > threshold)
    )
    holdout_false_positive = float(
        np.mean(np.abs(selected_confirmation) > threshold)
    )

    return {
        "seed": float(seed),
        "trials": float(trials),
        "comparisons": float(comparisons),
        "target_alpha": alpha,
        "two_sided_z_threshold": threshold,
        "exact_holdout_type1": independent_holdout_selected_type1(alpha),
        "exact_reuse_false_positive": selected_max_abs_naive_false_positive(
            1.0 - alpha,
            comparisons,
        ),
        "empirical_reuse_false_positive": reuse_false_positive,
        "empirical_holdout_false_positive": holdout_false_positive,
    }
