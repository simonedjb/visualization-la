from dash.dependencies import Input, Output, State
import dash_html_components as html
import dash_core_components as dcc

from app import app

from frontend import frontend

interface = frontend.frontend()

_n_clicks = 0

_page_name = "thanks"

layout = html.Div([
    interface.survey_end()
])