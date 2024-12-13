

import requests
from pymongo import MongoClient

# try:
#     eri = "mongodb://localhost:27017/"
#     client = MongoClient(eri)

#     print("Connected successfully")
#         # other application code
#     client.close()
# except Exception as e:
#     raise Exception(
#         "The following error occurred: ", e)
endpoint = "http://api.citybik.es/v2/networks"

datos = requests.get(endpoint)

# for network in datos['network']:
#         # Verificamos si el nombre de la red es 'BiciCoruña'
#         if network['name'] == 'Bicicoruña':
#             print(network)
