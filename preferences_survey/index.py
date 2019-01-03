from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from flask import Flask, session

from app import app
from frontend import frontend, home, eadxp, aboutyou, abouteadxp, aboutstudentinformation, aboutlogs, aboutvisualization, notfound, thanks
from views import prefv001_1, prefv002_1, prefv001_2, prefv003_1, prefv004_1, prefv005_1, prefv006_1, prefv007_1, prefv008_1, prefv008_2, prefv009_1, prefv010_1, prefv011_1
from backend import backend

_control = backend.backend()
_interface = frontend.frontend()
_current_page = "/"

app.layout = _interface.survey_body()


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
    global _control
    global _interface
    print (pathname)
    if pathname == '/' or pathname == None or home._user_cache == None:
        print("index - /")
        clear_settings()
        # return prefv001_1.layout
        # return prefv001_2.layout
        # return prefv008_1.layout
        # return prefv008_2.layout
        # return prefv002_1.layout
        # return prefv003_1.layout
        # return prefv009_1.layout
        # return prefv004_1.layout
        # return prefv010_1.layout
        # return prefv005_1.layout
        # return prefv006_1.layout
        # return prefv011_1.layout
        # return prefv007_1.layout
        # return aboutstudentinformation.layout
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
        aboutvisualization.control = _control
        return aboutvisualization.layout
    elif pathname == '/prefv001_1':
        print("index - /prefv001_1")
        prefv001_1.control = _control
        return prefv001_1.layout
    elif pathname == '/prefv001_2':
        print("index - /prefv001_2")
        prefv001_2.control = _control
        return prefv001_2.layout
    elif pathname == '/prefv002_1':
        print("index - /prefv002_1")
        prefv002_1.control = _control
        return prefv002_1.layout
    elif pathname == '/prefv003_1':
        print("index - /prefv003_1")
        prefv003_1.control = _control
        return prefv003_1.layout
    elif pathname == '/prefv004_1':
        print("index - /prefv004_1")
        prefv004_1.control = _control
        return prefv004_1.layout
    elif pathname == '/prefv005_1':
        print("index - /prefv005_1")
        prefv005_1.control = _control
        return prefv005_1.layout
    elif pathname == '/prefv006_1':
        print("index - /prefv006_1")
        prefv006_1.control = _control
        return prefv006_1.layout
    elif pathname == '/prefv007_1':
        print("index - /prefv007_1")
        prefv007_1.control = _control
        return prefv007_1.layout
    elif pathname == '/prefv008_1':
        print("index - /prefv008_1")
        prefv008_1.control = _control
        return prefv008_1.layout
    elif pathname == '/prefv008_2':
        print("index - /prefv008_2")
        prefv008_2.control = _control
        return prefv008_2.layout
    elif pathname == '/prefv009_1':
        print("index - /prefv009_1")
        prefv009_1.control = _control
        return prefv009_1.layout
    elif pathname == '/prefv010_1':
        print("index - /prefv010_1")
        prefv010_1.control = _control
        return prefv010_1.layout
    elif pathname == '/prefv011_1':
        print("index - /prefv011_1")
        prefv011_1.control = _control
        return prefv011_1.layout

    # elif pathname == '/assignsdone':
    #     print("index - /assignsdone")
    #     return prefv001.layout
    # elif pathname == '/avaaccess':
    #     print("index - /avaaccess")
    #     return prefv008.layout
    # elif pathname == '/accessmaterials':
    #     print("index - /accessmaterials")
    #     return prefv002.layout
    # elif pathname == '/foruminteraction':
    #     print("index - /foruminteraction")
    #     return prefv003.layout
    # elif pathname == '/videointeraction':
    #     print("index - /videointeraction")
    #     return prefv009.layout
    # elif pathname == '/videostay':
    #     print("index - /videostay")
    #     return prefv004.layout
    # elif pathname == '/understandingvideo':
    #     print("index - /understandingvideo")
    #     return prefv010.layout
    # elif pathname == '/correlationgrade':
    #     print("index - /correlationgrade")
    #     return prefv005.layout
    # elif pathname == '/correlationprofile':
    #     print("index - /correlationprofile")
    #     return prefv006.layout
    # elif pathname == '/navigatepattern':
    #     print("index - /navigatepattern")
    #     return prefv011.layout
    # elif pathname == '/gradeprediction':
    #     print("index - /gradeprediction")
    #     return prefv007.layout
    elif pathname == '/thanks':
        print("index - /thanks")
        clear_settings()
        return thanks.layout
    else:
        print("index - /404")
        clear_settings()
        return notfound.layout

@app.callback(Output('page_cache', 'children'),
              [Input('url', 'pathname')])
def update_page_cache(current_page):
    global _current_page
    global _control
    
    user = home._user_cache
    if user == None or user == "":
        _current_page = None
        return
    
    print("update_page_cache")
    print(current_page)
    if not current_page in ['/eadxp','/aboutyou','/abouteadxp','/aboutlogs','/aboutstudentinformation','/aboutvisualization',
                            '/prefv001_1','/prefv002_1','/prefv001_2','/prefv003_1','/prefv004_1','/prefv005_1','/prefv006_1',
                            '/prefv007_1','/prefv008_1','/prefv008_2','/prefv009_1','/prefv010_1','/prefv011_1']:
        _current_page = current_page = None

    if not _current_page == current_page:
        if _current_page == '/' or _current_page == None:
            if not _control.db_has_database(user):

                _control.db_make_database(user)
                _control.record_data(user, home._data_cache)
            else:
                _control.db_load_database(user)
        elif _current_page == '/eadxp':
            _control.record_data(user, eadxp._data_cache)
        elif _current_page == '/aboutyou':
            _control.record_data(user, aboutyou._data_cache)
        elif _current_page == '/abouteadxp':
            _control.record_data(user, abouteadxp._data_cache)
        elif _current_page == '/aboutlogs':
            _control.record_data(user, aboutlogs._data_cache)
        elif _current_page == '/aboutstudentinformation':
            _control.record_data(user, aboutstudentinformation._data_cache)
        elif _current_page == '/aboutvisualization':
            _control.record_data(user, aboutvisualization._data_cache)
        
        _current_page = current_page

    return current_page

if __name__ == '__main__':
    app.run_server(debug=True, port=7000)


# aboutstudentinformation : Onde se escolhe as visões
#V00*
# Escala de 1-7
# Qual vc usaria
# No final um dropdown para escolher qual o melhor gráfico para aquela pergunta

