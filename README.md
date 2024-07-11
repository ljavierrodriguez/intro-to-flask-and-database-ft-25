### Habilitar el comando flask

Windows:
```shell
SET FLASK_APP=app.py
```

Linux o Mac:
```shell
export FLASK_APP=app.py
```

### Comandos para generar las migraciones

Crear la carpeta migrations
```shell
flask db init
```

Crear las migrationes
```shell
flask db migrate
```

Ejecutar las migraciones en la base de datos
```shell
flask db upgrade
```


### Para trabajar con MySQL o PostgreSQL 

Mysql port 3306
```shell
pipenv install pymysql
```
Actualizar el ***.env*** con la siguiente estructura
```env
# DATABASE=mysql+pymysql://<user>:<pass>@<host>:<port>/database_name
DATABASE=mysql+pymysql://root:root@localhost:3306/prueba
```
PostgreSQL port 5432
```shell
pipenv install psycopg2-binary
```
Actualizar el ***.env*** con la siguiente estructura
```env
# DATABASE=postgresql+psycopg2://<user>:<pass>@<host>:<port>/database_name
DATABASE=postgresql+psycopg2://postgres:postgres@localhost:5432/prueba
```