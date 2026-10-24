import plotly.express as px
import streamlit as st


def render_trends(view):
    st.subheader("4. Is access improving?")

    trends = view["trends"].copy()
    national_apl = float(
        view["national"].loc[
            view["national"]["apl_year"].eq(2024), "weighted_apl"
        ].iloc[0]
    )

    trends["direction"] = trends["absolute_change"].map(
        lambda value: (
            "Increase" if value > 0
            else "Decrease" if value < 0
            else "No change"
        )
    )

    fig = px.scatter(
        trends,
        x="apl_2024",
        y="relative_change_pct",
        color="direction",
        symbol="direction",
        color_discrete_map={
            "Increase": "#2E86C1",
            "Decrease": "#E69F00",
            "No change": "#808080",
        },
        symbol_map={
            "Increase": "circle",
            "Decrease": "triangle-down",
            "No change": "square",
        },
        hover_name="department_name",
        hover_data={
            "department_code": True,
            "apl_2024": ":.3f",
            "apl_2023": ":.3f",
            "relative_change_pct": ":+.2f",
            "absolute_change": ":+.3f",
            "direction": False,
        },
        labels={
            "apl_2024": "2024 potential access (APL)",
            "apl_2023": "2023 potential access (APL)",
            "relative_change_pct": "Change from 2023 to 2024 (%)",
            "absolute_change": "Absolute APL change",
            "department_code": "Department code",
            "direction": "Change direction",
        },
        title=(
            "Access levels and recent changes"
            "<br><sup>One point per selected department · "
            "GPs aged 65 or younger · Source: DREES</sup>"
        ),
        height=500,
    )

    fig.update_traces(
        marker={
            "size": 11,
            "opacity": 0.8,
            "line": {"width": 0.6, "color": "white"},
        }
    )

    lower = min(float(trends["relative_change_pct"].min()), 0)
    upper = max(float(trends["relative_change_pct"].max()), 0)
    padding = max(upper - lower, 1) * 0.12

    fig.update_yaxes(range=[lower - padding, upper + padding])
    fig.update_xaxes(
        range=[0, max(national_apl, trends["apl_2024"].max()) * 1.15]
    )

    fig.add_hline(
        y=0,
        line_dash="dash",
        line_color="#808080",
    )
    fig.add_vline(
        x=national_apl,
        line_dash="dash",
        line_color="#808080",
        annotation_text=f"National APL: {national_apl:.2f}",
        annotation_position="top right",
    )

    st.plotly_chart(
        fig,
        width="stretch",
        theme="streamlit",
        key="department_trends",
        config={"displaylogo": False, "scrollZoom": False},
        alt=(
            "Scatter plot comparing departmental APL in 2024 with "
            "its percentage change since 2023. Reference lines mark "
            "the national APL and zero change."
        ),
    )

    st.caption(
        "Lower-left: below the national APL benchmark and declining. "
        "Colours and symbols distinguish increases from decreases."
    )

    declining = int(trends["absolute_change"].lt(0).sum())
    increasing = int(trends["absolute_change"].gt(0).sum())

    st.write(
        f"**{declining} of {len(trends)} selected departments** "
        f"recorded a decrease; **{increasing}** recorded an increase."
    )

    both_conditions = trends.loc[
        trends["apl_2024"].lt(national_apl)
        & trends["absolute_change"].lt(0)
    ]

    departments = view["departments"]
    residents = departments.loc[
        departments["department_code"].isin(
            both_conditions["department_code"]
        ),
        "total_population",
    ].sum()
    selected_population = departments["total_population"].sum()
    share = 100 * residents / selected_population

    st.write(
        f"**{len(both_conditions)} departments** combine below-national "
        f"APL in 2024 with a decline since 2023. "
        f"**{residents:,.0f} residents** live in these departments "
        f"(**{share:.1f}%** of the selected population, reference year 2022)."
    )

    st.caption(
        "Department averages can hide local differences. "
        "These resident counts do not mean every individual has low access. "
        "Comparisons use each year's full dataset and population weights; "
        "they do not establish the causes of change."
    )
