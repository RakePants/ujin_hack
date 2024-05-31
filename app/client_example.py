from python_sdk.client import Client, Config
from python_sdk.models import requests


client = Client(Config(
    con_token='ust-739109-3fe72efd12ef86582919741571b1cb40',
    host='https://api-uae-test.ujin.tech'
))

rm = requests.HealthCheckRequest()

res = client.execute(rm)

