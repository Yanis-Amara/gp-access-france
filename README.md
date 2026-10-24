# Access to General Practitioners in France

A Streamlit dashboard exploring geographical differences in potential access
to general practitioners in 2024 and changes since 2023.

This project is motivated by my upcoming healthcare research internship
and an interest in territorial inequalities in access to care.

## Author

- **Name:** Yanis AMARA
- **Student number / group:** 20232166 / DE2
- **Institution:** EFREI
- **Programme:** DATA ENGINEERING
- **Academic year:** 2026-2027
- **Course:** Data Analysis & Visualization
- **Professor:** Dr. Mano MATHEW
- **Email:** Yanis.amara@efrei.net
- **LinkedIn:** https://www.linkedin.com/in/yanis-amara-3a3953292/

## Audience and questions

The dashboard is intended for municipalities, healthcare centres and
regional health authorities.

**Main question:** How does potential access to GPs vary across France?

1. Which departments have the lowest or highest potential access in 2024?
2. What differences are hidden within department averages?
3. Where did potential access decline between 2023 and 2024?

## Main findings

These figures refer to the complete national selection, excluding Mayotte.

- Population-weighted APL decreased from **3.295 in 2023 to 3.259 in 2024**,
  a change of **-1.09%**.
- **79 of 100 departments** recorded a decrease.
- **50 departments** combined below-national APL in 2024 with a decline.
  They contained **25,788,500 residents**, or **38.1%** of the covered
  population, using the 2022 population reference.
- In Guyane, **12 of 22 communes** had zero APL for GPs aged 65 or younger.
  These communes contained **47,077 residents**, or **16.3%** of the
  department population.

Living in a qualifying department does not mean that every resident
experiences low access. Zero APL does not establish an absence of all healthcare.

## Dashboard walkthrough

1. **Overview:** KPIs respond to the sidebar area and department filters.
2. **Compare departments:** switch between the lowest and highest APL rankings.
3. **Explore geography:** inspect the map, including overseas departments.
4. **Look within a department:** explore the population-weighted distribution
   of commune-level access.
5. **Examine change:** compare 2024 access with its percentage change since 2023.
6. **Interpret the evidence:** read recommendations, methods and limitations.

The map-focus control changes the displayed geography only.
Sidebar filters determine the analytical selection.
The map colour scale remains fixed across views.

## Data and methods

**Main source:** DREES Localised Potential Accessibility (APL), referenced on
[data.gouv.fr](https://www.data.gouv.fr/datasets/accessibilite-potentielle-localisee-apl-aux-professionnels-de-sante).

Scope: France excluding Mayotte; GPs aged 65 or younger.
APL describes annual accessible consultations, home visits and teleconsultations
per age-standardised inhabitant.

- National and department APL averages use **standardised population weights**.
- Resident counts and population shares use **actual population**.
- APL 2024 uses the **2022 population reference**; APL 2023 uses **2021**.
- Each year is aggregated using its complete set of observations.
- The national average is a comparison benchmark, not an official
  medical-desert threshold.

Detailed preparation and interpretation:
[DATA_PREPARATION.md](DATA_PREPARATION.md) and
[CONTEXT_AND_LIMITATIONS.md](CONTEXT_AND_LIMITATIONS.md).

Source URLs, licences and SHA-256 fingerprints are recorded in
[data_sources.json](data_sources.json).

## Run locally

Run the following commands from the project directory.
The Colab development environment used **Python 3.13.16**.

### Windows PowerShell

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe download_data.py
.\.venv\Scripts\python.exe -m streamlit run app.py
```

### macOS / Linux

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python download_data.py
.venv/bin/python -m streamlit run app.py
```

The application reads the included processed CSV snapshots.
The downloader reuses verified source files and retrieves missing files.
If an online resource has changed since the recorded snapshot, verification
stops rather than silently substituting new data.

### Pinned dependencies

```text
streamlit==1.66.0
pandas==2.2.3
numpy==2.1.3
plotly==5.24.1
openpyxl==3.1.5
requests==2.32.4
```

## Project organisation

- `app.py`: application entry point.
- `data_and_filters.py`: cached loading and sidebar filters.
- `metrics.py`: weighted calculations and KPI cards.
- `ranking.py`, `map_view.py`, `local_view.py`, `trend_view.py`: interactive charts.
- `context_view.py`: recommendations and explanatory notes.
- `data/raw/`: original workbook.
- `data/processed/`: prepared tables and numerical audit.
- `assets/`: department boundaries, EFREI logo and context notes.
- `download_data.py`: cached source downloader with fingerprint verification.
- `requirements.txt`: pinned application dependencies.
- `project_metadata.json`: author details and submission links.

## Validation status

Streamlit AppTest passed four filter scenarios:

- France excluding Mayotte.
- Guyane.
- Metropolitan France.
- Seine-et-Marne selected through the department filter.

Checks cover expected KPIs, percentage changes, chart count,
department options and map focus.

All four filter scenarios passed in a fresh virtual environment. Desktop visual review passed for the four national charts and the Guyane filter.
AppTest execution checks alone do not establish visual correctness.

## Limits and context

APL measures potential access, not actual waiting times, acceptance of new
patients or quality of care. Department averages can conceal local disparities.

Teleconsultations are included in APL activity, but the workbook does not
separate their contribution or measure the effect of platforms such as Doctolib.

The 2023-2024 observations predate the later policy initiatives discussed
in the context notes and cannot establish their effectiveness.

## Licences and attribution

- DREES APL data: **Open Licence 2.0**.
- Department boundaries, Etalab/IGN: **ODbL**.
- EFREI logo: institutional branding, separate from the data licences.

The project uses aggregate territorial data and contains no patient-level data.

## Submission checklist

- [x] Streamlit application with four interactive charts and sidebar filters.
- [x] Source files, download script and source manifest.
- [x] Pinned requirements and local run instructions.
- [x] Include the completed notebook as `analysis.ipynb`.
- [x] Complete the clean-environment check.
- [x] Complete the desktop visual review.
- [x] Add [REPORT.pdf](REPORT.pdf).
- [x] Add [STORYBOARD.md](STORYBOARD.md).
- [x] Add the repository URL.
- [x] Add the validated deployment URL.
- [x] Record the 2-4 minute demo and add its link.
- [x] Create `StApp26_20232166_AMARA_DE2.zip`.

**App URL:** https://gp-access-france-ahs5sneep9sfvukvtlnrbx.streamlit.app/
**Repository URL:** https://github.com/Yanis-Amara/gp-access-france
**Demo video URL:** https://drive.google.com/file/d/14FoVSiHnxjcu0wHv8CMeZwwxg1eIT0k9/view

## Reproducing the validated environment

Use `requirements-lock.txt` instead of `requirements.txt` to install the complete dependency versions recorded during validation.

Run `python tests/check_app.py` inside the installed environment to repeat the functional checks. Results are saved in `VALIDATION.json`.
