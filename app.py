
from flask import Flask, render_template, request
from services.data_service import load_data, get_top_10, get_years

app = Flask(__name__)


@app.route('/')
def dashboard():

    # CARGAR LOS DATOS DEL CSV
    datos = load_data()

    # OBTENER LOS AÑOS DISPONIBLES
    anios = get_years(datos)

    # OBTENER EL AÑO SELECCIONADO (2024 POR DEFECTO)
    anio = request.args.get("anio", default=2024, type=int)

    # COMPROBAR QUE EL AÑO EXISTE
    if anio not in anios:
        anio = anios[0]

    # TOP 10 LLEGADAS TURÍSTICAS
    top_llegadas = get_top_10(datos, anio, "llegadas_miles")

    # TOP 10 INGRESOS TURÍSTICOS
    top_ingresos = get_top_10(datos, anio, "ingresos_millones_usd")

    # ENVIAR LOS DATOS AL HTML
    return render_template(
        "dashboard.html",
        top_llegadas=top_llegadas,
        top_ingresos=top_ingresos,
        anios=anios,
        anio=anio
    )


if __name__ == "__main__":
    app.run(debug=True)
