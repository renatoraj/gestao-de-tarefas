from unittest import TestCase
from unittest.mock import patch, MagicMock
from src.api.controllers.tasks_controller import TaskController
from src.api.services.task_service import TaskService
from src.api.dtos.task_dto import TaskDTO

class TestTaskController(TestCase):

    @patch.object(TaskService, 'create_task')
    def test_create_task(self, mock_create_task):
        mock_create_task.return_value = TaskDTO(id='1', title='Test Task', description='A test task', is_complete=False)

        controller = TaskController()
        response = controller.create_task({'title': 'Test Task', 'description': 'A test task'})

        self.assertEqual(response.status_code, 201)
        self.assertIn('id', response.json)
        self.assertEqual(response.json['title'], 'Test Task')

    @patch.object(TaskService, 'list_tasks')
    def test_list_tasks(self, mock_list_tasks):
        mock_list_tasks.return_value = [TaskDTO(id='1', title='Test Task', description='A test task', is_complete=False)]

        controller = TaskController()
        response = controller.list_tasks()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), 1)
        self.assertEqual(response.json[0]['title'], 'Test Task')

    @patch.object(TaskService, 'update_task_status')
    def test_update_task_status(self, mock_update_task_status):
        mock_update_task_status.return_value = TaskDTO(id='1', title='Test Task', description='A test task', is_complete=True)

        controller = TaskController()
        response = controller.update_task_status('1', {'is_complete': True})

        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json['is_complete'])

    @patch.object(TaskService, 'delete_task')
    def test_delete_task(self, mock_delete_task):
        mock_delete_task.return_value = True

        controller = TaskController()
        response = controller.delete_task('1')

        self.assertEqual(response.status_code, 204)

    @patch.object(TaskService, 'get_task')
    def test_get_task_not_found(self, mock_get_task):
        mock_get_task.side_effect = Exception("Task not found")

        controller = TaskController()
        response = controller.get_task('non-existent-id')

        self.assertEqual(response.status_code, 404)
        self.assertIn('error', response.json)