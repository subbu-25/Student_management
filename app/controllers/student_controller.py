from app.services.student_service import StudentService
from app.models.student import Student,UpdateStudent

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
    def update_student(student_id: str, student_data: UpdateStudent):
        # Extract the fields provided in the update request
        update_data = student_data.dict(exclude_unset=True)
        existing_student = StudentService.fetch_student(student_id)

        if not existing_student:
            raise HTTPException(status_code=404, detail="Student not found")

        # Merge the provided data with the existing student data
        merged_data = {
            "name": update_data.get("name", existing_student["name"]),
            "age": update_data.get("age", existing_student["age"]),
            "address": {
                "city": existing_student["address"].get("city"),
                "country": existing_student["address"].get("country")
            }
        }

        # If address is provided in the update_data, override existing fields
        if "address" in update_data and update_data["address"] is not None:
            if "city" in update_data["address"] and update_data["address"]["city"] is not None:
                merged_data["address"]["city"] = update_data["address"]["city"]
            if "country" in update_data["address"] and update_data["address"]["country"] is not None:
                merged_data["address"]["country"] = update_data["address"]["country"]

        StudentService.update_student(student_id, merged_data)
        return {"message": "Student updated successfully"}

    @staticmethod
    def delete_student(student_id: str):
        StudentService.delete_student(student_id)
        return {}