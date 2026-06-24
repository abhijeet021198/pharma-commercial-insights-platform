import sys
from pathlib import Path

project_root = Path(__file__).resolve().parents[2]
sys.path.append(str(project_root / "python"))

import pandas as pd
from snowflake.connector.pandas_tools import write_pandas

from utils.snowflake_connection import get_snowflake_connection

from load.table_definitions import (
    ACCOUNTS_DDL,
    PRODUCTS_DDL,
    ORDERS_DDL,
    INVENTORY_DDL,
    INTERACTIONS_DDL,
    SALES_REP_DDL
)


def load_csv_to_table(file_path, table_name, ddl):

    print(f"\nLoading {table_name}...")

    df = pd.read_csv(file_path)

    df.columns = [col.upper() for col in df.columns]

    conn = get_snowflake_connection()

    cursor = conn.cursor()

    try:

        cursor.execute(ddl)

        cursor.execute(
            f"TRUNCATE TABLE {table_name}"
            )

        success, nchunks, nrows, _ = write_pandas(
            conn,
            df,
            table_name
        )

        cursor.execute(
            f"SELECT COUNT(*) FROM {table_name}"
        )

        row_count = cursor.fetchone()[0]

        print(f"Rows Loaded: {nrows}")
        print(f"Snowflake Row Count: {row_count}")

    finally:

        cursor.close()
        conn.close()


if __name__ == "__main__":

    load_csv_to_table(
        "data/accounts.csv",
        "ACCOUNTS",
        ACCOUNTS_DDL
    )

    load_csv_to_table(
        "data/products.csv",
        "PRODUCTS",
        PRODUCTS_DDL
)
    
    load_csv_to_table(
    "data/orders.csv",
    "ORDERS",
    ORDERS_DDL
)

load_csv_to_table(
    "data/inventory.csv",
    "INVENTORY",
    INVENTORY_DDL
)

load_csv_to_table(
    "data/interactions.csv",
    "INTERACTIONS",
    INTERACTIONS_DDL
)

load_csv_to_table(
    "data/sales_rep.csv",
    "SALES_REP",
    SALES_REP_DDL
)