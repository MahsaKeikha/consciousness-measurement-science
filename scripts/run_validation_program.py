"""Run the deterministic Research III formal validation battery.

Outputs are simulation/analytic validation records, not human empirical data.
"""

from __future__ import annotations

import csv
import json
from pathlib import Path

from consciousness_measurement.simulation_validation import (
    ChannelCalibration,
    dependence_stress_experiment,
    finite_sample_coverage_experiment,
    structural_alignment_power_experiment,
    transport_stress_experiment,
)

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
FIGURES = ROOT / "docs" / "figures"


def write_csv(name: str, rows: list[dict[str, float]]) -> None:
    path = RESULTS / name
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def svg_header(width: int, height: int, title: str, desc: str) -> list[str]:
    scale = max(1000.0 / width, 600.0 / height, 1.0)
    intrinsic_width = width * scale
    intrinsic_height = height * scale
    return [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{intrinsic_width:.3f}" height="{intrinsic_height:.3f}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">',
        f"<title id=\"title\">{title}</title>",
        f"<desc id=\"desc\">{desc}</desc>",
        "<style>",
        ".bg{fill:#ffffff}.panel{fill:#f8fafc;stroke:#d7dee8;stroke-width:1}.axis{stroke:#334155;stroke-width:1.2}.grid{stroke:#dbe3ec;stroke-width:1}.txt{font-family:Arial,Helvetica,sans-serif;fill:#172033}.small{font-size:13px}.label{font-size:15px;font-weight:600}.title{font-size:21px;font-weight:700}.line1{fill:none;stroke:#0f5f78;stroke-width:3}.line2{fill:none;stroke:#9a4e0d;stroke-width:3}.line3{fill:none;stroke:#6b4fa3;stroke-width:3}.dot1{fill:#0f5f78}.dot2{fill:#9a4e0d}.dot3{fill:#6b4fa3}.ref{stroke:#6b7280;stroke-width:1.5;stroke-dasharray:6 5}.zero{stroke:#111827;stroke-width:1.4}.heattext{font-family:Arial,Helvetica,sans-serif;font-size:12px;fill:#172033;text-anchor:middle}.note{font-family:Arial,Helvetica,sans-serif;font-size:12px;fill:#475569}",
        "</style>",
        '<rect class="bg" width="100%" height="100%"/>',
    ]


def polyline(points: list[tuple[float, float]], klass: str) -> str:
    coords = " ".join(f"{x:.1f},{y:.1f}" for x, y in points)
    return f'<polyline class="{klass}" points="{coords}"/>'


def plot_xy(
    path: Path,
    *,
    title: str,
    desc: str,
    x_values: list[float],
    series: list[tuple[str, list[float], str, str]],
    x_label: str,
    y_label: str,
    y_min: float,
    y_max: float,
    reference_y: float | None = None,
    x_log: bool = False,
) -> None:
    width, height = 900, 560
    left, right, top, bottom = 90, 40, 85, 85
    plot_w, plot_h = width - left - right, height - top - bottom
    import math

    x_map_values = [math.log10(x) if x_log else x for x in x_values]
    xmin, xmax = min(x_map_values), max(x_map_values)

    def sx(x: float) -> float:
        xv = math.log10(x) if x_log else x
        return left + (xv - xmin) / (xmax - xmin) * plot_w if xmax > xmin else left + plot_w / 2

    def sy(y: float) -> float:
        return top + (y_max - y) / (y_max - y_min) * plot_h

    out = svg_header(width, height, title, desc)
    out.append(f'<rect class="panel" x="{left}" y="{top}" width="{plot_w}" height="{plot_h}" rx="8"/>')
    for i in range(6):
        y = y_min + i * (y_max - y_min) / 5
        py = sy(y)
        out.append(f'<line class="grid" x1="{left}" y1="{py:.1f}" x2="{left+plot_w}" y2="{py:.1f}"/>')
        out.append(f'<text class="txt small" x="{left-12}" y="{py+4:.1f}" text-anchor="end">{y:.2f}</text>')
    for x in x_values:
        px = sx(x)
        out.append(f'<line class="grid" x1="{px:.1f}" y1="{top}" x2="{px:.1f}" y2="{top+plot_h}"/>')
        label = f"{int(x)}" if abs(x-round(x)) < 1e-9 else f"{x:g}"
        out.append(f'<text class="txt small" x="{px:.1f}" y="{top+plot_h+25}" text-anchor="middle">{label}</text>')
    if reference_y is not None and y_min <= reference_y <= y_max:
        py = sy(reference_y)
        out.append(f'<line class="ref" x1="{left}" y1="{py:.1f}" x2="{left+plot_w}" y2="{py:.1f}"/>')
    out.append(f'<line class="axis" x1="{left}" y1="{top+plot_h}" x2="{left+plot_w}" y2="{top+plot_h}"/>')
    out.append(f'<line class="axis" x1="{left}" y1="{top}" x2="{left}" y2="{top+plot_h}"/>')
    out.append(f'<text class="txt title" x="{left}" y="42">{title}</text>')
    out.append(f'<text class="txt label" x="{left+plot_w/2}" y="{height-28}" text-anchor="middle">{x_label}</text>')
    out.append(f'<text class="txt label" transform="translate(26 {top+plot_h/2}) rotate(-90)" text-anchor="middle">{y_label}</text>')

    legend_x = left + 12
    for idx, (name, ys, line_class, dot_class) in enumerate(series):
        points = [(sx(x), sy(y)) for x, y in zip(x_values, ys, strict=True)]
        out.append(polyline(points, line_class))
        for x, y in points:
            out.append(f'<circle class="{dot_class}" cx="{x:.1f}" cy="{y:.1f}" r="4"/>')
        ly = 62 + idx * 20
        out.append(f'<line class="{line_class}" x1="{legend_x}" y1="{ly}" x2="{legend_x+28}" y2="{ly}"/>')
        out.append(f'<text class="txt small" x="{legend_x+36}" y="{ly+4}">{name}</text>')
    out.append('</svg>')
    path.write_text("\n".join(out), encoding="utf-8")


def heatmap_transport(path: Path, rows: list[dict[str, float]]) -> None:
    width, height = 760, 650
    out = svg_header(
        width,
        height,
        "Calibration transport stress test",
        "Exact absolute bias in a latent contrast when sensitivity and specificity shift but baseline calibration is reused.",
    )
    vals_s = sorted({row["sensitivity_shift"] for row in rows})
    vals_c = sorted({row["specificity_shift"] for row in rows})
    lookup = {(r["sensitivity_shift"], r["specificity_shift"]): r["absolute_bias"] for r in rows}
    max_bias = max(lookup.values()) or 1.0
    left, top, cell = 155, 105, 82
    out.append('<text class="txt title" x="70" y="45">Calibration transport stress test</text>')
    out.append('<text class="note" x="70" y="68">Cell value = |bias| in corrected latent contrast; zero shift must return zero.</text>')
    for j, dc in enumerate(vals_c):
        x = left + j * cell + cell / 2
        out.append(f'<text class="txt small" x="{x}" y="{top-18}" text-anchor="middle">{dc:+.2f}</text>')
    for i, ds in enumerate(reversed(vals_s)):
        y = top + i * cell + cell / 2
        out.append(f'<text class="txt small" x="{left-18}" y="{y+4}" text-anchor="end">{ds:+.2f}</text>')
        for j, dc in enumerate(vals_c):
            x0 = left + j * cell
            y0 = top + i * cell
            value = lookup[(ds, dc)]
            intensity = value / max_bias
            r = int(244 - 75 * intensity)
            g = int(248 - 118 * intensity)
            b = int(252 - 135 * intensity)
            out.append(f'<rect x="{x0}" y="{y0}" width="{cell}" height="{cell}" fill="rgb({r},{g},{b})" stroke="#ffffff"/>')
            out.append(f'<text class="heattext" x="{x0+cell/2}" y="{y0+cell/2+4}">{value:.3f}</text>')
    out.append(f'<text class="txt label" x="{left+len(vals_c)*cell/2}" y="{top+len(vals_s)*cell+48}" text-anchor="middle">specificity shift</text>')
    out.append(f'<text class="txt label" transform="translate(36 {top+len(vals_s)*cell/2}) rotate(-90)" text-anchor="middle">sensitivity shift</text>')
    out.append('</svg>')
    path.write_text("\n".join(out), encoding="utf-8")


def main() -> None:
    RESULTS.mkdir(parents=True, exist_ok=True)
    FIGURES.mkdir(parents=True, exist_ok=True)

    coverage = finite_sample_coverage_experiment(
        prevalence=0.40,
        sensitivity=0.84,
        specificity=0.91,
        calibration_half_width=0.02,
        sample_sizes=(50, 100, 250, 500, 1000, 2500),
        repetitions=2500,
        delta=0.05,
        seed=20260917,
    )
    dependence = dependence_stress_experiment(
        prior=0.35,
        channels=(
            ChannelCalibration(0.80, 0.90),
            ChannelCalibration(0.85, 0.88),
            ChannelCalibration(0.78, 0.92),
        ),
        dependence_grid=(0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0),
    )
    transport = transport_stress_experiment(
        latent_prevalence_after=0.55,
        baseline_sensitivity=0.84,
        baseline_specificity=0.91,
        sensitivity_shifts=(-0.10, -0.05, 0.0, 0.05, 0.10),
        specificity_shifts=(-0.10, -0.05, 0.0, 0.05, 0.10),
    )
    structural = structural_alignment_power_experiment(
        signal_levels=(0.0, 0.25, 0.50, 0.75, 0.90),
        replicates=160,
        items=20,
        dimensions=3,
        permutations=199,
        alpha=0.05,
        seed=20260917,
    )

    write_csv("finite_sample_coverage.csv", coverage)
    write_csv("dependence_stress.csv", dependence)
    write_csv("transport_stress.csv", transport)
    write_csv("structural_alignment_power.csv", structural)

    summary = {
        "status": "synthetic_and_analytic_validation_only",
        "seed": 20260917,
        "finite_sample": {
            "nominal_coverage": 0.95,
            "minimum_observed_coverage": min(row["coverage"] for row in coverage),
            "width_n50": coverage[0]["mean_width"],
            "width_n2500": coverage[-1]["mean_width"],
        },
        "dependence": {
            "naive_posterior": dependence[0]["naive_independence_posterior"],
            "posterior_at_full_shared_dependence": dependence[-1]["true_posterior"],
            "absolute_error_at_full_shared_dependence": dependence[-1]["absolute_error"],
        },
        "transport": {
            "zero_shift_bias": next(
                row["bias"] for row in transport
                if row["sensitivity_shift"] == 0.0 and row["specificity_shift"] == 0.0
            ),
            "maximum_absolute_bias_on_grid": max(row["absolute_bias"] for row in transport),
        },
        "structural_alignment": {
            "null_rejection_rate": structural[0]["rejection_rate"],
            "high_signal_rejection_rate": structural[-1]["rejection_rate"],
            "high_signal_mean_alignment": structural[-1]["mean_alignment"],
        },
    }
    (RESULTS / "validation_summary.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    plot_xy(
        FIGURES / "finite_sample_identification.svg",
        title="Finite-sample identification: width contracts with sample size",
        desc="Mean width of a conservative latent prevalence interval across 2500 Bernoulli simulations at each sample size.",
        x_values=[row["n"] for row in coverage],
        series=[("mean identification width", [row["mean_width"] for row in coverage], "line1", "dot1")],
        x_label="sample size n (log scale)",
        y_label="mean interval width",
        y_min=0.0,
        y_max=max(row["mean_width"] for row in coverage) * 1.08,
        x_log=True,
    )
    plot_xy(
        FIGURES / "finite_sample_coverage.svg",
        title="Finite-sample coverage stress test",
        desc="Empirical coverage of the conservative interval, with a dashed 0.95 nominal reference line.",
        x_values=[row["n"] for row in coverage],
        series=[("empirical coverage", [row["coverage"] for row in coverage], "line1", "dot1")],
        x_label="sample size n (log scale)",
        y_label="coverage",
        y_min=0.90,
        y_max=1.0,
        reference_y=0.95,
        x_log=True,
    )
    plot_xy(
        FIGURES / "dependence_stress.svg",
        title="Conditional dependence breaks naive multimodal fusion",
        desc="Exact posterior under a shared-uniform dependence model compared with the conditional-independence posterior.",
        x_values=[row["dependence"] for row in dependence],
        series=[
            ("true posterior under dependence", [row["true_posterior"] for row in dependence], "line1", "dot1"),
            ("naive independence posterior", [row["naive_independence_posterior"] for row in dependence], "line2", "dot2"),
        ],
        x_label="dependence mixture rho",
        y_label="posterior for declared latent target",
        y_min=min(row["true_posterior"] for row in dependence) * 0.95,
        y_max=1.0,
    )
    heatmap_transport(FIGURES / "transport_bias_surface.svg", transport)
    plot_xy(
        FIGURES / "structural_alignment_power.svg",
        title="Relational-geometry permutation test: null and power behavior",
        desc="Rejection rate across synthetic signal strengths using a permutation test on distance-matrix alignment.",
        x_values=[row["signal"] for row in structural],
        series=[("rejection rate", [row["rejection_rate"] for row in structural], "line3", "dot3")],
        x_label="shared latent geometry signal",
        y_label="rejection rate at alpha = 0.05",
        y_min=0.0,
        y_max=1.0,
        reference_y=0.05,
    )

    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
