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

                                     #{'id': 0, 'label': 'Cluster 1','color': '#5AB1BB', 'shape':'box', 'size':'5', 'level':'1'},
                                     #{'id': 1, 'label': 'Begin Season', 'color':'#5AB1BB', 'level':'1'},
                                    {'id':0, 'label': '00s', 'color':'rgb(120,255,120)', 'level':'1', 'shape':'circle', 'size':'5', 'x':0, 'y':0, 'font':{'size':22}},
                                    {'id':1, 'label': '01s', 'color':'rgb(120,255,120)', 'level':'1', 'shape':'circle', 'size':'5', 'x':100, 'y':0, 'font':{'size':22}},
                                    {'id':2, 'label': '02s', 'color':'rgb(120,255,120)', 'level':'1', 'shape':'circle', 'size':'5', 'x':200, 'y':0, 'font':{'size':22}},
                                    {'id':3, 'label': '03s', 'color':'rgb(120,255,120)', 'level':'1', 'shape':'circle', 'size':'5', 'x':300, 'y':0, 'font':{'size':22}},
                                    {'id':4, 'label': '04s', 'color':'rgb(120,255,120)', 'level':'1', 'shape':'circle', 'size':'5', 'x':400, 'y':0, 'font':{'size':22}},
                                    {'id':5, 'label': '05s', 'color':'rgb(120,255,120)', 'level':'1', 'shape':'circle', 'size':'5', 'x':500, 'y':0, 'font':{'size':22}},
                                    {'id':6, 'label': '06s', 'color':'rgb(120,255,120)', 'level':'1', 'shape':'circle', 'size':'5', 'x':600, 'y':0, 'font':{'size':22}},
                                    {'id':7, 'label': '07s', 'color':'rgb(120,255,120)', 'level':'1', 'shape':'circle', 'size':'5', 'x':700, 'y':0, 'font':{'size':22}},
                                    {'id':8, 'label': '08s', 'color':'rgb(120,255,120)', 'level':'1', 'shape':'circle', 'size':'5', 'x':800, 'y':0, 'font':{'size':22}},
                                    {'id':9, 'label': '09s', 'color':'rgb(120,255,120)', 'level':'1', 'shape':'circle', 'size':'5', 'x':900, 'y':0, 'font':{'size':22}},
                                    {'id':10, 'label': '10s', 'color':'rgb(120,255,120)', 'level':'1', 'shape':'circle', 'size':'5', 'x':1000, 'y':0, 'font':{'size':22}},
                                    {'id':11, 'label': '11s', 'color':'rgb(120,255,120)', 'level':'1', 'shape':'circle', 'size':'5', 'x':1100, 'y':0, 'font':{'size':22}},
                                    {'id':12, 'label': '12s', 'color':'rgb(120,255,120)', 'level':'1', 'shape':'circle', 'size':'5', 'x':1200, 'y':0, 'font':{'size':22}},
                                    {'id':13, 'label': '13s', 'color':'rgb(120,255,120)', 'level':'1', 'shape':'circle', 'size':'5', 'x':1300, 'y':0, 'font':{'size':22}},
                                    {'id':14, 'label': '14s', 'color':'rgb(120,255,120)', 'level':'1', 'shape':'circle', 'size':'5', 'x':1400, 'y':0, 'font':{'size':22}},
                                    {'id':15, 'label': '15s', 'color':'rgb(120,255,120)', 'level':'1', 'shape':'circle', 'size':'5', 'x':1500, 'y':0, 'font':{'size':22}},
                                    {'id':16, 'label': '16s', 'color':'rgb(120,255,120)', 'level':'1', 'shape':'circle', 'size':'5', 'x':1600, 'y':0, 'font':{'size':22}},
                                    {'id':17, 'label': '17s', 'color':'rgb(120,255,120)', 'level':'1', 'shape':'circle', 'size':'5', 'x':1700, 'y':0, 'font':{'size':22}},
                                    {'id':18, 'label': '18s', 'color':'rgb(120,255,120)', 'level':'1', 'shape':'circle', 'size':'5', 'x':1800, 'y':0, 'font':{'size':22}},
                                    {'id':19, 'label': '19s', 'color':'rgb(120,255,120)', 'level':'1', 'shape':'circle', 'size':'5', 'x':1900, 'y':0, 'font':{'size':22}},
                                    {'id':20, 'label': '20s', 'color':'rgb(120,255,120)', 'level':'1', 'shape':'circle', 'size':'5', 'x':2000, 'y':0, 'font':{'size':22}},
                                    {'id':21, 'label': '21s', 'color':'rgb(120,255,120)', 'level':'1', 'shape':'circle', 'size':'5', 'x':2100, 'y':0, 'font':{'size':22}},
                                    {'id':22, 'label': '22s', 'color':'rgb(120,255,120)', 'level':'1', 'shape':'circle', 'size':'5', 'x':2200, 'y':0, 'font':{'size':22}},
                                    {'id':23, 'label': '23s', 'color':'rgb(120,255,120)', 'level':'1', 'shape':'circle', 'size':'5', 'x':2300, 'y':0, 'font':{'size':22}},
                                    {'id':24, 'label': '24s', 'color':'rgb(120,255,120)', 'level':'1', 'shape':'circle', 'size':'5', 'x':2400, 'y':0, 'font':{'size':22}},
                                    {'id':25, 'label': '25s', 'color':'rgb(120,255,120)', 'level':'1', 'shape':'circle', 'size':'5', 'x':2500, 'y':0, 'font':{'size':22}},
                                    {'id':26, 'label': '26s', 'color':'rgb(120,255,120)', 'level':'1', 'shape':'circle', 'size':'5', 'x':2600, 'y':0, 'font':{'size':22}},
                                    {'id':27, 'label': '27s', 'color':'rgb(120,255,120)', 'level':'1', 'shape':'circle', 'size':'5', 'x':2700, 'y':0, 'font':{'size':22}},
                                    {'id':28, 'label': '28s', 'color':'rgb(120,255,120)', 'level':'1', 'shape':'circle', 'size':'5', 'x':2800, 'y':0, 'font':{'size':22}},
                                    {'id':29, 'label': '29s', 'color':'rgb(120,255,120)', 'level':'1', 'shape':'circle', 'size':'5', 'x':2900, 'y':0, 'font':{'size':22}}


                                    ],

                             'edges':[
                                    {'id':'1−8', 'arrows':'arrow.to','from': 1, 'to': 8, 'width':1,'color':{'color':'rgb(120,120,255)'}},
                                    {'id':'2−16', 'arrows':'arrow.to','from': 2, 'to': 16, 'width':1,'color':{'color':'rgb(120,120,255)'}},
                                    {'id':'3−25', 'arrows':'arrow.to','from': 3, 'to': 25, 'width':1,'color':{'color':'rgb(120,120,255)'}},
                                    {'id':'4−8', 'arrows':'arrow.to','from': 4, 'to': 8, 'width':1,'color':{'color':'rgb(120,120,255)'}},
                                    {'id':'6−2', 'arrows':'arrow.to','from': 6, 'to': 2, 'width':1,'color':{'color':'rgb(255,120,120)'}},
                                    {'id':'6−4', 'arrows':'arrow.to','from': 6, 'to': 4, 'width':1,'color':{'color':'rgb(255,120,120)'}},
                                    {'id':'6−23', 'arrows':'arrow.to','from': 6, 'to': 23, 'width':1,'color':{'color':'rgb(120,120,255)'}},
                                    {'id':'8−21', 'arrows':'arrow.to','from': 8, 'to': 21, 'width':1,'color':{'color':'rgb(120,120,255)'}},
                                    {'id':'9−13', 'arrows':'arrow.to','from': 9, 'to': 13, 'width':1,'color':{'color':'rgb(120,120,255)'}},
                                    {'id':'10−15', 'arrows':'arrow.to','from': 10, 'to': 15, 'width':1,'color':{'color':'rgb(120,120,255)'}},
                                    {'id':'11−18', 'arrows':'arrow.to','from': 11, 'to': 18, 'width':1,'color':{'color':'rgb(120,120,255)'}},
                                    {'id':'11−14', 'arrows':'arrow.to','from': 11, 'to': 14, 'width':1,'color':{'color':'rgb(120,120,255)'}},
                                    {'id':'11−15', 'arrows':'arrow.to','from': 11, 'to': 15, 'width':1,'color':{'color':'rgb(120,120,255)'}},
                                    {'id':'11−3', 'arrows':'arrow.to','from': 11, 'to': 3, 'width':1,'color':{'color':'rgb(255,120,120)'}},
                                    {'id':'13−12', 'arrows':'arrow.to','from': 13, 'to': 12, 'width':1,'color':{'color':'rgb(255,120,120)'}},
                                    {'id':'14−10', 'arrows':'arrow.to','from': 14, 'to': 10, 'width':1,'color':{'color':'rgb(255,120,120)'}},
                                    {'id':'14−4', 'arrows':'arrow.to','from': 14, 'to': 4, 'width':1,'color':{'color':'rgb(255,120,120)'}},
                                    {'id':'14−0', 'arrows':'arrow.to','from': 14, 'to': 0, 'width':1,'color':{'color':'rgb(255,120,120)'}},
                                    {'id':'15−16', 'arrows':'arrow.to','from': 15, 'to': 16, 'width':3,'color':{'color':'rgb(120,120,255)'}},
                                    {'id':'16−8', 'arrows':'arrow.to','from': 16, 'to': 8, 'width':1,'color':{'color':'rgb(255,120,120)'}},
                                    {'id':'16−13', 'arrows':'arrow.to','from': 16, 'to': 13, 'width':1,'color':{'color':'rgb(255,120,120)'}},
                                    {'id':'17−13', 'arrows':'arrow.to','from': 17, 'to': 13, 'width':1,'color':{'color':'rgb(255,120,120)'}},
                                    {'id':'17−11', 'arrows':'arrow.to','from': 17, 'to': 11, 'width':1,'color':{'color':'rgb(255,120,120)'}},
                                    {'id':'17−16', 'arrows':'arrow.to','from': 17, 'to': 16, 'width':1,'color':{'color':'rgb(255,120,120)'}},
                                    {'id':'17−19', 'arrows':'arrow.to','from': 17, 'to': 19, 'width':1,'color':{'color':'rgb(120,120,255)'}},
                                    {'id':'17−27', 'arrows':'arrow.to','from': 17, 'to': 27, 'width':1,'color':{'color':'rgb(120,120,255)'}},
                                    {'id':'17−18', 'arrows':'arrow.to','from': 17, 'to': 18, 'width':1,'color':{'color':'rgb(120,120,255)'}},
                                    {'id':'18−19', 'arrows':'arrow.to','from': 18, 'to': 19, 'width':1,'color':{'color':'rgb(120,120,255)'}},
                                    {'id':'18−15', 'arrows':'arrow.to','from': 18, 'to': 15, 'width':1,'color':{'color':'rgb(255,120,120)'}},
                                    {'id':'18−10', 'arrows':'arrow.to','from': 18, 'to': 10, 'width':1,'color':{'color':'rgb(255,120,120)'}},
                                    {'id':'20−18', 'arrows':'arrow.to','from': 20, 'to': 18, 'width':1,'color':{'color':'rgb(255,120,120)'}},
                                    {'id':'21−20', 'arrows':'arrow.to','from': 21, 'to': 20, 'width':1,'color':{'color':'rgb(255,120,120)'}},
                                    {'id':'21−4', 'arrows':'arrow.to','from': 21, 'to': 4, 'width':1,'color':{'color':'rgb(255,120,120)'}},
                                    {'id':'21−12', 'arrows':'arrow.to','from': 21, 'to': 12, 'width':1,'color':{'color':'rgb(255,120,120)'}},
                                    {'id':'21−14', 'arrows':'arrow.to','from': 21, 'to': 14, 'width':1,'color':{'color':'rgb(255,120,120)'}},
                                    {'id':'21−26', 'arrows':'arrow.to','from': 21, 'to': 26, 'width':1,'color':{'color':'rgb(120,120,255)'}},
                                    {'id':'22−2', 'arrows':'arrow.to','from': 22, 'to': 2, 'width':1,'color':{'color':'rgb(255,120,120)'}},
                                    {'id':'22−0', 'arrows':'arrow.to','from': 22, 'to': 0, 'width':1,'color':{'color':'rgb(255,120,120)'}},
                                    {'id':'22−21', 'arrows':'arrow.to','from': 22, 'to': 21, 'width':1,'color':{'color':'rgb(255,120,120)'}},
                                    {'id':'22−18', 'arrows':'arrow.to','from': 22, 'to': 18, 'width':1,'color':{'color':'rgb(255,120,120)'}},
                                    {'id':'22−19', 'arrows':'arrow.to','from': 22, 'to': 19, 'width':1,'color':{'color':'rgb(255,120,120)'}},
                                    {'id':'23−20', 'arrows':'arrow.to','from': 23, 'to': 20, 'width':1,'color':{'color':'rgb(255,120,120)'}},
                                    {'id':'23−6', 'arrows':'arrow.to','from': 23, 'to': 6, 'width':1,'color':{'color':'rgb(255,120,120)'}},
                                    {'id':'23−11', 'arrows':'arrow.to','from': 23, 'to': 11, 'width':1,'color':{'color':'rgb(255,120,120)'}},
                                    {'id':'23−27', 'arrows':'arrow.to','from': 23, 'to': 27, 'width':1,'color':{'color':'rgb(120,120,255)'}},
                                    {'id':'24−21', 'arrows':'arrow.to','from': 24, 'to': 21, 'width':1,'color':{'color':'rgb(255,120,120)'}},
                                    {'id':'25−17', 'arrows':'arrow.to','from': 25, 'to': 17, 'width':1,'color':{'color':'rgb(255,120,120)'}},
                                    {'id':'25−18', 'arrows':'arrow.to','from': 25, 'to': 18, 'width':1,'color':{'color':'rgb(255,120,120)'}},
                                    {'id':'26−15', 'arrows':'arrow.to','from': 26, 'to': 15, 'width':1,'color':{'color':'rgb(255,120,120)'}},
                                    {'id':'26−11', 'arrows':'arrow.to','from': 26, 'to': 11, 'width':1,'color':{'color':'rgb(255,120,120)'}},
                                    {'id':'26−16', 'arrows':'arrow.to','from': 26, 'to': 16, 'width':1,'color':{'color':'rgb(255,120,120)'}},
                                    {'id':'27−6', 'arrows':'arrow.to','from': 27, 'to': 6, 'width':1,'color':{'color':'rgb(255,120,120)'}},
                                    {'id':'27−9', 'arrows':'arrow.to','from': 27, 'to': 9, 'width':1,'color':{'color':'rgb(255,120,120)'}},
                                    {'id':'28−14', 'arrows':'arrow.to','from': 28, 'to': 14, 'width':1,'color':{'color':'rgb(255,120,120)'}},
                                    {'id':'28−21', 'arrows':'arrow.to','from': 28, 'to': 21, 'width':1,'color':{'color':'rgb(255,120,120)'}},

                                    {'id':'1-2','from': 1, 'to': 2,'color':{'color':'rgb(120,120,255)'}},
                                    {'id':'2-3','from': 2, 'to': 3,'color':{'color':'rgb(120,120,255)'}},
                                    {'id':'3-4','from': 3, 'to': 4,'color':{'color':'rgb(120,120,255)'}},
                                    {'id':'4-5','from': 4, 'to': 5,'color':{'color':'rgb(120,120,255)'}},
                                    {'id':'5-6','from': 5, 'to': 6,'color':{'color':'rgb(120,120,255)'}},
                                    {'id':'6-7','from': 6, 'to': 7,'color':{'color':'rgb(120,120,255)'}},
                                    {'id':'7-8','from': 7, 'to': 8,'color':{'color':'rgb(120,120,255)'}},
                                    {'id':'8-9','from': 8, 'to': 9,'color':{'color':'rgb(120,120,255)'}},
                                    {'id':'9-10','from': 9, 'to': 10,'color':{'color':'rgb(120,120,255)'}},
                                    {'id':'10-11','from': 10, 'to': 11,'color':{'color':'rgb(120,120,255)'}},
                                    {'id':'11-12','from': 11, 'to': 12,'color':{'color':'rgb(120,120,255)'}},
                                    {'id':'12-13','from': 12, 'to': 13,'color':{'color':'rgb(120,120,255)'}},
                                    {'id':'13-14','from': 13, 'to': 14,'color':{'color':'rgb(120,120,255)'}},
                                    {'id':'14-15','from': 14, 'to': 15,'color':{'color':'rgb(120,120,255)'}},
                                    {'id':'15-16','from': 15, 'to': 16,'color':{'color':'rgb(120,120,255)'}},
                                    {'id':'16-17','from': 16, 'to': 17,'color':{'color':'rgb(120,120,255)'}},
                                    {'id':'17-18','from': 17, 'to': 18,'color':{'color':'rgb(120,120,255)'}},
                                    {'id':'18-19','from': 18, 'to': 19,'color':{'color':'rgb(120,120,255)'}},
                                    {'id':'19-20','from': 19, 'to': 20,'color':{'color':'rgb(120,120,255)'}},
                                    {'id':'20-21','from': 20, 'to': 21,'color':{'color':'rgb(120,120,255)'}},
                                    {'id':'21-22','from': 21, 'to': 22,'color':{'color':'rgb(120,120,255)'}},
                                    {'id':'22-23','from': 22, 'to': 23,'color':{'color':'rgb(120,120,255)'}},
                                    {'id':'23-24','from': 23, 'to': 24,'color':{'color':'rgb(120,120,255)'}},
                                    {'id':'24-25','from': 24, 'to': 25,'color':{'color':'rgb(120,120,255)'}},
                                    {'id':'25-26','from': 25, 'to': 26,'color':{'color':'rgb(120,120,255)'}},
                                    {'id':'26-27','from': 26, 'to': 27,'color':{'color':'rgb(120,120,255)'}},
                                    {'id':'27-28','from': 27, 'to': 28,'color':{'color':'rgb(120,120,255)'}},
                                    {'id':'28-29','from': 28, 'to': 29,'color':{'color':'rgb(120,120,255)'}},
                                    {'id':'29-30','from': 29, 'to': 30,'color':{'color':'rgb(120,120,255)'}}

                                      ],
                     },

                     options={
                     'height':'600px',
                     'width':'100%',
                     'layout': {
                                'hierarchical': {
                                'enabled': False,
                                'sortMethod': 'directed',
                                'parentCentralization': True,
                                }
                     },
                     'physics':{'barnesHut': {'avoidOverlap': 0.4}},
                     #physics={'barnesHut': {'avoidOverlap': 0}},
                     'edges':{'arrows': {'to': {'enabled': True}},
                            'smooth': {'type': "curvedCW", 'forceDirection': 'vertical'}},
                     'nodes':{'fixed':{'x':True, 'y':True},'shape':'dot'},
                     'interaction':{'zoomView':False,'dragNodes':False,'dragView':False}
                     #fixed={'fixed.x':'true'}

                     }
                     ),
])

@app.callback(
    Output('net', 'options'),
#    [Input('color', 'value')]
    )
def myfun(x):
    return {}

if __name__ == '__main__':
    app.run_server(debug=True)
