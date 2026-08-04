from pydantic import BaseModel

class SectionResponse(BaseModel):
    section_name: str

class SectionCreate(BaseModel):
    class_id: int
    section_name: str