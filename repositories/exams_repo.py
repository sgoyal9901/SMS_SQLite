from database.db_manager import get_connection
from models.exams import Exams

class ExamsRepository:
    def __init__(self):
        self.connection = get_connection()

    def add_exams(self, exam_name):
        conn = self.connection
        cursor = conn.cursor()
        cursor.execute('INSERT INTO exams (exam_name) VALUES (?)', (exam_name,))
        conn.commit()
        exam_id = cursor.lastrowid
        return exam_id
    
    def row_to_exams(self, row):
        return Exams(
            exam_id=row[0],
            exam_name=row[1]
        )
    
    def get_all_exams(self):
        conn = self.connection
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM exams')
        rows = cursor.fetchall()
        exams = []
        for row in rows:
            exams.append(self.row_to_exams(row))
        return exams
    
    def get_exams_by_id(self, exam_id):
        conn = self.connection
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM exams WHERE exam_id = ?', (exam_id,))
        row = cursor.fetchone()
        if row:
            return self.row_to_exams(row)
        return None
    
    def get_exams_by_name(self, exam_name):
        conn = self.connection
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM exams WHERE exam_name = ?', (exam_name,))
        row = cursor.fetchone()
        if row:
            return self.row_to_exams(row)
        return None
    
    def delete_exams_by_id(self, exam_id):
        conn = self.connection
        cursor = conn.cursor()
        cursor.execute('DELETE FROM exams WHERE exam_id = ?', (exam_id,))
        conn.commit()
        return
    
    def update_exams_by_id(self, exam_id, exam_name):
        conn = self.connection
        cursor = conn.cursor()
        cursor.execute('UPDATE exams SET exam_name = ? WHERE exam_id = ?', (exam_name, exam_id))
        conn.commit()
        return