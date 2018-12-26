from dash.dependencies import Input, Output, State
import dash_html_components as html
import dash_core_components as dcc

from app import app

from frontend import frontend

interface = frontend.frontend()

_page_name = "home"

layout = html.Div([
    interface.survey_presentation(),
    interface.survey_send("send_"+_page_name,"eadxp")
])