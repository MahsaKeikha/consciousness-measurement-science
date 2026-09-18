from __future__ import annotations

import pytest

from consciousness_measurement.electromagnetic_sparse_simulations import (
    v36_coherence_and_welch_bound,
    v37_sparse_uniqueness_guarantee,
    v38_restricted_gram_conditioning,
    v39_nuisance_adjusted_fisher_information,
    v40_sequential_sensor_information_gain,
)


def test_v36_regular_simplex_attains_welch_bound() -> None:
    rows = {row["dictionary"]: row for row in v36_coherence_and_welch_bound()}
    simplex = rows["regular_simplex"]
    assert simplex["rank"] == pytest.approx(4.0)
    assert simplex["mutual_coherence"] == pytest.approx(0.25, abs=1e-14)
    assert simplex["welch_lower_bound"] == pytest.approx(0.25)
    assert rows["coherent"]["mutual_coherence"] > 0.99


def test_v37_coherence_guarantee_separates_simplex_and_coherent_dictionaries() -> None:
    rows = {row["dictionary"]: row for row in v37_sparse_uniqueness_guarantee()}
    assert rows["regular_simplex"]["strict_sparsity_threshold"] == pytest.approx(2.5)
    assert rows["regular_simplex"]["largest_guaranteed_integer_sparsity"] == pytest.approx(2.0)
    assert rows["coherent"]["strict_sparsity_threshold"] == pytest.approx(1.0025442867315455)
    assert rows["coherent"]["largest_guaranteed_integer_sparsity"] == pytest.approx(1.0)


def test_v38_restricted_gram_spectrum_obeys_coherence_bounds() -> None:
    rows = {int(row["sparsity"]): row for row in v38_restricted_gram_conditioning()}
    assert rows[2]["gershgorin_lower_bound"] == pytest.approx(0.75)
    assert rows[2]["observed_minimum_eigenvalue"] == pytest.approx(0.75)
    assert rows[2]["observed_maximum_eigenvalue"] == pytest.approx(1.25)
    assert rows[2]["gershgorin_upper_bound"] == pytest.approx(1.25)
    assert rows[3]["gershgorin_lower_bound"] == pytest.approx(0.5)
    assert rows[3]["observed_minimum_eigenvalue"] == pytest.approx(0.5)
    assert rows[3]["observed_maximum_eigenvalue"] == pytest.approx(1.25)
    assert rows[3]["gershgorin_upper_bound"] == pytest.approx(1.5)


def test_v39_nuisance_adjusted_information_has_expected_limits() -> None:
    rows = {row["nuisance_case"]: row for row in v39_nuisance_adjusted_fisher_information()}
    assert rows["orthogonal"]["nuisance_adjusted_information"] == pytest.approx(1.0)
    assert rows["partial_30deg"]["nuisance_adjusted_information"] == pytest.approx(0.25)
    assert rows["contains_target"]["nuisance_adjusted_information"] == pytest.approx(0.0)


def test_v40_weak_direction_has_largest_incremental_information_gain() -> None:
    rows = {row["candidate"]: row for row in v40_sequential_sensor_information_gain()}
    assert rows["strong_direction"]["determinant_lemma_gain"] == pytest.approx(0.09531017980432487)
    assert rows["mixed_direction"]["determinant_lemma_gain"] == pytest.approx(0.4382549309311552)
    assert rows["weak_direction"]["determinant_lemma_gain"] == pytest.approx(0.6931471805599453)
    for row in rows.values():
        assert row["determinant_lemma_gain"] == pytest.approx(row["direct_logdet_gain"])
