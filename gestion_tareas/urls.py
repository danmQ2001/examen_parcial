from.import views
from django.urls import path

app_name='gestion_tareas'

urlpatterns=[
    path('',views.login,name='login'),
    path('dashboard/<str:id_user>/<str:tarea_id_finalizar>/<str:tarea_id_eliminar>',views.dashboard,name='dashboard'),
    path('crear_tarea/<str:mantener_id>',views.crear_tarea,name='crear_tarea'),
    path('editar_tarea/<str:ind>',views.editar_tarea,name='editar_tarea'),
    path('mostrar_info/<str:ind>',views.mostrar_info,name='mostrar_info'),
]

