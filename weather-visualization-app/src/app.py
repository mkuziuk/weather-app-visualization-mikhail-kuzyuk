from dash import Dash, dcc, html, Input, Output, State
import os
import dash_bootstrap_components as dbc
import dash_leaflet as dl
from components.temperature_graph import create_temperature_graph
from components.wind_speed_graph import create_wind_speed_graph
from components.precipitation_graph import create_precipitation_graph
from data.weather_data import get_weather_data

api_key = os.getenv("hNLslNHqYdLIxpOm36dyy1143FnopGCi")

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div(
    [
        dbc.Container(
            [
                html.H1("Weather Data Visualization"),
                dcc.Dropdown(
                    id="time-interval-dropdown",
                    options=[
                        {"label": "1 Day", "value": 1},
                        {"label": "3 Days", "value": 3},
                        {"label": "5 Days", "value": 5},
                    ],
                    value=1,
                    clearable=False,
                ),
                html.Div(
                    id="route-points-container",
                    children=[
                        dcc.Input(
                            id="start-point", type="text", placeholder="Start Point"
                        ),
                        dcc.Input(id="end-point", type="text", placeholder="End Point"),
                        html.Button("Add Stop", id="add-stop-button", n_clicks=0),
                        html.Div(id="stops-container"),
                    ],
                ),
                html.Button("Get Weather", id="get-weather-button", n_clicks=0),
                html.Div(id="graphs-container"),
                dl.Map(
                    id="map",
                    center=[56.1304, -106.3468],
                    zoom=4,
                    children=[
                        dl.TileLayer(),
                        dl.LayerGroup(id="layer"),
                    ],
                    style={"width": "100%", "height": "500px"},
                ),
            ]
        )
    ]
)


@app.callback(
    Output("stops-container", "children"),
    Input("add-stop-button", "n_clicks"),
    State("stops-container", "children"),
)
def add_stop(n_clicks, children):
    if children is None:
        children = []
    new_stop = dcc.Input(type="text", placeholder=f"Stop {n_clicks}")
    children.append(new_stop)
    return children


@app.callback(
    Output("graphs-container", "children"),
    Output("layer", "children"),
    Input("get-weather-button", "n_clicks"),
    State("start-point", "value"),
    State("end-point", "value"),
    State("stops-container", "children"),
    State("time-interval-dropdown", "value"),
)
def update_graphs_and_map(n_clicks, start_point, end_point, stops, selected_interval):
    if n_clicks == 0:
        return [], []

    locations = [start_point]
    if stops:
        for stop in stops:
            if isinstance(stop, dict) and "props" in stop and "value" in stop["props"]:
                locations.append(stop["props"]["value"])
    locations.append(end_point)

    all_weather_data = []
    markers = []
    for location in locations:
        try:
            weather_data = get_weather_data(api_key, location, selected_interval)
            all_weather_data.append(weather_data)
            markers.append(
                dl.Marker(
                    position=[weather_data["lat"], weather_data["lon"]],
                    children=[
                        dl.Tooltip(location),
                        dl.Popup(f"Weather: {weather_data['weather']}"),
                    ],
                )
            )
        except Exception as e:
            return [html.Div(f"Error fetching data for {location}: {str(e)}")], []

    graphs = []
    for i, weather_data in enumerate(all_weather_data):
        temperature_graph = create_temperature_graph(weather_data)
        wind_speed_graph = create_wind_speed_graph(weather_data)
        precipitation_graph = create_precipitation_graph(weather_data)

        graphs.append(
            html.Div(
                [
                    html.Div(f"Location {i+1}: {locations[i]}"),
                    dcc.Graph(figure=temperature_graph),
                    dcc.Graph(figure=wind_speed_graph),
                    dcc.Graph(figure=precipitation_graph),
                ]
            )
        )

    return graphs, markers


if __name__ == "__main__":
    app.run_server(debug=True)
