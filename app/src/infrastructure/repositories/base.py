import abc
import datetime
from dataclasses import dataclass

from app.src.domain.entities.person import Person


@dataclass
class BasePersonsRepository(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    async def add_new_log_for_person(self, person: Person):
        raise NotImplementedError

    @abc.abstractmethod
    async def get_logs_for_person(self, person: Person):
        raise NotImplementedError

    @abc.abstractmethod
    async def get_all_logs_by_time(self, start_time: datetime.datetime, end_time: datetime.datetime):
        raise NotImplementedError
