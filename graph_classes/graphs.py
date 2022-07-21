import dash
from dash import html
from dash import dcc
import plotly.graph_objects as go
import plotly.express as px
from configparser import ConfigParser
import pandas as pd

class Graphs:
    def windrose(self, slider_number):
        
        df = px.data.wind()
        df['frequency'] = df['frequency']*slider_number
        
        fig = px.bar_polar(df, r="frequency", theta="direction",
                   color="strength", template="plotly_dark",
                   color_discrete_sequence= px.colors.sequential.Plasma_r)
        return fig