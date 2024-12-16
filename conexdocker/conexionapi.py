import requests
import time
from pymongo import MongoClient
from datetime import datetime

# Configuración de MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client.citybikes_db  # Nombre de la base de datos
collection = db.stations  # Nombre de la colección donde guardaremos los datos de las estaciones

# URL de la API de CityBikes
url = "http://api.citybik.es/v2/networks/bicicorunha"

# Función para obtener los datos de la API
def obtener_datos():
    try:
        # Realizar la solicitud a la API
        response = requests.get(url)
        # Verificar si la solicitud fue exitosa
        if response.status_code == 200:
            response.json()
            return response.json()
        else:
            print(f"Error al obtener los datos: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error de conexión: {e}")
        return None

# Función para almacenar o actualizar solo los datos de las estaciones en MongoDB
def almacenar_datos_estaciones(datos):
    try:
        # Extraer solo los datos de las estaciones
        estaciones = datos['network']['stations']  
        print(estaciones)
        # Iterar sobre las estaciones y realizar un upsert (insertar o actualizar)
        for estacion in estaciones:
            # Usar el 'id' o 'name' de la estación como criterio único para actualizarla
            # Puedes ajustar el criterio de búsqueda dependiendo de la estructura de los datos
            # En este caso, supongo que cada estación tiene un campo 'id' único
            result = collection.update_one(
                {'id': estacion['id']},  # Si el 'id' de la estación ya existe
                {'$set': estacion},  # Actualizar los datos de la estación
                upsert=True  # Si no existe, insertar un nuevo documento
            )

            if result.modified_count > 0:
                print(f"Estación {estacion['id']} actualizada correctamente.")
            elif result.upserted_id:
                print(f"Estación {estacion['id']} insertada correctamente.")
            else:
                print(f"Estación {estacion['id']} ya estaba actualizada.")
        print(f"Datos de {len(estaciones)} estaciones procesados.")
    except Exception as e:
        print(f"Error al almacenar los datos de las estaciones: {e}")

# Función principal que obtiene y almacena los datos de las estaciones a intervalos regulares
def ejecutar(intervalo):
    while True:
        print("Obteniendo datos de las estaciones de la API...")
        datos = obtener_datos()
        if datos:
            almacenar_datos_estaciones(datos)
        # Esperar el intervalo antes de obtener los datos nuevamente
        print(f"Esperando {intervalo} segundos para la próxima ejecución...")
        time.sleep(intervalo)

# Intervalo en segundos (5 minutos)
intervalo = 300

# Iniciar la ejecución
ejecutar(intervalo)
