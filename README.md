# Project Management System

A Django-based project management system that helps teams collaborate effectively. Built with Django REST Framework, this API provides endpoints for managing users, projects, tasks, and comments.

## Features

- User Authentication (JWT Tokens)
- Project Management
- Task Tracking
- Comment System
- Role-based Project Membership

## Getting Started

These instructions will help you set up the project on your local machine.

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git

### Installation

1. Clone this repository to your local machine:

```
git clone https://github.com/banothvamshi/project-management.git
cd project-management
```

2. Create a virtual environment:

```
python -m venv venv
source venv/bin/activate
```

3. Install dependencies:

```
pip install -r requirements.txt
```

4. Run migrations:

```
python manage.py makemigrations
python manage.py migrate
```

5. Create a superuser (admin):

```
python manage.py createsuperuser
```

6. Start the server:

```
python manage.py runserver
```


The API will be available at http://localhost:8000/api/

## API Endpoints

### Authentication
- `POST /api/users/register/` - Register new user
- `POST /api/users/login/` - Login and get token

### Users
- `GET /api/users/` - List users
- `GET /api/users/{id}/` - Get user details
- `PUT /api/users/{id}/` - Update user
- `DELETE /api/users/{id}/` - Delete user

### Projects
- `GET /api/projects/` - List all projects
- `POST /api/projects/` - Create new project
- `GET /api/projects/{id}/` - Get project details
- `PUT /api/projects/{id}/` - Update project
- `DELETE /api/projects/{id}/` - Delete project

### Tasks
- `GET /api/projects/{project_id}/tasks/` - List tasks in project
- `POST /api/projects/{project_id}/tasks/` - Create task
- `GET /api/tasks/{id}/` - Get task details
- `PUT /api/tasks/{id}/` - Update task
- `DELETE /api/tasks/{id}/` - Delete task

### Comments
- `GET /api/projects/{project_id}/tasks/{task_id}/comments/` - List comments
- `POST /api/projects/{project_id}/tasks/{task_id}/comments/` - Add comment
- `GET /api/comments/{id}/` - Get comment details
- `PUT /api/comments/{id}/` - Update comment
- `DELETE /api/comments/{id}/` - Delete comment

## Usage Example

1. Register a new user:

```
POST /api/users/register/
Content-Type: application/json
{"username":"testuser","password":"testpass123","email":"test@example.com"}
```

2. Login and get token:

```
POST /api/users/login/
Content-Type: application/json
{"username":"testuser","password":"testpass123"}
```


3. Create a project (use token from login):

```
POST /api/projects/
Authorization: Bearer your_token_here
Content-Type: application/json
{"name":"My Project","description":"Project description"}
```

## Tech Stack

- Django 5.1.3
- Django REST Framework 3.14.0
- Simple JWT for authentication
- SQLite (default database)


## Author

Vamshi Banoth  - [banothvamshi@gmail.com](mailto:banothvamshi@gmail.com)
