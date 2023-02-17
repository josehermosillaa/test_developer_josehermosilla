import json
import datetime
from django.core.management.base import BaseCommand
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tarea2.models import Proyecto


class Command(BaseCommand):
    def handle(self, *args, **options):
        data = []
        url = "https://seia.sea.gob.cl/busqueda/buscarProyectoAction.php"
        # selenium
        driver = webdriver.Chrome()
        driver.get(url)
        pagination = driver.find_elements(By.NAME, "pagina_offset")
        last_page = int(pagination[0].text.split()[-1])
        for i in range(1, last_page + 1):
            WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable(
                    (
                        By.XPATH,
                        f"/html/body/div[1]/div[1]/div/div[3]/div[4]/div/select/option[{i}]",
                    )
                )
            ).click()
            table = driver.find_element(By.CLASS_NAME, "tabla_datos")
            rows = table.find_elements(
                By.XPATH, '//*[@id="main"]/div[3]/div[4]/div/table/tbody'
            )
            for row in rows[0].find_elements(By.TAG_NAME, "tr"):
                columns = row.find_elements(By.TAG_NAME, "td")

                def change(str1):
                    str1 = str1.replace(".", "x")
                    str1 = str1.replace(",", ".")
                    str1 = str1.replace("x", "")
                    return str1

                decimal = change(columns[6].text)
                print(decimal)
                print(columns[0].text)
                dato = {
                    "id_proyecto": int(columns[0].text),
                    "nombre_proyecto": columns[1].text,
                    "tipo_proyecto": columns[2].text,
                    "region": columns[3].text,
                    "tipologia": columns[4].text,
                    "titular": columns[5].text,
                    "inversion": float(decimal),
                    "fecha_ingreso": datetime.datetime.strptime(
                        columns[7].text, "%d/%m/%Y"
                    ).strftime("%Y-%m-%d"),
                    "estado": columns[8].text,
                }
                Proyecto.objects.update_or_create(
                    id_proyecto=dato["id_proyecto"],
                    nombre_proyecto=dato["nombre_proyecto"],
                    tipo_proyecto=dato["tipo_proyecto"],
                    region=dato["region"],
                    tipologia=dato["tipologia"],
                    titular=dato["titular"],
                    inversion=dato["inversion"],
                    fecha_ingreso=dato["fecha_ingreso"],
                    estado=dato["estado"],
                )
                data.append(dato)
        # # Guardar la información en un archivo JSON
        with open("informacion_proyectos.json", "w") as file:
            json.dump(data, file, ensure_ascii=False)

        self.stdout.write(
            self.style.SUCCESS(
                "Se han cargado los datos de Bikesantiago, correctamente"
            )
        )
