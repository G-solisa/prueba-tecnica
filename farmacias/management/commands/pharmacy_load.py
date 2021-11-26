from django.core.management.base import BaseCommand
from farmacias.models import Farmacia
import requests
import json

url = 'https://farmanet.minsal.cl/maps/index.php/ws/getLocalesTurnos'


class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        response = requests.get(url)

        if response.status_code == 200:
            j_data = response.json()

        instances = [Farmacia(fecha=data['fecha'],
                              local_id=data['local_id'],
                              local_nombre=data['local_nombre'],
                              comuna_nombre=data['comuna_nombre'],
                              fk_localidad=data['fk_localidad'],
                              localidad_nombre=data['localidad_nombre'],
                              local_direccion=data['local_direccion'],
                              funcionamiento_hora_apertura=data['funcionamiento_hora_apertura'],
                              funcionamiento_hora_cierre=data['funcionamiento_hora_cierre'],
                              local_telefono=data['local_telefono'],
                              local_lat=data['local_lat'],
                              local_lng=data['local_lng'],
                              funcionamiento_dia=data['funcionamiento_dia'],
                              fk_region=data['fk_region'],
                              fk_comuna=data['fk_comuna']) for data in j_data]

        Farmacia.objects.bulk_create(instances)
        
        pharmas_filter = Farmacia.objects.all()
        
        clean_filter = []
        result = Farmacia.objects.values_list('local_nombre', flat=True)
        for  x in result:
            if x not in clean_filter:
                clean_filter.append(x)
    
    
        print(clean_filter)
            #     # for i in pharmas_filter:
            #     #     if i not in clean_filter:
            #     #         clean_filter.append(i)
            #     # print(clean_filter)   

