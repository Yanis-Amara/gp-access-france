# Storyboard — Access to General Practitioners in France

**Author:** Yanis AMARA  
**Student number / group:** 20232166 / DE2  
**Course:** Data Analysis & Visualization  
**Professor:** Dr. Mano MATHEW

## Purpose and audience

Help municipalities, healthcare centres and regional health authorities
identify geographical differences in potential GP access and decide where
further local investigation is needed.

## Motivation

I chose this topic because of my upcoming healthcare research internship
and my interest in territorial inequalities in access to care.

## Main question

How does potential access to general practitioners vary across France,
and where did it decline between 2023 and 2024?

## Opening hook

A national average can hide local gaps. In 2024, national potential access
was 3.26 annual consultations per age-standardised inhabitant, but access
varied substantially between and within departments.

## Story sequence

The figures below describe the national selection, excluding Mayotte.
Displayed results change when the user filters the dashboard.

| Stage | User question | Evidence and visual | Interaction | Intended takeaway |
|---|---|---|---|---|
| Overview | What is the overall situation? | Four KPI cards: APL, residents, department count and declining departments. | Select an area or departments in the sidebar. | National APL fell by 1.09%; 79 of 100 departments recorded a decrease. |
| Compare departments | Where is potential access lowest or highest? | Horizontal ranking with a national reference line. | Switch between lowest and highest APL; inspect hover details. | Guyane has the lowest departmental APL, around 1.41 compared with 3.26 nationally. |
| Explore geography | How are differences distributed geographically? | Department choropleth with a fixed national colour scale. | Change map focus between metropolitan France and overseas departments. | Geographical comparisons should include overseas territories and use a consistent scale. |
| Look within a department | What does the department average hide? | Population-weighted histogram and zero-APL indicators. | Select a department and hover over the distribution. | In Guyane, 16.3% of residents live in communes with zero APL for GPs aged 65 or younger. |
| Examine change | Which departments combine lower access with decline? | Scatter plot of 2024 APL against percentage change since 2023. | Hover over points and filter territories. | Fifty departments meet both conditions, containing 38.1% of the covered population. |
| Interpret and act | What should decision-makers investigate next? | Recommendations and expandable methods, limitations and policy context. | Open the relevant explanatory sections. | Investigate local appointment availability, staffing, transport and digital access before choosing interventions. |

## Interpretation safeguards

- APL measures potential access, not actual appointment waiting times.
- Weighted APL uses standardised population; resident shares use actual population.
- The national average is a benchmark, not an official shortage threshold.
- Zero APL does not establish an absence of all healthcare.
- Residents of a qualifying department do not all experience the same access.
- The population reference is 2022 for APL 2024 and 2021 for APL 2023.
- Teleconsultations are included in APL activity, but their separate contribution
  and platform effects cannot be measured from this workbook.
- The 2023-2024 observations cannot evaluate initiatives introduced later.
- Changes describe associations and trends; they do not establish causes.

## Planned demo — approximately 2 minutes 45 seconds

| Time | What to show | What to explain |
|---|---|---|
| 00:00–00:20 | Title and national overview. | Motivation, audience and the question behind the dashboard. |
| 00:20–00:45 | National KPI cards. | Meaning of APL, population reference and the 1.09% decline. |
| 00:45–01:15 | Ranking and map; switch to Guyane. | Department differences and the importance of including overseas territories. |
| 01:15–01:45 | Guyane distribution. | Why an average can conceal local gaps; explain the 16.3% figure carefully. |
| 01:45–02:15 | Return to national selection and show the scatter plot. | Explain the lower-left quadrant, 50 departments and the 38.1% population share. |
| 02:15–02:45 | Conclusions and limitations. | Suggest local investigation; clarify teleconsultations and the timing of policy initiatives. |

## Closing message

Use national comparisons to locate potential pressure, then examine local
differences before deciding what action is appropriate.
