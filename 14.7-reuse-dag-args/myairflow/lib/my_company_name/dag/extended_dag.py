from airflow import DAG
import logging as log


class ExtendedDAG(DAG):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        log.info('Executing ExtendedDAG constructor')
