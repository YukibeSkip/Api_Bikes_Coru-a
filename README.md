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
##Script 1:ConexionAPI --> Conexión a la API y almacenamiento de datos en MongoDB

El script se conecta con la API citybikes a intervalos regulares, obtiene los datos y los almacena en una base de datos MongoDB. El script ejecuta un ciclo infinito que solo se detiene cuando el usuario lo cancela manualmente. En este caso los datos que imprime son los de las paradas de bicis de A Coruña.

### 🖥Funcionalidades:
  -Conexión a la API a intervalos regulares (esta puesto cada 5 minutos pero puede modificarse facilmente).
  
  -Obtención de datos de la API.
  
  -Almacenamiento de los datos en MongoDB.
  
  -El script sigue ejecutándose hasta ser detenido por el usuario.

###⚙ Intrucciones de uso
  -Asegura de que Mongodb este corriendo y que este puesto en el puerto: 27017 (o si lo pones em uno diferente asegurate de cambiarlo en el codigo 😉👍)

  -Ejecuta el script "python script1.py"
