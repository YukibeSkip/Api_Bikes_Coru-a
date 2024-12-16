

import requests
import json
#from pymongo import MongoClient

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

id = []
name =[]
location = []
href = []
company = []
license =[]
ebikes =[]
gbfs_href =[]
stations =[]


import requests


response = requests.get(endpoint)


# Verificar si la solicitud fue exitosa
print(response)

# print(response)

# for i in paradas["network"]:
#     name.append(i["name"])
#     stations.append(i['stations'])
#     company.append(i['company'])
#     href.append(i['href'])
#     location.append(i['location'])
#     id.append(i["id"])

# datos = {"Name":name, "Sations":stations, "Company":company, "href":href, "Location":location, "Id":id}

#print(datos)
