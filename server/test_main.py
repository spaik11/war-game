from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_read_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to war!"}


def test_post_users():
    all_users = client.get('/users/')
    initial_user_count = len(all_users.json())
    response = client.post(
        "/user/", json={"id": 99, "username": "test", "password": "123", "wins": 99})
    new_all_users = client.get('/users/')
    new_user_count = len(new_all_users.json())
    # import ipdb
    # ipdb.set_trace()

    assert response.status_code == 200
    assert initial_user_count + 1 == new_user_count


# def test_read_war():
#     response = client.get("/war/")
#     assert response.status_code == 200
