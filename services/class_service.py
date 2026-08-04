from repositories.class_repo import ClassRepository
from repositories.student_repo import StudentRepository
from repositories.section_repo import SectionRepository
from models.school_class import SchoolClass
import exception.class_ as class_er

class ClassService:
    def __init__(self):
        self.class_repository = ClassRepository()
        self.student_repository = StudentRepository()
        self.section_repository = SectionRepository()

    def add_class(self, class_name):
        if not class_name.strip():
            raise class_er.InvalidClassDataError("Class name cannot be empty")
        if self.class_repository.get_class_by_name(class_name):
            raise class_er.ClassAlreadyExistsError("Class already exists")
        self.class_repository.add_class(class_name)
        
    def get_all_classes(self):
        classes = self.class_repository.get_all_classes()
        if not classes:
            raise class_er.ClassNotFoundError("No classes found")
        return classes
    
    def get_class_by_id(self, class_id):
        class_ = self.class_repository.get_class_by_id(class_id)
        if not class_:
            raise class_er.ClassNotFoundError("Class not found")
        return class_
    
    def delete_class(self, class_id):
        class_ = self.get_class_by_id(class_id)
        if not class_:
            raise class_er.ClassNotFoundError("Class not found")
        if self.student_repository.count_students_in_class(class_id) > 0:
            raise class_er.ClassInUseError("Cannot delete class with students")
        sections = self.section_repository.get_sections_by_class(class_id)
        for section in sections:
            self.section_repository.delete_section(section.section_id)
        self.class_repository.delete_class(class_id)

    def get_classes_with_sections(self):
        classes = self.class_repository.get_all_classes()
        if not classes:
            raise class_er.ClassNotFoundError("No classes found")
        for class_ in classes:
            class_.sections = self.section_repository.get_sections_by_class(class_.class_id)
        return classes