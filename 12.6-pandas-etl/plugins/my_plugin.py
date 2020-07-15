from airflow.plugins_manager import AirflowPlugin
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults
from airflow.operators.sensors import BaseSensorOperator
from airflow.hooks.postgres_hook import PostgresHook
import logging as log
from datetime import datetime


class MyFirstSensor(BaseSensorOperator):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def poke(self, context):
        current_minute = datetime.now().minute
        if current_minute % 2 != 0:
            return False
        task_instance = context['task_instance']
        task_instance.xcom_push('minute', current_minute)
        return True


class MyFirstOperator(BaseOperator):

    @apply_defaults
    def __init__(self, param, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.param = param

    def execute(self, context):
        task_instance = context['task_instance']
        minute = task_instance.xcom_pull('task_id2', key='minute')
        log.info(minute)
        log.info(self.param)


class PandasETLOverPostgresOperator(BaseOperator):

    @apply_defaults
    def __init__(self, connection_id, sql_query, etl_function, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.connection_id = connection_id
        self.sql_query = sql_query
        self.etl_function = etl_function

    def execute(self, context):
        log.info('Run Pandas over postgres')
        postgres_instance = PostgresHook(postgres_conn_id=self.connection_id)
        df = postgres_instance.get_pandas_df(self.sql_query)
        self.etl_function(df)


class MyFirstPlugin(AirflowPlugin):
    name = 'my_first_plugin'
    operators = [MyFirstOperator, MyFirstSensor, PandasETLOverPostgresOperator]
    hooks = []
