from motor.motor_asyncio import AsyncIOMotorClient
import punq
from functools import lru_cache

from app.src.infrastructure.repositories.base import BasePersonsRepository
from app.src.infrastructure.repositories.mongo_repository import MongoPersonsRepository
from app.src.infrastructure.integrations.submissions import BaseSubmission, UJINSubmissions
from app.src.infrastructure.integrations.omissions import BaseOmissions, UJINOmission
from app.src.config.config import Config as AppConfig
from app.src.infrastructure.websockets.managers import BaseConnectionManager, ConnectionManager
from app.src.infrastructure.integrations.s3 import BaseS3, ServiceS3


@lru_cache(maxsize=None)
def init_container() -> punq.Container:
    container: punq.Container = punq.Container()
    container.register(AppConfig, instance=AppConfig(), scope=punq.Scope.singleton)
    config: AppConfig = container.resolve(AppConfig)

    def create_mongodb_client():
        return AsyncIOMotorClient(
            config.MONGODB_CONNECTION_URI
        )

    container.register(AsyncIOMotorClient, factory=create_mongodb_client, scope=punq.Scope.singleton)
    client: AsyncIOMotorClient = container.resolve(AsyncIOMotorClient)

    def init_mongodb_repository() -> BasePersonsRepository:
        return MongoPersonsRepository(
            mongo_db_client=client,
            mongo_db_name='logs'
        )

    container.register(BasePersonsRepository, factory=init_mongodb_repository, scope=punq.Scope.singleton)

    def init_submission_integration() -> BaseSubmission:
        return UJINSubmissions()

    def init_omission_integration() -> BaseOmissions:
        return UJINOmission()

    container.register(BaseSubmission, factory=init_submission_integration, scope=punq.Scope.singleton)
    container.register(BaseOmissions, factory=init_omission_integration, scope=punq.Scope.singleton)

    container.register(BaseConnectionManager, instance=ConnectionManager(), scope=punq.Scope.singleton)

    container.register(BaseS3, instance=ServiceS3(), scope=punq.Scope.singleton)
    
    return container
