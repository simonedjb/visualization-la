from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from app import app
from frontend import frontend, home, eadxp, aboutyou, abouteadxp, aboutstudentinformation, aboutlogs, aboutvisualization, thanks
from frontend import prefv001, prefv008, prefv002, prefv003, prefv009, prefv004, prefv010, prefv005, prefv006, prefv011, prefv007
# from backend import backend

interface = frontend.frontend()

_current_page = 1

app.layout = interface.survey_body()

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
    global _current_page
    global interface
    print (pathname)
    # if _current_page == 1:
    #     return eadxp.layout
    if pathname == '/':
        print("index - /presentation")
        clear_settings()
        return home.layout
    elif pathname == '/presentation':
        print("index - /presentation")
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

if __name__ == '__main__':
    app.run_server(debug=True, port=7000)





































































