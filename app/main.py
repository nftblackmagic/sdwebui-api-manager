from fastapi import FastAPI
from starlette.responses import Response

from app.models import UserAnswer
import json

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Fast API in Python"}


@app.get("/user")
def read_user():
    with open('app/data/users.json') as stream:
        users = json.load(stream)

    return users


@app.get("/question/{position}", status_code=200)
def read_questions(position: int, response: Response):
    with open('app/data/questions.json') as stream:
        questions = json.load(stream)

    if position > len(questions) or position == 0:
        response.status_code = 400
        return {"message": "Error"}

    for question in questions:
        if question['position'] == position:
            return question


@app.get("/alternatives/{question_id}")
def read_alternatives(question_id: int):
    alternatives_question = []

    with open('app/data/alternatives.json') as stream:
        alternatives = json.load(stream)

    for alternative in alternatives:
        if alternative['question_id'] == question_id:
            alternatives_question.append(alternative)

    return alternatives_question


@app.post("/answer", status_code=201)
def create_answer(payload: UserAnswer):
    payload = payload.dict()
    answers = []
    result = []

    with open('app/data/alternatives.json') as stream:
        alternatives = json.load(stream)

    for question in payload['answers']:
        for alternative in alternatives:
            if alternative['question_id'] == question['question_id']:
                answers.append(alternative['alternative'])
                break

    with open('app/data/cars.json') as stream:
        cars = json.load(stream)

    for car in cars:
        if answers[0] in car.values() and answers[1] in car.values() and answers[2] in car.values():
            result.append(car)

    return result


@app.get("/result/{user_id}")
def read_result(user_id: int):
    user_result = []

    with open('app/data/results.json') as stream:
        results = json.load(stream)

    with open('app/data/users.json') as stream:
        users = json.load(stream)

    with open('app/data/cars.json') as stream:
        cars = json.load(stream)

    for result in results:
        if result['user_id'] == user_id:
            for user in users:
                if user['id'] == result['user_id']:
                    user_result.append({'user': user})
                    break

        for car_id in result['cars']:
            for car in cars:
                if car_id == car['id']:
                    user_result.append(car)

    return user_result
