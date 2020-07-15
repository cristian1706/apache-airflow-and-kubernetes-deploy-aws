from airflow.contrib.kubernetes.pod import Pod


def pod_mutation_hook(pod: Pod):
    volume = {
            'name': 'a1-airflow-plugins',
            'persistentVolumeClaim': {
                'claimName': 'a1-airflow-plugins'
            }
    }
    pod.volumes.append(volume)

    volume_mount = {
        'name': 'a1-airflow-plugins',
        'mountPath': '/usr/local/airflow/myairflow/lib',
        'readOnly': True,
    }
    pod.volume_mounts.append(volume_mount)
