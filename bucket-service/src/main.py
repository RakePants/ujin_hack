from fastapi import FastAPI
from src.api import s3_router
import uvicorn

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


app.include_router(s3_router)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
