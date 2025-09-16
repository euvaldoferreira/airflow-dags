# pytest configuration for Airflow DAGs
import os
import tempfile
import pytest

@pytest.fixture(scope="session", autouse=True)
def airflow_home_tmpdir():
    tmpdir = tempfile.mkdtemp(prefix="airflow_home_")
    os.environ["AIRFLOW_HOME"] = tmpdir
    yield tmpdir
