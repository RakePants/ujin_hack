import base64
import datetime
import uuid
from dataclasses import dataclass, asdict


@dataclass
class Face:
    face_id: uuid.UUID
    is_identified: bool
    event_time: datetime.datetime | str
    image: bytes | str
    first_name: str | None
    last_name: str | None
    patronymic: str | None

    def __post_init__(self) -> None:
        if isinstance(self.image, bytes):
            self.image = base64.b64encode(self.image)
        if isinstance(self.event_time, str):
            self.event_time = datetime.datetime.strptime(self.event_time, "%d.%m.%Y %H:%M:%S.%f")
        if isinstance(self.is_identified, str):
            self.is_identified = (True if self.is_identified == "True" else False)

    def as_generic_type(self) -> dict:
        return asdict(self)

    @classmethod
    def create_face(cls, data: dict) -> 'Face':
        return Face(**data)
