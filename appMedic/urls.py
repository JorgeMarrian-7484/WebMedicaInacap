from django.urls import path
from appMedic.views import (login, logout_view, registro, cmedico, emedico, dmedico, chorario, ehorario, dhorario,
                            horario, medico, paciente, cpaciente, epaciente, dpaciente, agendar, mis_citas, usuarios,
                            cambiar_contraseña,
                            exportar_medicos_excel, exportar_pacientes_excel, exportar_horarios_excel, 
                            exportar_agenda_excel)

urlpatterns = [
    # Login y Registro
    path('IniciarSesion/', login, name='login'),
    path('CerrarSesion/', logout_view, name='logout'),
    path('registrarse/', registro, name='registro'),
    
    # Médicos
    path('creacionMedico/', cmedico, name='crearMedico'),
    path('medico/', medico, name='medico'),
    path('medico/editar/<int:id>/', emedico, name='editarMedico'),
    path('medico/eliminar/<int:id>/', dmedico, name='eliminarMedico'),
    path('medico/exportar/excel/', exportar_medicos_excel, name='exportarMedicosExcel'),
    
    # Horarios
    path('horario/', horario, name='horario'),
    path('crearHorario/', chorario, name='crearHorario'),
    path('horario/editar/<int:id>/', ehorario, name='editarHorario'),
    path('horario/eliminar/<int:id>/', dhorario, name='eliminarHorario'),
    path('horario/exportar/excel/', exportar_horarios_excel, name='exportarHorariosExcel'),
    
    # Pacientes
    path('paciente/', paciente, name='paciente'),
    path('crearPaciente/', cpaciente, name='cpaciente'),
    path('paciente/editar/<int:id>/', epaciente, name='editarPaciente'),
    path('paciente/eliminar/<int:id>/', dpaciente, name='eliminarPaciente'),
    path('paciente/exportar/excel/', exportar_pacientes_excel, name='exportarPacientesExcel'),
    path('mis-citas/', mis_citas, name='misCitas'),
    
    # Citas
    path('agendarCita/', agendar, name='agendar'),
    path('agenda/exportar/excel/', exportar_agenda_excel, name='exportarAgendaExcel'),
    
    # Usuarios
    path('usuarios/', usuarios, name='usuarios'),
    path('usuarios/<int:user_id>/cambiar-contraseña/', cambiar_contraseña, name='cambiarContraseña')
]