import os
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'medicWeb.settings')
django.setup()

from appMedic.models import MedicoModel, PacienteModel, HorarioMedicoModel, AgendaModel
from datetime import time, date, timedelta

def populate_database():
    """Populate database with sample data"""
    
    print("🏥 Iniciando población de base de datos...")
    
    # Limpiar datos existentes (opcional)
    print("\n📋 Limpiando datos existentes...")
    MedicoModel.objects.all().delete()
    PacienteModel.objects.all().delete()
    HorarioMedicoModel.objects.all().delete()
    AgendaModel.objects.all().delete()
    print("✅ Base de datos limpiada")
    
    # Crear médicos
    print("\n👨‍⚕️ Creando médicos...")
    medicos_data = [
        {
            'nombre': 'Dr. Carlos González',
            'especialidad': 'Cardiología',
            'correo': 'carlos.gonzalez@hospital.cl',
            'telefono': 912345678
        },
        {
            'nombre': 'Dra. María Rodríguez',
            'especialidad': 'Pediatría',
            'correo': 'maria.rodriguez@hospital.cl',
            'telefono': 923456789
        },
        {
            'nombre': 'Dr. Juan Martínez',
            'especialidad': 'Neurología',
            'correo': 'juan.martinez@hospital.cl',
            'telefono': 934567890
        },
        {
            'nombre': 'Dra. Ana López',
            'especialidad': 'Dermatología',
            'correo': 'ana.lopez@hospital.cl',
            'telefono': 945678901
        },
        {
            'nombre': 'Dr. Roberto Fernández',
            'especialidad': 'Oftalmología',
            'correo': 'roberto.fernandez@hospital.cl',
            'telefono': 956789012
        },
    ]
    
    medicos = []
    for med_data in medicos_data:
        medico, created = MedicoModel.objects.get_or_create(
            nombre=med_data['nombre'],
            defaults={
                'especialidad': med_data['especialidad'],
                'correo': med_data['correo'],
                'telefono': med_data['telefono']
            }
        )
        medicos.append(medico)
        status = "✨ Creado" if created else "📌 Existente"
        print(f"  {status}: {medico.nombre} ({medico.especialidad})")
    
    # Crear pacientes
    print("\n👥 Creando pacientes...")
    pacientes_data = [
        {
            'nombre': 'Felipe Sánchez García',
            'rut': '182345679',
            'correo': 'felipe.sanchez@email.com',
            'telefono': 987654321,
            'direccion': 'Calle Principal 123, Santiago'
        },
        {
            'nombre': 'Laura Mora Pérez',
            'rut': '193456780',
            'correo': 'laura.mora@email.com',
            'telefono': 988765432,
            'direccion': 'Avenida Libertad 456, Santiago'
        },
        {
            'nombre': 'Miguel Torres Guzmán',
            'rut': '174567891',
            'correo': 'miguel.torres@email.com',
            'telefono': 989876543,
            'direccion': 'Pasaje Central 789, Valparaíso'
        },
        {
            'nombre': 'Patricia Díaz Vargas',
            'rut': '165678902',
            'correo': 'patricia.diaz@email.com',
            'telefono': 990987654,
            'direccion': 'Camino al Sur 321, Valparaíso'
        },
        {
            'nombre': 'Ricardo Navarro Espinoza',
            'rut': '156789013',
            'correo': 'ricardo.navarro@email.com',
            'telefono': 991098765,
            'direccion': 'Los Acacias 654, Concepción'
        },
        {
            'nombre': 'Gabriela Herrera Silva',
            'rut': '147890124',
            'correo': 'gabriela.herrera@email.com',
            'telefono': 992109876,
            'direccion': 'Paseo Real 987, Concepción'
        },
    ]
    
    pacientes = []
    for pac_data in pacientes_data:
        paciente, created = PacienteModel.objects.get_or_create(
            rut=pac_data['rut'],
            defaults={
                'nombre': pac_data['nombre'],
                'correo': pac_data['correo'],
                'telefono': pac_data['telefono'],
                'direccion': pac_data['direccion']
            }
        )
        pacientes.append(paciente)
        status = "✨ Creado" if created else "📌 Existente"
        print(f"  {status}: {paciente.nombre} (RUT: {paciente.rut})")
    
    # Crear horarios médicos
    print("\n📅 Creando horarios médicos...")
    horarios_data = [
        # Dr. Carlos González - Cardiología
        {'medico': medicos[0], 'dia': 1, 'inicio': '08:00', 'fin': '12:00'},
        {'medico': medicos[0], 'dia': 1, 'inicio': '14:00', 'fin': '18:00'},
        {'medico': medicos[0], 'dia': 3, 'inicio': '09:00', 'fin': '13:00'},
        {'medico': medicos[0], 'dia': 5, 'inicio': '08:00', 'fin': '12:00'},
        
        # Dra. María Rodríguez - Pediatría
        {'medico': medicos[1], 'dia': 2, 'inicio': '09:00', 'fin': '13:00'},
        {'medico': medicos[1], 'dia': 2, 'inicio': '14:00', 'fin': '17:00'},
        {'medico': medicos[1], 'dia': 4, 'inicio': '08:30', 'fin': '12:30'},
        {'medico': medicos[1], 'dia': 5, 'inicio': '09:00', 'fin': '13:00'},
        
        # Dr. Juan Martínez - Neurología
        {'medico': medicos[2], 'dia': 1, 'inicio': '09:30', 'fin': '13:30'},
        {'medico': medicos[2], 'dia': 3, 'inicio': '10:00', 'fin': '14:00'},
        {'medico': medicos[2], 'dia': 4, 'inicio': '08:00', 'fin': '12:00'},
        
        # Dra. Ana López - Dermatología
        {'medico': medicos[3], 'dia': 2, 'inicio': '08:00', 'fin': '12:00'},
        {'medico': medicos[3], 'dia': 4, 'inicio': '13:00', 'fin': '17:00'},
        {'medico': medicos[3], 'dia': 5, 'inicio': '10:00', 'fin': '14:00'},
        
        # Dr. Roberto Fernández - Oftalmología
        {'medico': medicos[4], 'dia': 1, 'inicio': '10:00', 'fin': '14:00'},
        {'medico': medicos[4], 'dia': 3, 'inicio': '08:00', 'fin': '12:00'},
        {'medico': medicos[4], 'dia': 5, 'inicio': '14:00', 'fin': '18:00'},
    ]
    
    horario_count = 0
    for h_data in horarios_data:
        horario, created = HorarioMedicoModel.objects.get_or_create(
            fk_medico=h_data['medico'],
            dia_semana=h_data['dia'],
            hora_inicio=time.fromisoformat(h_data['inicio']),
            defaults={
                'hora_fin': time.fromisoformat(h_data['fin']),
                'activo': True
            }
        )
        if created:
            horario_count += 1
            dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes']
            print(f"  ✨ Creado: {h_data['medico'].nombre} - {dias[h_data['dia']-1]} ({h_data['inicio']}-{h_data['fin']})")
    
    # Crear citas agendadas
    print("\n📝 Creando citas agendadas...")
    hoy = date.today()
    
    # Encontrar horarios para crear citas
    citas_data = []
    for i in range(min(8, len(HorarioMedicoModel.objects.all()))):
        horario = HorarioMedicoModel.objects.all()[i]
        paciente = pacientes[i % len(pacientes)]
        # Crear cita para próxima semana
        fecha_cita = hoy + timedelta(days=7 + (i % 5))
        citas_data.append({
            'horario': horario,
            'paciente': paciente,
            'fecha': fecha_cita
        })
    
    cita_count = 0
    for cita_data in citas_data:
        cita, created = AgendaModel.objects.get_or_create(
            fk_horario=cita_data['horario'],
            fecha=cita_data['fecha'],
            defaults={
                'fk_paciente': cita_data['paciente'],
                'disponible': False
            }
        )
        if created:
            cita_count += 1
            print(f"  ✨ Creada: {cita_data['paciente'].nombre} - Dr(a). {cita_data['horario'].fk_medico.nombre} ({cita_data['fecha']})")
    
    # Resumen
    print("\n" + "="*60)
    print("✅ POBLACIÓN DE BASE DE DATOS COMPLETADA")
    print("="*60)
    print(f"📊 Resumen:")
    print(f"   • Médicos: {len(medicos)}")
    print(f"   • Pacientes: {len(pacientes)}")
    print(f"   • Horarios creados: {horario_count}")
    print(f"   • Citas agendadas: {cita_count}")
    print("="*60)
    print("\n✨ Los datos están listos para pruebas. ¡Accede a http://127.0.0.1:8000/\n")

if __name__ == '__main__':
    populate_database()
