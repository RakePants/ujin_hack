from models.errors import BadRequestError, UnauthorizedError, ForbiddenError, NotFoundError, ServerError
from models import BaseRequest, BaseResponse, BaseError
from .config import Config
import httpx


class Client:
    def __init__(self, config: Config) -> None:
        self._config: Config = config
        self._client = httpx.Client(base_url=f'{self._config.protocol}{self._config.host}')

    def execute(self, request_model: BaseRequest, **kwargs) -> BaseResponse:
        response: httpx.Response = self._client.request(
            request_model.method,
            request_model.endpoint,
            headers=request_model.headers.model_dump(exclude_none=True),
            params=request_model.query.model_dump(exclude_none=True).update({'token': self._config.auth.con_token, 'egt': self._config.auth.entity_guid_type}),
            json=request_model.body.model_dump(exclude_none=True),
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
            raise BaseError(ex)