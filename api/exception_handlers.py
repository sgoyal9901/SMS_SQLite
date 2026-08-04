from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
import exception.student as student
import exception.class_ as class_
import exception.section as section

def register_exception_handlers(app: FastAPI):
    @app.exception_handler(student.StudentNotFoundError)
    def handle_student_not_found(request: Request, exc: student.StudentNotFoundError):
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"detail": str(exc)}
        )

    @app.exception_handler(student.StudentAlreadyExistsError)
    def handle_student_already_exists(request: Request, exc: student.StudentAlreadyExistsError):
        return JSONResponse(
            status_code=status.HTTP_409_CONFLICT,
            content={"detail": str(exc)}
        )

    @app.exception_handler(ValueError)
    def handle_value_error(request: Request, exc: ValueError):
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"detail": str(exc)}
        )

    @app.exception_handler(class_.ClassNotFoundError)
    def handle_class_not_found(request: Request, exc: class_.ClassNotFoundError):
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"detail": str(exc)}
        )

    @app.exception_handler(class_.ClassAlreadyExistsError)
    def handle_class_already_exists(request: Request, exc: class_.ClassAlreadyExistsError):
        return JSONResponse(
            status_code=status.HTTP_409_CONFLICT,
            content={"detail": str(exc)}
        )

    @app.exception_handler(class_.InvalidClassDataError)
    def handle_invalid_class_data(request: Request, exc: class_.InvalidClassDataError):
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"detail": str(exc)}
    )

    @app.exception_handler(class_.ClassInUseError)
    def handle_class_in_use(request: Request, exc: class_.ClassInUseError):
        return JSONResponse(
            status_code=status.HTTP_409_CONFLICT,
            content={"detail": str(exc)}
    )

    @app.exception_handler(section.SectionNotFoundError)
    def handle_section_not_found(request: Request, exc: section.SectionNotFoundError):
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"detail": str(exc)}
        )

    @app.exception_handler(section.SectionAlreadyExistsError)
    def handle_section_already_exists(request: Request, exc: section.SectionAlreadyExistsError):
        return JSONResponse(
            status_code=status.HTTP_409_CONFLICT,
            content={"detail": str(exc)}
        )

    @app.exception_handler(section.InvalidSectionDataError)
    def handle_invalid_section_data(request: Request, exc: section.InvalidSectionDataError):
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"detail": str(exc)}
    )

    @app.exception_handler(section.SectionInUseError)
    def handle_section_in_use(request: Request, exc: section.SectionInUseError):
        return JSONResponse(
            status_code=status.HTTP_409_CONFLICT,
            content={"detail": str(exc)}
    )