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
    eadxp._data_cache=[]
    aboutyou._data_cache=[]
    abouteadxp._data_cache=[]
    aboutlogs._data_cache=[]
    aboutstudentinformation._data_cache=[]
    aboutvisualization._data_cache=[]
    prefv001_1._data_cache=[]
    prefv001_2._data_cache=[]
    prefv002_1._data_cache=[]
    prefv003_1._data_cache=[]
    prefv004_1._data_cache=[]
    prefv005_1._data_cache=[]
    prefv006_1._data_cache=[]
    prefv007_1._data_cache=[]
    prefv008_1._data_cache=[]
    prefv008_2._data_cache=[]
    prefv009_1._data_cache=[]
    prefv010_1._data_cache=[]
    prefv011_1._data_cache=[]
    eadxp.feedmsg.set_clicks(0)
    aboutyou.feedmsg.set_clicks(0)
    abouteadxp.feedmsg.set_clicks(0)
    aboutlogs.feedmsg.set_clicks(0)
    aboutstudentinformation.feedmsg.set_clicks(0)
    aboutvisualization.feedmsg.set_clicks(0)
    prefv001_1.feedmsg.set_clicks(0)
    prefv001_2.feedmsg.set_clicks(0)
    prefv002_1.feedmsg.set_clicks(0)
    prefv003_1.feedmsg.set_clicks(0)
    prefv004_1.feedmsg.set_clicks(0)
    prefv005_1.feedmsg.set_clicks(0)
    prefv006_1.feedmsg.set_clicks(0)
    prefv007_1.feedmsg.set_clicks(0)
    prefv008_1.feedmsg.set_clicks(0)
    prefv008_2.feedmsg.set_clicks(0)
    prefv009_1.feedmsg.set_clicks(0)
    prefv010_1.feedmsg.set_clicks(0)
    prefv011_1.feedmsg.set_clicks(0)

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    global _control
    global _interface
    print (pathname)
    if pathname == '/' or pathname == None or home._user_cache == None:
        print("index - /")
        clear_settings()
        # return prefv001_1.layout()
        # return prefv001_2.layout()
        # return prefv008_1.layout()
        # return prefv008_2.layout()
        # return prefv002_1.layout()
        # return prefv003_1.layout()
        # return prefv004_1.layout()
        # return prefv010_1.layout()
        # return prefv005_1.layout()
        # return prefv006_1.layout()
        # return prefv007_1.layout()
        # return prefv009_1.layout() #Falta
        # return prefv011_1.layout() #Falta
        return home.layout()
        # return eadxp.layout()
        # return aboutyou.layout()
        # return abouteadxp.layout()
        # return aboutlogs.layout()
        # return aboutstudentinformation.layout()
        # return aboutvisualization.layout()
    elif pathname == '/eadxp':
        print("index - /eadxp")
        return eadxp.layout()
    elif pathname == '/aboutyou':
        print("index - /aboutyou")
        return aboutyou.layout(aboutyou._data_cache)
    elif pathname == '/abouteadxp':
        print("index - /abouteadxp")
        return abouteadxp.layout(abouteadxp._data_cache)
    elif pathname == '/aboutlogs':
        print("index - /aboutlogs")
        return aboutlogs.layout(aboutlogs._data_cache)
    elif pathname == '/aboutstudentinformation':
        print("index - /aboutstudentinformation")
        return aboutstudentinformation.layout(aboutstudentinformation._data_cache)
    elif pathname == '/aboutvisualization':
        print("index - /aboutvisualization")
        aboutvisualization.control = _control
        return aboutvisualization.layout(aboutvisualization._data_cache)
    elif pathname == '/prefv001_1':
        print("index - /prefv001_1")
        prefv001_1.control = _control
        return prefv001_1.layout(prefv001_1._data_cache)
    elif pathname == '/prefv001_2':
        print("index - /prefv001_2")
        prefv001_2.control = _control
        return prefv001_2.layout(prefv001_2._data_cache)
    elif pathname == '/prefv002_1':
        print("index - /prefv002_1")
        prefv002_1.control = _control
        return prefv002_1.layout(prefv002_1._data_cache)
    elif pathname == '/prefv003_1':
        print("index - /prefv003_1")
        prefv003_1.control = _control
        return prefv003_1.layout(prefv003_1._data_cache)
    elif pathname == '/prefv004_1':
        print("index - /prefv004_1")
        prefv004_1.control = _control
        return prefv004_1.layout(prefv004_1._data_cache)
    elif pathname == '/prefv005_1':
        print("index - /prefv005_1")
        prefv005_1.control = _control
        return prefv005_1.layout(prefv005_1._data_cache)
    elif pathname == '/prefv006_1':
        print("index - /prefv006_1")
        prefv006_1.control = _control
        return prefv006_1.layout(prefv006_1._data_cache)
    elif pathname == '/prefv007_1':
        print("index - /prefv007_1")
        prefv007_1.control = _control
        return prefv007_1.layout(prefv007_1._data_cache)
    elif pathname == '/prefv008_1':
        print("index - /prefv008_1")
        prefv008_1.control = _control
        return prefv008_1.layout(prefv008_1._data_cache)
    elif pathname == '/prefv008_2':
        print("index - /prefv008_2")
        prefv008_2.control = _control
        return prefv008_2.layout(prefv008_2._data_cache)
    elif pathname == '/prefv009_1':
        print("index - /prefv009_1")
        prefv009_1.control = _control
        return prefv009_1.layout(prefv009_1._data_cache)
    elif pathname == '/prefv010_1':
        print("index - /prefv010_1")
        prefv010_1.control = _control
        return prefv010_1.layout(prefv010_1._data_cache)
    elif pathname == '/prefv011_1':
        print("index - /prefv011_1")
        prefv011_1.control = _control
        return prefv011_1.layout(prefv011_1._data_cache)
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
    if not current_page in ['/eadxp','/aboutyou','/abouteadxp','/aboutlogs','/aboutstudentinformation','/aboutvisualization','/thanks',
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
        elif _current_page == '/prefv001_1':
            _control.record_data(user, prefv001_1._data_cache)
        elif _current_page == '/prefv001_2':
            _control.record_data(user, prefv001_2._data_cache)
        elif _current_page == '/prefv002_1':
            _control.record_data(user, prefv002_1._data_cache)
        elif _current_page == '/prefv003_1':
            _control.record_data(user, prefv003_1._data_cache)
        elif _current_page == '/prefv004_1':
            _control.record_data(user, prefv004_1._data_cache)
        elif _current_page == '/prefv005_1':
            _control.record_data(user, prefv005_1._data_cache)
        elif _current_page == '/prefv006_1':
            _control.record_data(user, prefv006_1._data_cache)
        elif _current_page == '/prefv007_1':
            _control.record_data(user, prefv007_1._data_cache)
        elif _current_page == '/prefv008_1':
            _control.record_data(user, prefv008_1._data_cache)
        elif _current_page == '/prefv008_2':
            _control.record_data(user, prefv008_2._data_cache)
        elif _current_page == '/prefv009_1':
            _control.record_data(user, prefv009_1._data_cache)
        elif _current_page == '/prefv010_1':
            _control.record_data(user, prefv010_1._data_cache)
        elif _current_page == '/prefv011_1':
            _control.record_data(user, prefv011_1._data_cache)

        _current_page = current_page
        
    return current_page

if __name__ == '__main__':
    app.run_server(debug=True, port=7000)