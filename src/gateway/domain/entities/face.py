import base64
import datetime
import uuid
from dataclasses import dataclass, asdict


@dataclass
class Face:
    face_id: uuid.UUID | str
    is_identified: bool | str
    event_time: datetime.datetime | str
    image: bytes | str
    first_name: str
    last_name: str
    patronymic: str

    def __post_init__(self) -> None:
        if isinstance(self.image, bytes):
            self.image = base64.b64encode(self.image)
        if isinstance(self.event_time, str):
            self.event_time = datetime.datetime.strptime(self.event_time, "%d.%m.%Y %H:%M:%S.%f")
        if isinstance(self.is_identified, str):
            self.is_identified = bool(self.is_identified)

    def as_generic_type(self) -> dict:
        return asdict(self)

    @classmethod
    def create_face(cls, data: dict) -> 'Face':
        return Face(**data)
