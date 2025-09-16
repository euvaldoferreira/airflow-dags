from airflow import DAG
from airflow.providers.standard.operators.empty import EmptyOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2025, 9, 15),
}

dag = DAG(
    'example_dag',
    default_args=default_args,
    schedule=None,
    catchup=False,
)


start = EmptyOperator(task_id='start', dag=dag)
end = EmptyOperator(task_id='end', dag=dag)

start >> end
