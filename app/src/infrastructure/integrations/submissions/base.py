import abc


class BaseSubmission(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    async def create_submission(self, submission):
        raise NotImplementedError

    @abc.abstractmethod
    async def get_submissions(self, submission_id):
        raise NotImplementedError