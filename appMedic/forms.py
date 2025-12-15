from django import forms
from appMedic.models import MedicoModel, HorarioMedicoModel, PacienteModel, AgendaModel, UsuarioModel
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError

#Clases para horarios de los medicos

class MedicoForms (forms.ModelForm):
    """Formulario para crear médico - SIEMPRE crea usuario automáticamente"""
    username = forms.CharField(
        max_length=150,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Usuario (auto-generado si está vacío)',
        }),
        help_text='Si lo dejas en blanco, se generará desde el nombre'
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Contraseña (mín. 6 caracteres)',
            'required': True,
            'minlength': 6
        }),
        min_length=6,
        help_text='Mínimo 6 caracteres'
    )
    confirmar_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirmar contraseña',
            'required': True
        })
    )
    
    class Meta:
        model = MedicoModel
        fields = ['nombre', 'especialidad', 'correo', 'telefono']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class':'form-control',
                'placeholder': 'Nombre completo del médico',
                'required': True
            }),
            'especialidad': forms.TextInput(attrs={
                'class':'form-control',
                'placeholder': 'Ej: Cardiología, Pediatría',
                'required': True
            }),
            'correo': forms.EmailInput(attrs={
                'class':'form-control',
                'placeholder': 'correo@ejemplo.com',
                'required': True
            }),
            'telefono': forms.NumberInput(attrs={
                'class':'form-control',
                'placeholder': 'Número de teléfono',
                'required': True
            })
        }
    
    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if nombre and len(nombre) < 3:
            raise forms.ValidationError('El nombre debe tener al menos 3 caracteres')
        return nombre
    
    def clean_telefono(self):
        telefono = self.cleaned_data.get('telefono')
        if telefono and telefono < 0:
            raise forms.ValidationError('El teléfono no puede ser negativo')
        return telefono
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirmar_password = cleaned_data.get('confirmar_password')
        
        if password and confirmar_password:
            if password != confirmar_password:
                self.add_error('confirmar_password', '❌ Las contraseñas no coinciden')
            if len(password) < 6:
                self.add_error('password', '❌ La contraseña debe tener al menos 6 caracteres')
        
        return cleaned_data
    
    def save(self, commit=True):
        medico = super().save(commit=False)
        
        # Obtener datos de usuario
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        
        # Auto-generar username desde nombre si está vacío
        if not username:
            nombre = self.cleaned_data.get('nombre', '').lower()
            nombre = nombre.replace(' ', '_').replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u')
            import re
            username = re.sub(r'[^a-z0-9_]', '', nombre)
        
        # Verificar que el username no exista
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(f'El usuario "{username}" ya existe')
        
        # Crear usuario
        user = User.objects.create_user(
            username=username,
            email=self.cleaned_data.get('correo', ''),
            password=password,
            first_name=self.cleaned_data.get('nombre', '')
        )
        
        # Asignar al grupo "Medico"
        from django.contrib.auth.models import Group
        medico_group, _ = Group.objects.get_or_create(name='Medico')
        user.groups.add(medico_group)
        
        # Vincular usuario al médico
        medico.user = user
        
        if commit:
            medico.save()
        
        return medico


class MedicoConUsuarioForms(forms.ModelForm):
    """Formulario para crear médico con usuario de login"""
    username = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Nombre de usuario para login',
            'required': True
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Contraseña',
            'required': True
        })
    )
    confirmar_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirmar contraseña',
            'required': True
        })
    )
    
    class Meta:
        model = MedicoModel
        fields = ['nombre', 'especialidad', 'correo', 'telefono']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class':'form-control',
                'placeholder': 'Nombre completo del médico',
                'required': True
            }),
            'especialidad': forms.TextInput(attrs={
                'class':'form-control',
                'placeholder': 'Ej: Cardiología, Pediatría',
                'required': True
            }),
            'correo': forms.EmailInput(attrs={
                'class':'form-control',
                'placeholder': 'correo@ejemplo.com',
                'required': True
            }),
            'telefono': forms.NumberInput(attrs={
                'class':'form-control',
                'placeholder': 'Número de teléfono',
                'required': True
            })
        }
    
    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if nombre and len(nombre) < 3:
            raise forms.ValidationError('El nombre debe tener al menos 3 caracteres')
        return nombre
    
    def clean_telefono(self):
        telefono = self.cleaned_data.get('telefono')
        if telefono and telefono < 0:
            raise forms.ValidationError('El teléfono no puede ser negativo')
        return telefono
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise ValidationError('Este nombre de usuario ya está registrado')
        if len(username) < 3:
            raise ValidationError('El nombre de usuario debe tener al menos 3 caracteres')
        return username
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirmar_password = cleaned_data.get('confirmar_password')
        
        if password and confirmar_password:
            if password != confirmar_password:
                raise ValidationError('Las contraseñas no coinciden')
            if len(password) < 6:
                raise ValidationError('La contraseña debe tener al menos 6 caracteres')
        
        return cleaned_data
    
    def save(self, commit=True):
        medico = super().save(commit=False)
        # Crear usuario
        usuario = User.objects.create_user(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['correo'],
            password=self.cleaned_data['password'],
            first_name=self.cleaned_data['nombre']
        )
        # Agregar al grupo Medico
        from django.contrib.auth.models import Group
        try:
            medico_group = Group.objects.get(name='Medico')
            usuario.groups.add(medico_group)
        except Group.DoesNotExist:
            pass
        
        medico.user = usuario
        if commit:
            medico.save()
        return medico

class HorarioForms (forms.ModelForm):
    class Meta:
        model = HorarioMedicoModel
        fields = ['fk_medico','dia_semana', 'hora_inicio', 'hora_fin', 'activo']
        widgets = {
            'fk_medico': forms.Select(attrs={
                'class':'form-select',
                'required': True
            }),
            'dia_semana': forms.Select(attrs={
                'class':'form-select',
                'required': True
            }),
            'hora_inicio': forms.TimeInput(attrs={
                'class':'form-control',
                'type': 'time',
                'required': True
            }),
            'hora_fin': forms.TimeInput(attrs={
                'class':'form-control',
                'type': 'time',
                'required': True
            }),
            'activo': forms.CheckboxInput(attrs={
                'class':'form-check-input'
            })
        }
    
    def clean(self):
        cleaned_data = super().clean()
        hora_inicio = cleaned_data.get('hora_inicio')
        hora_fin = cleaned_data.get('hora_fin')
        
        if hora_inicio and hora_fin:
            if hora_inicio >= hora_fin:
                raise forms.ValidationError('La hora de inicio debe ser menor a la hora de fin')
        return cleaned_data

class PacienteForms (forms.ModelForm):
    class Meta:
        model = PacienteModel
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class':'form-control',
                'placeholder': 'Nombre completo del paciente',
                'required': True
            }),
            'rut': forms.TextInput(attrs={
                'class':'form-control',
                'placeholder': 'Ej: 12345678-9',
                'required': True
            }),
            'correo': forms.EmailInput(attrs={
                'class':'form-control',
                'placeholder': 'correo@ejemplo.com',
                'required': True
            }),
            'telefono': forms.NumberInput(attrs={
                'class':'form-control',
                'placeholder': 'Número de teléfono',
                'required': True
            }),
            'direccion': forms.TextInput(attrs={
                'class':'form-control',
                'placeholder': 'Dirección del paciente',
                'required': True
            })
        }
    
    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if nombre and len(nombre) < 3:
            raise forms.ValidationError('El nombre debe tener al menos 3 caracteres')
        return nombre
    
    def clean_rut(self):
        rut = self.cleaned_data.get('rut')
        if rut and len(rut) < 8:
            raise forms.ValidationError('El RUT debe tener al menos 8 caracteres')
        return rut

class AgendaForms(forms.ModelForm):
    class Meta:
        model = AgendaModel
        fields = ['fk_horario', 'fk_paciente', 'fecha']
        widgets = {
            'fk_horario': forms.Select(attrs={
                'class':'form-select',
                'required': True
            }),
            'fk_paciente': forms.Select(attrs={
                'class':'form-select',
                'required': True
            }),
            'fecha': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
                'required': True
            })
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filtrar solo horarios activos
        self.fields['fk_horario'].queryset = HorarioMedicoModel.objects.filter(activo=True)
        # Ordenar pacientes por nombre
        self.fields['fk_paciente'].queryset = PacienteModel.objects.all().order_by('nombre')


class AgendaFormasPaciente(forms.ModelForm):
    """Formulario simplificado para pacientes - solo seleccionan horario y fecha"""
    class Meta:
        model = AgendaModel
        fields = ['fk_horario', 'fecha']
        widgets = {
            'fk_horario': forms.Select(attrs={
                'class':'form-select',
                'required': True
            }),
            'fecha': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
                'required': True
            })
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filtrar solo horarios activos
        self.fields['fk_horario'].queryset = HorarioMedicoModel.objects.filter(activo=True)

class RegistroUsuarioForms(forms.ModelForm):
    confirmar_contraseña = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirmar contraseña',
            'required': True
        })
    )
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'email']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre de usuario',
                'required': True
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre completo',
                'required': True
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'correo@ejemplo.com',
                'required': True
            })
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Agregar campo de contraseña
        self.fields['password'] = forms.CharField(
            widget=forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Contraseña',
                'required': True
            })
        )
        # Reordenar campos
        field_order = ['username', 'first_name', 'email', 'password', 'confirmar_contraseña']
        self.fields = {k: self.fields[k] for k in field_order if k in self.fields}
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirmar_contraseña = cleaned_data.get('confirmar_contraseña')
        
        if password and confirmar_contraseña:
            if password != confirmar_contraseña:
                raise ValidationError('Las contraseñas no coinciden')
            if len(password) < 6:
                raise ValidationError('La contraseña debe tener al menos 6 caracteres')
        
        return cleaned_data
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise ValidationError('Este nombre de usuario ya está registrado')
        if len(username) < 3:
            raise ValidationError('El nombre de usuario debe tener al menos 3 caracteres')
        return username
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError('Este correo ya está registrado')
        return email
    
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if first_name and len(first_name) < 3:
            raise ValidationError('El nombre debe tener al menos 3 caracteres')
        return first_name
    
    def save(self, commit=True):
        user = super().save(commit=False)
        # Establecer contraseña
        user.set_password(self.cleaned_data.get('password'))
        if commit:
            user.save()
            # Agregar al grupo Paciente por defecto
            from django.contrib.auth.models import Group
            try:
                paciente_group = Group.objects.get(name='Paciente')
                user.groups.add(paciente_group)
            except Group.DoesNotExist:
                pass
        return user


class CambiarContraseñaForms(forms.Form):
    """Formulario para cambiar contraseña - Solo admin"""
    nueva_contraseña = forms.CharField(
        label='Nueva Contraseña',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Nueva contraseña (mín. 6 caracteres)',
            'required': True,
            'minlength': 6
        }),
        min_length=6,
        help_text='Mínimo 6 caracteres'
    )
    confirmar_contraseña = forms.CharField(
        label='Confirmar Contraseña',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirmar contraseña',
            'required': True
        })
    )
    
    def clean(self):
        cleaned_data = super().clean()
        nueva_contraseña = cleaned_data.get('nueva_contraseña')
        confirmar_contraseña = cleaned_data.get('confirmar_contraseña')
        
        if nueva_contraseña and confirmar_contraseña:
            if nueva_contraseña != confirmar_contraseña:
                self.add_error('confirmar_contraseña', '❌ Las contraseñas no coinciden')
            if len(nueva_contraseña) < 6:
                self.add_error('nueva_contraseña', '❌ La contraseña debe tener al menos 6 caracteres')
        
        return cleaned_data