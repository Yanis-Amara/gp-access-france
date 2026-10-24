import streamlit as st


def weighted_apl(data):
    weights = data["standardised_population"]
    total_weight = weights.sum()
    if total_weight <= 0:
        return None
    return (data["apl_65_or_younger"] * weights).sum() / total_weight


def render_metrics(view):
    data = view["communes"]
    current = data.loc[data["apl_year"].eq(2024)]
    previous = data.loc[data["apl_year"].eq(2023)]

    current_apl = weighted_apl(current)
    previous_apl = weighted_apl(previous)

    delta = None
    if current_apl is not None and previous_apl is not None and previous_apl > 0:
        change_pct = 100 * (current_apl / previous_apl - 1)
        rounded_change = round(change_pct, 2)
        delta = 0 if rounded_change == 0 else f"{rounded_change:+.2f}%"

    population = current["total_population"].sum()
    population_display = (
        f"{population / 1_000_000:.2f}M"
        if population >= 1_000_000
        else f"{population:,.0f}"
    )

    department_count = len(view["departments"])
    declining_count = int(view["trends"]["absolute_change"].lt(0).sum())

    st.subheader("Access in your selected territories")
    st.caption(f"{view['area']} · 2024 indicators, compared with 2023")

    cards = st.columns(4)

    cards[0].metric(
        "2024 potential access",
        f"{current_apl:.2f}" if current_apl is not None else None,
        delta=delta,
        delta_description="vs 2023",
        help="Annual accessible consultations per age-standardised inhabitant.",
        border=True,
    )
    cards[1].metric(
        "Residents (2022)",
        population_display,
        help=f"{population:,.0f} residents. M means million.",
        border=True,
    )
    cards[2].metric(
        "Departments",
        str(department_count),
        border=True,
    )
    cards[3].metric(
        "Declining departments",
        f"{declining_count} / {department_count}",
        help="Selected departments with any negative APL change from 2023 to 2024.",
        border=True,
    )
