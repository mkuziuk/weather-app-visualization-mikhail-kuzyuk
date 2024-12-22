from dash import dcc, html
import plotly.graph_objects as go


def create_temperature_graph(data):
    fig = go.Figure()
    dates = [day["date"] for day in data]
    temperatures_min = [day["temperature_min"] for day in data]
    temperatures_max = [day["temperature_max"] for day in data]

    fig.add_trace(
        go.Scatter(
            x=dates, y=temperatures_min, mode="lines+markers", name="Min Temperature"
        )
    )
    fig.add_trace(
        go.Scatter(
            x=dates, y=temperatures_max, mode="lines+markers", name="Max Temperature"
        )
    )

    fig.update_layout(
        title="Temperature Over Time",
        xaxis_title="Date",
        yaxis_title="Temperature (°C)",
    )
    return fig
