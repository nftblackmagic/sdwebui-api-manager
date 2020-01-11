from fastapi import FastAPI
from starlette.responses import Response

import json

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Fast API in Python"}


@app.get("/user")
def read_user():
    with open('data/users.json') as stream:
        users = json.load(stream)

    return users


@app.get("/question/{position}", status_code=200)
def read_questions(position: int, response: Response):
    with open('data/questions.json') as stream:
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

    with open('data/alternatives.json') as stream:
        alternatives = json.load(stream)

    for alternative in alternatives:
        if alternative['question_id'] == question_id:
            alternatives_question.append(alternative)

    return alternatives_question
