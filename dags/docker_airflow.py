from datetime import datetime, timedelta

from airflow import DAG
from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.utils.dates import days_ago

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": days_ago(2),
    "email": ["airflow@example.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=2),
}

dag = DAG("docker_sample", default_args=default_args, schedule_interval=None)

start = BashOperator(task_id="print_date", bash_command="date", dag=dag)

passing = KubernetesPodOperator(
    namespace="default",
    image="vdinesh1990/test_airflow:v1",
    cmds=None,
    arguments=["52"],
    # volume_mounts=volume_mount_list,
    # volumes=volume_list,
    labels={"foo": "bar"},
    name="passing-test",
    task_id="passing-task",
    in_cluster=True,
    # config_file="/home/dinesh.velmuruga/.kube/config",
    get_logs=True,
    dag=dag,
)
passing.set_upstream(start)
