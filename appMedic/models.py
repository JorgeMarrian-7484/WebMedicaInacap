from django.db import models

# Create your models here.

class PacienteModel(models.Model):
    id_paciente = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)
    rut = models.CharField(max_length=9)
    correo = models.EmailField(max_lenght=150)
    telefono = models.IntegerField(max_length=10)
    direccion = models.CharField(max_length=50)
    def __str__(self):
        return self.rut
    class Meta:
        db_table = 'paciente'

class MedicoModel (models.Model):
    id_medico = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)
    correo = models.EmailField()
    telefono = models.IntegerField(max_length=10)
    especialidad = models.CharField(max_length=15)


#Revisar como funciona esta clase en particular (Fuente: IA Deepseek)... Recuerda agregar un comentario, explicando las funciones desconocidas y como se relacionan
class HorarioMedicoModel (models.Model):
    fk_medico = models.ForeignKey(MedicoModel, on_delete=models.RESTRICT, related_name='horarios')
    dia_semana = [
        (0, 'Lunes'),
        (1, 'Martes'),
        (2, 'Miercoles'),
        (3, 'Jueves'),
        (4, 'Viernes'),
    ]
    fecha_select = models.IntegerField(choices=dia_semana)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    activo = models.BooleanField(default=True)
    class Meta:
        unique_together = ['fk_medico','fecha_select','hora_inicio']
        ordering = ['fecha_select','hora_inicio']

#Revisar esta clase relacionada con "HorarioMedicoModel", por si llegara a recibir un error
class AgendaModel (models.Model):
    id_agenda = models.IntegerField(primary_key=True)
    fk_medico = models.ForeignKey(MedicoModel,related_name='agendas', on_delete=models.RESTRICT)
    fecha = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    disponible = models.BooleanField(default=True)
    fk_paciente = models.ForeignKey(PacienteModel, null=True, blank=True, on_delete=models.SET_NULL)
    class Meta:
        unique_together = ['fk_medico','fecha','hora_inicio']

