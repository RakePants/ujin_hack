import datetime
from dataclasses import dataclass
from typing import Coroutine

from httpx import AsyncClient

from src.gateway.domain.entities.face import Face
from src.gateway.domain.values.face import AppFormat
from src.gateway.infrastructure.integrations.app.base import BaseAppClient


@dataclass
class AppClient(BaseAppClient):
    client: AsyncClient

    def format(self, notification: Face) -> AppFormat:
        return {"face_id": notification.face_id, "is_identified": notification.is_identified,
                "full_name": (f"{notification.last_name} {notification.first_name} {notification.patronymic}" if notification.first_name != '' else ''),
                "start_time": datetime.datetime.isoformat(notification.event_time),
                "end_time": datetime.datetime.isoformat(notification.event_time + datetime.timedelta(minutes=15)),
                "image": notification.image}

    async def send(self, notification: Face) -> None:
        async with self.client as async_client:
            await async_client.post('http://localhost:8081/face', json=self.format(notification=notification))
