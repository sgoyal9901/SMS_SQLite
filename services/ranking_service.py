from models.ranking import Ranking
from repositories.result_repo import ResultRepository
from repositories.student_repo import StudentRepository
from services.report_card_service import ReportCardService

class RankingService:
    def __init__(self):
        self.repo = ResultRepository()
        self.student_repo = StudentRepository()
        self.report_card_service = ReportCardService()

    def get_ranking(self, class_id, exam_id):        
        students = self.student_repo.get_students_by_class_id(class_id)
        if not students:
            raise ValueError("No students found in the class")
        report_cards = []
        for student in students:
            report_card = self.report_card_service.generate_report_card(student.student_id, exam_id)
            report_cards.append(report_card)
        rankings = report_cards.sort(key=lambda x: x.percentage, reverse=True)
        return rankings
        