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

_page_name = "aboutlogs"

layout = html.Div([
    interface.survey_warning("warning_"+_page_name),
    interface.survey_logs(),
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
    Output('aboutlogs_cache', 'children'),
    [Input('user_students_progress', 'value'),
     Input('user_logs_presentation', 'value'),
     Input('user_logs_analyse', 'value'),
     Input('user_logs_performance', 'value'),
     Input('user_logs_dropout', 'value'),
     Input('user_logs_engagement', 'value')])
def record_about_logs(input1,input2,input3,input4,input5,input6):
    
    inputs = [{'user_students_progress':input1},
              {'user_logs_presentation':input2},
              {'user_logs_analyse':input3},
              {'user_logs_performance':input4},
              {'user_logs_dropout':input5},
              {'user_logs_engagement':input6},
              {'page':_page_name}
              ]
    
    return json.dumps(inputs)

@app.callback(
    Output('send_'+_page_name, 'href'),
    [Input('user_cache', 'children'),
     Input('user_students_progress', 'value'),
     Input('user_logs_presentation', 'value'),
     Input('user_logs_analyse', 'value'),
     Input('user_logs_performance', 'value'),
     Input('user_logs_dropout', 'value'),
     Input('user_logs_engagement', 'value')])
def update_body_about_logs(input1,input2,input3,input4,input5,input6,input7):
    if input1 == None:
        return '/'

    if input2 == '':
        return None
    else:
        return "aboutstudentinformation"