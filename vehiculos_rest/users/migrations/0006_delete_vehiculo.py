# Generated by Django 4.1.7 on 2023-03-23 01:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_vehiculo_options_alter_vehiculo_hora_salida'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Vehiculo',
        ),
    ]