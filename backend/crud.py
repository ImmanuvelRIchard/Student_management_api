
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from backend import models, schemas


# CREATE STUDENT
def create_student(db: Session, student: schemas.StudentCreate):

    new_student = models.Student(**student.model_dump())

    try:
        db.add(new_student)
        db.commit()
        db.refresh(new_student)

        return new_student

    except IntegrityError:
        db.rollback()
        return False


# GET ALL STUDENTS WITH SEARCH, FILTER AND PAGINATION
def get_students(
    db: Session,
    search: str | None = None,
    course: str | None = None,
    skip: int = 0,
    limit: int = 10
):

    query = db.query(models.Student)

    if search:
        query = query.filter(
            models.Student.name.ilike(f"%{search}%")
        )

    if course:
        query = query.filter(
            models.Student.course.ilike(f"%{course}%")
        )

    return query.offset(skip).limit(limit).all()


# GET STUDENT BY ID
def get_student(db: Session, student_id: int):

    return db.query(models.Student).filter(
        models.Student.id == student_id
    ).first()


# UPDATE STUDENT
def update_student(
    db: Session,
    student_id: int,
    student: schemas.StudentCreate
):

    db_student = get_student(db, student_id)

    if db_student is None:
        return None

    update_data = student.model_dump()

    try:
        for key, value in update_data.items():
            setattr(db_student, key, value)

        db.commit()
        db.refresh(db_student)

        return db_student

    except IntegrityError:
        db.rollback()
        return False


# PARTIAL UPDATE STUDENT
def partial_update_student(
    db: Session,
    student_id: int,
    student: schemas.StudentUpdate
):

    db_student = get_student(db, student_id)

    if db_student is None:
        return None

    update_data = student.model_dump(
        exclude_unset=True,
        exclude_none=True
    )

    if not update_data:
        return db_student

    try:
        for key, value in update_data.items():
            setattr(db_student, key, value)

        db.commit()
        db.refresh(db_student)

        return db_student

    except IntegrityError:
        db.rollback()
        return False


# DELETE STUDENT
def delete_student(db: Session, student_id: int):

    db_student = get_student(db, student_id)

    if db_student is None:
        return None

    db.delete(db_student)
    db.commit()

    return db_student
