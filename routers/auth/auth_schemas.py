from pydantic import BaseModel


class TokenSchema(BaseModel):
    username: str
    password: str

    class Config:
        schema_extra = {
            "example": {
                "username": "user0",
                "password": "123"
            }
        }
