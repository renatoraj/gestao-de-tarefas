import sys
import os
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../..', 'src'))

from unittest.mock import Mock
from api.services.task_service import TaskService
from api.dtos.task_dto import TaskCreateDTO, TaskUpdateDTO
from api.models.task import Task
from api.exceptions import TaskNotFoundException
from datetime import datetime

class TestTaskService:
    
    def test_create_task_success(self):
        # Arrange
        mock_repo = Mock()
        service = TaskService(repository=mock_repo)
        task_dto = TaskCreateDTO(title="Test Task", description="Test Description")
        
        # Act
        result = service.create_task(task_dto)
        
        # Assert
        assert result.title == "Test Task"
        assert result.description == "Test Description"
        assert result.is_complete is False
        assert result.id is not None
        mock_repo.add.assert_called_once()
    
    def test_get_task_success(self):
        # Arrange
        mock_repo = Mock()
        mock_task = Task(id="123", title="Test Task", description="Test Desc")
        mock_repo.get.return_value = mock_task
        service = TaskService(repository=mock_repo)
        
        # Act
        result = service.get_task("123")
        
        # Assert
        assert result == mock_task
        mock_repo.get.assert_called_once_with("123")
    
    def test_get_task_not_found(self):
        # Arrange
        mock_repo = Mock()
        mock_repo.get.return_value = None
        service = TaskService(repository=mock_repo)
        
        # Act & Assert
        with pytest.raises(TaskNotFoundException):
            service.get_task("123")
    
    def test_list_tasks(self):
        # Arrange
        mock_repo = Mock()
        mock_tasks = [
            Task(id="1", title="Task 1"),
            Task(id="2", title="Task 2")
        ]
        mock_repo.get_all.return_value = mock_tasks
        service = TaskService(repository=mock_repo)
        
        # Act
        result = service.list_tasks()
        
        # Assert
        assert result == mock_tasks
        mock_repo.get_all.assert_called_once()
    
    def test_update_task_success(self):
        # Arrange
        mock_repo = Mock()
        existing_task = Task(id="123", title="Old Title", description="Old Desc", is_complete=False)
        mock_repo.get.return_value = existing_task
        service = TaskService(repository=mock_repo)
        
        update_dto = TaskUpdateDTO(title="New Title", is_complete=True)
        
        # Act
        result = service.update_task("123", update_dto)
        
        # Assert
        assert result.title == "New Title"
        assert result.is_complete is True
        assert result.description == "Old Desc"  # Não foi alterado
        mock_repo.update.assert_called_once()
    
    def test_delete_task_success(self):
        # Arrange
        mock_repo = Mock()
        mock_task = Task(id="123", title="Test Task")
        mock_repo.get.return_value = mock_task
        mock_repo.delete.return_value = True
        service = TaskService(repository=mock_repo)
        
        # Act
        result = service.delete_task("123")
        
        # Assert
        assert result is True
        mock_repo.delete.assert_called_once_with("123")
    
    def test_delete_task_not_found(self):
        # Arrange
        mock_repo = Mock()
        mock_repo.get.return_value = None
        service = TaskService(repository=mock_repo)
        
        # Act & Assert
        with pytest.raises(TaskNotFoundException):
            service.delete_task("123")