from fastapi import FastAPI, Depends, HTTPException, status, Query
from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session

from backend.database import engine, Base, get_db
from backend import models, schemas, crud


# Create database tables
models.Base.metadata.create_all(bind=engine)


# Create FastAPI application
app = FastAPI(title="Student Management API")


# HOME PAGE
@app.get("/")
def home():
    return {
        "message": "Welcome to Student Management API",
        "status": "Backend is running"
    }



# CREATE - Add a new student
@app.post(
    "/students",
    response_model=schemas.StudentResponse,
    status_code=status.HTTP_201_CREATED
)
def create_student(
    student: schemas.StudentCreate,
    db: Session = Depends(get_db)
):
    new_student = crud.create_student(db, student)

    if new_student is None:
        raise HTTPException(
            status_code=409,
            detail="Email already registered"
        )

    return new_student


# READ - Get all students

# GET - Search, filter and paginate students
@app.get("/students", response_model=list[schemas.StudentResponse])
def get_students(
    search: str | None = None,
    course: str | None = None,
    skip: int = Query(default=0, ge=0),
    limit: int = Query(default=10, ge=1, le=100),
    db: Session = Depends(get_db)
):
    return crud.get_students(
        db=db,
        search=search,
        course=course,
        skip=skip,
        limit=limit
    )


# READ - Get student by ID
@app.get("/students/{student_id}",
         response_model=schemas.StudentResponse)
def get_student(student_id: int, db: Session = Depends(get_db)):
    student = crud.get_student(db, student_id)

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return student


# UPDATE - Update student details
@app.put("/students/{student_id}",
         response_model=schemas.StudentResponse)
def update_student(
    student_id: int,
    student: schemas.StudentCreate,
    db: Session = Depends(get_db)
):
    updated_student = crud.update_student(
        db, student_id, student
    )

    if updated_student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return updated_student


# DELETE - Delete student
@app.delete("/students/{student_id}")
def delete_student(
    student_id: int,
    db: Session = Depends(get_db)
):
    deleted_student = crud.delete_student(db, student_id)

    if deleted_student is None:
        raise HTTPException(
            status_code=404,
            detail="Sorry, student not found"
        )

    return {
        "message": "AWW !! Student deleted successfully"
    }

# PATCH - Update selected student fields
@app.patch(
    "/students/{student_id}",
    response_model=schemas.StudentResponse
)
def partial_update_student(
    student_id: int,
    student: schemas.StudentUpdate,
    db: Session = Depends(get_db)
):
    if not student.model_fields_set:
        raise HTTPException(
            status_code=400,
            detail="Provide at least one field to update"
        )

    updated_student = crud.partial_update_student(
        db, student_id, student
    )

    if updated_student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found or no valid updates provided"
        )

    if updated_student is False:
        raise HTTPException(
            status_code=409,
            detail="Email already registered"
        )

    return updated_student
