from fastapi import APIRouter
from app.controllers.student_controller import StudentController
from app.models.student import Student,UpdateStudent,StudentsListResponse,CreateStudentResponse



router = APIRouter()

@router.post("/students", response_model=CreateStudentResponse, status_code=201)
async def create_student(student: Student):
    return StudentController.create_student(student)

@router.get("/students", response_model=StudentsListResponse, status_code=200)
async def list_students(country: str = None, age: int = None):
    return StudentController.list_students(country, age)

@router.get("/students/{id}", response_model=Student, status_code=200)
async def fetch_student(id: str):
    return StudentController.fetch_student(id)

@router.patch("/students/{id}", status_code=204)
async def update_student(id: str, student: UpdateStudent):
    
     StudentController.update_student(id, student)
     return {}

@router.delete("/students/{id}",response_model=dict, status_code=200)
async def delete_student(id: str):
    return StudentController.delete_student(id)