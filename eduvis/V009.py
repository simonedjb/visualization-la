import dash
import dash_core_components as dcc
import dash_html_components as html
import random

import pandas as pd
import numpy as np

from plotly.graph_objs import Figure, Layout, Bar, Table, Heatmap, Scatter, Box, Violin
from plotly.offline import init_notebook_mode, iplot

from sklearn import metrics
from sklearn.cluster import KMeans


init_notebook_mode(connected=True) # initiate notebook for offline plot

class V009:
    NUMBER_STUDENTS = 50
    DATASET = pd.DataFrame()

    _language = "pt"
    _type_result="jupyter-notebook"

    def __init__(self, language="pt", type_result = "jupyter-notebook"):
        self._language = language
        self._type_result = type_result

    def generate_dataset(self, number_students = 20):
        self.NUMBER_STUDENTS = number_students

        names = pd.read_csv("names.csv")
        self.DATASET = pd.DataFrame(columns=["Students","Action","Age"])

        self.DATASET.Age = np.random.triangular(18,30,70,self.NUMBER_STUDENTS)
        self.DATASET["Age"] = self.DATASET.apply(self.convert_to_int, axis=1)

        rand_names = [names.group_name[np.random.randint(0,len(names.group_name)+1)] for n in range(0,self.NUMBER_STUDENTS)]
        rand_names.sort()

        k = 0

        for i in range(0,self.NUMBER_STUDENTS//5):
            playrequired = True
            currentTime = 0

            for j in range(0,5):
                timeModifierFrom = int(currentTime + np.random.triangular(2,5,20))
                timeModifierTo = int(np.random.triangular(0,currentTime,120))

                self.DATASET.loc[k,"Students"] = rand_names[i]

                if(playrequired == True):
                    playrequired = False
                    self.DATASET.loc[k,"Action"] = 'Play %ds'%currentTime
                    lastAction = 'Play'

                elif(lastAction == 'Pause'):

                    currentAction = random.choice(['Play', 'Seek'])

                    if(currentAction == 'Play'):
                        self.DATASET.loc[k,"Action"] = 'Play %ds'%currentTime
                        lastAction = 'Play'

                    elif(currentAction == 'Seek'):
                        self.DATASET.loc[k,"Action"] = 'Seek from %ds to %ds'%(timeModifierFrom, timeModifierTo)
                        currentTime = timeModifierTo
                        lastAction = 'Seek'

                else:
                    currentAction = random.choice(['Seek', 'Pause'])

                    if(currentAction == 'Pause'):
                        self.DATASET.loc[k,"Action"] = 'Pause %ds'%timeModifierFrom
                        currentTime = timeModifierFrom
                        lastAction = 'Pause'

                    elif(currentAction == 'Seek'):
                        self.DATASET.loc[k,"Action"] = 'Seek from %ds to %ds'%(timeModifierFrom,timeModifierTo)
                        currentTime = timeModifierTo
                        lastAction = 'Seek'

                k+= 1


    def convert_to_int(self,row):
        return int(row["Age"])

    # Table presenting raw data
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
                id='V009@1',
                figure={"data": data}
            )
    def print_all_graphs(self,language="pt"):
        self._language = language
        self.graph_01() #Table
