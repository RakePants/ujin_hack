import uuid
import datetime
from pydantic import BaseModel, EmailStr, UUID4

from app.src.domain.entities.person import Person


class CreateUserRequestSchema(BaseModel):
    face_id: UUID4
    is_identified: bool
    first_name: str
    last_name: str
    patronymic: str
    start_time: datetime.datetime
    end_time: datetime.datetime
    image: str


class CreateUserResponseSchema(BaseModel):
    log_id: uuid.UUID

    @classmethod
    def from_model(cls, person: Person) -> "CreateUserResponseSchema":
        return CreateUserResponseSchema(
            log_id=str(uuid.uuid4()),
        )