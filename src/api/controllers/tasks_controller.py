from flask import Blueprint, request, jsonify
from api.services.task_service import TaskService
from api.dtos.task_dto import TaskDTO

tasks_controller = Blueprint('tasks_controller', __name__)
task_service = TaskService()

@tasks_controller.route('/api/tasks', methods=['POST'])
def create_task():
    data = request.json
    task_dto = TaskDTO(**data)
    task = task_service.create_task(task_dto)
    return jsonify(task), 201

@tasks_controller.route('/api/tasks', methods=['GET'])
def list_tasks():
    tasks = task_service.list_tasks()
    return jsonify(tasks), 200

@tasks_controller.route('/api/tasks/<task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.json
    task_dto = TaskDTO(**data)
    updated_task = task_service.update_task(task_id, task_dto)
    if updated_task:
        return jsonify(updated_task), 200
    return jsonify({"error": "Task not found"}), 404

@tasks_controller.route('/api/tasks/<task_id>', methods=['DELETE'])
def delete_task(task_id):
    success = task_service.delete_task(task_id)
    if success:
        return '', 204
    return jsonify({"error": "Task not found"}), 404