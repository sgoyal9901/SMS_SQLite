from database.db_manager import get_connection
from models.class_subjects import ClassSubjects

class ClassSubjectsRepository:
    def __init__(self):
        self.connection = get_connection()

    def add_class_subject(self, class_id, subject_id):
        conn = self.connection
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO class_subjects (class_id, subject_id)
                        VALUES (?, ?)''', (class_id, subject_id))
        conn.commit()
        class_subject_id = cursor.lastrowid
        return class_subject_id
    
    def row_to_class_subject(self, row):
        return ClassSubjects(
            class_subject_id=row[0],
            class_id=row[1],
            subject_id=row[2],
            subject_name=row[3]
        )
    
    def view_subjects_by_class(self, class_id):
        conn = self.connection
        cursor = conn.cursor()
        cursor.execute('''
            SELECT
                       class_subjects.class_subject_id,
                       class_subjects.class_id,
                       class_subjects.subject_id,
                       subjects.subject_name
            FROM class_subjects
            JOIN subjects ON class_subjects.subject_id = subjects.subject_id
            WHERE class_subjects.class_id = ?
        ''', (class_id,))
        rows = cursor.fetchall()
        class_subjects = []
        for row in rows:
            class_subject = self.row_to_class_subject(row)
            class_subjects.append(class_subject)
        return class_subjects
    
    def delete_subject_from_class(self, class_id, subject_id):
        conn = self.connection
        cursor = conn.cursor()
        cursor.execute('DELETE FROM class_subjects WHERE class_id = ? AND subject_id = ?',\
                        (class_id, subject_id))
        conn.commit()

    def count_classes_with_subject(self, subject_id):
        conn = self.connection
        cursor = conn.cursor()
        cursor.execute('SELECT COUNT(*) FROM class_subjects WHERE subject_id = ?', (subject_id,))
        count = cursor.fetchone()[0]
        return count
    
    def subject_exist_in_class(self, class_id, subject_id):
        conn = self.connection
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM class_subjects WHERE class_id = ? AND subject_id = ?',\
                        (class_id, subject_id))
        row = cursor.fetchone()
        if row:
            return True
        return False
    
    def get_class_subject_by_id(self, class_subject_id):
        conn = self.connection
        cursor = conn.cursor()
        cursor.execute('''SELECT 
                        class_subjects.class_subject_id,
                        class_subjects.class_id,
                        class_subjects.subject_id,
                        subjects.subject_name
                        FROM class_subjects
                        JOIN subjects ON class_subjects.subject_id = subjects.subject_id
                        WHERE class_subjects.class_subject_id = ?''', (class_subject_id,))
        row = cursor.fetchone()
        if row:
            class_subject = self.row_to_class_subject(row)
            return class_subject
        return None 