import pandas as pd
import sqlite3

DB_PATH = "database.db"
CSV_PATH = "data/DZ_user_actions.csv"

df = pd.read_csv(CSV_PATH)

# проверка типов
df["timestamp"] = pd.to_datetime(df["timestamp"])

conn = sqlite3.connect(DB_PATH)

df.to_sql("user_actions", conn, if_exists="replace", index=False)

conn.close()

print("Data loaded into SQLite")