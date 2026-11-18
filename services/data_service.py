
import csv
from pathlib import Path


def load_data():

    ruta = Path(__file__).resolve().parent.parent / "data" / "turismo_limpio.csv"

    datos = []

    with open(ruta, encoding="utf-8-sig", newline="") as archivo:
        lector = csv.DictReader(archivo)

        for fila in lector:

            #COMPROBAR CAMPOS CON DATOS (SIN VACÍOS)
            if (fila["pais"].strip() != "" and
                fila["anio"].strip() != "" and
                fila["llegadas_miles"].strip() != "" and
                fila["ingresos_millones_usd"].strip() != ""):

                #CONVERTIR A INT/FLOAT
                try:
                    fila["anio"] = int(fila["anio"])
                    fila["llegadas_miles"] = float(fila["llegadas_miles"])
                    fila["ingresos_millones_usd"] = float(fila["ingresos_millones_usd"])

                    datos.append(fila)

                except ValueError:
                    continue

    return datos


def get_top_10(datos, anio, columna):

    #FILTRAR POR AÑO
    filtrados = []

    for fila in datos:
        if fila["anio"] == anio:
            filtrados.append(fila)

    #ORDENAR DE MAYOR A MENOR
    filtrados.sort(
        key=lambda fila: fila[columna],
        reverse=True
    )

    #DEVOLVER LOS 10 PRIMEROS
    return filtrados[:10]


def get_years(datos):

    #OBTENER LOS AÑOS DISPONIBLES
    anios = []

    for fila in datos:
        if fila["anio"] not in anios:
            anios.append(fila["anio"])

    # ORDENAR DEL MÁS RECIENTE AL MÁS ANTIGUO
    anios.sort(reverse=True)

    return anios
