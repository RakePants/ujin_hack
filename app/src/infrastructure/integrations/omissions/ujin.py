from dataclasses import dataclass

from app.src.infrastructure.integrations.omissions.base import BaseOmissions
from app.python_sdk.models.requests import OmissionRequest
from app.python_sdk.client import Client


# TODO реализовать методы
@dataclass
class UJINOmission(BaseOmissions):
    client: Client

    async def create_omission(self, omission: OmissionRequest):
        raise NotImplementedError

    async def get_omission(self, omissions_id):
        raise NotImplementedError
