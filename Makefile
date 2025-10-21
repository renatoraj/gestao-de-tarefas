# Makefile for the Todo Microservice Project

.PHONY: run build test

run:
	@echo "Running the Todo Microservice..."
	FLASK_APP=src/app.py flask run

build:
	@echo "Building the Docker image..."
	docker build -t todo-microservice-python .

test:
	@echo "Running unit tests..."
	pytest src/tests/unit --maxfail=1 --disable-warnings -q

docker-compose:
	@echo "Starting services with Docker Compose..."
	docker-compose up -d

docker-compose-down:
	@echo "Stopping services with Docker Compose..."
	docker-compose down