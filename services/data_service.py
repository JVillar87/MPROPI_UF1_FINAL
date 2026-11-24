
import csv
from pathlib import Path


def load_data():

    # CARGA Y LIMPIEZA DE DATOS
    ruta = Path(__file__).resolve().parent.parent / "data" / "turismo_limpio.csv"

    datos = []

    with open(ruta, encoding="utf-8-sig", newline="") as archivo:
        lector = csv.DictReader(archivo)

        for fila in lector:

            # COMPROBAR PAÍS Y AÑO
            if fila["pais"].strip() != "" and fila["anio"].strip() != "":

                try:
                    # CONVERTIR EL AÑO A ENTERO
                    fila["anio"] = int(fila["anio"])

                    # CONVERTIR LOS INDICADORES SI TIENEN DATOS
                    if fila["llegadas_miles"].strip() != "":
                        fila["llegadas_miles"] = float(fila["llegadas_miles"])
                    else:
                        fila["llegadas_miles"] = None

                    if fila["ingresos_millones_usd"].strip() != "":
                        fila["ingresos_millones_usd"] = float(fila["ingresos_millones_usd"])
                    else:
                        fila["ingresos_millones_usd"] = None

                    datos.append(fila)

                except ValueError:
                    continue

    return datos

 
def get_data_by_year(datos, anio, columna, orden, limite):
    # FILTRAR POR AÑO
    filtrados = []

    for fila in datos:
        if fila["anio"] == anio and fila[columna] is not None:
            filtrados.append(fila)

    # ORDENAR LOS RESULTADOS
    filtrados.sort(
        key=lambda fila: fila[columna],
        reverse=(orden == "desc")
    )

    # DEVOLVER LA CANTIDAD SOLICITADA
    return filtrados[:limite]


def get_years(datos):

    #OBTENER LOS AÑOS DISPONIBLES
    anios = []

    for fila in datos:
        if fila["anio"] not in anios:
            anios.append(fila["anio"])

    # ORDENAR DEL MÁS RECIENTE AL MÁS ANTIGUO
    anios.sort(reverse=True)

    return anios
