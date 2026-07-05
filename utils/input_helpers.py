from services.class_service import ClassService
from services.section_service import SectionService

class_service = ClassService()
section_service = SectionService()

def select_class():
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


def select_section(class_id):
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

