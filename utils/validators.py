def val_student_name(student_name):
    if not student_name.strip():
        raise ValueError("Student name cannot be empty.")
    if not student_name.replace(' ', '').isalpha():
        raise ValueError("Student name must contain only letters.")
    
def val_student_id(student_id):
    if not isinstance(student_id, int):
        raise ValueError("Student ID must be an integer.")
    if not student_id:
        raise ValueError("Student ID cannot be empty.")
    if student_id < 0:
        raise ValueError("Student ID cannot be negative.")

def val_father_name(father_name):
    if not father_name.strip():
        raise ValueError("Father name cannot be empty.")
    if not father_name.replace(' ', '').isalpha():
        raise ValueError("Father name must contain only letters.")
    

def val_contact_number(contact_number):
    if not contact_number.strip():
        raise ValueError("Contact number cannot be empty.")
    if not contact_number.isdigit() or len(contact_number) != 10:
        raise ValueError("Contact number must be a 10-digit number.")
    

def val_section_id(section_id):
    if not section_id:
        raise ValueError("Section_id cannot be empty.")
    

def val_date(date):
        from datetime import datetime
        try:
            datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Invalid date format. Date must be in YYYY-MM-DD format.")
        if date > datetime.now().strftime('%Y-%m-%d'):
            raise ValueError("Date cannot be in the future.")
        

def val_class_subject_id (class_subject_id):
    if not class_subject_id.strip():
        raise ValueError("Class_subject_id cannot be empty.")
    

def val_exam_id(exam_id):
    if not exam_id.strip():
        raise ValueError("Exam_id cannot be empty.")
        

def val_marks(marks):
    if not isinstance(marks, int):
        raise ValueError("Marks must be an integer.")
    if not marks:
        raise ValueError("Marks cannot be empty.")
    if marks < 0 or marks > 100:
        raise ValueError("Marks must be between 0 and 100.")
    