from pydantic import BaseModel


class UserSignUp(BaseModel):
    _id: 0
    email: str
    name: int
    password: str

class UserLoginSchema(BaseModel):
    _id : 0
    email: str
    password: str
