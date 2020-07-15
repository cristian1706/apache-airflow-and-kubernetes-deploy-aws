from airflow.plugins_manager import AirflowPlugin
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults
from airflow.operators.sensors import BaseSensorOperator
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


class MyFirstPlugin(AirflowPlugin):
    name = 'my_first_plugin'
    operators = [MyFirstOperator, MyFirstSensor]
    hooks = []
