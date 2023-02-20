from fastapi import FastAPI
import app.schemas as schemas
from . import ops
from fastapi.encoders import jsonable_encoder

app = FastAPI()

@app.get("/")
def root():
    return {"hello": "world"}


@app.post("/inserter", tags=["test"])
async def inserter(info: schemas.UserSignUp):
    encoded_info = jsonable_encoder(info)
    ops.inserter(encoded_info)
    print(type(info))
    return (True, info)
