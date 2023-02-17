from django.core.management.base import BaseCommand

from tarea2.models import Proyecto


# from bs4 import BeautifulSoup


class Command(BaseCommand):
    def handle(self, *args, **options):
        Proyecto.objects.all().delete()
