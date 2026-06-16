import sqlite3

database_name = 'school.db'

def get_connection():
    conn = sqlite3.connect(database_name)
    conn.execute("PRAGMA foreign_keys = ON")
    return conn