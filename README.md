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

El script se conecta con la API citybikes a intervalos regulares (yo le puse cada 5 minutos pero puede ser mas o menos), obtiene los datos y los almacena en una base de datos MongoDB. El script ejecuta un ciclo infinito que solo se detiene cuando el usuario lo cancela manualmente. En este caso los datos que imprime son los de las paradas de bicis de A Coruña.


