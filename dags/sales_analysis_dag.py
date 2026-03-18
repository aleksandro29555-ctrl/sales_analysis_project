from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="sales_analysis_pipeline",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False,
    tags=["sales", "sqlite", "plotly"],
) as dag:

    load_data = BashOperator(
        task_id="load_to_sqlite",
        bash_command="cd /opt/airflow && python scripts/load_to_sqlite.py"
    )

    run_analysis = BashOperator(
        task_id="analyze_sales",
        bash_command="cd /opt/airflow && python scripts/analyze_sales.py"
    )

    log_success = BashOperator(
        task_id="log_success",
        bash_command='echo "DAG completed successfully: sales analysis files were created."'
    )

    load_data >> run_analysis >> log_success