from app.python_sdk.models.errors import BadRequestError, UnauthorizedError, ForbiddenError, NotFoundError, ServerError
from app.python_sdk.models import BaseRequest, BaseResponse, BaseError
from .config import Config
import httpx


class Client:
    def __init__(self, config: Config) -> None:
        self._config: Config = config
        self._client = httpx.AsyncClient(base_url=f'{self._config.protocol}{self._config.host}')

    async def execute(self, request_model: BaseRequest, **kwargs) -> BaseResponse:
        response: httpx.Response = await self._client.request(
            request_model.method,
            request_model.endpoint,
            headers=(request_model.headers.model_dump(exclude_none=True) if request_model.headers else None),
            params=(request_model.query.model_dump(exclude_none=True) if request_model.query else {}).update({'token': self._config.auth.con_token, 'egt': self._config.auth.entity_guid_type}),
            json=(request_model.body.model_dump(exclude_none=True) if request_model.body else None),
            **kwargs
        )

        if response.status_code == 400:
            raise BadRequestError()
        elif response.status_code == 401:
            raise UnauthorizedError()
        elif response.status_code == 403:
            raise ForbiddenError()
        elif response.status_code == 404:
            raise NotFoundError()
        elif 500 <= response.status_code < 600:
            raise ServerError()

        try:
            return request_model.response_model(**response.json())
        except Exception as ex:
            print(ex)
            raise BaseError(ex)