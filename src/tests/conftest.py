from pytest import fixture

@fixture
def client():
    from src.app import app
    with app.test_client() as client:
        yield client

@fixture
def sample_task():
    return {
        "title": "Sample Task",
        "description": "This is a sample task for testing."
    }