from pydantic import BaseModel


class CustomerSchema(BaseModel):
    name: str
    address: str
    phone: str
    job: str
