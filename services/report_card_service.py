from repositories.exams_repo import ExamsRepository
from repositories.result_repo import ResultRepository
from repositories.class_subject_repo import ClassSubjectsRepository
from models.report_card import ReportCard


class ReportCardService:
    def __init__(self):
        self.exams_repo = ExamsRepository()
        self.result_repo = ResultRepository()
        self.class_subject_repo = ClassSubjectsRepository()

    def get_report_card(self, student_id, exam_id):
        results = self.result_repo.get_result_of_student(student_id, exam_id)
        if not results:
            raise ValueError("No results found for this student.")
        obtained_marks = 0
        for result in results:
            obtained_marks += result.marks
            subject = self.class_subject_repo.get_class_subject_by_id(result.class_subject_id)
            result.subject_name = subject.subject_name
        no_of_subjects = len(results)
        total_marks = no_of_subjects * 100
        percentage = (obtained_marks / total_marks) * 100
        return results, obtained_marks, total_marks, percentage 