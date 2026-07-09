from repositories.result_repo import ResultRepository
import utils.validators as val

class ResultService:
    def __init__(self):
        self.repo = ResultRepository()

    def add_result(self, result):
        repo = self.repo
        val.val_marks(result.marks)
        val.val_student_id(result.student_id)
        val.val_class_subject_id(result.class_subject_id)
        val.val_exam_id(result.exam_id)
        exiting_result = repo.check_existing_result(result.student_id, result.class_subject_id, result.exam_id)
        if exiting_result:
            raise ValueError(f"Result already exists for this student.")
        result_id = repo.add_result(result)
        return result_id
    
    def get_result_by_student_id (self, student_id):
        val.val_student_id(student_id)
        repo = self.repo
        result = repo.get_result_by_student_id(student_id)
        return result

    def get_result_by_class_subject_id(self, class_subject_id):
        repo = self.repo
        result = repo.get_result_by_class_subject_id(class_subject_id)
        return result
    
    def get_result_by_exam_id(self, exam_id):
        repo = self.repo
        result = repo.get_result_by_exam_id(exam_id)
        return result
     
    
    def update_result_by_id(self, result_id, marks):
        val.val_marks(marks)
        repo = self.repo
        repo.update_result_by_id(result_id, marks)
        return
    
    def delete_result_by_id(self, result_id):
        repo = self.repo
        repo.delete_result_by_id(result_id)
        return
    
    def check_existing_result(self, student_id, class_subject_id, exam_id):
        repo = self.repo
        result = repo.check_existing_result(student_id, class_subject_id, exam_id)
        return result
    
    def get_result_id_by_data(self, student_id, class_subject_id, exam_id):
        repo = self.repo
        result_id = repo.get_result_id_by_data(student_id, class_subject_id, exam_id)
        return result_id