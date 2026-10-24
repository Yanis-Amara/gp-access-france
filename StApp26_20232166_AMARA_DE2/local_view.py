import plotly.express as px
import streamlit as st

from metrics import weighted_apl


def render_local(view):
    st.subheader("3. Look beyond the department average")

    departments = view["departments"].sort_values("apl_65_or_younger")
    names = departments.set_index("department_code")["department_name"].to_dict()
    codes = departments["department_code"].tolist()

    selected_code = st.selectbox(
        "Department to explore",
        options=codes,
        format_func=lambda code: f"{names[code]} ({code})",
        key="local_department_" + "|".join(codes),
    )
    department_name = names[selected_code]

    communes = view["communes"]
    local = communes.loc[
        communes["apl_year"].eq(2024)
        & communes["department_code"].eq(selected_code)
    ].copy()

    department_apl = weighted_apl(local)
    national_apl = float(
        view["national"].loc[
            view["national"]["apl_year"].eq(2024), "weighted_apl"
        ].iloc[0]
    )

    population = local["total_population"].sum()
    zero_apl = local["apl_65_or_younger"].eq(0)
    zero_population = local.loc[zero_apl, "total_population"].sum()

    below_national = local["apl_65_or_younger"].lt(national_apl)
    below_population = local.loc[
        below_national, "total_population"
    ].sum()

    fig = px.histogram(
        local,
        x="apl_65_or_younger",
        y="total_population",
        histfunc="sum",
        histnorm="percent",
        nbins=15,
        color_discrete_sequence=["#2E86C1"],
        title=(
            f"Where residents fall on the access spectrum: {department_name}"
            "<br><sup>2024 APL · Population reference: 2022 · "
            "GPs aged 65 or younger</sup>"
        ),
        height=430,
    )

    fig.update_traces(
        marker_line_width=0.5,
        marker_line_color="white",
        hovertemplate=(
            "APL bin: %{x}<br>"
            "Share of department residents: %{y:.1f}%"
            "<extra></extra>"
        ),
    )
    fig.update_layout(
        bargap=0.05,
        xaxis_title=(
            "Annual accessible consultations per age-standardised inhabitant"
        ),
        yaxis_title="Share of department residents (%)",
    )
    fig.update_xaxes(rangemode="tozero")
    fig.update_yaxes(rangemode="tozero")

    fig.add_vline(
        x=department_apl,
        line_dash="dash",
        line_color="#808080",
        annotation_text=f"Department average: {department_apl:.2f}",
        annotation_position="top right",
    )

    st.plotly_chart(
        fig,
        width="stretch",
        theme="streamlit",
        key="local_distribution",
        config={"displaylogo": False, "scrollZoom": False},
        alt=(
            f"Population-weighted distribution of commune-level APL "
            f"in {department_name}, with the department average marked."
        ),
    )

    st.caption(
        "Each bar groups geographical units with similar APL. "
        "Its height represents their share of department residents."
    )

    st.write(
        f"**{int(zero_apl.sum())} of {len(local)} geographical units** "
        f"have zero APL for GPs aged 65 or younger, covering "
        f"**{zero_population:,.0f} residents "
        f"({100 * zero_population / population:.1f}%)**."
    )
    st.write(
        f"**{100 * below_population / population:.1f}% of residents** "
        f"live in geographical units below the national APL benchmark "
        f"of **{national_apl:.2f}**."
    )
    st.caption(
        "Zero APL does not establish an absence of all healthcare. "
        "The national average is a comparison benchmark, "
        "not an official shortage threshold."
    )
