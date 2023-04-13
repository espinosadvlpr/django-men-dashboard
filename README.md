# BACKEND PARA EL DESARROLLO DE UN DASHBOARD USANDO DJANGO

Para el desarrollo de esta aplicacion se uso la informacion publica del SNIES perteneciente
al Ministerio de Educación Nacional.

## Requisitos para el proyecto

Para poder ejecutar correctamente el proyecto es necesario tener instalando `Python`,
ademas de un servidor de bases de datos como **[MySQL](https://dev.mysql.com/downloads/workbench/)** o `MariaDB`.

## Clonando del proyecto

Primero debe clonar este repositorio usando el comando:

```
$ git clone https://github.com/espinosadvlpr/django-men-dashboard.git
```

## Instalando el proyecto

Si desea trabajar sobre un entorno virtual de Python puede dar [clic aqui](https://www.geeksforgeeks.org/creating-python-virtual-environment-windows-linux/)
para seguir un tutorial para instalar un entorno virtual en el sistema operativo que desee.

Realice la instalación de las librerias necesarias para la ejecución del proyecto usando el comando

```
$ pip install -r requirements.txt
```

Edite la configuración de usuario y contraseña de `MySQL` para la conexion de la base de datos en la linea 78 del archivo `dashboard_men/settings.py`

**NOTA:** debe crear previamente una base de datos para el proyecto y agregar el nombre a la configuración en el campo "[database_name]".

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '[database_name]',
        'USER': '',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

Una vez cambiada la información para la conexión a la base de datos y las librerias necesarias esten instaladas, debe realizar lo siguiente para la migración
de las tablas a la base de datos creada previamente en **MySQL**.

```
$ python manage.py makemigrations
$ python manage.py migrate
```

Para realizar la inserción de los datos, edite la configuración de usuario y contraseña de la base de datos para la conexion de la con **MySQL**
en la linea 11 del script `data_management.py`:

```
'mysql+pymysql://[user]:[password]@127.0.0.1/[database_name]'
```

Ejecutando el script con el siguiente comando se realizara la inserción de los datos en **MySQL**:

```
$ python data_management.py
```

Para ejecutar el proyecto de **Django** debe usar el siguiente comando:

```
$ python manage.py runserver
```

## Funcionamiento del proyecto

- Para ingresar a la API en el navegador ingrese el siguiente link <http://127.0.0.1:8000/api/>

- Si desea revisar los datos subidos al proyecto lo puede realizar desde el `admin`:

Cree un usuario administrador con el comando :

```
$ python manage.py createsuperuser
```

Una vez creado el usuario, para ingresar al `admin` en el navegador ingrese el siguiente link <http://127.0.0.1:8000/admin>

## Endpoints de la API

1. Para hacer una petición GET a todos los datos del proyecto:

```
GET http://localhost:8000/api/men_info
```

2. Para hacer una peticion GET a cada una de las preguntas del dashboard:

```
GET http://localhost:8000/api/first_question/
GET http://localhost:8000/api/second_question/
GET http://localhost:8000/api/third_question/
GET http://localhost:8000/api/fourth_question/
GET http://localhost:8000/api/fifth_question/
GET http://localhost:8000/api/sixth_question/
GET http://localhost:8000/api/seventh_question/
GET http://localhost:8000/api/eight_question/
GET http://localhost:8000/api/ninth_question/
GET http://localhost:8000/api/tenth_question/
```
