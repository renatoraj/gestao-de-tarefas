from typing import List, Optional
from api.models.task import Task

class MemoryRepository:
    def __init__(self):
        self._tasks = {}
    
    def add(self, task: Task) -> None:
        self._tasks[task.id] = task
    
    def get(self, task_id: str) -> Optional[Task]:
        return self._tasks.get(task_id)
    
    def get_all(self) -> List[Task]:
        return list(self._tasks.values())
    
    def update(self, task: Task) -> None:
        if task.id in self._tasks:
            self._tasks[task.id] = task
    
    def delete(self, task_id: str) -> bool:
        if task_id in self._tasks:
            del self._tasks[task_id]
            return True
        return False