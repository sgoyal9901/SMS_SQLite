from services.student_service import StudentService
from services.class_service import ClassService
from services.section_service import SectionService
import utils.input_helpers as help
student_service = StudentService()
class_service = ClassService()
section_service = SectionService()

def student_menu():
    while True:
        print("Student Management System")
        print('''
1. Add new student
2. Search student by ID
3. Search student by contact number
4. Update student information
5. Delete student
6. Display all students
7. Back
        ''')
        print("Enter your choice (1-7): ")
        choice = input()
        if choice == '1':
            print("Enter student name: ")
            name = input().title()
            print("Enter father name: ")
            father_name = input().title()
            print("Choose class: ")
            try:
                class_id = help.select_class()
            except ValueError as e:
                print(f"Error: {e}")
                continue
            print("Choose section: ")
            try:
                section_id = help.select_section(class_id)
            except ValueError as e:
                print(f"Error: {e}")
                continue
            print("Enter contact number: ")
            contact_number = input()

            try:
                student = student_service.add_student(name, father_name, section_id, contact_number)
                print(f"Student added successfully. with info: {student}")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == '2':
            print("Enter student ID: ")
            student_id = input()
            try:
                student = student_service.get_student_by_id(student_id)
                if student:
                    print(student)
                else:
                    print("Student not found.")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == '3':
            print("Enter contact number: ")
            contact_number = input()
            try:
                students = student_service.get_students_by_contact_number(contact_number)
                for student in students:
                    if student:
                        print(student)
                    else:
                        print("Student not found.")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == '4':
            print("Enter student ID to update: ")
            student_id = input()
            try :
                student = student_service.get_student_by_id(student_id)
                if not student:
                    print("Student not found.")
                else:
                    print(student)
                    print("Enter new name (leave blank to keep current): ")
                    name = input().title()
                    if name.strip() == "":
                        name = None
                    print("Enter new father name (leave blank to keep current): ")
                    father_name = input().title()
                    if father_name.strip() == "":
                        father_name = None
                    print("Enter 'Y' to update class or section (leave blank to keep current): ")
                    update_class_or_section = input().upper()
                    if update_class_or_section == 'Y':
                        print("Choose class: ")
                        try:
                            class_id = help.select_class()
                        except ValueError as e:
                            print(f"Error: {e}")
                            continue
                        print("Choose section: ")
                        try:
                            section_id = help.select_section(class_id)
                        except ValueError as e:
                            print(f"Error: {e}")
                            continue
                    else:
                        section_id = None
                    print("Enter new contact number (leave blank to keep current): ")
                    contact_number = input()
                    if contact_number.strip() == "":
                        contact_number = None
                    if name is None and father_name is None and section_id is None and contact_number is None:
                        print("No changes made.")
                        print(student)
                        continue
                    try:
                        student = student_service.update_student\
                            (student_id, name, father_name, section_id, contact_number)    
                        print("Student information updated successfully.")
                        print(student)
                    except ValueError as e:
                        print(f"Error: {e}")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == '5':
            print("Enter student ID to delete: ")
            student_id = input()
            try:
                student = student_service.get_student_by_id(student_id)
                if not student:
                    print("Student not found.")
                else:
                    print(student)
                    print("Are you sure you want to delete this student? (Y/N): ")
                    confirm = input().upper()
                    if confirm == 'Y':
                        try:
                            student_service.delete_student(student_id)
                            print("Student deleted successfully.")
                        except ValueError as e:
                            print(f"Error: {e}")
                    else:
                        print("Deletion cancelled.")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == '6':
            students = student_service.get_all_students()
            if students:
                for student in students:
                    print(student)
            else:
                print("No students found.")

        elif choice == '7':
            break