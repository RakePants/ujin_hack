from abc import (
    ABC,
    abstractmethod,
)
from dataclasses import (
    dataclass,
    field,
)

from fastapi import WebSocket


@dataclass
class BaseConnectionManager(ABC):
    connections_map: list[WebSocket] = field(
        default_factory=list,
        kw_only=True,
    )

    @abstractmethod
    async def accept_connection(self, websocket: WebSocket, key: str):
        ...

    @abstractmethod
    async def remove_connection(self, websocket: WebSocket, key: str):
        ...

    @abstractmethod
    async def send_all(self, data: dict):
        ...

    @abstractmethod
    async def disconnect_all(self, key: str):
        ...


@dataclass
class ConnectionManager(BaseConnectionManager):
    async def accept_connection(self, websocket: WebSocket, key: str):
        await websocket.accept()
        self.connections_map.append(websocket)

    async def remove_connection(self, websocket: WebSocket, key: str):
        self.connections_map.remove(websocket)

    async def send_all(self, data: dict):
        for websocket in self.connections_map:
            await websocket.send_json(data)

    async def disconnect_all(self, key: str):
        for websocket in self.connections_map:
            await websocket.close()
