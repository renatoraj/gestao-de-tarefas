import sys
import os
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../..', 'src'))

from unittest.mock import Mock, patch
from api.controllers.tasks_controller import tasks_blueprint
from api.services.task_service import TaskService
from api.dtos.task_dto import TaskCreateDTO, TaskUpdateDTO, TaskResponseDTO
from api.exceptions import TaskNotFoundException, InvalidTaskDataException
from api.models.task import Task
from datetime import datetime

class TestTasksController:
    
    @pytest.fixture
    def client(self):
        from app import create_app
        
        app = create_app()
        app.config['TESTING'] = True
        with app.test_client() as client:
            yield client
    
    @pytest.fixture
    def sample_task(self):
        return Task(
            id="123",
            title="Test Task",
            description="Test Description",
            is_complete=False,
            created_at=datetime(2023, 1, 1, 12, 0, 0)
        )
    
    def test_create_task_success(self, client, sample_task):
        # Arrange
        with patch.object(TaskService, 'create_task') as mock_create:
            mock_create.return_value = sample_task
            task_data = {
                "title": "Test Task",
                "description": "Test Description"
            }
            
            # Act
            response = client.post('/api/tasks', json=task_data)
            
            # Assert
            assert response.status_code == 201
            data = response.get_json()
            assert data['id'] == "123"
            assert data['title'] == "Test Task"
            mock_create.assert_called_once()
    
    def test_create_task_invalid_data(self, client):
        # Arrange
        invalid_data = {
            "title": "",  # título vazio - deve falhar na validação
        }
        
        # Act
        response = client.post('/api/tasks', json=invalid_data)
        
        # Assert
        assert response.status_code == 400
    
    def test_list_tasks_success(self, client, sample_task):
        # Arrange
        with patch.object(TaskService, 'list_tasks') as mock_list:
            mock_list.return_value = [sample_task]
            
            # Act
            response = client.get('/api/tasks')
            
            # Assert
            assert response.status_code == 200
            data = response.get_json()
            assert len(data) == 1
            assert data[0]['title'] == "Test Task"
    
    def test_get_task_success(self, client, sample_task):
        # Arrange
        with patch.object(TaskService, 'get_task') as mock_get:
            mock_get.return_value = sample_task
            
            # Act
            response = client.get('/api/tasks/123')
            
            # Assert
            assert response.status_code == 200
            data = response.get_json()
            assert data['id'] == "123"
    
    def test_get_task_not_found(self, client):
        # Arrange
        with patch.object(TaskService, 'get_task') as mock_get:
            mock_get.side_effect = TaskNotFoundException("Task not found")
            
            # Act
            response = client.get('/api/tasks/999')
            
            # Assert
            assert response.status_code == 404
    
    def test_update_task_success(self, client, sample_task):
        # Arrange
        with patch.object(TaskService, 'update_task') as mock_update:
            updated_task = Task(
                id="123",
                title="Updated Task",
                description="Updated Description",
                is_complete=True,
                created_at=datetime(2023, 1, 1, 12, 0, 0)
            )
            mock_update.return_value = updated_task
            
            update_data = {
                "title": "Updated Task",
                "is_complete": True
            }
            
            # Act
            response = client.put('/api/tasks/123', json=update_data)
            
            # Assert
            assert response.status_code == 200
            data = response.get_json()
            assert data['title'] == "Updated Task"
            assert data['is_complete'] is True
    
    def test_delete_task_success(self, client):
        # Arrange
        with patch.object(TaskService, 'delete_task') as mock_delete:
            mock_delete.return_value = True
            
            # Act
            response = client.delete('/api/tasks/123')
            
            # Assert
            assert response.status_code == 204
    
    def test_delete_task_not_found(self, client):
        # Arrange
        with patch.object(TaskService, 'delete_task') as mock_delete:
            mock_delete.side_effect = TaskNotFoundException("Task not found")
            
            # Act
            response = client.delete('/api/tasks/999')
            
            # Assert
            assert response.status_code == 404