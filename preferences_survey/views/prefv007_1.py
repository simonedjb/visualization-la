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

layout = html.Div([
    interface.survey_warning("warning_"+_page_name),
    interface.survey_chart_preference(control.get_view_question_page_view("V007",_page_name),_page_name),
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

# @app.callback(
#     Output('send_'+_page_name, 'href'),
#     [Input('user_cache', 'children'),
#      Input("chart_01", 'value'),
#      Input("chart_02", 'value'),
#      Input("chart_03", 'value'),
#      Input("chart_07", 'value'),
#      Input("chart_11", 'value'),
#      Input("chart_15", 'value'),
#      Input("chart_18", 'value'),
#      Input("chart_19", 'value'),
#      Input("chart_22", 'value'),
#      Input("chart_23", 'value'),
#      Input("chart_24", 'value'),
#      Input("chart_27", 'value'),
#      Input("chart_30", 'value'),
#      Input("id_chart_v010_1", 'value')])
# def update_body_prefv010_1(input1,chart1,chart2,chart3,chart4,chart5,chart6,chart7,chart8,chart9,chart10,chart11,chart12,chart13,select_chart):
#     global _data_cache
#     global _page_name

#     next_page = "thanks"
#     if(control.has_next_page(_page_name)):
#         next_page =control.get_next_page(_page_name)

#     print(str("Gráfico 1 "+str(chart1)))
#     print(str("Gráfico 2 "+str(chart2)))
#     print(str("Gráfico 3 "+str(chart3)))
#     print(str("Gráfico 4 "+str(chart4)))
#     print(str("Gráfico 5 "+str(chart5)))
#     print(str("Gráfico 6 "+str(chart6)))
#     print(str("Gráfico 7 "+str(chart7)))
#     print(str("Gráfico 8 "+str(chart8)))
#     print(str("Gráfico 9 "+str(chart9)))
#     print(str("Gráfico 10 "+str(chart10)))
#     print(str("Gráfico 11 "+str(chart11)))
#     print(str("Gráfico 12 "+str(chart11)))
#     print(str("Gráfico 13 "+str(chart11)))
#     print(str("Selection "+str(select_chart)))

#     _data_cache= [{"field":'user_V008_4',"value":[
#                                                   {"id_chart_01":"03","value":chart1},
#                                                   {"id_chart_02":"06","value":chart2},
#                                                   {"id_chart_03":"07","value":chart3},
#                                                   {"id_chart_04":"09","value":chart4},
#                                                   {"id_chart_05":"11","value":chart5},
#                                                   {"id_chart_06":"10","value":chart6},
#                                                   {"id_chart_07":"07","value":chart7},
#                                                   {"id_chart_08":"08","value":chart8},
#                                                   {"id_chart_09":"09","value":chart9},
#                                                   {"id_chart_10":"11","value":chart10},
#                                                   {"id_chart_11":"11","value":chart11},
#                                                   {"id_chart_12":"11","value":chart12},
#                                                   {"id_chart_13":"11","value":chart13},
#                                                   {"preference_chart":select_chart},
#                                                  ]},
#                   {"field":'page',"value":next_page}]

#     print(_data_cache)

#     if input1 == None:
#         return '/'

#     if chart1 == '':
#         return None
#     else:
#         return next_page