from airflow.plugins_manager import AirflowPlugin


class MyFirstPlugin(AirflowPlugin):
    name = 'my_first_plugin'
