# Generated by Django 4.1 on 2022-09-04 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tarea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(default='', max_length=128)),
                ('fecha_creacion', models.CharField(default='', max_length=128)),
                ('fecha_entrega', models.CharField(default='', max_length=128)),
                ('usuario_responsable', models.CharField(default='', max_length=128)),
                ('estado_tarea', models.CharField(default='', max_length=128)),
            ],
        ),
    ]