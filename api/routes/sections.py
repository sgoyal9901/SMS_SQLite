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