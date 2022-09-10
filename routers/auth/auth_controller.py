from datetime import datetime, timedelta

from fastapi import Depends, HTTPException, Request
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jose import jwt

from database.data import users_data
from routers.auth.auth_schemas import TokenSchema
from settings import settings

auth_scheme = HTTPBearer()


class AuthController:
    def __new__(self, payload: TokenSchema):
        self.username = payload.username.strip().lower()
        self.password = payload.password.strip()
        self.users = users_data
        if self.authenticate(self):
            return {"token": self.generate_token(self)}
        return None

    def authenticate(self):
        for user in self.users:
            if user.username == self.username and user.password == self.password:
                return True
        return False

    def generate_token(self):
        expiration = datetime.utcnow() + timedelta(minutes=15)
        to_encode = {"username": self.username, "exp": expiration}
        return jwt.encode(to_encode, settings.jwt_secret_key, "HS256")

    @staticmethod
    def verify_token(
        request: Request,
        authorization: HTTPAuthorizationCredentials = Depends(auth_scheme),
    ):
        try:
            request.state.token = jwt.decode(
                authorization.credentials, settings.jwt_secret_key, "HS256"
            )
        except Exception as exc:
            print(f"Exception verify token: {exc}")
            raise HTTPException(401)
