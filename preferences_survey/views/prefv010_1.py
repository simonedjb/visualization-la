from dash.dependencies import Input, Output, State
import dash_html_components as html
import dash_core_components as dcc

from app import app

from frontend import frontend
from backend import backend, feedbackmessage

feedmsg = feedbackmessage.feedbackmessage()
control = backend.backend()
interface = frontend.frontend()

_page_name = "prefv010_1"
_data_cache = []

def layout(data_cache=[]):
    global interface
    global _page_name
    return html.Div([
                interface.survey_warning("warning_"+_page_name),
                interface.survey_chart_preference(control.get_view_question_page_view("V010",_page_name),_page_name,data_cache),
                interface.survey_send("send_"+_page_name)
            ])

@app.callback(
    Output('warning_'+_page_name, 'children'),
    [Input('send_'+_page_name, 'href')])
def warning_body_prefv010_1(input1):
    global feedmsg    
    if feedmsg.get_clicks() > 0:
        if input1 == None:
            return feedmsg.warning_message()

    feedmsg.add_clicks()
    return ""

@app.callback(
    Output('send_'+_page_name, 'href'),
    [Input('user_cache', 'children'),
     Input("chart_01", 'value'),
     Input("chart_02", 'value'),
     Input("chart_03", 'value'),
     Input("chart_07", 'value'),
     Input("chart_11", 'value'),
     Input("chart_15", 'value'),
     Input("chart_18", 'value'),
     Input("chart_19", 'value'),
     Input("chart_22", 'value'),
     Input("chart_23", 'value'),
     Input("chart_24", 'value'),
     Input("chart_27", 'value'),
     Input("chart_30", 'value'),
     Input("id_chart_v010_1", 'value'),
     Input("comments_id_chart_v010_10",'value')])
def update_body_prefv010_1(input1,chart1,chart2,chart3,chart4,chart5,chart6,chart7,chart8,chart9,chart10,chart11,chart12,chart13,select_chart,comments):
    global _data_cache
    global _page_name

    next_page = "thanks"
    if(control.has_next_page(_page_name)):
        next_page =control.get_next_page(_page_name)

    _data_cache= [{"field":'user_V010_10',"value":[
                                                  {"field":"chart_01","value":chart1},
                                                  {"field":"chart_02","value":chart2},
                                                  {"field":"chart_03","value":chart3},
                                                  {"field":"chart_07","value":chart4},
                                                  {"field":"chart_11","value":chart5},
                                                  {"field":"chart_15","value":chart6},
                                                  {"field":"chart_18","value":chart7},
                                                  {"field":"chart_19","value":chart8},
                                                  {"field":"chart_22","value":chart9},
                                                  {"field":"chart_23","value":chart10},
                                                  {"field":"chart_24","value":chart11},
                                                  {"field":"chart_27","value":chart12},
                                                  {"field":"chart_30","value":chart13},
                                                  {"field":"preference_chart","value":select_chart},
                                                 ]},
                  {"field":'comments_id_chart_v010_10',"value":comments},
                  {"field":'page',"value":next_page}]

    if input1 == None:
        return '/'

    if chart1 == '' or chart1 == '' or chart2 == '' or chart3 == '' or chart4 == '' or chart5 == '' or chart6 == '' or chart7 == '' or chart8 == '' or chart9 == '' or chart10 == '' or chart11 == '' or chart12 == '' or chart13 == '' or select_chart == '':
        return None
    else:
        return next_page