## Preconditions:

- Python 3

## Inspired by the project

https://github.com/marciovrl/fastapi-example.git

## Run local

### Install dependencies

```
pip install -r requirements.txt
```

### Run server

```
uvicorn app.main:app --reload
```

### Run test

```
pytest app/test.py
```

## Run with docker

### Run server

```
docker-compose up -d --build
```

### Run test

```
docker-compose exec app pytest test/test.py
```

## API documentation (provided by Swagger UI)

```
http://127.0.0.1:8000/docs
```

### Run server

```
docker-compose exec db psql --username=fastapi --dbname=fastapi_dev
```
