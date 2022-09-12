from pydantic import BaseSettings


class Settings(BaseSettings):
    jwt_secret_key: str
    jwt_expire_minutes: int

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
