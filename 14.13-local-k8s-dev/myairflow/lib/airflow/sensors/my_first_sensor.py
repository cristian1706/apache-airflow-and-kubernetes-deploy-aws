from airflow.operators.sensors import BaseSensorOperator
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
