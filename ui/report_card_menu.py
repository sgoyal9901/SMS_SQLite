from services.report_card_service import ReportCardService
from services.student_service import StudentService
from models.report_card import ReportCard
import utils.input_helpers as help

report_card_service = ReportCardService()
student_service = StudentService()
report_card = ReportCard()

def report_card_menu():
    while True:
        print("Report Card Management System")
        print('''
1. Generate Report Card
2. Back
        ''')
        print("Enter your choice (1-2): ")
        choice = input()
        if choice == '1':
            print("Enter student ID: ")
            student_id = help.input_student_id()
            student = student_service.get_student_by_id(student_id)
            if not student:
                print(f"No student found by ID: {student_id}")
                continue
            else:
                print(f'''
Name: {student.name}
Class: {student.class_name} {student.section_name}
Roll Number: {student.roll_number}
    ''')
            print("Choose Exam by number: ")
            try:
                exam_id = help.select_exam()
            except ValueError as e:
                print(f"Error: {e}")
                continue
            try:
                results, obtained_marks, total_marks, percentage = \
                    report_card_service.get_report_card(student_id, exam_id)
                for result in results:
                    print(f"Subject: {result.subject_name} | Marks: {result.marks}/100")
                print(f'''
Obtained Marks: {obtained_marks}
Total Marks: {total_marks}
Percentage: {percentage}%
                    ''')
            except ValueError as e:
                print(f"Error: {e}")
                continue