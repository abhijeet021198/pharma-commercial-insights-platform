from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

# --------------------------------------------------
# Python Functions
# --------------------------------------------------

def extract_accounts():
    print("Extracting accounts data...")

def extract_products():
    print("Extracting products data...")

def extract_orders():
    print("Extracting orders data...")

def extract_interactions():
    print("Extracting interactions data...")

def extract_inventory():
    print("Extracting inventory data...")

def load_to_snowflake():
    print("Loading data into Snowflake BRONZE tables...")

def run_dbt_models():
    print("Running dbt transformations...")

# --------------------------------------------------
# DAG Definition
# --------------------------------------------------

with DAG(
    dag_id="pharma_analytics_pipeline",
    start_date=datetime(2026, 1, 1),
    schedule="@daily",
    catchup=False,
    tags=["pharma", "snowflake", "dbt"]
) as dag:

    accounts_task = PythonOperator(
        task_id="extract_accounts",
        python_callable=extract_accounts
    )

    products_task = PythonOperator(
        task_id="extract_products",
        python_callable=extract_products
    )

    orders_task = PythonOperator(
        task_id="extract_orders",
        python_callable=extract_orders
    )

    interactions_task = PythonOperator(
        task_id="extract_interactions",
        python_callable=extract_interactions
    )

    inventory_task = PythonOperator(
        task_id="extract_inventory",
        python_callable=extract_inventory
    )

    snowflake_task = PythonOperator(
        task_id="load_to_snowflake",
        python_callable=load_to_snowflake
    )

    dbt_task = PythonOperator(
        task_id="run_dbt_models",
        python_callable=run_dbt_models
    )

    [
        accounts_task,
        products_task,
        orders_task,
        interactions_task,
        inventory_task
    ] >> snowflake_task >> dbt_task
