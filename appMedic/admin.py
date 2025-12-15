from django.contrib import admin
from django.contrib.auth.models import User, Group
from appMedic.models import MedicoModel, PacienteModel, HorarioMedicoModel, AgendaModel, ExpedienteModel
from django import forms

class MedicoAdminForm(forms.ModelForm):
    """Formulario personalizado para crear médicos con usuario"""
    # Campos para la creación de usuario
    username = forms.CharField(
        max_length=150,
        required=False,
        help_text='Username para el usuario (si no se completa, se usará el nombre)'
    )
    email = forms.EmailField(
        required=False,
        help_text='Email del usuario'
    )
    password = forms.CharField(
        widget=forms.PasswordInput,
        required=False,
        help_text='Contraseña (si no se completa, se generará una aleatoria)',
        min_length=6
    )
    crear_usuario = forms.BooleanField(
        required=False,
        initial=True,
        help_text='¿Crear una cuenta de usuario para este médico?'
    )

    class Meta:
        model = MedicoModel
        fields = ['nombre', 'correo', 'telefono', 'especialidad', 'user']

    def clean(self):
        cleaned_data = super().clean()
        crear_usuario = cleaned_data.get('crear_usuario')
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        
        if crear_usuario:
            if not username:
                # Generar username desde el nombre: convertir a minúsculas y reemplazar espacios
                nombre = cleaned_data.get('nombre', '').lower().replace(' ', '_').replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u')
                # Remover caracteres especiales
                import re
                nombre = re.sub(r'[^a-z0-9_]', '', nombre)
                if nombre:
                    username = nombre
                    cleaned_data['username'] = username
            
            if not password or len(password) < 6:
                raise forms.ValidationError('La contraseña debe tener al menos 6 caracteres cuando se crea usuario')
        
        return cleaned_data

    def save(self, commit=True):
        medico = super().save(commit=False)
        crear_usuario = self.cleaned_data.get('crear_usuario')
        
        if crear_usuario:
            username = self.cleaned_data.get('username')
            email = self.cleaned_data.get('email')
            password = self.cleaned_data.get('password')
            
            # Crear usuario Django
            user = User.objects.create_user(
                username=username,
                email=email or '',
                password=password,
                first_name=self.cleaned_data.get('nombre', '')
            )
            
            # Asignar al grupo "Medico"
            medico_group, _ = Group.objects.get_or_create(name='Medico')
            user.groups.add(medico_group)
            
            # Asignar usuario al médico
            medico.user = user
        
        if commit:
            medico.save()
        
        return medico


class MedicoModelAdmin(admin.ModelAdmin):
    form = MedicoAdminForm
    list_display = ('nombre', 'especialidad', 'correo', 'telefono', 'user', 'tiene_usuario')
    list_filter = ('especialidad', 'user')
    search_fields = ('nombre', 'correo', 'especialidad')
    fieldsets = (
        ('Información del Médico', {
            'fields': ('nombre', 'especialidad', 'correo', 'telefono')
        }),
        ('Cuenta de Usuario', {
            'fields': ('crear_usuario', 'username', 'email', 'password', 'user'),
            'description': 'Completa estos campos para crear una cuenta de usuario para el médico'
        }),
    )

    def tiene_usuario(self, obj):
        if obj.user:
            return f"✅ {obj.user.username}"
        return "❌ Sin usuario"
    tiene_usuario.short_description = 'Estado de Cuenta'


class PacienteModelAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'rut', 'correo', 'telefono', 'user', 'tiene_usuario')
    list_filter = ('user',)
    search_fields = ('nombre', 'rut', 'correo')
    
    def tiene_usuario(self, obj):
        if obj.user:
            return f"✅ {obj.user.username}"
        return "❌ Sin usuario"
    tiene_usuario.short_description = 'Estado de Cuenta'


class HorarioMedicoModelAdmin(admin.ModelAdmin):
    list_display = ('fk_medico', 'get_dia_semana', 'hora_inicio', 'hora_fin', 'activo')
    list_filter = ('dia_semana', 'activo', 'fk_medico')
    search_fields = ('fk_medico__nombre',)
    
    def get_dia_semana(self, obj):
        return obj.get_dia_semana_display()
    get_dia_semana.short_description = 'Día'


class AgendaModelAdmin(admin.ModelAdmin):
    list_display = ('fk_paciente', 'fk_horario', 'fecha', 'disponible')
    list_filter = ('disponible', 'fecha')
    search_fields = ('fk_paciente__nombre', 'fk_horario__fk_medico__nombre')


class ExpedienteModelAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fk_paciente', 'fecha_creacion')
    list_filter = ('fecha_creacion',)
    search_fields = ('nombre', 'fk_paciente__nombre')


# Registrar modelos
admin.site.register(MedicoModel, MedicoModelAdmin)
admin.site.register(PacienteModel, PacienteModelAdmin)
admin.site.register(HorarioMedicoModel, HorarioMedicoModelAdmin)
admin.site.register(AgendaModel, AgendaModelAdmin)
admin.site.register(ExpedienteModel, ExpedienteModelAdmin)
