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
                report_card = report_card_service.generate_report_card(student_id, exam_id)
                print(f'''
Name: {report_card.name}
Class: {report_card.class_name} {report_card.section_name}
Roll Number: {report_card.roll_number}
Exam: {report_card.exam_name}
                      ''')
                for subject, marks in report_card.subject_results:
                    print(f"{subject}: {marks}")
                print(f'''
Obtained Marks: {report_card.obtained_marks}
Total Marks: {report_card.total_marks}
Percentage: {report_card.percentage}
Grade: {report_card.grade}
                      ''')
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == '2':
            break