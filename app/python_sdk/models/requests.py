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
    method: str = 'POST'
    endpoint: str = '/api/v1/tck/bms/tickets/create/'
    body: BodyModel = BodyModel(body={
        "title": "заявка",
        "description": "Обнаружен потусторонний объект",
        "priority": "high",
        "class": "client",
        "status": "new",
        "initiator.id": 739109,
        "types": [1667],
        "assignees": [],
        "contracting_companies": [],
        "objects": [
            {
                "type": "apartment",
                "id": 1467
            }
        ],
        "planned_start_at": None,
        "planned_end_at": None,
        "hide_planned_at_from_resident": None,
        "extra": None  # todo: face_id
    })
    response_model: SubmissionResponse


class OmissionRequest(BaseRequest):
    response_model = OmissionResponse
    # TODO написать запрос для получения пропуска
