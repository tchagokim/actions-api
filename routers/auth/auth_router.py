from fastapi import APIRouter

from routers.auth.auth_controller import AuthController
from routers.auth.auth_schemas import TokenSchema

auth_router = APIRouter(tags=["Auth"])


@auth_router.post("/token", summary="get token")
def auth_route(payload: TokenSchema):
    return AuthController(payload)
