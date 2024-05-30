import uvicorn
from fastapi import FastAPI, Body

app = FastAPI()


@app.post('/face')
async def face(body: dict = Body(...)):
    print(body)


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8081)
