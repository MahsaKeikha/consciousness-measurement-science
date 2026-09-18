from __future__ import annotations

import csv
import json
from pathlib import Path

from consciousness_measurement.electromagnetic_inverse_simulations import (
    v21_reference_invariance_grid,
    v22_lead_field_nonidentifiability,
    v23_regularization_path,
    v24_multimodal_nullity,
    v25_forward_model_perturbation_grid,
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
    if value == 0.0:
        return "0"
    if abs(value) >= 1000 or abs(value) < 1e-3:
        return f"{value:.6e}"
    return f"{value:.9f}".rstrip("0").rstrip(".")


def _svg(
    *,
    v21: list[dict[str, float]],
    v22: dict[str, float],
    v23: list[dict[str, float]],
    v24: list[dict[str, float]],
    v25: list[dict[str, float]],
) -> str:
    x23 = [220 + 130 * i for i in range(len(v23))]
    max_residual = max(row["measurement_residual"] for row in v23)
    y23 = [
        780 - 230 * row["measurement_residual"] / max_residual
        for row in v23
    ]
    points23 = " ".join(
        f"{x},{y:.2f}" for x, y in zip(x23, y23, strict=True)
    )
    v24_map = {int(row["modality_code"]): row for row in v24}
    max_ref_error = max(row["max_pairwise_difference_error"] for row in v21)
    max_bound_ratio = max(row["bound_ratio"] for row in v25)

    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="1000" viewBox="0 0 1600 1000">
  <rect width="1600" height="1000" fill="#ffffff"/>
  <text x="85" y="72" font-family="Arial, Helvetica, sans-serif" font-size="34" font-weight="700" fill="#13243a">Research III V21-V25: electromagnetic forward and inverse limits</text>
  <text x="85" y="112" font-family="Arial, Helvetica, sans-serif" font-size="18" fill="#46586c">Reference invariance, source non-identifiability, regularization dependence, multimodal complementarity, and forward-model error.</text>

  <rect x="85" y="155" width="460" height="250" rx="20" fill="#f5f8fb" stroke="#c7d3df" stroke-width="2"/>
  <text x="120" y="202" font-family="Arial, Helvetica, sans-serif" font-size="23" font-weight="700" fill="#173b63">V21 reference invariance</text>
  <text x="120" y="252" font-family="Arial, Helvetica, sans-serif" font-size="17" fill="#34495e">Max pairwise-difference error</text>
  <text x="500" y="252" text-anchor="end" font-family="Arial, Helvetica, sans-serif" font-size="20" font-weight="700" fill="#173b63">{_fmt(max_ref_error)}</text>
  <text x="120" y="304" font-family="Arial, Helvetica, sans-serif" font-size="16" fill="#5b6c7c">Common rereferencing changes absolute voltages</text>
  <text x="120" y="332" font-family="Arial, Helvetica, sans-serif" font-size="16" fill="#5b6c7c">but preserves pairwise sensor differences.</text>
  <text x="120" y="372" font-family="Arial, Helvetica, sans-serif" font-size="15" fill="#6b7785">This does not make source localization reference-free.</text>

  <rect x="570" y="155" width="460" height="250" rx="20" fill="#f7f8f4" stroke="#ced4c2" stroke-width="2"/>
  <text x="605" y="202" font-family="Arial, Helvetica, sans-serif" font-size="23" font-weight="700" fill="#3b5b32">V22 source non-identifiability</text>
  <text x="605" y="250" font-family="Arial, Helvetica, sans-serif" font-size="17" fill="#34495e">Lead-field rank / nullity</text>
  <text x="985" y="250" text-anchor="end" font-family="Arial, Helvetica, sans-serif" font-size="20" font-weight="700" fill="#3b5b32">{int(v22["rank"])} / {int(v22["nullity"])}</text>
  <text x="605" y="296" font-family="Arial, Helvetica, sans-serif" font-size="17" fill="#34495e">Sensor residual</text>
  <text x="985" y="296" text-anchor="end" font-family="Arial, Helvetica, sans-serif" font-size="20" font-weight="700" fill="#3b5b32">{_fmt(v22["sensor_residual"])}</text>
  <text x="605" y="342" font-family="Arial, Helvetica, sans-serif" font-size="17" fill="#34495e">Source separation</text>
  <text x="985" y="342" text-anchor="end" font-family="Arial, Helvetica, sans-serif" font-size="20" font-weight="700" fill="#3b5b32">{_fmt(v22["source_separation"])}</text>
  <text x="605" y="377" font-family="Arial, Helvetica, sans-serif" font-size="15" fill="#6b7785">Distinct sources can produce the same ideal sensor data.</text>

  <rect x="1055" y="155" width="460" height="250" rx="20" fill="#faf6f8" stroke="#d8c8d0" stroke-width="2"/>
  <text x="1090" y="202" font-family="Arial, Helvetica, sans-serif" font-size="23" font-weight="700" fill="#6a3f57">V24 multimodal complementarity</text>
  <text x="1090" y="252" font-family="Arial, Helvetica, sans-serif" font-size="17" fill="#34495e">EEG nullity</text>
  <text x="1470" y="252" text-anchor="end" font-family="Arial, Helvetica, sans-serif" font-size="20" font-weight="700" fill="#6a3f57">{int(v24_map[1]["nullity"])}</text>
  <text x="1090" y="298" font-family="Arial, Helvetica, sans-serif" font-size="17" fill="#34495e">MEG nullity</text>
  <text x="1470" y="298" text-anchor="end" font-family="Arial, Helvetica, sans-serif" font-size="20" font-weight="700" fill="#6a3f57">{int(v24_map[2]["nullity"])}</text>
  <text x="1090" y="344" font-family="Arial, Helvetica, sans-serif" font-size="17" fill="#34495e">Combined nullity</text>
  <text x="1470" y="344" text-anchor="end" font-family="Arial, Helvetica, sans-serif" font-size="20" font-weight="700" fill="#6a3f57">{int(v24_map[3]["nullity"])}</text>
  <text x="1090" y="377" font-family="Arial, Helvetica, sans-serif" font-size="15" fill="#6b7785">Complementary modalities can reduce ambiguity without guaranteeing uniqueness.</text>

  <rect x="85" y="440" width="930" height="450" rx="20" fill="#fbfbfc" stroke="#d4d9df" stroke-width="2"/>
  <text x="120" y="487" font-family="Arial, Helvetica, sans-serif" font-size="23" font-weight="700" fill="#294f64">V23 regularization sensitivity</text>
  <text x="120" y="523" font-family="Arial, Helvetica, sans-serif" font-size="16" fill="#5b6c7c">Measurement residual rises as the L2 prior is strengthened.</text>
  <line x1="220" y1="780" x2="740" y2="780" stroke="#8795a5" stroke-width="2"/>
  <line x1="220" y1="550" x2="220" y2="780" stroke="#8795a5" stroke-width="2"/>
  <polyline points="{points23}" fill="none" stroke="#294f64" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>
  <text x="480" y="825" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="16" fill="#46586c">increasing regularization</text>
  <text x="150" y="665" transform="rotate(-90 150 665)" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="16" fill="#46586c">sensor residual</text>
  <text x="780" y="610" font-family="Arial, Helvetica, sans-serif" font-size="16" fill="#34495e">Weak lambda preserves fit</text>
  <text x="780" y="648" font-family="Arial, Helvetica, sans-serif" font-size="16" fill="#34495e">Strong lambda shrinks source norm</text>
  <text x="780" y="700" font-family="Arial, Helvetica, sans-serif" font-size="15" fill="#6b7785">The reconstructed source depends on the inverse prior.</text>

  <rect x="1040" y="440" width="475" height="450" rx="20" fill="#f8faf8" stroke="#ced8ce" stroke-width="2"/>
  <text x="1075" y="487" font-family="Arial, Helvetica, sans-serif" font-size="23" font-weight="700" fill="#43634a">V25 forward-model perturbation</text>
  <text x="1075" y="543" font-family="Arial, Helvetica, sans-serif" font-size="17" fill="#34495e">Max mismatch / bound ratio</text>
  <text x="1470" y="543" text-anchor="end" font-family="Arial, Helvetica, sans-serif" font-size="20" font-weight="700" fill="#43634a">{_fmt(max_bound_ratio)}</text>
  <text x="1075" y="600" font-family="Arial, Helvetica, sans-serif" font-size="16" fill="#5b6c7c">For every tested perturbation:</text>
  <text x="1075" y="645" font-family="Arial, Helvetica, sans-serif" font-size="22" font-weight="700" fill="#43634a">||delta L j|| <= ||delta L|| ||j||</text>
  <text x="1075" y="703" font-family="Arial, Helvetica, sans-serif" font-size="16" fill="#5b6c7c">Geometry or conductivity error therefore enters</text>
  <text x="1075" y="731" font-family="Arial, Helvetica, sans-serif" font-size="16" fill="#5b6c7c">the sensor prediction through a bounded operator perturbation.</text>
  <text x="1075" y="795" font-family="Arial, Helvetica, sans-serif" font-size="15" fill="#6b7785">A small residual does not prove the forward model is uniquely correct.</text>

  <text x="85" y="950" font-family="Arial, Helvetica, sans-serif" font-size="15" fill="#6a7684">Deterministic synthetic measurement validation. No human empirical data and no direct measurement of consciousness or qualia.</text>
</svg>
"""


def main() -> None:
    RESULTS.mkdir(parents=True, exist_ok=True)
    FIGURES.mkdir(parents=True, exist_ok=True)

    v21 = v21_reference_invariance_grid()
    v22 = v22_lead_field_nonidentifiability()
    v23 = v23_regularization_path()
    v24 = v24_multimodal_nullity()
    v25 = v25_forward_model_perturbation_grid()

    _write_csv(RESULTS / "v21_reference_invariance.csv", v21)
    _write_csv(RESULTS / "v23_regularization_path.csv", v23)
    _write_csv(RESULTS / "v24_multimodal_nullity.csv", v24)
    _write_csv(RESULTS / "v25_forward_model_perturbation.csv", v25)
    (RESULTS / "electromagnetic_inverse_validation_summary.json").write_text(
        json.dumps(
            {
                "status": "analytic_and_synthetic_only",
                "claim_boundary": (
                    "forward and inverse electromagnetic validation does not "
                    "identify consciousness or uniquely identify neural sources"
                ),
                "v22_lead_field_nonidentifiability": v22,
            },
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )
    (FIGURES / "v21_v25_electromagnetic_inverse_validation.svg").write_text(
        _svg(v21=v21, v22=v22, v23=v23, v24=v24, v25=v25),
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
