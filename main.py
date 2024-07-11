from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from database import create_connection, create_student, get_students, get_student_by_id, update_student, delete_student

app = FastAPI()

#Create database connection.
connection = create_connection()

#This is kind of POJO.
class Student(BaseModel):
    name: str
    age: int
    grade: str

#Endpoint of POST API to create new record.
@app.post("/students/")
def api_create_student(student: Student):
    create_student(connection, student.name, student.age, student.grade)
    return {"message": "Student Created successfully"}

#Endpoint of GET API to get all records.
@app.get("/students/")
def api_get_students():
    students = get_students(connection)
    return students

#Endpoint of GET API BY ID to get particular record.
@app.get("/students/{student_id}")
def api_get_student(student_id: int):
    student = get_student_by_id(connection, student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

#Endpoint of PUT API to update particular record in database.
@app.put("/students/{student_id}")
def api_update_student(student_id: int, student: Student):
    update_student(connection, student_id, student.name, student.age, student.grade)
    return {"message": "Student Updated Successfully"}

#Endpoint to delete particular record in database.
@app.delete("/students/{student_id}")
def api_delete_student(student_id: int):
    delete_student(connection, student_id)
    return {"Message": "Student Deleted Successfully"}