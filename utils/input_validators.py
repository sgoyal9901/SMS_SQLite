def val_student_id(student_id):
    if not student_id.strip():
        raise ValueError("Student ID cannot be empty.")
    if not student_id.isdigit():
        raise ValueError("Student ID must be a number.")
    student_id = int(student_id)
    return student_id

def val_marks(marks):
    if not marks.strip():
        raise ValueError("Marks cannot be empty.")
    if not marks.lstrip('-').isdigit():
        raise ValueError("Marks must be a number.")
    if int(marks) < 0 or int(marks) > 100:
        raise ValueError("Marks must be between 0 and 100.")
    return marks