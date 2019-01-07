from dash.dependencies import Input, Output, State
import dash_html_components as html
import dash_core_components as dcc

from app import app

from frontend import frontend
from backend import backend, feedbackmessage

feedmsg = feedbackmessage.feedbackmessage()
control = backend.backend()
interface = frontend.frontend()

_page_name = "aboutyou"
_data_cache = []

def layout(data_cache=[]):
    global interface
    global _page_name
    return html.Div([
                interface.survey_warning("warning_"+_page_name),
                interface.survey_profile(data_cache),
                interface.survey_send("send_"+_page_name)
            ])

@app.callback(
    Output('warning_'+_page_name, 'children'),
    [Input('send_'+_page_name, 'href')])
def warning_body_about_you(input1):
    global feedmsg
    if feedmsg.get_clicks() > 0:
        if input1 == None:
            return feedmsg.warning_message()

    feedmsg.add_clicks()
    return ""

@app.callback(
    Output('send_'+_page_name, 'href'),
    [Input('user_cache', 'children'),
     Input('user_name', 'value'),
     Input('user_gender', 'value'),
     Input('user_age', 'value'),
     Input('user_place_birth', 'value'),
     Input('user_place_work', 'value'),
     Input('user_scholarship', 'value'),
     Input('user_scholarship_degree', 'value'),
     Input('user_job', 'value'),
     Input('user_programming_xp', 'value'),
     Input('user_programming_last_time', 'value'),
     Input('user_programming_language', 'value')])
def update_body_about_you(input1,input2,input3,input4,input5,input6,input7,input8,input9,input10,input11,input12):
    global _data_cache
    global _page_name

    next_page = 'abouteadxp' 

    _data_cache= [{"field":'user_name',"value":input2},
                  {"field":'user_gender',"value":input3},
                  {"field":'user_age',"value":input4},
                  {"field":'user_place_birth',"value":input5},
                  {"field":'user_place_work',"value":input6},
                  {"field":'user_scholarship',"value":input7},
                  {"field":'user_scholarship_degree',"value":input8},
                  {"field":'user_job',"value":input9},
                  {"field":'user_programming_xp',"value":input10},
                  {"field":'user_programming_last_time',"value":input11},
                  {"field":'user_programming_language',"value":input12},
                  {"field":'page',"value":next_page}]

    if input1 == None:
        return '/'

    if input2 == '' or input3 == '' or input4 == '' or input5 == '' or input6 == '' or input7 == '' or input8 == '' or input9 == '' or input10 == '':
        return None
    else:
        return next_page