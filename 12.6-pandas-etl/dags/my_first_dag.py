from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators import MyFirstOperator, MyFirstSensor


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

task1 = MyFirstOperator(task_id='task_id1', param='some random text', dag=dag)

task2 = MyFirstSensor(task_id='task_id2', poke_interval=30, dag=dag)

task2 >> task1

