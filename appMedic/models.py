from django.db import models

# Create your models here.

class PacienteModel(models.Model):
    nombre = models.CharField(max_length=30)
    rut = models.CharField(max_length=9)
    correo = models.EmailField(max_length=150)
    telefono = models.IntegerField()
    direccion = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.nombre} - {self.rut}"
    class Meta:
        db_table = 'paciente'

#Esta clase tendra su formulario, quien tendra acceso solamente el admin

class MedicoModel (models.Model):
    nombre = models.CharField(max_length=30)
    correo = models.EmailField()
    telefono = models.IntegerField()
    especialidad = models.CharField(max_length=15)
    def __str__(self):
        return f"{self.nombre} - {self.especialidad}"
    class Meta:
        db_table = 'medico'



# Esta clase solo podra tener acceso el medico. EL ADMIN NO DEBE PODER CAMBIAR SUS HORARIOS
class HorarioMedicoModel(models.Model):
    DIAS_SEMANA = [
        (1, 'Lunes'),
        (2, 'Martes'),
        (3, 'Miércoles'),
        (4, 'Jueves'),
        (5, 'Viernes'),
    ]
    
    fk_medico = models.ForeignKey('MedicoModel', on_delete=models.RESTRICT, related_name='horarios')
    dia_semana = models.IntegerField(choices=DIAS_SEMANA)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    activo = models.BooleanField(default=True)
    class Meta:
        unique_together = ['fk_medico','dia_semana','hora_inicio']
        ordering = ['dia_semana','hora_inicio']
        verbose_name = 'Horario Médico'                 #Investigar que es estas funciones
        verbose_name_plural = 'Horarios Médicos'        #esta igual
    def __str__(self):
        return f"{self.fk_medico.nombre} - {self.get_dia_semana_display()} {self.hora_inicio}-{self.hora_fin}"

#Revisar esta clase relacionada con "HorarioMedicoModel", por si llegara a recibir un error
class AgendaModel(models.Model):
    fk_horario = models.ForeignKey(
        HorarioMedicoModel, 
        on_delete=models.CASCADE,
        related_name='citas_agendadas'
    )
    fk_paciente = models.ForeignKey(
        PacienteModel, 
        null=True, blank=True, 
        on_delete=models.SET_NULL
    )
    fecha = models.DateField()
    disponible = models.BooleanField(default=True)
    
    class Meta:
        unique_together = ['fk_horario', 'fecha'] 
        ordering = ['fecha', 'fk_horario__hora_inicio']
    
    def __str__(self):
        return f"Cita {self.fecha} - Dr.{self.fk_horario.fk_medico.nombre}"
    
    @property
    def fk_medico(self):
        return self.fk_horario.fk_medico

class ExpedienteModel(models.Model):
    id_expediente = models.IntegerField(primary_key = True)
    fk_paciente = models.ForeignKey(PacienteModel, on_delete = models.RESTRICT)
    nombre = models.CharField(max_length = 15)
    descripcion = models.TextField()


#Agregar modelos de administracion con integracion de medicos. LOS MEDICOS DEBEN SER REGISTRADOS POR EL ADMINISTRADOR DE LA WEB...  


