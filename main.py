from services.student_service import StudentService
from database.init_db import initialize_database


initialize_database()
student_service = StudentService()
while True:
    print("Student Management System")
    print('''
      1. Add new student
      2. Search student by ID
      3. Search student by contact number
      4. Update student information
      5. Delete student
      6. Display all students
      7. Exit
''')
    print("Enter your choice (1-7): ")    
    choice = input()
    if choice == '1':
        print("Enter student name: ")
        name = input().title()
        print("Enter father name: ")
        father_name = input().title()
        print("Enter class name: ")
        class_name = input()
        print("Enter section: ")
        section = input().upper()
        print("Enter contact number: ")
        contact_number = input()
        try:
            student = student_service.add_student(name, father_name, class_name, section, contact_number)
            print(f"Student added successfully. with ID: {student.student_id}")
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
            if students:
                for student in students:
                    print(student)
            else:
                print("Student not found.")
        except ValueError as e:
            print(f"Error: {e}")

    elif choice == '4':
        print("Enter student ID to update: ")
        student_id = input()
        try:
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
                print("Enter new class name (leave blank to keep current): ")
                class_name = input()
                if class_name.strip() == "":
                    class_name = None
                print("Enter new section (leave blank to keep current): ")
                section = input().upper()
                if section.strip() == "":
                    section = None
                print("Enter new contact number (leave blank to keep current): ")
                contact_number = input()
                if contact_number.strip() == "":
                    contact_number = None
                try:
                    student = student_service.update_student(student_id, name, father_name, class_name, section, contact_number)
                    print("Student information updated successfully.")
                    print(student)
                except ValueError as e:
                    print(f"Error: {e}")
        except ValueError as e:
            print(f"Error: {e}")

    elif choice == '5':
        print("Enter student ID to delete: ")
        student_id = input()
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

    elif choice == '6':
        students = student_service.get_all_students()
        if students:
            for student in students:
                print(student)
        else:
            print("No students found.")

    elif choice == '7':
        print("Confirm exit? (Y/N): ")
        confirm = input().upper()
        if confirm == 'Y':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Exit cancelled.")    