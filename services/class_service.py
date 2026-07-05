from repositories.class_repo import ClassRepository
from repositories.student_repo import StudentRepository
from repositories.section_repo import SectionRepository
from models.school_class import SchoolClass

class ClassService:
    def __init__(self):
        self.class_repository = ClassRepository()
        self.student_repository = StudentRepository()
        self.section_repository = SectionRepository()

    def add_class(self, class_name):
        if not class_name.strip():
            raise ValueError("Class name cannot be empty")
        if self.class_repository.get_class_by_name(class_name):
            raise ValueError("Class already exists")
        self.class_repository.add_class(class_name)
        
    def get_all_classes(self):
        return self.class_repository.get_all_classes()
    
    def get_class_by_id(self, class_id):
        return self.class_repository.get_class_by_id(class_id)
    
    def delete_class(self, class_id):
        class_ = self.get_class_by_id(class_id)
        if not class_:
            raise ValueError("Class not found")
        if self.student_repository.count_students_in_class(class_id) > 0:
            raise ValueError("Cannot delete class with students")
        sections = self.section_repository.get_sections_by_class(class_id)
        for section in sections:
            self.section_repository.delete_section(section.section_id)
        self.class_repository.delete_class(class_id)