import dash
from dash import html,dcc

app = dash.Dash(__name__)

app.layout = html.Div(
    children=[
        html.H1("Plotly Dash Example"),
        dcc.Graph(
            id="example-graph",
            figure={
                "data": [
                    {
                        "x": [1, 2, 3, 4, 5],
                        "y": [4, 1, 3, 5, 2],
                        "type": "bar",
                        "name": "Example Bar Chart",
                    }
                ],
                "layout": {
                    "title": "Bar Chart Title",
                    "xaxis": {"title": "X-axis"},
                    "yaxis": {"title": "Y-axis"},
                },
            },
        ),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
