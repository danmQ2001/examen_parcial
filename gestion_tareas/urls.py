from.import views
from django.urls import path

app_name='gestion_tareas'

urlpatterns=[
    path('login',views.login,name='login'),
    path('dashboard',views.dashboard,name='dashboard'),
]

