from fastapi import FastAPI
from app.routers import student_router

app = FastAPI()

# Register the student router
app.include_router(student_router.router)
