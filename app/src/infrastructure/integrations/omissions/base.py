import abc

from src.config.config import Config
from src.domain.entities.person import Person


class BaseOmissions(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    async def create_omission(self, person: Person, config: Config):
        pass
