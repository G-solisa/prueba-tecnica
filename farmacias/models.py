from django.db import models


class Farmacia(models.Model):

    fecha = models.DateField()
    local_id = models.IntegerField()
    local_nombre = models.CharField(max_length=255)
    comuna_nombre = models.CharField(max_length=255)
    fk_localidad = models.IntegerField()
    localidad_nombre = models.CharField(max_length=255)
    local_direccion = models.CharField(max_length=255)
    funcionamiento_hora_apertura = models.DateTimeField()
    funcionamiento_hora_cierre = models.DateTimeField()
    local_telefono = models.IntegerField()
    local_lat = models.CharField(max_length=255)
    local_lng = models.CharField(max_length=255)
    funcionamiento_dia = models.CharField(max_length=255)
    fk_region = models.CharField(max_length=255)
    fk_comuna = models.CharField(max_length=255)
    

    def __str__(self):
        return self.local_nombres
