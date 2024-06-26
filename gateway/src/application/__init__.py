import httpx
import punq

from ..infrastructure.integrations.app.base import BaseAppClient
from ..infrastructure.integrations.app.app import AppClient


def init_container() -> punq.Container:
    container = punq.Container()
    container.register(BaseAppClient, instance=AppClient(httpx.AsyncClient()), scope=punq.Scope.singleton)
    return container
