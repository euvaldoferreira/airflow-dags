"""
Template para criação de novas DAGs Airflow
Autor: <seu_nome>
Data de criação: <data>
Descrição: <descreva o objetivo da DAG>
"""

from airflow import DAG
from airflow.providers.standard.operators.empty import EmptyOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2025, 9, 15),
    # 'email': ['seu@email.com'],
    # 'retries': 1,
}

dag = DAG(
    'nome_da_dag',
    default_args=default_args,
    description='Descrição da DAG',
    schedule=None,
    catchup=False,
)

start = EmptyOperator(task_id='start', dag=dag)
end = EmptyOperator(task_id='end', dag=dag)

start >> end
