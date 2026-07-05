from repositories.exams_repo import ExamsRepository

class ExamsService:
    def __init__(self):
        self.repo = ExamsRepository

    def add_exams(self, exam_name):
        repo = self.repo
        if not exam_name.strip():
            raise ValueError("Exam name cannot be empty.")
        if repo.get_exams_by_name(exam_name):
            raise ValueError(f"An exam with the name '{exam_name}' already exists.")
        exams_id = repo.add_exams(exam_name)
        return exams_id
    
    def get_all_exams(self):
        repo = self.repo
        exams = repo.get_all_exams()
        return exams
    
    def get_exams_by_id(self, exam_id):
        repo = self.repo
        exams = repo.get_exams_by_id(exam_id)
        return exams
    
    def get_exams_by_name(self, exam_name):
        repo = self.repo
        exams = repo.get_exams_by_name(exam_name)
        return exams
    
    def delete_exams_by_id(self, exam_id):
        repo = self.repo
        repo.delete_exams_by_id(exam_id)

    def update_exams_by_id(self, exam_id, exam_name):
        repo = self.repo
        if not exam_name.strip():
            raise ValueError("Exam name cannot be empty.")
        if repo.get_exams_by_name(exam_name):
            raise ValueError(f"An exam with the name '{exam_name}' already exists.")
        repo.update_exams_by_id(exam_id, exam_name)