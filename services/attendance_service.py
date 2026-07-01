from repositories.attendance_repositories import AttendanceRepository
from repositories.student_repository import StudentRepository
from models.attendance import Attendance

class AttendanceService:
    def __init__(self):
        self.attendance_repository = AttendanceRepository()
        self.student_repository = StudentRepository()

    
    def validate_attendance(self, status):
        if status not in ['P', 'A', 'L']:
            return ValueError\
                ("Invalid status. Status must be 'P' (Present), 'A' (Absent), or 'L' (Leave).")
        return None
    
    
    def validate_date(self, date):
        from datetime import datetime
        #if date > datetime.now().strftime('%Y-%m-%d'):
         #   raise ValueError("Date cannot be in the future.")
        try:
            datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Invalid date format. Date must be in YYYY-MM-DD format.")
        if date > datetime.now().strftime('%Y-%m-%d'):
            raise ValueError("Date cannot be in the future.")

    def mark_attendance(self, student_id, date, status):
        self.validate_attendance(status)
        existing_attendance = self.attendance_repository.get_attendance_by_student_and_date\
            (student_id, date)
        if existing_attendance:
            raise ValueError("Attendance already marked for this student and date.")
        attendance = Attendance(student_id, status, date)
        attendance_id = self.attendance_repository.mark_attendance(attendance)
        return attendance_id
    
    def get_attendance_by_student_and_date(self, student_id, date):
        return self.attendance_repository.get_attendance_by_student_and_date\
            (student_id, date)
    
    def get_attendance_by_section_and_date(self, section_id, date):
        self.validate_date(date)
        return self.attendance_repository.get_attendance_by_section_and_date\
            (section_id, date)
    