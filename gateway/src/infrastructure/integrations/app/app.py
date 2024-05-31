import datetime
from dataclasses import dataclass

from httpx import AsyncClient

from gateway.src.domain.entities.face import Face
from gateway.src.domain.values.face import AppFormat, AppFormatIdentified
from gateway.src.infrastructure.integrations.app.base import BaseAppClient


@dataclass
class AppClient(BaseAppClient):
    client: AsyncClient

    def format(self, notification: Face) -> AppFormat | AppFormatIdentified:
        data = {"face_id": notification.face_id, "is_identified": notification.is_identified,
                "detection_time": datetime.datetime.isoformat(notification.event_time),
                "image": notification.image}
        if not notification.is_identified:
            return data
        else:
            data["first_name"] = notification.first_name,
            data["last_name"] = notification.last_name,
            data["patronymic"] = notification.patronymic,
            data['start_time'] = datetime.datetime.isoformat(notification.event_time)
            data['end_time'] = datetime.datetime.isoformat(notification.event_time + datetime.timedelta(minutes=15))
            return data

    async def send(self, notification: Face) -> None:
        async with self.client as async_client:
            await async_client.post('http://77.223.100.176:8081/person', json=self.format(notification=notification))
