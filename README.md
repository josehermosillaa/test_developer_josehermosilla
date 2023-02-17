# test_developer_josehermosilla
Se construye un proyecto en Django 4 con los requerimientos solicitados**

## Base de datos
Para el proyecto se conecto base de datos postgresql al proyecto Django
esto se realizo modificando en el settings.py.


        ```
            DATABASES = {
            "default": {
                "ENGINE": "django.db.backends.postgresql",
                "NAME": "mydatabase1",
                "USER": "admin",
                "PASSWORD": "admin",
                "HOST": "127.0.0.1",
                "PORT": "5432",
                }   
            }
        ```

como se observa el nombre de la base de datos es mydatabase1, user :admin y contraseña: admin
## Admin de Django
Se creo un usuario admin con el nombre admin y password admin, de todas formas recuerde que puede crear uno con:

En Linux o Mac:

    ``` python3 manage.py createsuperuser```
En Windows:

    ``` python manage.py createsuperuser```

## Requerimientos para el proyecto
se adjunta un archivo requirements.txt con el cual puede instalar las dependencias

    ``` pip install -r requirements.txt```
se encuentra ubicado en la carpeta del proyecto
se observan los siguientes paquetes
``` 
asgiref==3.6.0
async-generator==1.10
attrs==22.2.0
certifi==2022.12.7
charset-normalizer==3.0.1
DateTime==5.0
Django==4.1.7
exceptiongroup==1.1.0
h11==0.14.0
idna==3.4
outcome==1.2.0
psycopg2==2.9.5
PySocks==1.7.1
pytz==2022.7.1
requests==2.28.2
selenium==4.8.1
sniffio==1.3.0
sortedcontainers==2.4.0
sqlparse==0.4.3
trio==0.22.0
trio-websocket==0.9.2
urllib3==1.26.14
wsproto==1.2.0
zope.interface==5.5.2

```
## Como Ejecutar el proyecto
Se debe primero correr hacer las migraciones para poblar la base de datos

   Windows:


        ```python manage.py makemigrations```
        ```python manage.py migrate```
luego correr el servidor con

        ```python manage.py runserver```
Linux o Mac:


        ```python3 manage.py makemigrations```
        ```python3 manage.py migrate```
        ```python3 manage.py runserver```
        

## Consideraciones


* se envia la base de datos utilizadas en caso que quieran ejecutarla directamente
* se deja arriba el JSON Obtenido del script de la tarea 2
* se crearon dos aplicaciones (tarea1 y tarea2), las cuales hacen referencias a     cada una de los puntos solicitados en el test
* Se escribio un management command en Django para cada script solicitado, se explica el uso mas adelante
### Tarea 1
para esta tarea se solicito obtener los datos de "http://api.citybik.es/v2/networks/bikesantiago", para esto se escribio in script con la libreria request para traer los datos y escribirlos en django
* El script se encuentra en la app tarea1/management/commands/
* su nombre es write_bike_data.py
para ejecutarlo debe usar
```python3 manage.py write_bike_data ```

Se escribieron dos modelos (tarea1/models.py):
* Uno donde se guardo la data de la compañia llamado Networks
* class Station, que tiene los datos de las estaciones de estas bicicletas

se pueden ver los datos cargados en localhost:8000/admin/ y realizar busqueda por nombre
ademas se logro representar los datos en una tabla que se encuentra directamente en localhost:8000/
* si pulsa sobre el nombre de la estacion, podra obtener mas detalles de ella
* se agregaron colores para representar estaciones que tienen 0 Bicicletas y otros para cuando hay disponibles
### Tarea 2