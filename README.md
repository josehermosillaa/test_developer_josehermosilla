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

## Como Ejecutar el proyecto
   Windows:
        ```python manage.py makemigrations```
        ```python manage.py migrate```
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

### Tarea 2