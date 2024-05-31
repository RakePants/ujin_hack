from dataclasses import dataclass

from app.python_sdk.client import Client
from app.python_sdk.models.requests import SubmissionRequest
from app.src.infrastructure.integrations.submissions.base import BaseSubmission


@dataclass
class UJINSubmissions(BaseSubmission):
    client: Client

    async def create_submission(self, submission: SubmissionRequest):
        print(submission)
        return await self.client.execute(request_model=submission)

    async def get_submissions(self, submission_id):
        raise NotImplementedError
