import uuid
from dataclasses import dataclass, field

from bson import ObjectId


@dataclass
class Log:
    oid: ObjectId = field(default_factory=ObjectId, kw_only=True)
    face_id: uuid.UUID
    first_name: str
    last_name: str
    patronymic: str
