class StudentError(Exception):
    """Base class for student exceptions."""
    pass


class StudentNotFoundError(StudentError):
    pass

class StudentAlreadyExistsError(StudentError):
    pass

class InvalidStudentDataError(StudentError):
    pass