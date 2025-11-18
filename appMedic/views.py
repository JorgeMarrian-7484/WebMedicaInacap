from django.shortcuts import render
from appMedic.models import AgendaModel,MedicoModel,ExpedienteModel, HorarioMedicoModel,PacienteModel
from appMedic.forms import MedicoForms, HorarioForms,PacienteForms,AgendaForms
from django.contrib import messages

# Create your views here.

def inicio (request):
    return render(request,'index.html')
def login (request):
    return render(request,'components/login.html')
def medico (request):
    medico = MedicoModel.objects.all().order_by('nombre')
    data = {
        'titulo': 'Lista Medicos',
        'categoria':'Lista',
        'medico': medico
    }
    return render(request,'components/medico.html',data)

def cmedico (request):
    form = MedicoForms()
    data = {
        'titulo':'Crear Medicos 🩺',
        'form': form,
        'ruta': '/components/medico'
    }
    if request.method == 'POST':
        form = MedicoForms(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Medico Registrado')
    return render(request,'components/create.html',data) # esta opcion tenla en cuenta para que el admin sea quien acceda a ella

def horario (request):
    horario = HorarioMedicoModel.objects.all().order_by()
    data = {
        'titulo' : 'Listar Horario',
        'horario': horario
    }
    return render(request,'components/horario.html',data)

def chorario (request):
    form = HorarioForms()
    data = {
        'titulo':'Crear Horario',
        'form': form,
        'ruta':'/components/horario/'
    }
    if request.method == 'POST':
        form = HorarioForms(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Horario Creado')
    return render(request,'components/create.html',data)

def paciente(request):
    paciente = PacienteModel.objects.all().order_by('nombre')
    data = {
        'titulo':'Lista de pacientes',
        'paciente': paciente
    }
    return render(request,'components/paciente.html',data)

def cpaciente (request):
    form = PacienteForms()
    data = {
        'titulo':'Guardar pacientes',
        'form': form,
        'ruta': '/components/paciente'
    }
    if request.method == 'POST':
        form = PacienteForms(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Paciente Registrado')
    return render (request,'components/create.html',data)

def agendar(request):
    form = AgendaForms()
    data = {
        'titulo':'Crear cita medica',
        'form': form,
        'agendar': agendar
    }
    return render(request,'components/create.html',data)