# Student Management API

## 1. Project Overview

The Student Management API is a RESTful backend application developed using Python and FastAPI.

The application allows users to manage student information through API endpoints. It supports creating, retrieving, updating, searching, filtering and deleting student records.

## 2. Technology Stack

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| FastAPI | REST API framework |
| SQLAlchemy | Database ORM |
| SQLite | Database |
| Pydantic | Data validation |
| Uvicorn | ASGI server |
| Swagger UI | API testing and documentation |

## 3. Project Structure

```text
student_management_api/
│
├── backend/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   └── crud.py
│
├── .venv/
├── students.db
├── requirements.txt
├── .gitignore
└── README.md
```

## 4. Features

- Create student records.
- Retrieve all students.
- Retrieve individual students by ID.
- Update complete student information.
- Partially update student information.
- Delete student records.
- Search students by name.
- Filter students by course.
- Pagination using skip and limit.
- Input validation.
- Duplicate email prevention.

## 5. Installation

### Prerequisites

- Python 3.10 or later.
- Visual Studio Code or another Python editor.
- pip package manager.

### Step 1: Clone the project

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd student_management_api
```

### Step 2: Create a virtual environment

```bash
python -m venv .venv
```

### Step 3: Activate the virtual environment

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### Step 4: Install dependencies

```bash
python -m pip install -r requirements.txt
```

## 6. Run the Application

Execute:

```bash
python -m uvicorn backend.main:app --reload
```

Application URL:

http://127.0.0.1:8000

Swagger API documentation:

http://127.0.0.1:8000/docs

## 7. API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | / | Welcome message |
| POST | /students | Create student |
| GET | /students | Retrieve all students |
| GET | /students/{student_id} | Retrieve student by ID |
| PUT | /students/{student_id} | Update complete record |
| PATCH | /students/{student_id} | Partially update record |
| DELETE | /students/{student_id} | Delete student |

## 8. Sample API Request

### Create Student

POST `/students`

Request body:

```json
{
  "name": "Immanuel",
  "age": 22,
  "email": "immanuel@example.com",
  "course": "Python"
}
```

Successful response:

```json
{
  "id": 1,
  "name": "Immanuel",
  "age": 22,
  "email": "immanuel@example.com",
  "course": "Python"
}
```

HTTP status: 201 Created.

## 9. Search, Filtering and Pagination

Search by name:

`GET /students?search=Immanuel`

Filter by course:

`GET /students?course=Python`

Pagination:

`GET /students?skip=0&limit=5`

## 10. HTTP Status Codes

| Status | Meaning |
|---|---|
| 200 | Request successful |
| 201 | Student created |
| 404 | Student not found |
| 409 | Duplicate email |
| 422 | Input validation failed |

## 11. Database

The application uses SQLite for storing student information.

SQLAlchemy manages database operations through ORM models.

The database file is created automatically when the application initializes.

## 12. Project Scope

This project currently implements the backend REST API.

Frontend integration, user authentication, authorization and production deployment are outside the current scope.

## 13. Conclusion

The Student Management API demonstrates the implementation of RESTful API development using Python, FastAPI, SQLAlchemy and SQLite.

It provides fundamental student record management operations with validation, search, filtering and pagination.
