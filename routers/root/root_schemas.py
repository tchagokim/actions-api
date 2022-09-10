from pydantic import BaseModel


class PayloadSchema(BaseModel):
    action: str
    data: dict

    class Config:
        schema_extra = {
            "example": {
                "action": "customers.get_id",
                "data": {"id" : 1}
            }
        }
