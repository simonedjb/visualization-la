from dash.dependencies import Input, Output, State
import dash_html_components as html
import dash_core_components as dcc

from app import app

from frontend import frontend
from backend import backend, feedbackmessage

feedmsg = feedbackmessage.feedbackmessage()
control = backend.backend()
interface = frontend.frontend()

_page_name = "prefv007_1"
_data_cache = []

def layout(data_cache=[]):
    global interface
    global _page_name
    return html.Div([
                interface.survey_warning("warning_"+_page_name),
                interface.survey_chart_preference(control.get_view_question_page_view("V007",_page_name),_page_name,data_cache),
                interface.survey_send("send_"+_page_name)
            ])

@app.callback(
    Output('warning_'+_page_name, 'children'),
    [Input('send_'+_page_name, 'href')])
def warning_body_prefv007_1(input1):
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
     Input("chart_04", 'value'),
     Input("id_chart_v007_1", 'value'),
     Input("comments_id_chart_v007_23",'value')])
def update_body_prefv007_1(input1,chart1,chart2,chart3,chart4,select_chart,comments):
    global _data_cache
    global _page_name

    next_page = "thanks"
    if(control.has_next_page(_page_name)):
        next_page =control.get_next_page(_page_name)

    print(str("Gráfico 1 "+str(chart1)))
    print(str("Gráfico 2 "+str(chart2)))
    print(str("Gráfico 3 "+str(chart3)))
    print(str("Gráfico 4 "+str(chart4)))
    # print(str("Gráfico 5 "+str(chart5)))
    # print(str("Gráfico 6 "+str(chart6)))
    # print(str("Gráfico 7 "+str(chart7)))
    # print(str("Gráfico 8 "+str(chart8)))
    # print(str("Gráfico 9 "+str(chart9)))
    # print(str("Gráfico 10 "+str(chart10)))
    # print(str("Gráfico 11 "+str(chart11)))
    # print(str("Gráfico 12 "+str(chart11)))
    # print(str("Gráfico 13 "+str(chart11)))
    print(str("Selection "+str(select_chart)))

    _data_cache= [{"field":'user_V007_23',"value":[
                                                  {"field":"chart_01","value":chart1},
                                                  {"field":"chart_02","value":chart2},
                                                  {"field":"chart_03","value":chart3},
                                                  {"field":"chart_04","value":chart4},
                                                  {"field":"preference_chart","value":select_chart},
                                                 ]},
                  {"field":'comments_id_chart_v007_23',"value":comments},
                  {"field":'page',"value":next_page}]

    print(_data_cache)

    if input1 == None:
        return '/'

    if chart1 == '':
        return None
    else:
        return next_page