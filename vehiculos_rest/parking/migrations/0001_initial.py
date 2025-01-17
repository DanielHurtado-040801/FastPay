# Generated by Django 4.1.7 on 2023-09-20 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Parking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor_minuto', models.DecimalField(decimal_places=2, default=85, max_digits=3, verbose_name='Valor Minuto')),
                ('tarifa_minima', models.DecimalField(decimal_places=2, default=800, max_digits=5, verbose_name='Valor Tarifa Minima')),
                ('tarifa_maxima', models.DecimalField(decimal_places=2, default=25000, max_digits=5, verbose_name='Valor Tarifa Maxima')),
            ],
        ),
    ]
