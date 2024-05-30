import uvicorn
from fastapi import FastAPI

from src.gateway.application.api.faces import handlers


def create_app() -> FastAPI:
    app = FastAPI(
        title='GateWay API',
        version='0.0.1',
        description='GateWay для получения и отправки изображений из macroscop',
        debug=True,
        docs_url='/api/docs',
        redoc_url='/api/redoc',
    )
    app.include_router(router=handlers.router)
    return app


if __name__ == '__main__':
    uvicorn.run(create_app(), host='localhost', port=8080)
