# Generated by Django 4.1.7 on 2023-05-22 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('modified_date', models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha de modificacion')),
                ('delete_date', models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha de eliminacion')),
                ('placa', models.CharField(max_length=10, unique=True, verbose_name='Placa identificada')),
                ('img_placa', models.ImageField(max_length=255, null=True, upload_to='placas/', verbose_name='Imagen Placa')),
                ('hora_ingreso', models.DateTimeField(verbose_name='Hora de ingreso')),
                ('hora_pago', models.DateTimeField(null=True, verbose_name='Hora de pago')),
                ('valor_pagar', models.DecimalField(decimal_places=2, default=0, max_digits=8, null=True)),
                ('salida', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Modelo Base',
                'verbose_name_plural': 'Modelos Base',
                'abstract': False,
            },
        ),
    ]
