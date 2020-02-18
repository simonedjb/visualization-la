import dash
import dash_core_components as dcc
import dash_html_components as html

import pandas as pd
import numpy as np

from random import randrange
import datetime

import json

from plotly.utils import PlotlyJSONEncoder
from plotly.graph_objs import Figure, Layout, Bar, Table, Heatmap, Scatter, Box, Violin
from plotly.offline import init_notebook_mode, iplot

init_notebook_mode(connected=True) # initiate notebook for offline plot

class V009:
    NUMBER_STUDENTS = 10
    VIDEO_SIZE = 30
    DATASET = pd.DataFrame()

    _language = "pt"
    _type_result="jupyter-notebook"

    def __init__(self, language="pt", type_result = "jupyter-notebook"):
        self._language = language
        self._type_result = type_result

    def load_dataset(self, url):
        pass

    def generate_dataset(self, number_actions = 100, video_size = 30, students_names = pd.DataFrame()):
        self.NUMBER_ACTIONS = number_actions
        self.VIDEO_SIZE = video_size

        if len(students_names.columns.tolist()) == 0:
            names = pd.read_csv("assets/names.csv")
        else:
            names = students_names

        self.DATASET = pd.DataFrame(columns=["Students","Time (seconds)","Play","Pause","Seek from","Seek to","Dropout"])

        rand_names = [names.group_name[np.random.randint(0,len(names.group_name)+1)] for n in range(0,self.NUMBER_STUDENTS)]
        rand_names.sort()

        
        lst = [ [rand_names[i]]*(video_size+1) for i in range(0,self.NUMBER_STUDENTS)]
        names = []
        for i in range(0, len(lst)):
            names = names+lst[i]
        
        self.DATASET[self.DATASET.columns[0]] = names
        
        curr = ''
        time = 0
        for i in range(0,len(names)):
            self.DATASET.loc[i,self.DATASET.columns[2]] = np.random.randint(0, 2, size=1)[0]
            self.DATASET.loc[i,self.DATASET.columns[3]] = np.random.randint(0, 2, size=1)[0]
            self.DATASET.loc[i,self.DATASET.columns[4]] = np.random.randint(0, 4, size=1)[0]
            self.DATASET.loc[i,self.DATASET.columns[5]] = np.random.randint(0, 4, size=1)[0]
            self.DATASET.loc[i,self.DATASET.columns[6]] = np.random.randint(0, 2, size=1)[0]

            if names[i] != curr:
                curr = names[i]
                time = 0
                self.DATASET.loc[i,self.DATASET.columns[2]] = np.random.randint(1, 9, size=1)[0]

            self.DATASET.loc[i,self.DATASET.columns[1]] = time
            time = time+1

            if time == self.VIDEO_SIZE-3:
                self.DATASET.loc[i,self.DATASET.columns[6]] = np.random.randint(0, 4, size=1)[0]
            elif time == self.VIDEO_SIZE-2:
                self.DATASET.loc[i,self.DATASET.columns[6]] = np.random.randint(0, 5, size=1)[0]
            elif time == self.VIDEO_SIZE-1:
                self.DATASET.loc[i,self.DATASET.columns[6]] = np.random.randint(0, 6, size=1)[0]
            elif time == self.VIDEO_SIZE:
                self.DATASET.loc[i,self.DATASET.columns[6]] = np.random.randint(0, 7, size=1)[0]

        return self.DATASET


    # Table presenting raw data
    def graph_01(self):
        legend = {"title":"Número de interações por estudante a cada segundo do vídeo"}
        if (self._language == "en"):
            legend = {"title":"Number of interaction by student in each video time"}
        
        
        trace = [Table(
            header=dict(
                values=list(self.DATASET.columns[:len(self.DATASET.columns)]),
                fill = dict(color='#C2D4FF'),
                align = 'center'
            ),
            cells=dict(
                values=[self.DATASET[i].tolist() for i in self.DATASET.columns[:len(self.DATASET.columns)]],
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
                id='V009@1',
                figure={"data": data}
            )
        elif self._type_result == "flask":
            modeBarButtonsToRemove = ['toImage', 'sendDataToCloud', 'hoverCompareCartesian', 'lasso2d', 'hoverClosestCartesian', 'toggleHover', 'hoverClosest3d', 'hoverClosestGeo', 'hoverClosestGl2d', 'hoverClosestPie']
            config = {"displaylogo": False, "responsive": True, "displayModeBar": True, "modeBarButtonsToRemove": modeBarButtonsToRemove}
            return {"id":"V009@1","layout":json.dumps({"data": data, "layout": layout, "config": config}, cls=PlotlyJSONEncoder)}

    def graph_02(self):
        legend = {"title":"Número de interações por tempo do vídeo"}
        if (self._language == "en"):
            legend = {"title":"Number of interaction by video time"}
        
        df = pd.DataFrame(columns=self.DATASET.columns[1:].tolist())
        
        for i in range(0,self.VIDEO_SIZE+1):
            df_aux = self.DATASET[self.DATASET.columns[2:]].loc[self.DATASET[self.DATASET.columns[1]] == i].apply(np.sum)
            df.loc[i] = df_aux.append(pd.Series([i],index=[self.DATASET.columns[1]]))

        trace = [Table(
            header=dict(
                values=list(df.columns[:len(df.columns)]),
                fill = dict(color='#C2D4FF'),
                align = 'center'
            ),
            cells=dict(
                values=[df[i].tolist() for i in df.columns[:len(df.columns)]],
                fill = dict(color='#F5F8FF'),
                align = ['center','center']
            )
        )]

        data = trace
        layout = Layout( title = legend["title"] )
        
        fig = Figure(data=data, layout=layout)
        if self._type_result == "jupyter-notebook":
            iplot(data, filename = 'pandas_table')
        elif self._type_result == "dash":
            return dcc.Graph(
                id='V009@2',
                figure={"data": data}
            )
        elif self._type_result == "flask":
            modeBarButtonsToRemove = ['toImage', 'sendDataToCloud', 'hoverCompareCartesian', 'lasso2d', 'hoverClosestCartesian', 'toggleHover', 'hoverClosest3d', 'hoverClosestGeo', 'hoverClosestGl2d', 'hoverClosestPie']
            config = {"displaylogo": False, "responsive": True, "displayModeBar": True, "modeBarButtonsToRemove": modeBarButtonsToRemove}
            return {"id":"V009@2","layout":json.dumps({"data": data, "layout": layout, "config": config}, cls=PlotlyJSONEncoder)}

    def graph_03(self):
        legend = {"title":"Cronologia de interações dos alunos"}
        if (self._language == "en"):
            legend = {"title":"Chronology of students' interaction"}

        df = pd.DataFrame(columns=[self.DATASET.columns[0],'Timestamp','Action'])

        textAction = ['Play at ', 'Pause at ', 'Seek from ', ' to ', 'Dropout at ']

        length = len(self.DATASET)
        actions = self.DATASET.columns[2:].tolist()
        lst_students = []
        lst_timestamp = []
        lst_action = []
        for i in range(0, length):
            student = self.DATASET.iloc[i,0]
            for j in range(0,len(actions)):
                if (self.DATASET.iloc[i,j+2] == 0):
                    continue

                if(j == 3): #Seek to
                    continue

                lst_students.append(student)
                lst_timestamp.append(datetime.datetime(year=2019, month=np.random.randint(1, 6, size=1)[0], day=np.random.randint(1, 27, size=1)[0], hour=np.random.randint(0, 23, size=1)[0], minute=np.random.randint(0, 59, size=1)[0], second=np.random.randint(0, 59, size=1)[0]))
                
                action = textAction[j]+str(self.DATASET.iloc[i,1])+"s"
                if(j == 2): #Seek from adding seek to
                    action = action+textAction[3]+str(np.random.randint(0, self.VIDEO_SIZE, size=1)[0])+"s"

                lst_action.append(action)

        df[df.columns[0]] = lst_students
        df[df.columns[1]] = lst_timestamp
        df[df.columns[2]] = lst_action

        df = df.sort_values(by=[df.columns[0],df.columns[1]])
        
        trace = [Table(
            header=dict(
                values=list(df.columns[:len(df.columns)]),
                fill = dict(color='#C2D4FF'),
                align = 'center'
            ),
            cells=dict(
                values=[df[i].tolist() for i in df.columns[:len(df.columns)]],
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
                id='V009@2',
                figure={"data": data}
            )
        elif self._type_result == "flask":
            modeBarButtonsToRemove = ['toImage', 'sendDataToCloud', 'hoverCompareCartesian', 'lasso2d', 'hoverClosestCartesian', 'toggleHover', 'hoverClosest3d', 'hoverClosestGeo', 'hoverClosestGl2d', 'hoverClosestPie']
            config = {"displaylogo": False, "responsive": True, "displayModeBar": True, "modeBarButtonsToRemove": modeBarButtonsToRemove}
            return {"id":"V009@3","layout":json.dumps({"data": data, "layout": layout, "config": config}, cls=PlotlyJSONEncoder)}
        

    def graph_04(self):
        legend = {"title":"Número de interações por tempo do vídeo",
                    "xaxis":"Tempo do vídeo em segundos",
                    "yaxis":"Interação",
                }
        if (self._language == "en"):
            legend = {"title":"Number of interaction by video time",
                        "xaxis":"Video time in seconds",
                        "yaxis":"Interaction",
                    }
        
        df = pd.DataFrame(columns=self.DATASET.columns[1:].tolist())        
        
        for i in range(0,self.VIDEO_SIZE+1):
            df_aux = self.DATASET[self.DATASET.columns[2:]].loc[self.DATASET[self.DATASET.columns[1]] == i].apply(np.sum)
            df.loc[i] = df_aux.append(pd.Series([i],index=[self.DATASET.columns[1]]))

        # color = ["rgb(100,100,100)","rgb(255,0,0)","rgb(127,0,127)","rgb(0,0,255)","rgb(0,127,127)","rgb(0,255,0)"]
        color = ["rgb(0,127,127)", "rgb(0,255,0)", "rgb(127,0,127)", "rgb(255,0,0)", "rgb(0,0,255)", "rgb(100,100,100)"]
        trace = []
        for i in range(1,len(df.columns.tolist())):
            trace.append(
                Scatter(
                    x=df[df.columns[0]],
                    y=df[df.columns[i]],
                    hoverinfo='x+y',
                    mode='lines',
                    name=df.columns[i],
                    text = [df.columns[i]],
                    line=dict(width=0.5, 
                                color=color[i]),
                    stackgroup='one'
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
                # autorange = False,
                # fixedrange = False,
                # range = [0, self.DATASET["AVA Access"].max()+10],
                # rangemode = "normal",
                # zeroline= False,
                # showline = True,
            ),
            yaxis = dict(
                title = legend["yaxis"],
                titlefont=dict(
                    # family='Arial, sans-serif',
                    # size=18,
                    color='rgb(180,180,180)',
                ),
                # autorange = False,
                # fixedrange = False,
                # range = [0, self.DATASET["Predicted Grade"].max()+10],
                # rangemode = "normal",
                # showline = True,
            )
        )

        data = trace
        fig = Figure(data=data, layout=layout)
        if self._type_result == "jupyter-notebook":
            iplot(fig, filename='stacked-area')
        elif self._type_result == "dash":
            return dcc.Graph(
                id='V009@3',
                figure=fig
            )
        elif self._type_result == "flask":
            modeBarButtonsToRemove = ['toImage', 'sendDataToCloud', 'hoverCompareCartesian', 'lasso2d', 'hoverClosestCartesian', 'toggleHover', 'hoverClosest3d', 'hoverClosestGeo', 'hoverClosestGl2d', 'hoverClosestPie']
            config = {"displaylogo": False, "responsive": True, "displayModeBar": True, "modeBarButtonsToRemove": modeBarButtonsToRemove}
            return {"id":"V009@4","layout":json.dumps({"data": data, "layout": layout, "config": config}, cls=PlotlyJSONEncoder)}
            
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
            return self.graph_03()
        else:
            print("V009@"+str(id)+" not found")

    def print_all_graphs(self,language="pt"):
        self._language = language
        self.graph_01() #Raw Table
        self.graph_02() 
        self.graph_03()
        self.graph_04() #Area Chart
        # self.graph_05() #Arc Diagram

# instance = V009()
# instance.generate_dataset(number_actions = 100, video_size = 30)
# res = instance.graph_03()

# for i in range(0,30+1):
    

