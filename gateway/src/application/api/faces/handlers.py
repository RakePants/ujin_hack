from fastapi import APIRouter, Body, Depends
from punq import Container

from gateway.src.application import init_container
from gateway.src.infrastructure.integrations.app.base import BaseAppClient
from gateway.src.domain.entities.face import Face

router = APIRouter()


@router.post('/event')
async def new_event(body: dict = Body(...), container: Container = Depends(init_container)):
    app_client: BaseAppClient = container.resolve(BaseAppClient)
    await app_client.send(notification=Face.create_face(data=body))
