from services.attendance_service import AttendanceService
from services.student_service import StudentService
import utils.input_helpers as help
import utils.validators as val

attendance_service = AttendanceService()
student_service = StudentService()

def attendance_menu():
    while True:
        print("Attendance Management System")
        print('''
1. Mark attendance
2. View attendance
3. Back
        ''')
        print("Enter your choice (1-3): ")
        choice = input()
        if choice == '1':
            print("Enter class")
            try:
                class_id = help.select_class()
            except ValueError as e:
                print(f"Error: {e}")
                continue
            print("Enter section")
            try:
                section_id = help.select_section(class_id)
            except ValueError as e:
                print(f"Error: {e}")
                continue
            from datetime import date
            date = str(date.today())
            print(date)
            students = student_service.get_student_by_section(section_id)
            for student in students:
                print(f"Roll Number: {student.roll_number} | Name: {student.name}")
                print("Choose: P (Present), A (Absent), L (Leave): ")
                status = input().upper()
                try:
                    attendance_service.mark_attendance(student.student_id, date, status)
                except ValueError as e:
                    print(f"Error: {e}")
                    continue

        elif choice == '2':
            print("Enter class")
            try:
                class_id = help.select_class()
            except ValueError as e:
                print(f"Error: {e}")
                continue
            print("Enter section")
            try:
                section_id = help.select_section(class_id)
            except ValueError as e:
                print(f"Error: {e}")
                continue
            date = input("Enter date(YYYY-MM-DD) OR Leave blank for today: ")
            if date.strip() == "":
                from datetime import date
                date = str(date.today())
            else:    
                try:
                    val.val_date(date)
                except ValueError as e:
                    print(f"Error: {e}")
                    continue
            try:
                attendances = attendance_service.get_attendance_by_section_and_date(section_id, date)
                if not attendances:
                    print("No attendance found.")
                    continue
                print(f"Attendance of Class {attendances[0].class_name} {attendances[0].section_name} on {date}")
                for attendance in attendances:
                    print(attendance)
            except ValueError as e:
                print(f"Error: {e}")
                continue

        elif choice == '3':
            break