from repositories.section_repo import SectionRepository
from repositories.class_repo import ClassRepository
from repositories.student_repo import StudentRepository
from models.section import Section
import exceptions.section as section_er
import exceptions.class_ as class_er

class SectionService:
    def __init__(self):
        self.section_repository = SectionRepository()
        self.class_repository = ClassRepository()
        self.student_repository = StudentRepository()

    def add_section(self, section_name, class_id):
        if not section_name.strip():
            raise section_er.InvalidSectionDataError("Section name cannot be empty.")
        class_obj = self.class_repository.get_class_by_id(class_id)
        if not class_obj:
            raise class_er.ClassNotFoundError("No class found")
        if self.section_repository.get_section_by_name(section_name, class_id):
            raise section_er.DuplicateSectionError("Section already exists")
        self.section_repository.add_section(section_name, class_id)

    def get_all_sections(self):
        sections = self.section_repository.get_all_sections()
        if not sections:
            raise section_er.SectionNotFoundError("No sections found")
        return sections
    
    def get_sections_by_class(self, class_id):
        sections = self.section_repository.get_sections_by_class(class_id)
        if not sections:
            raise section_er.SectionNotFoundError("No sections found")
        return sections
    
    def get_section_by_id(self, section_id):
        section = self.section_repository.get_section_by_id(section_id)
        if not section:
            raise section_er.SectionNotFoundError("No section found")
        return section
    
    def delete_section(self, section_id):
        section = self.get_section_by_id(section_id)
        if not section:
            raise section_er.SectionNotFoundError("Section not found")
        if self.student_repository.count_students_in_section(section_id) > 0:
            raise section_er.SectionInUseError("Cannot delete section with students")
        self.section_repository.delete_section(section_id)