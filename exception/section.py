class SectionError(Exception):
    pass


class SectionNotFoundError(SectionError):
    pass


class SectionAlreadyExistsError(SectionError):
    pass


class InvalidSectionDataError(SectionError):
    pass


class SectionInUseError(SectionError):
    pass