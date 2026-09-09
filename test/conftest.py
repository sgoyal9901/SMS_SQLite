import pytest
from database.connection import set_database_name
from database.init_db import initialize_database

@pytest.fixture(scope="session", autouse=True)
def test_database():
    set_database_name("test_school.db")
    initialize_database()
    yield