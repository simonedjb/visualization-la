import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, Event, State

import visdcc

app = dash.Dash()

app.layout = html.Div([
      visdcc.Network(id='net',
                     data={
                             'nodes':[
                                    {'id': 0, 'label': 'Cluster 1','color': '#5AB1BB', 'shape':'box', 'size':'5', 'level':'1'},
                                    {'id': 1, 'label': 'Begin Season', 'color':'#5AB1BB', 'level':'1'},
                                    {'id': 2, 'label': 'Video 1', 'color':'#A5C882', 'level':'1'},
                                    {'id': 3, 'label': 'Video 2', 'color':'#A5C882', 'level':'1'},
                                    {'id': 4, 'label': 'Video 3', 'color':'#A5C882', 'level':'1'},
                                    {'id': 5, 'label': 'Final Test', 'color':'#A5C882', 'level':'1'},
                                    {'id': 6, 'label': 'End Season', 'color':'#5AB1BB', 'level':'1'},

                                    {'id': 10, 'label': 'Cluster 2', 'color': '#AD5C5C', 'shape':'box', 'size':'10', 'level':'3'},
                                    {'id': 11, 'label': 'Begin Season', 'color':'#AD5C5C', 'x':'150', 'y':'50', 'level':'3'},
                                    {'id': 12, 'label': 'Video 1', 'color':'#CA9797', 'level':'3'},
                                    {'id': 13, 'label': 'Video 2', 'color':'#CA9797', 'level':'2'},
                                    {'id': 14, 'label': 'Video 3', 'color':'#CA9797', 'level':'2'},
                                    {'id': 15, 'label': 'Assigment 1', 'color':'#CA9797', 'level':'4'},
                                    {'id': 16, 'label': 'Assigment 2', 'color':'#CA9797', 'level':'4'},
                                    {'id': 17, 'label': 'Assigment 3', 'color':'#CA9797', 'level':'4'},
                                    {'id': 18, 'label': 'Final Test', 'color':'#CA9797', 'level':'3'},
                                    {'id': 19, 'label': 'End Season', 'color':'#AD5C5C', 'level':'3'},

                                    {'id': 20, 'label': 'Cluster 3', 'color': '#9797FF', 'shape':'box', 'size':'10', 'level':'1'},
                                    {'id': 21, 'label': 'Begin Season', 'color':'#9797FF', 'level':'1'},
                                    {'id': 22, 'label': 'Video 1', 'color':'#CACAFF', 'level':'1'},
                                    {'id': 23, 'label': 'Video 2', 'color':'#CACAFF', 'level':'1'},
                                    {'id': 24, 'label': 'Video 3', 'color':'#CACAFF', 'level':'1'},
                                    {'id': 25, 'label': 'Assigment 1', 'color':'#CACAFF', 'level':'2'},
                                    {'id': 26, 'label': 'Assigment 2', 'color':'#CACAFF', 'level':'2'},
                                    {'id': 27, 'label': 'Assigment 3', 'color':'#CACAFF', 'level':'2'},
                                    {'id': 28, 'label': 'Final Test', 'color':'#CACAFF', 'level':'2'},
                                    {'id': 29, 'label': 'Forum', 'color':'#CACAFF', 'level':'0'},
                                    {'id': 30, 'label': 'End Season', 'color':'#9797FF', 'level':'2'}

                                    ],

                             'edges':[
                                      {'id':'0-1','from': 0, 'to': 1, 'hidden':'false'},
                                      {'id':'0-10','from': 0, 'to': 10, 'hidden':'false'},
                                      {'id':'0-20','from': 0, 'to': 20, 'hidden':'false'},
                                      {'id':'1-2', 'arrows':'arrow.to','from': 1, 'to': 2, 'width':4},
                                      {'id':'2-3', 'arrows':'arrow.to','from': 2, 'to': 3, 'width':4},
                                      {'id':'2-2', 'arrows':'arrow.to','from': 2, 'to': 2},
                                      {'id':'3-4', 'arrows':'arrow.to','from': 3, 'to': 4, 'width':4},
                                      {'id':'3-3', 'arrows':'arrow.to','from': 3, 'to': 3},
                                      {'id':'4-5', 'arrows':'arrow.to','from': 4, 'to': 5, 'width':4},
                                      {'id':'4-4', 'arrows':'arrow.to','from': 4, 'to': 4},
                                      {'id':'5-6', 'arrows':'arrow.to','from': 5, 'to': 6, 'width':4},

                                      {'id':'10-11','from': 10, 'to': 11, 'hidden':'true'},
                                      {'id':'11-12', 'arrows':'arrow.to','from': 11, 'to': 12, 'width':4},
                                      {'id':'12-13', 'arrows':'arrow.to','from': 12, 'to': 13, 'width':1},
                                      {'id':'12-15', 'arrows':'arrow.to','from': 12, 'to': 15, 'width':4},
                                      {'id':'13-14', 'arrows':'arrow.to','from': 13, 'to': 14, 'width':1},
                                      {'id':'13-16', 'arrows':'arrow.to','from': 13, 'to': 16, 'width':1},
                                      {'id':'14-17', 'arrows':'arrow.to','from': 14, 'to': 17, 'width':1},
                                      {'id':'15-13', 'arrows':'arrow.to','from': 15, 'to': 13, 'width':1},
                                      {'id':'15-16', 'arrows':'arrow.to','from': 15, 'to': 16, 'width':4},
                                      {'id':'16-14', 'arrows':'arrow.to','from': 16, 'to': 14, 'width':1},
                                      {'id':'16-17', 'arrows':'arrow.to','from': 16, 'to': 17, 'width':4},
                                      {'id':'17-18', 'arrows':'arrow.to','from': 17, 'to': 18, 'width':4},
                                      {'id':'18-19', 'arrows':'arrow.to','from': 18, 'to': 19, 'width':4},

                                      {'id':'20-21','from': 20, 'to': 21, 'hidden':'true'},
                                      {'id':'20-30','from': 20, 'to': 30, 'hidden':'true'},
                                      {'id':'21-22', 'arrows':'arrow.to','from': 21, 'to': 22, 'width':4},
                                      {'id':'21-25', 'arrows':'arrow.to','from': 21, 'to': 25, 'width':1},
                                      {'id':'22-25', 'arrows':'arrow.to','from': 22, 'to': 25, 'width':4},
                                      {'id':'22-29', 'arrows':'arrow.to','from': 22, 'to': 29, 'width':1},
                                      {'id':'23-24', 'arrows':'arrow.to','from': 23, 'to': 24, 'width':1},
                                      {'id':'23-26', 'arrows':'arrow.to','from': 23, 'to': 26, 'width':1},
                                      {'id':'24-27', 'arrows':'arrow.to','from': 24, 'to': 27, 'width':4},
                                      {'id':'24-28', 'arrows':'arrow.to','from': 24, 'to': 28, 'width':1},
                                      {'id':'25-22', 'arrows':'arrow.to','from': 25, 'to': 22, 'width':1},
                                      {'id':'25-26', 'arrows':'arrow.to','from': 25, 'to': 26, 'width':4},
                                      {'id':'25-23', 'arrows':'arrow.to','from': 25, 'to': 23, 'width':1},
                                      {'id':'26-23', 'arrows':'arrow.to','from': 26, 'to': 23, 'width':1},
                                      {'id':'26-24', 'arrows':'arrow.to','from': 26, 'to': 24, 'width':4},
                                      {'id':'27-24', 'arrows':'arrow.to','from': 27, 'to': 24, 'width':1},
                                      {'id':'27-28', 'arrows':'arrow.to','from': 27, 'to': 28, 'width':4},
                                      {'id':'28-30', 'arrows':'arrow.to','from': 28, 'to': 30, 'width':4},
                                      {'id':'29-23', 'arrows':'arrow.to','from': 29, 'to': 23, 'width':1},




                                      ],

                     },


                     options=dict(height='800px',
                     width='100%',
                     layout={'hierarchical': {'hierarchical.enabled':'True'}}
                     )),
      dcc.RadioItems(id='color',
                     options=[{'label': 'Red'  , 'value': '#ff0000'},
                              {'label': 'Green', 'value': '#00ff00'},
                              {'label': 'Blue' , 'value': '#0000ff'},

                              ],

                     value='Red')
])

@app.callback(
    Output('net', 'options'),
#    [Input('color', 'value')]
    )
def myfun(x):
    return {}

if __name__ == '__main__':
    app.run_server(debug=True)
