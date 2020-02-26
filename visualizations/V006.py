import dash
import dash_core_components as dcc
import dash_html_components as html

import pandas as pd
import numpy as np

import json

from plotly.utils import PlotlyJSONEncoder
from plotly.graph_objs import Figure, Layout, Bar, Table, Heatmap, Scatter, Box, Violin
from plotly.offline import init_notebook_mode, iplot

from sklearn import metrics
from sklearn.cluster import KMeans


init_notebook_mode(connected=True) # initiate notebook for offline plot

class V006:
    NUMBER_STUDENTS = 50
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
        self.DATASET = pd.DataFrame(columns=["Students","Age","Forum Access","Forum Post","Forum Replies","Forum Add Thread","Cluster"])

        self.DATASET.Age = np.random.triangular(18,30,70,self.NUMBER_STUDENTS)
        self.DATASET["Age"] = self.DATASET.apply(self.convert_to_int, axis=1)

        rand_names = [names.group_name[np.random.randint(0,len(names.group_name)+1)] for n in range(0,self.NUMBER_STUDENTS)]
        rand_names.sort()

        for i in range(0,self.NUMBER_STUDENTS):
            self.DATASET.loc[i,"Students"] = rand_names[i]

            if (self.DATASET.loc[i,"Age"] <= 25):
                self.DATASET.loc[i,"Forum Post"] = np.random.randint(0,4)
                self.DATASET.loc[i,"Forum Replies"] = np.random.randint(0,4)
                self.DATASET.loc[i,"Forum Add Thread"] = np.random.randint(0,4)

                self.DATASET.loc[i,"Forum Access"] =  self.DATASET.loc[i,"Forum Post"] + self.DATASET.loc[i,"Forum Replies"] + self.DATASET.loc[i,"Forum Add Thread"] + np.random.randint(0,7)
                self.DATASET.loc[i,"Cluster"] = 1

            elif (self.DATASET.loc[i,"Age"] <= 30):
                self.DATASET.loc[i,"Forum Post"] = np.random.randint(0,8)
                self.DATASET.loc[i,"Forum Replies"] = np.random.randint(0,8)
                self.DATASET.loc[i,"Forum Add Thread"] = np.random.randint(0,4)

                self.DATASET.loc[i,"Forum Access"] = self.DATASET.loc[i,"Forum Post"] + self.DATASET.loc[i,"Forum Replies"] + self.DATASET.loc[i,"Forum Add Thread"] + np.random.randint(0,22)
                self.DATASET.loc[i,"Cluster"] = 2

            elif (self.DATASET.loc[i,"Age"] <= 40):
                self.DATASET.loc[i,"Forum Post"] = np.random.randint(1,12)
                self.DATASET.loc[i,"Forum Replies"] = np.random.randint(0,12)
                self.DATASET.loc[i,"Forum Add Thread"] = np.random.randint(0,8)

                self.DATASET.loc[i,"Forum Access"] =  self.DATASET.loc[i,"Forum Post"] + self.DATASET.loc[i,"Forum Replies"] + self.DATASET.loc[i,"Forum Add Thread"] + np.random.randint(2,26)
                self.DATASET.loc[i,"Cluster"] = 3

            elif (self.DATASET.loc[i,"Age"] <= 50):
                self.DATASET.loc[i,"Forum Post"] = np.random.randint(2,21)
                self.DATASET.loc[i,"Forum Replies"] = np.random.randint(2,21)
                self.DATASET.loc[i,"Forum Add Thread"] = np.random.randint(0,7)

                self.DATASET.loc[i,"Forum Access"] =  self.DATASET.loc[i,"Forum Post"] + self.DATASET.loc[i,"Forum Replies"] + self.DATASET.loc[i,"Forum Add Thread"] + np.random.randint(4,31)
                self.DATASET.loc[i,"Cluster"] = 4

            elif (self.DATASET.loc[i,"Age"] <= 60):
                self.DATASET.loc[i,"Forum Post"] = np.random.randint(5,36)
                self.DATASET.loc[i,"Forum Replies"] = np.random.randint(5,36)
                self.DATASET.loc[i,"Forum Add Thread"] = np.random.randint(1,11)

                self.DATASET.loc[i,"Forum Access"] =  self.DATASET.loc[i,"Forum Post"] + self.DATASET.loc[i,"Forum Replies"] + self.DATASET.loc[i,"Forum Add Thread"] + np.random.randint(6,36)
                self.DATASET.loc[i,"Cluster"] = 5

            else:
                self.DATASET.loc[i,"Forum Post"] = np.random.randint(10,41)
                self.DATASET.loc[i,"Forum Replies"] = np.random.randint(10,41)
                self.DATASET.loc[i,"Forum Add Thread"] = np.random.randint(3,14)

                self.DATASET.loc[i,"Forum Access"] =  self.DATASET.loc[i,"Forum Post"] + self.DATASET.loc[i,"Forum Replies"] + self.DATASET.loc[i,"Forum Add Thread"] + np.random.randint(10,41)
                self.DATASET.loc[i,"Cluster"] = 6

    def convert_to_int(self,row):
        return int(row["Age"])

    # Table presenting raw data
    def graph_01(self):
        legend = {"title":"Relação entre as notas dos estudantes e seus acessos no AVA"}
        if (self._language == "en"):
            legend = {"title":"Relation between either students' grades and their access in the VLE"}
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
                id='V006@1',
                figure={"data": data}
            )
        elif self._type_result == "flask":
            modeBarButtonsToRemove = ['toImage', 'sendDataToCloud', 'hoverCompareCartesian', 'lasso2d', 'hoverClosestCartesian', 'toggleHover', 'hoverClosest3d', 'hoverClosestGeo', 'hoverClosestGl2d', 'hoverClosestPie']
            config = {"displaylogo": False, "responsive": True, "displayModeBar": True, "modeBarButtonsToRemove": modeBarButtonsToRemove}
            return {"id":"V006@1","layout":json.dumps({"data": data, "layout": layout, "config": config}, cls=PlotlyJSONEncoder)}

    # Scatter
    def graph_02(self):
        legend = {"title":"Relação entre a idade dos estudantes e seus acessos no fórum",
                    "xaxis":"Acessos no fórum",
                    "yaxis":"Idade",
                }
        if (self._language == "en"):
            legend = {"title":"Relation between either students' age and their access in the forum",
                        "xaxis":"Access in the forum",
                        "yaxis":"Age",
                    }        
        color = ["rgb(127,0,0)","rgb(255,0,0)","rgb(127,0,127)","rgb(0,0,255)","rgb(0,127,127)","rgb(0,255,0)"]
        trace = []
        for i in range(0, self.NUMBER_STUDENTS):
            trace.append(
                Scatter(
                    x=[self.DATASET["Forum Access"][i]], #Acesso ao fórum
                    y=[self.DATASET.Age[i]], #Age
                    mode='markers',
                    name=self.DATASET.Students[i], #each student name
                    text = [str(self.DATASET.Students[i])],
                    marker=dict(
                        size=12,
                        symbol=self.DATASET.Cluster[i]-1,
                        color = color[self.DATASET.Cluster[i]-1],
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
                range = [0, self.DATASET["Forum Access"].max()+10],
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
                range = [0, self.DATASET.Age.max()+10],
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
                id='V006@2',
                figure=fig
            )
        elif self._type_result == "flask":
            modeBarButtonsToRemove = ['toImage', 'sendDataToCloud', 'hoverCompareCartesian', 'lasso2d', 'hoverClosestCartesian', 'toggleHover', 'hoverClosest3d', 'hoverClosestGeo', 'hoverClosestGl2d', 'hoverClosestPie']
            config = {"displaylogo": False, "responsive": True, "displayModeBar": True, "modeBarButtonsToRemove": modeBarButtonsToRemove}
            return {"id":"V006@2","layout":json.dumps({"data": data, "layout": layout, "config": config}, cls=PlotlyJSONEncoder)}

    def graph_03(self):
        legend = {"title":"Relação entre a idade dos estudantes e suas postagens no fórum",
                    "xaxis":"Postagens no fórum",
                    "yaxis":"Idade",
                }
        if (self._language == "en"):
            legend = {"title":"Relation between either students' age and their posts in the forum",
                        "xaxis":"Posts in the forum",
                        "yaxis":"Age",
                    }
        color = ["rgb(127,0,0)","rgb(255,0,0)","rgb(127,0,127)","rgb(0,0,255)","rgb(0,127,127)","rgb(0,255,0)"]
        trace = []
        for i in range(0, self.NUMBER_STUDENTS):
            trace.append(
                Scatter(
                    x=[self.DATASET["Forum Post"][i]], #Posts
                    y=[self.DATASET.Age[i]], #Age
                    mode='markers',
                    name=self.DATASET.Students[i], #each student name                    
                    text = [str(self.DATASET.Students[i])],                    
                    marker=dict(
                        size=12,                        
                        symbol=self.DATASET.Cluster[i]-1,
                        color = color[self.DATASET.Cluster[i]-1],
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
                range = [0, self.DATASET["Forum Post"].max()+10],
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
                range = [0, self.DATASET.Age.max()+10],
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
                id='V006@3',
                figure=fig
            )
        elif self._type_result == "flask":
            modeBarButtonsToRemove = ['toImage', 'sendDataToCloud', 'hoverCompareCartesian', 'lasso2d', 'hoverClosestCartesian', 'toggleHover', 'hoverClosest3d', 'hoverClosestGeo', 'hoverClosestGl2d', 'hoverClosestPie']
            config = {"displaylogo": False, "responsive": True, "displayModeBar": True, "modeBarButtonsToRemove": modeBarButtonsToRemove}
            return {"id":"V006@3","layout":json.dumps({"data": data, "layout": layout, "config": config}, cls=PlotlyJSONEncoder)}

    def graph_04(self):
        legend = {"title":"Relação entre a idade dos estudantes e suas réplicas no fórum",
                    "xaxis":"Réplicas no fórum",
                    "yaxis":"Idade",
                }
        if (self._language == "en"):
            legend = {"title":"Relation between either students' age and their replies in the forum",
                        "xaxis":"Replies in the forum",
                        "yaxis":"Age",
                    }
        color = ["rgb(127,0,0)","rgb(255,0,0)","rgb(127,0,127)","rgb(0,0,255)","rgb(0,127,127)","rgb(0,255,0)"]
        trace = []
        for i in range(0, self.NUMBER_STUDENTS):
            trace.append(
                Scatter(
                    x=[self.DATASET["Forum Replies"][i]], #Replies
                    y=[self.DATASET.Age[i]], #Age
                    mode='markers',
                    name=self.DATASET.Students[i], #each student name                    
                    text = [str(self.DATASET.Students[i])],                    
                    marker=dict(
                        size=12,                        
                        symbol=self.DATASET.Cluster[i]-1,
                        color = color[self.DATASET.Cluster[i]-1],
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
                range = [0, self.DATASET["Forum Replies"].max()+10],
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
                range = [0, self.DATASET.Age.max()+10],
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
                id='V006@4',
                figure=fig
            )
        elif self._type_result == "flask":
            modeBarButtonsToRemove = ['toImage', 'sendDataToCloud', 'hoverCompareCartesian', 'lasso2d', 'hoverClosestCartesian', 'toggleHover', 'hoverClosest3d', 'hoverClosestGeo', 'hoverClosestGl2d', 'hoverClosestPie']
            config = {"displaylogo": False, "responsive": True, "displayModeBar": True, "modeBarButtonsToRemove": modeBarButtonsToRemove}
            return {"id":"V006@4","layout":json.dumps({"data": data, "layout": layout, "config": config}, cls=PlotlyJSONEncoder)}

    def graph_05(self):
        legend = {"title":"Relação entre a idade dos estudantes e seus tópicos adicionados no fórum",
                    "xaxis":"Tópicos no fórum",
                    "yaxis":"Idade",
                }
        if (self._language == "en"):
            legend = {"title":"Relation between either students' age and their threads added in the forum",
                        "xaxis":"Threads in the forum",
                        "yaxis":"Age",
                    }
        color = ["rgb(127,0,0)","rgb(255,0,0)","rgb(127,0,127)","rgb(0,0,255)","rgb(0,127,127)","rgb(0,255,0)"]
        trace = []
        for i in range(0, self.NUMBER_STUDENTS):
            trace.append(
                Scatter(
                    x=[self.DATASET["Forum Add Thread"][i]], #Init threads in forum
                    y=[self.DATASET.Age[i]], #Age
                    mode='markers',
                    name=self.DATASET.Students[i], #each student name                    
                    text = [str(self.DATASET.Students[i])],                    
                    marker=dict(
                        size=12,                        
                        symbol=self.DATASET.Cluster[i]-1,
                        color = color[self.DATASET.Cluster[i]-1],
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
                range = [0, self.DATASET["Forum Add Thread"].max()+10],
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
                range = [0, self.DATASET.Age.max()+10],
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
                id='V006@5',
                figure=fig
            )
        elif self._type_result == "flask":
            modeBarButtonsToRemove = ['toImage', 'sendDataToCloud', 'hoverCompareCartesian', 'lasso2d', 'hoverClosestCartesian', 'toggleHover', 'hoverClosest3d', 'hoverClosestGeo', 'hoverClosestGl2d', 'hoverClosestPie']
            config = {"displaylogo": False, "responsive": True, "displayModeBar": True, "modeBarButtonsToRemove": modeBarButtonsToRemove}
            return {"id":"V006@5","layout":json.dumps({"data": data, "layout": layout, "config": config}, cls=PlotlyJSONEncoder)}

    #Box
    def graph_06(self):
        legend = {"title":"Variação de acessos no fórum por idade",
                    "xaxis":"",
                    "yaxis":"Acessos no fórum",
                    "age":{1:"até 25 anos", 2:"26 à 30 anos", 3:"31 à 40 anos", 4: "41 à 50 anos", 5: "51 à 60 anos", 6: "mais de 60 anos"},
                }
        if (self._language == "en"):
            legend = {"title":"Variation of students' access in the forum by age",
                        "xaxis":"",
                        "yaxis":"Access in the forum",
                        "age":{1:"until 25 years", 2:"26 to 30 years", 3:"31 to 40 years", 4: "41 to 50 years", 5: "51 to 60 years", 6: "over 60 years"},
                    }
        df = self.DATASET.sort_values(by="Age")
        Clusters = df.Cluster.unique()
        color = ["rgb(127,0,0)","rgb(255,0,0)","rgb(127,0,127)","rgb(0,0,255)","rgb(0,127,127)","rgb(0,255,0)"]        
        # print(Clusters)
        trace = []
        for i in range(0,len(Clusters)):
            trace.append(
                Box(
                    y=df["Forum Access"].loc[df['Cluster']==Clusters[i]].values.tolist(),
                    name=legend['age'][i+1],
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
                range = [-1, self.DATASET["Forum Access"].max()+10],
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
                id='V006@6',
                figure=fig
            )
        elif self._type_result == "flask":
            modeBarButtonsToRemove = ['toImage', 'sendDataToCloud', 'hoverCompareCartesian', 'lasso2d', 'hoverClosestCartesian', 'toggleHover', 'hoverClosest3d', 'hoverClosestGeo', 'hoverClosestGl2d', 'hoverClosestPie']
            config = {"displaylogo": False, "responsive": True, "displayModeBar": True, "modeBarButtonsToRemove": modeBarButtonsToRemove}
            return {"id":"V006@6","layout":json.dumps({"data": data, "layout": layout, "config": config}, cls=PlotlyJSONEncoder)}

    def graph_07(self):
        legend = {"title":"Variação de postagens no fórum por idade",
                    "xaxis":"",
                    "yaxis":"Postagens no fórum",
                    "age":{1:"até 25 anos", 2:"26 à 30 anos", 3:"31 à 40 anos", 4: "41 à 50 anos", 5: "51 à 60 anos", 6: "mais de 60 anos"},
                }
        if (self._language == "en"):
            legend = {"title":"Variation of students' posts in the forum by age",
                        "xaxis":"",
                        "yaxis":"Posts in the forum",
                        "age":{1:"until 25 years", 2:"26 to 30 years", 3:"31 to 40 years", 4: "41 to 50 years", 5: "51 to 60 years", 6: "over 60 years"},
                    }
        df = self.DATASET.sort_values(by="Age")
        Clusters = df.Cluster.unique()
        color = ["rgb(127,0,0)","rgb(255,0,0)","rgb(127,0,127)","rgb(0,0,255)","rgb(0,127,127)","rgb(0,255,0)"]        
        # print(Clusters)
        trace = []
        for i in range(0,len(Clusters)):
            trace.append(
                Box(
                    y=df["Forum Post"].loc[df['Cluster']==Clusters[i]].values.tolist(),
                    name=legend['age'][i+1],
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
                range = [-1, self.DATASET["Forum Post"].max()+10],
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
                id='V006@7',
                figure=fig
            )
        elif self._type_result == "flask":
            modeBarButtonsToRemove = ['toImage', 'sendDataToCloud', 'hoverCompareCartesian', 'lasso2d', 'hoverClosestCartesian', 'toggleHover', 'hoverClosest3d', 'hoverClosestGeo', 'hoverClosestGl2d', 'hoverClosestPie']
            config = {"displaylogo": False, "responsive": True, "displayModeBar": True, "modeBarButtonsToRemove": modeBarButtonsToRemove}
            return {"id":"V006@7","layout":json.dumps({"data": data, "layout": layout, "config": config}, cls=PlotlyJSONEncoder)}

    def graph_08(self):
        legend = {"title":"Variação de réplicas no fórum por idade",
                    "xaxis":"",
                    "yaxis":"Réplicas no fórum",
                    "age":{1:"até 25 anos", 2:"26 à 30 anos", 3:"31 à 40 anos", 4: "41 à 50 anos", 5: "51 à 60 anos", 6: "mais de 60 anos"},
                }
        if (self._language == "en"):
            legend = {"title":"Variation of students' replies in the forum by age",
                        "xaxis":"",
                        "yaxis":"Replies in the forum",
                        "age":{1:"until 25 years", 2:"26 to 30 years", 3:"31 to 40 years", 4: "41 to 50 years", 5: "51 to 60 years", 6: "over 60 years"},
                    }
        df = self.DATASET.sort_values(by="Age")
        Clusters = df.Cluster.unique()
        color = ["rgb(127,0,0)","rgb(255,0,0)","rgb(127,0,127)","rgb(0,0,255)","rgb(0,127,127)","rgb(0,255,0)"]        
        # print(Clusters)
        trace = []
        for i in range(0,len(Clusters)):
            trace.append(
                Box(
                    y=df["Forum Replies"].loc[df['Cluster']==Clusters[i]].values.tolist(),
                    name=legend['age'][i+1],
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
                range = [-1, self.DATASET["Forum Replies"].max()+10],
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
                id='V006@8',
                figure=fig
            )
        elif self._type_result == "flask":
            modeBarButtonsToRemove = ['toImage', 'sendDataToCloud', 'hoverCompareCartesian', 'lasso2d', 'hoverClosestCartesian', 'toggleHover', 'hoverClosest3d', 'hoverClosestGeo', 'hoverClosestGl2d', 'hoverClosestPie']
            config = {"displaylogo": False, "responsive": True, "displayModeBar": True, "modeBarButtonsToRemove": modeBarButtonsToRemove}
            return {"id":"V006@8","layout":json.dumps({"data": data, "layout": layout, "config": config}, cls=PlotlyJSONEncoder)}

    def graph_09(self):
        legend = {"title":"Variação de tópicos adicionados no fórum por idade",
                    "xaxis":"",
                    "yaxis":"Tópicos no fórum",
                    "age":{1:"até 25 anos", 2:"26 à 30 anos", 3:"31 à 40 anos", 4: "41 à 50 anos", 5: "51 à 60 anos", 6: "mais de 60 anos"},
                }
        if (self._language == "en"):
            legend = {"title":"Variation of students' threads added in the forum by age",
                        "xaxis":"",
                        "yaxis":"Threads in the forum",
                        "age":{1:"until 25 years", 2:"26 to 30 years", 3:"31 to 40 years", 4: "41 to 50 years", 5: "51 to 60 years", 6: "over 60 years"},
                    }
        df = self.DATASET.sort_values(by="Age")
        Clusters = df.Cluster.unique()
        color = ["rgb(127,0,0)","rgb(255,0,0)","rgb(127,0,127)","rgb(0,0,255)","rgb(0,127,127)","rgb(0,255,0)"]        
        # print(Clusters)
        trace = []
        for i in range(0,len(Clusters)):
            trace.append(
                Box(
                    y=df["Forum Add Thread"].loc[df['Cluster']==Clusters[i]].values.tolist(),
                    name=legend['age'][i+1],
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
                range = [-1, self.DATASET["Forum Add Thread"].max()+10],
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
                id='V006@9',
                figure=fig
            )
        elif self._type_result == "flask":
            modeBarButtonsToRemove = ['toImage', 'sendDataToCloud', 'hoverCompareCartesian', 'lasso2d', 'hoverClosestCartesian', 'toggleHover', 'hoverClosest3d', 'hoverClosestGeo', 'hoverClosestGl2d', 'hoverClosestPie']
            config = {"displaylogo": False, "responsive": True, "displayModeBar": True, "modeBarButtonsToRemove": modeBarButtonsToRemove}
            return {"id":"V006@9","layout":json.dumps({"data": data, "layout": layout, "config": config}, cls=PlotlyJSONEncoder)}

    #Violin
    def graph_10(self):
        legend = {"title":"Variação de acessos no fórum por idade",
                    "xaxis":"",
                    "yaxis":"Acessos no fórum",
                    "age":{1:"até 25 anos", 2:"26 à 30 anos", 3:"31 à 40 anos", 4: "41 à 50 anos", 5: "51 à 60 anos", 6: "mais de 60 anos"},
                }
        if (self._language == "en"):
            legend = {"title":"Variation of students' access in the forum by age",
                        "xaxis":"",
                        "yaxis":"Access in the forum",
                        "age":{1:"until 25 years", 2:"26 to 30 years", 3:"31 to 40 years", 4: "41 to 50 years", 5: "51 to 60 years", 6: "over 60 years"},
                    }
        # https://plot.ly/python/violin/#reference
        # https://plot.ly/python/reference/#violin
        df = self.DATASET.sort_values(by="Age")
        Clusters = df.Cluster.unique()
        color = ["rgb(127,0,0)","rgb(255,0,0)","rgb(127,0,127)","rgb(0,0,255)","rgb(0,127,127)","rgb(0,255,0)"]
        # print(Clusters)
        trace = []
        for i in range(0,len(Clusters)):
            trace.append(
                {
                    "type":'violin',
                    "x":[legend['age'][i+1]]*len(df.loc[df['Cluster']==Clusters[i]]),
                    "y":df["Forum Access"].loc[df['Cluster']==Clusters[i]],
                    "name":legend['age'][i+1],
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
                range = [-15, self.DATASET["Forum Access"].max()+10],                
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
                id='V006@10',
                figure=fig
            )
        elif self._type_result == "flask":
            modeBarButtonsToRemove = ['toImage', 'sendDataToCloud', 'hoverCompareCartesian', 'lasso2d', 'hoverClosestCartesian', 'toggleHover', 'hoverClosest3d', 'hoverClosestGeo', 'hoverClosestGl2d', 'hoverClosestPie']
            config = {"displaylogo": False, "responsive": True, "displayModeBar": True, "modeBarButtonsToRemove": modeBarButtonsToRemove}
            return {"id":"V006@10","layout":json.dumps({"data": data, "layout": layout, "config": config}, cls=PlotlyJSONEncoder)}

    def graph_11(self):
        legend = {"title":"Variação de postagens no fórum por idade",
                    "xaxis":"",
                    "yaxis":"Postagens no fórum",
                    "age":{1:"até 25 anos", 2:"26 à 30 anos", 3:"31 à 40 anos", 4: "41 à 50 anos", 5: "51 à 60 anos", 6: "mais de 60 anos"},
                }
        if (self._language == "en"):
            legend = {"title":"Variation of students' posts in the forum by age",
                        "xaxis":"",
                        "yaxis":"Posts in the forum",
                        "age":{1:"until 25 years", 2:"26 to 30 years", 3:"31 to 40 years", 4: "41 to 50 years", 5: "51 to 60 years", 6: "over 60 years"},
                    }
        # https://plot.ly/python/violin/#reference
        # https://plot.ly/python/reference/#violin
        df = self.DATASET.sort_values(by="Age")
        Clusters = df.Cluster.unique()
        color = ["rgb(127,0,0)","rgb(255,0,0)","rgb(127,0,127)","rgb(0,0,255)","rgb(0,127,127)","rgb(0,255,0)"]
        # print(Clusters)
        trace = []
        for i in range(0,len(Clusters)):
            trace.append(
                {
                    "type":'violin',
                    "x":[legend['age'][i+1]]*len(df.loc[df['Cluster']==Clusters[i]]),
                    "y":df["Forum Post"].loc[df['Cluster']==Clusters[i]],
                    "name":legend['age'][i+1],
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
                range = [-15, self.DATASET["Forum Post"].max()+10],                
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
                id='V006@11',
                figure=fig
            )
        elif self._type_result == "flask":
            modeBarButtonsToRemove = ['toImage', 'sendDataToCloud', 'hoverCompareCartesian', 'lasso2d', 'hoverClosestCartesian', 'toggleHover', 'hoverClosest3d', 'hoverClosestGeo', 'hoverClosestGl2d', 'hoverClosestPie']
            config = {"displaylogo": False, "responsive": True, "displayModeBar": True, "modeBarButtonsToRemove": modeBarButtonsToRemove}
            return {"id":"V006@11","layout":json.dumps({"data": data, "layout": layout, "config": config}, cls=PlotlyJSONEncoder)}

    def graph_12(self):
        legend = {"title":"Variação de réplicas no fórum por idade",
                    "xaxis":"",
                    "yaxis":"Réplicas no fórum",
                    "age":{1:"até 25 anos", 2:"26 à 30 anos", 3:"31 à 40 anos", 4: "41 à 50 anos", 5: "51 à 60 anos", 6: "mais de 60 anos"},
                }
        if (self._language == "en"):
            legend = {"title":"Variation of students' replies in the forum by age",
                        "xaxis":"",
                        "yaxis":"Replies in the forum",
                        "age":{1:"until 25 years", 2:"26 to 30 years", 3:"31 to 40 years", 4: "41 to 50 years", 5: "51 to 60 years", 6: "over 60 years"},
                    }
        # https://plot.ly/python/violin/#reference
        # https://plot.ly/python/reference/#violin
        df = self.DATASET.sort_values(by="Age")
        Clusters = df.Cluster.unique()
        color = ["rgb(127,0,0)","rgb(255,0,0)","rgb(127,0,127)","rgb(0,0,255)","rgb(0,127,127)","rgb(0,255,0)"]
        # print(Clusters)
        trace = []
        for i in range(0,len(Clusters)):
            trace.append(
                {
                    "type":'violin',
                    "x":[legend['age'][i+1]]*len(df.loc[df['Cluster']==Clusters[i]]),
                    "y":df["Forum Replies"].loc[df['Cluster']==Clusters[i]],
                    "name":legend['age'][i+1],
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
                range = [-15, self.DATASET["Forum Replies"].max()+10],                
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
                id='V006@12',
                figure=fig
            )
        elif self._type_result == "flask":
            modeBarButtonsToRemove = ['toImage', 'sendDataToCloud', 'hoverCompareCartesian', 'lasso2d', 'hoverClosestCartesian', 'toggleHover', 'hoverClosest3d', 'hoverClosestGeo', 'hoverClosestGl2d', 'hoverClosestPie']
            config = {"displaylogo": False, "responsive": True, "displayModeBar": True, "modeBarButtonsToRemove": modeBarButtonsToRemove}
            return {"id":"V006@12","layout":json.dumps({"data": data, "layout": layout, "config": config}, cls=PlotlyJSONEncoder)}

    def graph_13(self):
        legend = {"title":"Variação de tópicos adicionados no fórum por idade",
                    "xaxis":"",
                    "yaxis":"Tópicos no fórum",
                    "age":{1:"até 25 anos", 2:"26 à 30 anos", 3:"31 à 40 anos", 4: "41 à 50 anos", 5: "51 à 60 anos", 6: "mais de 60 anos"},
                }
        if (self._language == "en"):
            legend = {"title":"Variation of students' threads added in the forum by age",
                        "xaxis":"",
                        "yaxis":"Threads in the forum",
                        "age":{1:"until 25 years", 2:"26 to 30 years", 3:"31 to 40 years", 4: "41 to 50 years", 5: "51 to 60 years", 6: "over 60 years"},
                    }
        # https://plot.ly/python/violin/#reference
        # https://plot.ly/python/reference/#violin
        df = self.DATASET.sort_values(by="Age")
        Clusters = df.Cluster.unique()
        color = ["rgb(127,0,0)","rgb(255,0,0)","rgb(127,0,127)","rgb(0,0,255)","rgb(0,127,127)","rgb(0,255,0)"]
        # print(Clusters)
        trace = []
        for i in range(0,len(Clusters)):
            trace.append(
                {
                    "type":'violin',
                    "x":[legend['age'][i+1]]*len(df.loc[df['Cluster']==Clusters[i]]),
                    "y":df["Forum Add Thread"].loc[df['Cluster']==Clusters[i]],
                    "name":legend['age'][i+1],
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
                range = [-15, self.DATASET["Forum Add Thread"].max()+10],                
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
                id='V006@13',
                figure=fig
            )
        elif self._type_result == "flask":
            modeBarButtonsToRemove = ['toImage', 'sendDataToCloud', 'hoverCompareCartesian', 'lasso2d', 'hoverClosestCartesian', 'toggleHover', 'hoverClosest3d', 'hoverClosestGeo', 'hoverClosestGl2d', 'hoverClosestPie']
            config = {"displaylogo": False, "responsive": True, "displayModeBar": True, "modeBarButtonsToRemove": modeBarButtonsToRemove}
            return {"id":"V006@13","layout":json.dumps({"data": data, "layout": layout, "config": config}, cls=PlotlyJSONEncoder)}

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
        elif id == 6:
            return self.graph_06()
        elif id == 7:
            return self.graph_07()
        elif id == 8:
            return self.graph_08()
        elif id == 9:
            return self.graph_09()
        elif id == 10:
            return self.graph_10()
        elif id == 11:
            return self.graph_11()
        elif id == 12:
            return self.graph_12()
        elif id == 13:
            return self.graph_13()        
        else:
            print("V006@"+str(id)+" not found")

    def get_preprocessed_chart(self,id):
        if not os.path.exists(self._preprocessed_folder):
            print('There is no preprocessed folder')
            return
        
        file_name = 'V006_'+str(id)+'.pkl'
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
        
        file_name = 'V006_'+str(id)+'.pkl'
        file_path = os.path.join(self._preprocessed_folder,file_name)
        f = open(file_path,'wb')
        pickle.dump(self.get_chart(id),f)
        f.close()

        self._type_result = aux_type_result

    def print_all_graphs(self,language="pt"):
        self._language = language
        self.graph_01() #Table
        self.graph_02() #Scatter
        self.graph_03()
        self.graph_04()
        self.graph_05()
        self.graph_06() #Box
        self.graph_07()
        self.graph_08()
        self.graph_09()
        self.graph_10() #Violin
        self.graph_11()
        self.graph_12()
        self.graph_13()

# instance = V006()
# instance.generate_dataset(number_students = 60)
# instance.print_all_graphs("pt")
# instance.print_all_graphs("en")