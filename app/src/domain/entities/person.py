import datetime
import uuid
from dataclasses import dataclass, asdict


@dataclass
class Person:
    face_id: uuid.UUID
    is_identified: bool
    detection_time: datetime.datetime
    image: str
    first_name: str | None
    last_name: str | None
    patronymic: str | None
    start_time: datetime.datetime | None
    end_time: datetime.datetime | None

    def as_dict(self):
        return asdict(self)

    def convert_from_entities_to_document(self) -> dict:
        data = {"face_id": str(self.face_id),
                "is_identified": self.is_identified,
                "first_name": self.first_name,
                "last_name": self.last_name,
                "patronymic": self.patronymic,
                "detection_date": self.start_time,
                "pass_issue_date": (self.start_time if self.is_identified else None),
                "pass_expiration_date": (self.end_time if self.is_identified else None),
                "image": self.image}
        return data


