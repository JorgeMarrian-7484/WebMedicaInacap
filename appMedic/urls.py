from django.urls import path
from appMedic.views import login,cmedico,chorario,horario,medico, paciente, cpaciente, agendar

urlpatterns = [
    path('IniciarSesion/',login,name='login'),
    path('creacionMedico/',cmedico,name='crearMedico'),
    path('horario/',horario,name='horario'),
    path('crearHorario/',chorario,name='crearHorario'),
    path('medico/',medico,name='medico'),
    path('paciente/',paciente, name= 'paciente'),
    path('crearPaciente/',cpaciente, name='cpaciente'),
    path('agendarCita/',agendar, name='agendar')

]