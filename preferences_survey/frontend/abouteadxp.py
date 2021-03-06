from dash.dependencies import Input, Output, State
import dash_html_components as html
import dash_core_components as dcc

from app import app

from frontend import frontend
from backend import backend, feedbackmessage

feedmsg = feedbackmessage.feedbackmessage()
control = backend.backend()
interface = frontend.frontend()

_page_name = "abouteadxp"
_data_cache = []

def layout(data_cache=[]):
    global interface
    global _page_name
    return html.Div([
                interface.survey_warning("warning_"+_page_name),
                interface.survey_ead_xp(data_cache),
                interface.survey_send("send_"+_page_name)
            ])

@app.callback(
    Output('warning_'+_page_name, 'children'),
    [Input('send_'+_page_name, 'href')])
def warning_body_about_ead_xp(input1):
    global feedmsg    
    if feedmsg.get_clicks() > 0:
        if input1 == None:
            return feedmsg.warning_message()

    feedmsg.add_clicks()
    return ""

@app.callback(
    Output('send_'+_page_name, 'href'),
    [Input('user_cache', 'children'),
     Input('user_job_ead', 'value'),
     Input('user_time_experience', 'value'),
     Input('user_organization_worked', 'value'),
     Input('user_subject', 'value'),
     Input('user_ead_modality', 'value'),
     Input('user_avas_performed', 'value'),
     Input('user_avas_resources', 'value'),
     Input('user_students_age', 'value'),
     Input('user_students_scholarship', 'value'),
     Input('user_students_scholarship_degree', 'value'),
     Input('user_students_meaningful', 'value')])
def update_body_about_ead_xp(input1,input2,input3,input4,input5,input6,input7,input8,input9,input10,input11,input12):
    global _data_cache
    global _page_name

    next_page = 'aboutlogs' 

    _data_cache= [{"field":'user_job_ead',"value":input2},
                  {"field":'user_time_experience',"value":input3},
                  {"field":'user_organization_worked',"value":input4},
                  {"field":'user_subject',"value":input5},
                  {"field":'user_ead_modality',"value":input6},
                  {"field":'user_avas_performed',"value":input7},
                  {"field":'user_avas_resources',"value":input8},
                  {"field":'user_students_age',"value":input9},
                  {"field":'user_students_scholarship',"value":input10},
                  {"field":'user_students_scholarship_degree',"value":input11},
                  {"field":'user_students_meaningful',"value":input12},
                  {"field":'page',"value":next_page}]

    if input1 == None:
        return '/'

    if input2 == '' or input3 == '' or input4 == '' or input5 == '' or input6 == '' or input7 == '' or input8 == '' or input9 == '' or input10 == '' or input11 == '' or input12 == '':
        return None
    else:
        return next_page