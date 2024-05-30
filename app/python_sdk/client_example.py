from client import Client, Config
from models import requests


client = Client(Config(
    con_token='con-1837-89364359ef71333c0c20a5673a9ae55b', 
    host='https://api-product.mysmartflat.ru/api'
))

rm = requests.HealthCheckRequest()

res = client.execute(rm)

print(res)
