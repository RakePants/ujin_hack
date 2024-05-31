import uuid

from fastapi import Depends, FastAPI, Request, Response, APIRouter, Body
from punq import Container
from pymongo.results import InsertOneResult

from app.src.application import init_container
from app.src.domain.entities.person import Person
from app.src.infrastructure.repositories.base import BasePersonsRepository
from app.src.application.api.persons.schema import PersonRequestSchema, PersonResponseSchema
from app.src.infrastructure.integrations.submissions import BaseSubmission
from app.src.infrastructure.integrations.omissions import BaseOmissions
from app.python_sdk.models.requests import SubmissionRequest, CreateOmissionRequest

router = APIRouter()


@router.post('/person',
             response_model=PersonResponseSchema,
             status_code=201)
async def get_person(person: PersonRequestSchema, container: Container = Depends(init_container)):
    print(person)
    persons_repository: BasePersonsRepository = container.resolve(BasePersonsRepository)
    log: InsertOneResult = await persons_repository.add_new_log_for_person(Person(**person.dict()))
    submission: BaseSubmission = container.resolve(BaseSubmission)
    omission: BaseOmissions = container.resolve(BaseOmissions)
    res1 = await submission.create_submission(SubmissionRequest())
    res2 = await omission.create_omission(person)
    print(res1, res2)

    return PersonResponseSchema.from_model(log_id=str(log.inserted_id))
