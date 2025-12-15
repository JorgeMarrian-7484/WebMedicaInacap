#!/usr/bin/env python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'medicWeb.settings')
django.setup()

from django.test import Client
from django.contrib.auth.models import User

print("=" * 80)
print("DEMOSTRACIÓN: ERRORES DE VALIDACIÓN EN CAMBIO DE CONTRASEÑA")
print("=" * 80)

# Login como admin
client = Client()
client.login(username='admin', password='admin123')
print("\n✅ Logueado como admin\n")

# Obtener un usuario de prueba
test_user = User.objects.get(username='medico2')
print(f"Pruebas de cambio de contraseña para: {test_user.username}\n")

# TEST 1: Contraseñas no coinciden
print("--- TEST 1: Contraseñas NO coinciden ---")
response = client.post(
    f'/components/usuarios/{test_user.id}/cambiar-contraseña/',
    {
        'nueva_contraseña': 'password123',
        'confirmar_contraseña': 'password456'
    }
)
print(f"Status: {response.status_code}")
if response.status_code == 200:
    content = response.content.decode()
    if 'no coinciden' in content.lower() or 'coinciden' in content.lower():
        print("✅ Página muestra error: 'no coinciden'")
    elif 'confirmar' in content.lower() and ('error' in content.lower() or 'no' in content.lower()):
        print("✅ Página muestra error en campo 'confirmar'")
    else:
        # Buscar en cualquier lado
        if 'password456' in content or 'nueva_contraseña' in content:
            print("⚠️ Respuesta contiene el formulario")
            # Buscar más específicamente
            import re
            errors = re.findall(r'<div class="text-danger[^>]*>(.*?)</div>', content, re.DOTALL)
            if errors:
                print(f"✅ Errores encontrados: {errors}")
            else:
                print("❌ No se encuentran mensajes de error claramente")
        else:
            print("❌ No se encuentra el formulario en la respuesta")
        
# TEST 2: Contraseña muy corta
print("\n--- TEST 2: Contraseña muy corta (menos de 6 caracteres) ---")
response = client.post(
    f'/components/usuarios/{test_user.id}/cambiar-contraseña/',
    {
        'nueva_contraseña': 'abc',
        'confirmar_contraseña': 'abc'
    }
)
print(f"Status: {response.status_code}")
if response.status_code == 200:
    content = response.content.decode()
    if '6' in content or 'caracteres' in content.lower():
        print("✅ Página muestra error de longitud mínima")
    else:
        print("⚠️ Error de longitud no mostrado claramente")

# TEST 3: Contraseña válida
print("\n--- TEST 3: Contraseña VÁLIDA (6+ caracteres, coinciden) ---")
response = client.post(
    f'/components/usuarios/{test_user.id}/cambiar-contraseña/',
    {
        'nueva_contraseña': 'nuevaPassword123',
        'confirmar_contraseña': 'nuevaPassword123'
    }
)
print(f"Status: {response.status_code}")
if response.status_code == 302:
    print("✅ Redirect (302) - Cambio exitoso")
    # Verificar que la contraseña cambió
    test_user.refresh_from_db()
    if test_user.check_password('nuevaPassword123'):
        print("✅ Contraseña fue actualizada en la BD")
    else:
        print("❌ Contraseña no fue actualizada")

print("\n" + "=" * 80)
