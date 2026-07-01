from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime, timedelta


# --------------------------------------------------
# Placeholder Python Functions
# (Will be replaced by the real extraction framework)
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
# Default Arguments
# --------------------------------------------------

default_args = {
    "owner": "data_engineering",
    "retries": 2,
    "retry_delay": timedelta(minutes=5),
}


# --------------------------------------------------
# DAG Definition
# --------------------------------------------------

with DAG(
    dag_id="pharma_analytics_pipeline",
    description="Enterprise Pharma Commercial Insights Pipeline",
    default_args=default_args,
    start_date=datetime(2026, 1, 1),
    schedule="@daily",
    catchup=False,
    tags=["pharma", "snowflake", "dbt"],
) as dag:

    # --------------------------
    # Python Extraction Tasks
    # --------------------------

    extract_accounts_task = BashOperator(
        task_id="extract_accounts",
        bash_command="cd /home/abhijeet/projects/pharma-commercial-insights-platform && python python/main.py extract_accounts",
    )

    extract_products_task = BashOperator(
        task_id="extract_products",
        bash_command="cd /home/abhijeet/projects/pharma-commercial-insights-platform && python python/main.py extract_products",
    )

    extract_orders_task = BashOperator(
        task_id="extract_orders",
        bash_command="cd /home/abhijeet/projects/pharma-commercial-insights-platform && python python/main.py extract_orders",
    )

    extract_inventory_task = BashOperator(
        task_id="extract_inventory",
        bash_command="cd /home/abhijeet/projects/pharma-commercial-insights-platform && python python/main.py extract_inventory",
    )

    extract_interactions_task = BashOperator(
        task_id="extract_interactions",
        bash_command="cd /home/abhijeet/projects/pharma-commercial-insights-platform && python python/main.py extract_interactions",
    )

    # --------------------------
    # Bronze Load
    # --------------------------

    load_bronze_task = BashOperator(
        task_id="load_to_snowflake",
        bash_command="cd /home/abhijeet/projects/pharma-commercial-insights-platform && python python/load/bronze_loader.py",
    )

    # --------------------------
    # dbt Bronze
    # --------------------------

    dbt_bronze_task = BashOperator(
        task_id="run_dbt_models",
        bash_command="cd /mnt/c/Repo/pharma-commercial-insights-platform/dbt/pharma_dbt && dbt run",
    )

    # --------------------------
    # Future BashOperator
    # (Temporary - validation only)
    # --------------------------

    # run_accounts_entrypoint = BashOperator(
    #     task_id="run_accounts_entrypoint",
    #     bash_command="python python/main.py extract_accounts",
    # )

    # --------------------------
    # Main Pipeline
    # --------------------------

    [
        extract_accounts_task,
        extract_products_task,
        extract_orders_task,
        extract_inventory_task,
        extract_interactions_task,
    ] >> load_bronze_task >> dbt_bronze_task

    # NOTE:
    # run_accounts_entrypoint is intentionally left independent.
    # We'll test it first before replacing the PythonOperator.