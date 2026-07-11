from services.class_service import ClassService
from services.section_service import SectionService
from services.exams_service import ExamsService
from services.class_subject_service import ClassSubjectsService
from services.student_service import StudentService

class_service = ClassService()
section_service = SectionService()
exams_service = ExamsService()
class_subject_service = ClassSubjectsService()
student_service = StudentService()

def input_student_id():
    while True:
        student_id = input()
        if not student_id.strip():
            print("Student ID cannot be empty.")
        if not student_id.isdigit():
            print("Student ID must be a number.")
        else:
            return int(student_id)

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

def val_marks_ui(marks):
    if not marks.strip():
        raise ValueError("Marks cannot be empty.")
    if not marks.isdigit():
        raise ValueError("Marks must be a number.")
    if int(marks) < 0 or int(marks) > 100:
        raise ValueError("Marks must be between 0 and 100.")
    
def select_exam():
    exams = exams_service.get_all_exams()
    if not exams:
        raise ValueError("No exams found.")
    for i, exam in enumerate(exams, start=1):
        print(f"{i}. {exam.exam_name}")
    exam_choice = input()
    try:
        exam_id = exams[int(exam_choice) - 1].exam_id
        return exam_id
    except:
        raise ValueError("Invalid exam choice.")
    
def select_class_subject(class_id):
    class_subjects = class_subject_service.view_subjects_by_class(class_id)
    if not class_subjects:
        raise ValueError("No subjects found for this class.")
    for i, class_subject in enumerate(class_subjects, start=1):
        print(f"{i}. {class_subject.subject_name}")
    class_subject_choice = input()
    try:
        class_subject_id = class_subjects[int(class_subject_choice) - 1].class_subject_id
        return class_subject_id
    except:
        raise ValueError("Invalid class subject choice.")
    
def select_all_for_result():
    while True:
        print("Choose Class by number: ")
        try:
            class_id = select_class()
        except ValueError as e:
            print(f"Error: {e}")
            continue
        print("Choose Section by number: ")
        try:
            section_id = select_section(class_id)
        except ValueError as e:
            print(f"Error: {e}")
            continue
        students = student_service.get_student_by_section(section_id)
        if not students:
            print("No students found.")
            break
        print("Choose Subject by number: ")
        try:
            class_subject_id = select_class_subject(class_id)
        except ValueError as e:
            print(f"Error: {e}")
            continue
        print("Choose Exam by number: ")
        try:
            exam_id = select_exam()
        except ValueError as e:
            print(f"Error: {e}")
            continue
        return students, class_subject_id, exam_id

def input_marks():
    while True:
        marks = input()
        if not marks.strip():
            print("Marks cannot be empty.")
        if not marks.lstrip('-').isdigit():
            print("Marks must be a number.")
        if int(marks) < 0 or int(marks) > 100:
            print("Marks must be between 0 and 100.")
        else:
            return int(marks)    
