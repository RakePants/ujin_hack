# Tutorial - User Guide¶

Предназначение этого руководства в том, чтобы показать основные возможноти UjinSDK. Оно базируется на двух столпах: [Pydantic](https://docs.pydantic.dev/latest/) и [httpx](https://www.python-httpx.org).

**Разделы**:

* [Установка](#Установка)
* [Параметры авторизации](#Параметры%20авторизации)
* [Клиентское подключение](#Клиентское%20подключение)
* [Обмен сообщениями](#Обмен%20сообщениями)
* [Requests](#Requests)
* [Responses](#Responses)
* [Errors](#Errors)

### Установка

```bash
pip install ujin-sdk
```

## Подключение, установка соединения

### Параметры авторизации

Для работы через UjinSDK, необходимо получить мастер-ключ от платформы, выдаваемый на имя приложения в ЛК Разработчика.

Создаем объект, конфигурирующий подключение клиантского приложения UjinSDK к платформе Ujin.

```Python
config = Config(
    con_token='<master-key>', 
    host='<https://cell-host.ujin>'
)
```

### Клиентское подключение

Создаем объект клиентского приложения и устанавливаем соединение с платформой Ujin.

```Python
client = Client(config=config)
```

Приложение настроено и готово к работе.

### Обмен сообщениями

Клиентское приложение предоствляет гибкий унифицированный интерфейс для составления запросов к платформе, инкапсулирая эту логику в указанном методе класса `Client`.

```Python
def execute(self, request_model: BaseRequest, **kwargs) -> BaseResponse:
    ...
```

Это основной способ послать сообщение на платформу.


## Модели

UjinSDK предоставляет гибкую объектную модель для средств языка программирования, чтобы можно было быстро и удобно управлять ресурсами на платформе Ujin.

### Requests

Запросы в сторону платформы формируются с помощью моделей `Pydantic` для валидации входных данных непосредственно перед отправкой.

```Python
TResponse = TypeVar('TResponse')

class BaseRequest(BaseModel, Generic[TResponse]):
    method: str
    endpoint: str
    headers: HeadersModel = None
    query: QueryModel = None
    body: BodyModel = None
    response_model: Type[TResponse]
```

Этот класс описывает базовую модель запроса к платформе. Его предназначение в том, чтобы классы наследники, реализующие в себе логику конкретного запроса, предоставляли клиентскому коду только интерфейс для заполнения входных данных. Инкапсулирует в себе логику валидации данных перед их отправкой.

### Responses

Успешные ответы от платформы десериализуются в объкты наследники класса `BaseResponse`. Цели все те же - валидация данных, перед отправкой пользователю и преоставление интерфейса объектной модели, чтобы гико работать с данными средствами языка.

```Python
class BaseResponse(BaseModel):
    command: str
    error: int
    message: str
    data: dict = None
    connection: dict
    token: str
    fromdomain: str
    worktime: str
```

### Errors

Обработка ошибок и генерация исключений строятся похожим образом.

```Python
class BaseError(BaseModel):
    error_code: Union[str, int]
    message: str
```

Провал в валидации объектов предыдущих моделей неизбежно приведет к генерации исключения определенного типа со стороны SDK, объект которого будет наследником указанного класса и будет содержать специфическую информацию об ошибке.


## Простейший пример клиентского приложения

```Python
from client import Client, Config
from models import requests


client = Client(Config(
    con_token='<master-key>', 
    host='<https://cell-host.ujin>'
))

request = requests.HealthCheckRequest()
response = client.execute(request_model)
```