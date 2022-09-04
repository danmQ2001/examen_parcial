from django.shortcuts import render
from django.http import HttpResponse
from gestion_tareas.models import usuario,tarea
from django.http import HttpResponseRedirect
from django.urls import reverse
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
            return HttpResponseRedirect(reverse('gestion_tareas:dashboard'))
        else:
            return render(request,'gestion_tareas/login.html',{
                'mensaje':'Los datos ingresados no son correcto o no están registrados',
            })            
    return render(request,'gestion_tareas/login.html')
def dashboard(request):
    return render(request,'gestion_tareas/dashboard.html')
