from database.db_manager import get_connection

def initialize_database():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                        student_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        father_name TEXT NOT NULL,
                        class_name TEXT NOT NULL,
                        section TEXT NOT NULL,
                        roll_number INTEGER NOT NULL,
                        contact_number TEXT NOT NULL
                    )''')
    conn.commit()

