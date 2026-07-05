def val_student_name(student_name):
    if not student_name.strip():
        raise ValueError("Student name cannot be empty.")
    if not student_name.isalpha():
        raise ValueError("Student name must contain only alphabetic characters.")
    
def val_student_id(student_id):
    if not student_id.strip():
        raise ValueError("Student ID cannot be empty.")
    if not student_id.isdigit():
        raise ValueError("Student ID must be a number.")

def val_father_name(father_name):
    if not father_name.strip():
        raise ValueError("Father name cannot be empty.")
    

def val_contact_number(contact_number):
    if not contact_number.strip():
        raise ValueError("Contact number cannot be empty.")
    if not contact_number.isdigit() or len(contact_number) != 10:
        raise ValueError("Contact number must be a 10-digit number.")
    

def val_section_id(section_id):
    if not section_id:
        raise ValueError("Section_id cannot be empty.")
    

def validate_date(date):
        from datetime import datetime
        try:
            datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Invalid date format. Date must be in YYYY-MM-DD format.")
        if date > datetime.now().strftime('%Y-%m-%d'):
            raise ValueError("Date cannot be in the future.")
        

def val_marks(marks):
    if not marks.strip():
        raise ValueError("Marks cannot be empty.")
    if not marks.isdigit():
        raise ValueError("Marks must be a number.")