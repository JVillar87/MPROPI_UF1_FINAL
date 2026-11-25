
import base64
from io import BytesIO

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt


def create_graph(data, column, title):

    # OBTENER PAÍSES
    countries = []

    for row in data:
        country = row["pais"]

        if country == "United Kingdom of Great Britain and Northern Ireland":
            country = "UK"

        elif country == "United States of America":
            country = "USA"

        countries.append(country)

    # OBTENER VALORES
    values = [row[column] for row in data]

    # CREAR GRÁFICO
    figure, axis = plt.subplots(figsize=(9, 5))

    if column == "llegadas_miles": 
        # Colores llegadas
        colores = [
            "#58A6FF",
            "#8B7CF6",
            "#40BFAF",
            "#D38FE8",
            "#4389BD"
        ]
    else:
        # Colores ingresos
        colores = [
            "#5EC8B8",
            "#4289B5",
            "#B49AE5",
            "#E6B66D",
            "#D87998"
        ]

    # CREAR GRÁFICO CIRCULAR
    axis.pie(
        values,
        colors=colores, 
        labels=countries,
        autopct="%1.1f%%",
        startangle=90,
            textprops={
        "color": "white",
        "fontsize": 12,
        "fontweight": "bold"
    }
    )

    axis.axis("equal")
    axis.set_title(title,
    color="white",
    fontsize=15,
    fontweight="bold",
    pad=20
    )

    # GUARDAR GRÁFICO EN MEMORIA
    image = BytesIO()
    figure.savefig(image, format="png", bbox_inches="tight", transparent=True)
    image.seek(0)
    plt.close(figure)

    # CONVERTIR IMAGEN A BASE64
    graph = base64.b64encode(image.getvalue()).decode("utf-8")

    return graph
