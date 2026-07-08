def val_student_id(student_id):
    if not student_id.strip():
        raise ValueError("Student ID cannot be empty.")
    if not student_id.isdigit():
        raise ValueError("Student ID must be a number.")
    student_id = int(student_id)
    return student_id