#!/usr/bin/env python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'medicWeb.settings')
django.setup()

from django.test import Client
from django.contrib.auth.models import User, Group

print("=" * 80)
print("PRUEBA COMPLETA: CAMBIAR CONTRASEÑA Y LOGIN")
print("=" * 80)

# 1. Crear usuario de prueba fresco
print("\n--- PASO 1: Crear usuario de prueba ---")
try:
    test_user = User.objects.get(username='test_medico_debug')
    test_user.delete()
    print("✅ Usuario anterior eliminado")
except User.DoesNotExist:
    pass

test_user = User.objects.create_user(
    username='test_medico_debug',
    email='test@example.com',
    password='original123'
)
print(f"✅ Usuario creado: {test_user.username}")
print(f"   Email: {test_user.email}")

# Asignar a grupo Médico
medico_group, _ = Group.objects.get_or_create(name='Medico')
test_user.groups.add(medico_group)
print(f"✅ Usuario asignado al grupo 'Medico'")

# 2. Verificar login con contraseña original
print("\n--- PASO 2: Verificar login con contraseña original ---")
client = Client()
result = client.login(username='test_medico_debug', password='original123')
if result:
    print("✅ Login exitoso con contraseña original 'original123'")
    client.logout()
else:
    print("❌ Login fallido con contraseña original")

# 3. Cambiar contraseña como admin (simular lo que hace la interfaz)
print("\n--- PASO 3: Cambiar contraseña (simular admin) ---")
nueva_contraseña = 'nuevaContraseña456'
test_user.set_password(nueva_contraseña)
test_user.save()
print(f"✅ Contraseña cambiada a: '{nueva_contraseña}'")

# 4. Recargar del DB
test_user.refresh_from_db()
print(f"✅ Usuario recarado de BD")

# 5. Verificar que la contraseña nueva funciona locally
print("\n--- PASO 4: Verificar contraseña nueva (direct check) ---")
if test_user.check_password(nueva_contraseña):
    print(f"✅ check_password() confirma: '{nueva_contraseña}' es CORRECTA")
else:
    print(f"❌ check_password() dice: '{nueva_contraseña}' es INCORRECTA")

# 6. Verificar que authenticate funciona
print("\n--- PASO 5: Verificar authenticate() ---")
from django.contrib.auth import authenticate
auth_result = authenticate(username='test_medico_debug', password=nueva_contraseña)
if auth_result:
    print(f"✅ authenticate() retorna usuario: {auth_result.username}")
else:
    print(f"❌ authenticate() retorna None")

# 7. Intentar login con cliente HTTP (como se hace en la interfaz)
print("\n--- PASO 6: Intentar login por HTTP (como usuario real) ---")
client = Client()
response = client.post('/components/IniciarSesion/', {
    'username': 'test_medico_debug',
    'password': nueva_contraseña
})

# Revisar resultado
if response.status_code == 302:  # Redirect después de login
    print(f"✅ POST a login retorna 302 (redirect)")
    # Verificar que la sesión está establecida
    if 'test_medico_debug' in response.wsgi_request.session.get('_auth_user_id', ''):
        print("✅ Sesión establecida correctamente")
    else:
        print("⚠️ No se puede verificar sesión desde POST response")
elif response.status_code == 200:
    print(f"❌ POST a login retorna 200 (no hubo redirect - login fallido)")
    # Buscar mensaje de error
    content = response.content.decode()
    if 'incorrectos' in content or 'error' in content.lower():
        print("❌ Página contiene mensaje de error de credenciales")
else:
    print(f"❌ POST a login retorna {response.status_code}")

print("\n" + "=" * 80)
print("CONCLUSIÓN: Si todos los tests pasaron, la funcionalidad está OK")
print("=" * 80)
