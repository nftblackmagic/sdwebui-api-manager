from fastapi import FastAPI, HTTPException
from starlette.responses import Response

from app.db.models import Img2imgArgs, Txt2imgArgs, ExtraSingleImage
from app.api import api
from app.manager import reqq

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Fast API in Python"}


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


@app.get("/controlnet/model_list")
def controlnet_model_list():
    return api.controlnet_model_list()


@app.get("/controlnet/module_list")
def controlnet_module_list():
    return api.controlnet_module_list()


@app.post("/sdapi/v1/extra-single-image", status_code=201)
def extra_single_image(payload: ExtraSingleImage):
    payload = payload.dict()
    return api.extra_single_image(payload)


@app.get("/sdapi/v1/sd-models")
def sd_models():
    return api.sd_models()
