import dash
import os

from flask import send_from_directory


app = dash.Dash()
server = app.server
app.config.supress_callback_exceptions = True

external_css = ['/assets/style.css']
for css in external_css:
    app.css.append_css({"external_url": css})


@app.server.route('/static/<path:path>')
def static_file(path):
    static_folder = os.path.join(os.getcwd(), 'static')
    return send_from_directory(static_folder, path)



# import numpy as np
# import pandas as pd

# import plotly.graph_objs as go

# import dash
# import dash_core_components as dcc
# import dash_html_components as html
# from dash.dependencies import Input, Output, State

# import plotly.graph_objs as go

# import frontend

# from app import app
# from apps import app1, app2


# app.layout = html.Div([
#     dcc.Location(id='url', refresh=False),
#     html.Div(id='page-content')
# ])


# @app.callback(Output('page-content', 'children'),
#               [Input('url', 'pathname')])
# def display_page(pathname):
#     if pathname == '/apps/app1':
#          return app1.layout
#     elif pathname == '/apps/app2':
#          return app2.layout
#     else:
#         return '404'

# if __name__ == '__main__':
#     app.run_server(debug=True, port=7050)




# import numpy as np
# import pandas as pd

# import plotly.graph_objs as go

# import dash
# import dash_core_components as dcc
# import dash_html_components as html
# from dash.dependencies import Input, Output, State

# import plotly.graph_objs as go

# import frontend
# # import backend

# # import users

# # import V001 as view1
# # import V002 as view2
# # import V003 as view3
# # import V004 as view4
# # import V005 as view5
# # import V006 as view6
# # # import V007 as view7
# # import V008 as view8
# # # import V009 as view9
# # import V010 as view10
# # # import V011 as view11

# global_df = 1
# layout = frontend.frontend()
# # control = backend.backend(user = user, language = language)


# #materialize-v1.0.0/materialize/css/materialize.css'
# # external_stylesheets = ['https://fonts.googleapis.com/icon?family=Material+Icons',
# #                         'starter-template/css/materialize.css',
# #                         'starter-template/css/style.css']
# # external_stylesheets = ['https://fonts.googleapis.com/icon?family=Material+Icons',
# #                         'https://codepen.io/chriddyp/pen/bWLwgP.css']

# # external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# app = dash.Dash(__name__, 
#                 # external_stylesheets=external_stylesheets, 
#                 meta_tags=[
#                             {
#                                 'name': 'viewport',
#                                 'content': 'width=device-width, initial-scale=1, maximum-scale=1.0'
#                             },
#                             {
#                                 'http-equiv': 'Content-Type',
#                                 'content': 'text/html; charset=UTF-8'
#                             }
#                         ])

# app.title = "Survey Preferences"
# # app.favicon = ""


# # app.layout = html.Div(children=[layout.survey_profile(),
# #                                 layout.survey_logs(),
# #                                 layout.survey_visualization(),
# #                                 layout.survey_send()])

# app.layout = html.Div(children=[layout.survey_hidden_values(),
#                                 layout.survey_body(),
#                                 layout.survey_send()])

# # @app.callback(
# #     Output('output-state', 'children'),
# #     [Input('send', 'n_clicks')],
# #     [State('input-1-state', 'value'),
# #      State('input-2-state', 'value')])
# @app.callback(
#     Output('output-state', 'children'),
#     [Input('send', 'n_clicks')])
# def update_body(n_clicks):
#     global global_df
#     global layout
#     print ("Page: "+str(global_df))
#     if global_df == 1:
#         global_df += 1        
#         return layout.survey_filter()
#     elif global_df == 2:
#         global_df += 1
#         return layout.survey_profile()
#     elif global_df == 3:
#         global_df += 1
#         return layout.survey_ead_xp()
#     elif global_df == 4:
#         global_df += 1
#         return layout.survey_logs()
#     elif global_df == 5:
#         global_df += 1
#         return layout.survey_visualization()
#     elif global_df == 6:
#         global_df += 1
#         return layout.survey_end()
    
#     return layout.survey_end()

# # app.callback

# app.config.supress_callback_exceptions = True
# # print("Registering callback 1")
# @app.callback(
#     Output('hidden-div', 'children'),
#     [Input('send', 'n_clicks')],
#     [State('user_ead_xp', 'value')])
# def update_body_pag1(n_clicks,input1):
#     print("input1")
#     # print(input1)
#     return html.Div(id='hidden-div', style={'display':'none'})

# # if global_df == 1:
    
# # elif global_df == 2:
    
# # elif global_df == 3:
# #     global_df += 1
# #     return layout.survey_ead_xp()
# # elif global_df == 4:
# #     global_df += 1
# #     return layout.survey_logs()
# # elif global_df == 5:
# #     global_df += 1
# #     return layout.survey_visualization()
# # elif global_df == 6:
# #     global_df += 1
# #     return layout.survey_end()


# # @app.callback(
# #     Output('output-state', 'children'),
# #     [Input('opt-1', 'n_clicks_timestamp'),
# #     Input('opt-2', 'n_clicks_timestamp'),
# #     Input('opt-3', 'n_clicks_timestamp'),
# #     Input('opt-4', 'n_clicks_timestamp'),
# #     Input('opt-5', 'n_clicks_timestamp'),
# #     Input('opt-6', 'n_clicks_timestamp'),
# #     Input('opt-7', 'n_clicks_timestamp'),
# #     Input('opt-8', 'n_clicks_timestamp'),
# #     Input('opt-9', 'n_clicks_timestamp'),
# #     Input('opt-10', 'n_clicks_timestamp'),
# #     Input('opt-11', 'n_clicks_timestamp'),
# #     Input('submit-search', 'n_clicks_timestamp')])

# # def display_click_data(opt1, opt2, opt3, opt4, opt5, opt6, opt7, opt8, opt9, opt10, opt11, search):
# #     lst_opt = [int(opt1), int(opt2), int(opt3), int(opt4), int(opt5), int(opt6), int(opt7), int(opt8), int(opt9), int(opt10), int(opt11), int(search)]
# #     val_max = max(lst_opt)
    
# #     if val_max == 0:
# #         return html.H1(className="header center orange-text", children=["Wellcome to EduVis, “User "+str(user_id)+"”"]),

# #     if lst_opt.index(val_max) == 11:
# #         return control.get_preference_graph(1)

# #     val_index = lst_opt.index(val_max)+1

# #     return control.get_preference_graph(val_index)


# if __name__ == '__main__':
#     app.run_server(debug=True, port=7000)
#     # sorted(dir(html))




# # poll
# # bar_chart
# # assessment
# # bubble_chart
# # insert_chart
# # insert_chart_outlined
# # account_circle
# # school
# # plus_one
# # chevron_right
# # arrow_right
# # apps
# # view_comfy
# # tune
# # dehaze
# # https://material.io/tools/icons/?style=baseline

# #Rock the mountain