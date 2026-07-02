from database.db_manager import get_connection
from models.class_subjects import ClassSubjects

class ClassSubjectsRepository:
    def __init__(self):
        self.connection = get_connection()

    def add_class_subject(self, class_subject):
        conn = self.connection
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO class_subjects (class_id, subject_id)
                        VALUES (?, ?)''', (class_subject.class_id, class_subject.subject_id))
        conn.commit()
        class_subject_id = cursor.lastrowid
        return class_subject_id
    
    def row_to_class_subject(self, row):
        return ClassSubjects(
            class_subject_id=row[0],
            class_id=row[1],
            subject_id=row[2]
        )
    
    def view_subjects_by_class(self, class_id):
        conn = self.connection
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM class_subjects WHERE class_id = ?', (class_id,))
        rows = cursor.fetchall()
        class_subjects = []
        for row in rows:
            class_subject = self.row_to_class_subject(row)
            class_subjects.append(class_subject)
        return class_subjects
    
    def delete_class_subject(self, class_subject_id):
        conn = self.connection
        cursor = conn.cursor()
        cursor.execute('DELETE FROM class_subjects WHERE class_subject_id = ?', (class_subject_id,))
        conn.commit()