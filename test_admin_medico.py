#!/usr/bin/env python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'medicWeb.settings')
django.setup()

from django.test import Client
from django.contrib.auth.models import User, Group
from appMedic.models import MedicoModel
from appMedic.forms import MedicoForms

print("=" * 80)
print("PRUEBA: CREAR MÉDICO - SIEMPRE CON USUARIO")
print("=" * 80)

# Limpiar datos anteriores
MedicoModel.objects.filter(nombre__startswith='Test').delete()
User.objects.filter(username__startswith='test_').delete()

# Test 1: Crear médico desde formulario (sin usuario previo)
print("\n--- TEST 1: Crear médico desde formulario web ---")
form_data = {
    'nombre': 'Test Doctor García',
    'especialidad': 'Neurología',
    'correo': 'test@hospital.com',
    'telefono': 912345678,
    'username': 'test_doctor_garcia',
    'password': 'medico123456',
    'confirmar_password': 'medico123456'
}
form = MedicoForms(data=form_data)
if form.is_valid():
    medico = form.save()
    print(f"✅ Médico creado: {medico.nombre}")
    print(f"   Usuario: {medico.user.username if medico.user else 'SIN USUARIO (ERROR!)'}")
    print(f"   Email usuario: {medico.user.email}")
    
    # Verificar que está en grupo Médico
    if medico.user.groups.filter(name='Medico').exists():
        print(f"   ✅ Asignado al grupo 'Medico'")
    else:
        print(f"   ❌ NO está en grupo 'Medico'")
    
    # Verificar autenticación
    from django.contrib.auth import authenticate
    auth = authenticate(username='test_doctor_garcia', password='medico123456')
    if auth:
        print(f"   ✅ Autenticación funciona")
    else:
        print(f"   ❌ Autenticación fallida")
else:
    print(f"❌ Error en formulario: {form.errors}")

# Test 2: Crear médico con username auto-generado
print("\n--- TEST 2: Crear médico con username auto-generado ---")
MedicoModel.objects.filter(nombre='Dra. María López').delete()
User.objects.filter(username='dra_maria_lopez').delete()

form_data = {
    'nombre': 'Dra. María López',
    'especialidad': 'Pediatría',
    'correo': 'maria@hospital.com',
    'telefono': 923456789,
    'username': '',  # Vacío para auto-generar
    'password': 'pediatra123456',
    'confirmar_password': 'pediatra123456'
}
form = MedicoForms(data=form_data)
if form.is_valid():
    medico = form.save()
    print(f"✅ Médico creado: {medico.nombre}")
    print(f"   Usuario auto-generado: {medico.user.username if medico.user else 'NO CREADO'}")
else:
    print(f"❌ Error en formulario: {form.errors}")

# Test 3: Crear médico con contraseñas no coincidentes (debe fallar)
print("\n--- TEST 3: Contraseñas no coincidentes (debe fallar) ---")
form_data = {
    'nombre': 'Dr. Test Error',
    'especialidad': 'Cardiología',
    'correo': 'test@hospital.com',
    'telefono': 934567890,
    'username': 'test_error',
    'password': 'password123',
    'confirmar_password': 'password456'  # Diferente
}
form = MedicoForms(data=form_data)
if form.is_valid():
    print(f"❌ ERROR: Debería rechazar contraseñas diferentes")
else:
    if 'coinciden' in str(form.errors).lower():
        print(f"✅ Correctamente rechazado: Contraseñas no coinciden")
    else:
        print(f"⚠️ Rechazado pero por otra razón: {form.errors}")

# Test 4: Crear médico con contraseña corta (debe fallar)
print("\n--- TEST 4: Contraseña corta (debe fallar) ---")
form_data = {
    'nombre': 'Dr. Test Corto',
    'especialidad': 'Oftalmología',
    'correo': 'test@hospital.com',
    'telefono': 945678901,
    'username': 'test_short',
    'password': 'abc',  # Muy corta
    'confirmar_password': 'abc'
}
form = MedicoForms(data=form_data)
if form.is_valid():
    print(f"❌ ERROR: Debería rechazar contraseña corta")
else:
    if '6' in str(form.errors) or 'caracteres' in str(form.errors).lower():
        print(f"✅ Correctamente rechazado: Contraseña muy corta")
    else:
        print(f"⚠️ Rechazado: {form.errors}")

# Test 5: Acceso HTTP al formulario de creación
print("\n--- TEST 5: Acceso HTTP al formulario ---")
client = Client()
client.login(username='admin', password='admin123')
response = client.get('/components/creacionMedico/')
if response.status_code == 200:
    print(f"✅ Acceso al formulario web exitoso")
    content = response.content.decode()
    if 'password' in content.lower() and 'username' in content.lower():
        print(f"✅ Formulario contiene campos de usuario y contraseña")
    else:
        print(f"⚠️ Campos de usuario/contraseña no encontrados claramente")
else:
    print(f"❌ Error al acceder al formulario (status: {response.status_code})")

print("\n" + "=" * 80)
print("PRUEBAS COMPLETADAS")
print("=" * 80)
