from django.db import models


class Farmacia(models.Model):

    fecha = models.CharField(max_length=255)
    local_id = models.CharField(max_length=255)
    local_nombre = models.CharField(max_length=255)
    comuna_nombre = models.CharField(max_length=255)
    fk_localidad = models.CharField(max_length=255)
    localidad_nombre = models.CharField(max_length=255)
    local_direccion = models.CharField(max_length=255)
    funcionamiento_hora_apertura = models.CharField(max_length=255)
    funcionamiento_hora_cierre = models.CharField(max_length=255)
    local_telefono = models.CharField(max_length=255)
    local_lat = models.CharField(max_length=255)
    local_lng = models.CharField(max_length=255)
    funcionamiento_dia = models.CharField(max_length=255)
    fk_region = models.CharField(max_length=255)
    fk_comuna = models.CharField(max_length=255)
    

    def __str__(self):
        return self.local_nombre
