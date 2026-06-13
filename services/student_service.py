from repositories.student_repository import StudentRepository
from models.student import Student

class StudentService:
    def __init__(self):
        self.repository = StudentRepository()

    def validate_student_data(self, name, father_name, class_name, section, contact_number):
        if not name.strip():
            raise ValueError("Student name cannot be empty.")
        if not father_name.strip():
            raise ValueError("Father name cannot be empty.")
        if not class_name.strip():
            raise ValueError("Class name cannot be empty.")
        if not section.strip():
            raise ValueError("Section cannot be empty.")
        if not contact_number.strip():
            raise ValueError("Contact number cannot be empty.")
        if not contact_number.isdigit() or len(contact_number) != 10:
            raise ValueError("Contact number must be a 10-digit number.")
        
    def generate_roll_number(self, class_name, section):
        repo = self.repository
        generated_roll_number = repo.generate_roll_number(class_name, section)
        return generated_roll_number
    
    def check_duplicate_student(self, name, father_name, contact_number):
        repo = self.repository
        is_duplicate = repo.check_duplicate_student(name, father_name, contact_number)
        return is_duplicate

    def add_student(self, name, father_name, class_name, section, contact_number):
        repo = self.repository
        self.validate_student_data(name, father_name, class_name, section, contact_number)
        if self.check_duplicate_student(name, father_name, contact_number):
            raise ValueError("A student with the same name, father name, and contact number already exists.")
        roll_number = self.generate_roll_number(class_name, section)
        new_student = Student(
            name=name,
            father_name=father_name,
            class_name=class_name,
            section=section,
            roll_number=roll_number,
            contact_number=contact_number
        )
        student_id = repo.add_student(new_student)
        new_student.student_id = student_id
        return new_student  
    
    def get_all_students(self):
        repo = self.repository
        students = repo.get_all_students()
        return students
    
    def get_student_by_id(self, student_id):
        if not student_id:
            raise ValueError("Student ID is required.")
        if not student_id.isdigit():
            raise ValueError("Student ID must be a number.")
        repo = self.repository
        student = repo.get_student_by_id(student_id)
        return student
    
    def get_students_by_contact_number(self, contact_number):
        if not contact_number.strip():
            raise ValueError("Contact number cannot be empty.")
        if not contact_number.isdigit() or len(contact_number) != 10:
            raise ValueError("Contact number must be a 10-digit number.")
        repo = self.repository
        students = repo.get_students_by_contact_number(contact_number)
        return students
    
    def delete_student(self, student_id):
        if not student_id:
            raise ValueError("Student ID is required.")
        if not student_id.isdigit():
            raise ValueError("Student ID must be a number.")
        repo = self.repository
        repo.delete_student(student_id)
    
    def update_student(self, student_id, name=None, father_name=None, class_name=None, section=None, contact_number=None):
        if not student_id:
            raise ValueError("Student ID is required.")
        if not student_id.isdigit():
            raise ValueError("Student ID must be a number.")
        repo = self.repository
        student = repo.get_student_by_id(student_id)
        if not student:
            raise ValueError(f"No student found by ID: {student_id}")
        old_class_name = student.class_name
        old_section = student.section
        if name is not None:
            if not name.strip():
                raise ValueError("Student name cannot be empty.")
            student.name = name
        if father_name is not None:
            if not father_name.strip():
                raise ValueError("Father name cannot be empty.")
            student.father_name = father_name
        if class_name is not None:
            if not class_name.strip():
                raise ValueError("Class name cannot be empty.")
            student.class_name = class_name
        if section is not None:
            if not section.strip():
                raise ValueError("Section cannot be empty.")
            student.section = section
        if contact_number is not None:
            if not contact_number.strip():
                raise ValueError("Contact number cannot be empty.")
            if not contact_number.isdigit() or len(contact_number) != 10:
                raise ValueError("Contact number must be a 10-digit number.")
            student.contact_number = contact_number
        if (class_name is not None and class_name != old_class_name) \
            or (section is not None and section != old_section):
            student.roll_number = self.generate_roll_number(student.class_name, student.section)
        repo.update_student(student)
        return student
    