from dash.dependencies import Input, Output, State
import dash_html_components as html
import dash_core_components as dcc

from app import app

from frontend import frontend
from backend import backend, feedbackmessage

feedmsg = feedbackmessage.feedbackmessage()
control = backend.backend()
interface = frontend.frontend()

_page_name = "prefv002_1"
_data_cache = []

layout = html.Div([
    interface.survey_warning("warning_"+_page_name),
    interface.survey_chart_preference(control.get_view_question_page_view("V002",_page_name),_page_name),
    interface.survey_send("send_"+_page_name)
])


@app.callback(
    Output('warning_'+_page_name, 'children'),
    [Input('send_'+_page_name, 'href')])
def warning_body_prefv002_1(input1):
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
     Input("chart_05", 'value'),
     Input("chart_07", 'value'),
     Input("chart_08", 'value'),
     Input("chart_09", 'value'),
     Input("chart_10", 'value'),
     Input("chart_11", 'value'),
     Input("chart_12", 'value'),
     Input("id_chart_v002_1", 'value')])
def update_body_prefv002_1(input1,chart1,chart2,chart3,chart4,chart5,chart6,chart7,chart8,chart9,chart10,select_chart):
    global _data_cache
    global _page_name

    next_page = "thanks"
    if(control.has_next_page(_page_name)):
        next_page =control.get_next_page(_page_name)

    _data_cache= [{"field":'user_V002_5',"value":[
                                                  {"id_chart_01":"01","value":chart1},
                                                  {"id_chart_02":"02","value":chart2},
                                                  {"id_chart_03":"03","value":chart3},
                                                  {"id_chart_04":"05","value":chart4},
                                                  {"id_chart_05":"07","value":chart5},
                                                  {"id_chart_06":"08","value":chart6},
                                                  {"id_chart_07":"09","value":chart7},
                                                  {"id_chart_08":"10","value":chart8},
                                                  {"id_chart_09":"11","value":chart9},
                                                  {"id_chart_10":"12","value":chart10},
                                                  {"preference_chart":select_chart},
                                                 ]},
                  {"field":'page',"value":next_page}]

    if input1 == None:
        return '/'

    if chart1 == '' or chart1 == '' or chart2 == '' or chart3 == '' or chart4 == '' or chart5 == '' or chart6 == '' or chart7 == '' or chart8 == '' or chart9 == '' or chart10 == '' or select_chart == '':
        return None
    else:
        return next_page