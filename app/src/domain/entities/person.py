import datetime
import uuid
from dataclasses import dataclass, asdict

from bson import ObjectId


@dataclass
class Person:
    face_id: uuid.UUID
    is_identified: bool
    first_name: str
    last_name: str
    patronymic: str
    start_time: datetime.datetime
    end_time: datetime.datetime
    image: str

    def as_dict(self):
        return asdict(self)

    def convert_from_entities_to_document(self) -> dict:
        data = {"ObjectId": ObjectId(),
                "face_id": self.face_id,
                "is_identified": self.is_identified,
                "first_name": self.first_name,
                "last_name": self.last_name,
                "patronymic": self.patronymic,
                "detection_date": self.start_time,
                "pass_issue_date": (self.start_time if self.is_identified else ''),
                "pass_expiration_date": (self.end_time if self.is_identified else ''),
                "image": self.image}


