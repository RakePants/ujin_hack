from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field


class Config(BaseSettings):
    MONGODB_CONNECTION_URI: str = Field('MONGODB_CONNECTION_URI')
