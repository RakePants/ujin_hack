import uvicorn
from fastapi import FastAPI, Request, Response

from app.src.application.api.persons import handlers


def create_app():
    app = FastAPI(

    )
    app.include_router(handlers.router)

    return app


if __name__ == '__main__':
    uvicorn.run(app=create_app(), host='localhost', port=8081)