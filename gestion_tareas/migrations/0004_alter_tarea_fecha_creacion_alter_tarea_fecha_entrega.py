# Generated by Django 4.1 on 2022-09-09 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_tareas', '0003_rename_contraseña_usuario_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarea',
            name='fecha_creacion',
            field=models.DateField(default='', max_length=128),
        ),
        migrations.AlterField(
            model_name='tarea',
            name='fecha_entrega',
            field=models.DateField(default='', max_length=128),
        ),
    ]
