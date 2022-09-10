from fastapi import Depends, FastAPI

from routers.auth.auth_controller import AuthController
from routers.auth.auth_router import auth_router
from routers.root.root_router import root_router

app = FastAPI()

app.include_router(auth_router)
app.include_router(root_router, dependencies=[Depends(AuthController.verify_token)])
