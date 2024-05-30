from motor.motor_asyncio import AsyncIOMotorClient
import punq

from app.python_sdk.client import Client, Config as UJINConfig

from app.src.infrastructure.repositories.base import BasePersonsRepository
from app.src.infrastructure.repositories.mongo_repository import MongoPersonsRepository
from app.src.infrastructure.integrations.submissions import BaseSubmission, UJINSubmissions
from app.src.infrastructure.integrations.omissions import BaseOmissions, UJINOmission
from app.src.config.config import Config as AppConfig


def init_container() -> punq.Container:
    container: punq.Container = punq.Container()
    config: AppConfig = container.register(AppConfig, instance=AppConfig(), scope=punq.Scope.singleton)

    def create_mongodb_client():
        return AsyncIOMotorClient(
            config.MONGODB_CONNECTION_URI
        )

    #container.register(AsyncIOMotorClient, factory=create_mongodb_client, scope=punq.Scope.singleton)
    #client = container.resolve(AsyncIOMotorClient)
#
    #def init_mongodb_repository() -> BasePersonsRepository:
    #    return MongoPersonsRepository(
    #        mongo_db_client=container.resolve(client),
    #        mongo_db_name='logs'
    #    )
#
    #container.register(BasePersonsRepository, factory=init_mongodb_repository(), scope=punq.Scope.singleton)

    ujin_client: Client = Client(UJINConfig(con_token=config.UJIN_TOKEN))

    def init_submission_integration() -> BaseSubmission:
        return UJINSubmissions(client=ujin_client)

    def init_omission_integration() -> BaseOmissions:
        return UJINOmission(client=ujin_client)

    container.register(BaseSubmission, factory=init_submission_integration, scope=punq.Scope.singleton)
    container.register(BaseOmissions, factory=init_omission_integration, scope=punq.Scope.singleton)
    
    return container
