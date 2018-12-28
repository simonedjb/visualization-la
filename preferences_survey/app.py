import dash
import os

from flask import send_from_directory
from flask_caching import Cache

app = dash.Dash()
cache = Cache(app.server, config={
    'CACHE_TYPE': 'filesystem',
    'CACHE_DIR': 'cache-directory',
    'CACHE_THRESHOLD': 50  # should be equal to maximum number of active users
})

server = app.server
app.config.supress_callback_exceptions = True

app.favicon = "assets/favicon.ico"

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
