import uuid
from dataclasses import dataclass
from motor.core import AgnosticClient, AgnosticCollection
from motor.motor_asyncio import AsyncIOMotorCollection
import datetime

from pymongo.results import InsertOneResult

from ...domain.entities.person import Person
from ...infrastructure.repositories.base import BasePersonsRepository


@dataclass
class MongoPersonsRepository(BasePersonsRepository):
    mongo_db_client: AgnosticClient
    mongo_db_name: str

    def _get_collection(self, collection: uuid.UUID) -> AgnosticCollection:
        return self.mongo_db_client[self.mongo_db_name][str(collection)]

    async def add_new_log_for_person(self, inserted_data: dict) -> InsertOneResult:
        collection: AsyncIOMotorCollection = self._get_collection(inserted_data["face_id"])
        async with await self.mongo_db_client.start_session() as session:
            return await collection.insert_one(inserted_data, session=session)

    async def get_logs_for_person(self, person: Person):
        pass

    async def get_all_logs_by_time(self, start_time: datetime.datetime, end_time: datetime.datetime):
        pass
