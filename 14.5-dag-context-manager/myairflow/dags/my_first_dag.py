from airflow import DAG
from datetime import datetime, timedelta
from myairflow.lib.airflow.sensors.my_first_sensor import MyFirstSensor
from myairflow.lib.airflow.operators.my_first_operator import MyFirstOperator


default_arguments = {
    'owner': 'airflow',
    'start_date': datetime(2019, 5, 15, 0, 0, 0),
    'retries': 3,
    'retry_delay': timedelta(minutes=10)
}

with DAG(dag_id='my_first_dag',
         max_active_runs=5,
         schedule_interval='0 * * * *',
         default_args=default_arguments,
         catchup=False) as dag:

    task1 = MyFirstOperator(task_id='task_id1', param='some random text')

    task2 = MyFirstSensor(task_id='task_id2', poke_interval=30)

    task2 >> task1
