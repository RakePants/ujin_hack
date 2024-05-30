import datetime
import uuid
from typing import TypedDict


class AppFormat(TypedDict):
    face_id: uuid.UUID
    is_identified: bool
    full_name: str
    start_time: str
    end_time: str
    image: str | bytes
