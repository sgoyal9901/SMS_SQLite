from repositories.student_repository import StudentRepository
from repositories.section_repository import SectionRepository
from repositories.class_repository import ClassRepository
from models.student import Student

class StudentService:
    def __init__(self):
        self.repository = StudentRepository()
        self.section_repository = SectionRepository()
        self.class_repository = ClassRepository()

    def validate_student_data(self, name, father_name, section_id, contact_number):
        if not name.strip():
            raise ValueError("Student name cannot be empty.")
        if not father_name.strip():
            raise ValueError("Father name cannot be empty.")
        if not section_id:
            raise ValueError("Section_id cannot be empty.")
        if not contact_number.strip():
            raise ValueError("Contact number cannot be empty.")
        if not contact_number.isdigit() or len(contact_number) != 10:
            raise ValueError("Contact number must be a 10-digit number.")
        
    def generate_roll_number(self, section_id):
        repo = self.repository
        generated_roll_number = repo.generate_roll_number(section_id)
        return generated_roll_number
    
    def check_duplicate_student(self, name, father_name, contact_number):
        repo = self.repository
        is_duplicate = repo.check_duplicate_student(name, father_name, contact_number)
        return is_duplicate

    def add_student(self, name, father_name, section_id, contact_number):
        repo = self.repository
        self.validate_student_data(name, father_name, section_id, contact_number)
        if self.check_duplicate_student(name, father_name, contact_number):
            raise ValueError("A student with the same name, father name, and contact number already exists.")
        roll_number = self.generate_roll_number(section_id)
        new_student = Student(
            name=name,
            father_name=father_name,
            section_id=section_id,
            roll_number=roll_number,
            contact_number=contact_number
        )
        student_id = repo.add_student(new_student)
        new_student.student_id = student_id
        student = self.get_student_details(student_id)
        return student 
    
    def get_all_students(self):
        repo = self.repository
        students = repo.get_all_students()
        all_students = []
        for student in students:
            student = self.get_student_details(student.student_id)
            all_students.append(student)
        return all_students
    
    def get_student_by_id(self, student_id):
        if not student_id:
            raise ValueError("Student ID is required.")
        if not student_id.isdigit():
            raise ValueError("Student ID must be a number.")
        repo = self.repository
        student = repo.get_student_by_id(student_id)
        if not student:
            raise ValueError(f"No student found by ID: {student_id}")
        student = self.get_student_details(student_id)
        return student
    
    def get_students_by_contact_number(self, contact_number):
        if not contact_number.strip():
            raise ValueError("Contact number cannot be empty.")
        if not contact_number.isdigit() or len(contact_number) != 10:
            raise ValueError("Contact number must be a 10-digit number.")
        repo = self.repository
        students = repo.get_students_by_contact_number(contact_number)
        all_students = []
        if not students:
            raise ValueError(f"No student found by contact number: {contact_number}")
        for student in students:
            student = self.get_student_details(student.student_id)
            all_students.append(student)
        return all_students
    
    def delete_student(self, student_id):
        if not student_id:
            raise ValueError("Student ID is required.")
        if not student_id.isdigit():
            raise ValueError("Student ID must be a number.")
        repo = self.repository
        repo.delete_student(student_id)
    
    def update_student(self, student_id, name=None, father_name=None,\
                        section_id=None, contact_number=None):
        if not student_id:
            raise ValueError("Student ID is required.")
        if not student_id.isdigit():
            raise ValueError("Student ID must be a number.")
        repo = self.repository
        student = repo.get_student_by_id(student_id)
        if not student:
            raise ValueError(f"No student found by ID: {student_id}")
        old_section_id = student.section_id
        if name is not None:
            if not name.strip():
                raise ValueError("Student name cannot be empty.")
            student.name = name
        if father_name is not None:
            if not father_name.strip():
                raise ValueError("Father name cannot be empty.")
            student.father_name = father_name
        if section_id is not None:
            if not section_id:
                raise ValueError("Section_id cannot be empty.")
            student.section_id = section_id
        if contact_number is not None:
            if not contact_number.strip():
                raise ValueError("Contact number cannot be empty.")
            if not contact_number.isdigit() or len(contact_number) != 10:
                raise ValueError("Contact number must be a 10-digit number.")
            student.contact_number = contact_number
        if (section_id is not None and section_id != old_section_id):
            student.roll_number = self.generate_roll_number(section_id)
        repo.update_student(student)
        student = self.get_student_details(student_id)
        return student
    
    def get_student_details(self, student_id):
        repo = self.repository
        student = repo.get_student_by_id(student_id)
        section = self.section_repository.get_section_by_id(student.section_id)
        student.section_name = section.section_name
        class_ = self.class_repository.get_class_by_id(section.class_id)
        student.class_name = class_.class_name
        return student
    
    def get_student_by_section(self, section_id):
        repo = self.repository
        students = repo.get_student_by_section(section_id)
        return students