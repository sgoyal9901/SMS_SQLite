from database.db_manager import get_connection
from models.result import Result

class ResultRepository:
    def __init__(self):
        self.connection = get_connection()

    def row_to_result(self, row):
        return Result(
            result_id = row[0],
            student_id = row[1],
            class_subject_id= row[2],
            exam_id = row[3],
            marks = row[4],
            name = row[5],
            roll_number = row[6],
            class_name = row[7],
            section_name = row[8]
            )

    def add_result(self, result):
        conn = self.connection
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO results (student_id, class_subject_id, exam_id, marks)
            VALUES (?, ?, ?, ?)
        ''', (result.student_id, result.class_subject_id, result.exam_id, result.marks))
        conn.commit()
        result_id = cursor.lastrowid
        return result_id
    
    def get_result_by_student_id(self, student_id):
        conn = self.connection
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM results WHERE student_id = ?', (student_id,))
        rows = cursor.fetchall()
        results = [self.row_to_result(row) for row in rows]
        return results
    
    def get_result_by_class_subject_id (self, class_subject_id):
        conn = self.connection
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM results WHERE class_subject_id = ?', (class_subject_id,))
        rows = cursor.fetchall()
        results = [self.row_to_result(row) for row in rows]
        return results
    
    def get_result_by_exam_id(self, exam_id):
        conn = self.connection
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM results WHERE exam_id = ?', (exam_id,))
        rows = cursor.fetchall()
        results = [self.row_to_result(row) for row in rows]
        return results
    
    def update_result_by_id(self, result_id, marks):
        conn = self.connection
        cursor = conn.cursor()
        cursor.execute('UPDATE results SET marks = ? WHERE result_id = ?', (marks, result_id))
        conn.commit()
        return
    
    def delete_result_by_id(self, result_id):
        conn = self.connection
        cursor = conn.cursor()
        cursor.execute('DELETE FROM results WHERE result_id = ?', (result_id,))
        conn.commit()
        return