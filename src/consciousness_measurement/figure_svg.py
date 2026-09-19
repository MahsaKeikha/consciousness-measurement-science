from __future__ import annotations

from html import escape
FONT = "Arial, Helvetica, sans-serif"


def text(
    x: float,
    y: float,
    value: object,
    *,
    size: int = 18,
    weight: int = 400,
    fill: str = "#253244",
    anchor: str = "start",
) -> str:
    return (
        f'<text x="{x}" y="{y}" text-anchor="{anchor}" '
        f'font-family="{FONT}" font-size="{size}" font-weight="{weight}" '
        f'fill="{fill}">{escape(str(value))}</text>'
    )


def line(
    x1: float,
    y1: float,
    x2: float,
    y2: float,
    *,
    stroke: str = "#d8dee8",
    width: float = 1.0,
    dash: str | None = None,
) -> str:
    dash_attr = f' stroke-dasharray="{dash}"' if dash else ""
    return (
        f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" '
        f'stroke="{stroke}" stroke-width="{width}"{dash_attr}/>'
    )


def rect(
    x: float,
    y: float,
    width: float,
    height: float,
    *,
    fill: str = "#ffffff",
    stroke: str = "#d5dce7",
    stroke_width: float = 1.0,
    radius: float = 0.0,
) -> str:
    return (
        f'<rect x="{x}" y="{y}" width="{width}" height="{height}" '
        f'rx="{radius}" fill="{fill}" stroke="{stroke}" '
        f'stroke-width="{stroke_width}"/>'
    )


def circle(x: float, y: float, radius: float, *, fill: str) -> str:
    return f'<circle cx="{x}" cy="{y}" r="{radius}" fill="{fill}"/>'


def polyline(
    points: list[tuple[float, float]],
    *,
    stroke: str,
    width: float = 4.0,
    dash: str | None = None,
) -> str:
    dash_attr = f' stroke-dasharray="{dash}"' if dash else ""
    encoded = " ".join(f"{x:.1f},{y:.1f}" for x, y in points)
    return (
        f'<polyline points="{encoded}" fill="none" stroke="{stroke}" '
        f'stroke-width="{width}" stroke-linecap="round" '
        f'stroke-linejoin="round"{dash_attr}/>'
    )


def metric_card(
    x: float,
    y: float,
    width: float,
    height: float,
    *,
    kicker: str,
    title: str,
    value: str,
    note: str,
    accent: str,
) -> str:
    parts = [
        rect(
            x,
            y,
            width,
            height,
            fill="#ffffff",
            stroke="#d6dde7",
            stroke_width=1.2,
            radius=12,
        ),
        text(x + 22, y + 29, kicker.upper(), size=12, weight=700, fill=accent),
        text(x + 22, y + 58, title, size=17, weight=700, fill="#182437"),
        text(x + 22, y + 103, value, size=28, weight=700, fill=accent),
        text(x + 22, y + 132, note, size=13, fill="#637083"),
    ]
    return "\n".join(parts)
