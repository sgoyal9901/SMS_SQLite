from pydantic import BaseModel

class StudentCreate(BaseModel):
    name: str
    father_name: str
    section_id: int
    contact_number: str