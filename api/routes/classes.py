from fastapi import APIRouter
from services.class_service import ClassService
from api.schemas.class_ import ClassResponse , ClassWithSectionsResponse , ClassCreate

router = APIRouter(
    prefix="/classes",
    tags=["classes"],
)

class_service = ClassService()

@router.get("", response_model=list[ClassResponse])
def get_classes():
    return class_service.get_all_classes()

@router.get("/with_sections", response_model=list[ClassWithSectionsResponse])
def get_classes_with_sections():
    return class_service.get_classes_with_sections()

@router.post("", response_model=ClassResponse)
def add_class(class_name: ClassCreate):
    class_service.add_class(class_name)
    return {"class_name": class_name}
    
@router.delete("/{class_id}")
def delete_class(class_id: int):
    class_service.delete_class(class_id)
    return {"message": "Class deleted successfully"}