## How to interpret APL

- Scope: France excluding Mayotte; GPs aged 65 or younger.
- APL measures potential access to consultations, home visits and
  teleconsultations, accounting for nearby supply, activity and population needs.
- Department and national averages use standardised population as weights:
  **weighted APL = sum(APL × standardised population) /
  sum(standardised population)**.
- Resident counts and population shares use actual population.
- Population references are 2022 for APL 2024 and 2021 for APL 2023.
- The map focus changes the displayed geography; sidebar filters determine
  the analytical selection.

## Data quality and limitations

- The prepared tables contain 34,890 geographical units in 2024 and
  34,954 in 2023, with no missing values or duplicate commune codes within a year.
- Zero APL values are retained. They do not establish an absence of all healthcare.
- Three zero-population observations in 2023 are retained and flagged;
  they contribute no weight to population-weighted averages.
- High APL values are retained. Excluding the five highest 2024 observations
  changes national APL from 3.258882 to 3.258369.
- Commune codes differ between years. Comparisons use each year's full dataset,
  rather than treating unmatched codes as lost or newly opened practices.
- APL does not directly measure appointment waiting times, acceptance of new
  patients, affordability or quality of care.
- Department averages can hide differences between communes.
  Below-national APL is not an official medical-desert classification.
- Changes are descriptive. They do not establish causes or predict retirements.
  Population standardisation does not fully account for changing healthcare
  needs caused by national population ageing between years.

## Teleconsultations and digital access

**Teleconsultations are included in the activity underlying APL.**
This workbook does not separate remote from in-person care or identify
platforms such as Doctolib. It cannot show how much remote care compensates
for geographical isolation or limited appointment availability.

A separate DREES study of adults in metropolitan France reports that, in 2024,
21% of residents in large urban centres used teleconsultation, compared with
around 10% in rural areas. Among teleconsultation users, 43% cited long waits
for an in-person appointment. The study covers GPs and specialists.

These findings suggest that remote care is relevant to access, but do not
support assuming that the most isolated residents use it most.

[Source: DREES, Études et Résultats 1366, February 2026](https://drees.solidarites-sante.gouv.fr/publications-communique-de-presse/etudes-et-resultats/260212-recours-aux-t%C3%A9l%C3%A9consultations).

## Policy context — checked 23 October 2026

The Ministry describes **Un médecin près de chez vous**, operating since
September 2025 in 153 priority territories, with voluntary participation
by doctors in its pilot implementation.
[Ministry programme description](https://sante.gouv.fr/grands-dossiers/un-meilleur-acces-aux-soins-pour-tous-sur-le-territoire/article/pacte-de-lutte-contre-les-deserts-medicaux-151-zones-prioritaires-identifiees).

The **France Santé** circular of 16 June 2026 sets out the network's deployment
and funding, with a target of 5,000 labelled structures by 2027.
This is a target, not a result established by this dashboard.
[Official circular](https://bulletins-officiels.social.gouv.fr/circulaire-interministerielle-ndeg-dgossdasas2dgclsdcatc3202686-du-16-juin-2026-relative-au-deploiement-et-au-financement-du-reseau-france-sante).

**The 2023–2024 observations predate these initiatives and cannot evaluate
their effectiveness.** Later data and a dedicated evaluation would be needed.

## Sources and licences

- [Main APL dataset: DREES, referenced on data.gouv.fr](https://www.data.gouv.fr/datasets/accessibilite-potentielle-localisee-apl-aux-professionnels-de-sante)
  — Open Licence 2.0.
- [DREES publication on access in 2024](https://drees.solidarites-sante.gouv.fr/communique-de-presse-jeux-de-donnees/jeux-de-donnees/260722-accessibilite-aux-soins-de-premier-recours-en-2024).
- [Department boundaries: Etalab/IGN, 2024 edition](https://www.data.gouv.fr/datasets/contours-administratifs)
  — ODbL.
- [Department names: French geographic API](https://geo.api.gouv.fr/departements).

Teleconsultation and policy references provide context; they are not
additional observations in the APL analysis.