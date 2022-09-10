from pydantic import BaseModel


class UserSchema(BaseModel):
    username: str
    password: str
    name: str
    phone: str
    job: str
