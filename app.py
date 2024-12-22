from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
from accuweather import get_location_key, get_weather_data

app = Dash(__name__)

app.layout = html.Div(
    children=[
        dcc.Dropdown(
            id="city-dropdown",
            options=[
                {"label": "Москва", "value": "Moscow"},
                {"label": "Лондон", "value": "London"},
                {"label": "Нью-Йорк", "value": "New York"},
            ],
            value="Москва",
        ),
        dcc.Graph(id="weather-graph"),
    ]
)


@app.callback(Output("weather-graph", "figure"), [Input("city-dropdown", "value")])
def update_graph(selected_city):
    location_key = get_location_key(selected_city)
    current_conditions, forecast = get_weather_data(location_key)

    # Обработка данных для графика
    temperatures = [
        day["Temperature"]["Maximum"]["Value"] for day in forecast["DailyForecasts"]
    ]
    dates = [day["Date"][:10] for day in forecast["DailyForecasts"]]

    figure = {
        "data": [
            go.Scatter(
                x=dates,
                y=temperatures,
                mode="lines+markers",
                name="Максимальная температура",
            )
        ],
        "layout": go.Layout(title=f"Прогноз погоды в {selected_city}"),
    }
    return figure


if __name__ == "__main__":
    app.run_server(debug=True)
