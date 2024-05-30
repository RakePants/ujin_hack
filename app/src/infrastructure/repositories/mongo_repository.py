import uuid
from dataclasses import dataclass
from functools import wraps
from motor.core import AgnosticClient, AgnosticCollection
from motor.motor_asyncio import AsyncIOMotorCollection
import datetime

from app.src.domain.entities.person import Person
from app.src.infrastructure.repositories.base import BasePersonsRepository


@dataclass
class MongoPersonsRepository(BasePersonsRepository):
    mongo_db_client: AgnosticClient
    mongo_db_name: str

    def _get_collection(self, collection: uuid.UUID) -> AgnosticCollection:
        return self.mongo_db_client[self.mongo_db_name][str(collection)]

    async def add_new_log_for_person(self, person: Person):
        collection: AsyncIOMotorCollection = self._get_collection(person.face_id)
        async with await self.mongo_db_client.start_session() as session:
            async with session.start_transaction():
                await collection.insert_one(person.as_dict(), session=session)
        await collection.insert_one(person.as_dict())

    async def get_logs_for_person(self, person: Person):
        pass

    async def get_all_logs_by_time(self, start_time: datetime.datetime, end_time: datetime.datetime):
        pass