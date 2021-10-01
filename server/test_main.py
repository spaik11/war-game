from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_read_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to war!"}


def test_read_users():
    response = client.get("/users/")
    assert response.status_code == 200
    assert response.json() == {}
