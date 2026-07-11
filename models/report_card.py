class ReportCard:
    def __init__(self, name=None, class_name=None, section_name=None, roll_number=None, \
                 exam_name=None, subjects=None, obtained_marks=None, total_marks=None, \
                    percentage=None, grade=None):
        self.name = name
        self.class_name = class_name
        self.section_name = section_name
        self.roll_number = roll_number
        self.exam_name = exam_name
        self.subjects = subjects
        self.obtained_marks = obtained_marks
        self.total_marks = total_marks
        self.percentage = percentage
        self.grade = grade 