from pydantic import BaseModel


class InternalServerError(BaseModel, Exception):
    pass


class InvallidRequestData(BaseModel, Exception):
    pass
