from datetime import datetime, timedelta

from airflow import DAG
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

dag = DAG("kubernetes_sample", default_args=default_args, schedule_interval=None)

start = DummyOperator(task_id="run_this_first", dag=dag)

passing = BashOperator(task_id="print_date", bash_command="date", dag=dag)
passing.set_upstream(start)
