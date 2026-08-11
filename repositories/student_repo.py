from database.connection import get_connection
from models.student import Student

class StudentRepository:
    def generate_roll_number(self, section_id):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT MAX(roll_number) FROM students 
                WHERE section_id = ?
            ''', (section_id,))
            result = cursor.fetchone()
            max_roll_number = result[0] if result[0] is not None else 0
            return max_roll_number + 1
    
    def check_duplicate_student(self, name, father_name, contact_number):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT * FROM students 
                WHERE name = ? AND father_name = ? AND contact_number = ?
            ''', (name, father_name, contact_number))
            row = cursor.fetchone()
            return row is not None

    def add_student(self, student):
        with get_connection() as conn:
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

    def _build_student_filter(self, class_id, section_id, search):
        filters = []
        parameter = []
        if class_id:
            filters.append('classes.class_id = ?')
            parameter.append(class_id)
        if section_id:
            filters.append('sections.section_id = ?')
            parameter.append(section_id)
        if search:
            filters.append('(name LIKE ? OR father_name LIKE ?)')
            parameter.extend([f"%{search}%", f"%{search}%"])
        return filters, parameter

    def get_all_students(self, page: int=1, limit: int=20, class_id: int|None=None,\
                          section_id: int|None=None, search: str|None=None,\
                          sort: str="student_id", order: str="asc"):
        with get_connection() as conn:
            cursor = conn.cursor()
            offset = (page - 1)*limit
            quary = '''
            SELECT * FROM students
            JOIN sections ON students.section_id = sections.section_id
            JOIN classes ON sections.class_id = classes.class_id
            '''
            filters, parameter = self._build_student_filter(class_id, section_id, search)
            if filters:
                quary += ' WHERE ' + ' AND '.join(filters)
            quary += f' ORDER BY {sort} {order.upper()}'
            quary += ' LIMIT ? OFFSET ?'
            parameter.extend([limit, offset])
            cursor.execute(quary, parameter)
            rows = cursor.fetchall()
            students = []
            for row in rows:
                student = self.row_to_student(row)
                students.append(student)
            return students

    def get_all_students_count(self, class_id: int|None=None, section_id: int|None=None,\
                               search: str|None=None):
        with get_connection() as conn:
            cursor = conn.cursor()
            quary = '''
            SELECT COUNT(*) FROM students
            JOIN sections ON students.section_id = sections.section_id
            JOIN classes ON sections.class_id = classes.class_id
            '''
            filters, parameter = self._build_student_filter(class_id, section_id, search)
            if filters:
                quary += ' WHERE ' + ' AND '.join(filters)
            cursor.execute(quary, parameter)
            count = cursor.fetchone()[0]
            return count
    
    def get_student_by_id(self, student_id):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM students WHERE student_id = ?', (student_id,))
            row = cursor.fetchone()
            if row:
                student = self.row_to_student(row)
                return student
            return None

    def get_students_by_contact_number(self, contact_number):
        with get_connection() as conn:
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
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM students WHERE student_id = ?', (student_id,))
            if cursor.rowcount == 0:
                raise ValueError(f"No student found with ID {student_id}")
            conn.commit()


    def update_student(self, student):
        with get_connection() as conn:
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
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT COUNT(*) FROM students WHERE section_id = ?', (section_id,))
            count = cursor.fetchone()[0]
            return count
    
    def count_students_in_class(self, class_id):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT COUNT(*) FROM students JOIN sections \
                        ON students.section_id = sections.section_id \
                        WHERE sections.class_id = ?', (class_id,))
            count = cursor.fetchone()[0]
            return count
    
    def get_student_by_section(self, section_id):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM students WHERE section_id = ?\
                        ORDER BY roll_number', (section_id,))
            rows = cursor.fetchall()
            students = []
            for row in rows:
                student = self.row_to_student(row)
                students.append(student)
            return students
    
    def get_students_by_class_id(self, class_id):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM students JOIN sections \
                        ON students.section_id = sections.section_id \
                        WHERE sections.class_id = ?', (class_id,))
            rows = cursor.fetchall()
            students = []
            for row in rows:
                student = self.row_to_student(row)
                students.append(student)
            return students