import requests

endpoint = "http://api.citybik.es/v2/networks/velib"

response = requests.get(endpoint)

# Listas para almacenar los datos
id = []
name = []
location = []
href = []
company = []
license = []
ebikes = []
gbfs_href = []
stations = []

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    data = response.json()
else:
    print("Error al obtener datos de la API")
    data = None  # Si no es exitoso, asignamos None a data y evitamos continuar con el ciclo

# Procesar la información si se recibe una respuesta válida
if data and "network" in data:
    networks = data["network"]
    found = False  # Variable para saber si encontramos la red de "bicicoruña"
    
    for network in networks:  # Iterar sobre todas las redes
          # Verificar que network sea un diccionario y tenga la clave 'name'
        if "velib" in network["id"]:  # Comparación insensible a mayúsculas/minúsculas
            id.append(network["id"])
            name.append(network["name"])
            location.append(network["location"])
            href.append(network["href"])
            company.append(network["company"])
            license.append(network["license"])
            ebikes.append(network["ebikes"])
            gbfs_href.append(network["gbfs_href"])
            stations.append(network["stations"])
            found = True
            break  # Detener el ciclo si encontramos la red

    if not found:
        print("No se encontró la red 'bicicoruña'.")
else:
    print("No se encontraron datos en 'networks'.")

# Crear el diccionario con los resultados
datos = {
    "Id": id,
    "name": name,
    "location": location,
    "href": href,
    "company": company,
    "license": license,
    "ebikes": ebikes,
    "gbfs_href": gbfs_href,
    "stations": stations
}

# Mostrar los resultados
print(datos)
