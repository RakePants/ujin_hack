import abc


class BaseS3(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    async def upload_image(self, file: str):
        raise NotImplementedError
