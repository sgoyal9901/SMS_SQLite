from fastapi import APIRouter
from services.class_service import ClassService
from api.schemas.class_ import ClassResponse , ClassWithSectionsResponse
from fastapi import HTTPException

router = APIRouter(
    prefix="/classes",
    tags=["classes"],
)

class_service = ClassService()

@router.get("/classes", response_model=list[ClassResponse])
def get_classes():
    try:
        return class_service.get_all_classes()
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/all_classes", response_model=list[ClassWithSectionsResponse])
def get_classes_with_sections():
    try:
        return class_service.get_classes_with_sections()
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/add_class", response_model=ClassResponse)
def add_class(class_name: str):
    try:
        class_service.add_class(class_name)
        return {"class_name": class_name}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/delete_class/{class_id}")
def delete_class(class_id: int):
    try:
        class_service.delete_class(class_id)
        return {"message": "Class deleted successfully"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))