from flask import jsonify

class TaskNotFoundException(Exception):
    """Exceção quando task não é encontrada"""
    pass

class InvalidTaskDataException(Exception):
    """Exceção quando dados da task são inválidos"""
    pass

def handle_task_not_found(error):
    return jsonify({"error": "Task not found"}), 404

def handle_invalid_task_data(error):
    return jsonify({"error": str(error)}), 400

def register_error_handlers(app):
    app.errorhandler(TaskNotFoundException)(handle_task_not_found)
    app.errorhandler(InvalidTaskDataException)(handle_invalid_task_data)
    
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({"error": "Resource not found"}), 404

    @app.errorhandler(500)
    def internal_error(error):
        return jsonify({"error": "Internal server error"}), 500