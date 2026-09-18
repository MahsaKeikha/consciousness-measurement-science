from __future__ import annotations

import csv
import json
from pathlib import Path

from consciousness_measurement.electromagnetic_simulations import (
    v16_field_identity,
    v17_scale_invariance,
    v18_power_nonidentifiability,
    v19_common_mode_confound,
    v20_frequency_specific_structure,
)

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
FIGURES = ROOT / "docs" / "figures"


def _write_csv(path: Path, rows: list[dict[str, float]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def _fmt(value: float) -> str:
    if abs(value) < 1e-12:
        return "0"
    if abs(value) >= 1000 or abs(value) < 1e-3:
        return f"{value:.6e}"
    return f"{value:.9f}".rstrip("0").rstrip(".")


def _validation_svg(
    *,
    v18: dict[str, float],
    v19: list[dict[str, float]],
    v20: list[dict[str, float]],
) -> str:
    raw_x = [260 + i * 220 for i in range(len(v19))]
    raw_y = [780 - 360 * row["phase_concentration_raw"] for row in v19]
    clean_y = [
        780 - 360 * row["phase_concentration_after_common_mode_removal"] for row in v19
    ]
    raw_points = " ".join(f"{x},{y:.2f}" for x, y in zip(raw_x, raw_y, strict=True))
    clean_points = " ".join(f"{x},{y:.2f}" for x, y in zip(raw_x, clean_y, strict=True))
    v20_map = {row["frequency_hz"]: row["phase_concentration"] for row in v20}

    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="1000" viewBox="0 0 1600 1000">
  <rect width="1600" height="1000" fill="#ffffff"/>
  <text x="90" y="82" font-family="Arial, Helvetica, sans-serif" font-size="34" font-weight="700" fill="#13243a">Research III V16-V20: electromagnetic observables</text>
  <text x="90" y="124" font-family="Arial, Helvetica, sans-serif" font-size="19" fill="#44556a">Physical field quantities + organization descriptors + confound stress tests. Not a consciousness detector.</text>
  <rect x="90" y="180" width="690" height="250" rx="20" fill="#f5f8fb" stroke="#c7d3df" stroke-width="2"/>
  <text x="125" y="225" font-family="Arial, Helvetica, sans-serif" font-size="24" font-weight="700" fill="#173b63">V18 matched-power non-identifiability</text>
  <text x="125" y="265" font-family="Arial, Helvetica, sans-serif" font-size="18" fill="#34495e">Max relative channel-power difference</text>
  <text x="710" y="265" text-anchor="end" font-family="Arial, Helvetica, sans-serif" font-size="20" font-weight="700" fill="#173b63">{_fmt(v18["max_relative_channel_power_difference"])}</text>
  <text x="125" y="310" font-family="Arial, Helvetica, sans-serif" font-size="18" fill="#34495e">Coherent phase concentration</text>
  <text x="710" y="310" text-anchor="end" font-family="Arial, Helvetica, sans-serif" font-size="20" font-weight="700" fill="#173b63">{_fmt(v18["coherent_phase_concentration"])}</text>
  <text x="125" y="355" font-family="Arial, Helvetica, sans-serif" font-size="18" fill="#34495e">Phase-balanced concentration</text>
  <text x="710" y="355" text-anchor="end" font-family="Arial, Helvetica, sans-serif" font-size="20" font-weight="700" fill="#173b63">{_fmt(v18["balanced_phase_concentration"])}</text>
  <text x="125" y="398" font-family="Arial, Helvetica, sans-serif" font-size="16" fill="#5b6c7c">Same power does not identify spatial phase organization.</text>
  <rect x="820" y="180" width="690" height="250" rx="20" fill="#f7f8f4" stroke="#ced4c2" stroke-width="2"/>
  <text x="855" y="225" font-family="Arial, Helvetica, sans-serif" font-size="24" font-weight="700" fill="#3b5b32">V20 frequency-specific structure</text>
  <text x="855" y="282" font-family="Arial, Helvetica, sans-serif" font-size="18" fill="#34495e">10 Hz phase concentration</text>
  <text x="1440" y="282" text-anchor="end" font-family="Arial, Helvetica, sans-serif" font-size="20" font-weight="700" fill="#3b5b32">{_fmt(v20_map[10.0])}</text>
  <text x="855" y="330" font-family="Arial, Helvetica, sans-serif" font-size="18" fill="#34495e">17 Hz phase concentration</text>
  <text x="1440" y="330" text-anchor="end" font-family="Arial, Helvetica, sans-serif" font-size="20" font-weight="700" fill="#3b5b32">{_fmt(v20_map[17.0])}</text>
  <text x="855" y="388" font-family="Arial, Helvetica, sans-serif" font-size="16" fill="#5b6c7c">Organization must be declared in frequency and space, not collapsed into one scalar.</text>
  <rect x="90" y="470" width="1420" height="430" rx="20" fill="#fbfbfc" stroke="#d4d9df" stroke-width="2"/>
  <text x="125" y="515" font-family="Arial, Helvetica, sans-serif" font-size="24" font-weight="700" fill="#6a3f57">V19 common-mode confound stress test</text>
  <line x1="260" y1="780" x2="1140" y2="780" stroke="#8593a3" stroke-width="2"/>
  <line x1="260" y1="420" x2="260" y2="780" stroke="#8593a3" stroke-width="2"/>
  <polyline points="{raw_points}" fill="none" stroke="#6a3f57" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>
  <polyline points="{clean_points}" fill="none" stroke="#2d5f73" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
  <text x="1180" y="580" font-family="Arial, Helvetica, sans-serif" font-size="17" fill="#6a3f57">raw sensor phase concentration</text>
  <text x="1180" y="620" font-family="Arial, Helvetica, sans-serif" font-size="17" fill="#2d5f73">after common-mode removal</text>
  <text x="700" y="835" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="17" fill="#44556a">shared contaminant amplitude</text>
  <text x="150" y="620" transform="rotate(-90 150 620)" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="17" fill="#44556a">phase concentration</text>
  <text x="125" y="875" font-family="Arial, Helvetica, sans-serif" font-size="16" fill="#5b6c7c">A shared field or reference artifact can mimic global organization. Sensor-level synchrony therefore requires explicit nuisance modeling and source/field-spread controls.</text>
  <text x="90" y="955" font-family="Arial, Helvetica, sans-serif" font-size="15" fill="#6a7684">Synthetic validation record. No human empirical data and no direct measurement of qualia.</text>
</svg>
"""


def main() -> None:
    RESULTS.mkdir(parents=True, exist_ok=True)
    FIGURES.mkdir(parents=True, exist_ok=True)
    v16 = v16_field_identity()
    v17 = v17_scale_invariance()
    v18 = v18_power_nonidentifiability()
    v19 = v19_common_mode_confound()
    v20 = v20_frequency_specific_structure()
    _write_csv(RESULTS / "v17_em_scale_invariance.csv", v17)
    _write_csv(RESULTS / "v19_common_mode_confound.csv", v19)
    _write_csv(RESULTS / "v20_frequency_specific_structure.csv", v20)
    summary = {
        "status": "analytic_and_synthetic_only",
        "claim_boundary": "electromagnetic observables are candidate evidence channels, not direct measures of consciousness",
        "v16_field_identity": v16,
        "v18_power_nonidentifiability": v18,
    }
    (RESULTS / "electromagnetic_validation_summary.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    (FIGURES / "v16_v20_electromagnetic_validation.svg").write_text(
        _validation_svg(v18=v18, v19=v19, v20=v20),
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
