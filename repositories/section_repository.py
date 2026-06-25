from database.db_manager import get_connection
from models.section import Section

class SectionRepository:
    def __init__(self):
        self.connection = get_connection()

    def add_section(self, section_name, class_id):
        conn = self.connection
        cursor = conn.cursor()
        cursor.execute('INSERT INTO sections (section_name, class_id) \
                        VALUES (?, ?)', (section_name, class_id))
        conn.commit()

    def get_section_by_name(self, section_name, class_id):
        conn = self.connection
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM sections WHERE section_name = ? AND class_id = ?', (section_name, class_id))
        row = cursor.fetchone()
        if row:
            section = self.rows_to_section(row)
            return section
        return None

    def get_all_sections(self):
        conn = self.connection
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM sections')
        rows = cursor.fetchall()
        sections = []
        for row in rows:
            section = self.rows_to_section(row)
            sections.append(section)
        return sections
    
    def rows_to_section(self, row):
        return Section(
            section_id=row[0],
            section_name=row[1],
            class_id=row[2]
        )
    
    def get_section_by_id(self, section_id):
        conn = self.connection
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM sections WHERE section_id = ?', (section_id,))
        row = cursor.fetchone()
        if row:
            section = self.rows_to_section(row)
            return section
        return None
    
    def get_sections_by_class(self, class_id):
        conn = self.connection
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM sections WHERE class_id = ?', (class_id,))
        rows = cursor.fetchall()
        sections = []
        for row in rows:
            section = self.rows_to_section(row)
            sections.append(section)
        return sections
    
    def delete_section(self, section_id):
        conn = self.connection
        cursor = conn.cursor()
        cursor.execute('DELETE FROM sections WHERE section_id = ?', (section_id,))
        if cursor.rowcount == 0:
            raise ValueError(f"No section found with ID {section_id}")
        conn.commit()