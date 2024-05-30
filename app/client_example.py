from python_sdk.client import Client, Config
from python_sdk.models import requests


client = Client(Config(
    con_token='sfd',
    host='https://api-uae-test.ujin.tech'
))

rm = requests.HealthCheckRequest()

res = client.execute(rm)

print(res)
