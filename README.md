# Task Management Microservice

This project is a simple Task Management (To-Do List) REST API built using Python and Flask. It demonstrates the core principles of back-end development, including API design, data persistence, and unit testing. The project is structured to allow easy integration with a .NET client and can be run using Docker.

## Features

- **RESTful API**: Implements endpoints for creating, reading, updating, and deleting tasks.
- **In-Memory Data Storage**: Uses an in-memory repository for simplicity, with the option to switch to PostgreSQL/MySQL.
- **DTOs**: Utilizes Data Transfer Objects (DTOs) to separate the API layer from the data model.
- **Error Handling**: Global error handling to provide standardized error responses.
- **Unit Testing**: Includes unit tests for service and controller layers to ensure code quality.
- **Docker Support**: Comes with a Dockerfile and Docker Compose configuration for easy deployment.

## Getting Started

### Prerequisites

- Python 3.x
- Docker (optional, for containerization)
- .NET SDK (for the .NET client)

### Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   ```

2. Install Python dependencies:
   ```
   pip install -r requirements.txt
   ```

### Running the Application

To run the application locally:
```
python src/app.py
```

To run the application using Docker:
```
docker-compose up --build
```

### Running Tests

To run the unit tests:
```
pytest src/tests/unit
```

## API Endpoints

- `POST /api/tasks`: Create a new task
- `GET /api/tasks`: List all tasks
- `PUT /api/tasks/<task_id>`: Update task status
- `DELETE /api/tasks/<task_id>`: Delete a task