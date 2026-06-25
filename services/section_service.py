from repositories.section_repository import SectionRepository
from repositories.class_repository import ClassRepository
from repositories.student_repository import StudentRepository
from models.section import Section

class SectionService:
    def __init__(self):
        self.section_repository = SectionRepository()
        self.class_repository = ClassRepository()
        self.student_repository = StudentRepository()

    def add_section(self, section_name, class_id):
        if not section_name.strip():
            raise ValueError("Section name cannot be empty.")
        class_obj = self.class_repository.get_class_by_id(class_id)
        if not class_obj:
            raise ValueError(f"No class found")
        if self.section_repository.get_section_by_name(section_name, class_id):
            raise ValueError("Section already exists")
        self.section_repository.add_section(section_name, class_id)

    def get_all_sections(self):
        return self.section_repository.get_all_sections()
    
    def get_sections_by_class(self, class_id):
        return self.section_repository.get_sections_by_class(class_id)
    
    def get_section_by_id(self, section_id):
        return self.section_repository.get_section_by_id(section_id)
    
    def delete_section(self, section_id):
        section = self.get_section_by_id(section_id)
        if not section:
            raise ValueError("Section not found")
        if self.student_repository.count_students_in_section(section_id) > 0:
            raise ValueError("Cannot delete section with students")
        self.section_repository.delete_section(section_id)