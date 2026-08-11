from fastapi import FastAPI
from api.routes.students import router as student_router
from api.routes.classes import router as class_router
from api.routes.sections import router as section_router
from api.exception_handlers import register_exception_handlers
from api.middleware import register_middleware

app = FastAPI(
    title="School Management System",
    version="1.0.0"
)

register_exception_handlers(app)
register_middleware(app)
app.include_router(student_router, prefix="/api/v1")
app.include_router(class_router, prefix="/api/v1")
app.include_router(section_router, prefix="/api/v1")