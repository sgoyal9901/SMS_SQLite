from repositories.exams_repo import ExamsRepository
from repositories.result_repo import ResultRepository
from repositories.class_subject_repo import ClassSubjectsRepository
from services.student_service import StudentService
from models.report_card import ReportCard


class ReportCardService:
    def __init__(self):
        self.exams_repo = ExamsRepository()
        self.result_repo = ResultRepository()
        self.class_subject_repo = ClassSubjectsRepository()
        self.report_card = ReportCard()
        self.student_service = StudentService()

    def generate_report_card(self, student_id, exam_id):
        student = self.student_service.get_student_by_id(student_id)
        results = self.result_repo.get_result_of_student(student_id, exam_id)
        if not results:
            raise ValueError("No results found for this student.")
        subject_results = []
        obtained_marks = 0
        for result in results:
            result.subject_name = self.class_subject_repo.\
                get_class_subject_by_id(result.class_subject_id).subject_name
            obtained_marks += result.marks
            subject_results.append(
                (result.subject_name, result.marks)
            )
        no_of_subjects = len(results)
        total_marks = no_of_subjects * 100
        percentage = (obtained_marks / total_marks) * 100
        if percentage > 90:
            grade = "A"
        elif percentage > 80:
            grade = "B"
        elif percentage > 70:
            grade = "C"
        elif percentage > 60:
            grade = "D"
        elif percentage > 50:
            grade = "E"
        else:
            grade = "F"
        report = self.report_card
        report.name = student.name
        report.class_name = student.class_name
        report.section_name = student.section_name
        report.roll_number = student.roll_number
        report.exam_name = self.exams_repo.get_exams_by_id(exam_id).exam_name
        report.subject_results = results
        report.obtained_marks = obtained_marks
        report.total_marks = total_marks
        report.percentage = percentage
        report.grade = grade
        return report