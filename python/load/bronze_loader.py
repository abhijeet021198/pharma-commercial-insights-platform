import sys
from pathlib import Path

project_root = Path(__file__).resolve().parents[2]
sys.path.append(str(project_root / "python"))

import pandas as pd

from snowflake.connector.pandas_tools import write_pandas

from utils.snowflake_connection import (
    get_snowflake_connection
)


def load_accounts():

    print("Reading accounts.csv...")

    df = pd.read_csv("data/accounts.csv")

    df.columns = [col.upper() for col in df.columns]

    print(df.columns.tolist())

    conn = get_snowflake_connection()
    
    print("Connected to Snowflake")

    cursor = conn.cursor()

    try:

        print("Creating ACCOUNTS table...")

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS ACCOUNTS (
            ACCOUNT_ID VARCHAR,
            ACCOUNT_NAME VARCHAR,
            ACCOUNT_TYPE VARCHAR,
            CITY VARCHAR,
            STATE VARCHAR,
            REGION VARCHAR
        )
        """)

        print("Loading data into Snowflake...")

        success, nchunks, nrows, _ = write_pandas(
            conn,
            df,
            "ACCOUNTS"
        )

        print(f"Rows Loaded: {nrows}")

        cursor.execute("""
        SELECT COUNT(*)
        FROM ACCOUNTS
        """)

        row_count = cursor.fetchone()[0]

        print(f"Snowflake Row Count: {row_count}")

        print("Accounts load completed successfully")

    finally:

        cursor.close()
        conn.close()


if __name__ == "__main__":
    load_accounts()