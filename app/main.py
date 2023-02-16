from fastapi import FastAPI
import app.schemas as schemas

app = FastAPI()

@app.get("/")
def root():
    return {"hello": "world"}


@app.get("/data", tags=["test"])
async def func(info: schemas.UserSignUp):
    return info
