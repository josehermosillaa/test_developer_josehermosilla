import requests
from django.core.management.base import BaseCommand
from tarea1.models import Network, Station


class Command(BaseCommand):
    def handle(self, *args, **options):
        response = requests.get("http://api.citybik.es/v2/networks/bikesantiago")
        if response.status_code == 200:
            data = response.json()

            Network.objects.update_or_create(
                name=data["network"]["name"],
                company=data["network"]["company"],
                identification=data["network"]["id"],
                href=data["network"]["href"],
                city=data["network"]["location"]["city"],
                country=data["network"]["location"]["country"],
                latitude=data["network"]["location"]["latitude"],
                longitude=data["network"]["location"]["longitude"],
            )

            for station_data in data["network"]["stations"]:
                Station.objects.update_or_create(
                    name=station_data["name"],
                    identification=station_data["id"],
                    latitude=station_data["latitude"],
                    longitude=station_data["longitude"],
                    free_bikes=station_data["free_bikes"],
                    empty_slots=station_data["empty_slots"],
                    address=station_data["extra"]["address"],
                    ebikes=station_data["extra"]["ebikes"],
                    has_ebikes=station_data["extra"]["has_ebikes"],
                    normal_bikes=station_data["extra"]["normal_bikes"],
                    payment=station_data["extra"]["payment"],
                    payment_terminal=station_data["extra"]["payment-terminal"],
                    post_code=" "
                    if not "post_code" in station_data["extra"]
                    else station_data["extra"]["post_code"],
                    renting=station_data["extra"]["renting"],
                    returning=station_data["extra"]["returning"],
                    slots=station_data["extra"]["slots"],
                    uid=station_data["extra"]["uid"],
                    date=station_data["timestamp"],
                )

        print("Hola si funciono!!!!!")

        self.stdout.write(
            self.style.SUCCESS("Se han cargado los datos correctamente!!!!")
        )
