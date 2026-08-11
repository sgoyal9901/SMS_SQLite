from pydantic import BaseModel

class StudentCreate(BaseModel):
    name: str
    father_name: str
    section_id: int
    contact_number: str

class StudentResponse(BaseModel):
    student_id: int
    name: str
    father_name: str
    class_name: str
    section_name: str
    roll_number: int
    contact_number: str

class StudentPaginationResponse(BaseModel):
    page: int
    limit: int
    total: int
    total_pages: int
    data: list[StudentResponse]