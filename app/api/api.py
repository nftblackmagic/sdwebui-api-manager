import json
import requests
import urllib.parse as urlparse
from urllib.parse import urlencode

def read_user():
    with open('data/users.json') as stream:
        users = json.load(stream)

    return users


def read_questions(position: int):
    with open('data/questions.json') as stream:
        questions = json.load(stream)

    for question in questions:
        if question['position'] == position:
            return question


def read_alternatives(question_id: int):
    alternatives_question = []
    with open('data/alternatives.json') as stream:
        alternatives = json.load(stream)

    for alternative in alternatives:
        if alternative['question_id'] == question_id:
            alternatives_question.append(alternative)

    return alternatives_question


def create_answer(payload):
    answers = []
    result = []

    with open('data/alternatives.json') as stream:
        alternatives = json.load(stream)

    for question in payload['answers']:
        for alternative in alternatives:
            if alternative['question_id'] == question['question_id']:
                answers.append(alternative['alternative'])
                break

    with open('data/cars.json') as stream:
        cars = json.load(stream)

    for car in cars:
        if answers[0] in car.values() and answers[1] in car.values() and answers[2] in car.values():
            result.append(car)

    return result


def read_result(user_id: int):
    user_result = []

    with open('data/results.json') as stream:
        results = json.load(stream)

    with open('data/users.json') as stream:
        users = json.load(stream)

    with open('data/cars.json') as stream:
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


def img2img(payload):

    url = 'http://0.0.0.0:7860/sdapi/v1/img2img'

    headers = {
        'Content-Type': 'application/json',
    }

    filter_data = {}

    for k,v in payload.items():
        if payload[k] != None:
            filter_data[k] = v

    response = requests.post(url, headers=headers, data=json.dumps(filter_data))    

    res = response.json()

    print(res)

    return res

def txt2img(payload):

    url = 'http://0.0.0.0:7860/sdapi/v1/txt2img'

    headers = {
        'Content-Type': 'application/json',
    }

    filter_data = {}

    for k,v in payload.items():
        if payload[k] != None:
            filter_data[k] = v

    response = requests.post(url, headers=headers, data=json.dumps(filter_data))    

    res = response.json()

    return res

def progress():
    url = 'http://0.0.0.0:7860/sdapi/v1/progress?skip_current_image=false'

    headers = {
        'Content-Type': 'application/json',
    }

    response = requests.get(url, headers=headers)

    res = response.json()

    return res