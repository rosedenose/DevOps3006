import datetime
from time import sleep
import requests
response = requests.get("https://github.com")
print(datetime.datetime.now())
sleep(10)
print(datetime.datetime.now())
if response.status_code == 200:
    print("all good man")