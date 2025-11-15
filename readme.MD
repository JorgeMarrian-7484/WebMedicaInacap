# crear proyecto 
django-admin startproject storeProject

# ir al directorio
cd storeProject

# crear app
django-admin startapp productApp

# crear carpetas static y templates

# ejecutar el proyecto
py manage.py runserver

# instalar dependencias
pip install -r  requirements.txt

# crear migraciones
py manage.py makemigrations

# ejecutar migración
py manage.py migrate

# crear super usuario
py manage.py createsuperuser