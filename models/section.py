class Section:
    def __init__(self, section_name, class_id, section_id=None):
        self.section_id = section_id
        self.section_name = section_name
        self.class_id = class_id
        
    def __str__(self):
        return f"Class: {self.class_id} {self.section_name}"