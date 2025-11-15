from django import forms
from appMedic.models import MedicoModel, HorarioMedicoModel, PacienteModel

#Clases para horarios de los medicos

class MedicoForms (forms.ModelForm):
    class Meta:
        model = MedicoModel
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'especialidad': forms.TextInput(attrs={'class':'form-control'}),
            'correo': forms.EmailInput(attrs={'class':'form-control'}),
            'telefono': forms.NumberInput(attrs={'class':'form-control'})

        }

class HorarioForms (forms.ModelForm):
    class Meta:
        model = HorarioMedicoModel
        fields = ['fk_medico','dia_semana', 'hora_inicio', 'hora_fin']
        widgets = {
            'fk_medico':forms.Select(attrs={'class':'form-select'}),
            'dia_semana': forms.Select(attrs={'class':'form-control'}),
            'hora_inicio': forms.TimeInput(attrs={'class':'form-control', 'type': 'time'}),
            'hora_fin': forms.TimeInput(attrs={'class':'form-control', 'type': 'time'}),
        }

class PacienteForms (forms.ModelForm):
    class Meta:
        model = PacienteModel
        fields = '__all__'
        widgets = {
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'rut':forms.TextInput(attrs={'class':'form-control'}),
            'correo': forms.EmailInput(attrs={'class':'form-control'}),
        }