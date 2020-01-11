from starlette.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_main():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {'message': 'Fast API in Python'}


def test_read_user():
    response = client.get('/user')
    assert response.status_code == 200
    assert len(response.json()) != 0


def test_read_question():
    response = client.get('/question/1')
    assert response.status_code == 200
    assert response.json()['position'] == 1


def test_read_question_invalid():
    response = client.get('/question/0')
    assert response.status_code == 400
    assert response.json() == {'message': 'Error'}


def test_read_alternatives():
    response = client.get('/alternatives/1')
    assert response.status_code == 200
    assert response.json()[1]['question_id'] == 1
