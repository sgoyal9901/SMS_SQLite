from services.exams_service import ExamsService
from services.result_service import ResultService
import utils.input_helpers as help

exams_service = ExamsService()
result_service = ResultService()

def exams_menu():
    while True:
        print("Exams Management System")
        print('''
1. Add Exam
2. View Exams
3. Delete Exam
4. Update Exam
5. Back
        ''')
        print("Enter your choice (1-5): ")
        choice = input()
        if choice == '1':
            print("Enter exam name: ")
            exam_name = input().title()
            try:
                exams_service.add_exams(exam_name)
                print(f"Exam '{exam_name}' added successfully.")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == '2':
            exams = exams_service.get_all_exams()
            if exams:
                for exam in exams:
                    print(exam)
            else:
                print("No exams found.")

        elif choice == '3':
            print("Choose exam number to delete: ")
            try:
                exam_id = help.select_exam()
            except ValueError as e:
                print(f"Error: {e}")
                continue
            try:
                exams_service.delete_exams_by_id(exam_id)
                print(f"Exam deleted successfully.")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == '4':
            print("Choose exam number to update: ")
            try:
                exam_id = help.select_exam()
            except ValueError as e:
                print(f"Error: {e}")
                continue
            print("Enter new exam name: ")
            new_exam_name = input().title()
            check_duplicate = exams_service.get_exams_by_name(new_exam_name)
            if check_duplicate:
                print(f"An exam with the name '{new_exam_name}' already exists.")
                continue
            try:
                exams_service.update_exams_by_id(exam_id, new_exam_name)
                print(f"Exam '{new_exam_name}' updated successfully.")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == '5':
            break