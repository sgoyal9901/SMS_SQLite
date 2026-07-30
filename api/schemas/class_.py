from pydantic import BaseModel
from api.schemas.section import SectionResponse

class ClassResponse(BaseModel):
    class_name: str

class ClassWithSectionsResponse(BaseModel):
    class_name: str
    sections: list[SectionResponse]