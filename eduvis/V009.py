import dash
import dash_core_components as dcc
import dash_html_components as html
import random

import plotly.plotly as py
import plotly.tools as tls

import pandas as pd
import numpy as np


from plotly.graph_objs import Figure, Layout, Bar, Table, Heatmap, Scatter, Box, Violin
from plotly.offline import init_notebook_mode, iplot


from sklearn import metrics
from sklearn.cluster import KMeans


init_notebook_mode(connected=True) # initiate notebook for offline plot

class V009:
    NUMBER_ACTIONS = 50
    VIDEO_SIZE = 120
    RAWDATASET = pd.DataFrame()
    PROCDATASET = pd.DataFrame()

    _language = "pt"
    _type_result="jupyter-notebook"

    def __init__(self, language="pt", type_result = "jupyter-notebook"):
        self._language = language
        self._type_result = type_result

    def generate_dataset(self, number_actions = 20, video_size = 120):
        self.NUMBER_ACTIONS = number_actions
        self.VIDEO_SIZE = video_size

        names = pd.read_csv("names.csv")
        self.RAWDATASET = pd.DataFrame(columns=["Students","Action","Age"])
        self.PROCDATASET = pd.DataFrame(0, index= range(video_size), columns=["Time","Play","Pause","Seek from","Seek to"])
        for i in range(0,video_size): self.PROCDATASET.loc[i,"Time"] = i

        rand_names = [names.group_name[np.random.randint(0,len(names.group_name)+1)] for n in range(0,self.NUMBER_ACTIONS)]
        rand_names.sort()

        k = 0

        for i in range(0,self.NUMBER_ACTIONS//5):
            playrequired = True
            currentTime = 0

            for j in range(0,5):
                timeModifierFrom = int(currentTime + np.random.triangular(0, (video_size - currentTime - 5)//2 ,video_size - currentTime - 5))
                timeModifierTo = int(np.random.triangular(0,currentTime,video_size))

                self.RAWDATASET.loc[k,"Students"] = rand_names[i]

                if(playrequired == True):
                    playrequired = False
                    self.RAWDATASET.loc[k,"Action"] = 'Play %ds'%currentTime
                    lastAction = 'Play'
                    self.PROCDATASET.loc[currentTime,"Play"] += 1

                elif(lastAction == 'Pause'):

                    currentAction = random.choice(['Play', 'Seek'])

                    if(currentAction == 'Play'):
                        self.RAWDATASET.loc[k,"Action"] = 'Play %ds'%currentTime
                        lastAction = 'Play'
                        self.PROCDATASET.loc[currentTime,"Play"] += 1


                    elif(currentAction == 'Seek'):
                        self.RAWDATASET.loc[k,"Action"] = 'Seek from %ds to %ds'%(currentTime, timeModifierTo)
                        currentTime = timeModifierTo
                        lastAction = 'Seek'

                else:
                    currentAction = random.choice(['Seek', 'Pause'])

                    if(currentAction == 'Pause'):
                        self.RAWDATASET.loc[k,"Action"] = 'Pause %ds'%timeModifierFrom
                        currentTime = timeModifierFrom
                        self.PROCDATASET.loc[currentTime,"Pause"] += 1
                        lastAction = 'Pause'

                    elif(currentAction == 'Seek'):
                        self.RAWDATASET.loc[k,"Action"] = 'Seek from %ds to %ds'%(timeModifierFrom,timeModifierTo)
                        currentTime = timeModifierTo
                        self.PROCDATASET.loc[timeModifierFrom,"Seek from"] += 1
                        self.PROCDATASET.loc[timeModifierTo,"Seek to"] += 1
                        lastAction = 'Seek'

                k+= 1

        df = self.PROCDATASET
        df2 = df.set_index("Time")
        x= df.index.get_level_values(0).values
        print(x)
        y=df.iloc[:,2].tolist()
        print(y)
        j = df.iloc[0,1:].tolist()
        #print(j)



    # Table presenting raw data
    def graph_01(self):
        df = self.RAWDATASET

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
                id='V009@1',
                figure={"data": data}
            )

    # Table presenting processed data
    def graph_02(self):
        df = self.PROCDATASET

        trace = Table(
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
        )

        data = [trace]
        if self._type_result == "jupyter-notebook":
            iplot(data, filename = 'pandas_table')
        elif self._type_result == "dash":
            return dcc.Graph(
                id='V009@1',
                figure={"data": data}
            )


    def graph_03(self):

        legend = {"title":"adicionar titulo",
                    "xaxis":"",
                    "yaxis":"",
                }
        if (self._language == "en"):
            legend = {"title":"adicionar titulo", #bacalhau
                        "xaxis":"",
                        "yaxis":"",
                    }

        color = ["rgb(127,0,0)","rgb(255,0,0)","rgb(127,0,127)","rgb(0,0,255)","rgb(0,127,127)","rgb(0,255,0)"]

        dft = self.PROCDATASET
        df = dft.set_index("Time")

        sizeref = 0.01

        trace = []
        for i in range(0, len(df.columns[1:])):
            trace.append(
                Scatter(
                    x=df.index.get_level_values(0).values, #time
                    y=df.iloc[:,i].tolist(), #actions
                    hoverinfo='x+y',
                    mode='lines',

                    #stackgroup='one'

                )
            )


        layout = Layout(

        )

        data = trace
        fig=Figure(data=data, layout=layout)
        if self._type_result == "jupyter-notebook":
            iplot(fig, filename='Scatter')
        elif self._type_result == "dash":
            return dcc.Graph(
                id='V009@3',
                figure=fig
            )


    def print_all_graphs(self,language="pt"):
        self._language = language
        self.graph_01() #Raw Table
        self.graph_02() #Processed Table
        self.graph_03()
        self.graph_04()
