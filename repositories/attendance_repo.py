from database.db_manager import get_connection
from models.attendance import Attendance

class AttendanceRepository:
    def __init__(self):
        self.connection = get_connection()

    def mark_attendance(self, attendance):
        conn = self.connection
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO attendance (student_id, date, status)
            VALUES (?, ?, ?)
        ''', (attendance.student_id, attendance.date, attendance.status))
        conn.commit()
        attendance_id = cursor.lastrowid
        return attendance_id
    
    def row_to_attendace(self, row):
        return Attendance(
            attendance_id=row[0],
            student_id=row[1],
            status=row[2],
            date=row[3],
            name=row[4],
            roll_number=row[5],
            class_name=row[6],
            section_name=row[7]
        )
    
    def get_attendance_by_student_and_date(self, student_id, date):
        conn = self.connection
        cursor = conn.cursor()
        cursor.execute('''
            SELECT * FROM attendance
            WHERE student_id = ? AND date = ?
        ''', (student_id, date))
        row = cursor.fetchone()
        if row:
            attendance = self.row_to_attendace(row)
            return attendance
        return None
    
    def get_attendance_by_section_and_date(self, section_id, date):
        conn = self.connection
        cursor = conn.cursor()
        cursor.execute('''
            SELECT
                attendance.attendance_id,
                attendance.student_id,  
                attendance.status,
                attendance.date,
                students.name,
                students.roll_number,
                classes.class_name,
                sections.section_name
            FROM attendance
            JOIN students ON attendance.student_id = students.student_id 
            JOIN sections ON students.section_id = sections.section_id
            JOIN classes ON sections.class_id = classes.class_id
            WHERE students.section_id = ? AND date = ?
            ORDER BY students.roll_number
        ''', (section_id, date))
        rows = cursor.fetchall()
        attendances = []
        for row in rows:
            attendance = self.row_to_attendace(row)
            attendances.append(attendance)
        return attendances
    
