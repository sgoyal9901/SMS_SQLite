from repositories.subjects_repositories import SubjectsRepository
from repositories.class_subject_repositories import ClassSubjectsRepository
from models.subjects import Subjects

class SubjectsService:
    def __init__(self):
        self.subjects_repository = SubjectsRepository()
        self.class_subject_repository = ClassSubjectsRepository()

    def add_subject(self, subject_name):
        if not subject_name.strip():
            raise ValueError("Subject name cannot be empty.")
        if self.subjects_repository.subject_exists(subject_name):
            return False
        self.subjects_repository.add_subject(subject_name)
        return True
    
    def view_subjects(self):
        subjects = self.subjects_repository.view_subjects()
        return subjects
    
    def delete_subject(self, subject_id):
        if self.class_subject_repository.count_classes_with_subject(subject_id) > 0:
            raise ValueError("Cannot delete subject with associated classes.")
        self.subjects_repository.delete_subject(subject_id)

    def get_subject_by_id(self, subject_id):
        subject = self.subjects_repository.get_subject_by_id(subject_id)
        return subject