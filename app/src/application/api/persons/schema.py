import uuid
import datetime
from pydantic import BaseModel, EmailStr, UUID4, Field


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

    def to_dict(self) -> dict:
        #data = {'face_id': str(self.face_id), 'is_identified': self.is_identified, "detection_time": self.detection_time.isoformat(),
        #        "image": }
        #data['face_id'] = str(data['face_id'])
        #return data
        ...


class PersonResponseSchema(BaseModel):
    log_id: str = Field(examples=['66590de020e3f308dc579e39'])

    @classmethod
    def from_model(cls, log_id: str) -> "PersonResponseSchema":
        return PersonResponseSchema(
            log_id=log_id,
        )