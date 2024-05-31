import uuid

from fastapi import Depends, FastAPI, Request, Response, APIRouter, Body
from fastapi.websockets import WebSocket
from punq import Container
from pymongo.results import InsertOneResult
from starlette.websockets import WebSocketDisconnect

from app.src.application import init_container
from app.src.application.api.persons.converters import from_model_to_entity
from app.src.config.config import Config
from app.src.domain.entities.person import Person
from app.src.infrastructure.integrations.s3.base import BaseS3
from app.src.infrastructure.repositories.base import BasePersonsRepository
from app.src.application.api.persons.schema import PersonRequestSchema, PersonResponseSchema
from app.src.infrastructure.integrations.submissions import BaseSubmission
from app.src.infrastructure.integrations.omissions import BaseOmissions
from app.src.infrastructure.websockets.managers import BaseConnectionManager

router = APIRouter()


@router.post('/person',
             response_model=PersonResponseSchema,
             status_code=201)
async def get_person(person: PersonRequestSchema, container: Container = Depends(init_container)):
    print(person)
    persons_repository: BasePersonsRepository = container.resolve(BasePersonsRepository)
    connection_manager: BaseConnectionManager = container.resolve(BaseConnectionManager)
    service_s3: BaseS3 = container.resolve(BaseS3)
    submission: BaseSubmission = container.resolve(BaseSubmission)
    omission: BaseOmissions = container.resolve(BaseOmissions)
    config: Config = container.resolve(Config)
    if not person.is_identified:
        res1 = await submission.create_submission(config)
        print(res1)
    else:
        res2 = await omission.create_omission(Person(**person.dict()), config)
        print(res2)

    file_name = await service_s3.upload_image(person.image)
    converted = from_model_to_entity(person, file_name)
    print(converted)
    log: InsertOneResult = await persons_repository.add_new_log_for_person(converted)
    del converted['_id']
    print(connection_manager.connections_map, log, converted)
    await connection_manager.send_all(data=converted)

    return PersonResponseSchema.from_model(log_id=str(log.inserted_id))


@router.websocket('/realtime')
async def realtime(websocket: WebSocket, container: Container = Depends(init_container)):
    connection_manager: BaseConnectionManager = container.resolve(BaseConnectionManager)
    await connection_manager.accept_connection(websocket, websocket.client.host)
    print(connection_manager.connections_map)
    try:
        while True:
            await websocket.receive_json()
    except WebSocketDisconnect:
        await connection_manager.remove_connection(websocket=websocket, key=websocket.client.host)