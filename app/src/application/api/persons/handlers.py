from fastapi import Depends, FastAPI, Request, Response, APIRouter, Body
from punq import Container

from app.src.application import init_container
from app.src.infrastructure.repositories.base import BasePersonsRepository

router = APIRouter()


@router.post('/person')
async def get_person(body: dict = Body(...), container: Container = Depends(init_container)):
    print(body)
    #persons_repository: BasePersonsRepository = container.resolve(BasePersonsRepository)
    #await persons_repository.add_new_log_for_person()