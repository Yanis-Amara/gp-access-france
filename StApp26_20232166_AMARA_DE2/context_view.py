import json
from pathlib import Path

import streamlit as st


def render_context(view):
    st.subheader("5. From evidence to local action")
    st.caption(
        "For municipalities, healthcare centres and regional health authorities."
    )

    st.write(
        "Start with departments combining below-national access and decline, "
        "then inspect the differences between their communes. "
        "Use these signals to guide further local investigation."
    )
    st.markdown(
        "- Check waiting times and whether practices accept new patients.\n"
        "- Discuss staffing, transport and digital access with local services.\n"
        "- Follow later APL releases before assessing policy outcomes."
    )

    st.caption(
        f"Current selection: {len(view['departments'])} departments. "
        "The methodological notes below apply to every selection."
    )

    path = Path(__file__).resolve().parent / "assets" / "context_notes.json"
    sections = json.loads(path.read_text(encoding="utf-8"))

    for title, text in sections.items():
        with st.expander(title):
            st.markdown(text)
