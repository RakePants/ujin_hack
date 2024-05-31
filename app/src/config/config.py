from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field


class Config(BaseSettings):
    #model_config = SettingsConfigDict(env_file='../../.env')
    MONGODB_CONNECTION_URI: str = Field(alias='MONGODB_CONNECTION_URI', default='mongodb://mongodb-service:27017/')
    UJIN_CON_TOKEN: str = Field(alias='UJIN_CON_TOKEN', default='ust-739109-3fe72efd12ef86582919741571b1cb40')
    UJIN_HOST: str = Field(alias='UJIN_HOST', default='api-uae-test.ujin.tech')
