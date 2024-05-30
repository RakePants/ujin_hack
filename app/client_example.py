from client import Client, Config
from models import requests


client = Client(Config(
    con_token='sfd',
    host='https://api-product.mysmartflat.ru/api'
))

rm = requests.HealthCheckRequest()

res = client.execute(rm)

print(res)
