import json
import platform
import sys
from importlib.metadata import version
from pathlib import Path

from streamlit.testing.v1 import AppTest

BASE_DIR = Path(__file__).resolve().parents[1]

installed_versions = {}
for line in (BASE_DIR / "requirements.txt").read_text().splitlines():
    line = line.strip()
    if not line or line.startswith("#"):
        continue
    package, expected = line.split("==")
    actual = version(package)
    assert actual == expected, f"{package}: {actual} != {expected}"
    installed_versions[package] = actual

scenarios = [
    (
        "National", "France excluding Mayotte", None,
        ["3.26", "67.76M", "100", "79 / 100"], "-1.09%",
    ),
    (
        "Guyane", "Guyane", None,
        ["1.41", "288,382", "1", "1 / 1"], "-8.87%",
    ),
    (
        "Metropolitan France", "Metropolitan France", None,
        ["3.25", "65.85M", "96", "77 / 96"], None,
    ),
    (
        "Seine-et-Marne", "Metropolitan France", ["77"],
        ["1.94", "1.45M", "1", "1 / 1"], "-4.06%",
    ),
]

app = AppTest.from_file(str(BASE_DIR / "app.py")).run(timeout=60)
results = []

for label, area, departments, expected, delta in scenarios:
    assert not app.exception, f"{label}: app execution failed."

    if app.sidebar.selectbox[0].value != area:
        app.sidebar.selectbox[0].set_value(area).run(timeout=60)

    if departments is not None:
        app.sidebar.multiselect[0].set_value(departments).run(timeout=60)

    assert not app.exception, f"{label}: filter execution failed."

    values = [metric.value for metric in app.metric[:4]]
    assert values == expected, f"{label}: {values} != {expected}"

    if delta is not None:
        assert app.metric[0].delta == delta, f"{label}: unexpected change."

    assert len(app.get("plotly_chart")) == 4, f"{label}: missing chart."

    local_selector = next(
        widget for widget in app.selectbox
        if widget.label == "Department to explore"
    )
    assert len(local_selector.options) == int(expected[2])

    results.append({"selection": label, "status": "passed"})
    print(f"Passed: {label}")

report = {
    "python_version": platform.python_version(),
    "isolated_environment": sys.prefix != sys.base_prefix,
    "pinned_versions": installed_versions,
    "functional_checks": results,
    "visual_review": "Full dashboard review still pending",
}

(BASE_DIR / "VALIDATION.json").write_text(
    json.dumps(report, indent=2),
    encoding="utf-8",
)
