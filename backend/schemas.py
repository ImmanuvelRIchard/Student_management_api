
from pydantic import BaseModel, Field, ConfigDict


# Schema for creating a student
class StudentCreate(BaseModel):

    name: str = Field(min_length=2, max_length=100)

    age: int = Field(ge=1, le=100)

    email: str = Field(min_length=5, max_length=150)

    course: str = Field(min_length=2, max_length=100)


# Schema for updating a student partially
class StudentUpdate(BaseModel):

    name: str | None = Field(default=None, min_length=2, max_length=100)

    age: int | None = Field(default=None, ge=1, le=100)

    email: str | None = Field(default=None, min_length=5, max_length=150)

    course: str | None = Field(default=None, min_length=2, max_length=100)


# Schema for returning student information
class StudentResponse(BaseModel):

    id: int
    name: str
    age: int
    email: str
    course: str

    model_config = ConfigDict(from_attributes=True)
