from __future__ import annotations

import pytest

from consciousness_measurement.electromagnetic_selection_simulations import (
    v41_arbitrary_dependence_bonferroni,
    v42_holm_step_down_gain,
    v43_exact_sign_flip_max_statistic,
    v44_post_selection_coverage_collapse,
    v45_independent_holdout_confirmation,
)


def test_v41_bonferroni_is_valid_under_union_bound_and_conservative_when_independent() -> None:
    rows = v41_arbitrary_dependence_bonferroni()
    thresholds = [row["two_sided_z_threshold"] for row in rows]
    assert thresholds == pytest.approx(
        [
            1.9599639845400536,
            2.8070337683438114,
            3.4807564043462422,
            4.055626981121907,
        ]
    )
    for row in rows:
        assert row["union_bound_fwer"] == pytest.approx(0.05, abs=2e-13)
        assert row["independent_exact_fwer"] <= row["union_bound_fwer"] + 1e-13


def test_v42_holm_step_down_gains_rejections_without_changing_target_alpha() -> None:
    rows = v42_holm_step_down_gain()
    adjusted = [row["holm_adjusted_pvalue"] for row in rows]
    assert adjusted == pytest.approx([0.004, 0.048, 0.048, 0.5])
    assert sum(row["holm_reject"] for row in rows) == pytest.approx(3.0)
    assert sum(row["bonferroni_reject"] for row in rows) == pytest.approx(1.0)


def test_v43_exact_sign_flip_max_statistic_has_finite_orbit_pvalue() -> None:
    result = v43_exact_sign_flip_max_statistic()
    assert result["orbit_size"] == pytest.approx(64.0)
    assert result["exceedances"] == pytest.approx(2.0)
    assert result["observed_max_abs_mean"] == pytest.approx(1.0083333333333333)
    assert result["exact_randomization_pvalue"] == pytest.approx(0.03125)


def test_v44_post_selection_coverage_collapses_with_search_size() -> None:
    rows = v44_post_selection_coverage_collapse()
    coverages = [row["selected_naive_coverage"] for row in rows]
    assert coverages == sorted(coverages, reverse=True)
    assert coverages[:3] == pytest.approx(
        [0.95, 0.5987369392383787, 0.0059205292203339975]
    )
    assert coverages[-1] == pytest.approx(5.2918227477448005e-23)


def test_v45_independent_holdout_confirmation_recovers_nominal_false_positive_rate() -> None:
    result = v45_independent_holdout_confirmation()
    assert result["exact_holdout_type1"] == pytest.approx(0.05)
    assert result["exact_reuse_false_positive"] == pytest.approx(
        0.994079470779666
    )
    assert result["empirical_reuse_false_positive"] == pytest.approx(
        0.99382,
        abs=0.002,
    )
    assert result["empirical_holdout_false_positive"] == pytest.approx(
        0.04986,
        abs=0.003,
    )
