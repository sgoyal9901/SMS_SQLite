from services.class_service import ClassService
from services.section_service import SectionService

class_service = ClassService()
section_service = SectionService()

def select_classes():
    classes = class_service.get_all_classes()
    if not classes:
        raise ValueError("No classes found.")
    for i, class_ in enumerate(classes, start=1):
        print(f"{i}. {class_.class_name}")
    class_choice = input()
    try:
        class_id = classes[int(class_choice) - 1].class_id
        return class_id
    except:
        raise ValueError("Invalid class choice.")


def select_sections(class_id):
    sections = section_service.get_sections_by_class(class_id)
    if not sections:
        raise ValueError("No sections found.")
    for i, section in enumerate(sections, start=1):
        print(f"{i}. {section.section_name}")
    section_choice = input()
    try:
        section_id = sections[int(section_choice) - 1].section_id
        return section_id
    except:
        raise ValueError("Invalid section choice.") 


def school_structure():
    while True:
        print("School Structure")
        print('''
    1. Add Class
    2. View Class
    3. Add Section
    4. View Section
    5. Delete Class
    6. Delete Section
    7. Back
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
                class_id = select_classes()
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
                class_id = select_classes()
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
            try:
                class_id = select_classes()
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

        elif choice == '6':
            try:
                class_id = select_classes()
            except ValueError as e:
                print(f"Error: {e}")
                continue
            try:
                section_id = select_sections(class_id)
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

        elif choice == '7':
            break