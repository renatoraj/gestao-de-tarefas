from datetime import datetime
import uuid
from api.repositories.memory_repository import MemoryRepository
from api.models.task import Task
from api.dtos.task_dto import TaskCreateDTO, TaskUpdateDTO
from api.exceptions import TaskNotFoundException

class TaskService:
    def __init__(self, repository=None):
        self.repository = repository or MemoryRepository()

    def create_task(self, task_dto: TaskCreateDTO) -> Task:
        task_id = str(uuid.uuid4())
        task = Task(
            id=task_id,
            title=task_dto.title,
            description=task_dto.description,
            is_complete=False,
            created_at=datetime.now()
        )
        self.repository.add(task)
        return task

    def list_tasks(self) -> list[Task]:
        return self.repository.get_all()

    def get_task(self, task_id: str) -> Task:
        task = self.repository.get(task_id)
        if not task:
            raise TaskNotFoundException(f"Task with id {task_id} not found")
        return task

    def update_task(self, task_id: str, task_dto: TaskUpdateDTO) -> Task:
        task = self.get_task(task_id)
        
        # Atualiza apenas os campos fornecidos
        if task_dto.title is not None:
            task.title = task_dto.title
        if task_dto.description is not None:
            task.description = task_dto.description
        if task_dto.is_complete is not None:
            task.is_complete = task_dto.is_complete
            
        self.repository.update(task)
        return task

    def delete_task(self, task_id: str) -> bool:
        task = self.repository.get(task_id)
        if not task:
            raise TaskNotFoundException(f"Task with id {task_id} not found")
        return self.repository.delete(task_id)