from dash.dependencies import Input, Output, State
import dash_html_components as html
import dash_core_components as dcc

from app import app

from frontend import frontend
from backend import feedbackmessage

feedmsg = feedbackmessage.feedbackmessage()

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
    Output('send_'+_page_name, 'href'),
    [Input('user_ead_xp', 'value')])
def update_body_ead_xp(input1):
    if input1 == "S":
        return "aboutyou"
    elif input1 == "N":
        return "thanks"