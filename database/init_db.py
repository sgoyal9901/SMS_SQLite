from database.db_manager import get_connection

def initialize_database():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS classes (
                   class_id INTEGER PRIMARY KEY AUTOINCREMENT,
                   class_name TEXT NOT NULL UNIQUE
               )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS sections (
                   section_id INTEGER PRIMARY KEY AUTOINCREMENT,
                   section_name TEXT NOT NULL,
                   class_id INTEGER NOT NULL,
                   UNIQUE (section_name, class_id),
                   FOREIGN KEY (class_id) REFERENCES classes(class_id)
               )''')
        
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                        student_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        father_name TEXT NOT NULL,
                        section_id INTEGER NOT NULL,
                        roll_number INTEGER NOT NULL,
                        contact_number TEXT NOT NULL,
                        UNIQUE (name, father_name, contact_number),
                        UNIQUE (section_id, roll_number),
                        FOREIGN KEY (section_id) REFERENCES sections(section_id)
                    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS attendance (
                        attendance_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        student_id INTEGER NOT NULL,
                        status TEXT NOT NULL,
                        date TEXT NOT NULL,
                        UNIQUE (student_id, date),
                        FOREIGN KEY (student_id) REFERENCES students(student_id)
                    )''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS subjects (
                        subject_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        subject_name TEXT NOT NULL UNIQUE)
                    ''')
    conn.commit()
    conn.close()