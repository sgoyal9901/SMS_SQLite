from fastapi import APIRouter
from services.class_service import ClassService
from api.schemas.class_ import ClassResponse

router = APIRouter(
    prefix="/classes",
    tags=["classes"],
)

class_service = ClassService()

@router.get("/all_classes", response_model=list[ClassResponse])
def get_all_classes():
    return class_service.get_all_classes()