import duckdb
from datetime import datetime

# IMPORTANT
# this var will change what date we will load the raws into ducktb
# during development I will pick just the first dataset.
# but this can create several versions of the dataset to keep track over time

# target_date = datetime.now().strftime("%Y-%m-%d")
target_date = '2026-03-02'

con = duckdb.connect(database='data/mal_data.duckdb')

# select all .json files created during the extraction phase
json_path = f"data/raw/{target_date}/*.json"

# query to create our raw_anime table
query = f"""
CREATE OR REPLACE TABLE raw_anime_{target_date.replace("-", "_")} AS
SELECT * FROM read_json_auto('{json_path}');
"""
try:
    con.execute(query)
    print(f"Successfully loaded dated from {target_date} into DuckDB")
except Exception as e:
    print(f"Error loading to DuckDB: {e}")
finally:
    con.close()
