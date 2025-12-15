#!/bin/bash
# Script para inicializar el proyecto MediWeb con roles y datos de prueba

echo "🚀 Inicializando MediWeb..."

# Crear grupos de permisos
echo "📌 Creando grupos de permisos..."
python manage.py crear_grupos

# Crear superuser (admin)
echo "👨‍💼 ¿Deseas crear un usuario administrador? (s/n)"
read -r create_admin

if [ "$create_admin" = "s" ]; then
    echo "Ingresa los datos del administrador:"
    python manage.py createsuperuser
fi

# Ejecutar populate_db
echo "📊 ¿Deseas poblar la base de datos con datos de prueba? (s/n)"
read -r populate

if [ "$populate" = "s" ]; then
    echo "Poblando base de datos..."
    python populate_db.py
fi

# Iniciar servidor
echo "✅ Configuración completada!"
echo "🌐 Iniciando servidor en http://127.0.0.1:8000/"
python manage.py runserver
