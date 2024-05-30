from typing import Type, TypeVar, Generic, Union
from pydantic import BaseModel, Json
from .responses import *


TResponse = TypeVar('TResponse')


class HeadersModel(BaseModel):
    headers: dict


class QueryModel(BaseModel):
    query: dict


class BodyModel(BaseModel):
    body: dict


class BaseRequest(BaseModel, Generic[TResponse]):
    method: str
    endpoint: str
    headers: HeadersModel = None
    query: QueryModel = None
    body: BodyModel = None
    response_model: Type[TResponse]


class HealthCheckRequest(BaseRequest):
    method: str = 'GET'
    endpoint: str = '/echo/'
    query: QueryModel = QueryModel(query={'json': 1})
    response_model: HealthCheckResponse


class SubmissionRequest(BaseRequest):
    response_model = SubmissionResponse
    # TODO написать запрос для отправки заявки в УК


class OmissionRequest(BaseRequest):
    response_model = OmissionResponse
    # TODO написать запрос для получения пропуска
