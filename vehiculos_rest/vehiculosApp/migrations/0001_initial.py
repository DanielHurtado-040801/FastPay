# Generated by Django 4.1.7 on 2023-03-22 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placa', models.CharField(max_length=6, unique=True, verbose_name='Placa identificada')),
                ('img_placa', models.ImageField(max_length=255, unique=True, upload_to='', verbose_name='Imagen Placa')),
                ('hora_ingreso', models.TimeField(auto_now_add=True, verbose_name='Hora de ingreso')),
                ('hora_salida', models.TimeField(auto_now_add=True, null=True, verbose_name='Hora de salida')),
                ('salida', models.BooleanField(default=False)),
            ],
        ),
    ]