# 🚲🚲 Datos de las paradas de bici de A Coruña

#📝🤔 De que va el proyecto?:

El proyecto utliza dos scripts en python para interactuar con una API, almacenar los datos en MongoDB y luego procesarlos y exportalos en formatos direfrentes

## ☝🤓Requisitos:
- Python 3.13 
- MongoDB en ejecución (local o remoto)
- Paquetes de Python necesarios: (Puedes intalar los paquetes usando pip)
  - `requests`
  - `pandas`
  - `pymongo`
  - `pyarrow`
  - `schedule`
    
 -Api de la que saco los datos: http://api.citybik.es/v2/networks


# 👨‍💻Descripción de los scripts:
## 👩‍💻Script 1:ConexionAPI --> Conexión a la API y almacenamiento de datos en MongoDB

El script se conecta con la API citybikes a intervalos regulares, obtiene los datos y los almacena en una base de datos MongoDB. El script ejecuta un ciclo infinito que solo se detiene cuando el usuario lo cancela manualmente. En este caso los datos que imprime son los de las paradas de bicis de A Coruña.

### 🖥Funcionalidades:
  -Conexión a la API a intervalos regulares (esta puesto cada 5 minutos pero puede modificarse facilmente).
  
  -Obtención de datos de la API.
  
  -Almacenamiento de los datos en MongoDB.
  
  -El script sigue ejecutándose hasta ser detenido por el usuario.

### ⚙ Intrucciones de uso
  -Asegura de que Mongodb este corriendo y que este puesto en el puerto: 27017 (o si lo pones em uno diferente asegurate de cambiarlo en el codigo 😉👍)

  -Ejecuta el script "*python script1.py*"
  
El script descargará y almacenará los datos de la API en MongoDB de manera continua hasta que lo detengas manualmente.

## 👨‍💻Script 2:Almacenamiento -->Carga de datos de MongoDB, procesamiento y exportación
Este script lee los datos almacenados en MongoDB, los carga en un DataFrame de pandas, y los exporta a los formatos CSV y Parquet. Puedes ejecutarlo en cualquier momento para extraer todos los documentos de la base de datos y exportarlos.

### 🖥Funcionalidades:
ee los documentos almacenados en MongoDB.
  -Extrae los campos seleccionados: 
    `id`, `name`, `timestamp`, `free_bikes`,
    `empty_slots`, `uid`, `last_updated`,
    `slots`, `normal_bikes`, `ebikes`.

  -Exporta los datos en los siguientes formatos:
    -CSV
    -Parquet

### ⚙ Intrucciones de uso
-Asegúrate de que MongoDB tenga datos almacenados (esto debe ser el resultado de la ejecución del Script 1).

-Ejecuta el script: "*python script2.py*"

## 💾 Estrutura de Base de datos en MongoDB
La base de datos MongoDB debe contener una colección con los documentos que tienen la siguiente estructura:
  {
    "id": "unique_id",
    "name": "bike_station_name",
    "timestamp": "2024-12-17T12:00:00",
    "free_bikes": 10,
    "empty_slots": 5,
    "uid": "station_uid",
    "last_updated": "2024-12-17T12:01:00",
    "slots": 20,
    "normal_bikes": 12,
    "ebikes": 8
  }
  
El Script 1 almacenará los documentos en MongoDB y el Script 2 los extraerá y los exportará en los formatos solicitados.

# 📚 Datos
-Todos los datos estan guardados en la carpeta datos

# 🔩 Dokcer

-Con el codigo del documento: docker-compose.yml podras crear la base de datos de MongoDB con docker 

-En la carpeta conexdocker ya esta preparado el scrip 1: ConexionAPI, àra ejecutarlo con dockers 

-Además podras craer una imagen de docker con el documento Dockerfile


