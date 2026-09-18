from __future__ import annotations

import numpy as np
import pytest

from consciousness_measurement.electromagnetic_replication import (
    bonferroni_partial_conjunction_pvalue,
    cochran_q_known_variance,
    common_effect_estimate,
    delete_site_variance_inflation,
    effective_site_count,
    leave_one_site_out_estimates,
    leave_one_site_out_shift_identity,
    normalized_site_weights,
)


def test_common_effect_estimate_matches_inverse_variance_formula() -> None:
    estimates = np.asarray([1.0, 2.0, 3.0])
    standard_errors = np.asarray([1.0, 2.0, 1.0])
    weights = 1.0 / np.square(standard_errors)
    expected = float(np.dot(weights, estimates) / np.sum(weights))
    pooled, pooled_se = common_effect_estimate(estimates, standard_errors)
    assert pooled == pytest.approx(expected)
    assert pooled_se**2 == pytest.approx(1.0 / np.sum(weights))


def test_cochran_q_is_zero_for_identical_site_estimates() -> None:
    estimates = np.asarray([0.4, 0.4, 0.4, 0.4])
    standard_errors = np.asarray([0.1, 0.2, 0.15, 0.12])
    assert cochran_q_known_variance(estimates, standard_errors) == pytest.approx(0.0)


def test_delete_one_shift_identity_is_exact() -> None:
    estimates = np.asarray([0.42, 0.55, 0.37, 0.48])
    standard_errors = np.asarray([0.12, 0.18, 0.10, 0.15])
    pooled, _ = common_effect_estimate(estimates, standard_errors)
    delete_estimates = leave_one_site_out_estimates(estimates, standard_errors)
    identity_shifts = leave_one_site_out_shift_identity(estimates, standard_errors)
    assert delete_estimates - pooled == pytest.approx(identity_shifts)


def test_partial_conjunction_union_bound_formula() -> None:
    p_values = np.asarray([0.001, 0.012, 0.04, 0.21, 0.45])
    assert bonferroni_partial_conjunction_pvalue(p_values, 1) == pytest.approx(0.005)
    assert bonferroni_partial_conjunction_pvalue(p_values, 2) == pytest.approx(0.048)
    assert bonferroni_partial_conjunction_pvalue(p_values, 3) == pytest.approx(0.12)
    assert bonferroni_partial_conjunction_pvalue(p_values, 4) == pytest.approx(0.42)
    assert bonferroni_partial_conjunction_pvalue(p_values, 5) == pytest.approx(0.45)


def test_balanced_site_weights_have_full_effective_count() -> None:
    standard_errors = np.asarray([0.1, 0.1, 0.1, 0.1])
    assert normalized_site_weights(standard_errors) == pytest.approx(np.full(4, 0.25))
    assert effective_site_count(standard_errors) == pytest.approx(4.0)
    assert delete_site_variance_inflation(standard_errors) == pytest.approx(
        np.full(4, 4.0 / 3.0)
    )


def test_dominant_site_reduces_effective_site_count() -> None:
    standard_errors = np.asarray([0.05, 0.20, 0.20, 0.20])
    weights = normalized_site_weights(standard_errors)
    inflations = delete_site_variance_inflation(standard_errors)
    assert np.max(weights) == pytest.approx(16.0 / 19.0)
    assert effective_site_count(standard_errors) == pytest.approx(1.3938223938223941)
    assert np.max(inflations) == pytest.approx(19.0 / 3.0)
