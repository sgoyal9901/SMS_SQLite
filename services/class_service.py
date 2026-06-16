from repositories.class_repository import ClassRepository
from models.school_class import SchoolClass

class ClassService:
    def __init__(self):
        self.class_repository = ClassRepository()

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