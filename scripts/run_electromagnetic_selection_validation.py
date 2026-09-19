from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Any

from consciousness_measurement.electromagnetic_selection_simulations import (
    v41_arbitrary_dependence_bonferroni,
    v42_holm_step_down_gain,
    v43_exact_sign_flip_max_statistic,
    v44_post_selection_coverage_collapse,
    v45_independent_holdout_confirmation,
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
        return f"{value:.6e}"
    return f"{value:.9f}".rstrip("0").rstrip(".")


def _render_svg(
    v41: list[dict[str, float]],
    v42: list[dict[str, float]],
    v43: dict[str, float],
    v44: list[dict[str, float]],
    v45: dict[str, float],
) -> str:
    threshold_points: list[str] = []
    for index, row in enumerate(v41):
        x = 160 + index * 120
        threshold = float(row["two_sided_z_threshold"])
        y = 815 - (threshold - 1.8) / (4.2 - 1.8) * 235
        threshold_points.append(f"{x:.2f},{y:.2f}")

    coverage_points: list[str] = []
    log_floor = -24.0
    for index, row in enumerate(v44):
        x = 875 + index * 120
        coverage = max(float(row["selected_naive_coverage"]), 1e-24)
        log10_coverage = max(__import__("math").log10(coverage), log_floor)
        y = 815 - (log10_coverage - log_floor) / (0.0 - log_floor) * 235
        coverage_points.append(f"{x:.2f},{y:.2f}")

    holm_rejections = int(sum(row["holm_reject"] for row in v42))
    bonferroni_rejections = int(sum(row["bonferroni_reject"] for row in v42))

    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="1000" viewBox="0 0 1600 1000">
  <rect width="1600" height="1000" fill="#ffffff"/>
  <text x="85" y="72" font-family="Arial, Helvetica, sans-serif" font-size="34" font-weight="700" fill="#13243a">Research III V41-V45: multiplicity and selection-safe electromagnetic inference</text>
  <text x="85" y="112" font-family="Arial, Helvetica, sans-serif" font-size="18" fill="#46586c">Arbitrary-dependence FWER control, Holm step-down testing, exact sign-flip inference, post-selection coverage, and independent confirmation.</text>

  <rect x="85" y="155" width="455" height="245" rx="20" fill="#f5f8fb" stroke="#c7d3df" stroke-width="2"/>
  <text x="120" y="202" font-family="Arial, Helvetica, sans-serif" font-size="23" font-weight="700" fill="#173b63">V42 Holm step-down gain</text>
  <text x="120" y="255" font-family="Arial, Helvetica, sans-serif" font-size="17" fill="#34495e">Holm rejections at alpha = 0.05</text>
  <text x="500" y="255" text-anchor="end" font-family="Arial, Helvetica, sans-serif" font-size="22" font-weight="700" fill="#173b63">{holm_rejections}</text>
  <text x="120" y="305" font-family="Arial, Helvetica, sans-serif" font-size="17" fill="#34495e">Single-step Bonferroni rejections</text>
  <text x="500" y="305" text-anchor="end" font-family="Arial, Helvetica, sans-serif" font-size="22" font-weight="700" fill="#173b63">{bonferroni_rejections}</text>
  <text x="120" y="360" font-family="Arial, Helvetica, sans-serif" font-size="15" fill="#6b7785">Holm keeps strong FWER control while using ordered evidence.</text>

  <rect x="570" y="155" width="455" height="245" rx="20" fill="#f7f8f4" stroke="#ced4c2" stroke-width="2"/>
  <text x="605" y="202" font-family="Arial, Helvetica, sans-serif" font-size="23" font-weight="700" fill="#3b5b32">V43 exact sign-flip max statistic</text>
  <text x="605" y="255" font-family="Arial, Helvetica, sans-serif" font-size="17" fill="#34495e">Sign-flip orbit size</text>
  <text x="985" y="255" text-anchor="end" font-family="Arial, Helvetica, sans-serif" font-size="22" font-weight="700" fill="#3b5b32">{int(v43["orbit_size"])}</text>
  <text x="605" y="305" font-family="Arial, Helvetica, sans-serif" font-size="17" fill="#34495e">Exceeding orbit points</text>
  <text x="985" y="305" text-anchor="end" font-family="Arial, Helvetica, sans-serif" font-size="22" font-weight="700" fill="#3b5b32">{int(v43["exceedances"])}</text>
  <text x="605" y="350" font-family="Arial, Helvetica, sans-serif" font-size="17" fill="#34495e">Exact randomization p-value</text>
  <text x="985" y="350" text-anchor="end" font-family="Arial, Helvetica, sans-serif" font-size="22" font-weight="700" fill="#3b5b32">{_fmt(float(v43["exact_randomization_pvalue"]))}</text>

  <rect x="1055" y="155" width="460" height="245" rx="20" fill="#faf6f8" stroke="#d8c8d0" stroke-width="2"/>
  <text x="1090" y="202" font-family="Arial, Helvetica, sans-serif" font-size="23" font-weight="700" fill="#6a3f57">V45 independent confirmation</text>
  <text x="1090" y="255" font-family="Arial, Helvetica, sans-serif" font-size="17" fill="#34495e">Same-data reuse false positive</text>
  <text x="1470" y="255" text-anchor="end" font-family="Arial, Helvetica, sans-serif" font-size="22" font-weight="700" fill="#6a3f57">{_fmt(float(v45["empirical_reuse_false_positive"]))}</text>
  <text x="1090" y="305" font-family="Arial, Helvetica, sans-serif" font-size="17" fill="#34495e">Independent holdout false positive</text>
  <text x="1470" y="305" text-anchor="end" font-family="Arial, Helvetica, sans-serif" font-size="22" font-weight="700" fill="#6a3f57">{_fmt(float(v45["empirical_holdout_false_positive"]))}</text>
  <text x="1090" y="360" font-family="Arial, Helvetica, sans-serif" font-size="15" fill="#6b7785">Selection and confirmation use independent Gaussian samples.</text>

  <rect x="85" y="440" width="680" height="455" rx="20" fill="#fbfbfc" stroke="#d4d9df" stroke-width="2"/>
  <text x="120" y="487" font-family="Arial, Helvetica, sans-serif" font-size="23" font-weight="700" fill="#294f64">V41 arbitrary-dependence Bonferroni threshold</text>
  <text x="120" y="522" font-family="Arial, Helvetica, sans-serif" font-size="16" fill="#5b6c7c">The union bound remains valid without independence assumptions.</text>
  <line x1="160" y1="815" x2="520" y2="815" stroke="#8795a5" stroke-width="2"/>
  <line x1="160" y1="580" x2="160" y2="815" stroke="#8795a5" stroke-width="2"/>
  <polyline points="{" ".join(threshold_points)}" fill="none" stroke="#294f64" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>
  <circle cx="160" cy="799.34" r="5" fill="#ffffff" stroke="#294f64" stroke-width="3"/>
  <circle cx="280" cy="716.39" r="5" fill="#ffffff" stroke="#294f64" stroke-width="3"/>
  <circle cx="400" cy="650.43" r="5" fill="#ffffff" stroke="#294f64" stroke-width="3"/>
  <circle cx="520" cy="594.14" r="5" fill="#ffffff" stroke="#294f64" stroke-width="3"/>
  <text x="340" y="855" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="16" fill="#46586c">comparisons: 1, 10, 100, 1000</text>
  <text x="120" y="875" font-family="Arial, Helvetica, sans-serif" font-size="15" fill="#6b7785">Target FWER = 0.05 for every union-bound threshold.</text>

  <rect x="795" y="440" width="720" height="455" rx="20" fill="#f8faf8" stroke="#ced8ce" stroke-width="2"/>
  <text x="830" y="487" font-family="Arial, Helvetica, sans-serif" font-size="23" font-weight="700" fill="#43634a">V44 naive post-selection coverage collapse</text>
  <text x="830" y="518" font-family="Arial, Helvetica, sans-serif" font-size="15" fill="#5b6c7c">Select the largest absolute null statistic, then reuse its ordinary</text>
  <text x="830" y="540" font-family="Arial, Helvetica, sans-serif" font-size="15" fill="#5b6c7c">marginal interval.</text>
  <line x1="875" y1="815" x2="1235" y2="815" stroke="#8795a5" stroke-width="2"/>
  <line x1="875" y1="580" x2="875" y2="815" stroke="#8795a5" stroke-width="2"/>
  <polyline points="{" ".join(coverage_points)}" fill="none" stroke="#43634a" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>
  <text x="1055" y="855" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="16" fill="#46586c">comparisons: 1, 10, 100, 1000</text>
  <text x="1280" y="610" font-family="Arial, Helvetica, sans-serif" font-size="16" fill="#34495e">K = 1: coverage = 0.95</text>
  <text x="1280" y="650" font-family="Arial, Helvetica, sans-serif" font-size="16" fill="#34495e">K = 10: coverage = 0.598737</text>
  <text x="1280" y="690" font-family="Arial, Helvetica, sans-serif" font-size="16" fill="#34495e">K = 100: coverage = 0.005921</text>
  <text x="1280" y="730" font-family="Arial, Helvetica, sans-serif" font-size="16" fill="#34495e">K = 1000: coverage approx 5.29e-23</text>
  <text x="830" y="875" font-family="Arial, Helvetica, sans-serif" font-size="15" fill="#6b7785">The exact law is marginal_coverage^K under independent null coordinates.</text>

  <text x="85" y="955" font-family="Arial, Helvetica, sans-serif" font-size="15" fill="#6a7684">Analytic and fixed-seed synthetic inference. No human empirical data and no direct measurement of consciousness or qualia.</text>
</svg>
"""


def main() -> None:
    v41 = v41_arbitrary_dependence_bonferroni()
    v42 = v42_holm_step_down_gain()
    v43 = v43_exact_sign_flip_max_statistic()
    v44 = v44_post_selection_coverage_collapse()
    v45 = v45_independent_holdout_confirmation()

    _write_csv(RESULTS / "v41_bonferroni_arbitrary_dependence.csv", v41)
    _write_csv(RESULTS / "v42_holm_step_down.csv", v42)
    _write_single_row_csv(RESULTS / "v43_sign_flip_max_statistic.csv", v43)
    _write_csv(RESULTS / "v44_post_selection_coverage.csv", v44)
    _write_single_row_csv(RESULTS / "v45_independent_holdout.csv", v45)

    summary = {
        "status": "analytic_and_synthetic_only",
        "claim_boundary": (
            "multiplicity and selection-safe inference do not identify consciousness "
            "or turn statistical significance into an experiential measurement"
        ),
        "v41_arbitrary_dependence_bonferroni": v41,
        "v42_holm_step_down": v42,
        "v43_exact_sign_flip_max_statistic": v43,
        "v44_post_selection_coverage": v44,
        "v45_independent_holdout": v45,
    }
    RESULTS.mkdir(parents=True, exist_ok=True)
    (RESULTS / "electromagnetic_selection_validation_summary.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    FIGURES.mkdir(parents=True, exist_ok=True)
    (FIGURES / "v41_v45_electromagnetic_selection_validation.svg").write_text(
        _render_svg(v41, v42, v43, v44, v45),
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
