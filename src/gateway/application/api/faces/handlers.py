from fastapi import APIRouter, Body, Depends
from punq import Container

from src.gateway.application import init_container
from src.gateway.infrastructure.integrations.app.base import BaseAppClient
from src.gateway.domain.entities.face import Face

router = APIRouter()


@router.post('/event')
async def new_event(body: dict = Body(...), container: Container = Depends(init_container)):
    app_client: BaseAppClient = container.resolve(BaseAppClient)
    print(body)
    await app_client.send(notification=Face.create_face(data=body))
