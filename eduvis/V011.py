import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, Event, State

import visdcc
import random

import plotly
import plotly.plotly as py
import plotly.tools as tls
import plotly.graph_objs as go

import pandas as pd
import numpy as np


from plotly.graph_objs import Figure, Layout, Bar, Table, Heatmap, Scatter, Box, Violin
from plotly.offline import init_notebook_mode, iplot


from sklearn import metrics
from sklearn.cluster import KMeans


init_notebook_mode(connected=True) # initiate notebook for offline plot
plotly.__version__

class V011:
    NUMBER_ACTIONS = 50
    COUNTDATA = pd.DataFrame()
    DATASET = pd.DataFrame()


    _language = "pt"
    _type_result="jupyter-notebook"

    def __init__(self, language="pt", type_result = "jupyter-notebook"):
        self._language = language
        self._type_result = type_result

    def generate_dataset(self, number_students = 20, students_names = pd.DataFrame()):
        self.NUMBER_STUDENTS = number_students
        self.COUNTDATA = pd.DataFrame(0, index=range(0,1), columns=["Dropout", "0 - 60", "61 - 70", "71 - 80", "81 - 90", "91 - 100"])

        if len(students_names.columns.tolist()) == 0:
            names = pd.read_csv("names.csv")
        else:
            names = students_names
        rand_names = [names.group_name[np.random.randint(0,len(names.group_name)+1)] for n in range(0,self.NUMBER_STUDENTS)]
        rand_names.sort()


        self.DATASET = pd.DataFrame(columns=["Students","Predicted Grade","Grade","Predicted Dropout","Dropout",
        	                                 "AVA Access","Forum Post","Forum Replies","Forum Add Thread","Forum Access", "Cluster"])

        for i in range(0,self.NUMBER_STUDENTS):
            self.DATASET.loc[i,"Students"] = rand_names[i]
            self.DATASET.loc[i,"Predicted Grade"] = random.choice(['Dropout','0 - 60','61 - 70', '71 - 80', '81 - 90', '91 - 100'])
            if self.DATASET.loc[i,"Predicted Grade"] == 'Dropout':
                self.DATASET.loc[i,"Predicted Dropout"] = True
                self.DATASET.loc[i,"Grade"] = 0
                self.DATASET.loc[i,"Cluster"] = 0
                self.COUNTDATA.loc[0,"Dropout"] += 1

                self.DATASET.loc[i,"AVA Access"] = np.random.randint(5,26)
                self.DATASET.loc[i,"Forum Post"] = np.random.randint(0,4)
                self.DATASET.loc[i,"Forum Replies"] = np.random.randint(0,4)
                self.DATASET.loc[i,"Forum Add Thread"] = np.random.randint(0,4)
                self.DATASET.loc[i,"Forum Access"] =  self.DATASET.loc[i,"Forum Post"] + self.DATASET.loc[i,"Forum Replies"] + self.DATASET.loc[i,"Forum Add Thread"] + np.random.randint(0,7)

            elif self.DATASET.loc[i,"Predicted Grade"] == '0 - 60':
                self.DATASET.loc[i,"Predicted Dropout"] = False
                self.DATASET.loc[i,"Grade"] = int(random.triangular(0,30,80))
                self.DATASET.loc[i,"Cluster"] = 0
                self.COUNTDATA.loc[0,"0 - 60"] += 1

                self.DATASET.loc[i,"AVA Access"] = np.random.randint(20,41)
                self.DATASET.loc[i,"Forum Post"] = np.random.randint(0,8)
                self.DATASET.loc[i,"Forum Replies"] = np.random.randint(0,8)
                self.DATASET.loc[i,"Forum Add Thread"] = np.random.randint(0,4)
                self.DATASET.loc[i,"Forum Access"] = self.DATASET.loc[i,"Forum Post"] + self.DATASET.loc[i,"Forum Replies"] + self.DATASET.loc[i,"Forum Add Thread"] + np.random.randint(0,22)

            elif self.DATASET.loc[i,"Predicted Grade"] == '61 - 70':
                self.DATASET.loc[i,"Predicted Dropout"] = False
                self.DATASET.loc[i,"Grade"] = int(random.triangular(50,65,80))
                self.DATASET.loc[i,"Cluster"] = 1
                self.COUNTDATA.loc[0,"61 - 70"] += 1

                self.DATASET.loc[i,"AVA Access"] = np.random.randint(35,57)
                self.DATASET.loc[i,"Forum Post"] = np.random.randint(1,12)
                self.DATASET.loc[i,"Forum Replies"] = np.random.randint(0,12)
                self.DATASET.loc[i,"Forum Add Thread"] = np.random.randint(0,8)
                self.DATASET.loc[i,"Forum Access"] =  self.DATASET.loc[i,"Forum Post"] + self.DATASET.loc[i,"Forum Replies"] + self.DATASET.loc[i,"Forum Add Thread"] + np.random.randint(2,26)

            elif self.DATASET.loc[i,"Predicted Grade"] == '71 - 80':
                self.DATASET.loc[i,"Predicted Dropout"] = False
                self.DATASET.loc[i,"Grade"] = int(random.triangular(60,75,90))
                self.DATASET.loc[i,"Cluster"] = 1
                self.COUNTDATA.loc[0,"71 - 80"] += 1

                self.DATASET.loc[i,"AVA Access"] = np.random.randint(50,71)
                self.DATASET.loc[i,"Forum Post"] = np.random.randint(2,21)
                self.DATASET.loc[i,"Forum Replies"] = np.random.randint(2,21)
                self.DATASET.loc[i,"Forum Add Thread"] = np.random.randint(0,7)
                self.DATASET.loc[i,"Forum Access"] =  self.DATASET.loc[i,"Forum Post"] + self.DATASET.loc[i,"Forum Replies"] + self.DATASET.loc[i,"Forum Add Thread"] + np.random.randint(4,31)

            elif self.DATASET.loc[i,"Predicted Grade"] == '81 - 90':
                self.DATASET.loc[i,"Predicted Dropout"] = False
                self.DATASET.loc[i,"Grade"] = int(random.triangular(70,85,100))
                self.DATASET.loc[i,"Cluster"] = 2
                self.COUNTDATA.loc[0,"81 - 90"] += 1

                self.DATASET.loc[i,"AVA Access"] = np.random.randint(65,86)
                self.DATASET.loc[i,"Forum Post"] = np.random.randint(5,36)
                self.DATASET.loc[i,"Forum Replies"] = np.random.randint(5,36)
                self.DATASET.loc[i,"Forum Add Thread"] = np.random.randint(1,11)
                self.DATASET.loc[i,"Forum Access"] =  self.DATASET.loc[i,"Forum Post"] + self.DATASET.loc[i,"Forum Replies"] + self.DATASET.loc[i,"Forum Add Thread"] + np.random.randint(6,36)

            elif self.DATASET.loc[i,"Predicted Grade"] == '91 - 100':
                self.DATASET.loc[i,"Predicted Dropout"] = False
                self.DATASET.loc[i,"Grade"] = int(random.triangular(70,95,100))
                self.DATASET.loc[i,"Cluster"] = 2
                self.COUNTDATA.loc[0,"91 - 100"] += 1

                self.DATASET.loc[i,"AVA Access"] = np.random.randint(80,101)
                self.DATASET.loc[i,"Forum Post"] = np.random.randint(10,41)
                self.DATASET.loc[i,"Forum Replies"] = np.random.randint(10,41)
                self.DATASET.loc[i,"Forum Add Thread"] = np.random.randint(3,14)
                self.DATASET.loc[i,"Forum Access"] =  self.DATASET.loc[i,"Forum Post"] + self.DATASET.loc[i,"Forum Replies"] + self.DATASET.loc[i,"Forum Add Thread"] + np.random.randint(10,41)



    def graph_11(self):
        df = self.DATASET

        trace = Table(
            header=dict(
                values=list(df.columns[:len(df.columns)-1]),
                fill = dict(color='#C2D4FF'),
                align = 'center'
            ),
            cells=dict(
                values=[df[i].tolist() for i in df.columns[:len(df.columns)-1]],
                fill = dict(color='#F5F8FF'),
                align = ['left','center']
            )
        )

        data = [trace]
        if self._type_result == "jupyter-notebook":
            iplot(data, filename = 'pandas_table')
        elif self._type_result == "dash":
            return dcc.Graph(
                id='V011@1',
                figure={"data": data}
            )


    def graph_01(self):
        df = self.DATASET

        trace = Table(
            header=dict(
                values=list(df.columns[:len(df.columns)-1]),
                fill = dict(color='#C2D4FF'),
                align = 'center'
            ),
            cells=dict(
                values=[df[i].tolist() for i in df.columns[:len(df.columns)-1]],
                fill = dict(color='#F5F8FF'),
                align = ['left','center']
            )
        )

        data = [trace]
        if self._type_result == "jupyter-notebook":
            iplot(data, filename = 'pandas_table')
        elif self._type_result == "dash":
            return dcc.Graph(
                id='V011@1',
                figure={"data": data}
            )


    def graph_02(self):
        legend = {"title":"Variação de notas dos estudantes e acesso no AVA",
                    "xaxis":"Acesso ao AVA",
                    "yaxis":"Notas",
                }
        if (self._language == "en"):
            legend = {"title":"Students' grades variation versus VLE' access",
                        "xaxis":"AVA Access",
                        "yaxis":"Grade",
                    }
        color = ["rgb(198, 218, 32)","rgb(121,64,64)","rgb(0,0,204)"]
        trace = []
        for i in range(0, self.NUMBER_STUDENTS):
            trace.append(
                Scatter(
                    x=[self.DATASET["AVA Access"][i]],
                    y=[self.DATASET["Grade"][i]],
                    mode='markers',
                    name=self.DATASET.Students[i], #each student name
                    text = [str(self.DATASET.Students[i])],
                    #text = (self.DATASET["Predicted Grade"][i]),

                    marker=dict(
                        size=12,
                        symbol=self.DATASET.Cluster[i],
                        color = color[int(self.DATASET.Cluster[i])],
                        line=dict(
                            width=2
                        )
                    )
                )
            )

        layout = Layout(
            title=legend['title'],
            hovermode = "closest",
            showlegend = True,
            xaxis = dict(
                title = legend["xaxis"],
                titlefont=dict(
                    # family='Arial, sans-serif',
                    # size=18,
                    color='rgb(180,180,180)',
                ),
                autorange = True,
                zeroline= False,
                showline = True,
            ),
            yaxis = dict(
                title = legend["yaxis"],
                titlefont=dict(
                    # family='Arial, sans-serif',
                    # size=18,
                    color='rgb(180,180,180)',
                ),
                autorange = False,
                fixedrange = True,
                range = [0, self.DATASET.Grade.max()+10],
                rangemode = "normal",
                showline = True,
            )
        )

        data = trace
        fig = Figure(data=data, layout=layout)
        if self._type_result == "jupyter-notebook":
            iplot(fig, filename='Scatter')
        elif self._type_result == "dash":
            return dcc.Graph(
                id='V011@2',
                figure=fig
            )

    # Box
    def graph_03(self):
        legend = {"title":"Variação de notas dos estudantes por cluster",
                    "xaxis":"",
                    "yaxis":"Notas",
                }
        if (self._language == "en"):
            legend = {"title":"Students' grades variation by cluster",
                        "xaxis":"",
                        "yaxis":"Grades",
                    }
        df = self.DATASET.sort_values(by="Grade")
        Clusters = df.Cluster.unique()
        color = ["rgb(198, 218, 32)","rgb(121,64,64)","rgb(0,0,204)"]
        # print(Clusters)
        trace = []
        for i in range(0,len(Clusters)):
            trace.append(
                Box(
                    y=df.Grade.loc[df['Cluster']==Clusters[i]].values.tolist(), #Access
                    name="Cluster "+str(i+1),
                    text=df["Students"].loc[df['Cluster']==Clusters[i]].values.tolist(),
                    boxpoints = 'all',
                    marker=dict(
                        color = color[i],
                        line=dict(
                            width=1
                        )
                    ),
                    boxmean=True
                )
            )

        layout = Layout(
            title=legend['title'],
            # hovermode = "closest",
            showlegend = True,
            xaxis = dict(
                title = legend["xaxis"],
                titlefont=dict(
                    # family='Arial, sans-serif',
                    # size=18,
                    color='rgb(180,180,180)',
                ),
            ),
            yaxis = dict(
                title = legend["yaxis"],
                titlefont=dict(
                    # family='Arial, sans-serif',
                    # size=18,
                    color='rgb(180,180,180)',
                ),
                fixedrange = False,
                range = [-1, self.DATASET.Grade.max()+10],
                rangemode = "normal",
                # showline = True,
                zeroline = False,
            )
        )

        data = trace
        fig = Figure(data=data, layout=layout)
        if self._type_result == "jupyter-notebook":
            iplot(fig, filename='Box')
        elif self._type_result == "dash":
            return dcc.Graph(
                id='V005@9',
                figure=fig
            )

    # Violin
    def graph_04(self):
        legend = {"title":"Variação de notas dos estudantes por cluster",
                    "xaxis":"",
                    "yaxis":"Notas",
                }
        if (self._language == "en"):
            legend = {"title":"Students' grades variation by cluster",
                        "xaxis":"",
                        "yaxis":"Grades",
                    }
        # https://plot.ly/python/violin/#reference
        # https://plot.ly/python/reference/#violin
        df = self.DATASET.sort_values(by="Grade")
        Clusters = df.Cluster.unique()
        color = ["rgb(198, 218, 32)","rgb(121,64,64)","rgb(0,0,204)"]
        # print(Clusters)
        trace = []
        for i in range(0,len(Clusters)):
            trace.append(
                {
                    "type":'violin',
                    "x":["Cluster "+str(i+1)]*len(df.Grade.loc[df['Cluster']==Clusters[i]]),
                    "y":df.Grade.loc[df['Cluster']==Clusters[i]],
                    "name":"Cluster "+str(i+1),
                    "text":df["Students"].loc[df['Cluster']==Clusters[i]].values.tolist(),
                    "box":{
                        "visible":True
                        },
                    "points": 'all',
                    "meanline":{
                        "visible":True
                        },
                    "line":{
                        "color":color[i],
                    },
                    "marker": {
                        "line": {
                            "width": 1,
                        }
                    },
                }
            )

        layout = Layout(
            title=legend['title'],
            hovermode = "closest",
            showlegend = True,
            xaxis = dict(
                title = legend["xaxis"],
                titlefont=dict(
                    # family='Arial, sans-serif',
                    # size=18,
                    color='rgb(180,180,180)',
                ),
            ),
            yaxis = dict(
                title = legend["yaxis"],
                titlefont=dict(
                    # family='Arial, sans-serif',
                    # size=18,
                    color='rgb(180,180,180)',
                ),
                fixedrange = False,
                range = [-15, self.DATASET.Grade.max()+10],
                rangemode = "normal",
                zeroline = False,
            )
        )

        data = trace
        fig = Figure(data=data, layout=layout)
        if self._type_result == "jupyter-notebook":
            iplot(fig, filename='Violin')
        elif self._type_result == "dash":
            return dcc.Graph(
                id='V005@17',
                figure=fig
            )


    def graph_10(self):
        x = [1]
        trace1 = {
          'x': [1],
          'y': [-(self.COUNTDATA["Dropout"][0])],
          'name': 'Dropout',
          'type': 'bar'
        };

        trace2 = {
          'x': x,
          'y': [self.COUNTDATA["0 - 60"][0]],
          'name': '0 - 60',
          'type': 'bar'
        };

        trace3 = {
          'x': x,
          'y': [self.COUNTDATA["61 - 70"][0]],
          'name': '61 - 70',
          'type': 'bar'
          };
        trace4 = {
           'x': x,
           'y': [self.COUNTDATA["71 - 80"][0]],
           'name': '71 - 80',
           'type': 'bar'
          };

        trace5 = {
            'x': x,
            'y': [self.COUNTDATA["81 - 90"][0]],
            'name': '81 - 90',
            'type': 'bar'
           };
        trace6 = {
             'x': x,
             'y': [self.COUNTDATA["91 - 100"][0]],
             'name': '91 - 100',
             'type': 'bar'
            }


        data = [trace1, trace2, trace3, trace4, trace5, trace6];
        layout = {
          'xaxis': {'title': 'X axis'},
          'yaxis': {'title': 'Y axis'},
          'barmode': 'relative',
          'title': 'Alterar'
        };


        plotly.offline.iplot({'data': data, 'layout': layout}, filename='barmode-relative')

    def graph_12(self):
        legend = {"title":"--",
                    "xaxis":"Grade",
                    "yaxis":"Grade",
                }
        if (self._language == "en"):
            legend = {"title":"--",
                        "xaxis":"Predicted Grade",
                        "yaxis":"Grade",
                    }
        color = ["rgb(127,0,0)","rgb(255,0,0)","rgb(127,0,127)","rgb(0,0,255)","rgb(0,127,127)","rgb(0,255,0)"]
        trace = []
        for i in range(0, self.NUMBER_STUDENTS):
            trace.append(
                Scatter(
                    x=[self.DATASET["Predicted Grade"][i]],
                    y=[self.DATASET["Grade"][i]],
                    mode='markers',
                    name=self.DATASET.Students[i], #each student name
                    text = [str(self.DATASET.Students[i])],
                )
            )

        layout = Layout(
            title=legend['title'],
            hovermode = "closest",
            showlegend = True,
            xaxis = dict(
                type='category',
                title = legend["xaxis"],
                titlefont=dict(
                    # family='Arial, sans-serif',
                    # size=18,
                    color='rgb(180,180,180)',
                ),
                rangemode = 'normal',
                zeroline= False,
                showline = True,
            ),
            yaxis = dict(
                title = legend["yaxis"],
                titlefont=dict(
                    # family='Arial, sans-serif',
                    # size=18,
                    color='rgb(180,180,180)',
                ),
                autorange = False,
                fixedrange = True,
                range = [0, self.DATASET.Grade.max()+10],
                rangemode = "normal",
                showline = True,
            )
        )

        data = trace
        fig = Figure(data=data, layout=layout)
        if self._type_result == "jupyter-notebook":
            iplot(fig, filename='Scatter')
        elif self._type_result == "dash":
            return dcc.Graph(
                id='V011@2',
                figure=fig
            )

    def graph_05(self):
        return html.Div([
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
                    ])

    def print_all_graphs(self,language="pt"):
        self._language = language
        self.graph_01() #Table
        self.graph_02()
        self.graph_03()
        self.graph_04()
