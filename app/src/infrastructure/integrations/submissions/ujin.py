from dataclasses import dataclass

from app.python_sdk.client import Client
from app.python_sdk.models.requests import SubmissionRequest
from app.src.infrastructure.integrations.submissions.base import BaseSubmission


# TODO реализовать методы
@dataclass
class UJINSubmissions(BaseSubmission):
    client: Client

    async def create_submission(self, submission: SubmissionRequest):
        raise NotImplementedError

    async def get_submissions(self, submission_id):
        raise NotImplementedError
