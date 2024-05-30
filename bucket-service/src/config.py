from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")

    access_key: str
    secret_key: str
    endpoint_url: str
    bucket_name: str


settings = Settings()
