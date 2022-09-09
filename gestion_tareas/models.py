from datetime import date, datetime
from django.db import models

# Create your models here.
class tarea(models.Model):
    descripcion = models.CharField(max_length=128,default='')
    fecha_creacion= models.DateField(default=date.today())
    fecha_entrega= models.DateField(default=date.today())
    usuario_responsable= models.CharField(max_length=128,default='')
    estado_tarea= models.CharField(max_length=128,default='')

class usuario(models.Model):
    nombre= models.CharField(max_length=128,default='')
    apellido= models.CharField(max_length=128,default='')
    codigo_usuario= models.CharField(max_length=128,default='')
    password= models.CharField(max_length=128,default='')