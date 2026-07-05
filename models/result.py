class Result:
    def __init__(self, student_id, subject_id, exam_id, marks, result_id=None):
        self.result_id = result_id
        self.student_id = student_id
        self.subject_id = subject_id
        self.exam_id = exam_id
        self.marks = marks