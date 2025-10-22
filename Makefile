.PHONY: build run test clean

build:
	docker-compose build

run:
	docker-compose up

dev:
	docker-compose up --build

down:
	docker-compose down

test:
	docker-compose run --rm todo-api pytest

clean:
	docker-compose down -v
	docker system prune -f