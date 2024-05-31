from dataclasses import dataclass

import httpx

from app.python_sdk.client import Client
from app.python_sdk.models.requests import SubmissionRequest
from app.src.infrastructure.integrations.submissions.base import BaseSubmission
from app.src.config.config import Config


@dataclass
class UJINSubmissions(BaseSubmission):
    client: Client

    async def create_submission(self, submission: SubmissionRequest):
        url = f'{Config.UJIN_HOST}/api/v1/tck/bms/tickets/create/?token={Config.UJIN_CON_TOKEN}'
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json'
        }
        data = {
            "title": "Обнаружен посторонний!",
            "description": "На территории был обнаружен посторонний!",
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
            "extra": None
        }

        async with httpx.AsyncClient() as client:
            response = await client.post(url, headers=headers, json=data)

    async def get_submissions(self, submission_id):
        raise NotImplementedError
