from fastapi import APIRouter
from services.section_service import SectionService
from api.schemas.section import SectionResponse

router = APIRouter(
    prefix="/sections",
    tags=["sections"],
)

section_service = SectionService()

@router.get("/sections_by_class/{class_id}", response_model=list[SectionResponse])
def get_sections_by_class(class_id: int):
    return section_service.get_sections_by_class(class_id)

@router.post("/add_section", response_model=SectionResponse)
def add_section(section_name: str, class_id: int):
    section_service.add_section(section_name, class_id)
    return {"section_name": section_name}

@router.delete("/delete_section/{section_id}")
def delete_section(section_id: int):
    section_service.delete_section(section_id)
    return {"message": "Section deleted successfully"}