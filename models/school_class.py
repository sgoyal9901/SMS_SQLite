class SchoolClass:
    def __init__(self, class_name, class_id=None):
        self.class_id = class_id
        self.class_name = class_name

    def __str__(self):
        return f"Class: {self.class_name}"