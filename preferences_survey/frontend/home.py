import json, datetime

from dash.dependencies import Input, Output, State
import dash_html_components as html
import dash_core_components as dcc

from app import app

from frontend import frontend
from backend import backend

control = backend.backend()
interface = frontend.frontend()

_page_name = "presentation"

layout = html.Div([
    interface.survey_presentation(),
    interface.survey_send("send_"+_page_name)
])

@app.callback(
    Output('user_cache', 'children'),
    [Input('user_email', 'value')])
def update_body_user_cache(input1):
    if input1 == '':
        return None

    return json.dumps(input1)

@app.callback(
    Output('send_'+_page_name, 'href'),
    [Input('user_email', 'value')])
def update_body_presentation(input1):
    global control
    if input1 == '':
        return None
    
    if control.db_has_database(input1):
        return control.db_select_value("page")
    
    return "eadxp"