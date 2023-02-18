from pydantic import BaseModel


class UserSignUp(BaseModel):
    email: str
    phone: int
    name: str
