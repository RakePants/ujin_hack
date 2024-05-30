from typing import Type, TypeVar, Generic
from pydantic import BaseModel


class BaseResponse(BaseModel):
    command: str
    error: int
    message: str
    data: dict = None
    connection: dict
    token: str
    fromdomain: str
    worktime: str

class HealthCheckResponse(BaseResponse):
    pass