from dash import dcc, html
import plotly.graph_objects as go


def create_wind_speed_graph(data):
    fig = go.Figure()
    dates = [day["date"] for day in data]
    wind_speeds = [day["wind_speed"] for day in data]

    fig.add_trace(
        go.Scatter(x=dates, y=wind_speeds, mode="lines+markers", name="Wind Speed")
    )

    fig.update_layout(
        title="Wind Speed Over Time",
        xaxis_title="Date",
        yaxis_title="Wind Speed (km/h)",
    )
    return dcc.Graph(figure=fig)
