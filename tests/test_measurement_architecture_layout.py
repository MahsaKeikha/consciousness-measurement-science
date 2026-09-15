from __future__ import annotations

import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIGURE = ROOT / "docs" / "figures" / "measurement_architecture.svg"
SVG_NS = "{http://www.w3.org/2000/svg}"
FONT_SIZE = {"b": 17.0, "s": 13.5, "s2": 15.0}
HORIZONTAL_PADDING = 16.0
WIDTH_FACTOR = 0.58
EXPECTED_NODES = {
    "latent",
    "report",
    "behavior",
    "neural",
    "perturbation",
    "physiology",
    "context",
    "cep",
    "output",
}


def _number(element: ET.Element, name: str) -> float:
    return float(element.attrib[name])


def _label_lines(element: ET.Element) -> list[str]:
    tspans = element.findall(f"{SVG_NS}tspan")
    if tspans:
        return ["".join(t.itertext()).strip() for t in tspans]
    return ["".join(element.itertext()).strip()]


def _baselines(element: ET.Element) -> list[float]:
    tspans = element.findall(f"{SVG_NS}tspan")
    if tspans:
        values = []
        for tspan in tspans:
            y = tspan.attrib.get("y", element.attrib.get("y"))
            assert y is not None
            values.append(float(y))
        return values
    return [float(element.attrib["y"])]


def test_measurement_architecture_labels_stay_inside_parent_boxes() -> None:
    root = ET.parse(FIGURE).getroot()
    _, _, view_width, view_height = [
        float(value) for value in root.attrib["viewBox"].split()
    ]

    boxes: dict[str, ET.Element] = {}
    for rect in root.iter(f"{SVG_NS}rect"):
        node = rect.attrib.get("data-node")
        if node:
            boxes[node] = rect
            x = _number(rect, "x")
            y = _number(rect, "y")
            width = _number(rect, "width")
            height = _number(rect, "height")
            assert 0 <= x < x + width <= view_width
            assert 0 <= y < y + height <= view_height

    assert set(boxes) == EXPECTED_NODES

    checked = 0
    for text in root.iter(f"{SVG_NS}text"):
        parent = text.attrib.get("data-parent")
        if not parent:
            continue
        checked += 1
        assert parent in boxes
        box = boxes[parent]
        box_x = _number(box, "x")
        box_y = _number(box, "y")
        box_width = _number(box, "width")
        box_height = _number(box, "height")

        assert text.attrib.get("text-anchor") == "middle"
        text_x = _number(text, "x")
        assert abs(text_x - (box_x + box_width / 2.0)) <= 0.5

        css_class = text.attrib["class"]
        font_size = FONT_SIZE[css_class]
        available_width = box_width - 2.0 * HORIZONTAL_PADDING
        for line in _label_lines(text):
            estimated_width = len(line) * font_size * WIDTH_FACTOR
            assert estimated_width <= available_width, (
                f"{parent!r} label {line!r} exceeds conservative width budget: "
                f"{estimated_width:.1f} > {available_width:.1f}"
            )

        for baseline in _baselines(text):
            assert box_y + 16.0 <= baseline <= box_y + box_height - 10.0

    assert checked == 21
