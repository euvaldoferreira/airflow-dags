import pytest
from airflow.models import DagBag

def test_example_dag_import():
    dagbag = DagBag(dag_folder='dags', include_examples=False)
    assert 'example_dag' in dagbag.dags
    assert dagbag.import_errors == {}

def test_example_dag_structure():
    dagbag = DagBag(dag_folder='dags', include_examples=False)
    dag = dagbag.get_dag('example_dag')
    assert dag is not None
    assert set([t.task_id for t in dag.tasks]) == {'start', 'end'}
