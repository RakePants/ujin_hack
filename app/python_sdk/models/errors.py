from typing import Union
from pydantic import BaseModel


class BaseError(BaseModel):
    error_code: Union[str, int]
    message: str


class BadRequestError(BaseError):
    pass


class UnauthorizedError(BaseError):
    pass


class ForbiddenError(BaseError):
    pass


class NotFoundError(BaseError):
    pass


class ServerError(BaseError):
    pass


class InvallidRequestData(BaseModel):
    pass
