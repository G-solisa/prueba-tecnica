from django.core.management.base import BaseCommand
from farmacias.models import Farmacia
import requests
from django.core.mail import send_mail

url = 'https://farmanet.minsal.cl/maps/index.php/ws/getLocalesTurnos'


class Command(BaseCommand):
    
    def add_arguments(self, parser):
        parser.add_argument('email')

    def handle(self, *args, **options):
        email = options['email']

        response = requests.get(url)

        if response.status_code == 200:
            j_data = response.json() #list of dics ??
            # clean_j_data = {json.loads(j_data[0])}
            for x in j_data:
                Farmacia.objects.update_or_create(**x)

        clean_filter = []
        result = Farmacia.objects.values_list('local_nombre', flat=True)
        for x in result:
            if x not in clean_filter:
                clean_filter.append(x)
        total = 0
        message = []
        for pharma_names in clean_filter:
            a = Farmacia.objects.filter(local_nombre=pharma_names).count()
            total += a
            message.append(f'{pharma_names}=>{a}')
            print(f'{pharma_names}=>{a}')

        print(f'TOTAL FARMACIAS DE TURNO {total}')

        send_mail(
            'Farmacias de turno',
            f'{[x for x in message]}',
            'gsolis275@gmail.com',
            [email],
            fail_silently=False,
        )