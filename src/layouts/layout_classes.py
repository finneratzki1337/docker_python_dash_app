from src.graphs.graph_classes import Graphs
from src.maindash import app
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

# Just for playing around with the callback function, please remove
import random

my_graphs = Graphs()


class LayoutOne:
    def make_layout(self):
        layout = html.Div(
            [
                html.Div(
                    [
                        dcc.Graph(id="regression_plot"),
                        html.P(
                            "Standard Deviation",
                            style={"color": "white", "marginLeft": "20px"},
                        ),
                        dcc.Slider(
                            id="std_slider",
                            min=1979,
                            max=2022,
                            step=1,
                            value=1979,
                            marks={i: str(i) for i in range(1979, 2022, 2)},
                        ),
                    ]
                ),
            ]
        )
        return layout


@app.callback(
    Output(component_id="regression_plot", component_property="figure"),
    [Input(component_id="std_slider", component_property="value")],
)
def update_regression_plot(std):
    number = random.randint(0, 1)

    if number == 1:
        return my_graphs.iris(std)
    else:
        return my_graphs.windrose(std)
