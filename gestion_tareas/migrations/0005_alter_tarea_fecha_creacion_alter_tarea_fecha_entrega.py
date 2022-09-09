# Generated by Django 4.1 on 2022-09-09 06:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_tareas', '0004_alter_tarea_fecha_creacion_alter_tarea_fecha_entrega'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarea',
            name='fecha_creacion',
            field=models.DateField(default=datetime.date(2022, 9, 9)),
        ),
        migrations.AlterField(
            model_name='tarea',
            name='fecha_entrega',
            field=models.DateField(default=datetime.date(2022, 9, 9)),
        ),
    ]