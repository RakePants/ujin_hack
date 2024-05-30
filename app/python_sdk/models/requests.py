import uuid
from datetime import datetime, timedelta, timezone
from typing import Generic, Type, TypeVar, Union

from pydantic import BaseModel, Json

from .responses import *

TResponse = TypeVar("TResponse")


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
    method: str = "GET"
    endpoint: str = "/echo/"
    query: QueryModel = QueryModel(query={"json": 1})
    response_model: HealthCheckResponse


class CreateOmissionRequest(BaseRequest):
    method: str = "POST"
    endpoint: str = "/v1/pass/create/"
    body: BodyModel = BodyModel(
        body={
            "apartment_id": 1467,
            "type": "guest",
            "guest_fullname": None,
            "guest_phone": 78945612322,
            "brand": "ABC",
            "id_number": "a12345bc",
            "comment": None,
            "date_start": None,
            "date_end": None,
        }
    )
    response_model: OmissionResponse

    @classmethod
    def create_with_params(cls, full_name: str, face_id: uuid.UUID):
        current_time = datetime.now(timezone.utc)
        date_start = int(current_time.timestamp())
        date_end = int((current_time + timedelta(hours=4)).timestamp())

        body_params = cls.body.body.copy()
        body_params.update(
            {
                "guest_fullname": full_name,
                "comment": str(face_id),
                "date_start": date_start,
                "date_end": date_end,
            }
        )

        return cls(body=BodyModel(body=body_params))


class GetOmissionsListRequest(BaseRequest):
    method: str = "GET"
    endpoint: str = "/v1/pass/crm/get-list"
    query: QueryModel = QueryModel(
        query={
            "search": None,  # Set default to None
            "type": "guest",
            "apartment_id": 1467,
            "per_page": 100,
            "page": 1,
        }
    )
    response_model: OmissionResponse

    @classmethod
    def create_with_params(cls, full_name: str):
        query_params = cls.query.query.copy()
        query_params.update(
            {
                "search": full_name,
            }
        )

        return cls(query=QueryModel(query=query_params))


class SubmissionRequest(BaseRequest):
    response_model: SubmissionResponse
    # TODO написать запрос для получения пропуска
