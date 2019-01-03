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


from plotly.graph_objs import Figure, Layout, Bar, Table, Heatmap, Scatter, Box, Violin
from plotly.offline import init_notebook_mode, iplot


from sklearn import metrics
from sklearn.cluster import KMeans


init_notebook_mode(connected=True) # initiate notebook for offline plot
plotly.__version__

class V007:
    NUMBER_ACTIONS = 50
    DATASET = pd.DataFrame()


    _language = "pt"
    _type_result="jupyter-notebook"

    def __init__(self, language="pt", type_result = "jupyter-notebook"):
        self._language = language
        self._type_result = type_result

    def generate_dataset(self, number_students = 20):
        self.NUMBER_STUDENTS = number_students

        names = pd.read_csv("names.csv")
        rand_names = [names.group_name[np.random.randint(0,len(names.group_name)+1)] for n in range(0,self.NUMBER_STUDENTS)]
        rand_names.sort()

        self.RAWDATASET = pd.DataFrame(columns=["Students","Predicted Grade","Predicted Dropout", "Grade", "Cluster"])
        for i in range(0,self.NUMBER_STUDENTS):
            self.DATASET.loc[i,"Students"] = rand_names[i]
            self.DATASET.loc[i,"Predicted Grade"] = random.choice(['-','0 - 60','61 - 70', '71 - 80', '81 - 90', '91 - 100'])
            if self.DATASET.loc[i,"Predicted Grade"] == '-':
                self.DATASET.loc[i,"Predicted Dropout"] = True
                self.DATASET.loc[i,"Grade"] = None
                self.DATASET.loc[i,"Cluster"] = 0

            elif self.DATASET.loc[i,"Predicted Grade"] == '0 - 60':
                self.DATASET.loc[i,"Predicted Dropout"] = False
                self.DATASET.loc[i,"Grade"] = int(random.triangular(0,30,80))
                self.DATASET.loc[i,"Cluster"] = 1

            elif self.DATASET.loc[i,"Predicted Grade"] == '61 - 70':
                self.DATASET.loc[i,"Predicted Dropout"] = False
                self.DATASET.loc[i,"Grade"] = int(random.triangular(50,65,80))
                self.DATASET.loc[i,"Cluster"] = 2

            elif self.DATASET.loc[i,"Predicted Grade"] == '71 - 80':
                self.DATASET.loc[i,"Predicted Dropout"] = False
                self.DATASET.loc[i,"Grade"] = int(random.triangular(60,75,90))
                self.DATASET.loc[i,"Cluster"] = 3

            elif self.DATASET.loc[i,"Predicted Grade"] == '81 - 90':
                self.DATASET.loc[i,"Predicted Dropout"] = False
                self.DATASET.loc[i,"Grade"] = int(random.triangular(70,85,100))
                self.DATASET.loc[i,"Cluster"] = 4

            elif self.DATASET.loc[i,"Predicted Grade"] == '91 - 100':
                self.DATASET.loc[i,"Predicted Dropout"] = False
                self.DATASET.loc[i,"Grade"] = int(random.triangular(70,95,100))
                self.DATASET.loc[i,"Cluster"] = 5

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
                id='V007@1',
                figure={"data": data}
            )

    def graph_02(self):
        legend = {"title":"--",
                    "xaxis":"Grade",
                    "yaxis":"Idade",
                }
        if (self._language == "en"):
            legend = {"title":"--",
                        "xaxis":"Predicted Grade",
                        "yaxis":"Age",
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
                #autorange = False,
                #fixedrange = False,
                #range = [0, self.DATASET["Forum Access"].max()+10],
                #rangemode = "normal",
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
                id='V007@2',
                figure=fig
            )


    def print_all_graphs(self,language="pt"):
        self._language = language
        self.graph_01() #Table
        self.graph_02()
