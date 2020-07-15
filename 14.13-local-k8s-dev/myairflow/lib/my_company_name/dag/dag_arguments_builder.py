from datetime import timedelta


class DAGArgumentsBuilder:

    @staticmethod
    def build(start_date,
              owner='airflow',
              retries=3,
              retry_delay=10):

        return {
            'owner': owner,
            'start_date': start_date,
            'retries': retries,
            'retry_delay': timedelta(minutes=retry_delay)
        }
