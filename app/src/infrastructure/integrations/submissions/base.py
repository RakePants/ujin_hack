import abc

from ....config.config import Config


class BaseSubmission(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    async def create_submission(self, config: Config):
        raise NotImplementedError

    @abc.abstractmethod
    async def get_submissions(self, submission_id):
        raise NotImplementedError