# Generated by Django 4.1.7 on 2023-09-20 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculosApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehiculo',
            name='comentario',
            field=models.TextField(default='', null=True),
        ),
    ]
