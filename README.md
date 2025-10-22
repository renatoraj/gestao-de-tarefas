🚀 Task Management Microservice
A full-stack microservice demonstration featuring a Python Flask REST API and a .NET Console Client, showcasing multi-technology integration, clean architecture, and comprehensive testing.

📋 Project Overview
This project demonstrates a complete microservice ecosystem with:

Backend: Python Flask REST API with clean architecture

Frontend/Client: .NET Console application

Infrastructure: Docker containerization

Testing: Comprehensive unit tests for both Python and .NET

🏗️ Architecture
text
gestao-de-tarefas/
├── 📁 src/                    # Python Backend
│   ├── api/
│   │   ├── controllers/       # REST endpoints
│   │   ├── services/          # Business logic
│   │   ├── repositories/      # Data access
│   │   ├── models/            # Domain models
│   │   └── dtos/              # Data Transfer Objects
│   ├── tests/                 # Python unit tests
│   └── app.py                 # Flask application
├── 📁 clients/                # API Clients
│   └── dotnet/               # .NET Console Client
├── 🐳 docker-compose.yml      # Container orchestration
├── 📝 requirements.txt        # Python dependencies
└── 🧪 pyproject.toml          # Project configuration


✨ Features
Backend (Python/Flask)
✅ RESTful API with proper HTTP status codes

✅ Clean Architecture with separation of concerns

✅ DTO Pattern for request/response validation

✅ Global Error Handling with custom exceptions

✅ In-Memory Storage (easily swappable for PostgreSQL/MySQL)

✅ Comprehensive Unit Testing with 100% test coverage

✅ Pydantic Validation for data integrity

Client (.NET)
✅ Interactive Console Interface

✅ HTTP Client with error handling

✅ JSON Serialization/Deserialization

✅ Multi-technology integration demonstration

DevOps
✅ Docker Containerization

✅ Docker Compose for easy deployment

✅ Cross-platform compatibility


🚀 Quick Start
Prerequisites
Python 3.9+

.NET 9.0 SDK

Docker (optional)

Method 1: Local Development
Backend (Python)
bash
# Install dependencies
pip install -r requirements.txt

# Run the API
python src/app.py
Client (.NET)
bash
# Navigate to client directory
cd clients/dotnet

# Run the .NET client
dotnet run
Method 2: Docker (Recommended)
bash
# Start everything with Docker Compose
docker-compose up --build

# The API will be available at http://localhost:5000
# You can then run the .NET client separately

🧪 Testing
Python Backend Tests
bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src

# Run specific test categories
pytest tests/unit/services/    # Service layer tests
pytest tests/unit/controllers/ # Controller layer tests
.NET Client Tests
bash
cd clients/dotnet/Tests
dotnet test
Test Coverage:

✅ Python: 15+ unit tests covering services and controllers

✅ .NET: Client functionality verified manually

✅ Integration: End-to-end API consumption tested


📡 API Documentation
Endpoints
Method	Endpoint	Description	Status Codes
POST	/api/tasks	Create new task	201, 400
GET	/api/tasks	List all tasks	200
GET	/api/tasks/{id}	Get specific task	200, 404
PUT	/api/tasks/{id}	Update task	200, 400, 404
DELETE	/api/tasks/{id}	Delete task	204, 404

Example Usage
Create Task
bash
curl -X POST http://localhost:5000/api/tasks \
  -H "Content-Type: application/json" \
  -d '{"title": "Learn Python", "description": "Study Flask framework"}'
List Tasks
bash
curl http://localhost:5000/api/tasks

🛠️ Technology Stack
Backend
Python 3.9 - Runtime

Flask - Web framework

Pydantic - Data validation

Pytest - Testing framework

Client
.NET 9.0 - Runtime

HttpClient - HTTP communications

Newtonsoft.Json - JSON serialization

Infrastructure
Docker - Containerization

Docker Compose - Orchestration


🎯 Project Highlights

Clean Code Practices
✅ Separation of Concerns (Controller/Service/Repository)

✅ Dependency Injection patterns

✅ DTO/Mapper separation from entities

✅ Comprehensive error handling

✅ RESTful design principles

Testing Strategy
✅ Unit Tests for business logic

✅ Mocking of dependencies

✅ Test-driven development approach

✅ Multiple assertion scenarios

Professional Development
✅ Multi-technology integration

✅ Container-ready deployment

✅ API documentation

✅ Git version control best practices

🔄 Development Workflow
Backend First: Start Python API (python src/app.py)

Client Integration: Run .NET client (dotnet run in clients/dotnet)

Testing: Execute test suites for both components

Containerization: Use Docker for consistent environments


🤝 Contributing

Fork the repository

Create a feature branch (git checkout -b feature/amazing-feature)

Commit changes (git commit -m 'Add amazing feature')

Push to branch (git push origin feature/amazing-feature)

Open a Pull Request


🏆 Skills Demonstrated

Backend Development: Python, Flask, REST APIs, Architecture Patterns

Client Development: .NET, Console Applications, HTTP Clients

Testing: Unit Testing, Mocking, Test Coverage

DevOps: Docker, Containerization, CI/CD readiness

Software Design: Clean Architecture, Design Patterns, Code Quality

Built with ❤️ using Python, .NET, and modern development practices.
