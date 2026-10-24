import plotly.express as px
import streamlit as st


def render_ranking(view):
    departments = view["departments"]
    metric = "apl_65_or_younger"

    national_apl = float(
        view["national"].loc[
            view["national"]["apl_year"].eq(2024), "weighted_apl"
        ].iloc[0]
    )

    st.subheader("1. Compare departments")
    order = st.radio(
        "Show departments with",
        ["Lowest APL", "Highest APL"],
        horizontal=True,
        key="ranking_order",
    )

    ranked = (
        departments.nsmallest(10, metric)
        if order == "Lowest APL"
        else departments.nlargest(10, metric)
    )

    fig = px.bar(
        ranked,
        x=metric,
        y="department_name",
        orientation="h",
        text_auto=".2f",
        hover_data={
            metric: ":.3f",
            "department_code": True,
            "total_population": ":,.0f",
        },
        labels={
            metric: "APL (consultations/year/standardised inhabitant)",
            "department_name": "Department",
            "department_code": "Department code",
            "total_population": "Population (2022)",
        },
        title=(
            f"{order} among selected departments, 2024"
            "<br><sup>GPs aged 65 or younger. Source: DREES.</sup>"
        ),
        color_discrete_sequence=["#2E86C1"],
        range_x=[0, 1.2 * max(national_apl, ranked[metric].max())],
        height=max(340, 40 * len(ranked) + 140),
    )

    fig.update_yaxes(autorange="reversed", automargin=True)
    fig.update_traces(textposition="outside", cliponaxis=False)
    fig.add_vline(
        x=national_apl,
        line_dash="dash",
        line_color="#808080",
        annotation_text=f"National APL: {national_apl:.2f}",
        annotation_position="top left",
    )

    st.plotly_chart(
        fig,
        width="stretch",
        theme="streamlit",
        key="department_ranking",
        config={"displaylogo": False, "scrollZoom": False},
        alt="Horizontal bars comparing departmental APL with the national benchmark.",
    )

    focus = ranked.iloc[0]
    st.write(
        f"**{focus['department_name']}**: APL **{focus[metric]:.2f}**, "
        f"compared with **{national_apl:.2f}** nationally."
    )
    st.caption(
        f"{len(ranked)} of {len(departments)} selected departments shown."
    )
