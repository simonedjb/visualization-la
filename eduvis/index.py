import pandas as pd
import numpy as pd

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

import plotly.graph_objs as go

import frontend
import backend

import users

import V001 as view1
import V002 as view2
import V003 as view3
import V004 as view4
import V005 as view5
import V006 as view6
# import V007 as view7
import V008 as view8
# import V009 as view9
import V010 as view10
# import V011 as view11

user = users.users(user_id = 3)
language = user.user_language_preference()

layout = frontend.frontend(language = language)
control = backend.backend(user = user, language = language)


#materialize-v1.0.0/materialize/css/materialize.css'
# external_stylesheets = ['https://fonts.googleapis.com/icon?family=Material+Icons',
#                         'starter-template/css/materialize.css',
#                         'starter-template/css/style.css']
external_stylesheets = ['https://fonts.googleapis.com/icon?family=Material+Icons']

app = dash.Dash(__name__, 
                external_stylesheets=external_stylesheets, 
                meta_tags=[
                            {
                                'name': 'viewport',
                                'content': 'width=device-width, initial-scale=1, maximum-scale=1.0'
                            },
                            {
                                'http-equiv': 'Content-Type',
                                'content': 'text/html; charset=UTF-8'
                            }
                        ])

app.title = "EduVis"
# app.favicon = ""


app.layout = html.Div(children=[layout.nav(), layout.workspace_teacher(), layout.footer()])

@app.callback(
    Output('output-state', 'children'),
    [Input('opt-1', 'n_clicks_timestamp'),
    Input('opt-2', 'n_clicks_timestamp'),
    Input('opt-3', 'n_clicks_timestamp'),
    Input('opt-4', 'n_clicks_timestamp'),
    Input('opt-5', 'n_clicks_timestamp'),
    Input('opt-6', 'n_clicks_timestamp'),
    Input('opt-7', 'n_clicks_timestamp'),
    Input('opt-8', 'n_clicks_timestamp'),
    Input('opt-9', 'n_clicks_timestamp'),
    Input('opt-10', 'n_clicks_timestamp'),
    Input('opt-11', 'n_clicks_timestamp')])

def display_click_data(opt1, opt2, opt3, opt4, opt5, opt6, opt7, opt8, opt9, opt10, opt11):
    lst_opt = [int(opt1), int(opt2), int(opt3), int(opt4), int(opt5), int(opt6), int(opt7), int(opt8), int(opt9), int(opt10), int(opt11)]    
    val_max = max(lst_opt)
    
    if val_max == 0: 
        return html.H1(className="header center orange-text", children=["Wellcome to EduVis"]),

    val_index = lst_opt.index(val_max)+1

    return control.get_preference_graph(val_index)

    

    
if __name__ == '__main__':
    app.run_server(debug=True)
    # sorted(dir(html))

# poll
# bar_chart
# assessment
# bubble_chart
# insert_chart
# insert_chart_outlined
# account_circle
# school
# plus_one
# chevron_right
# arrow_right
# apps
# view_comfy
# tune
# dehaze
# https://material.io/tools/icons/?style=baseline

#Rock the mountain