import sqlite3
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

DB_PATH = BASE_DIR / "predictionsDB.db"

print("Database exists:", DB_PATH.exists())

# Connect to database
conn = sqlite3.connect(DB_PATH)

# Display predictions table
df = pd.read_sql_query(
    "SELECT * FROM predictions",
    conn
)

print("\nPrediction Records:")
print(df.to_string(index=False))

conn.close()