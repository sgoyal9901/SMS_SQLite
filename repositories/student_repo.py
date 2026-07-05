from database.db_manager import get_connection
from models.student import Student

class StudentRepository:
    def __init__(self):
        self.connection = get_connection()

    def generate_roll_number(self, section_id):
        conn = self.connection
        cursor = conn.cursor()
        cursor.execute('''
            SELECT MAX(roll_number) FROM students 
            WHERE section_id = ?
        ''', (section_id,))
        result = cursor.fetchone()
        max_roll_number = result[0] if result[0] is not None else 0
        return max_roll_number + 1
    
    def check_duplicate_student(self, name, father_name, contact_number):
        conn = self.connection
        cursor = conn.cursor()
        cursor.execute('''
            SELECT * FROM students 
            WHERE name = ? AND father_name = ? AND contact_number = ?
        ''', (name, father_name, contact_number))
        row = cursor.fetchone()
        return row is not None

    def add_student(self, student):
        conn = self.connection
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO students (name, father_name, section_id, roll_number, contact_number)
            VALUES (?, ?, ?, ?, ?)
        ''', 
        (
            student.name, student.father_name,  student.section_id, student.roll_number, 
            student.contact_number
        ))
        conn.commit()
        student_id = cursor.lastrowid
        return student_id
    
    def row_to_student(self, row):
        return Student(
            student_id=row[0],
            name=row[1],
            father_name=row[2],
            section_id=row[3],
            roll_number=row[4],
            contact_number=row[5]
        )

    def get_all_students(self):
        conn = self.connection
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM students')
        rows = cursor.fetchall()
        students = []
        for row in rows:
            student = self.row_to_student(row)
            students.append(student)
        return students
    
    def get_student_by_id(self, student_id):
        conn = self.connection
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM students WHERE student_id = ?', (student_id,))
        row = cursor.fetchone()
        if row:
            student = self.row_to_student(row)
            return student
        return None

    def get_students_by_contact_number(self, contact_number):
        conn = self.connection
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM students WHERE contact_number = ?', (contact_number,))
        rows = cursor.fetchall()
        students = []
        for row in rows:
            student = self.row_to_student(row)
            students.append(student)
        if not students:
            return None
        return students
    
    def delete_student(self, student_id):
        conn = self.connection
        cursor = conn.cursor()
        cursor.execute('DELETE FROM students WHERE student_id = ?', (student_id,))
        if cursor.rowcount == 0:
            raise ValueError(f"No student found with ID {student_id}")
        conn.commit()


    def update_student(self, student):
        conn = self.connection
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE students
            SET 
                       name = ?, father_name = ?, section_id = ?, 
                       roll_number = ?, contact_number = ?
            WHERE 
                       student_id = ?
        ''', 
        (
            student.name, student.father_name, student.section_id, 
            student.roll_number, student.contact_number, student.student_id
        ))
        if cursor.rowcount == 0:
            raise ValueError(f"No student found with ID {student.student_id}")
        conn.commit()

    def count_students_in_section(self, section_id):
        conn = self.connection
        cursor = conn.cursor()
        cursor.execute('SELECT COUNT(*) FROM students WHERE section_id = ?', (section_id,))
        count = cursor.fetchone()[0]
        return count
    
    def count_students_in_class(self, class_id):
        conn = self.connection
        cursor = conn.cursor()
        cursor.execute('SELECT COUNT(*) FROM students JOIN sections \
                       ON students.section_id = sections.section_id \
                       WHERE sections.class_id = ?', (class_id,))
        count = cursor.fetchone()[0]
        return count
    
    def get_student_by_section(self, section_id):
        conn = self.connection
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM students WHERE section_id = ?\
                       ORDER BY roll_number', (section_id,))
        rows = cursor.fetchall()
        students = []
        for row in rows:
            student = self.row_to_student(row)
            students.append(student)
        return students