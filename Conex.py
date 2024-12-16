import requests
import time
from pymongo import MongoClient
from datetime import datetime

url = "http://api.citybik.es/v2/networks/bicicorunha"


response = requests.get(url)

data = response.json()
print(data)