from __future__ import annotations

import csv
import json
import math
from pathlib import Path
from typing import Any

from consciousness_measurement.electromagnetic_finite_sample_simulations import (
    v36_gls_amplitude_efficiency,
    v37_inverse_covariance_bias,
    v38_gaussian_source_discrimination,
    v39_independent_search_fwer,
    v40_covariance_mismatch_sandwich,
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
    v36: dict[str, float],
    v37: list[dict[str, float]],
    v38: list[dict[str, float]],
    v39: list[dict[str, float]],
    v40: list[dict[str, float | str]],
) -> str:
    discrimination_points = []
    max_d2 = max(row["mahalanobis_squared"] for row in v38)
    for row in v38:
        x = 480 + row["mahalanobis_squared"] / max_d2 * 225
        y = 805 - row["equal_prior_bayes_error"] / 0.5 * 235
        discrimination_points.append(f"{x:.2f},{y:.2f}")

    fwer_points = []
    max_log = 3.0
    for row in v39:
        comparisons = row["comparisons"]
        x = 1220 + (0.0 if comparisons <= 1.0 else math.log10(comparisons) / max_log * 270)
        y = 805 - (row["two_sided_z_threshold"] - 1.9) / (4.1 - 1.9) * 235
        fwer_points.append(f"{x:.2f},{y:.2f}")

    oracle = next(row for row in v40 if row["weight_model"] == "oracle_precision")
    identity = next(row for row in v40 if row["weight_model"] == "identity_weight")
    diagonal = next(row for row in v40 if row["weight_model"] == "diagonal_precision")

    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="1000" viewBox="0 0 1600 1000">
  <rect width="1600" height="1000" fill="#ffffff"/>
  <text x="85" y="72" font-family="Arial, Helvetica, sans-serif" font-size="34" font-weight="700" fill="#13243a">Research III V36-V40: finite-sample electromagnetic inference</text>
  <text x="85" y="112" font-family="Arial, Helvetica, sans-serif" font-size="18" fill="#46586c">Efficient amplitude inference, inverse-covariance bias, Gaussian discrimination, multiplicity control, and covariance-mismatch calibration.</text>

  <rect x="85" y="155" width="455" height="245" rx="20" fill="#f5f8fb" stroke="#c7d3df" stroke-width="2"/>
  <text x="120" y="202" font-family="Arial, Helvetica, sans-serif" font-size="23" font-weight="700" fill="#173b63">V36 GLS efficiency and coverage</text>
  <text x="120" y="250" font-family="Arial, Helvetica, sans-serif" font-size="17" fill="#34495e">Exact variance / CRLB</text>
  <text x="500" y="250" text-anchor="end" font-family="Arial, Helvetica, sans-serif" font-size="20" font-weight="700" fill="#173b63">{_fmt(v36["exact_variance"])}</text>
  <text x="120" y="296" font-family="Arial, Helvetica, sans-serif" font-size="17" fill="#34495e">Empirical variance</text>
  <text x="500" y="296" text-anchor="end" font-family="Arial, Helvetica, sans-serif" font-size="20" font-weight="700" fill="#173b63">{_fmt(v36["empirical_variance"])}</text>
  <text x="120" y="342" font-family="Arial, Helvetica, sans-serif" font-size="17" fill="#34495e">Empirical 95% coverage</text>
  <text x="500" y="342" text-anchor="end" font-family="Arial, Helvetica, sans-serif" font-size="20" font-weight="700" fill="#173b63">{_fmt(v36["empirical_coverage_95"])}</text>
  <text x="120" y="375" font-family="Arial, Helvetica, sans-serif" font-size="15" fill="#6b7785">Fixed seed: {int(v36["seed"])}; {int(v36["trials"])} Gaussian trials.</text>

  <rect x="570" y="155" width="455" height="245" rx="20" fill="#f7f8f4" stroke="#ced4c2" stroke-width="2"/>
  <text x="605" y="202" font-family="Arial, Helvetica, sans-serif" font-size="23" font-weight="700" fill="#3b5b32">V37 inverse covariance bias</text>
  <text x="605" y="250" font-family="Arial, Helvetica, sans-serif" font-size="17" fill="#34495e">Dimension p</text>
  <text x="985" y="250" text-anchor="end" font-family="Arial, Helvetica, sans-serif" font-size="20" font-weight="700" fill="#3b5b32">{int(v37[0]["dimension"])}</text>
  <text x="605" y="296" font-family="Arial, Helvetica, sans-serif" font-size="17" fill="#34495e">Bias factor at nu = 6</text>
  <text x="985" y="296" text-anchor="end" font-family="Arial, Helvetica, sans-serif" font-size="20" font-weight="700" fill="#3b5b32">{_fmt(v37[0]["inverse_covariance_bias_factor"])}</text>
  <text x="605" y="342" font-family="Arial, Helvetica, sans-serif" font-size="17" fill="#34495e">Bias factor at nu = 50</text>
  <text x="985" y="342" text-anchor="end" font-family="Arial, Helvetica, sans-serif" font-size="20" font-weight="700" fill="#3b5b32">{_fmt(v37[-1]["inverse_covariance_bias_factor"])}</text>
  <text x="605" y="375" font-family="Arial, Helvetica, sans-serif" font-size="15" fill="#6b7785">Finite noise samples can systematically inflate estimated precision.</text>

  <rect x="1055" y="155" width="460" height="245" rx="20" fill="#faf6f8" stroke="#d8c8d0" stroke-width="2"/>
  <text x="1090" y="202" font-family="Arial, Helvetica, sans-serif" font-size="23" font-weight="700" fill="#6a3f57">V40 covariance mismatch</text>
  <text x="1090" y="250" font-family="Arial, Helvetica, sans-serif" font-size="17" fill="#34495e">Oracle exact / nominal ratio</text>
  <text x="1470" y="250" text-anchor="end" font-family="Arial, Helvetica, sans-serif" font-size="20" font-weight="700" fill="#6a3f57">{_fmt(float(oracle["variance_ratio_exact_over_nominal"]))}</text>
  <text x="1090" y="296" font-family="Arial, Helvetica, sans-serif" font-size="17" fill="#34495e">Identity-weight ratio</text>
  <text x="1470" y="296" text-anchor="end" font-family="Arial, Helvetica, sans-serif" font-size="20" font-weight="700" fill="#6a3f57">{_fmt(float(identity["variance_ratio_exact_over_nominal"]))}</text>
  <text x="1090" y="342" font-family="Arial, Helvetica, sans-serif" font-size="17" fill="#34495e">Diagonal-weight ratio</text>
  <text x="1470" y="342" text-anchor="end" font-family="Arial, Helvetica, sans-serif" font-size="20" font-weight="700" fill="#6a3f57">{_fmt(float(diagonal["variance_ratio_exact_over_nominal"]))}</text>
  <text x="1090" y="375" font-family="Arial, Helvetica, sans-serif" font-size="15" fill="#6b7785">Misspecified noise weighting can understate uncertainty by about 33% here.</text>

  <rect x="85" y="440" width="680" height="455" rx="20" fill="#fbfbfc" stroke="#d4d9df" stroke-width="2"/>
  <text x="120" y="487" font-family="Arial, Helvetica, sans-serif" font-size="23" font-weight="700" fill="#294f64">V38 Gaussian source discrimination</text>
  <text x="120" y="522" font-family="Arial, Helvetica, sans-serif" font-size="16" fill="#5b6c7c">Equal-prior Bayes error falls exactly with Mahalanobis separation.</text>
  <text x="120" y="610" font-family="Arial, Helvetica, sans-serif" font-size="17" fill="#34495e">d squared = 0</text>
  <text x="395" y="610" text-anchor="end" font-family="Arial, Helvetica, sans-serif" font-size="18" font-weight="700" fill="#294f64">error = 0.5</text>
  <text x="120" y="655" font-family="Arial, Helvetica, sans-serif" font-size="17" fill="#34495e">d squared = 9</text>
  <text x="395" y="655" text-anchor="end" font-family="Arial, Helvetica, sans-serif" font-size="18" font-weight="700" fill="#294f64">error = {_fmt(v38[-1]["equal_prior_bayes_error"])}</text>
  <line x1="480" y1="805" x2="705" y2="805" stroke="#8795a5" stroke-width="2"/>
  <line x1="480" y1="570" x2="480" y2="805" stroke="#8795a5" stroke-width="2"/>
  <polyline points="{" ".join(discrimination_points)}" fill="none" stroke="#294f64" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>
  <circle cx="480" cy="570" r="5" fill="#fff" stroke="#294f64" stroke-width="3"/>
  <circle cx="486.25" cy="616.39" r="5" fill="#fff" stroke="#294f64" stroke-width="3"/>
  <circle cx="505" cy="659.99" r="5" fill="#fff" stroke="#294f64" stroke-width="3"/>
  <circle cx="580" cy="730.43" r="5" fill="#fff" stroke="#294f64" stroke-width="3"/>
  <circle cx="705" cy="773.60" r="5" fill="#fff" stroke="#294f64" stroke-width="3"/>
  <text x="592.5" y="850" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="16" fill="#46586c">Mahalanobis distance squared</text>

  <rect x="795" y="440" width="720" height="455" rx="20" fill="#f8faf8" stroke="#ced8ce" stroke-width="2"/>
  <text x="830" y="487" font-family="Arial, Helvetica, sans-serif" font-size="23" font-weight="700" fill="#43634a">V39 exact independent-search FWER control</text>
  <text x="830" y="522" font-family="Arial, Helvetica, sans-serif" font-size="16" fill="#5b6c7c">The two-sided z threshold must rise as the number of searched locations rises.</text>
  <text x="830" y="610" font-family="Arial, Helvetica, sans-serif" font-size="17" fill="#34495e">1 comparison</text>
  <text x="1125" y="610" text-anchor="end" font-family="Arial, Helvetica, sans-serif" font-size="18" font-weight="700" fill="#43634a">{_fmt(v39[0]["two_sided_z_threshold"])}</text>
  <text x="830" y="655" font-family="Arial, Helvetica, sans-serif" font-size="17" fill="#34495e">1000 comparisons</text>
  <text x="1125" y="655" text-anchor="end" font-family="Arial, Helvetica, sans-serif" font-size="18" font-weight="700" fill="#43634a">{_fmt(v39[-1]["two_sided_z_threshold"])}</text>
  <line x1="1220" y1="805" x2="1490" y2="805" stroke="#8795a5" stroke-width="2"/>
  <line x1="1220" y1="570" x2="1220" y2="805" stroke="#8795a5" stroke-width="2"/>
  <polyline points="{" ".join(fwer_points)}" fill="none" stroke="#43634a" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>
  <circle cx="1220" cy="798.59" r="5" fill="#fff" stroke="#43634a" stroke-width="3"/>
  <circle cx="1310" cy="708.90" r="5" fill="#fff" stroke="#43634a" stroke-width="3"/>
  <circle cx="1400" cy="636.87" r="5" fill="#fff" stroke="#43634a" stroke-width="3"/>
  <circle cx="1490" cy="575.38" r="5" fill="#fff" stroke="#43634a" stroke-width="3"/>
  <text x="1355" y="850" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="16" fill="#46586c">log10 comparison count</text>

  <text x="85" y="955" font-family="Arial, Helvetica, sans-serif" font-size="15" fill="#6a7684">Analytic and fixed-seed synthetic inference validation. No human empirical data and no direct measurement of consciousness or qualia.</text>
</svg>
"""


def main() -> None:
    v36 = v36_gls_amplitude_efficiency()
    v37 = v37_inverse_covariance_bias()
    v38 = v38_gaussian_source_discrimination()
    v39 = v39_independent_search_fwer()
    v40 = v40_covariance_mismatch_sandwich()

    _write_csv(RESULTS / "v36_gls_amplitude_efficiency.csv", [v36])
    _write_csv(RESULTS / "v37_inverse_covariance_bias.csv", v37)
    _write_csv(RESULTS / "v38_gaussian_source_discrimination.csv", v38)
    _write_csv(RESULTS / "v39_independent_search_fwer.csv", v39)
    _write_csv(RESULTS / "v40_covariance_mismatch_sandwich.csv", v40)

    summary = {
        "status": "analytic_and_seeded_synthetic_only",
        "claim_boundary": (
            "finite-sample electromagnetic inference and multiplicity control do not "
            "identify consciousness or qualia"
        ),
        "v36_gls_amplitude_efficiency": v36,
        "v37_inverse_covariance_bias": v37,
        "v38_gaussian_source_discrimination": v38,
        "v39_independent_search_fwer": v39,
        "v40_covariance_mismatch_sandwich": v40,
    }
    RESULTS.mkdir(parents=True, exist_ok=True)
    (RESULTS / "electromagnetic_finite_sample_validation_summary.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    FIGURES.mkdir(parents=True, exist_ok=True)
    (FIGURES / "v36_v40_electromagnetic_finite_sample_validation.svg").write_text(
        _render_svg(v36, v37, v38, v39, v40),
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
