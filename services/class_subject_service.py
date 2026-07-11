from repositories.class_subject_repo import ClassSubjectsRepository
from repositories.subjects_repo import SubjectsRepository

class ClassSubjectsService:
    def __init__(self):
        self.class_subject_repository = ClassSubjectsRepository()
        self.subjects_repository = SubjectsRepository()

    def add_subject_to_class(self, class_id, subject_id):
        if self.subject_exist_in_class(class_id, subject_id):
            return False
        self.class_subject_repository.add_class_subject(class_id, subject_id)
        return True
    
    def view_subjects_by_class(self, class_id):
        return self.class_subject_repository.view_subjects_by_class(class_id)
    
    def delete_subject_from_class(self, class_id, subject_id):
        self.class_subject_repository.delete_subject_from_class(class_id, subject_id)

    def subject_exist_in_class(self, class_id, subject_id):
        return self.class_subject_repository.subject_exist_in_class(class_id, subject_id)
    