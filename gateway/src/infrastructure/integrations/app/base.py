import abc
from dataclasses import dataclass

from ....domain.entities.face import Face


@dataclass
class BaseAppClient(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def format(self, notification: Face):
        raise NotImplementedError

    @abc.abstractmethod
    async def send(self, notification: Face):
        raise NotImplementedError
