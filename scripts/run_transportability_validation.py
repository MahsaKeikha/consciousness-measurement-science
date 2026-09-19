from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Any

from consciousness_measurement.transportability_simulations import (
    v51_invertible_sensor_coordinate_invariance,
    v52_projection_information_monotonicity,
    v53_cross_hardware_topography_mismatch,
    v54_importance_weighted_transport,
    v55_total_variation_transport_budget,
)

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
FIGURES = ROOT / "docs" / "figures"


def _write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def _write_single_row_csv(path: Path, row: dict[str, Any]) -> None:
    _write_csv(path, [row])


def _fmt(value: float) -> str:
    if value == 0.0:
        return "0"
    if abs(value) < 1e-4 or abs(value) >= 1e4:
        return f"{value:.3e}"
    return f"{value:.6f}".rstrip("0").rstrip(".")


def _render_svg(
    v51: dict[str, float],
    v52: list[dict[str, float | str]],
    v53: list[dict[str, float]],
    v54: list[dict[str, float]],
    v55: list[dict[str, float]],
) -> str:
    v52_rows = {str(row["projection"]): row for row in v52}
    v53_last = v53[-1]
    v54_last = v54[-1]
    v55_last = v55[-1]

    projection_bars: list[str] = []
    for index, name in enumerate(("all_sensors", "drop_sensor_3", "single_mixed_channel")):
        fraction = float(v52_rows[name]["information_fraction"])
        x = 185 + index * 160
        height = 150 * fraction
        y = 720 - height
        projection_bars.append(
            f'<rect x="{x}" y="{y:.2f}" width="92" height="{height:.2f}" rx="8" '
            'fill="#dce7ef" stroke="#315c7d" stroke-width="2"/>'
        )
        projection_bars.append(
            f'<text x="{x + 46}" y="{y - 12:.2f}" text-anchor="middle" '
            'font-family="Arial, Helvetica, sans-serif" font-size="16" fill="#173b63">'
            f'{fraction:.3f}</text>'
        )

    mismatch_points: list[str] = []
    bound_points: list[str] = []
    for index, row in enumerate(v53):
        x = 905 + index * 105
        bias = float(row["absolute_relative_bias"])
        bound = float(row["cauchy_schwarz_bias_bound"])
        mismatch_points.append(f"{x:.1f},{765 - 280 * bias:.2f}")
        bound_points.append(f"{x:.1f},{765 - 280 * bound:.2f}")

    ess_points: list[str] = []
    tv_points: list[str] = []
    for index, (row54, row55) in enumerate(zip(v54, v55, strict=True)):
        x = 905 + index * 105
        ess = float(row54["effective_sample_fraction"])
        tv = float(row55["total_variation"])
        ess_points.append(f"{x:.1f},{765 - 160 * ess:.2f}")
        tv_points.append(f"{x:.1f},{765 - 300 * tv:.2f}")

    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="1000" viewBox="0 0 1600 1000">
  <rect width="1600" height="1000" fill="#ffffff"/>
  <text x="85" y="70" font-family="Arial, Helvetica, sans-serif" font-size="34" font-weight="700" fill="#13243a">Research III V51-V55: transportability across sensor systems and states</text>
  <text x="85" y="110" font-family="Arial, Helvetica, sans-serif" font-size="18" fill="#46586c">Coordinate invariance, lossy projection, topography mismatch, covariate-shift reweighting, and sharp transport budgets.</text>
  <text x="85" y="137" font-family="Arial, Helvetica, sans-serif" font-size="11" font-weight="700" fill="#3156a3">SCIENTIFIC QUESTION</text>
  <text x="250" y="130" font-family="Arial, Helvetica, sans-serif" font-size="12" font-weight="700" fill="#26374d">Does the measurement relation survive coordinate changes,</text>
  <text x="250" y="146" font-family="Arial, Helvetica, sans-serif" font-size="12" font-weight="700" fill="#26374d">lossy sensors, hardware mismatch, and distribution shift?</text>

  <rect x="85" y="150" width="690" height="270" rx="18" fill="#f5f8fb" stroke="#c7d3df" stroke-width="2"/>
  <text x="120" y="198" font-family="Arial, Helvetica, sans-serif" font-size="23" font-weight="700" fill="#173b63">V51 invertible sensor-coordinate invariance</text>
  <text x="120" y="250" font-family="Arial, Helvetica, sans-serif" font-size="17" fill="#34495e">GLS amplitude estimate before transform</text>
  <text x="735" y="250" text-anchor="end" font-family="Arial, Helvetica, sans-serif" font-size="21" font-weight="700" fill="#173b63">{_fmt(float(v51["original_gls_estimate"]))}</text>
  <text x="120" y="300" font-family="Arial, Helvetica, sans-serif" font-size="17" fill="#34495e">GLS amplitude estimate after transform</text>
  <text x="735" y="300" text-anchor="end" font-family="Arial, Helvetica, sans-serif" font-size="21" font-weight="700" fill="#173b63">{_fmt(float(v51["transformed_gls_estimate"]))}</text>
  <text x="120" y="350" font-family="Arial, Helvetica, sans-serif" font-size="17" fill="#34495e">Fisher information difference</text>
  <text x="735" y="350" text-anchor="end" font-family="Arial, Helvetica, sans-serif" font-size="21" font-weight="700" fill="#173b63">{_fmt(float(v51["absolute_information_difference"]))}</text>
  <text x="120" y="382" font-family="Arial, Helvetica, sans-serif" font-size="14" fill="#6b7785">An invertible sensor-coordinate change preserves the Gaussian likelihood</text>
  <text x="120" y="404" font-family="Arial, Helvetica, sans-serif" font-size="14" fill="#6b7785">when the data and complete model are transformed consistently.</text>

  <rect x="805" y="150" width="710" height="270" rx="18" fill="#f7f8f4" stroke="#ced4c2" stroke-width="2"/>
  <text x="840" y="198" font-family="Arial, Helvetica, sans-serif" font-size="23" font-weight="700" fill="#3b5b32">V54-V55 transport under distribution shift</text>
  <text x="840" y="250" font-family="Arial, Helvetica, sans-serif" font-size="17" fill="#34495e">Maximum importance weight at alpha = 0.40</text>
  <text x="1475" y="250" text-anchor="end" font-family="Arial, Helvetica, sans-serif" font-size="21" font-weight="700" fill="#3b5b32">{_fmt(float(v54_last["maximum_importance_weight"]))}</text>
  <text x="840" y="300" font-family="Arial, Helvetica, sans-serif" font-size="17" fill="#34495e">Effective sample fraction</text>
  <text x="1475" y="300" text-anchor="end" font-family="Arial, Helvetica, sans-serif" font-size="21" font-weight="700" fill="#3b5b32">{_fmt(float(v54_last["effective_sample_fraction"]))}</text>
  <text x="840" y="350" font-family="Arial, Helvetica, sans-serif" font-size="17" fill="#34495e">Total-variation transport budget</text>
  <text x="1475" y="350" text-anchor="end" font-family="Arial, Helvetica, sans-serif" font-size="21" font-weight="700" fill="#3b5b32">{_fmt(float(v55_last["sharp_tv_bound"]))}</text>
  <text x="840" y="382" font-family="Arial, Helvetica, sans-serif" font-size="14" fill="#6b7785">Exact reweighting can recover a target expectation under covariate shift.</text>
  <text x="840" y="404" font-family="Arial, Helvetica, sans-serif" font-size="14" fill="#6b7785">Concentrated weights reduce effective information and expose unstable transport.</text>
  <rect x="735" y="166" width="26" height="22" rx="11" fill="#eef4f8" stroke="#c8d7e2"/>
  <text x="748" y="181" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="11" font-weight="700" fill="#173b63">A</text>
  <rect x="1475" y="166" width="26" height="22" rx="11" fill="#f1f5ee" stroke="#cfdbc7"/>
  <text x="1488" y="181" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="11" font-weight="700" fill="#3b5b32">B</text>

  <rect x="85" y="455" width="690" height="440" rx="18" fill="#fbfbfc" stroke="#d4d9df" stroke-width="2"/>
  <text x="120" y="503" font-family="Arial, Helvetica, sans-serif" font-size="23" font-weight="700" fill="#294f64">V52 information retained after linear sensor projection</text>
  <text x="120" y="538" font-family="Arial, Helvetica, sans-serif" font-size="16" fill="#5b6c7c">Information fraction relative to the full three-sensor Gaussian model.</text>
  <line x1="155" y1="720" x2="650" y2="720" stroke="#8795a5" stroke-width="2"/>
  {"".join(projection_bars)}
  <text x="231" y="755" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="14" fill="#46586c">all</text>
  <text x="391" y="755" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="14" fill="#46586c">drop S3</text>
  <text x="551" y="755" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="14" fill="#46586c">one mixture</text>
  <text x="120" y="835" font-family="Arial, Helvetica, sans-serif" font-size="16" fill="#34495e">Full information: {_fmt(float(v52_rows["all_sensors"]["retained_information"]))}</text>
  <text x="120" y="858" font-family="Arial, Helvetica, sans-serif" font-size="14" fill="#6b7785">A rank-reducing acquisition or preprocessing map cannot increase Fisher information</text>
  <text x="120" y="880" font-family="Arial, Helvetica, sans-serif" font-size="14" fill="#6b7785">for the declared scalar target.</text>

  <rect x="805" y="455" width="710" height="440" rx="18" fill="#faf6f8" stroke="#d8c8d0" stroke-width="2"/>
  <text x="840" y="503" font-family="Arial, Helvetica, sans-serif" font-size="23" font-weight="700" fill="#6a3f57">V53 cross-hardware topography mismatch</text>
  <text x="840" y="538" font-family="Arial, Helvetica, sans-serif" font-size="16" fill="#5b6c7c">Absolute amplitude bias and the covariance-weighted Cauchy-Schwarz bound.</text>
  <rect x="735" y="471" width="26" height="22" rx="11" fill="#eef4f8" stroke="#c8d7e2"/>
  <text x="748" y="486" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="11" font-weight="700" fill="#294f64">C</text>
  <text x="120" y="800" font-family="Arial, Helvetica, sans-serif" font-size="13" font-weight="700" fill="#294f64">Information monotonicity: I(PY) &lt;= I(Y)</text>
  <rect x="1475" y="471" width="26" height="22" rx="11" fill="#f8f0f4" stroke="#e1cfd8"/>
  <text x="1488" y="486" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="11" font-weight="700" fill="#6a3f57">D</text>
  <text x="840" y="568" font-family="Arial, Helvetica, sans-serif" font-size="12" font-weight="700" fill="#6a3f57">Pass: |relative bias| &lt;= covariance-weighted bound</text>
  <line x1="875" y1="765" x2="1355" y2="765" stroke="#8795a5" stroke-width="2"/>
  <polyline points="{" ".join(mismatch_points)}" fill="none" stroke="#6a3f57" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>
  <polyline points="{" ".join(bound_points)}" fill="none" stroke="#aa879a" stroke-width="4" stroke-dasharray="9 7" stroke-linecap="round" stroke-linejoin="round"/>
  <text x="1375" y="615" font-family="Arial, Helvetica, sans-serif" font-size="14" fill="#6a3f57">bound</text>
  <text x="1375" y="730" font-family="Arial, Helvetica, sans-serif" font-size="14" fill="#6a3f57">bias</text>
  <text x="840" y="812" font-family="Arial, Helvetica, sans-serif" font-size="15" fill="#34495e">At mismatch 0.40: bias = {_fmt(float(v53_last["absolute_relative_bias"]))}</text>
  <text x="840" y="836" font-family="Arial, Helvetica, sans-serif" font-size="15" fill="#34495e">Cauchy-Schwarz bound = {_fmt(float(v53_last["cauchy_schwarz_bias_bound"]))}</text>
  <text x="840" y="865" font-family="Arial, Helvetica, sans-serif" font-size="14" fill="#6b7785">Hardware or forward-model changes can bias the amplitude estimate.</text>

  <text x="85" y="955" font-family="Arial, Helvetica, sans-serif" font-size="15" fill="#6a7684">Analytic and deterministic transportability validation only. No human dataset, no empirical cross-device replication, and no direct measurement of consciousness or qualia.</text>
</svg>
"""


def main() -> None:
    v51 = v51_invertible_sensor_coordinate_invariance()
    v52 = v52_projection_information_monotonicity()
    v53 = v53_cross_hardware_topography_mismatch()
    v54 = v54_importance_weighted_transport()
    v55 = v55_total_variation_transport_budget()

    _write_single_row_csv(RESULTS / "v51_coordinate_invariance.csv", v51)
    _write_csv(RESULTS / "v52_projection_information.csv", v52)
    _write_csv(RESULTS / "v53_topography_mismatch.csv", v53)
    _write_csv(RESULTS / "v54_importance_transport.csv", v54)
    _write_csv(RESULTS / "v55_total_variation_transport.csv", v55)

    summary = {
        "status": "analytic_and_deterministic_only",
        "claim_boundary": (
            "transportability calculations do not constitute empirical cross-device, "
            "cross-state, or cross-population validation and do not identify consciousness"
        ),
        "v51_coordinate_invariance": v51,
        "v52_projection_information": v52,
        "v53_topography_mismatch": v53,
        "v54_importance_transport": v54,
        "v55_total_variation_transport": v55,
    }
    RESULTS.mkdir(parents=True, exist_ok=True)
    (RESULTS / "transportability_validation_summary.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    FIGURES.mkdir(parents=True, exist_ok=True)
    (FIGURES / "v51_v55_transportability_validation.svg").write_text(
        _render_svg(v51, v52, v53, v54, v55),
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
