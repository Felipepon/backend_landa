# backend_landa
# Proyecto Django con Celery y Documentos DANE

Este proyecto es una aplicación Django que permite la gestión de perfiles de usuario y documentos. Además, incluye una funcionalidad para descargar y actualizar documentos automáticamente desde el sitio web del DANE utilizando Celery.

## Requisitos

- Python 
- Django
- Django Rest Framework
- Celery
- PostgreSQL (u otro gestor de base de datos compatible)
- Redis (como broker de mensajes para Celery)

## Instalación

1. Clona el repositorio:

   ```sh
   git clone git@github.com:Felipepon/backend_landa.git
   cd myproject

2. Crea un entorno virtual e instala las dependencias:

    ```sh
    python -m venv env
    source env/bin/activate
    pip install -r requirements.txt

3. Configura la base de datos en config/database.yml:

    ```yaml
    default: &default
    adapter: postgresql
    encoding: unicode
    pool: 5
    username: your_username
    password: your_password

    development:
    <<: *default
    database: your_database_name

    test:
    <<: *default
    database: your_database_name_test

    production:
    <<: *default
    database: your_database_name_production

4. Realiza las migraciones de la base de datos:
     ```sh
    python manage.py makemigrations
    python manage.py migrate

5. Crea un superusuario para acceder al admin de Django:

    ```sh
    python manage.py createsuperuser

6. Inicia el servidor de desarrollo:

    ```sh
    python manage.py runserver

