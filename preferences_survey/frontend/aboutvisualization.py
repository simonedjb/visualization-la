from dash.dependencies import Input, Output, State
import dash_html_components as html
import dash_core_components as dcc

from app import app

from frontend import frontend
from backend import backend, feedbackmessage

feedmsg = feedbackmessage.feedbackmessage()
control = backend.backend()
interface = frontend.frontend()

_page_name = "aboutvisualization"
_data_cache = []

layout = html.Div([
    interface.survey_warning("warning_"+_page_name),
    interface.survey_visualization(),
    interface.survey_send("send_"+_page_name)
])


@app.callback(
    Output('warning_'+_page_name, 'children'),
    [Input('send_'+_page_name, 'href')])
def warning_body_about_visualization(input1):
    global feedmsg    
    if feedmsg.get_clicks() > 0:
        if input1 == None:
            return feedmsg.warning_message()

    feedmsg.add_clicks()
    return ""

@app.callback(
    Output('send_'+_page_name, 'href'),
    [Input('user_cache', 'children'),
     Input('user_view_read', 'value'),
     Input('user_view_make', 'value')])
def update_body_about_visualization(input1,input2,input3):
    global _data_cache
    global _page_name

    next_page = "thanks"
    if(control.has_next_page()):
        next_page =control.get_next_page()

    _data_cache= [{"field":'user_view_read',"value":input2},
                  {"field":'user_view_make',"value":input3},
                  {"field":'page',"value":next_page}]

    if input1 == None:
        return '/'

    if input2 == '':
        return None
    else:
        return next_page