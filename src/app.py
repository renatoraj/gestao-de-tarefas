from flask import Flask
from api.controllers.tasks_controller import tasks_blueprint
from api.exceptions import register_error_handlers

def create_app():
    app = Flask(__name__)
    app.config['JSON_SORT_KEYS'] = False
    app.register_blueprint(tasks_blueprint)
    register_error_handlers(app)
    return app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)