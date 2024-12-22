from dash import dcc, html
import plotly.graph_objects as go


def create_precipitation_graph(data):
    fig = go.Figure()
    dates = [day["date"] for day in data]
    precipitation_probabilities = [day["precipitation_probability"] for day in data]

    fig.add_trace(
        go.Scatter(
            x=dates,
            y=precipitation_probabilities,
            mode="lines+markers",
            name="Precipitation Probability",
        )
    )

    fig.update_layout(
        title="Precipitation Probability Over Time",
        xaxis_title="Date",
        yaxis_title="Precipitation Probability (%)",
    )
    return dcc.Graph(figure=fig)
