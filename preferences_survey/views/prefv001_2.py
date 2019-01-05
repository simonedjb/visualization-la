from dash.dependencies import Input, Output, State
import dash_html_components as html
import dash_core_components as dcc

from app import app

from frontend import frontend
from backend import backend, feedbackmessage

feedmsg = feedbackmessage.feedbackmessage()
control = backend.backend()
interface = frontend.frontend()

_page_name = "prefv001_2"
_data_cache = []

layout = html.Div([
    interface.survey_warning("warning_"+_page_name),
    interface.survey_chart_preference(control.get_view_question_page_view("V001",_page_name),_page_name),
    interface.survey_send("send_"+_page_name)
])


@app.callback(
    Output('warning_'+_page_name, 'children'),
    [Input('send_'+_page_name, 'href')])
def warning_body_prefv001_2(input1):
    global feedmsg    
    if feedmsg.get_clicks() > 0:
        if input1 == None:
            return feedmsg.warning_message()

    feedmsg.add_clicks()
    return ""

@app.callback(
    Output('send_'+_page_name, 'href'),
    [Input('user_cache', 'children'),
     Input("chart_14", 'value'),
     Input("chart_16", 'value'),
     Input("chart_22", 'value'),
     Input("chart_30", 'value'),
     Input("chart_36", 'value'),
     Input("chart_37", 'value'),
     Input("chart_41", 'value'),
     Input("chart_50", 'value'),
     Input("chart_53", 'value'),
     Input("id_chart_v001_2", 'value')])
def update_body_prefv001_2(input1,chart1,chart2,chart3,chart4,chart5,chart6,chart7,chart8,chart9,select_chart):
    global _data_cache
    global _page_name

    next_page = "thanks"
    if(control.has_next_page(_page_name)):
        next_page =control.get_next_page(_page_name)

    _data_cache= [{"field":'user_V001_2',"value":[
                                                  {"id_chart_01":"14","value":chart1},
                                                  {"id_chart_02":"16","value":chart2},
                                                  {"id_chart_03":"22","value":chart3},
                                                  {"id_chart_04":"30","value":chart4},
                                                  {"id_chart_05":"36","value":chart5},
                                                  {"id_chart_06":"37","value":chart6},
                                                  {"id_chart_07":"41","value":chart7},
                                                  {"id_chart_08":"50","value":chart8},
                                                  {"id_chart_09":"53","value":chart9},
                                                  {"preference_chart":select_chart},
                                                 ]},
                  {"field":'page',"value":next_page}]

    if input1 == None:
        return '/'

    if chart1 == '':
        return None
    else:
        return next_page