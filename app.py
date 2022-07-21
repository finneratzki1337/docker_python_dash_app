from configparser import ConfigParser
import os
from dotenv import load_dotenv


import dash
import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

#importing own modules
from module_template import module_class
from graph_classes.graphs import Graphs

#MY_ENV_VAR = os.getenv('MY_ENV_VAR')

#reading potential config
config = ConfigParser()
config.read("config/conf.conf")

if 'AM_I_IN_A_DOCKER_CONTAINER' not in os.environ:
    load_dotenv()
    
user_name = os.environ['USER_NAME']
password = os.environ['USER_PASSWORD']
my_setting = config['GENERAL']['MY_SETTING']

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

app.layout = html.Div(
    [
        html.Div(
            [
                dcc.Graph(id="regression_plot"),
                html.P(
                    "Standard Deviation", style={"color": "white", "marginLeft": "20px"}
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

@app.callback(
    Output(component_id="regression_plot", component_property="figure"),
    [Input(component_id="std_slider", component_property="value")],
)
def update_regression_plot(std):
    return my_graphs.windrose(std)

my_graphs = Graphs()
if __name__ == "__main__":
    app.run_server(host="0.0.0.0", port=8050, debug=True)