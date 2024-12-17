import pandas as pd
from pymongo import MongoClient
from datetime import datetime

# Configuración de MongoDB
client = MongoClient("mongodb://localhost:27017/")  # URL de conexión
db = client.citybikes_db  # Nombre de la base de datos
collection = db.stations  # Nombre de la colección

# Función para leer los datos de MongoDB y convertirlos en un DataFrame
def leer_datos():
    try:
        # Obtener todos los documentos de la colección
        datos = collection.find()

        # Lista para almacenar los datos filtrados
        datos_filtrados = []

        # Iterar sobre los documentos y filtrar los campos necesarios
        for documento in datos:
            datos_filtrados.append({
                "id": documento.get("id"),
                "name": documento.get("name"),
                "timestamp": documento.get("timestamp"),
                "free_bikes": documento.get("free_bikes"),
                "empty_slots": documento.get("empty_slots"),
                "uid": documento.get("extra", {}).get("uid"),
                "last_updated": documento.get("extra", {}).get("last_updated"),
                "slots": documento.get("extra", {}).get("slots"),
                "normal_bikes": documento.get("extra", {}).get("normal_bikes"),
                "ebikes": documento.get("extra", {}).get("ebikes")
            })

        # Si no se encontraron datos
        if not datos_filtrados:
            print("No se encontraron datos en la colección.")
            return None

        # Convertir la lista de datos filtrados en un DataFrame de pandas
        df = pd.DataFrame(datos_filtrados)

        # Convertir el campo 'timestamp' a formato datetime (si no está en el formato correcto)
        if 'timestamp' in df.columns:
            df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')

        return df
    
    except Exception as e:
        print(f"Error al leer los datos: {e}")
        return None

# Función para exportar el DataFrame a formatos CSV y Parquet
def exportar_datos(df):
    try:
        if df is not None:
            # Exportar a formato CSV
            df.to_csv("bicicoruña_datos.csv", index=False)
            print("Datos exportados a CSV correctamente.")
            
            # Exportar a formato Parquet
            df.to_parquet("bicicoruña_datos.parquet", index=False)
            print("Datos exportados a Parquet correctamente.")
        else:
            print("No se pudo exportar, el DataFrame está vacío.")
    except Exception as e:
        print(f"Error al exportar los datos: {e}")

# Ejecución del proceso
df = leer_datos()  # Leer los datos de MongoDB
if df is not None:
    exportar_datos(df)  # Exportar a CSV y Parquet