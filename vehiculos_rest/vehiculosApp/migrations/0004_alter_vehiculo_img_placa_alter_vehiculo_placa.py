# Generated by Django 4.1.7 on 2023-03-24 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculosApp', '0003_alter_vehiculo_hora_salida'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiculo',
            name='img_placa',
            field=models.ImageField(max_length=255, null=True, unique=True, upload_to='placas/', verbose_name='Imagen Placa'),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='placa',
            field=models.CharField(max_length=10, unique=True, verbose_name='Placa identificada'),
        ),
    ]