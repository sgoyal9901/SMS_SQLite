from database.init_db import initialize_database
from services.student_service import StudentService
from schemas.student import StudentCreate
from fastapi import FastAPI

initialize_database()
app = FastAPI()
student_service = StudentService()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/get_all_students")
def get_all_students():
    return student_service.get_all_students()

@app.post("/add_student")
def add_student(student: StudentCreate):
    return student_service.add_student(
        name=student.name,
        father_name=student.father_name,
        section_id=student.section_id,
        contact_number=student.contact_number
    )
