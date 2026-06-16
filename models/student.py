class Student:
    def __init__(self, name, father_name, section_id, roll_number, contact_number, student_id=None):
        self.student_id = student_id
        self.name = name
        self.father_name = father_name
        self.section_id = section_id
        self.roll_number = roll_number
        self.contact_number = contact_number

    def __str__(self):
        return f'''
Student ID: {self.student_id}
Name: {self.name}
Father's Name: {self.father_name}
Class: {self.class_name}
Section: {self.section_name}
Roll Number: {self.roll_number}
Contact Number: {self.contact_number}
            '''
    