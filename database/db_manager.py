import sqlite3

database_name = 'school.db'

def get_connection():
    conn = sqlite3.connect(database_name)
    return conn