from app.services.student_service import StudentService
from app.models.student import Student

class StudentController:
    @staticmethod
    def create_student(student: Student):
        student_data = student.dict()
        return StudentService.create_student(student_data)

    @staticmethod
    def list_students(country: str = None, age: int = None):
        return {"data": StudentService.list_students(country, age)}

    @staticmethod
    def fetch_student(student_id: str):
        student= StudentService.fetch_student(student_id)
        return {
            "name": student["name"],
            "age": student["age"],
            "address": {
                "city": student["address"]["city"],
                "country": student["address"]["country"]
            }
        }

    @staticmethod
    def update_student(student_id: str, student_data: dict):
        update_data = {k: v for k, v in student_data.dict().items() if v is not None}
        StudentService.update_student(student_id, update_data)
        return {}

    @staticmethod
    def delete_student(student_id: str):
        StudentService.delete_student(student_id)
        return {}
