import abc


class BaseOmissions(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    async def create_omission(self, omission):
        pass
