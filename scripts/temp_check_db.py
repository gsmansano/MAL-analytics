import duckdb

con = duckdb.connect(database='data/mal_data.duckdb')
result = con.execute("SELECT count(*) FROM raw_anime_2026_03_02;").fetchone()

print(f"Total rows in table: {result[0]}")
con.close()