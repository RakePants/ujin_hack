from dataclasses import dataclass
from datetime import datetime, timedelta, timezone

import httpx

from ....config.config import Config
from ....domain.entities.person import Person
from ....infrastructure.integrations.omissions.base import BaseOmissions


@dataclass
class UJINOmission(BaseOmissions):
    async def create_omission(self, person: Person, config: Config):
        query_params = {
            "token": config.UJIN_CON_TOKEN,
            "search": f"{person.last_name} {person.first_name} {person.patronymic}",
            "type": "guest",
            "apartment_id": 1467,
            "per_page": 100,
            "page": 1,
        }
        headers = {
            "Content-Type": "application/json",
        }
        url = f"https://{config.UJIN_HOST}/v1/pass/crm/get-list"

        async with httpx.AsyncClient() as client:
            response = await client.get(url, params=query_params, headers=headers)
            response.raise_for_status
        passes = response.json().get("data", {}).get("passes", [])

        if passes and any(
            pass_record.get("comment") == str(person.face_id) for pass_record in passes
        ):
            return

        current_time = datetime.now(timezone.utc)
        date_start = int(current_time.timestamp())
        date_end = int((current_time + timedelta(hours=4)).timestamp())

        body_params = {
            "apartment_id": 1467,
            "type": "guest",
            "guest_fullname": f"{person.last_name} {person.first_name} {person.patronymic}",
            "guest_phone": 78945612322,
            "brand": "ABC",
            "id_number": "a12345bc",
            "comment": str(person.face_id),
            "date_start": date_start,
            "date_end": date_end,
        }

        url = f"https://{Config.UJIN_HOST}/v1/pass/create/"
        headers = {
            "Content-Type": "application/json",
        }
        params = {
            "token": Config.UJIN_CON_TOKEN,
        }

        async with httpx.AsyncClient() as client:
            response = await client.post(
                url, json=body_params, headers=headers, params=params
            )
            response.raise_for_status()
