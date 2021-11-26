# Generated by Django 3.2.9 on 2021-11-26 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Farmacia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField()),
                ('local_id', models.IntegerField()),
                ('local_nombre', models.CharField(max_length=255)),
                ('comuna_nombre', models.CharField(max_length=255)),
                ('fk_localidad', models.IntegerField()),
                ('localidad_nombre', models.CharField(max_length=255)),
                ('local_direccion', models.CharField(max_length=255)),
                ('funcionamiento_hora_apertura', models.DateTimeField()),
                ('funcionamiento_hora_cierre', models.DateTimeField()),
                ('local_telefono', models.IntegerField()),
                ('local_lat', models.CharField(max_length=255)),
                ('local_lng', models.CharField(max_length=255)),
                ('funcionamiento_dia', models.CharField(max_length=255)),
                ('fk_region', models.CharField(max_length=255)),
                ('fk_comuna', models.CharField(max_length=255)),
            ],
        ),
    ]