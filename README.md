## Problem of stable diffusion webui

Stable diffusion webui provides a powerful tool for AI image generation. However, the webui api has some limitations:

1. a blocking REST api call, which might take more than 30s to return the final value. Most gateways don't allow such long blocking time on api call.
2. webui api is a single thread process. Once the thread is occupied, other webui api will fail. (Even though there is a multi thread mode in stable diffusion webui)

This repo is aiming to solve the above problems.

## Preconditions:

- Python 3
- Stable diffusion Webui

## Inspired by the project

https://github.com/marciovrl/fastapi-example.git

## Run local

### Before run this project, please make sure you launched the stable diffusion webui api.

### Install dependencies

```
pip install -r requirements.txt
```

### Run server

```
uvicorn app.main:app --reload --port 5001
```

<!-- ### Run test

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
``` -->

## API documentation (provided by Swagger UI)

```
http://127.0.0.1:8000/docs
```

<!-- ### Run server

```
docker-compose exec db psql --username=fastapi --dbname=fastapi_dev
``` -->

## Model swtich

There is an extra filed in txt2img/img2img api:

    options: Optional[dict]

You can swtich stable diffusion by using this options.

```
"options":
{
"sd_model_checkpoint": <The model you want to use>
}
```
