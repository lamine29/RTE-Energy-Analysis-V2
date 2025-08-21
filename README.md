# ⚡ RTE Energy Production and Consumption in France Analysis 

## 📌 Project Overview

This project analyzes energy production in France using multiple APIs provided by RTE (Réseau de Transport d'Électricité). The pipeline collects, processes, and stores production data and data consumption (nuclear, hydro, wind, solar, fossil fuels, etc.) to analyze trends and provide insights into the French energy .

**Main goals:**
- Automate data ingestion from RTE APIs.
- Orchestrate the workflow with Apache Airflow.
- Store processed data in a database (SQLite for local demo, AWS Data Warehouse for scaling).
- Provide queries and analysis for understanding production patterns.

---

## 🛠 Tech Stack

- **Data Orchestration:** Apache Airflow (DAGs to schedule API calls & transformations)
- **Database:**
  - Local: SQLite (`energy.db`) for quick prototyping
  - Cloud (optional): AWS Redshift / Athena for scalability
- **APIs:** RTE Open Data APIs (`/production` endpoints)
- **Containerization:** Docker & Docker Compose (Airflow + DB)
- **Programming Language:** Python (`requests`, `pandas`, `sqlite3`, `SQLAlchemy`)

---

## 📂 Project Architecture

```
energy_multi_api/
│── app/
│   ├── extract_generation.py
│   ├── extract_consumption.py
│   ├── extract_capacity.py
│   ├── transform.py
│   ├── load.py
│   ├── main.py          # Orchestration
│── data/
│   └── energy_analysis.db
│── viz/
│   └── dashboard.py     # Streamlit app
│── Dockerfile
│── docker-compose.yml   # Container orchestration (Airflow + DB)
│── requirements.txt
│── README.md

```

---

## ⚙️ Pipeline Workflow

**Extraction**
- Airflow triggers daily API calls to fetch production data.
- Multiple APIs are used (nuclear, wind, solar, hydro, fossil, etc.).

**Transformation**
- Data is cleaned with pandas (handling timestamps, missing values, and energy unit conversions).
- Production types are standardized into a single schema.

**Loading**
- Local Mode: Data is stored in SQLite (`energy.db`).
- Scalable Mode: Data is loaded into AWS Redshift for analytics & dashboards.

**Analysis**
- SQL queries provided to analyze:
  - Percentage contribution of each energy source
  - Daily/weekly production patterns
  - Historical trends in renewables vs. fossil fuels

---
