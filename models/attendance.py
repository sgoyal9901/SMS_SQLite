class Attendance:
    def __init__(self,  student_id, status, date, attendance_id=None, name=None, roll_number=None,\
                 class_name=None, section_name=None):
        self.attendance_id = attendance_id
        self.student_id = student_id
        self.status = status
        self.date = date
        self.name = name
        self.roll_number = roll_number
        self.class_name = class_name
        self.section_name = section_name

    def __str__(self):
        return f'''
Roll Number: {self.roll_number}
Name: {self.name}
Status: {self.status}
        '''