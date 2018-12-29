import json, datetime

from dash.dependencies import Input, Output, State
import dash_html_components as html
import dash_core_components as dcc

from app import app

from frontend import frontend
from backend import backend, feedbackmessage

feedmsg = feedbackmessage.feedbackmessage()
control = backend.backend()
interface = frontend.frontend()

_page_name = "eadxp"

layout = html.Div([
    interface.survey_warning("warning_"+_page_name),
    interface.survey_filter(),
    interface.survey_send("send_"+_page_name)
])


@app.callback(
    Output('warning_'+_page_name, 'children'),
    [Input('send_'+_page_name, 'href')])
def warning_body_ead_xp(input1):
    global feedmsg
    if feedmsg.get_clicks() > 0:
        if input1 == None:
            return feedmsg.warning_message()

    feedmsg.add_clicks()
    return ""

@app.callback(
    Output('date_start_cache', 'children'),
    [Input('user_ead_xp', 'value'),
     Input('user_cache', 'children')])
def update_body_date_cache(input1,input2):
    global control
    global _page_name 
    if input1 == "":
        return None
    
    user_cache = json.loads(input2)
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if not control.db_has_database(user_cache):
        control.db_make_database(user_cache)
        control.db_adding_value(["user_ead_xp","date_start_cache","page"],[input1,date,_page_name])

    return json.dumps(date)

@app.callback(
    Output('send_'+_page_name, 'href'),
    [Input('user_ead_xp', 'value')])
def update_body_ead_xp(input1):
    if input1 == "S":
        return "aboutyou"
    elif input1 == "N":
        return "thanks"