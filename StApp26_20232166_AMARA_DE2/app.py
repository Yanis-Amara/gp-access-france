from pathlib import Path
import streamlit as st
from context_view import render_context
from trend_view import render_trends
from local_view import render_local
from map_view import render_map
from ranking import render_ranking
from metrics import render_metrics
from data_and_filters import prepare_view

BASE_DIR = Path(__file__).resolve().parent

st.set_page_config(
    page_title="GP Access in France",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded",
)

with st.sidebar:
    st.image(
        str(BASE_DIR / "assets" / "efrei_logo.png"),
        width=180,
        alt="EFREI logo",
    )
    st.markdown("**Yanis AMARA**")
    st.caption("DATA ENGINEERING · 2026–2027")

    with st.expander("Course and contact"):
        st.markdown("""
**Institution:** EFREI
**Course:** Data Analysis & Visualization
**Professor:** Dr. Mano MATHEW

[Yanis.amara@efrei.net](mailto:Yanis.amara@efrei.net)
[LinkedIn profile](https://www.linkedin.com/in/yanis-amara-3a3953292/)
""")

st.title("Access to General Practitioners in France")

st.write(
    "A national average can hide local gaps. Explore differences "
    "between departments, what their averages hide, and how potential "
    "access changed between 2023 and 2024."
)

st.caption(
    "Source: DREES APL · France excluding Mayotte · "
    "2024 snapshot with a 2023 comparison"
)

st.info(
    "APL estimates potential access in annual consultations per "
    "age-standardised inhabitant. This dashboard focuses on GPs "
    "aged 65 or younger."
)


view = prepare_view(BASE_DIR)


render_metrics(view)


render_ranking(view)


render_map(view)


render_local(view)


render_trends(view)


render_context(view)
