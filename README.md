# ProManage API

ProManage is a robust task management REST API built with Django and Django REST Framework. It provides a secure and scalable backend for managing tasks and subtasks with user authentication and role-based access control.

## Features

- 🔐 JWT Authentication
- 👥 Role-based access control
- ✅ Task and subtask management
- 🔍 Full-text search capabilities
- 📚 Swagger/OpenAPI documentation
- 🚀 Production-ready configuration

## Tech Stack

- Django
- Django REST Framework
- PostgreSQL
- JWT Authentication
- Swagger/OpenAPI (drf-yasg)
- Whitenoise for static files

## Prerequisites

- Python 3.x
- PostgreSQL
- pip

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Yash114Bansal/ProManage.git
   cd ProManage
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   ```bash
   export SECRET_KEY='your-secret-key'
   export DATABASE='your-database-url'
   ```

5. Run migrations:
   ```bash
   python manage.py migrate
   ```

6. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

7. Run the development server:
   ```bash
   python manage.py runserver
   ```

## API Endpoints

### Authentication
- `POST /auth/generate/` - Generate JWT token
- `POST /auth/verify/` - Verify JWT token
- `POST /auth/refresh/` - Refresh JWT token
- `POST /auth/create/` - Create new user (Admin only)

### Tasks
- `GET /tasks/` - List all tasks
- `POST /tasks/` - Create a new task
- `GET /tasks/{id}/` - Retrieve a task
- `PUT /tasks/{id}/` - Update a task
- `DELETE /tasks/{id}/` - Delete a task
- `GET /tasks/search/{query}/` - Search tasks

## API Documentation

The API documentation is available at:
- Swagger UI: `/swagger/`
- ReDoc: `/redoc/`

## Authentication

The API uses JWT (JSON Web Token) authentication. To access protected endpoints:

1. Obtain a token using `/auth/generate/`
2. Include the token in the Authorization header:
   ```
   Authorization: Bearer <your-token>
   ```

## Permissions

- Regular users can view and update their own tasks
- Superusers have full access to all endpoints
- Only authenticated users can access the API
- Only superusers can create new users

## Models

### Task
- `user`: ForeignKey to User
- `title`: CharField (max 200 chars)
- `description`: CharField (max 1000 chars)
- `time`: DateTimeField (auto_now_add)
- `isComplete`: BooleanField
- `deadLine`: DateTimeField

### SubTask
- `task`: ForeignKey to Task
- `title`: CharField (max 200 chars)
- `description`: CharField (max 1000 chars)
- `time`: DateTimeField (auto_now_add)
- `isComplete`: BooleanField
- `deadLine`: DateTimeField