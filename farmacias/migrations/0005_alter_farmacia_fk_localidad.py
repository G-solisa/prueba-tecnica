# Generated by Django 3.2.9 on 2021-11-26 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmacias', '0004_alter_farmacia_local_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmacia',
            name='fk_localidad',
            field=models.CharField(max_length=255),
        ),
    ]
