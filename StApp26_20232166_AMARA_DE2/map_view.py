import json
from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st


@st.cache_data(show_spinner=False)
def load_map_assets(base_dir):
    boundaries = json.loads(
        (base_dir / "assets" / "departments_2024.geojson")
        .read_text(encoding="utf-8")
    )
    national_data = pd.read_csv(
        base_dir / "data" / "processed" / "apl_departments_2024.csv",
        usecols=["apl_65_or_younger"],
    )
    values = national_data["apl_65_or_younger"]
    return boundaries, [float(values.min()), float(values.max())]


def render_map(view):
    base_dir = Path(__file__).resolve().parent
    boundaries, colour_range = load_map_assets(base_dir)
    departments = view["departments"]
    selected_codes = set(departments["department_code"])

    area_codes = {
        "Metropolitan France": {
            code for code in selected_codes if not code.startswith("97")
        },
        "Guadeloupe": {"971"},
        "Martinique": {"972"},
        "Guyane": {"973"},
        "La Réunion": {"974"},
    }
    available = [
        area for area, codes in area_codes.items()
        if codes & selected_codes
    ]

    st.subheader("2. Explore geographic differences")

    focus = st.selectbox(
        "Map focus",
        available,
        key="map_focus_" + "|".join(available),
        disabled=len(available) == 1,
    )

    map_data = departments.loc[
        departments["department_code"].isin(area_codes[focus])
    ]
    map_codes = set(map_data["department_code"])
    map_geojson = {
        "type": "FeatureCollection",
        "features": [
            feature for feature in boundaries["features"]
            if feature["properties"]["code"] in map_codes
        ],
    }

    fig = px.choropleth(
        map_data,
        geojson=map_geojson,
        locations="department_code",
        featureidkey="properties.code",
        color="apl_65_or_younger",
        hover_name="department_name",
        hover_data={
            "apl_65_or_younger": ":.3f",
            "department_code": True,
            "total_population": ":,.0f",
        },
        labels={
            "apl_65_or_younger": "APL",
            "department_code": "Department code",
            "total_population": "Population (2022)",
        },
        color_continuous_scale="Cividis",
        range_color=colour_range,
        projection="mercator",
        title=(
            f"Potential GP access in {focus}, 2024"
            "<br><sup>GPs aged 65 or younger. Source: DREES.</sup>"
        ),
        height=550,
    )

    fig.update_geos(
        fitbounds="locations",
        visible=False,
        bgcolor="rgba(0,0,0,0)",
    )
    fig.update_traces(marker_line_color="white", marker_line_width=0.5)
    fig.update_layout(
        coloraxis_colorbar={
            "title": "Consultations/year<br>per standardised<br>inhabitant"
        }
    )

    st.plotly_chart(
        fig,
        width="stretch",
        theme="streamlit",
        key="department_map",
        config={"displaylogo": False, "scrollZoom": False},
        alt=f"Map of departmental potential GP access in {focus}, 2024.",
    )

    st.caption(
        f"{len(map_data)} of {len(departments)} selected departments shown. "
        "The national colour scale stays fixed across views."
    )
    st.caption(
        "[Boundaries: Etalab/IGN]"
        "(https://www.data.gouv.fr/datasets/contours-administratifs) · ODbL."
    )
