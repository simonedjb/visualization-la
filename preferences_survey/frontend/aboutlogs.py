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
_data_cache = []

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

# @app.callback(
#     Output('aboutlogs_cache', 'children'),
#     [Input('user_students_progress', 'value'),
#      Input('user_logs_presentation', 'value'),
#      Input('user_logs_analyse', 'value'),
#      Input('user_logs_performance', 'value'),
#      Input('user_logs_dropout', 'value'),
#      Input('user_logs_engagement', 'value')])
# def record_about_logs(input1,input2,input3,input4,input5,input6):
    
#     inputs = [{'user_students_progress':input1},
#               {'user_logs_presentation':input2},
#               {'user_logs_analyse':input3},
#               {'user_logs_performance':input4},
#               {'user_logs_dropout':input5},
#               {'user_logs_engagement':input6},
#               {'page':_page_name}
#               ]
    
#     return json.dumps(inputs)

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
    global _data_cache
    global _page_name

    next_page = "aboutstudentinformation"

    _data_cache= [{"field":'user_students_progress',"value":input2},
                  {"field":'user_logs_presentation',"value":input3},
                  {"field":'user_logs_analyse',"value":input4},
                  {"field":'user_logs_performance',"value":input5},
                  {"field":'user_logs_dropout',"value":input6},
                  {"field":'user_logs_engagement',"value":input7},
                  {"field":'page',"value":next_page}]

    if input1 == None:
        return '/'

    if input2 == '':
        return None
    else:
        return next_page

def record_data_about_logs(user = None):
    global control
    global _data_cache

    if user == None:
        return False
    
    fields = []
    values = []

    for i in range(0,len(_data_cache)):
        fields.append(_data_cache[i]["field"])
        values.append(_data_cache[i]["value"])

    control.db_adding_value(fields,values)

    return True