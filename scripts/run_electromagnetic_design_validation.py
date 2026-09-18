from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Any

from consciousness_measurement.electromagnetic_design_simulations import (
    v31_point_spread_cross_talk,
    v32_noise_aware_source_distinguishability,
    v33_sensor_design_information,
    v34_nuisance_subspace_information_loss,
    v35_robust_information_under_model_uncertainty,
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


def _fmt(value: float) -> str:
    if value == 0.0:
        return "0"
    if abs(value) < 1e-4 or abs(value) >= 1e4:
        return f"{value:.6e}"
    return f"{value:.9f}".rstrip("0").rstrip(".")


def _render_svg(
    v31: dict[str, float | list[float]],
    v32: list[dict[str, float | str]],
    v33: list[dict[str, float | str]],
    v34: list[dict[str, float]],
    v35: list[dict[str, float]],
) -> str:
    close_distance = float(v32[0]["mahalanobis_distance_squared"])
    distinct_distance = float(v32[1]["mahalanobis_distance_squared"])
    redundant = v33[0]
    complementary = v33[1]

    nuisance_points = []
    for row in v34:
        x = 865 + float(row["angle_degrees"]) / 90.0 * 300
        y = 805 - float(row["retained_information_fraction"]) * 235
        nuisance_points.append(f"{x:.2f},{y:.2f}")

    robust_points = []
    max_radius = max(float(row["uncertainty_radius"]) for row in v35)
    nominal = float(v35[0]["nominal_information"])
    for row in v35:
        x = 1250 + float(row["uncertainty_radius"]) / max_radius * 255
        y = 805 - float(row["robust_information_lower_bound"]) / nominal * 235
        robust_points.append(f"{x:.2f},{y:.2f}")

    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="1000" viewBox="0 0 1600 1000">
  <rect width="1600" height="1000" fill="#ffffff"/>
  <text x="85" y="72" font-family="Arial, Helvetica, sans-serif" font-size="34" font-weight="700" fill="#13243a">Research III V31-V35: electromagnetic design and spatial specificity</text>
  <text x="85" y="112" font-family="Arial, Helvetica, sans-serif" font-size="18" fill="#46586c">Point-spread and cross-talk, source distinguishability, information-aware sensor design, nuisance projection, and robust model uncertainty.</text>

  <rect x="85" y="155" width="455" height="245" rx="20" fill="#f5f8fb" stroke="#c7d3df" stroke-width="2"/>
  <text x="120" y="202" font-family="Arial, Helvetica, sans-serif" font-size="23" font-weight="700" fill="#173b63">V31 PSF and CTF</text>
  <text x="120" y="250" font-family="Arial, Helvetica, sans-serif" font-size="17" fill="#34495e">Point-spread leakage norm</text>
  <text x="500" y="250" text-anchor="end" font-family="Arial, Helvetica, sans-serif" font-size="20" font-weight="700" fill="#173b63">{_fmt(float(v31["point_spread_leakage_norm"]))}</text>
  <text x="120" y="296" font-family="Arial, Helvetica, sans-serif" font-size="17" fill="#34495e">Cross-talk leakage norm</text>
  <text x="500" y="296" text-anchor="end" font-family="Arial, Helvetica, sans-serif" font-size="20" font-weight="700" fill="#173b63">{_fmt(float(v31["cross_talk_leakage_norm"]))}</text>
  <text x="120" y="345" font-family="Arial, Helvetica, sans-serif" font-size="15" fill="#6b7785">Columns describe spread from a point source.</text>
  <text x="120" y="375" font-family="Arial, Helvetica, sans-serif" font-size="15" fill="#6b7785">Rows describe sources leaking into an estimate.</text>

  <rect x="570" y="155" width="455" height="245" rx="20" fill="#f7f8f4" stroke="#ced4c2" stroke-width="2"/>
  <text x="605" y="202" font-family="Arial, Helvetica, sans-serif" font-size="23" font-weight="700" fill="#3b5b32">V32 source distinguishability</text>
  <text x="605" y="250" font-family="Arial, Helvetica, sans-serif" font-size="17" fill="#34495e">Close topography distance squared</text>
  <text x="985" y="250" text-anchor="end" font-family="Arial, Helvetica, sans-serif" font-size="20" font-weight="700" fill="#3b5b32">{_fmt(close_distance)}</text>
  <text x="605" y="296" font-family="Arial, Helvetica, sans-serif" font-size="17" fill="#34495e">Distinct topography distance squared</text>
  <text x="985" y="296" text-anchor="end" font-family="Arial, Helvetica, sans-serif" font-size="20" font-weight="700" fill="#3b5b32">{_fmt(distinct_distance)}</text>
  <text x="605" y="350" font-family="Arial, Helvetica, sans-serif" font-size="15" fill="#6b7785">Distinguishability depends on sensor-noise geometry,</text>
  <text x="605" y="376" font-family="Arial, Helvetica, sans-serif" font-size="15" fill="#6b7785">not raw Euclidean separation alone.</text>

  <rect x="1055" y="155" width="460" height="245" rx="20" fill="#faf6f8" stroke="#d8c8d0" stroke-width="2"/>
  <text x="1090" y="202" font-family="Arial, Helvetica, sans-serif" font-size="23" font-weight="700" fill="#6a3f57">V33 sensor design information</text>
  <text x="1090" y="250" font-family="Arial, Helvetica, sans-serif" font-size="17" fill="#34495e">Redundant minimum eigenvalue</text>
  <text x="1470" y="250" text-anchor="end" font-family="Arial, Helvetica, sans-serif" font-size="20" font-weight="700" fill="#6a3f57">{_fmt(float(redundant["minimum_eigenvalue"]))}</text>
  <text x="1090" y="296" font-family="Arial, Helvetica, sans-serif" font-size="17" fill="#34495e">Complementary minimum eigenvalue</text>
  <text x="1470" y="296" text-anchor="end" font-family="Arial, Helvetica, sans-serif" font-size="20" font-weight="700" fill="#6a3f57">{_fmt(float(complementary["minimum_eigenvalue"]))}</text>
  <text x="1090" y="350" font-family="Arial, Helvetica, sans-serif" font-size="15" fill="#6b7785">Three sensors can carry very different information</text>
  <text x="1090" y="376" font-family="Arial, Helvetica, sans-serif" font-size="15" fill="#6b7785">depending on directional complementarity.</text>

  <rect x="85" y="440" width="680" height="455" rx="20" fill="#fbfbfc" stroke="#d4d9df" stroke-width="2"/>
  <text x="120" y="487" font-family="Arial, Helvetica, sans-serif" font-size="23" font-weight="700" fill="#294f64">V34 nuisance-subspace information loss</text>
  <text x="120" y="522" font-family="Arial, Helvetica, sans-serif" font-size="16" fill="#5b6c7c">For one target and one nuisance direction, retained information equals sin squared of their angle.</text>
  <line x1="865" y1="805" x2="1165" y2="805" stroke="#8795a5" stroke-width="2"/>
  <line x1="865" y1="570" x2="865" y2="805" stroke="#8795a5" stroke-width="2"/>
  <polyline points="{" ".join(nuisance_points)}" fill="none" stroke="#294f64" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>
  <text x="1015" y="850" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="16" fill="#46586c">target-nuisance angle: 0 to 90 degrees</text>
  <text x="805" y="690" transform="rotate(-90 805 690)" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="16" fill="#46586c">retained information fraction</text>
  <text x="120" y="610" font-family="Arial, Helvetica, sans-serif" font-size="17" fill="#34495e">Aligned nuisance</text>
  <text x="390" y="610" font-family="Arial, Helvetica, sans-serif" font-size="20" font-weight="700" fill="#294f64">0 retained</text>
  <text x="120" y="655" font-family="Arial, Helvetica, sans-serif" font-size="17" fill="#34495e">Orthogonal nuisance</text>
  <text x="390" y="655" font-family="Arial, Helvetica, sans-serif" font-size="20" font-weight="700" fill="#294f64">1 retained</text>

  <rect x="795" y="440" width="720" height="455" rx="20" fill="#f8faf8" stroke="#ced8ce" stroke-width="2"/>
  <text x="830" y="487" font-family="Arial, Helvetica, sans-serif" font-size="23" font-weight="700" fill="#43634a">V35 robust information under model uncertainty</text>
  <text x="830" y="522" font-family="Arial, Helvetica, sans-serif" font-size="16" fill="#5b6c7c">Worst-case Fisher information falls as an allowed whitened topography error grows.</text>
  <line x1="1250" y1="805" x2="1505" y2="805" stroke="#8795a5" stroke-width="2"/>
  <line x1="1250" y1="570" x2="1250" y2="805" stroke="#8795a5" stroke-width="2"/>
  <polyline points="{" ".join(robust_points)}" fill="none" stroke="#43634a" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>
  <text x="1377" y="850" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="16" fill="#46586c">whitened uncertainty radius</text>
  <text x="1190" y="690" transform="rotate(-90 1190 690)" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="16" fill="#46586c">robust information lower bound</text>
  <text x="830" y="610" font-family="Arial, Helvetica, sans-serif" font-size="17" fill="#34495e">Nominal information</text>
  <text x="1105" y="610" font-family="Arial, Helvetica, sans-serif" font-size="20" font-weight="700" fill="#43634a">{_fmt(nominal)}</text>
  <text x="830" y="655" font-family="Arial, Helvetica, sans-serif" font-size="17" fill="#34495e">Radius 1.2 lower bound</text>
  <text x="1105" y="655" font-family="Arial, Helvetica, sans-serif" font-size="20" font-weight="700" fill="#43634a">{_fmt(float(v35[-1]["robust_information_lower_bound"]))}</text>

  <text x="85" y="955" font-family="Arial, Helvetica, sans-serif" font-size="15" fill="#6a7684">Deterministic analytic and synthetic measurement-design validation. No human empirical data and no direct measurement of consciousness or qualia.</text>
</svg>
"""


def main() -> None:
    v31 = v31_point_spread_cross_talk()
    v32 = v32_noise_aware_source_distinguishability()
    v33 = v33_sensor_design_information()
    v34 = v34_nuisance_subspace_information_loss()
    v35 = v35_robust_information_under_model_uncertainty()

    psf = list(v31["point_spread"])
    ctf = list(v31["cross_talk"])
    v31_rows = [
        {
            "component_index": index,
            "point_spread_value": psf[index],
            "cross_talk_value": ctf[index],
        }
        for index in range(len(psf))
    ]
    _write_csv(RESULTS / "v31_point_spread_cross_talk.csv", v31_rows)
    _write_csv(RESULTS / "v32_source_distinguishability.csv", v32)
    _write_csv(RESULTS / "v33_sensor_design_information.csv", v33)
    _write_csv(RESULTS / "v34_nuisance_information_loss.csv", v34)
    _write_csv(RESULTS / "v35_robust_model_information.csv", v35)

    summary = {
        "status": "analytic_and_synthetic_only",
        "claim_boundary": (
            "sensor design, resolution, nuisance rejection, and robust information "
            "do not identify consciousness or qualia"
        ),
        "v31_point_spread_cross_talk": v31,
        "v32_source_distinguishability": v32,
        "v33_sensor_design_information": v33,
        "v34_nuisance_information_loss": v34,
        "v35_robust_model_information": v35,
    }
    RESULTS.mkdir(parents=True, exist_ok=True)
    (RESULTS / "electromagnetic_design_validation_summary.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    FIGURES.mkdir(parents=True, exist_ok=True)
    (FIGURES / "v31_v35_electromagnetic_design_validation.svg").write_text(
        _render_svg(v31, v32, v33, v34, v35),
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
