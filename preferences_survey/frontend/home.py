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
_user_cache = None
_data_cache = [] 

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
    global _user_cache
    global _data_cache
    if input1 == '':
        return None
    
    next_page = "eadxp"
    _user_cache = input1
    _data_cache= [{"field":"date_start_cache","value":datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")},
                  {"field":'page',"value":next_page}]

    if control.db_has_database(input1):
        control.db_load_database(_user_cache)
        return control.db_select_value(["page"])[0]
    
    return next_page

def record_data_home(user = None):
    global control
    global _data_cache

    if user == None:
        return False
    
    fields = []
    values = []

    for i in range(0,len(_data_cache)):
        fields.append(_data_cache[i]["field"])
        values.append(_data_cache[i]["value"])

    if not control.db_has_database(user):
        control.db_make_database(user)
        control.db_adding_value(fields,values)

    return True