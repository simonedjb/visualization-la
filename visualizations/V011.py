import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

import visdcc
import random

import plotly
import plotly.plotly as py
import plotly.tools as tls
import plotly.graph_objs as go

import pandas as pd
import numpy as np

import json

from plotly.utils import PlotlyJSONEncoder
from plotly.graph_objs import Figure, Layout, Bar, Table, Heatmap, Scatter, Box, Violin
from plotly.offline import init_notebook_mode, iplot


from sklearn import metrics
from sklearn.cluster import KMeans


init_notebook_mode(connected=True) # initiate notebook for offline plot
plotly.__version__

class V011:
    NUMBER_ACTIONS = 50
    DATASET = pd.DataFrame()


    _language = "pt"
    _type_result="jupyter-notebook"
    _preprocessed_folder = os.path.join('Preprocessed')

    def __init__(self, language="pt", type_result = "jupyter-notebook"):
        self._language = language
        self._type_result = type_result

    def generate_dataset(self, number_students = 20, students_names = pd.DataFrame()):
        self.NUMBER_STUDENTS = number_students

        if len(students_names.columns.tolist()) == 0:
            names = pd.read_csv("assets/names.csv")
        else:
            names = students_names
        rand_names = [names.group_name[np.random.randint(0,len(names.group_name)+1)] for n in range(0,self.NUMBER_STUDENTS)]
        rand_names.sort()


        self.DATASET = pd.DataFrame(columns=["Students","Grade",
        	                                 "AVA Access","Forum Post","Forum Replies","Forum Add Thread","Forum Access", "Cluster"])

        for i in range(0,self.NUMBER_STUDENTS):
            self.DATASET.loc[i,"Students"] = rand_names[i]
            random_value = random.choice([1,2,3,4,5,6])
            if random_value == 1:
                self.DATASET.loc[i,"Grade"] = 0
                self.DATASET.loc[i,"Cluster"] = 0

                self.DATASET.loc[i,"AVA Access"] = np.random.randint(5,26)
                self.DATASET.loc[i,"Forum Post"] = np.random.randint(0,4)
                self.DATASET.loc[i,"Forum Replies"] = np.random.randint(0,4)
                self.DATASET.loc[i,"Forum Add Thread"] = np.random.randint(0,4)
                self.DATASET.loc[i,"Forum Access"] =  self.DATASET.loc[i,"Forum Post"] + self.DATASET.loc[i,"Forum Replies"] + self.DATASET.loc[i,"Forum Add Thread"] + np.random.randint(0,7)

            elif random_value == 2:
                self.DATASET.loc[i,"Grade"] = int(random.triangular(0,30,80))
                self.DATASET.loc[i,"Cluster"] = 0

                self.DATASET.loc[i,"AVA Access"] = np.random.randint(20,41)
                self.DATASET.loc[i,"Forum Post"] = np.random.randint(0,8)
                self.DATASET.loc[i,"Forum Replies"] = np.random.randint(0,8)
                self.DATASET.loc[i,"Forum Add Thread"] = np.random.randint(0,4)
                self.DATASET.loc[i,"Forum Access"] = self.DATASET.loc[i,"Forum Post"] + self.DATASET.loc[i,"Forum Replies"] + self.DATASET.loc[i,"Forum Add Thread"] + np.random.randint(0,22)

            elif random_value == 3:
                self.DATASET.loc[i,"Grade"] = int(random.triangular(50,65,80))
                self.DATASET.loc[i,"Cluster"] = 1

                self.DATASET.loc[i,"AVA Access"] = np.random.randint(35,57)
                self.DATASET.loc[i,"Forum Post"] = np.random.randint(1,12)
                self.DATASET.loc[i,"Forum Replies"] = np.random.randint(0,12)
                self.DATASET.loc[i,"Forum Add Thread"] = np.random.randint(0,8)
                self.DATASET.loc[i,"Forum Access"] =  self.DATASET.loc[i,"Forum Post"] + self.DATASET.loc[i,"Forum Replies"] + self.DATASET.loc[i,"Forum Add Thread"] + np.random.randint(2,26)

            elif random_value == 4:
                self.DATASET.loc[i,"Grade"] = int(random.triangular(60,75,90))
                self.DATASET.loc[i,"Cluster"] = 1

                self.DATASET.loc[i,"AVA Access"] = np.random.randint(50,71)
                self.DATASET.loc[i,"Forum Post"] = np.random.randint(2,21)
                self.DATASET.loc[i,"Forum Replies"] = np.random.randint(2,21)
                self.DATASET.loc[i,"Forum Add Thread"] = np.random.randint(0,7)
                self.DATASET.loc[i,"Forum Access"] =  self.DATASET.loc[i,"Forum Post"] + self.DATASET.loc[i,"Forum Replies"] + self.DATASET.loc[i,"Forum Add Thread"] + np.random.randint(4,31)

            elif random_value == 5:
                self.DATASET.loc[i,"Grade"] = int(random.triangular(70,85,100))
                self.DATASET.loc[i,"Cluster"] = 2

                self.DATASET.loc[i,"AVA Access"] = np.random.randint(65,86)
                self.DATASET.loc[i,"Forum Post"] = np.random.randint(5,36)
                self.DATASET.loc[i,"Forum Replies"] = np.random.randint(5,36)
                self.DATASET.loc[i,"Forum Add Thread"] = np.random.randint(1,11)
                self.DATASET.loc[i,"Forum Access"] =  self.DATASET.loc[i,"Forum Post"] + self.DATASET.loc[i,"Forum Replies"] + self.DATASET.loc[i,"Forum Add Thread"] + np.random.randint(6,36)

            elif random_value == 6:
                self.DATASET.loc[i,"Grade"] = int(random.triangular(70,95,100))
                self.DATASET.loc[i,"Cluster"] = 2

                self.DATASET.loc[i,"AVA Access"] = np.random.randint(80,101)
                self.DATASET.loc[i,"Forum Post"] = np.random.randint(10,41)
                self.DATASET.loc[i,"Forum Replies"] = np.random.randint(10,41)
                self.DATASET.loc[i,"Forum Add Thread"] = np.random.randint(3,14)
                self.DATASET.loc[i,"Forum Access"] =  self.DATASET.loc[i,"Forum Post"] + self.DATASET.loc[i,"Forum Replies"] + self.DATASET.loc[i,"Forum Add Thread"] + np.random.randint(10,41)

    def graph_01(self):
        legend = {"title":"Relação de notas dos estudantes com acessos ao AVA por cluster navegação"}
        if (self._language == "en"):
            legend = {"title":"Relation of student grades with AVA access by navigate cluster"}
        df = self.DATASET

        trace = [Table(
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
        )]

        data = trace
        layout = Layout( title = legend["title"] )
        
        fig = Figure(data=data, layout=layout)
        if self._type_result == "jupyter-notebook":
            iplot(data, filename = 'pandas_table')
        elif self._type_result == "dash":
            return dcc.Graph(
                id='V011@1',
                figure={"data": data}
            )
        elif self._type_result == "flask":
            modeBarButtonsToRemove = ['toImage', 'sendDataToCloud', 'hoverCompareCartesian', 'lasso2d', 'hoverClosestCartesian', 'toggleHover', 'hoverClosest3d', 'hoverClosestGeo', 'hoverClosestGl2d', 'hoverClosestPie']
            config = {"displaylogo": False, "responsive": True, "displayModeBar": True, "modeBarButtonsToRemove": modeBarButtonsToRemove}
            return {"id":"V011@1","layout":json.dumps({"data": data, "layout": layout, "config": config}, cls=PlotlyJSONEncoder)}


    def graph_02(self):
        legend = {"title":"Relação de notas dos estudantes com acessos ao AVA por cluster navegação",
                    "xaxis":"Acesso ao AVA",
                    "yaxis":"Notas",
                }
        if (self._language == "en"):
            legend = {"title":"Relation of student grades with AVA access by navigate cluster",
                        "xaxis":"AVA Access",
                        "yaxis":"Grade",
                    }
        df = self.DATASET.sort_values(by=["Grade"])
        Clusters = df.Cluster.unique()
        color = ["rgb(255,0,0)","rgb(0,0,255)","rgb(0,255,0)"]
        color[Clusters[0]] = "rgb(255,0,0)"
        color[Clusters[1]] = "rgb(0,0,255)"
        color[Clusters[2]] = "rgb(0,255,0)"
        trace = []
        for i in range(0, self.NUMBER_STUDENTS):
            trace.append(
                Scatter(
                    x=[df["AVA Access"][i]], #Access
                    y=[df["Grade"][i]], #Grade
                    mode='markers',
                    name=df.Students[i], #each student name
                    text = [str(df.Students[i])],

                    marker=dict(
                        size=12,
                        symbol=self.DATASET.Cluster[i],
                        color = color[df.Cluster[i]],
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
                autorange = False,
                fixedrange = False,
                range = [0, self.DATASET["AVA Access"].max()+10],
                rangemode = "normal",
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
                fixedrange = False,
                range = [0, self.DATASET["Grade"].max()+10],
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
        elif self._type_result == "flask":
            modeBarButtonsToRemove = ['toImage', 'sendDataToCloud', 'hoverCompareCartesian', 'lasso2d', 'hoverClosestCartesian', 'toggleHover', 'hoverClosest3d', 'hoverClosestGeo', 'hoverClosestGl2d', 'hoverClosestPie']
            config = {"displaylogo": False, "responsive": True, "displayModeBar": True, "modeBarButtonsToRemove": modeBarButtonsToRemove}
            return {"id":"V011@2","layout":json.dumps({"data": data, "layout": layout, "config": config}, cls=PlotlyJSONEncoder)}

    # Box
    def graph_03(self):
        legend = {"title":"Variação de notas dos estudantes por cluster de navegação",
                    "xaxis":"",
                    "yaxis":"Notas",
                }
        if (self._language == "en"):
            legend = {"title":"Student grades variation by navigate cluster",
                        "xaxis":"",
                        "yaxis":"Grades",
                    }
        df = self.DATASET.sort_values(by="Grade")
        Clusters = df.Cluster.unique()
        color = ["rgb(198, 218, 32)","rgb(121,64,64)","rgb(0,0,204)"]
        color = ["rgb(255,0,0)","rgb(0,0,255)","rgb(0,255,0)"]
        # print(Clusters)
        trace = []
        for i in range(0,len(Clusters)):
            trace.append(
                Box(
                    y=df["Grade"].loc[df['Cluster']==Clusters[i]].values.tolist(), #Access
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
                range = [-1, self.DATASET["Grade"].max()+10],
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
                id='V011@3',
                figure=fig
            )
        elif self._type_result == "flask":
            modeBarButtonsToRemove = ['toImage', 'sendDataToCloud', 'hoverCompareCartesian', 'lasso2d', 'hoverClosestCartesian', 'toggleHover', 'hoverClosest3d', 'hoverClosestGeo', 'hoverClosestGl2d', 'hoverClosestPie']
            config = {"displaylogo": False, "responsive": True, "displayModeBar": True, "modeBarButtonsToRemove": modeBarButtonsToRemove}
            return {"id":"V011@3","layout":json.dumps({"data": data, "layout": layout, "config": config}, cls=PlotlyJSONEncoder)}

    # Violin
    def graph_04(self):
        legend = {"title":"Variação de notas dos estudantes por cluster de navegação",
                    "xaxis":"",
                    "yaxis":"Notas",
                }
        if (self._language == "en"):
            legend = {"title":"Student grades variation by navigate cluster",
                        "xaxis":"",
                        "yaxis":"Grades",
                    }
        # https://plot.ly/python/violin/#reference
        # https://plot.ly/python/reference/#violin
        df = self.DATASET.sort_values(by="Grade")
        Clusters = df.Cluster.unique()
        color = ["rgb(255,0,0)","rgb(0,0,255)","rgb(0,255,0)"]
        color[Clusters[0]] = "rgb(255,0,0)"
        color[Clusters[1]] = "rgb(0,0,255)"
        color[Clusters[2]] = "rgb(0,255,0)"
        # print(Clusters)
        trace = []
        for i in range(0,len(Clusters)):
            trace.append(
                {
                    "type":'violin',
                    "x":["Cluster "+str(i+1)]*len(df["Grade"].loc[df['Cluster']==Clusters[i]]),
                    "y":df["Grade"].loc[df['Cluster']==Clusters[i]],
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
                range = [-15, self.DATASET["Grade"].max()+10],
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
                id='V011@4',
                figure=fig
            )
        elif self._type_result == "flask":
            modeBarButtonsToRemove = ['toImage', 'sendDataToCloud', 'hoverCompareCartesian', 'lasso2d', 'hoverClosestCartesian', 'toggleHover', 'hoverClosest3d', 'hoverClosestGeo', 'hoverClosestGl2d', 'hoverClosestPie']
            config = {"displaylogo": False, "responsive": True, "displayModeBar": True, "modeBarButtonsToRemove": modeBarButtonsToRemove}
            return {"id":"V011@4","layout":json.dumps({"data": data, "layout": layout, "config": config}, cls=PlotlyJSONEncoder)}

    #Flow Chart
    def graph_05(self):
        legend = {"title":"Fluxo de navegação dos estudantes por cluster"}
        if (self._language == "en"):
            legend = {"title":"Students' navigation flow by cluster"}

        markerSize = 90
        mark_cluster = ["Inicio do Curso", "Fim do Curso"]        

        cluster = []
        cluster.append(['Video 1','Video 2','Video 3','Final Test'])
        cluster.append(['Video 1','Video 2','Video 3','Assignment 1','Assignment 2','Assignment 3','Final Test'])
        cluster.append(['Video 1','Video 2','Video 3','Assignment 1','Assignment 2','Assignment 3','Forum','Final Test'])

        x = []
        y = []        
        x.append([1,2,3,4]) #cluster1
        y.append([120,120,120,120,120]) #cluster1        

        x.append([1, 2, 3, 1.5, 2.5, 3.5, 4]) #cluster2
        y.append([80, 100, 100, 60, 60, 60, 80]) #cluster2        

        x.append([1, 2, 3, 1.5, 2.5, 3.5, 1.5, 4]) #cluster3
        y.append([20, 20, 20, 0, 0, 0, 40, 20]) #cluster3

        color = ["rgba(255,0,0,1)","rgba(0,0,255,1)","rgba(0,255,0,1)"]
        text_color = ["rgb(255,255,255)","rgb(255,255,255)","rgb(0,0,0)"]

        trace = []
        for i in range(0,len(cluster)):
            trace.append(
                    Scatter(
                        x=x[i],
                        y=y[i],
                        mode='markers+text',
                        name="Cluster"+str(i+1), #each cluster name
                        text = cluster[i],
                        textposition='middle center',
                        hoverinfo='none',
                        showlegend = False,
                        marker=dict(size=[markerSize]*len(cluster[i]), color = color[i], symbol='circle-open', line=dict(width=3))
                    )
                )
            
            trace.append(
                    Scatter(
                        x=[x[i][0]-1, x[i][len(x[i])-1]+1],
                        y=[y[i][0]-1, y[i][len(y[i])-1]+1],
                        mode='markers+text',
                        text = mark_cluster,
                        textposition='middle center',                        
                        textfont=dict(
                            # family="sans serif",
                            # size=18,
                            color=text_color[i]
                        ),
                        hoverinfo='none',
                        showlegend = False,
                        marker=dict(size=[markerSize]*len(mark_cluster), color = color[i], symbol='circle')
                    )

                )

            trace.append(
                    Scatter(
                        x=[x[i][0]-1.5],
                        y=[y[i][0]-1.5],
                        mode='markers+text',
                        text = ["Cluster "+str(i+1)],
                        textposition='middle center',
                        textfont=dict(
                            # family="sans serif",
                            # size=18,
                            color=text_color[i]
                        ),
                        hoverinfo='none',
                        showlegend = False,
                        marker=dict(size=[markerSize/1.5]*len(mark_cluster), color = color[i], symbol='square')
                    )

                )
            

        # Edges
        x0 = []
        x1 = []
        y0 = []
        y1 = []

        width = []

        xshift = []
        yshift = []
        
        #cluster1
        # cluster.append(['Video 1','Video 2','Video 3','Final Test'])
        x0.append([x[0][cluster[0].index('Video 1')]-1, x[0][cluster[0].index('Video 1')], x[0][cluster[0].index('Video 2')], x[0][cluster[0].index('Video 3')],    x[0][cluster[0].index('Final Test')]])
        x1.append([x[0][cluster[0].index('Video 1')]   ,x[0][cluster[0].index('Video 2')], x[0][cluster[0].index('Video 3')], x[0][cluster[0].index('Final Test')], x[0][cluster[0].index('Final Test')]+1])
        y0.append([y[0][cluster[0].index('Video 1')]-1, y[0][cluster[0].index('Video 1')], y[0][cluster[0].index('Video 2')], y[0][cluster[0].index('Video 3')],    y[0][cluster[0].index('Final Test')]])
        y1.append([y[0][cluster[0].index('Video 1')]  , y[0][cluster[0].index('Video 2')], y[0][cluster[0].index('Video 3')], y[0][cluster[0].index('Final Test')], y[0][cluster[0].index('Final Test')]+1])

        width.append([10, 9, 6, 5, 5])

        xshift.append([0,0,0,0,0])
        yshift.append([0,0,0,0,0])

        #cluster2
        # cluster.append(['Video 1','Video 2','Video 3','Assignment 1','Assignment 2','Assignment 3','Final Test'])
        x0.append([x[1][cluster[1].index('Video 1')]-1, x[1][cluster[1].index('Video 1')], x[1][cluster[1].index('Video 1')],      x[1][cluster[1].index('Video 2')], x[1][cluster[1].index('Video 2')],      x[1][cluster[1].index('Video 3')], x[1][cluster[1].index('Assignment 1')], x[1][cluster[1].index('Assignment 2')], x[1][cluster[1].index('Assignment 3')], x[1][cluster[1].index('Video 3')],    x[1][cluster[1].index('Final Test')]])
        x1.append([x[1][cluster[1].index('Video 1')],   x[1][cluster[1].index('Video 2')], x[1][cluster[1].index('Assignment 1')], x[1][cluster[1].index('Video 3')], x[1][cluster[1].index('Assignment 2')], x[1][cluster[1].index('Assignment 3')], x[1][cluster[1].index('Video 2')], x[1][cluster[1].index('Video 3')],      x[1][cluster[1].index('Final Test')],   x[1][cluster[1].index('Final Test')], x[1][cluster[1].index('Final Test')]+1])
        y0.append([y[1][cluster[1].index('Video 1')]-1, y[1][cluster[1].index('Video 1')], y[1][cluster[1].index('Video 1')],      y[1][cluster[1].index('Video 2')], y[1][cluster[1].index('Video 2')],      y[1][cluster[1].index('Video 3')], y[1][cluster[1].index('Assignment 1')], y[1][cluster[1].index('Assignment 2')], y[1][cluster[1].index('Assignment 3')], y[1][cluster[1].index('Video 3')],    y[1][cluster[1].index('Final Test')]])
        y1.append([y[1][cluster[1].index('Video 1')],   y[1][cluster[1].index('Video 2')], y[1][cluster[1].index('Assignment 1')], y[1][cluster[1].index('Video 3')], y[1][cluster[1].index('Assignment 2')], y[1][cluster[1].index('Assignment 3')], y[1][cluster[1].index('Video 2')], y[1][cluster[1].index('Video 3')],      y[1][cluster[1].index('Final Test')],   y[1][cluster[1].index('Final Test')], y[1][cluster[1].index('Final Test')]+1])

        width.append([9, 4, 8, 3, 7, 6, 5, 7, 6, 4, 10])

        xshift.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        yshift.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

        #cluster3
        # cluster.append(['Video 1','Video 2','Video 3','Assignment 1','Assignment 2','Assignment 3','Forum','Final Test'])
        x0.append([x[2][cluster[2].index('Video 1')]-1, x[2][cluster[2].index('Video 1')]-1,    x[2][cluster[2].index('Video 1')], x[2][cluster[2].index('Video 1')],      x[2][cluster[2].index('Forum')],   x[2][cluster[2].index('Video 2')], x[2][cluster[2].index('Video 2')],      x[2][cluster[2].index('Video 3')],      x[2][cluster[2].index('Video 3')],    x[2][cluster[2].index('Assignment 1')], x[2][cluster[2].index('Assignment 1')], x[2][cluster[2].index('Assignment 2')], x[2][cluster[2].index('Assignment 2')], x[2][cluster[2].index('Assignment 3')], x[2][cluster[2].index('Assignment 3')], x[2][cluster[2].index('Final Test')]])
        x1.append([x[2][cluster[2].index('Video 1')],   x[2][cluster[2].index('Assignment 1')], x[2][cluster[2].index('Forum')],   x[2][cluster[2].index('Assignment 1')], x[2][cluster[2].index('Video 2')], x[2][cluster[2].index('Video 3')], x[2][cluster[2].index('Assignment 2')], x[2][cluster[2].index('Assignment 3')], x[2][cluster[2].index('Final Test')], x[2][cluster[2].index('Video 1')],      x[2][cluster[2].index('Video 2')],      x[2][cluster[2].index('Video 2')],      x[2][cluster[2].index('Video 3')],      x[2][cluster[2].index('Video 3')],      x[2][cluster[2].index('Final Test')],   x[2][cluster[2].index('Final Test')]+1])
        y0.append([y[2][cluster[2].index('Video 1')]-1, y[2][cluster[2].index('Video 1')]-1,    y[2][cluster[2].index('Video 1')], y[2][cluster[2].index('Video 1')],      y[2][cluster[2].index('Forum')],   y[2][cluster[2].index('Video 2')], y[2][cluster[2].index('Video 2')],      y[2][cluster[2].index('Video 3')],      y[2][cluster[2].index('Video 3')],    y[2][cluster[2].index('Assignment 1')], y[2][cluster[2].index('Assignment 1')], y[2][cluster[2].index('Assignment 2')], y[2][cluster[2].index('Assignment 2')], y[2][cluster[2].index('Assignment 3')], y[2][cluster[2].index('Assignment 3')], y[2][cluster[2].index('Final Test')]])
        y1.append([y[2][cluster[2].index('Video 1')],   y[2][cluster[2].index('Assignment 1')], y[2][cluster[2].index('Forum')],   y[2][cluster[2].index('Assignment 1')], y[2][cluster[2].index('Video 2')], y[2][cluster[2].index('Video 3')], y[2][cluster[2].index('Assignment 2')], y[2][cluster[2].index('Assignment 3')], y[2][cluster[2].index('Final Test')], y[2][cluster[2].index('Video 1')],      y[2][cluster[2].index('Video 2')],      y[2][cluster[2].index('Video 2')],      y[2][cluster[2].index('Video 3')],      y[2][cluster[2].index('Video 3')],      y[2][cluster[2].index('Final Test')],   y[2][cluster[2].index('Final Test')]+1])

        width.append([9, 3, 2, 5, 2, 2, 5, 5, 2, 3, 5, 2, 5, 2, 5, 7])

        xshift.append([0, -10, 0, 15, 0, 0, 15, 15, 0, -10, 0, -10, 0, -10, 0, 0])
        yshift.append([0, -15, 0, 10, 0, 0, 10, 10, 0, -10, 0, -10, 0, -10, 0, 0])
        
        annotations = []        
        for i in range(0,len(x0)):
            for j in range(0,len(x0[i])):
                annotations.append(
                    dict(ax=x0[i][j], ay=y0[i][j], axref='x', ayref='y',
                            x=x1[i][j], y=y1[i][j], xref='x', yref='y',
                            xshift = xshift[i][j], yshift = yshift[i][j],
                            startstandoff=markerSize/1.8,standoff=markerSize/1.8,
                            arrowcolor=color[i],arrowwidth=width[i][j],arrowsize=1,
                            showarrow=True, arrowhead=3,)
                )

        layout=Layout(
                title = legend["title"],
                autosize=True,
                # width=1500,
                height=1250,
                hovermode='closest',
                xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                annotations = annotations                
            )

        data = trace
        fig = Figure(data=data, layout=layout)
        # iplot(fig, filename='Scatter')
        if self._type_result == "jupyter-notebook":
            iplot(fig, filename='Scatter')
        elif self._type_result == "dash":
            return dcc.Graph(
                id='V011@5',
                figure=fig
            )
        elif self._type_result == "flask":
            modeBarButtonsToRemove = ['toImage', 'sendDataToCloud', 'hoverCompareCartesian', 'lasso2d', 'hoverClosestCartesian', 'toggleHover', 'hoverClosest3d', 'hoverClosestGeo', 'hoverClosestGl2d', 'hoverClosestPie']
            config = {"displaylogo": False, "responsive": True, "displayModeBar": True, "modeBarButtonsToRemove": modeBarButtonsToRemove}
            return {"id":"V011@5","layout":json.dumps({"data": data, "layout": layout, "config": config}, cls=PlotlyJSONEncoder)}

    def get_chart(self,id):
        if id == 1:
            return self.graph_01()
        elif id == 2:
            return self.graph_02()
        elif id == 3:
            return self.graph_03()
        elif id == 4:
            return self.graph_04()
        elif id == 5:
            return self.graph_05()
        else:
            print("V011@"+str(id)+" not found")

    def get_preprocessed_chart(self,id):
        if not os.path.exists(self._preprocessed_folder):
            print('There is no preprocessed folder')
            return
        
        file_name = 'V011_'+str(id)+'.pkl'
        file_path = os.path.join(self._preprocessed_folder,file_name)

        if not os.path.exists(file_path):
            print('There is no preprocessed chart')
            return

        f = open(file_path,'rb')
        data = pickle.load(f)
        f.close()
        
        return data

    def save_chart(self,id):
        aux_type_result = self._type_result
        self._type_result = "flask"
        
        if not os.path.exists(self._preprocessed_folder):
            os.mkdir(self._preprocessed_folder)
        
        file_name = 'V011_'+str(id)+'.pkl'
        file_path = os.path.join(self._preprocessed_folder,file_name)
        f = open(file_path,'wb')
        pickle.dump(self.get_chart(id),f)
        f.close()

        self._type_result = aux_type_result

    def print_all_graphs(self,language="pt"):
        self._language = language
        self.graph_01() #Table
        self.graph_02() #Scatter
        self.graph_03() #Box
        self.graph_04() #Violin
        self.graph_05() #Flow Chart