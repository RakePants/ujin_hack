import uuid
from typing import TypedDict


class AppFormat(TypedDict):
    face_id: uuid.UUID
    is_identified: bool
    detection_time: str
    image: str | bytes


class AppFormatIdentified(AppFormat):
    first_name: str
    last_name: str
    patronymic: str
    start_time: str
    end_time: str
