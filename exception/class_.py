class ClassError(Exception):
    """Base class for class exceptions."""
    pass

class ClassNotFoundError(ClassError):
    pass

class ClassAlreadyExistsError(ClassError):
    pass

class InvalidClassDataError(ClassError):
    pass

class ClassInUseError(ClassError):
    pass