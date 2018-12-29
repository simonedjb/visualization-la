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

_page_name = "aboutyou"

layout = html.Div([
    interface.survey_warning("warning_"+_page_name),
    interface.survey_profile(),
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
    Output('aboutyou_cache', 'children'),
    [Input('user_name', 'value'),
     Input('user_gender', 'value'),
     Input('user_age', 'value'),
     Input('user_place_birth', 'value'),
     Input('user_place_work', 'value'),
     Input('user_scholarship', 'value'),
     Input('user_scholarship_degree', 'value'),
     Input('user_job', 'value'),
     Input('user_programming_xp', 'value')])
def record_about_you(input1,input2,input3,input4,input5,input6,input7,input8,input9):
    
    inputs = [{'user_name':input1},
              {'user_gender':input2},
              {'user_age':input3},
              {'user_place_birth':input4},
              {'user_place_work':input5},
              {'user_scholarship':input6},
              {'user_scholarship_degree':input7},
              {'user_job':input8},
              {'user_programming_xp':input9},
              {'page':_page_name}
              ]
    
    return json.dumps(inputs)

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
     Input('user_programming_xp', 'value')])
def update_body_about_you(input1,input2,input3,input4,input5,input6,input7,input8,input9,input10):
    if input1 == None:
        return '/'

    if input2 == '':
        return None
    else:
        return 'abouteadxp'
    