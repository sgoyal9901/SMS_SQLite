from services.subjects_service import SubjectsService

subjects_service = SubjectsService()

def subjects_menu():
    while True:
        print("Subjects Management System")
        print('''
1. Add subject
2. View subjects
3. Delete subject
4. Back
        ''')
        print("Enter your choice (1-4): ")
        choice = input()
        if choice == '1':
            print("Enter subject name: ")
            subject_name = input().title()
            try:
                subject_id = subjects_service.add_subject(subject_name)
                print(f"Subject added successfully.")
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
                print("Are you sure you want to delete this subject? (Y/N): ")
                confirm = input().upper()
                if confirm == 'Y':
                    subjects_service.delete_subject(subject_id)
                    print("Subject deleted successfully.")
                else:
                    print("Subject deletion cancelled.")
            except:
                print("Invalid subject choice.")