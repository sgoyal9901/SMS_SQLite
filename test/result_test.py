import pytest
import database.db_manager as db
import database.init_db as init_db

db.set_database_name('test_school.db')
conn = db.get_connection()

init_db.initialize_database()

def print():
    with pytest.raises(ValueError):
        conn.execute("SELECT * FROM result")