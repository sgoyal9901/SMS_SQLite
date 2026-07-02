from database.init_db import initialize_database
from ui.student_menu import student_menu
from ui.school_structure_menu import school_structure
from ui.attendance_menu import attendance_menu
from ui.subjects_management import subjects_menu

initialize_database()

while True:
    print("School Management System")
    print('''
1. Student Menu
2. School Structure
3. Attendance Menu
4. Subject Menu
5. Exit
    ''')
    print("Enter your choice (1-5): ")
    choice = input()
    if choice == '1':
        student_menu()

    elif choice == '2':
        school_structure()

    elif choice == '3':
        attendance_menu()
    
    elif choice == '4':
        subjects_menu()

    elif choice == '5':
        print("Confirm exit? (Y/N): ")
        confirm = input().upper()
        if confirm == 'Y':
            break
        else:
            continue
