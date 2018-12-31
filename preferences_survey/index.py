from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from flask import Flask, session

from app import app
from frontend import frontend, home, eadxp, aboutyou, abouteadxp, aboutstudentinformation, aboutlogs, aboutvisualization, thanks
from frontend import prefv001, prefv008, prefv002, prefv003, prefv009, prefv004, prefv010, prefv005, prefv006, prefv011, prefv007
from backend import backend

control = backend.backend()
interface = frontend.frontend()
app.layout = interface.survey_body()
_current_page = "/"

def clear_settings():
    eadxp.feedmsg.set_clicks(0)
    aboutyou.feedmsg.set_clicks(0)
    abouteadxp.feedmsg.set_clicks(0)
    aboutlogs.feedmsg.set_clicks(0)
    aboutstudentinformation.feedmsg.set_clicks(0)
    aboutvisualization.feedmsg.set_clicks(0)

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    global interface
    print (pathname)
    if pathname == '/' or pathname == None or home._user_cache == None:
        print("index - /")
        clear_settings()
        return home.layout
    elif pathname == '/eadxp':
        print("index - /eadxp")
        return eadxp.layout
    elif pathname == '/aboutyou':
        print("index - /aboutyou")
        return aboutyou.layout
    elif pathname == '/abouteadxp':
        print("index - /abouteadxp")
        return abouteadxp.layout
    elif pathname == '/aboutlogs':
        print("index - /aboutlogs")
        return aboutlogs.layout
    elif pathname == '/aboutstudentinformation':
        print("index - /aboutstudentinformation")
        return aboutstudentinformation.layout
    elif pathname == '/aboutvisualization':
        print("index - /aboutvisualization")
        return aboutvisualization.layout
    elif pathname == '/assignsdone':
        print("index - /assignsdone")
        return prefv001.layout
    elif pathname == '/avaaccess':
        print("index - /avaaccess")
        return prefv008.layout
    elif pathname == '/accessmaterials':
        print("index - /accessmaterials")
        return prefv002.layout
    elif pathname == '/foruminteraction':
        print("index - /foruminteraction")
        return prefv003.layout
    elif pathname == '/videointeraction':
        print("index - /videointeraction")
        return prefv009.layout
    elif pathname == '/videostay':
        print("index - /videostay")
        return prefv004.layout
    elif pathname == '/understandingvideo':
        print("index - /understandingvideo")
        return prefv010.layout
    elif pathname == '/correlationgrade':
        print("index - /correlationgrade")
        return prefv005.layout
    elif pathname == '/correlationprofile':
        print("index - /correlationprofile")
        return prefv006.layout
    elif pathname == '/navigatepattern':
        print("index - /navigatepattern")
        return prefv011.layout
    elif pathname == '/gradeprediction':
        print("index - /gradeprediction")
        return prefv007.layout
    elif pathname == '/thanks':
        print("index - /thanks")
        clear_settings()
        return thanks.layout
    else:
        print("index - /404")
        clear_settings()
        return interface.survey_404()

@app.callback(Output('page_cache', 'children'),
              [Input('url', 'pathname')])
def update_page_cache(current_page):
    global _current_page
    global control
    
    user = home._user_cache
    if user == None or user == "":
        _current_page = None
        return
    
    if not _current_page == current_page:
        if _current_page == '/' or _current_page == None:
            if not control.db_has_database(user):
                control.db_make_database(user)
                control.record_data(user, home._data_cache)
        elif _current_page == '/eadxp':
            control.record_data(user, eadxp._data_cache)
        elif _current_page == '/aboutyou':
            control.record_data(user, aboutyou._data_cache)
        elif _current_page == '/abouteadxp':
            control.record_data(user, abouteadxp._data_cache)
        elif _current_page == '/aboutlogs':
            control.record_data(user, aboutlogs._data_cache)
        elif _current_page == '/aboutstudentinformation':
            control.record_data(user, aboutstudentinformation._data_cache)
        elif _current_page == '/aboutvisualization':
            control.record_data(user, aboutvisualization._data_cache)

        _current_page = current_page

    return current_page

if __name__ == '__main__':
    app.run_server(debug=True, port=7000)


#V00*
# Escala de 1-7
# Qual vc usaria
# No final um dropdown para escolher qual o melhor gráfico para aquela pergunta