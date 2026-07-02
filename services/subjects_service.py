from repositories.subjects_repositories import SubjectsRepository
from models.subjects import Subjects

class SubjectsService:
    def __init__(self):
        self.subjects_repository = SubjectsRepository()

    def add_subject(self, subject_name):
        if not subject_name.strip():
            raise ValueError("Subject name cannot be empty.")
        if self.subjects_repository.get_subject_by_name(subject_name):
            raise ValueError("Subject already exists")
        subject_id = self.subjects_repository.add_subject(subject_name)
        return subject_id
    
    def view_subjects(self):
        subjects = self.subjects_repository.view_subjects()
        return subjects
    
    def delete_subject(self, subject_id):
        self.subjects_repository.delete_subject(subject_id)

    def get_subject_by_id(self, subject_id):
        subject = self.subjects_repository.get_subject_by_id(subject_id)
        return subject