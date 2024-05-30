import uuid
import datetime
from pydantic import BaseModel, EmailStr, UUID4, Field

from app.src.domain.entities.person import Person


class PersonRequestSchema(BaseModel):
    face_id: UUID4
    is_identified: bool
    detection_time: datetime.datetime
    image: str
    first_name: str | None = Field(default=None)
    last_name: str | None = Field(default=None)
    patronymic: str | None = Field(default=None)
    start_time: datetime.datetime | None = Field(default=None)
    end_time: datetime.datetime | None = Field(default=None)


class PersonResponseSchema(BaseModel):
    log_id: str = Field(examples=['66590de020e3f308dc579e39'])

    @classmethod
    def from_model(cls, log_id: str) -> "PersonResponseSchema":
        return PersonResponseSchema(
            log_id=log_id,
        )