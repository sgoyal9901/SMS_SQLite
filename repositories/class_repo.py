from database.db_manager import get_connection
from models.school_class import SchoolClass

class ClassRepository:
    def __init__(self):
        self.connection = get_connection()

    def add_class(self, class_name):
        conn = self.connection
        cursor = conn.cursor()
        cursor.execute('INSERT INTO classes (class_name) VALUES (?)', (class_name,))
        conn.commit()

    def get_class_by_name(self, class_name):
        conn = self.connection
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM classes WHERE class_name = ?', (class_name,))
        row = cursor.fetchone()
        if row:
            school_class = self.row_to_class(row)
            return school_class
        return None

    def get_all_classes(self):
        conn = self.connection
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM classes')
        rows = cursor.fetchall()
        school_classes = []
        for row in rows:
            school_class = self.row_to_class(row)
            school_classes.append(school_class)
        return school_classes
    
    def row_to_class(self, row):
        return SchoolClass(
            class_id=row[0],
            class_name=row[1]
        )
    
    def get_class_by_id(self, class_id):
        conn = self.connection
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM classes WHERE class_id = ?', (class_id,))
        row = cursor.fetchone()
        if row:
            school_class= self.row_to_class(row)
            return school_class
        return None
    
    def delete_class(self, class_id):
        conn = self.connection
        cursor = conn.cursor()
        cursor.execute('DELETE FROM classes WHERE class_id = ?', (class_id,))
        if cursor.rowcount == 0:
            raise ValueError(f"No class found with ID {class_id}")
        conn.commit()