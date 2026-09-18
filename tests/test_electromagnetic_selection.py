from __future__ import annotations

from statistics import NormalDist

import numpy as np
import pytest

from consciousness_measurement.electromagnetic_selection import (
    bonferroni_fwer_union_bound,
    bonferroni_two_sided_z_threshold,
    holm_adjusted_pvalues,
    holm_rejections,
    independent_holdout_selected_type1,
    selected_max_abs_naive_false_positive,
    selected_max_abs_naive_null_coverage,
    sign_flip_max_statistic_distribution,
    sign_flip_max_statistic_pvalue,
    two_sided_standard_normal_tail,
)


def test_bonferroni_threshold_controls_union_bound_at_target_alpha() -> None:
    alpha = 0.05
    for comparisons in (1, 10, 100, 1000):
        threshold = bonferroni_two_sided_z_threshold(alpha, comparisons)
        bound = bonferroni_fwer_union_bound(threshold, comparisons)
        assert bound == pytest.approx(alpha, abs=2e-13)


def test_single_bonferroni_threshold_matches_standard_normal_interval() -> None:
    threshold = bonferroni_two_sided_z_threshold(0.05, 1)
    assert threshold == pytest.approx(NormalDist().inv_cdf(0.975))
    assert two_sided_standard_normal_tail(threshold) == pytest.approx(0.05)


def test_holm_adjusted_pvalues_are_monotone_in_sorted_order() -> None:
    pvalues = np.asarray([0.001, 0.016, 0.017, 0.5])
    adjusted = holm_adjusted_pvalues(pvalues)
    assert adjusted == pytest.approx([0.004, 0.048, 0.048, 0.5])
    assert holm_rejections(pvalues, 0.05).tolist() == [True, True, True, False]


def test_holm_can_reject_more_than_single_step_bonferroni() -> None:
    pvalues = np.asarray([0.001, 0.016, 0.017, 0.5])
    holm = holm_rejections(pvalues, 0.05)
    bonferroni = pvalues <= 0.05 / pvalues.size
    assert int(np.sum(holm)) == 3
    assert int(np.sum(bonferroni)) == 1


def test_exact_sign_flip_orbit_has_power_of_two_size() -> None:
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
    assert distribution.size == 64
    assert np.all(np.isfinite(distribution))
    assert sign_flip_max_statistic_pvalue(observations) == pytest.approx(0.03125)


def test_selected_max_abs_naive_coverage_has_exact_independent_null_law() -> None:
    assert selected_max_abs_naive_null_coverage(0.95, 1) == pytest.approx(0.95)
    assert selected_max_abs_naive_null_coverage(0.95, 10) == pytest.approx(
        0.5987369392383787
    )
    assert selected_max_abs_naive_null_coverage(0.95, 100) == pytest.approx(
        0.0059205292203339975
    )
    assert selected_max_abs_naive_false_positive(0.95, 100) == pytest.approx(
        0.994079470779666
    )


def test_independent_holdout_restores_nominal_type1_after_selection() -> None:
    assert independent_holdout_selected_type1(0.05) == pytest.approx(0.05)
