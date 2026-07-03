from services.subjects_service import SubjectsService
from services.class_subject_services import ClassSubjectsService
from ui.school_structure_menu import select_classes
from models.subjects import Subjects

subjects_service = SubjectsService()
class_subject_service = ClassSubjectsService()

def subjects_menu():
    while True:
        print("Subjects Management System")
        print('''
1. Add subject
2. View subjects
3. Delete subject
4. Add subjects to class
5. View subjects of class
6. Delete subjects of class
7.Back
        ''')
        print("Enter your choice (1-7): ")
        choice = input()
        if choice == '1':
            print("Enter subjects name (Separated by comma): ")
            subjects_name = input()
            subjects_name = [subject_name.strip().title() for subject_name in subjects_name.split(',')]
            try:
                for subject_name in subjects_name:
                    if not subject_name.strip():
                        continue
                    added = subjects_service.add_subject(subject_name)
                    if added:
                        print(f"Subject '{subject_name}' added successfully.")
                    else:
                        print(f"Subject '{subject_name}' already exists.")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == '2':
            subjects = subjects_service.view_subjects()
            if not subjects:
                print("No subjects found.")
            for i, subject in enumerate(subjects, start=1):
                print(f"{i}. {subject.subject_name}")

        elif choice == '3':
            subjects = subjects_service.view_subjects()
            if not subjects:
                print("No subjects found.")
                continue
            for i, subject in enumerate(subjects, start=1):
                print(f"{i}. {subject.subject_name}")
            print("Choose number: ")
            subject_choice = input()
            try:
                subject_id = subjects[int(subject_choice) - 1].subject_id
            except:
                print("Invalid subject choice.")
            print("Are you sure you want to delete this subject? (Y/N): ")
            confirm = input().upper()
            if confirm == 'Y':
                try:
                    subjects_service.delete_subject(subject_id)
                    print("Subject deleted successfully.")
                except ValueError as e:
                    print(f"Error: {e}")
            else:
                print("Subject deletion cancelled.")

        elif choice == '4':
            print("Choose class: ")
            try:
                class_id = select_classes()
            except ValueError as e:
                print(f"Error: {e}")
                continue
            subjects = subjects_service.view_subjects()
            if not subjects:
                print("No subjects found.")
                continue
            for i, subject in enumerate(subjects, start=1):
                print(f"{i}. {subject.subject_name}")
            print("Select subjects numbers (Separated by comma): ")
            subject_choices = input().split(',')
            subject_ids = []
            for subject_choice in subject_choices:
                if not subject_choice.strip():
                    continue
                try:
                    int(subject_choice)
                except:
                    print(f"Invalid subject choice: {subject_choice}")
                    continue
                if int(subject_choice) < 1 or int(subject_choice) > len(subjects):
                    print(f"Invalid subject choice: {subject_choice}")
                    continue
                subject_id = subjects[int(subject_choice) - 1].subject_id
                subject_ids.append(subject_id)
            for subject_id in subject_ids:
                try:
                    added = class_subject_service.add_subject_to_class(class_id, subject_id)
                    if added:
                        print(f"Subject added to class successfully.")
                    if not added:
                        print(f"Subject already exists in class.")
                except ValueError as e:
                    print(f"Error: {e}")
            
        elif choice == '5':
            print("Choose class: ")
            try:
                class_id = select_classes()
            except ValueError as e:
                print(f"Error: {e}")
                continue
            subjects = class_subject_service.view_subjects_by_class(class_id)
            if not subjects:
                print("No subjects found.")
            for i, subject in enumerate(subjects, start=1):
                print(f"{i}. {subject.subject_name}")