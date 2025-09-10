# ⚡ RTE Energy Production Analysis

## 📌 Project Overview

This project analyzes energy production in France using the RTE (Réseau de Transport d'Électricité) API. The pipeline extracts data on actual generation, actual generation per unit, installed generation capacities, and unavailability additional information. API calls are orchestrated with Apache Airflow according to recommended intervals, and all results are stored in a SQLite database for further analysis. Data analysis and visualization will be performed using Streamlit.

---

## 🛠 Tech Stack

- **Data Orchestration:** Apache Airflow (DAGs to schedule API calls)
- **Database:** SQLite (`energy_analysis.db`)
- **APIs:** RTE Open Data APIs (actual generation, actual generation per unit, installed capacities, unavailability info)
- **Programming Language:** Python (`requests`, `pandas`, `sqlite3`)
- **Containerization:** Docker & Docker Compose (Airflow + DB)
- **Visualization & Analysis:** Streamlit

---

## 📂 Project Architecture

```text
pipelines/
│── extraction/
│   ├── api_connector.py
│   ├── exctract_generation_forecast.py
│   ├── extract_generation_forecast.py
│   ├── extract_installed_capacity.py
│   ├── extract_unavailability_info.py
│── transform.py
│── load.py
main.py                # Orchestration (Airflow DAGs)
data/
│   └── energy_analysis.db
Viz/
│   └── dashboard.py   # Streamlit app
Dockerfile
requirements.txt
README.md
```

---

## ⚙️ Pipeline Workflow

### Extraction

- Airflow triggers API calls to fetch:
  - Actual generation
  - Actual generation per unit
  - Installed generation capacities
  - Unavailability additional information
- API calls are scheduled according to RTE documentation recommendations.

### Transformation

- Data is cleaned and standardized using pandas.

### Loading

- All processed data is stored in a local SQLite database (`energy_analysis.db`).

### Analysis

- SQL queries and visualizations are used to analyze energy production patterns, capacity trends, and unavailability events using Streamlit.

---

## API Information

### Actual Generation API
**Provides real-time and historical data on total electricity generation in France.**
- From this API we will fetch data about generation per production type, per unit type, water reserve, and mix 15 time scale.

#### Actual Generation API Value Translation Table

| English API Value                | French Translation                           |
|----------------------------------|----------------------------------------------|
| AC_LINK                          | Ligne alternative                            |
| APPLICATION_DATE                 | Date d'application                           |
| Belgium                          | Belgique                                     |
| BIOMASS                          | Biomasse                                     |
| CANCELLED                        | Annulée                                      |
| DC_LINK                          | Ligne continue                               |
| England                          | Angleterre                                   |
| FINISHED                         | Terminée                                     |
| FORCED_UNAVAILABILITY            | Indisponibilité fortuites                    |
| FOSSIL_GAS                       | Gaz issu du charbon                          |
| FOSSIL_HARD_COAL                 | Charbon                                      |
| FOSSIL_OIL                       | Fioul                                        |
| France                           | France                                       |
| GENERATION_UNIT                  | Groupe de production                         |
| Germany                          | Allemagne                                    |
| HYDRO_PUMPED_STORAGE             | Hydraulique step                             |
| HYDRO_RUN_OF_RIVER_AND_POUNDAGE  | Hydraulique file de l'eau éclusée            |
| HYDRO_WATER_RESERVOIR            | Hydraulique lacs                             |
| Italy                            | Italie                                       |
| NUCLEAR                          | Nucléaire                                    |
| PLANNED_MAINTENANCE              | Indisponibilité planifiée                    |
| PRODUCTION_UNIT                  | Centrale de production                       |
| SOLAR                            | Solaire                                      |
| Spain                            | Espagne                                      |
| SUBSTATION                       | Sous-station                                 |
| Switzerland                      | Suisse                                       |
| TRANSFORMER                      | Transformateur                               |
| UPDATED_DATE                     | Date de modification                         |
| WASTE                            | Déchets industriels                          |
| WIND_OFFSHORE                    | Eolien offshore                              |
| WINF_ONSHORE                     | Eolien terrestre                             |

### Actual Generation Per Unit API
Returns generation data broken down by production unit or technology.

### Installed Generation Capacities API
Delivers information about installed capacities for each energy source.

### Unavailability Additional Information API
Reports on outages, maintenance, and other events affecting energy production units.

Refer to the RTE Open Data API documentation for endpoint details, authentication, and recommended call intervals.

---

## Data Extraction and Loading Logic

The data pipeline follows a multi-stage approach to ensure data integrity and flexibility for downstream analysis:

1. **Extraction to Bronze Layer (Semi-Structured JSON):**
   - All raw data is first extracted from the RTE APIs and saved as JSON files (semi-structured format). This forms the "bronze" layer, preserving the original structure and details of the API responses for traceability and reprocessing if needed.

2. **Transformation to Silver Layer (Structured CSV, Still Bronze):**
   - The JSON files from the bronze layer are then parsed and transformed into structured CSV files. These CSV files are still considered part of the bronze layer, as they represent semi-processed data that is not yet fully integrated into the analytics system. This step standardizes the data, making it easier to analyze and load into relational databases.

3. **Loading into Database (Gold Layer):**
   - The structured CSV files (bronze) are loaded into the SQLite database. Once the data is in the database, it is considered to be in the "gold" layer. This final step enables efficient querying, aggregation, and integration with visualization tools like Streamlit.

This multi-layer approach (Bronze → Gold) ensures that raw and semi-processed data is always available for reprocessing, while also providing clean, structured data for analytics and reporting.

---

## API Calls Recommendation

- **Actual Generation Per production type:** One call per hour for 155 days interval. First date: 15/12/2014. The API response is saved as a JSON file for each call.

- **Actual Generation Per Unit:** One call per hour with an interval of 7 days. First data: 13/12/2011. The API response is saved as a JSON file for each call.

- **Water Reserve:** One call per week on Wednesday and 1 year call. The API response is saved as a JSON file for each call.

- **mix_15_min_time_scale:** Interval of 14 days. The API response is saved as a JSON file for each call.

All API responses are stored as JSON files for further processing and analysis.

---



