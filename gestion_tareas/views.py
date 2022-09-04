from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def login(request):
    if request.method=='POST':
        nombreUsuario=request.POST.get('nombreUsuario')
        passwordUsuario=request.POST.get('passwordUsuario')
    return render(request,'gestion_tareas/login.html')
def dashboard(request):
    return render(request,'gestion_tareas/dashboard.html')
