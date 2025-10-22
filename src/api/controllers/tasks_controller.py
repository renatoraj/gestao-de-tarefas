from flask import Blueprint, request, jsonify
from api.services.task_service import TaskService
from api.dtos.task_dto import TaskCreateDTO, TaskUpdateDTO, TaskResponseDTO
from api.exceptions import TaskNotFoundException, InvalidTaskDataException

tasks_blueprint = Blueprint('tasks', __name__)
task_service = TaskService()

@tasks_blueprint.route('/api/tasks', methods=['POST'])
def create_task():
    try:
        data = request.json
        if not data:
            return jsonify({"error": "No input data provided"}), 400
            
        task_dto = TaskCreateDTO(**data)
        task = task_service.create_task(task_dto)
        
        return jsonify({
            "id": task.id,
            "title": task.title,
            "description": task.description,
            "is_complete": task.is_complete,
            "created_at": task.created_at.isoformat() if hasattr(task.created_at, 'isoformat') else task.created_at
        }), 201
        
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@tasks_blueprint.route('/api/tasks', methods=['GET'])
def list_tasks():
    try:
        tasks = task_service.list_tasks()
        tasks_response = []
        for task in tasks:
            tasks_response.append({
                "id": task.id,
                "title": task.title,
                "description": task.description,
                "is_complete": task.is_complete,
                "created_at": task.created_at.isoformat() if hasattr(task.created_at, 'isoformat') else task.created_at
            })
        return jsonify(tasks_response), 200
    except Exception as e:
        return jsonify({"error": "Internal server error"}), 500

@tasks_blueprint.route('/api/tasks/<task_id>', methods=['GET'])
def get_task(task_id):
    try:
        task = task_service.get_task(task_id)
        return jsonify({
            "id": task.id,
            "title": task.title,
            "description": task.description,
            "is_complete": task.is_complete,
            "created_at": task.created_at.isoformat() if hasattr(task.created_at, 'isoformat') else task.created_at
        }), 200
    except TaskNotFoundException:
        raise
    except Exception as e:
        return jsonify({"error": "Internal server error"}), 500

@tasks_blueprint.route('/api/tasks/<task_id>', methods=['PUT'])
def update_task(task_id):
    try:
        data = request.json
        if not data:
            return jsonify({"error": "No input data provided"}), 400
            
        task_dto = TaskUpdateDTO(**data)
        updated_task = task_service.update_task(task_id, task_dto)
        
        return jsonify({
            "id": updated_task.id,
            "title": updated_task.title,
            "description": updated_task.description,
            "is_complete": updated_task.is_complete,
            "created_at": updated_task.created_at.isoformat() if hasattr(updated_task.created_at, 'isoformat') else updated_task.created_at
        }), 200
        
    except TaskNotFoundException:
        raise
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@tasks_blueprint.route('/api/tasks/<task_id>', methods=['DELETE'])
def delete_task(task_id):
    try:
        task_service.delete_task(task_id)
        return '', 204
    except TaskNotFoundException:
        raise
    except Exception as e:
        return jsonify({"error": "Internal server error"}), 500