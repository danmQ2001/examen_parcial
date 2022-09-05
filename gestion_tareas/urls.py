from.import views
from django.urls import path

app_name='gestion_tareas'

urlpatterns=[
    path('',views.login,name='login'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('crear_tarea',views.crear_tarea,name='crear_tarea'),
    path('editar_tarea/<str:ind>',views.editar_tarea,name='editar_tarea'),
]

