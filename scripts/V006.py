import pandas as pd
import numpy as np

from plotly.graph_objs import Figure, Layout, Bar, Table, Heatmap, Scatter
from plotly.offline import init_notebook_mode, iplot

from sklearn import metrics
from sklearn.cluster import KMeans


init_notebook_mode(connected=True) # initiate notebook for offline plot

class V006:
    NUMBER_STUDENTS = 50
    DATASET = pd.DataFrame()

    _df_sum = []

    def __init__(self, number_students = 20):
        self.NUMBER_STUDENTS = number_students
        self.generate_dataset()

    def generate_dataset(self):
        self.DATASET = pd.DataFrame(columns=["Students","Age","Forum Posts"])
        for i in range(1,self.NUMBER_STUDENTS):
            self.DATASET.loc[i,"Students"] = "Student_"+str(i)

            self.DATASET.loc[i,"Age"]=np.random.normal(16,80)
            if self.DATASET.loc[i,"Age"] < 20:
                self.DATASET.loc[i,"Forum Posts"]=np.random.triangular(0,3,10)
            elif self.DATASET.loc[i,"Age"] < 30:
                self.DATASET.loc[i,"Forum Posts"]=np.random.triangular(0,2,15)
            elif self.DATASET.loc[i,"Age"] < 40:
                self.DATASET.loc[i,"Forum Posts"]=np.random.triangular(0,7,20)
            elif self.DATASET.loc[i,"Age"] < 50:
                self.DATASET.loc[i,"Forum Posts"]=np.random.triangular(0,9,25)
            elif self.DATASET.loc[i,"Age"] < 60:
                self.DATASET.loc[i,"Forum Posts"]=np.random.triangular(0,11,30)
            elif self.DATASET.loc[i,"Age"] < 70:
                self.DATASET.loc[i,"Forum Posts"]=np.random.triangular(0,15,35)
            elif self.DATASET.loc[i,"Age"] < 80:
                self.DATASET.loc[i,"Forum Posts"]=np.random.triangular(0,20,40)

        self.get_students_frame()
        self.get_interactions_frame()

    def convert_to_int(self,row):
        return int(row["Grade"])

    # Table presenting raw data
    def graph_01(self):
        df = self.DATASET

        trace = Table(
            header=dict(
                values=list(df.columns),
                fill = dict(color='#C2D4FF'),
                align = 'center'
            ),
            cells=dict(
                values=[df[i].tolist() for i in df.columns[:]],
                fill = dict(color='#F5F8FF'),
                align = ['left','center']
            )
        )

        data = [trace]
        iplot(data, filename = 'pandas_table')

    def graph_02(self):
        Clusters = self._df_sum.Cluster.unique()
        color = ["rgb(255,0,0)","rgb(0,0,255)","rgb(255,255,255)","rgb(0,255,0)"]

        trace = []
        for i in range(0, self.NUMBER_STUDENTS):
            trace.append(
                Scatter(
                    x=[self.DATASET.Access[i]], #Access
                    y=[self.DATASET.Grade[i]], #Grade
                    mode='markers',
                    name=self.DATASET.Students[i], #each student name
                    text = [str(self.DATASET.Students[i])],
                    marker=dict(
                        size=12,
                        symbol=self._df_sum.Cluster[i],
                        color = color[self._df_sum.Cluster[i]],
                        colorscale='Viridis',
                        line=dict(
                            width=2
                        )
                    )
                )
            )

        layout = Layout(
            title='Notas dos estudantes vs acesso ao AVA',
            hovermode = "closest",
            showlegend = True,
            xaxis = dict(
                autorange = False,
                fixedrange = False,
                range = [0, self.DATASET.Access.max()+10],
                rangemode = "normal",
                zeroline= False,
                showline = True,
                title = "Acessos ao AVA",
                # type = "category"
            ),
            yaxis = dict(
                autorange = False,
                fixedrange = False,
                range = [0, self.DATASET.Grade.max()+10],
                rangemode = "normal",
                showline = True,
                title = "Notas",
                # type = "category"
            )
        )

        data = trace
        fig = Figure(data=data, layout=layout)
        iplot(fig, filename='scatter-plot')


    def print_all_graphs(self):
        self.graph_01()
        self.graph_02()
        self.graph_03()
        self.graph_04()
        # self.graph_05()

instance = V006(60)
instance.print_all_graphs()
