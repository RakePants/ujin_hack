import asyncio

from client import Client, Config
from models import requests


client = Client(Config(
    con_token='ust-739109-3fe72efd12ef86582919741571b1cb40',
    host='api-uae-test.ujin.tech'
))

rm = requests.HealthCheckRequest()

async def main():
    res = await client.execute(request_model=rm)


asyncio.run(main())
