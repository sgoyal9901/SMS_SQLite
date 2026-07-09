from services.class_service import ClassService
from services.section_service import SectionService
import utils.input_helpers as help

class_service = ClassService()
section_service = SectionService()

def school_structure():
    while True:
        print("School Structure")
        print('''
    1. Add Class
    2. View Class
    3. Add Section
    4. View Section
    5. View All classes
    6. Delete Class
    7. Delete Section
    8. Back
            ''')
        print("Enter your choice (1-7): ")
        choice = input()
        if choice == '1':
            print("Enter class name: ")
            class_name = input()
            try:
                class_service.add_class(class_name)
                print(f"Class added successfully.")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == '2':
            classes = class_service.get_all_classes()
            if classes:
                for class_ in classes:
                    print(class_)
            else:
                print("No classes found.")

        elif choice == '3':
            try:
                class_id = help.select_class()
            except ValueError as e:
                print(f"Error: {e}")
                continue
            print("Enter section name: ")
            section_name = input().capitalize()
            try:
                section_service.add_section(section_name, class_id)
                print(f"Section added successfully.")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == '4':
            try:
                class_id = help.select_class()
            except ValueError as e:
                print(f"Error: {e}")
                continue
            sections = section_service.get_sections_by_class(class_id)
            if sections:
                for section in sections:
                    print(section)
            else:
                print("No sections found.")

        elif choice == '5':
            classes = class_service.get_all_classes()
            if classes:
                for class_ in classes:
                    sections = section_service.get_sections_by_class(class_.class_id)
                    if sections:
                        for section in sections:
                            print(f"Class: {class_.class_name} {section.section_name}")
                    else:
                        print(f"Class: {class_.class_name} (no sections)")
            else:
                print("No classes found.")

        elif choice == '6':
            try:
                class_id = help.select_class()
            except ValueError as e:
                print(f"Error: {e}")
                continue
            sections = section_service.get_sections_by_class(class_id)
            for i, section in enumerate(sections, start=1):
                print(f"{i}. {section.section_name}")
            print ("Are you sure you want to delete this class and sections? (Y/N): ")
            confirm = input().upper()
            if confirm == 'Y':
                try:
                    class_service.delete_class(class_id)
                    print("Class deleted successfully.")
                except ValueError as e:
                    print(f"Error: {e}")
            else:
                print("Deletion cancelled.")

        elif choice == '7':
            try:
                class_id = help.select_class()
            except ValueError as e:
                print(f"Error: {e}")
                continue
            try:
                section_id = help.select_section(class_id)
            except ValueError as e:
                print(f"Error: {e}")
                continue
            print ("Are you sure you want to delete this section? (Y/N): ")
            confirm = input().upper()
            if confirm == 'Y':
                try:
                    section_service.delete_section(section_id)
                    print("Section deleted successfully.")
                except ValueError as e:
                    print(f"Error: {e}")
            else:
                print("Deletion cancelled.")

        elif choice == '8':
            break