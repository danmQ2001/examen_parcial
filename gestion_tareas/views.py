from django.shortcuts import render
from gestion_tareas.models import usuario,tarea
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from dateutil.parser import parse
from datetime import date, datetime
# Create your views here.
def login(request):
    if request.method=='POST':
        nombreUsuario = request.POST.get('nombreUsuario')
        passwordUsuario = request.POST.get('passwordUsuario')
        #validando usuarios
        parametro_o=0
        usuario_registrado=0
        usuarios_totales= usuario.objects.all()

        for persona in usuarios_totales:
            if persona.nombre == nombreUsuario and persona.password == passwordUsuario:
                usuario_registrado=1
                id_person=persona.id
       
        if usuario_registrado==1:
            return HttpResponseRedirect(reverse('gestion_tareas:dashboard', kwargs={'id_user' : id_person , 'tarea_id_finalizar' : parametro_o })
            )
        else:
            return render(request,'gestion_tareas/login.html',{
                'mensaje':'Los datos ingresados no son correcto o no están registrados',
            })            
    return render(request,'gestion_tareas/login.html')
def dashboard(request,id_user,tarea_id_finalizar):
    tareas_totales = tarea.objects.all()
    #Filtrar tareas del usuario
    lista_tareas = []
    user_responsable=usuario.objects.get(id=id_user)
    tareas_totales = tarea.objects.filter(usuario_responsable= user_responsable.nombre)
    if tarea_id_finalizar != '0' and tarea_id_finalizar != 0:
        finalizar_tarea=tarea.objects.get(id=int(tarea_id_finalizar))
    for homework in tareas_totales: 
        if tarea_id_finalizar != '0' and tarea_id_finalizar != 0 :
            if homework.id==finalizar_tarea.id:
                homework.estado_tarea='3'
                homework.save()
    # Calcular cantidad de días para realizar la tarea
        ga=homework.fecha_entrega


        fecha_f=homework.fecha_entrega
        fecha_i=date.today()


        remaining_days = (fecha_f - fecha_i).days
        if homework.estado_tarea !='3':
            if remaining_days>2 :
                homework.estado_tarea='1'
            elif remaining_days<=2 and remaining_days>=0 :
                homework.estado_tarea='2'
            else :
                homework.estado_tarea='4'
    #ciclo de filtración finalizado
        lista_tareas.append(homework)
        #tarea_id_finalizar=0
    return render(request,'gestion_tareas/dashboard.html',{
        'objTarea':lista_tareas,
        'user':id_user,
    })
def crear_tarea(request,mantener_id):
    if request.method =='POST':
        mantener_parametro='0'
        descripcion = request.POST.get('descripcion')
        fecha_creacion=request.POST.get('fecha_creacion')
        fecha_creacion=parse(fecha_creacion)
        fecha_entrega=request.POST.get('fecha_entrega')
        fecha_entrega=parse(fecha_entrega)
        usuario_responsable=request.POST.get('usuario_responsable')
        tarea(descripcion=descripcion,fecha_creacion=fecha_creacion,fecha_entrega=fecha_entrega,usuario_responsable=usuario_responsable,estado_tarea='1').save()
        return HttpResponseRedirect(reverse('gestion_tareas:dashboard',kwargs={'id_user' : mantener_id, 'tarea_id_finalizar' : mantener_parametro}))
    return render(request,'gestion_tareas/crear_tarea.html',{
        'id_persona':mantener_id,
    })

def editar_tarea(request,ind):
    EditarTarea=tarea.objects.get(id=ind)
    persona=usuario.objects.get(nombre=EditarTarea.usuario_responsable)
    id_persona=persona.id
    if request.method=='POST':
        EditarTarea.descripcion = request.POST.get('descripcion')
        EditarTarea.fecha_creacion=request.POST.get('fecha_creacion')    
        EditarTarea.fecha_entrega=request.POST.get('fecha_entrega')
        EditarTarea.usuario_responsable=request.POST.get('usuario_responsable')
        EditarTarea.save()
        return HttpResponseRedirect(reverse('gestion_tareas:dashboard',kwargs={'id_user' : id_persona, 'tarea_id_finalizar' : 0}))
    return render(request,'gestion_tareas/editar_tarea.html',{
        'tarea_info':EditarTarea,
        'id_username':id_persona,
    })    