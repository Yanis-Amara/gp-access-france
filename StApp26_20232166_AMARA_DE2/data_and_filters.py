import pandas as pd
import streamlit as st


@st.cache_data(show_spinner=False)
def load_tables(data_dir):
    files = {
        "communes": "apl_communes_2023_2024.csv",
        "departments": "apl_departments_2024.csv",
        "trends": "apl_department_trends.csv",
        "national": "apl_national_trend.csv",
    }
    return {
        name: pd.read_csv(
            data_dir / filename,
            dtype={"commune_code": "string", "department_code": "string"},
        )
        for name, filename in files.items()
    }


def prepare_view(base_dir):
    tables = load_tables(base_dir / "data" / "processed")

    department_names = (
        tables["departments"]
        .set_index("department_code")["department_name"]
        .to_dict()
    )
    all_codes = sorted(department_names, key=department_names.get)

    area_codes = {
        "France excluding Mayotte": all_codes,
        "Metropolitan France": [
            code for code in all_codes if not code.startswith("97")
        ],
        "Guadeloupe": ["971"],
        "Martinique": ["972"],
        "Guyane": ["973"],
        "La Réunion": ["974"],
    }

    st.sidebar.divider()
    st.sidebar.subheader("Explore")

    area = st.sidebar.selectbox(
        "Area",
        options=list(area_codes),
        key="area",
    )
    selected = st.sidebar.multiselect(
        "Departments",
        options=area_codes[area],
        format_func=lambda code: f"{department_names[code]} ({code})",
        placeholder="All departments in this area",
        help="Leave empty to include the whole selected area.",
        key=f"departments_{area}",
    )
    selected_codes = selected or area_codes[area]

    view = {}
    for name in ("communes", "departments", "trends"):
        data = tables[name]
        view[name] = data.loc[
            data["department_code"].isin(selected_codes)
        ].copy()

    view["national"] = tables["national"]
    view["area"] = area
    return view
