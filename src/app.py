from flask import Flask
from api.controllers.tasks_controller import TaskController

app = Flask(__name__)

# Initialize the TaskController
task_controller = TaskController()

# Define API routes
@app.route('/api/tasks', methods=['POST'])
def create_task():
    return task_controller.create_task()

@app.route('/api/tasks', methods=['GET'])
def list_tasks():
    return task_controller.list_tasks()

@app.route('/api/tasks/<task_id>', methods=['PUT'])
def update_task_status(task_id):
    return task_controller.update_task_status(task_id)

@app.route('/api/tasks/<task_id>', methods=['DELETE'])
def delete_task(task_id):
    return task_controller.delete_task(task_id)

if __name__ == '__main__':
    app.run(debug=True)