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
            marks = row[4]
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
    
    def check_existing_result(self, student_id, class_subject_id, exam_id):
        conn = self.connection
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM results WHERE student_id = ? AND class_subject_id = ? \
                       AND exam_id = ?', (student_id, class_subject_id, exam_id))
        row = cursor.fetchone()
        if row:
            result = self.row_to_result(row)
            return result
        return None

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
    
    def get_result_id_by_data(self, student_id, class_subject_id, exam_id):
        conn = self.connection
        cursor = conn.cursor()
        cursor.execute('SELECT result_id FROM results WHERE student_id = ? AND class_subject_id = ? \
                       AND exam_id = ?', (student_id, class_subject_id, exam_id))
        row = cursor.fetchone()
        if row:
            result_id = row[0]
            return result_id
        return None
    
    def get_result_of_student(self, student_id, exam_id):
        conn = self.connection
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM results WHERE student_id = ? AND exam_id = ?', (student_id, exam_id))
        rows = cursor.fetchall()
        results = [self.row_to_result(row) for row in rows]
        return results