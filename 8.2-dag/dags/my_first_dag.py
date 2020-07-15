from airflow import DAG
from datetime import datetime, timedelta

default_arguments = {
    'owner': 'airflow',
    'start_date': datetime(2019, 5, 15, 0, 0, 0),
    'retries': 3,
    'retry_delay': timedelta(minutes=10)
}

dag = DAG(dag_id='my_first_dag',
          max_active_runs=5,
          schedule_interval='0 * * * *',
          default_args=default_arguments,
          catchup=False)
