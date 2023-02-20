from pydantic import BaseModel


class UserSignUp(BaseModel):
    _id: 0
    email: str
    phone: int
    name: str
