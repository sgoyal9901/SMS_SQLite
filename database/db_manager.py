import sqlite3

database_name = 'school.db'

def set_database_name(name):
    global database_name
    database_name = name

def get_connection():
    conn = sqlite3.connect(database_name)
    conn.execute("PRAGMA foreign_keys = ON")
    return conn