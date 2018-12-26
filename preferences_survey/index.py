from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from app import app
from frontend import frontend, home, eadxp, aboutyou, abouteadxp, aboutlogs, aboutvisualization, thanks
# from backend import backend

interface = frontend.frontend()

_current_page = 1

app.layout = interface.survey_body()

def clear_settings():
    eadxp.feedmsg.set_clicks(0)
    aboutyou.feedmsg.set_clicks(0)
    abouteadxp.feedmsg.set_clicks(0)
    aboutlogs.feedmsg.set_clicks(0)
    aboutvisualization.feedmsg.set_clicks(0)

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    global _current_page
    global interface
    print (pathname)
    # if _current_page == 1:
    #     return eadxp.layout

    if pathname == '/survey/presentation':
        print("index - /survey/presentation")
        clear_settings()
        return home.layout
    elif pathname == '/survey/eadxp':
        print("index - /survey/eadxp")
        return eadxp.layout
    elif pathname == '/survey/aboutyou':
        print("index - /survey/aboutyou")
        return aboutyou.layout
    elif pathname == '/survey/abouteadxp':
        print("index - /survey/abouteadxp")
        return abouteadxp.layout
    elif pathname == '/survey/aboutlogs':
        print("index - /survey/aboutlogs")
        return aboutlogs.layout
    elif pathname == '/survey/aboutvisualization':
        print("index - /survey/aboutvisualization")
        return aboutvisualization.layout
    # elif pathname == '/survey/preferences1':
    #     return aboutvisualization.layout
    elif pathname == '/survey/thanks':
        print("index - /survey/thanks")
        clear_settings()
        return thanks.layout
    else:
        print("index - /survey/404")
        clear_settings()
        return interface.survey_404()

if __name__ == '__main__':
    app.run_server(debug=True, port=7000)