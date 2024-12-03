from typing import Optional,List
from pydantic import BaseModel

class Address(BaseModel):
    city: Optional[str] = None
    country: Optional[str] = None

class Student(BaseModel):
    name: str
    age: int
    address: Address

class StudentResponse(BaseModel):
    name: str
    age: int
class StudentsListResponse(BaseModel):
    data: List[StudentResponse]

class CreateStudentResponse(BaseModel):
    id: str
# Schema for partial updates
class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    address: Optional[Address] = None