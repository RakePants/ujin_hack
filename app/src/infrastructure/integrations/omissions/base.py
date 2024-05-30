import abc


class BaseOmissions(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    async def create_omission(self, omission):
        raise NotImplementedError

    @abc.abstractmethod
    async def get_omission(self, omissions_id):
        raise NotImplementedError
