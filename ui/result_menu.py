from services.result_service import ResultService
from services.student_service import StudentService
from models.result import Result
import utils.input_helpers as help


result_service = ResultService()
student_service = StudentService()


def result_menu():
    while True:
        print("Result Management System")
        print('''
1. Add Result
2. View Result
3. Update Result
4. Delete Result
5. Back
        ''')
        print("Enter your choice (1-5): ")
        choice = input()
        if choice == '1':
            students, class_subject_id, exam_id = help.select_all_for_result()
            for student in students:
                print(f"Roll Number: {student.roll_number} | Name: {student.name}")
                try:
                    check_existing = result_service.\
                        check_existing_result(student.student_id, class_subject_id, exam_id)
                    if check_existing:
                        result = check_existing
                        print(result.marks)
                        continue
                except ValueError as e:
                    print(f"Error: {e}")
                    continue
                print("Enter marks: ")
                marks = help.input_marks()
                try:
                    result_service.\
                        add_result(result=Result(
                            student_id=student.student_id, class_subject_id=class_subject_id,\
                                exam_id=exam_id, marks=marks))
                except ValueError as e:
                    print(f"Error: {e}")
                    continue

        elif choice == '2':
            try:
                veriables = help.select_all_for_result()
                if not veriables:
                    continue
                students, class_subject_id, exam_id = veriables
            except ValueError as e:
                print(f"Error: {e}")
                continue

            for student in students:
                print(f"Roll Number: {student.roll_number} | Name: {student.name}")
                try:
                    result = result_service.\
                        check_existing_result(student.student_id, class_subject_id, exam_id)
                    if result:
                        print(result.marks)
                        continue
                    else:
                        print("No marks added.")
                        continue
                except ValueError as e:
                    print(f"Error: {e}")
                    continue

        elif choice == '3':
            students, class_subject_id, exam_id = help.select_all_for_result()
            for student in students:
                try:
                    result = result_service.\
                        check_existing_result(student.student_id, class_subject_id, exam_id)
                    if result:
                        print(f"Roll Number: {student.roll_number} | Name: {student.name}")
                        print(result.marks)
                        print("Enter new marks: ")
                        marks = help.input_marks()
                        result_service.update_result_by_id(result.result_id, marks)
                        continue
                    else:
                        print("No added marks found.")
                        continue
                except ValueError as e:
                    print(f"Error: {e}")
                    continue
        
        elif choice == '4':
            students, class_subject_id, exam_id = help.select_all_for_result()
            for student in students:
                try:
                    result = result_service.\
                        check_existing_result(student.student_id, class_subject_id, exam_id)
                    if result:
                        print(f"Roll Number: {student.roll_number} | Name: {student.name}")
                        print(result.marks)
                        print("Are you sure you want to delete this result? (Y/N): ")
                        choice = input()
                        if choice.upper() == 'Y':
                            result_service.delete_result_by_id(result.result_id)
                            print("Result deleted successfully.")
                            continue
                        else:
                            continue
                    else:
                        print("No added marks found.")
                        continue
                except ValueError as e:
                    print(f"Error: {e}")
                    continue

        elif choice == '5':
            break