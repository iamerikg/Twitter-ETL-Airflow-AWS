from datetime import timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from datetime import datetime
from twitter_etl import run_twitter_etl

# Define default arguments
DEFAULT_ARGS = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2020, 11, 8),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

# Define the DAG
with DAG(
    'twitter_dag',
    default_args=DEFAULT_ARGS,
    description='Our first DAG with ETL process!',
    schedule_interval=timedelta(days=1),
) as dag:

    # Define the ETL task
    run_twitter_etl_task = PythonOperator(
        task_id='run_twitter_etl_task',
        python_callable=run_twitter_etl,
    )

# Set task dependencies
run_twitter_etl_task
