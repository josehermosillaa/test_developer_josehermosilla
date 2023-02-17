import json
from django.core.management.base import BaseCommand
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# from bs4 import BeautifulSoup


class Command(BaseCommand):
    def handle(self, *args, **options):
        data = []
        # ignored_exceptions = (
        #     NoSuchElementException,
        #     StaleElementReferenceException,
        # )
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

            # //*[@id="main"]/div[3]/div[4]/div/table/tbody/tr[1]
            # //*[@id="main"]/div[3]/div[4]/div/table/tbody/tr[2]
            for row in rows[0].find_elements(By.TAG_NAME, "tr"):
                columns = row.find_elements(By.TAG_NAME, "td")
                print(columns[0].text)
                dato = {
                    "id_proyecto": int(columns[0].text),
                    "nombre_proyecto": columns[1].text,
                    "tipo_proyecto": columns[2].text,
                    "region": columns[3].text,
                    "tipologia": columns[4].text,
                    "titular": columns[5].text,
                    "inversion": float(columns[6].text.replace(",", ".")),
                    "fecha_ingreso": columns[7].text,
                    "estado": columns[8].text,
                }
            data.append(dato)
        # # Guardar la información en un archivo JSON
        with open("informacion_proyectos.json", "w") as file:
            json.dump(data, file, ensure_ascii=False)

        self.stdout.write(
            self.style.SUCCESS(
                "Se han cargado los datos de Bikesantiago, correctamente"
            )
        )
