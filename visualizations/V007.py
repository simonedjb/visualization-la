import dash
import dash_core_components as dcc
import dash_html_components as html
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

class V007:
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


        self.DATASET = pd.DataFrame(columns=["Students","Predicted Cluster","Predicted Dropout","Predicted Grade",
        	                                 "AVA Access","Forum Post","Forum Replies","Forum Add Thread","Forum Access", "Cluster"])

        for i in range(0,self.NUMBER_STUDENTS):
            self.DATASET.loc[i,"Students"] = rand_names[i]
            self.DATASET.loc[i,"Predicted Cluster"] = random.choice(['Dropout','0 - 60','61 - 70', '71 - 80', '81 - 90', '91 - 100'])
            if self.DATASET.loc[i,"Predicted Cluster"] == 'Dropout':
                self.DATASET.loc[i,"Predicted Dropout"] = True
                self.DATASET.loc[i,"Predicted Grade"] = np.random.randint(0,5)
                self.DATASET.loc[i,"Cluster"] = 0

                self.DATASET.loc[i,"AVA Access"] = np.random.randint(5,26)
                self.DATASET.loc[i,"Forum Post"] = np.random.randint(0,4)
                self.DATASET.loc[i,"Forum Replies"] = np.random.randint(0,4)
                self.DATASET.loc[i,"Forum Add Thread"] = np.random.randint(0,4)
                self.DATASET.loc[i,"Forum Access"] =  self.DATASET.loc[i,"Forum Post"] + self.DATASET.loc[i,"Forum Replies"] + self.DATASET.loc[i,"Forum Add Thread"] + np.random.randint(0,7)

            elif self.DATASET.loc[i,"Predicted Cluster"] == '0 - 60':
                self.DATASET.loc[i,"Predicted Dropout"] = False
                self.DATASET.loc[i,"Predicted Grade"] = int(random.triangular(0,30,60))
                self.DATASET.loc[i,"Cluster"] = 1
                self.COUNTDATA.loc[0,"0 - 60"] += 1

                self.DATASET.loc[i,"AVA Access"] = np.random.randint(20,41)
                self.DATASET.loc[i,"Forum Post"] = np.random.randint(0,8)
                self.DATASET.loc[i,"Forum Replies"] = np.random.randint(0,8)
                self.DATASET.loc[i,"Forum Add Thread"] = np.random.randint(0,4)
                self.DATASET.loc[i,"Forum Access"] = self.DATASET.loc[i,"Forum Post"] + self.DATASET.loc[i,"Forum Replies"] + self.DATASET.loc[i,"Forum Add Thread"] + np.random.randint(0,22)

            elif self.DATASET.loc[i,"Predicted Cluster"] == '61 - 70':
                self.DATASET.loc[i,"Predicted Dropout"] = False
                self.DATASET.loc[i,"Predicted Grade"] = int(random.triangular(61,65,70))
                self.DATASET.loc[i,"Cluster"] = 2
                self.COUNTDATA.loc[0,"61 - 70"] += 1

                self.DATASET.loc[i,"AVA Access"] = np.random.randint(35,57)
                self.DATASET.loc[i,"Forum Post"] = np.random.randint(1,12)
                self.DATASET.loc[i,"Forum Replies"] = np.random.randint(0,12)
                self.DATASET.loc[i,"Forum Add Thread"] = np.random.randint(0,8)
                self.DATASET.loc[i,"Forum Access"] =  self.DATASET.loc[i,"Forum Post"] + self.DATASET.loc[i,"Forum Replies"] + self.DATASET.loc[i,"Forum Add Thread"] + np.random.randint(2,26)

            elif self.DATASET.loc[i,"Predicted Cluster"] == '71 - 80':
                self.DATASET.loc[i,"Predicted Dropout"] = False
                self.DATASET.loc[i,"Predicted Grade"] = int(random.triangular(71,75,80))
                self.DATASET.loc[i,"Cluster"] = 3
                self.COUNTDATA.loc[0,"71 - 80"] += 1

                self.DATASET.loc[i,"AVA Access"] = np.random.randint(50,71)
                self.DATASET.loc[i,"Forum Post"] = np.random.randint(2,21)
                self.DATASET.loc[i,"Forum Replies"] = np.random.randint(2,21)
                self.DATASET.loc[i,"Forum Add Thread"] = np.random.randint(0,7)
                self.DATASET.loc[i,"Forum Access"] =  self.DATASET.loc[i,"Forum Post"] + self.DATASET.loc[i,"Forum Replies"] + self.DATASET.loc[i,"Forum Add Thread"] + np.random.randint(4,31)

            elif self.DATASET.loc[i,"Predicted Cluster"] == '81 - 90':
                self.DATASET.loc[i,"Predicted Dropout"] = False
                self.DATASET.loc[i,"Predicted Grade"] = int(random.triangular(81,85,90))
                self.DATASET.loc[i,"Cluster"] = 4
                self.COUNTDATA.loc[0,"81 - 90"] += 1

                self.DATASET.loc[i,"AVA Access"] = np.random.randint(65,86)
                self.DATASET.loc[i,"Forum Post"] = np.random.randint(5,36)
                self.DATASET.loc[i,"Forum Replies"] = np.random.randint(5,36)
                self.DATASET.loc[i,"Forum Add Thread"] = np.random.randint(1,11)
                self.DATASET.loc[i,"Forum Access"] =  self.DATASET.loc[i,"Forum Post"] + self.DATASET.loc[i,"Forum Replies"] + self.DATASET.loc[i,"Forum Add Thread"] + np.random.randint(6,36)

            elif self.DATASET.loc[i,"Predicted Cluster"] == '91 - 100':
                self.DATASET.loc[i,"Predicted Dropout"] = False
                self.DATASET.loc[i,"Predicted Grade"] = int(random.triangular(91,95,100))
                self.DATASET.loc[i,"Cluster"] = 5
                self.COUNTDATA.loc[0,"91 - 100"] += 1

                self.DATASET.loc[i,"AVA Access"] = np.random.randint(80,101)
                self.DATASET.loc[i,"Forum Post"] = np.random.randint(10,41)
                self.DATASET.loc[i,"Forum Replies"] = np.random.randint(10,41)
                self.DATASET.loc[i,"Forum Add Thread"] = np.random.randint(3,14)
                self.DATASET.loc[i,"Forum Access"] =  self.DATASET.loc[i,"Forum Post"] + self.DATASET.loc[i,"Forum Replies"] + self.DATASET.loc[i,"Forum Add Thread"] + np.random.randint(10,41)

    def graph_01(self):
        legend = {"title":"Previsão das notas relacionado com o número de acessos no AVA"}
        if (self._language == "en"):
            legend = {"title":"Predicted grades related with the number of VLE access"}
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
                id='V007@1',
                figure={"data": data}
            )
        elif self._type_result == "flask":
            modeBarButtonsToRemove = ['toImage', 'sendDataToCloud', 'hoverCompareCartesian', 'lasso2d', 'hoverClosestCartesian', 'toggleHover', 'hoverClosest3d', 'hoverClosestGeo', 'hoverClosestGl2d', 'hoverClosestPie']
            config = {"displaylogo": False, "responsive": True, "displayModeBar": True, "modeBarButtonsToRemove": modeBarButtonsToRemove}
            return {"id":"V007@1","layout":json.dumps({"data": data, "layout": layout, "config": config}, cls=PlotlyJSONEncoder)}

    # Scatter
    def graph_02(self):
        legend = {"title":"Previsão das notas relacionado com o número de acessos no AVA",
                    "xaxis":"Acesso ao AVA",
                    "yaxis":"Previsão das Notas",
                }
        if (self._language == "en"):
            legend = {"title":"Predicted grades related with the number of VLE access",
                        "xaxis":"AVA Access",
                        "yaxis":"Predicted Grades",
                    }
        
        df = self.DATASET.sort_values(by=["Predicted Grade"])
        Clusters = df.Cluster.unique()
        color = ["rgb(100,100,100)","rgb(255,0,0)","rgb(127,0,127)","rgb(0,0,255)","rgb(0,127,127)","rgb(0,255,0)"]
        color[Clusters[0]] = "rgb(100,100,100)"
        color[Clusters[1]] = "rgb(255,0,0)"
        color[Clusters[2]] = "rgb(127,0,127)"
        color[Clusters[3]] = "rgb(0,0,255)"
        color[Clusters[4]] = "rgb(0,127,127)"
        color[Clusters[5]] = "rgb(0,255,0)"

        trace = []
        for i in range(0, self.NUMBER_STUDENTS):
            # print(df.Students[i])
            trace.append(
                Scatter(
                    x=[df["AVA Access"][i]], #Access
                    y=[df["Predicted Grade"][i]], #Grade
                    mode='markers',
                    name=df.Students[i], #each student name
                    text = [str(df.Students[i])],
                    marker=dict(
                        size=12,
                        symbol=df.Cluster[i],
                        color = color[df.Cluster[i]],
                        colorscale='Viridis',
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
                range = [0, self.DATASET["Predicted Grade"].max()+10],
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
                id='V007@2',
                figure=fig
            )
        elif self._type_result == "flask":
            modeBarButtonsToRemove = ['toImage', 'sendDataToCloud', 'hoverCompareCartesian', 'lasso2d', 'hoverClosestCartesian', 'toggleHover', 'hoverClosest3d', 'hoverClosestGeo', 'hoverClosestGl2d', 'hoverClosestPie']
            config = {"displaylogo": False, "responsive": True, "displayModeBar": True, "modeBarButtonsToRemove": modeBarButtonsToRemove}
            return {"id":"V007@2","layout":json.dumps({"data": data, "layout": layout, "config": config}, cls=PlotlyJSONEncoder)}

    # Box
    def graph_03(self):
        legend = {"title":"Variação da previsão de notas dos estudantes por cluster",
                    "xaxis":"",
                    "yaxis":"Previsão das Notas",
                    "cluster":["Desistentes",'Notas entre 0 e 60','Notas entre 61 e 70', 'Notas entre 71 e 80', 'Notas entre 81 e 90', 'Notas entre 91 e 100']
                }
        if (self._language == "en"):
            legend = {"title":"Student predicted grades variation by cluster",
                        "xaxis":"",
                        "yaxis":"Predicted Grades",
                        "cluster":["Dropout",'Grades between 0 and 60','Grades between 61 and 70', 'Grades between 71 and 80', 'Grades between 81 and 90', 'Grades between 91 and 100']
                    }
        
        df = self.DATASET.sort_values(by=["Predicted Grade"])
        Clusters = df.Cluster.unique()
        color = ["rgb(100,100,100)","rgb(255,0,0)","rgb(127,0,127)","rgb(0,0,255)","rgb(0,127,127)","rgb(0,255,0)"]
        # print(Clusters)
        trace = []
        for i in range(0,len(Clusters)):
            trace.append(
                Box(
                    y=df["Predicted Grade"].loc[df['Cluster']==Clusters[i]].values.tolist(), #Access
                    name=legend["cluster"][i],
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
                range = [-1, self.DATASET["Predicted Grade"].max()+10],
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
                id='V007@3',
                figure=fig
            )
        elif self._type_result == "flask":
            modeBarButtonsToRemove = ['toImage', 'sendDataToCloud', 'hoverCompareCartesian', 'lasso2d', 'hoverClosestCartesian', 'toggleHover', 'hoverClosest3d', 'hoverClosestGeo', 'hoverClosestGl2d', 'hoverClosestPie']
            config = {"displaylogo": False, "responsive": True, "displayModeBar": True, "modeBarButtonsToRemove": modeBarButtonsToRemove}
            return {"id":"V007@3","layout":json.dumps({"data": data, "layout": layout, "config": config}, cls=PlotlyJSONEncoder)}

    # Violin
    def graph_04(self):
        legend = {"title":"Variação da previsão de notas dos estudantes por cluster",
                    "xaxis":"",
                    "yaxis":"Previsão das Notas",
                    "cluster":["Desistentes",'Notas entre 0 e 60','Notas entre 61 e 70', 'Notas entre 71 e 80', 'Notas entre 81 e 90', 'Notas entre 91 e 100']
                }
        if (self._language == "en"):
            legend = {"title":"Student predicted grades variation by cluster",
                        "xaxis":"",
                        "yaxis":"Predicted Grades",
                        "cluster":["Dropout",'Grades between 0 and 60','Grades between 61 and 70', 'Grades between 71 and 80', 'Grades between 81 and 90', 'Grades between 91 and 100']
                    }
        # https://plot.ly/python/violin/#reference
        # https://plot.ly/python/reference/#violin
        df = self.DATASET.sort_values(by=["Predicted Grade"])
        Clusters = df.Cluster.unique()
        color = ["rgb(100,100,100)","rgb(255,0,0)","rgb(127,0,127)","rgb(0,0,255)","rgb(0,127,127)","rgb(0,255,0)"]
        color[Clusters[0]] = "rgb(100,100,100)"
        color[Clusters[1]] = "rgb(255,0,0)"
        color[Clusters[2]] = "rgb(127,0,127)"
        color[Clusters[3]] = "rgb(0,0,255)"
        color[Clusters[4]] = "rgb(0,127,127)"
        color[Clusters[5]] = "rgb(0,255,0)"
        # print(Clusters)
        trace = []
        for i in range(0,len(Clusters)):
            trace.append(
                {
                    "type":'violin',
                    "x":["Cluster "+str(i+1)]*len(df["Predicted Grade"].loc[df['Cluster']==Clusters[i]]),
                    "y":df["Predicted Grade"].loc[df['Cluster']==Clusters[i]],
                    "name":legend["cluster"][i],
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
                range = [-15, self.DATASET["Predicted Grade"].max()+10],
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
                id='V007@4',
                figure=fig
            )
        elif self._type_result == "flask":
            modeBarButtonsToRemove = ['toImage', 'sendDataToCloud', 'hoverCompareCartesian', 'lasso2d', 'hoverClosestCartesian', 'toggleHover', 'hoverClosest3d', 'hoverClosestGeo', 'hoverClosestGl2d', 'hoverClosestPie']
            config = {"displaylogo": False, "responsive": True, "displayModeBar": True, "modeBarButtonsToRemove": modeBarButtonsToRemove}
            return {"id":"V007@4","layout":json.dumps({"data": data, "layout": layout, "config": config}, cls=PlotlyJSONEncoder)}

    def get_chart(self,id):
        if id == 1:
            return self.graph_01()
        elif id == 2:
            return self.graph_02()
        elif id == 3:
            return self.graph_03()
        elif id == 4:
            return self.graph_04()
        else:
            print("V007@"+str(id)+" not found")

    def print_all_graphs(self,language="pt"):
        self._language = language
        self.graph_01() #Table
        self.graph_02() #Scatter
        self.graph_03() #Box
        self.graph_04() #Violin
