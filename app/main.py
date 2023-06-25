from fastapi import FastAPI, HTTPException
from starlette.responses import Response

from app.db.models import UserAnswer, Img2imgArgs, Txt2imgArgs
from app.api import api
from app.manager import reqq

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Fast API in Python"}


@app.get("/user")
def read_user():
    return api.read_user()


@app.get("/question/{position}", status_code=200)
def read_questions(position: int, response: Response):
    question = api.read_questions(position)

    if not question:
        raise HTTPException(status_code=400, detail="Error")

    return question


@app.get("/alternatives/{question_id}")
def read_alternatives(question_id: int):
    return api.read_alternatives(question_id)


@app.post("/answer", status_code=201)
def create_answer(payload: UserAnswer):
    payload = payload.dict()

    return api.create_answer(payload)


@app.get("/result/{user_id}")
def read_result(user_id: int):
    return api.read_result(user_id)


@app.post("/rawimg2img", status_code=201)
def rawimg2img(payload: Img2imgArgs):
    payload = payload.dict()

    return api.img2img(payload)

@app.post("/rawtxt2img", status_code=201)
def rawtxt2img(payload: Txt2imgArgs):
    payload = payload.dict()

    return api.txt2img(payload)

@app.post("/img2img", status_code=201)
def img2img(payload: Img2imgArgs):
    payload = payload.dict()
    return reqq.add_req_queue(payload, "img2img")

@app.post("/txt2img", status_code=201)
def txt2img(payload: Txt2imgArgs):
    payload = payload.dict()
    return reqq.add_req_queue(payload, "txt2img")

@app.get("/progress/{req_id}")
def progress(req_id: str):
    return reqq.get_result(req_id)