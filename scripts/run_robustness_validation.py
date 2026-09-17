"""Run Research III formal validation stages V6-V10.

Outputs are analytic and synthetic validation records. They are not human
empirical consciousness measurements.
"""

from __future__ import annotations

import csv
import json
from pathlib import Path

from consciousness_measurement.robustness_simulations import (
    calibration_sample_coverage_experiment,
    canonical_two_site_counterexample,
    conditioning_experiment,
    missingness_stress_experiment,
    resolution_abstention_frontier,
    two_site_nonidentifiability_experiment,
)

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
FIGURES = ROOT / "docs" / "figures"


def write_csv(path: Path, rows: list[dict[str, float]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def svg_header(title: str, desc: str) -> list[str]:
    return [
        '<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="720" viewBox="0 0 1200 720" role="img" aria-labelledby="title desc">',
        f'<title id="title">{title}</title>',
        f'<desc id="desc">{desc}</desc>',
        "<style>",
        ".bg{fill:#fff}.panel{fill:#f8fafc;stroke:#cbd5e1;stroke-width:1}.axis{stroke:#334155;stroke-width:1.4}.grid{stroke:#e2e8f0;stroke-width:1}.title{font:700 24px Arial,Helvetica,sans-serif;fill:#0f172a}.subtitle{font:14px Arial,Helvetica,sans-serif;fill:#475569}.label{font:600 15px Arial,Helvetica,sans-serif;fill:#1e293b}.tick{font:13px Arial,Helvetica,sans-serif;fill:#475569}.lineA{fill:none;stroke:#0f5f78;stroke-width:3}.lineB{fill:none;stroke:#9a4e0d;stroke-width:3}.lineC{fill:none;stroke:#6b4fa3;stroke-width:3}.dotA{fill:#0f5f78}.dotB{fill:#9a4e0d}.band{fill:#dceef3;stroke:none}.ref{stroke:#64748b;stroke-width:1.5;stroke-dasharray:7 6}.note{font:13px Arial,Helvetica,sans-serif;fill:#334155}.box{fill:#fff;stroke:#cbd5e1;stroke-width:1}",
        "</style>",
        '<rect class="bg" width="1200" height="720"/>',
    ]


def line_plot(
    path: Path,
    *,
    title: str,
    subtitle: str,
    x_values: list[float],
    series: list[tuple[str, list[float], str, str]],
    x_label: str,
    y_label: str,
    y_min: float,
    y_max: float,
    x_log: bool = False,
    ref_y: float | None = None,
) -> None:
    import math

    left, right, top, bottom = 110, 55, 105, 105
    plot_w, plot_h = 1200 - left - right, 720 - top - bottom
    transformed = [math.log10(x) if x_log else x for x in x_values]
    xmin, xmax = min(transformed), max(transformed)

    def sx(x: float) -> float:
        tx = math.log10(x) if x_log else x
        return left + (tx - xmin) / (xmax - xmin) * plot_w if xmax > xmin else left + plot_w / 2

    def sy(y: float) -> float:
        return top + (y_max - y) / (y_max - y_min) * plot_h

    out = svg_header(title, subtitle)
    out.append(f'<text class="title" x="{left}" y="42">{title}</text>')
    out.append(f'<text class="subtitle" x="{left}" y="68">{subtitle}</text>')
    out.append(f'<rect class="panel" x="{left}" y="{top}" width="{plot_w}" height="{plot_h}" rx="8"/>')
    for i in range(6):
        y = y_min + i * (y_max - y_min) / 5
        py = sy(y)
        out.append(f'<line class="grid" x1="{left}" y1="{py:.1f}" x2="{left+plot_w}" y2="{py:.1f}"/>')
        out.append(f'<text class="tick" x="{left-14}" y="{py+4:.1f}" text-anchor="end">{y:.3g}</text>')
    for x in x_values:
        px = sx(x)
        out.append(f'<line class="grid" x1="{px:.1f}" y1="{top}" x2="{px:.1f}" y2="{top+plot_h}"/>')
        label = f"{int(x)}" if abs(x-round(x)) < 1e-9 else f"{x:g}"
        out.append(f'<text class="tick" x="{px:.1f}" y="{top+plot_h+27}" text-anchor="middle">{label}</text>')
    if ref_y is not None and y_min <= ref_y <= y_max:
        py = sy(ref_y)
        out.append(f'<line class="ref" x1="{left}" y1="{py:.1f}" x2="{left+plot_w}" y2="{py:.1f}"/>')
    out.append(f'<line class="axis" x1="{left}" y1="{top+plot_h}" x2="{left+plot_w}" y2="{top+plot_h}"/>')
    out.append(f'<line class="axis" x1="{left}" y1="{top}" x2="{left}" y2="{top+plot_h}"/>')
    out.append(f'<text class="label" x="{left+plot_w/2}" y="{720-30}" text-anchor="middle">{x_label}</text>')
    out.append(f'<text class="label" transform="translate(31 {top+plot_h/2}) rotate(-90)" text-anchor="middle">{y_label}</text>')
    legend_y = 91
    legend_x = 650
    for index, (name, ys, line_class, dot_class) in enumerate(series):
        pts = [(sx(x), sy(y)) for x, y in zip(x_values, ys, strict=True)]
        coords = " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
        out.append(f'<polyline class="{line_class}" points="{coords}"/>')
        for x, y in pts:
            out.append(f'<circle class="{dot_class}" cx="{x:.1f}" cy="{y:.1f}" r="4.5"/>')
        ly = legend_y + index * 22
        out.append(f'<line class="{line_class}" x1="{legend_x}" y1="{ly}" x2="{legend_x+32}" y2="{ly}"/>')
        out.append(f'<text class="tick" x="{legend_x+42}" y="{ly+4}">{name}</text>')
    out.append('</svg>')
    path.write_text("\n".join(out), encoding="utf-8")


def interval_band_plot(path: Path, rows: list[dict[str, float]]) -> None:
    title = "Pooled site data can leave population prevalence partially identified"
    subtitle = "Two sites use different calibration channels; the band is the sharp average-prevalence set from the pooled proxy rate alone."
    left, right, top, bottom = 110, 55, 105, 105
    plot_w, plot_h = 1200-left-right, 720-top-bottom
    xmin, xmax = min(r["pooled_proxy_rate"] for r in rows), max(r["pooled_proxy_rate"] for r in rows)
    ymin, ymax = 0.0, 1.0

    def sx(x: float) -> float:
        return left + (x-xmin)/(xmax-xmin)*plot_w

    def sy(y: float) -> float:
        return top + (ymax-y)/(ymax-ymin)*plot_h

    out = svg_header(title, subtitle)
    out.append(f'<text class="title" x="{left}" y="42">{title}</text>')
    out.append(f'<text class="subtitle" x="{left}" y="68">{subtitle}</text>')
    out.append(f'<rect class="panel" x="{left}" y="{top}" width="{plot_w}" height="{plot_h}" rx="8"/>')
    for i in range(6):
        y=i/5
        py=sy(y)
        out.append(f'<line class="grid" x1="{left}" y1="{py:.1f}" x2="{left+plot_w}" y2="{py:.1f}"/>')
        out.append(f'<text class="tick" x="{left-14}" y="{py+4:.1f}" text-anchor="end">{y:.1f}</text>')
    for row in rows:
        px=sx(row["pooled_proxy_rate"])
        out.append(f'<line class="grid" x1="{px:.1f}" y1="{top}" x2="{px:.1f}" y2="{top+plot_h}"/>')
        out.append(f'<text class="tick" x="{px:.1f}" y="{top+plot_h+27}" text-anchor="middle">{row["pooled_proxy_rate"]:.2f}</text>')
    lower=[(sx(r["pooled_proxy_rate"]),sy(r["average_prevalence_lower"])) for r in rows]
    upper=[(sx(r["pooled_proxy_rate"]),sy(r["average_prevalence_upper"])) for r in rows]
    polygon=" ".join(f"{x:.1f},{y:.1f}" for x,y in lower + list(reversed(upper)))
    out.append(f'<polygon class="band" points="{polygon}"/>')
    out.append('<polyline class="lineA" points="' + " ".join(f"{x:.1f},{y:.1f}" for x,y in lower) + '"/>')
    out.append('<polyline class="lineB" points="' + " ".join(f"{x:.1f},{y:.1f}" for x,y in upper) + '"/>')
    out.append(f'<line class="axis" x1="{left}" y1="{top+plot_h}" x2="{left+plot_w}" y2="{top+plot_h}"/>')
    out.append(f'<line class="axis" x1="{left}" y1="{top}" x2="{left}" y2="{top+plot_h}"/>')
    out.append(f'<text class="label" x="{left+plot_w/2}" y="690" text-anchor="middle">pooled positive proxy rate</text>')
    out.append(f'<text class="label" transform="translate(31 {top+plot_h/2}) rotate(-90)" text-anchor="middle">population-average latent prevalence</text>')
    out.append('</svg>')
    path.write_text("\n".join(out), encoding="utf-8")


def main() -> None:
    RESULTS.mkdir(parents=True, exist_ok=True)
    FIGURES.mkdir(parents=True, exist_ok=True)

    calibration = calibration_sample_coverage_experiment(
        prevalence=0.40,
        sensitivity=0.84,
        specificity=0.91,
        deployment_n=1000,
        calibration_sizes=(50, 100, 250, 500, 1000, 2500),
        repetitions=1500,
        delta=0.05,
        seed=20260918,
    )
    missingness = missingness_stress_experiment(
        prevalence=0.40,
        sensitivity=0.84,
        specificity=0.91,
        total_trials=1000,
        missing_fractions=(0.0, 0.05, 0.10, 0.20, 0.30, 0.40, 0.50),
    )
    conditioning = conditioning_experiment(
        youden_values=(0.05, 0.10, 0.20, 0.30, 0.50, 0.75, 0.90),
        proxy_rate_error=0.02,
    )
    site = two_site_nonidentifiability_experiment(
        pooled_proxy_rates=(0.25, 0.30, 0.35, 0.40, 0.45, 0.50, 0.55, 0.60, 0.65),
        site1_weight=0.5,
        site1_sensitivity=0.9,
        site1_specificity=0.9,
        site2_sensitivity=0.7,
        site2_specificity=0.8,
    )
    frontier = resolution_abstention_frontier(
        prevalence=0.40,
        sensitivity=0.84,
        specificity=0.91,
        deployment_sizes=(250, 500, 750, 1000, 1500, 2500),
        calibration_n_per_class=2500,
        repetitions=800,
        delta=0.05,
        maximum_width=0.28,
        seed=20260918,
    )
    counterexample = canonical_two_site_counterexample()

    write_csv(RESULTS / "calibration_sample_uncertainty.csv", calibration)
    write_csv(RESULTS / "missingness_stress.csv", missingness)
    write_csv(RESULTS / "conditioning_stress.csv", conditioning)
    write_csv(RESULTS / "two_site_nonidentifiability.csv", site)
    write_csv(RESULTS / "resolution_abstention_frontier.csv", frontier)

    summary = {
        "status": "analytic_and_synthetic_validation_only",
        "seed": 20260918,
        "v6_calibration_uncertainty": {
            "mean_width_calibration_n50": calibration[0]["mean_width"],
            "mean_width_calibration_n2500": calibration[-1]["mean_width"],
            "minimum_conditional_coverage": min(r["conditional_coverage"] for r in calibration),
        },
        "v7_missingness": {
            "width_at_10_percent_missing": next(r["width"] for r in missingness if r["missing_fraction"] == 0.10),
            "width_at_30_percent_missing": next(r["width"] for r in missingness if r["missing_fraction"] == 0.30),
        },
        "v8_conditioning": {
            "amplification_at_youden_0_05": conditioning[0]["amplification"],
            "amplification_at_youden_0_90": conditioning[-1]["amplification"],
        },
        "v9_two_site": {
            **counterexample,
            "maximum_identified_width_on_grid": max(r["identified_width"] for r in site),
        },
        "v10_abstention": {
            "maximum_allowed_width": 0.28,
            "claim_rate_n750": next(r["resolution_claim_rate"] for r in frontier if r["deployment_n"] == 750.0),
            "claim_rate_n1000": next(r["resolution_claim_rate"] for r in frontier if r["deployment_n"] == 1000.0),
            "claim_rate_n1500": next(r["resolution_claim_rate"] for r in frontier if r["deployment_n"] == 1500.0),
        },
    }
    (RESULTS / "robustness_validation_summary.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    line_plot(
        FIGURES / "calibration_sample_uncertainty.svg",
        title="Finite calibration data dominate measurement uncertainty at small reference samples",
        subtitle="Mean outer identification width when proxy rate, sensitivity, and specificity are all estimated with simultaneous Hoeffding bounds.",
        x_values=[r["calibration_n_per_class"] for r in calibration],
        series=[("mean outer interval width", [r["mean_width"] for r in calibration], "lineA", "dotA")],
        x_label="calibration sample size per declared class (log scale)",
        y_label="mean prevalence interval width",
        y_min=0.0,
        y_max=1.0,
        x_log=True,
    )
    line_plot(
        FIGURES / "missingness_identification_loss.svg",
        title="Arbitrary missingness widens the identified set even with perfect calibration knowledge",
        subtitle="Worst-case missing outcomes are propagated before latent inversion; the widening is an identification result, not imputation noise.",
        x_values=[r["missing_fraction"] for r in missingness],
        series=[("identified-set width", [r["width"] for r in missingness], "lineB", "dotB")],
        x_label="fraction of proxy outcomes missing",
        y_label="latent prevalence interval width",
        y_min=0.0,
        y_max=0.75,
    )
    line_plot(
        FIGURES / "inverse_conditioning_youden.svg",
        title="Weak calibration makes latent inversion ill-conditioned",
        subtitle="A fixed proxy-rate error is amplified by exactly 1/J, where J is the Youden information margin.",
        x_values=[r["youden"] for r in conditioning],
        series=[("error amplification 1/J", [r["amplification"] for r in conditioning], "lineC", "dotA")],
        x_label="Youden information margin J",
        y_label="absolute proxy-to-latent error amplification",
        y_min=0.0,
        y_max=21.0,
    )
    interval_band_plot(FIGURES / "two_site_partial_identification.svg", site)
    line_plot(
        FIGURES / "resolution_abstention_frontier.svg",
        title="Predeclared resolution threshold creates an explicit abstention frontier",
        subtitle="A result is released only when the simultaneous finite-sample interval width is at most 0.28; otherwise the pipeline abstains.",
        x_values=[r["deployment_n"] for r in frontier],
        series=[("resolution claim rate", [r["resolution_claim_rate"] for r in frontier], "lineA", "dotA")],
        x_label="deployment sample size n",
        y_label="fraction of runs meeting resolution criterion",
        y_min=0.0,
        y_max=1.0,
    )

    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
