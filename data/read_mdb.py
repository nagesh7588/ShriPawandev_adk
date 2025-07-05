# read_mdb.py

import pyodbc
import pandas as pd
import os
import sys

def read_mdb_tables(mdb_path):
    if not os.path.exists(mdb_path):
        print(f"❌ MDB file not found at: {mdb_path}")
        sys.exit(1)

    conn_str = (
        r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};"
        f"DBQ={mdb_path};"
    )

    try:
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()

        # List table names
        tables = [row.table_name for row in cursor.tables(tableType='TABLE')]
        if not tables:
            print("⚠️ No tables found in the MDB file.")
            return

        print("📋 Tables found:", tables)

        output_dir = "data/csv_exports"
        os.makedirs(output_dir, exist_ok=True)

        for table in tables:
            df = pd.read_sql(f"SELECT * FROM [{table}]", conn)
            print(f"✅ Exporting {table}: {df.shape}")
            df.to_csv(os.path.join(output_dir, f"{table}.csv"), index=False)

        cursor.close()
        conn.close()
        print("🎉 All tables exported successfully!")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    mdb_file = os.path.abspath("avall.mdb")  # full path
    print(f"📂 Reading from: {mdb_file}")
    read_mdb_tables(mdb_file)
