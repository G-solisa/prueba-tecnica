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
            
        for instance in j_data:
            Farmacia.objects.get_or_create(instance)
        
