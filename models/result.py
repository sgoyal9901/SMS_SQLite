class Result:
    def __init__(self, student_id, class_subject_id, exam_id, marks, result_id=None, \
                 name=None, roll_number=None, class_name=None, section_name=None, \
                    subject_name=None, exam_name=None):
        self.result_id = result_id
        self.student_id = student_id
        self.class_subject_id = class_subject_id
        self.exam_id = exam_id
        self.marks = marks
        self.name = name
        self.roll_number = roll_number
        self.class_name = class_name
        self.section_name = section_name
        self.subject_name = subject_name
        self.exam_name = exam_name

    def __str__(self):
        return f'''
Roll Number: {self.roll_number}
Name: {self.name}
Marks: {self.marks}
        '''