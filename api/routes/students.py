from services.student_service import StudentService
from api.schemas.student import StudentCreate , StudentResponse, StudentPaginationResponse
from fastapi import APIRouter, status

router = APIRouter(
    prefix="/students",
    tags=["students"],
)
student_service = StudentService()

@router.post("", response_model=StudentResponse, status_code=status.HTTP_201_CREATED)
def add_student(student: StudentCreate):
    return student_service.add_student(student.name, student.father_name, student.section_id, \
                                        student.contact_number)

@router.get("", response_model=StudentPaginationResponse, status_code=status.HTTP_200_OK)
def get_all_students(page: int = 1, limit: int = 20, class_id: int | None = None,\
                     section_id: int | None = None, search: str | None = None,\
                     sort: str="student_id", order: str = "asc"):
    return student_service.get_all_students(page, limit, class_id, section_id, search, sort, order)

@router.get("/id/{student_id}", response_model=StudentResponse, status_code=status.HTTP_200_OK)
def get_student_by_id(student_id: int):
    return student_service.get_student_by_id(student_id)

@router.get("/contact/{contact_number}", response_model=list[StudentResponse],\
             status_code=status.HTTP_200_OK)
def get_student_by_contact_number(contact_number: str):
    return student_service.get_students_by_contact_number(contact_number)

@router.delete("/{student_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_student(student_id: int):
    student_service.delete_student(student_id)

@router.put("/{student_id}", response_model=StudentResponse, status_code=status.HTTP_200_OK)
def update_student(student_id: int, student: StudentCreate):
    return student_service.update_student(student_id, student.name, student.father_name, \
                                          student.section_id, student.contact_number)