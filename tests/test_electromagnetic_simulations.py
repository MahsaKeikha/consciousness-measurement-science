from __future__ import annotations

import pytest

from consciousness_measurement.electromagnetic_simulations import (
    v16_field_identity,
    v17_scale_invariance,
    v18_power_nonidentifiability,
    v19_common_mode_confound,
    v20_frequency_specific_structure,
)


def test_v16_field_identity_is_finite_and_directional() -> None:
    row = v16_field_identity()
    assert row["energy_density_j_m3"] > 0.0
    assert row["poynting_x_w_m2"] == pytest.approx(0.0)
    assert row["poynting_y_w_m2"] == pytest.approx(0.0)
    assert row["poynting_z_w_m2"] > 0.0


def test_v17_normalized_features_do_not_change_with_global_gain() -> None:
    rows = v17_scale_invariance()
    baseline = rows[1]
    for row in rows:
        for key in (
            "spectral_entropy",
            "phase_concentration",
            "effective_rank",
            "singular_entropy",
            "common_mode_fraction",
        ):
            assert row[key] == pytest.approx(baseline[key], abs=1e-12)


def test_v18_power_alone_does_not_identify_phase_structure() -> None:
    result = v18_power_nonidentifiability()
    assert result["max_relative_channel_power_difference"] < 1e-12
    assert result["coherent_phase_concentration"] > 0.999999
    assert result["balanced_phase_concentration"] < 1e-12
    assert result["balanced_effective_rank"] > result["coherent_effective_rank"]


def test_v19_common_mode_can_create_spurious_phase_organization() -> None:
    rows = v19_common_mode_confound()
    assert rows[-1]["phase_concentration_raw"] > 0.85
    for row in rows:
        assert row["phase_concentration_after_common_mode_removal"] < 1e-12


def test_v20_phase_structure_is_frequency_specific() -> None:
    rows = v20_frequency_specific_structure()
    by_frequency = {row["frequency_hz"]: row["phase_concentration"] for row in rows}
    assert by_frequency[10.0] > 0.999999
    assert by_frequency[17.0] < 1e-12
