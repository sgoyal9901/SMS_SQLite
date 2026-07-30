from services.student_service import StudentService
from api.schemas.student import StudentCreate , StudentResponse
from fastapi import APIRouter
from fastapi import HTTPException

router = APIRouter(
    prefix="/students",
    tags=["students"],
)
student_service = StudentService()

@router.post("/add_student", response_model=StudentResponse)
def add_student(student: StudentCreate):
    try:
        return student_service.add_student(student.name, student.father_name, student.section_id, \
                                           student.contact_number)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/all_students", response_model=list[StudentResponse])
def get_all_students():
    return student_service.get_all_students()

@router.get("/student/{student_id}", response_model=StudentResponse)
def get_student_by_id(student_id: int):
    try:
        return student_service.get_student_by_id(student_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/student/{contact_number}", response_model=list[StudentResponse])
def get_student_by_contact_number(contact_number: str):    
    try:
        return student_service.get_students_by_contact_number(contact_number)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/delete_student/{student_id}")
def delete_student(student_id: int):
    try:
        student_service.delete_student(student_id)
        return {"message": "Student deleted successfully"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/update_student/{student_id}", response_model=StudentResponse)
def update_student(student_id: int, student: StudentCreate):
    try:
        return student_service.update_student(student_id, student.name, student.father_name, \
                                              student.section_id, student.contact_number)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))