from django.shortcuts import redirect, render, get_object_or_404
from appMedic.models import AgendaModel,MedicoModel, HorarioMedicoModel,PacienteModel
from appMedic.forms import MedicoForms, HorarioForms,PacienteForms, RegistroUsuarioForms, CambiarContraseñaForms
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
import xlwt
from datetime import datetime

# Create your views here.

def inicio(request):
    """Página de inicio - Redirige a login si no está autenticado"""
    if not request.user.is_authenticated:
        return redirect('login')
    
    # Usuario autenticado, mostrar dashboard
    data = {
        'usuario': request.user,
        'es_admin': es_admin(request.user),
        'es_medico': es_medico(request.user),
        'es_paciente': es_paciente(request.user),
        'rol': obtener_rol(request.user)
    }
    return render(request, 'index.html', data)

def es_admin(user):
    """Verificar si el usuario es admin"""
    return user.is_staff or user.is_superuser

def es_medico(user):
    """Verificar si el usuario es médico"""
    return user.groups.filter(name='Medico').exists()

def es_paciente(user):
    """Verificar si el usuario es paciente"""
    return user.groups.filter(name='Paciente').exists()

def obtener_rol(user):
    """Obtener el rol del usuario como string"""
    if es_admin(user):
        return 'Administrador'
    elif es_medico(user):
        return 'Médico'
    elif es_paciente(user):
        return 'Paciente'
    return 'Usuario'

def login (request):
    """Vista de login con autenticación Django"""
    if request.user.is_authenticated:
        return redirect('inicio')
    
    error_message = None
    
    if request.method == 'POST':
        from django.contrib.auth import authenticate, login as auth_login
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            messages.success(request, f'✅ ¡Bienvenido {user.first_name or user.username}!')
            return redirect('inicio')
        else:
            error_message = '❌ Usuario o contraseña incorrectos'
    
    data = {
        'error': error_message
    }
    return render(request, 'components/login.html', data)

def logout_view(request):
    """Cerrar sesión"""
    from django.contrib.auth import logout
    logout(request)
    messages.success(request, '✅ Sesión cerrada correctamente')
    return redirect('login')

def registro(request):
    """Registrar nuevo usuario"""
    if request.user.is_authenticated:
        return redirect('inicio')
    
    form = RegistroUsuarioForms()
    data = {
        'titulo': '📝 Registrar Nueva Cuenta',
        'form': form,
        'ruta': '/'
    }
    
    if request.method == 'POST':
        form = RegistroUsuarioForms(request.POST)
        if form.is_valid():
            usuario = form.save()
            
            # Crear automáticamente un perfil de paciente vinculado al usuario
            PacienteModel.objects.create(
                user=usuario,
                nombre=usuario.first_name or usuario.username,
                rut='',  # Se puede dejar en blanco o pedir en el formulario después
                correo=usuario.email or '',
                telefono=0,  # Se puede actualizar después
                direccion=''  # Se puede actualizar después
            )
            
            messages.success(request, f'✅ Cuenta creada exitosamente. ¡Bienvenido {usuario.first_name or usuario.username}! Inicia sesión ahora.')
            return redirect('login')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{field}: {error}')
    
    return render(request, 'components/create.html', data)
###### Ajustes mios
def medico (request):
    medico = MedicoModel.objects.all().order_by('nombre')
    data = {
        'titulo': 'Lista de Médicos',
        'categoria':'Gestión Médica',
        'medico': medico
    }
    return render(request,'components/medico.html',data)

def cmedico (request):
    """Crear nuevo médico - Solo admin (SIEMPRE con usuario)"""
    if not es_admin(request.user):
        messages.error(request, '❌ No tienes permiso para crear médicos')
        return redirect('inicio')
    
    form = MedicoForms()
    titulo = 'Registrar Nuevo Médico 🩺'
    
    data = {
        'titulo': titulo,
        'form': form,
        'ruta': '/components/medico/'
    }
    
    if request.method == 'POST':
        form = MedicoForms(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request,'✅ Médico registrado exitosamente con cuenta de usuario')
            return redirect('medico')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'❌ {field}: {error}')
    
    return render(request,'components/create.html',data)

def emedico(request, id):
    """Editar médico existente - Solo admin"""
    if not es_admin(request.user):
        messages.error(request, '❌ No tienes permiso para editar médicos')
        return redirect('inicio')
    
    medico = get_object_or_404(MedicoModel, id=id)
    form = MedicoForms(instance=medico)
    data = {
        'titulo': f'Editar Médico: {medico.nombre}',
        'form': form,
        'ruta': '/components/medico/'
    }
    if request.method == 'POST':
        form = MedicoForms(request.POST, instance=medico)
        if form.is_valid():
            form.save()
            messages.success(request, f'✅ Médico {medico.nombre} actualizado correctamente')
            return redirect('medico')
    return render(request, 'components/create.html', data)

def dmedico(request, id):
    """Eliminar médico - Solo admin"""
    if not es_admin(request.user):
        messages.error(request, '❌ No tienes permiso para eliminar médicos')
        return redirect('inicio')
    
    medico = get_object_or_404(MedicoModel, id=id)
    if request.method == 'POST':
        # Si el médico tiene un usuario asociado, eliminarlo también
        if medico.user:
            medico.user.delete()
        medico.delete()
        messages.success(request, f'✅ Médico {medico.nombre} eliminado correctamente')
        return redirect('medico')
    
    data = {
        'titulo': f'Confirmar eliminación de {medico.nombre}',
        'medico': medico
    }
    return render(request, 'components/confirmar_eliminar.html', data)

def horario (request):
    horario = HorarioMedicoModel.objects.all().order_by('dia_semana','hora_inicio')
    data = {
        'titulo' : 'Lista de Horarios Médicos',
        'horario': horario
    }
    return render(request,'components/horario.html',data)

def chorario (request):
    """Crear nuevo horario - Solo admin y médicos"""
    if not (es_admin(request.user) or es_medico(request.user)):
        messages.error(request, '❌ No tienes permiso para crear horarios')
        return redirect('inicio')
    
    form = HorarioForms()
    data = {
        'titulo':'Crear Nuevo Horario 📅',
        'form': form,
        'ruta':'/components/horario/'
    }
    if request.method == 'POST':
        form = HorarioForms(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'✅ Horario creado exitosamente')
            return redirect('horario')
    return render(request,'components/create.html',data)

def ehorario(request, id):
    """Editar horario existente - Solo admin y médicos"""
    if not (es_admin(request.user) or es_medico(request.user)):
        messages.error(request, '❌ No tienes permiso para editar horarios')
        return redirect('inicio')
    
    horario = get_object_or_404(HorarioMedicoModel, id=id)
    form = HorarioForms(instance=horario)
    data = {
        'titulo': f'Editar Horario de {horario.fk_medico.nombre}',
        'form': form,
        'ruta': '/components/horario/'
    }
    if request.method == 'POST':
        form = HorarioForms(request.POST, instance=horario)
        if form.is_valid():
            form.save()
            messages.success(request, '✅ Horario actualizado correctamente')
            return redirect('horario')
    return render(request, 'components/create.html', data)

def dhorario(request, id):
    """Eliminar horario - Solo admin y médicos"""
    if not (es_admin(request.user) or es_medico(request.user)):
        messages.error(request, '❌ No tienes permiso para eliminar horarios')
        return redirect('inicio')
    
    horario = get_object_or_404(HorarioMedicoModel, id=id)
    if request.method == 'POST':
        medico_nombre = horario.fk_medico.nombre
        horario.delete()
        messages.success(request, f'✅ Horario de {medico_nombre} eliminado correctamente')
        return redirect('horario')
    
    data = {
        'titulo': f'Confirmar eliminación del horario',
        'horario': horario
    }
    return render(request, 'components/confirmar_eliminar_horario.html', data)

@login_required(login_url='login')
def paciente(request):
    """Ver lista de pacientes - Solo admin y médicos"""
    if not (es_admin(request.user) or es_medico(request.user)):
        messages.error(request, '❌ No tienes permiso para ver esta página')
        return redirect('inicio')
    
    paciente = PacienteModel.objects.all().order_by('nombre')
    data = {
        'titulo':'Lista de Pacientes',
        'categoria': 'Gestión de Pacientes',
        'paciente': paciente
    }
    return render(request,'components/paciente.html',data)

@login_required(login_url='login')
def mis_citas(request):
    """Ver citas del paciente autenticado"""
    # Obtener el perfil de paciente del usuario actual
    try:
        paciente = PacienteModel.objects.get(user=request.user)
        citas = AgendaModel.objects.filter(fk_paciente=paciente).order_by('fecha', 'fk_horario__hora_inicio')
    except PacienteModel.DoesNotExist:
        citas = []
        paciente = None
    
    data = {
        'titulo': 'Mis Citas Médicas',
        'citas': citas,
        'paciente': paciente
    }
    return render(request, 'components/mis_citas.html', data)

@login_required(login_url='login')
def cpaciente (request):
    """Crear paciente - Solo admin y médicos"""
    if not (es_admin(request.user) or es_medico(request.user)):
        messages.error(request, '❌ No tienes permiso para registrar pacientes')
        return redirect('inicio')
    
    form = PacienteForms()
    data = {
        'titulo':'Registrar Nuevo Paciente 👤',
        'form': form,
        'ruta': '/components/paciente/'
    }
    if request.method == 'POST':
        form = PacienteForms(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'✅ Paciente registrado exitosamente')
            return redirect('paciente')
    return render (request,'components/create.html',data)

@login_required(login_url='login')
def epaciente(request, id):
    """Editar paciente existente - Solo admin y médicos"""
    if not (es_admin(request.user) or es_medico(request.user)):
        messages.error(request, '❌ No tienes permiso para editar pacientes')
        return redirect('inicio')
    
    paciente = get_object_or_404(PacienteModel, id=id)
    form = PacienteForms(instance=paciente)
    data = {
        'titulo': f'Editar Paciente: {paciente.nombre}',
        'form': form,
        'ruta': '/components/paciente/'
    }
    if request.method == 'POST':
        form = PacienteForms(request.POST, instance=paciente)
        if form.is_valid():
            form.save()
            messages.success(request, f'✅ Paciente {paciente.nombre} actualizado correctamente')
            return redirect('paciente')
    return render(request, 'components/create.html', data)

@login_required(login_url='login')
def dpaciente(request, id):
    """Eliminar paciente - Solo admin y médicos"""
    if not (es_admin(request.user) or es_medico(request.user)):
        messages.error(request, '❌ No tienes permiso para eliminar pacientes')
        return redirect('inicio')
    
    paciente = get_object_or_404(PacienteModel, id=id)
    if request.method == 'POST':
        paciente.delete()
        messages.success(request, f'✅ Paciente {paciente.nombre} eliminado correctamente')
        return redirect('paciente')
    
    data = {
        'titulo': f'Confirmar eliminación de {paciente.nombre}',
        'paciente': paciente
    }
    return render(request, 'components/confirmar_eliminar_paciente.html', data)

def agendar(request):
    from appMedic.forms import AgendaForms, AgendaFormasPaciente
    
    # Determinar la ruta de retorno según el rol del usuario
    if es_paciente(request.user):
        ruta_retorno = 'misCitas'
        ruta_url = '/components/mis-citas/'
        form_class = AgendaFormasPaciente
    else:
        ruta_retorno = 'paciente'
        ruta_url = '/components/paciente/'
        form_class = AgendaForms
    
    form = form_class()
    data = {
        'titulo': '📝 Agendar Cita Médica',
        'form': form,
        'ruta': ruta_url,
        'es_paciente': es_paciente(request.user)
    }
    
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            cita = form.save(commit=False)
            
            # Si es paciente, asignar automáticamente su perfil
            if es_paciente(request.user):
                try:
                    paciente = PacienteModel.objects.get(user=request.user)
                    cita.fk_paciente = paciente
                except PacienteModel.DoesNotExist:
                    messages.error(request, '❌ No se encontró tu perfil de paciente')
                    return render(request, 'components/create.html', data)
            
            # Verificar si la cita ya existe
            if AgendaModel.objects.filter(
                fk_horario=cita.fk_horario, 
                fecha=cita.fecha
            ).exists():
                messages.error(request, '❌ Esta cita ya está ocupada. Por favor selecciona otro horario o fecha.')
            else:
                cita.save()
                messages.success(request, '✅ Cita agendada exitosamente')
                return redirect(ruta_retorno)
    
    return render(request, 'components/create.html', data)

# ==================== EXPORTAR A EXCEL ====================

@login_required(login_url='login')
def exportar_medicos_excel(request):
    """Exportar médicos a Excel - Solo admin"""
    if not es_admin(request.user):
        messages.error(request, '❌ No tienes permiso para exportar!')
        return redirect('medico')
    
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=medicos.xls'
    archivo = xlwt.Workbook(encoding='utf-8')
    hoja = archivo.add_sheet('Médicos')
    
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    
    columnas = ['ID', 'Nombre', 'Especialidad', 'Correo', 'Teléfono']
    for i in range(len(columnas)):
        hoja.write(row_num, i, columnas[i], font_style)
    
    font_style = xlwt.XFStyle()
    filas = MedicoModel.objects.all().values_list('id', 'nombre', 'especialidad', 'correo', 'telefono')
    
    for f in filas:
        row_num += 1
        for col_num in range(len(f)):
            hoja.write(row_num, col_num, str(f[col_num]), font_style)
    
    archivo.save(response)
    return response


@login_required(login_url='login')
def exportar_pacientes_excel(request):
    """Exportar pacientes a Excel - Solo admin"""
    if not es_admin(request.user):
        messages.error(request, '❌ No tienes permiso para exportar!')
        return redirect('paciente')
    
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=pacientes.xls'
    archivo = xlwt.Workbook(encoding='utf-8')
    hoja = archivo.add_sheet('Pacientes')
    
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    
    columnas = ['ID', 'Nombre', 'RUT', 'Correo', 'Teléfono', 'Dirección']
    for i in range(len(columnas)):
        hoja.write(row_num, i, columnas[i], font_style)
    
    font_style = xlwt.XFStyle()
    filas = PacienteModel.objects.all().values_list('id', 'nombre', 'rut', 'correo', 'telefono', 'direccion')
    
    for f in filas:
        row_num += 1
        for col_num in range(len(f)):
            hoja.write(row_num, col_num, str(f[col_num]), font_style)
    
    archivo.save(response)
    return response


@login_required(login_url='login')
def exportar_horarios_excel(request):
    """Exportar horarios a Excel - Solo admin o médicos"""
    if not (es_admin(request.user) or es_medico(request.user)):
        messages.error(request, '❌ No tienes permiso para exportar!')
        return redirect('horario')
    
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=horarios.xls'
    archivo = xlwt.Workbook(encoding='utf-8')
    hoja = archivo.add_sheet('Horarios')
    
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    
    columnas = ['ID', 'Médico', 'Día Semana', 'Hora Inicio', 'Hora Fin', 'Activo']
    for i in range(len(columnas)):
        hoja.write(row_num, i, columnas[i], font_style)
    
    font_style = xlwt.XFStyle()
    filas = HorarioMedicoModel.objects.all().values_list(
        'id', 'fk_medico__nombre', 'dia_semana', 'hora_inicio', 'hora_fin', 'activo'
    )
    
    dias_mapping = {1: 'Lunes', 2: 'Martes', 3: 'Miércoles', 4: 'Jueves', 5: 'Viernes'}
    
    for f in filas:
        row_num += 1
        fila_lista = list(f)
        # Reemplazar número de día por nombre
        fila_lista[2] = dias_mapping.get(fila_lista[2], fila_lista[2])
        # Convertir booleano a Sí/No
        fila_lista[5] = 'Sí' if fila_lista[5] else 'No'
        
        for col_num in range(len(fila_lista)):
            hoja.write(row_num, col_num, str(fila_lista[col_num]), font_style)
    
    archivo.save(response)
    return response


@login_required(login_url='login')
def exportar_agenda_excel(request):
    """Exportar agenda/citas a Excel - Solo admin o médicos"""
    if not (es_admin(request.user) or es_medico(request.user)):
        messages.error(request, '❌ No tienes permiso para exportar!')
        return redirect('paciente')
    
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=agenda.xls'
    archivo = xlwt.Workbook(encoding='utf-8')
    hoja = archivo.add_sheet('Agenda')
    
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    
    columnas = ['ID', 'Médico', 'Paciente', 'Fecha', 'Hora Inicio', 'Disponible']
    for i in range(len(columnas)):
        hoja.write(row_num, i, columnas[i], font_style)
    
    font_style = xlwt.XFStyle()
    filas = AgendaModel.objects.all().values_list(
        'id', 'fk_horario__fk_medico__nombre', 'fk_paciente__nombre', 
        'fecha', 'fk_horario__hora_inicio', 'disponible'
    )
    
    for f in filas:
        row_num += 1
        fila_lista = list(f)
        # Convertir booleano a Sí/No
        fila_lista[5] = 'Sí' if fila_lista[5] else 'No'
        
        for col_num in range(len(fila_lista)):
            hoja.write(row_num, col_num, str(fila_lista[col_num]), font_style)
    
    archivo.save(response)
    return response


@login_required(login_url='login')
def usuarios(request):
    """Ver lista de usuarios - Solo admin"""
    if not es_admin(request.user):
        messages.error(request, '❌ No tienes permiso para ver usuarios')
        return redirect('inicio')
    
    from django.contrib.auth.models import User
    
    usuarios_lista = User.objects.all().order_by('username')
    usuarios_data = []
    
    for usuario in usuarios_lista:
        rol = obtener_rol(usuario)
        datos_usuario = {
            'id': usuario.id,
            'usuario': usuario,
            'rol': rol,
            'username': usuario.username,
            'email': usuario.email,
            'es_staff': usuario.is_staff,
            'es_activo': usuario.is_active
        }
        usuarios_data.append(datos_usuario)
    
    data = {
        'titulo': '👥 Gestión de Usuarios',
        'usuarios': usuarios_data
    }
    return render(request, 'components/usuarios.html', data)


@login_required(login_url='login')
def cambiar_contraseña(request, user_id):
    """Cambiar contraseña de un usuario - Solo admin"""
    if not es_admin(request.user):
        messages.error(request, '❌ No tienes permiso para cambiar contraseñas')
        return redirect('inicio')
    
    from django.contrib.auth.models import User
    usuario = get_object_or_404(User, id=user_id)
    
    form = CambiarContraseñaForms()
    data = {
        'titulo': f'Cambiar Contraseña de {usuario.username}',
        'form': form,
        'ruta': '/components/usuarios/',
        'usuario_objetivo': usuario
    }
    
    if request.method == 'POST':
        form = CambiarContraseñaForms(request.POST)
        if form.is_valid():
            nueva_contraseña = form.cleaned_data['nueva_contraseña']
            usuario.set_password(nueva_contraseña)
            usuario.save()
            messages.success(request, f'✅ Contraseña de {usuario.username} actualizada correctamente')
            return redirect('usuarios')
    
    return render(request, 'components/create.html', data)