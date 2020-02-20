from starlette.testclient import TestClient
from app.main import app
import json

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
    assert response.json() == {'detail': 'Error'}


def test_read_alternatives():
    response = client.get('/alternatives/1')
    assert response.status_code == 200
    assert response.json()[1]['question_id'] == 1


def test_create_answer():
    body = {"user_id": 1, "answers": [{"question_id": 1, "alternative_id": 2}, {
        "question_id": 2, "alternative_id": 2}, {"question_id": 2, "alternative_id": 2}]}
    body = json.dumps(body)
    response = client.post('/answer', data=body)
    assert response.status_code == 201


def test_read_result():
    response = client.get('/result/1')
    assert response.status_code == 200
