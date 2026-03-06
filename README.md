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

## 📊 Analytical Insights (The Four Pillars)
The engineering work in this repository enables a deep-dive analysis into the anime market through four distinct lenses:

1. **The Value Gap:** Identifying "Hidden Gems" by calculating the delta between a title's Quality Rank (Score) and its Popularity Rank.
2. **Historical Trends:** Analyzing the "Production Boom" (1990–2025) to see how the industry scaled volume without sacrificing average quality.
3. **Studio Performance:** Benchmarking the "Brand Power" of major studios vs. niche producers to see who effectively "owns" audience attention.
4. **The Loyalty Funnel:** Calculating conversion rates from casual "Members" to "Advocates" (Favorites) across different media formats.