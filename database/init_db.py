from database.db_manager import get_connection

def initialize_database():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS classes (
                   class_id INTEGER PRIMARY KEY AUTOINCREMENT,
                   class_name TEXT NOT NULL
               )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS sections (
                   section_id INTEGER PRIMARY KEY AUTOINCREMENT,
                   section_name TEXT NOT NULL,
                   class_id INTEGER NOT NULL,
                   FOREIGN KEY (class_id) REFERENCES classes(class_id)
               )''')
        
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                        student_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        father_name TEXT NOT NULL,
                        section_id INTEGER NOT NULL,
                        roll_number INTEGER NOT NULL,
                        contact_number TEXT NOT NULL,
                        FOREIGN KEY (section_id) REFERENCES sections(section_id)
                    )''')

    conn.commit()
    