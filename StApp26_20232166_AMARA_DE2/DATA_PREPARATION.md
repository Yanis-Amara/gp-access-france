# Data preparation decisions

- Source: DREES Localised Potential Accessibility (APL).
- Scope: France excluding Mayotte, 2023 and 2024.
- Main indicator: access to GPs aged 65 or younger.
- Population reference years: 2021 for APL 2023; 2022 for APL 2024.
- Preserve commune codes as strings when loading CSV files.
- Retain zero APL values.
- Retain and flag the three zero-population observations in 2023.
  Their zero standardised weights contribute nothing to weighted averages.
- Retain high APL values. Excluding the five highest values changes
  national APL from 3.258882 to 3.258369.
- Use standardised population to aggregate APL.
- Use resident population for population counts and shares.
- Aggregate all observations for national and departmental comparisons.
  Do not interpret unmatched commune codes as changes in GP supply.
- Missing first-year changes in the national table indicate the baseline.
- The national benchmark is not an official shortage threshold.
