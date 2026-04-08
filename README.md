# Bedfordshire Crime Data Repository

A curated collection of UK police crime data for Bedfordshire, covering **May 2021 through April 2024** — 36 months of monthly snapshots across three data categories.

## Data Source

All data is sourced from the [UK Police Data API](https://data.police.uk/docs/) (`data.police.uk`) and stored in monthly CSV files, organised by year and month.

## What's Included

Each monthly folder contains three CSV file types:

| File Type | Description |
|-----------|-------------|
| `*-street.csv` | Street-level crime records (location, crime type, outcome) |
| `*-stop-and-search.csv` | Stop-and-search records (demographics, object, outcome) |
| `*-outcomes.csv` | Crime outcome data (investigation status, justice process) |

### Coverage

- **Force**: Bedfordshire Police
- **Time period**: 2021-05 to 2024-04 (36 months)
- **Geography**: Bedfordshire (Bedford, Central Bedfordshire, Luton)
- **LSOA level**: Lower-layer Super Output Area codes and names included

### Dataset Size

Approximately **~35MB per month** across the three CSV types, totalling around **1.2GB** of structured crime data.

## Project Structure

```
data/
├── data/
│   ├── 2021-05/
│   │   ├── 2021-05-bedfordshire-outcomes.csv
│   │   ├── 2021-05-bedfordshire-stop-and-search.csv
│   │   └── 2021-05-bedfordshire-street.csv
│   ├── 2021-06/
│   └── ...
│   └── 2024-04/
└── streamlit_app.py       # Interactive Streamlit dashboard
```

## Streamlit Dashboard

`streamlit_app.py` is a ready-to-run Streamlit app for visualising the data:

```bash
pip install pandas streamlit plotly matplotlib seaborn
streamlit run streamlit_app.py
```

Features:
- Monthly data aggregation across all 36 months
- Filtering by date range, crime type, and LSOA
- Interactive charts via Plotly
- Crime heatmaps and trend analysis

## Potential Use Cases

- **Machine learning** — crime trend prediction, anomaly detection
- **Public safety research** — spatial analysis of crime hotspots
- **Policy analysis** — outcome and justice process studies
- **Journalism** — data-driven reporting on UK policing
- **Dashboarding** — real-time BI dashboards with Streamlit, Tableau, or Power BI
- **Academic projects** — geospatial analysis, time-series forecasting

## Key Columns

### Street Crimes
`Reported by`, `Longitude`, `Latitude`, `Location`, `LSOA code`, `LSOA name`, `Crime type`, `Last outcome category`

### Stop and Search
`Age range`, `Gender`, `Officer defined ethnicity`, `Object of search`, `Outcome`, `Part of a policing operation`

### Outcomes
`Category`, `Date`, `Criminal justice outcome`, `Location`, `LSOA`

## License

MIT License — [github.com/JonasAmidu](https://github.com/JonasAmidu)
