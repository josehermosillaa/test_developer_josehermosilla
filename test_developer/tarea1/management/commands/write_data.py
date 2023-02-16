from django.core.management.base import BaseCommand
import requests


class Command(BaseCommand):
    def handle(self, *args, **options):
        response = requests.get("http://api.citybik.es/v2/networks/bikesantiago")
        if response.status_code == 200:
            data = response.json()

        print("Hola si funciono!!!!!")
