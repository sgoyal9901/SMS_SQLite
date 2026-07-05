class Exams:
    def __init__(self, exam_name, exam_id=None):
        self.exam_id = exam_id
        self.exam_name = exam_name

    def __str__(self):
        return f"{self.exam_name}"