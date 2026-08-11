class SectionError(Exception):
    pass


class SectionNotFoundError(SectionError):
    pass


class DuplicateSectionError(SectionError):
    pass


class InvalidSectionDataError(SectionError):
    pass


class SectionInUseError(SectionError):
    pass