#!/usr/bin/env python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'medicWeb.settings')
django.setup()

from django.test import Client
from django.contrib.auth.models import User
from appMedic.forms import CambiarContraseñaForms

client = Client()

print("=" * 60)
print("PRUEBA DE FUNCIONALIDAD: CAMBIAR CONTRASEÑA")
print("=" * 60)

# 1. Obtener usuario admin
try:
    admin_user = User.objects.get(username='admin')
    print(f"\n✅ Usuario admin encontrado: {admin_user.username} (id: {admin_user.id})")
except User.DoesNotExist:
    print("\n❌ Usuario admin no encontrado")
    exit(1)

# 2. Obtener usuario de prueba
try:
    test_user = User.objects.get(username='paciente1') or User.objects.all()[10]
    print(f"✅ Usuario de prueba encontrado: {test_user.username} (id: {test_user.id})")
except:
    test_user = User.objects.all()[10]
    print(f"✅ Usuario de prueba encontrado: {test_user.username} (id: {test_user.id})")

# 3. Hacer login como admin
print("\n--- PRUEBA 1: Login como admin ---")
login_ok = client.login(username='admin', password='admin123')
if login_ok:
    print("✅ Login exitoso como admin")
else:
    print("❌ Error al hacer login como admin")
    exit(1)

# 4. Acceder a página de usuarios
print("\n--- PRUEBA 2: Acceso a página de usuarios ---")
response = client.get('/components/usuarios/')
if response.status_code == 200:
    print(f"✅ Página de usuarios cargada (status: {response.status_code})")
else:
    print(f"❌ Error al acceder a página de usuarios (status: {response.status_code})")

# 5. Acceder a formulario de cambiar contraseña
print("\n--- PRUEBA 3: Acceso a formulario de cambiar contraseña ---")
response = client.get(f'/components/usuarios/{test_user.id}/cambiar-contraseña/')
if response.status_code == 200:
    print(f"✅ Formulario de cambiar contraseña cargado (status: {response.status_code})")
    # Verificar que el formulario está en la respuesta
    if 'cambiar' in response.content.decode().lower():
        print("✅ Página contiene referencias al cambio de contraseña")
else:
    print(f"❌ Error al acceder al formulario (status: {response.status_code})")

# 6. Probar cambio de contraseña
print("\n--- PRUEBA 4: Cambio de contraseña ---")
contraseña_nueva = 'nuevaContraseña123'
response = client.post(
    f'/components/usuarios/{test_user.id}/cambiar-contraseña/',
    {
        'nueva_contraseña': contraseña_nueva,
        'confirmar_contraseña': contraseña_nueva
    }
)

if response.status_code == 302:  # Redirect after success
    print(f"✅ POST exitoso (redirect status: {response.status_code})")
    
    # Verificar que la contraseña cambió
    test_user.refresh_from_db()
    if test_user.check_password(contraseña_nueva):
        print("✅ Contraseña actualizada correctamente")
    else:
        print("❌ Error: Contraseña no fue actualizada")
elif response.status_code == 200:
    print(f"⚠️ POST retornó status 200 (posible error en formulario)")
    # Buscar errores en la respuesta
    content = response.content.decode()
    if 'error' in content.lower():
        print("❌ Errores encontrados en la respuesta")
    else:
        print("⚠️ Revisar respuesta manualmente")
else:
    print(f"❌ Error POST (status: {response.status_code})")

# 7. Validar formulario directamente
print("\n--- PRUEBA 5: Validación del formulario ---")
form = CambiarContraseñaForms(data={
    'nueva_contraseña': 'test123456',
    'confirmar_contraseña': 'test123456'
})
if form.is_valid():
    print("✅ Formulario válido con contraseñas válidas")
else:
    print(f"❌ Errores en el formulario: {form.errors}")

# Probar validación de contraseñas que no coinciden
form_invalid = CambiarContraseñaForms(data={
    'nueva_contraseña': 'test123456',
    'confirmar_contraseña': 'diferente123'
})
if not form_invalid.is_valid():
    print("✅ Formulario rechaza contraseñas que no coinciden")
else:
    print("❌ Error: Formulario debería rechazar contraseñas diferentes")

# Probar validación de contraseña corta
form_short = CambiarContraseñaForms(data={
    'nueva_contraseña': 'abc',
    'confirmar_contraseña': 'abc'
})
if not form_short.is_valid():
    print("✅ Formulario rechaza contraseñas muy cortas")
else:
    print("❌ Error: Formulario debería rechazar contraseñas cortas")

print("\n" + "=" * 60)
print("PRUEBAS COMPLETADAS")
print("=" * 60)
