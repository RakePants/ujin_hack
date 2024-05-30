from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field


class Config(BaseSettings):
    #model_config = SettingsConfigDict(env_file='../../.env')
    MONGODB_CONNECTION_URI: str = Field(alias='MONGODB_CONNECTION_URI', default='mongodb://localhost:27017/')
    UJIN_CON_TOKEN: str = Field(alias='UJIN_CON_TOKEN')
    UJIN_HOST: str = Field(alias='UJIN_HOST', default='https://api-uae-test.ujin.tech')
