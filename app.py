
from flask import Flask, render_template, request
from services.data_service import load_data, get_data_by_year, get_years
from services.graphic_services import create_graph

app = Flask(__name__)


@app.route('/')
def dashboard():

    # CARGAR DATOS Y AÑOS DISPONIBLES
    data = load_data()
    years = get_years(data)

    # AÑOS QUE QUEREMOS COMPARAR
    year_1 = request.args.get("year_1", default=2020, type=int)
    year_2 = request.args.get("year_2", default=2024, type=int)

    # COMPROBAR QUE LOS AÑOS EXISTEN
    if year_1 not in years:
        year_1 = years[1] if len(years) > 1 else years[0]

    if year_2 not in years:
        year_2 = years[0]

    # ORDEN DE LOS RESULTADOS
    orden = request.args.get("orden", default="desc")

    # RANKINGS DE LLEGADAS TURÍSTICAS
    arrivals_1 = get_data_by_year(data, year_1, "llegadas_miles", orden, 5)
    arrivals_2 = get_data_by_year(data, year_2, "llegadas_miles", orden, 5)

    # RANKINGS DE INGRESOS TURÍSTICOS
    ingresos_1 = get_data_by_year(data, year_1, "ingresos_millones_usd", orden, 5)
    ingresos_2 = get_data_by_year(data, year_2, "ingresos_millones_usd", orden, 5)
    

    # GRÁFICO DE LLEGADAS TURÍSTICAS - PRIMER AÑO
    graph_arrivals_1 = create_graph(
        arrivals_1,
        "llegadas_miles",
        f"TOP 5 Llegadas turísticas - {year_1}"
    )

    # GRÁFICO DE LLEGADAS TURÍSTICAS - SEGUNDO AÑO
    graph_arrivals_2 = create_graph(
        arrivals_2,
        "llegadas_miles",
        f"TOP 5 Llegadas turísticas - {year_2}"
    )

    # GRÁFICO DE INGRESOS TURÍSTICOS - PRIMER AÑO
    graph_ingresos_1 = create_graph(
        ingresos_1,
        "ingresos_millones_usd",
        f"TOP 5 Ingresos turísticos - {year_1}"
    )

    # GRÁFICO DE INGRESOS TURÍSTICOS - SEGUNDO AÑO
    graph_ingresos_2 = create_graph(
        ingresos_2,
        "ingresos_millones_usd",
        f"TOP 5 Ingresos turísticos - {year_2}"
    )
    

    return render_template(
        "dashboard.html",
        years=years,
        year_1=year_1,
        year_2=year_2,
        orden=orden,
        arrivals_1=arrivals_1,
        arrivals_2=arrivals_2,
        graph_arrivals_1=graph_arrivals_1,
        graph_arrivals_2=graph_arrivals_2,
        ingresos_1=ingresos_1,
        ingresos_2=ingresos_2,
        graph_ingresos_1=graph_ingresos_1,
        graph_ingresos_2=graph_ingresos_2
    )


if __name__ == "__main__":
    app.run(debug=True)
