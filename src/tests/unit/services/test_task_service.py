from unittest import TestCase
from unittest.mock import MagicMock
from src.api.services.task_service import TaskService
from src.api.repositories.memory_repository import MemoryRepository
from src.api.dtos.task_dto import TaskDTO

class TestTaskService(TestCase):
    def setUp(self):
        self.repository = MemoryRepository()
        self.service = TaskService(self.repository)

    def test_create_task(self):
        task_data = {"title": "Test Task", "description": "Test Description"}
        task_dto = TaskDTO(**task_data)
        
        created_task = self.service.create_task(task_dto)
        
        self.assertEqual(created_task.title, task_dto.title)
        self.assertEqual(created_task.description, task_dto.description)
        self.assertFalse(created_task.is_complete)

    def test_update_task_status(self):
        task_data = {"title": "Test Task", "description": "Test Description"}
        task_dto = TaskDTO(**task_data)
        created_task = self.service.create_task(task_dto)
        
        updated_task = self.service.update_task_status(created_task.id, True)
        
        self.assertTrue(updated_task.is_complete)

    def test_delete_task(self):
        task_data = {"title": "Test Task", "description": "Test Description"}
        task_dto = TaskDTO(**task_data)
        created_task = self.service.create_task(task_dto)
        
        self.service.delete_task(created_task.id)
        
        with self.assertRaises(KeyError):
            self.service.get_task(created_task.id)

    def test_list_tasks(self):
        task_data1 = {"title": "Task 1", "description": "Description 1"}
        task_data2 = {"title": "Task 2", "description": "Description 2"}
        self.service.create_task(TaskDTO(**task_data1))
        self.service.create_task(TaskDTO(**task_data2))
        
        tasks = self.service.list_tasks()
        
        self.assertEqual(len(tasks), 2)