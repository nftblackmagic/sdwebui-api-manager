import json
import requests


def img2img(payload):

    url = 'http://0.0.0.0:7860/sdapi/v1/img2img'

    headers = {
        'Content-Type': 'application/json',
    }

    filter_data = {}

    for k, v in payload.items():
        if payload[k] != None:
            filter_data[k] = v

    print("img2img settings", filter_data)

    response = requests.post(url, headers=headers,
                             data=json.dumps(filter_data))

    res = response.json()

    return res


def txt2img(payload):

    url = 'http://0.0.0.0:7860/sdapi/v1/txt2img'

    headers = {
        'Content-Type': 'application/json',
    }

    filter_data = {}

    for k, v in payload.items():
        if payload[k] != None:
            filter_data[k] = v

    print("txt2img settings", filter_data)

    response = requests.post(url, headers=headers,
                             data=json.dumps(filter_data))

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


def get_options():
    url = 'http://0.0.0.0:7860/sdapi/v1/options'

    headers = {
        'Content-Type': 'application/json',
    }

    response = requests.get(url, headers=headers, timeout=5)

    res = response.json()

    return res


def set_options(payload):
    url = 'http://0.0.0.0:7860/sdapi/v1/options'

    headers = {
        'Content-Type': 'application/json',
    }

    filter_data = {}

    for k, v in payload.items():
        if payload[k] != None:
            filter_data[k] = v

    print("set_options settings", filter_data)

    response = requests.post(url, headers=headers,
                             data=json.dumps(filter_data))

    res = response.json()

    return res


def extra_single_image(payload):
    url = 'http://0.0.0.0:7860//sdapi/v1/extra-single-image'

    headers = {
        'Content-Type': 'application/json',
    }

    filter_data = {}

    for k, v in payload.items():
        if payload[k] != None:
            filter_data[k] = v

    print("set_options settings", filter_data)

    response = requests.post(url, headers=headers,
                             data=json.dumps(filter_data))

    res = response.json()

    return res
