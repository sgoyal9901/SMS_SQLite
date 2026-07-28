from database.connection import get_connection
from models.subjects import Subjects

class SubjectsRepository:
    def add_subject(self, subject_name):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO subjects (subject_name) VALUES (?)", (subject_name,))
            conn.commit()
            subject_id = cursor.lastrowid
            return subject_id
    
    def row_to_subjects(self, row):
        return Subjects(
            subject_id = row[0],
            subject_name = row[1]
        )
    
    def get_subject_by_id(self, subject_id):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM subjects WHERE subject_id = ?', (subject_id,))
            row = cursor.fetchone()
            if row:
                subject = self.row_to_subjects(row)
                return subject
            return None
    
    def get_subject_by_name(self, subject_name):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM subjects WHERE subject_name = ?', (subject_name,))
            row = cursor.fetchone()
            if row:
                subject = self.row_to_subjects(row)
                return subject
            return None
    
    def view_subjects(self):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM subjects')
            rows = cursor.fetchall()
            subjects = []
            for row in rows:
                subject = self.row_to_subjects(row)
                subjects.append(subject)
            return subjects

    def delete_subject(self, subject_id):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM subjects WHERE subject_id = ?', (subject_id,))
            if cursor.rowcount == 0:
                raise ValueError(f"No subject found with ID {subject_id}")
            conn.commit()

    def subject_exists(self, subject_name):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM subjects WHERE subject_name = ?', (subject_name,))
            row = cursor.fetchone()
            if row:
                return True
            return False
    
    def subject_exists_by_id(self, subject_id):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM subjects WHERE subject_id = ?', (subject_id,))
            row = cursor.fetchone()
            if row:
                return True
            return False