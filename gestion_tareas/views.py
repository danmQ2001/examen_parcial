from django.shortcuts import render
from django.http import HttpResponse
from gestion_tareas.models import usuario,tarea
from django.http import HttpResponseRedirect
from django.urls import reverse
from dateutil.parser import parse
# Create your views here.
def login(request):
    if request.method=='POST':
        nombreUsuario = request.POST.get('nombreUsuario')
        passwordUsuario = request.POST.get('passwordUsuario')
        #validando usuarios
        usuario_registrado=0
        usuarios_totales= usuario.objects.all()

        for persona in usuarios_totales:
            if persona.nombre == nombreUsuario and persona.password == passwordUsuario:
                usuario_registrado=1
       
        if usuario_registrado==1:
            return HttpResponseRedirect(reverse('gestion_tareas:dashboard'),{
                'usuario_ingresado': nombreUsuario,
            })
        else:
            return render(request,'gestion_tareas/login.html',{
                'mensaje':'Los datos ingresados no son correcto o no están registrados',
            })            
    return render(request,'gestion_tareas/login.html')
def dashboard(request):
    tareas_totales = tarea.objects.all()
    #Filtrar tareas del usuario
    lista_tareas = []
    tareas_totales = tarea.objects.filter(usuario_responsable='dany')
    for homework in tareas_totales:
        lista_tareas.append(homework)
    #ciclo de filtración finalizado
    return render(request,'gestion_tareas/dashboard.html',{
        'objTarea':lista_tareas,
    })
def crear_tarea(request):
    if request.method =='POST':
        descripcion = request.POST.get('descripcion')
        fecha_creacion=request.POST.get('fecha_creacion')
        fecha_creacion=parse(fecha_creacion)
        fecha_entrega=request.POST.get('fecha_entrega')
        fecha_entrega=parse(fecha_entrega)
        usuario_responsable=request.POST.get('usuario_responsable')
        tarea(descripcion=descripcion,fecha_creacion=fecha_creacion,fecha_entrega=fecha_entrega,usuario_responsable=usuario_responsable,estado_tarea='').save()
        return HttpResponseRedirect(reverse('gestion_tareas:dashboard'))
    return render(request,'gestion_tareas/crear_tarea.html')
         
