class StudentError(Exception):
    """Base class for student exceptions."""
    pass


class StudentNotFoundError(StudentError):
    pass

class DuplicateStudentError(StudentError):
    pass

class InvalidStudentDataError(StudentError):
    pass