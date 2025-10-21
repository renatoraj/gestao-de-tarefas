from datetime import datetime
import uuid
from api.repositories.memory_repository import MemoryRepository

class TaskService:
    def __init__(self, repository=None):
        self.repository = repository or MemoryRepository()

    def create_task(self, title, description=''):
        task_id = str(uuid.uuid4())
        task = {
            "id": task_id,
            "title": title,
            "description": description,
            "is_complete": False,
            "created_at": datetime.now().isoformat()
        }
        self.repository.add(task)
        return task

    def get_all_tasks(self):
        return self.repository.get_all()

    def update_task(self, task_id, is_complete):
        task = self.repository.get(task_id)
        if task:
            task['is_complete'] = is_complete
            return task
        return None

    def delete_task(self, task_id):
        return self.repository.delete(task_id)