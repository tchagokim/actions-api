from fastapi import APIRouter

from routers.root.root_controllers import RootController
from routers.root.root_schemas import PayloadSchema

root_router = APIRouter(tags=["Root"])


@root_router.post("/", summary="magic happens here")
def root_route(payload: PayloadSchema):
    return RootController(payload)
