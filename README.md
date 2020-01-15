# fastapi-example [![CircleCI](https://circleci.com/gh/marciovrl/fastapi-example.svg?style=svg)](https://circleci.com/gh/marciovrl/fastapi-example)

A simple example of using Fast API in Python.

## Preconditions:

- Python 3

## Clone the project

```
git clone https://github.com/marciovrl/fastapi-example.git
```

## Install dependencies

```
pip install -r requirements.txt
```

## Run server

```
uvicorn app.main:app --reload
```

## Run test

```
pytest app/test.py
```

## API documentation (provided by Swagger UI)

```
http://127.0.0.1:8000/docs
```
