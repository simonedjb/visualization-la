from dash.dependencies import Input, Output, State
import dash_html_components as html
import dash_core_components as dcc

from app import app

from frontend import frontend
from backend import backend, feedbackmessage

control = backend.backend()
feedmsg = feedbackmessage.feedbackmessage()
interface = frontend.frontend()

_view = "V007"
_page_name = control.get_view_page(_view)

layout = html.Div([
    interface.survey_warning("warning_"+_page_name),
    interface.survey_chart_preference(control.get_view_label(_view)),
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
#     Output('send_'+_page_name, 'href'),
#     [Input('user_interaction_access_students_logs', 'value'),
#      Input('user_interaction_access_students_logs_others', 'value')])
# def update_body_about_student_information(input1,input2):
#     global control
#     if input1 == '':
#         return None
#     else:
#         return "aboutvisualization"