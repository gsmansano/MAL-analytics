# The Otaku Engine: Analytics Edition 🎌

## Context
This repository is the dedicated **Data & Analytics Engineering** core of the Otaku Data Engine project. While the wider project handles full-stack features, this version focuses strictly on the **Modern Data Stack (MDS)**—moving data from raw API responses to high-value analytical insights.

The goal is to analyze the "Top 2500" anime from MyAnimeList to uncover trends in studio performance, genre evolution, and rating gaps over the last decade.

---

## 🛠️ The Tech Stack
* **Database:** [DuckDB](https://duckdb.org/) (In-process OLAP database for lightning-fast local analytics).
* **Transformation:** [dbt-core](https://www.getdbt.com/) (Data Build Tool) for modular SQL modeling.
* **Environment:** WSL2 (Ubuntu 24.04) + Python 3.12.
* **Source:** [Jikan API](https://jikan.moe/) (Unofficial MyAnimeList API).

---

## 🏗️ Data Architecture (Medallion)
I am implementing a **Medallion Architecture** to ensure data quality and scalability:

1.  **Bronze (Raw/Staging):** Direct ingestion of JSON responses into DuckDB tables with initial type casting.
2.  **Silver (Intermediate):** Cleaned and normalized data. This layer handles the "Many-to-Many" logic for Genres and Studios.
3.  **Gold (Mart):** Final business-ready tables optimized for visualization (e.g., "Top Performing Genres by Decade").

---
