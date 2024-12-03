from bson import ObjectId
from fastapi import HTTPException
from app.database import db

class StudentService:
    @staticmethod
    def create_student(student_data: dict):
        result = db.students.insert_one(student_data)
        return {"id": str(result.inserted_id)}

    @staticmethod
    def list_students(country: str = None, age: int = None):
        query = {}
        if country:
            query["address.country"] = country
        if age:
            query["age"] = {"$gte": age}
        students = list(db.students.find(query))
        return [
            {
                "name": student["name"],
                "age": student["age"]
            }
            for student in students
        ]

    @staticmethod
    def fetch_student(student_id: str):
        student = db.students.find_one({"_id": ObjectId(student_id)})
        if not student:
            raise HTTPException(status_code=404, detail="Student not found")
        del student["_id"]
        return {
            "name": student["name"],
            "age": student["age"],
            "address": student["address"]
        }

    @staticmethod
    def update_student(student_id: str, student: dict):
        result = db.students.update_one({"_id": ObjectId(student_id)}, {"$set": student})
        if result.matched_count == 0:
            raise HTTPException(status_code=404, detail="Student not found")

    @staticmethod
    def delete_student(student_id: str):
        result = db.students.delete_one({"_id": ObjectId(student_id)})
        if result.deleted_count == 0:
            raise HTTPException(status_code=404, detail="Student not found")
