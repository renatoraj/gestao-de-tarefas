from api.dtos.task_dto import TaskDTO
from api.models.task import Task

def task_to_dto(task: Task) -> TaskDTO:
    return TaskDTO(
        id=task.id,
        title=task.title,
        description=task.description,
        is_complete=task.is_complete,
        created_at=task.created_at
    )

def dto_to_task(task_dto: TaskDTO) -> Task:
    return Task(
        id=task_dto.id,
        title=task_dto.title,
        description=task_dto.description,
        is_complete=task_dto.is_complete,
        created_at=task_dto.created_at
    )