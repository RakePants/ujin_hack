from dataclasses import dataclass

from app.python_sdk.client import Client
from app.python_sdk.models.requests import (
    CreateOmissionRequest,
    GetOmissionsListRequest,
)
from app.src.domain.entities.person import Person
from app.src.infrastructure.integrations.omissions.base import BaseOmissions


@dataclass
class UJINOmission(BaseOmissions):
    client: Client

    async def create_omission(self, person: Person):
        request = GetOmissionsListRequest.create_with_params(
            full_name=f"{person.last_name} {person.first_name} {person.patronymic}"
        )
        
        response = await self.client.execute(request)
        body = response.model_dump()

        if body.data.passes:
            if any(d.comment == str(person.face_id) for d in body.data.passes):
                return

        request = CreateOmissionRequest.create_with_params(
            full_name=f"{person.last_name} {person.first_name} {person.patronymic}",
            face_id=person.face_id,
        )

        await self.client.execute(request)
