import requests
import time
from pymongo import MongoClient
from datetime import datetime

# Configuración de MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client.citybikes_db  # Nombre de la base de datos
collection = db.networks  # Nombre de la colección donde guardaremos los datos

# URL de la API de CityBikes
url = "http://api.citybik.es/v2/networks/bicicorunha"
# Función para obtener los datos de la API
def obtener_datos():
    try:
        # Realizar la solicitud a la API
        response = requests.get(url)
        # Verificar si la solicitud fue exitosa
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error al obtener los datos: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error de conexión: {e}")
        return None

# Función para almacenar los datos en MongoDB
def almacenar_datos(datos):
    try:
        # Agregar la fecha y hora de la captura de datos
        datos['fecha_captura'] = datetime.now()
        # Insertar los datos en la colección de MongoDB
        collection.insert_one(datos)
        print("Datos almacenados correctamente.")
    except Exception as e:
        print(f"Error al almacenar los datos: {e}")

# Función principal que obtiene y almacena los datos a intervalos regulares
def ejecutar(intervalo):
    while True:
        print("Obteniendo datos de la API...")
        datos = obtener_datos()
        if datos:
            almacenar_datos(datos)
        # Esperar el intervalo antes de obtener los datos nuevamente
        print(f"Esperando {intervalo} segundos para la próxima ejecución...")
        time.sleep(intervalo)

# Intervalo en segundos (por ejemplo, 10 minutos = 600 segundos)
intervalo = 300

# Iniciar la ejecución
ejecutar(intervalo)
