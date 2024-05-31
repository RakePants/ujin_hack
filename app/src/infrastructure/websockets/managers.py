import asyncio
from abc import (
    ABC,
    abstractmethod,
)
from collections import defaultdict
from dataclasses import (
    dataclass,
    field,
)

from fastapi import WebSocket


@dataclass
class BaseConnectionManager(ABC):
    connections_map: dict[str, WebSocket] = field(
        default_factory=lambda: dict(),
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
        self.connections_map[key] = websocket

    async def remove_connection(self, websocket: WebSocket, key: str):
        del self.connections_map[key]

    async def send_all(self, data: dict):
        for websocket in self.connections_map.values():
            await websocket.send_json(data)

    async def disconnect_all(self, key: str):
        for websocket in self.connections_map.values():
            await websocket.close()
