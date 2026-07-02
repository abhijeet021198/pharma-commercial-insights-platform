from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator
from airflow.utils.task_group import TaskGroup
from airflow.providers.standard.operators.empty import EmptyOperator
from datetime import datetime, timedelta
from pathlib import Path
from airflow.models import Variable
from airflow.utils.email import send_email

PROJECT_ROOT = Variable.get(
    "PROJECT_ROOT",
    default_var=str(Path(__file__).resolve().parents[2]),
)

DBT_PROJECT = Path(PROJECT_ROOT) / "dbt" / "pharma_dbt"


def create_extract_task(task_name):

    return BashOperator(
        task_id=f"extract_{task_name}",
        bash_command=(
            f"cd {PROJECT_ROOT} && "
            f"python python/main.py extract_{task_name}"
        ),
        execution_timeout=timedelta(minutes=10),
    )

def create_dbt_task(command):

    return BashOperator(
        task_id=f"dbt_{command}",
        bash_command=(
            f"cd {DBT_PROJECT} && "
            f"dbt {command}"
        ),
        execution_timeout=timedelta(minutes=10),
    )

def notify_failure(context):
    """
    Global failure callback for the DAG.
    Currently prints failure details.
    Can later be extended to Email, Slack, or MS Teams.
    """

    task_id = context["task_instance"].task_id
    dag_id = context["dag"].dag_id
    execution_date = context["logical_date"]

    print("=" * 60)
    print("PIPELINE FAILURE")
    print(f"DAG : {dag_id}")
    print(f"Task: {task_id}")
    print(f"Run : {execution_date}")
    print("=" * 60)

    # Future implementation
    # send_email(
    #     to=["data-team@company.com"],
    #     subject=f"Airflow Failure: {dag_id}",
    #     html_content=f"Task {task_id} failed.",
    # )

def notify_success(context):
    """
    Global success callback for the DAG.
    Currently prints success details.
    Can later be extended to Email, Slack, or MS Teams.
    """

    dag_id = context["dag"].dag_id
    execution_date = context["logical_date"]

    print("=" * 60)
    print("PIPELINE COMPLETED SUCCESSFULLY")
    print(f"DAG : {dag_id}")
    print(f"Run : {execution_date}")
    print("=" * 60)

    # Future implementation
    # send_email(
    #     to=["data-team@company.com"],
    #     subject=f"Airflow Success: {dag_id}",
    #     html_content="Pipeline completed successfully.",
    # )
    
# --------------------------------------------------
# Default Arguments
# --------------------------------------------------

default_args = {
    "owner": Variable.get("DAG_OWNER", default_var="data_engineering"),
    "depends_on_past": False,
    "retries": int(Variable.get("DAG_RETRIES", default_var=2)),
    "retry_delay": timedelta(
        minutes=int(Variable.get("RETRY_DELAY_MINUTES", default_var=5))
    ),
}

DAG_DOCUMENTATION = """
# Pharma Commercial Insights Pipeline

## Pipeline Flow

1. Extract source data
2. Load CSV files into Snowflake Bronze
3. Install dbt dependencies
4. Run dbt transformations
5. Execute dbt tests
6. Mark pipeline completion

## Technologies

- Airflow
- Python
- Snowflake
- dbt

## Owner

Data Engineering Team
"""

# --------------------------------------------------
# DAG Definition
# --------------------------------------------------

with DAG(
    dag_id="pharma_analytics_pipeline",
    description="Enterprise Pharma Commercial Insights Pipeline",
    doc_md=DAG_DOCUMENTATION,
    default_args=default_args,
    start_date=datetime(2026, 1, 1),
    schedule="@daily",
    catchup=False,
    on_failure_callback=notify_failure,
    on_success_callback=notify_success,
    tags=["pharma", "snowflake", "dbt"],
) as dag:

    # --------------------------------------------------
    # Extraction Tasks
    # --------------------------------------------------

    with TaskGroup(group_id="extract_data") as extract_group:

        extract_accounts_task = create_extract_task("accounts")

        extract_products_task = create_extract_task("products")

        extract_orders_task = create_extract_task("orders")

        extract_inventory_task = create_extract_task("inventory")

        extract_interactions_task = create_extract_task("interactions")

    # --------------------------------------------------
    # Bronze Load
    # --------------------------------------------------

    load_bronze_task = BashOperator(
        task_id="load_to_snowflake",
        bash_command=f"cd {PROJECT_ROOT} && python python/load/bronze_loader.py",
        trigger_rule="all_success",
        execution_timeout=timedelta(minutes=10),
    )

    # --------------------------------------------------
    # dbt Models
    # --------------------------------------------------

    dbt_deps_task = create_dbt_task("deps")

    dbt_run_task = create_dbt_task("run")

    dbt_test_task = create_dbt_task("test")

    pipeline_completed_task = EmptyOperator(
        task_id="pipeline_completed",
        trigger_rule="all_done",
    )

    # --------------------------------------------------
    # Pipeline
    # --------------------------------------------------

    extract_group >> load_bronze_task >> dbt_deps_task >> dbt_run_task >> dbt_test_task >> pipeline_completed_task