from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from appMedic.models import MedicoModel, PacienteModel, HorarioMedicoModel, AgendaModel


class Command(BaseCommand):
    help = 'Crea los grupos de permisos: Medico y Paciente'

    def handle(self, *args, **options):
        # Crear grupos
        medico_group, created = Group.objects.get_or_create(name='Medico')
        paciente_group, created = Group.objects.get_or_create(name='Paciente')
        
        # Obtener tipos de contenido
        medico_ct = ContentType.objects.get_for_model(MedicoModel)
        paciente_ct = ContentType.objects.get_for_model(PacienteModel)
        horario_ct = ContentType.objects.get_for_model(HorarioMedicoModel)
        agenda_ct = ContentType.objects.get_for_model(AgendaModel)
        
        # ==================== PERMISOS MÉDICO ====================
        # Los médicos pueden ver médicos, ver pacientes, ver horarios y gestionar citas
        medico_perms = Permission.objects.filter(
            content_type__in=[medico_ct, paciente_ct, horario_ct, agenda_ct],
            codename__in=['view_medicomodel', 'view_pacientemodel', 'view_horariomedicomodel', 
                          'view_agendamodel', 'add_agendamodel', 'change_agendamodel']
        )
        medico_group.permissions.set(medico_perms)
        
        # ==================== PERMISOS PACIENTE ====================
        # Los pacientes solo pueden ver médicos, horarios y sus citas
        paciente_perms = Permission.objects.filter(
            content_type__in=[medico_ct, horario_ct, agenda_ct],
            codename__in=['view_medicomodel', 'view_horariomedicomodel', 
                          'view_agendamodel', 'add_agendamodel']
        )
        paciente_group.permissions.set(paciente_perms)
        
        self.stdout.write(self.style.SUCCESS('✅ Grupos de permisos creados exitosamente!'))
        self.stdout.write('Grupo Médico: Ver médicos, pacientes, horarios y gestionar citas')
        self.stdout.write('Grupo Paciente: Ver médicos, horarios y agendar citas')
