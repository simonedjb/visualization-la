import pandas as pd
import numpy as np

from plotly.graph_objs import Figure, Layout, Bar, Table, Heatmap, Scatter
from plotly.offline import init_notebook_mode, iplot


init_notebook_mode(connected=True) # initiate notebook for offline plot

class V003:
    NUMBER_STUDENTS = 21
    DATASET = pd.DataFrame()

    _students = pd.DataFrame()
    _assigns = pd.DataFrame()

    def __init__(self, number_students = 21):
        self.NUMBER_STUDENTS = number_students+1
        self.generate_dataset()

    def generate_dataset(self):
        self.DATASET = pd.DataFrame(columns=["Students","Hits","Readings","Posts"])
        for i in range(1,self.NUMBER_STUDENTS):
            self.DATASET.loc[i] = [np.random.randint(0,20) for n in range(len(self.DATASET.columns))]
            self.DATASET.loc[i,"Students"] = "Student_"+str(i)

        self.get_students_frame()
        self.get_interactions_frame()

    def print_dataset(self):
        print(self.DATASET)

    def get_student(self, row):
        return row["Students"]

    def get_students_frame(self):
        self._students = pd.DataFrame(columns=["Name"])
        self._students["Name"] = self.DATASET.apply(self.get_student, axis=1)
        # print (self._students)

    def get_interactions_frame(self):
        self._interactions = pd.DataFrame(columns=["Name"])
        for i in range (0, len(self.DATASET.columns[1:])):
            self._assigns.loc[i,"Name"] = self.DATASET.columns[i+1]
        # print (self._assigns)

    # Table presenting raw data
    def graph_01(self):
        df = self.DATASET
        # df.replace(value="", to_replace=0, inplace=True)
        # df.replace(value="x", to_replace=1, inplace=True)

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
        trace = []
        for i in range(len(self.DATASET.columns[1:])):
            trace.append(Bar(
                    x=self.DATASET.Students.values,
                    y=self.DATASET.iloc[:,i+1].values,
                    name=self.DATASET.columns[i+1]
            ))

        data = trace
        layout = Layout(
                title='Número de acessos a Posts, Leituras e Likes agrupados por estudante',
                # title='Number of access in the materials grouped by student',
                yaxis=dict(
        #             title='AXIS TITLE',
                    titlefont=dict(
                        family='Arial, sans-serif',
        #                 size=18,
                        color='lightgrey'
                    ),
                    showticklabels=True,
                    tick0=0,
                    dtick=1,
        #             ticklen=4,
        #             tickwidth=4,
                    exponentformat='e',
                    showexponent='all',
                    gridcolor='#bdbdbd',
        #             range=[0, 4.1]
                )
            )

        fig = Figure(data=data, layout=layout)
        iplot(fig, filename='012_2')

    def graph_03(self):

        max_value=0
        for i in range(0, len(self.DATASET)): #Take the max value in whole dataframe
            if max(self.DATASET.iloc[:,1:].values[i]) > max_value:
                max_value = max(self.DATASET.iloc[:,1:].values[i])

        sizeref = 2.*max_value/(max_value**2)
        # print (sizeref)

        trace = []
        # for i in range(1, len(self.DATASET.columns)):
        for i in range(0, len(self.DATASET)):
            trace.append(
                Scatter(
                    x=[self.DATASET.iloc[i,0]]*len(self.DATASET.columns), #student
                    y=self.DATASET.columns[1:], #materials
                    mode='markers',
                    name=self.DATASET.iloc[i,0], #student name
                    text = self.DATASET.iloc[i,1:].values.tolist(),
                    marker=dict(
                        symbol='circle',
                        sizemode='area',
                        sizeref=sizeref,
                        size=self.DATASET.iloc[i,1:].values.tolist(),
                        line=dict(
                            width=2
                        )
                    )
                )
            )

        layout = Layout(
            title='Número de acessos a Posts, Leituras e Likes por estudante',
            # title='Number of access in the materials grouped by student',
            hovermode = "closest",
            showlegend = True,
            xaxis = dict(
                autorange = False,
                # categoryorder = "category ascending",
                fixedrange = False,
                range = [-1, len(self.DATASET)],
                rangemode = "normal",
                showline = True,
                title = "Estudantes",
                type = "category"
            ),
            yaxis = dict(
                autorange = False,
                categoryorder = "category ascending",
                fixedrange = False,
                range = [-1, len(self.DATASET.columns[1:])],
                rangemode = "normal",
                showline = True,
                type = "category"
            )
        )

        data = trace
        fig=Figure(data=data, layout=layout)
        iplot(fig, filename='bubblechart-size')

    def graph_04(self):
        trace = Heatmap(z=self.DATASET.iloc[:,1:].values,
                        x=self.DATASET.columns[1:], #Forum actions
                        y=self.DATASET.iloc[:,0].values, #Students
                        colorscale=[[0, 'rgb(255,255,255)'], [1, 'rgb(0,0,255)']],
                    )

        data = [trace]
        layout = Layout(
                title='Número de acessos a Posts, Leituras e Likes por estudante',
                # title='Number of access in the materials by student',
                yaxis=dict(
        #             title='AXIS TITLE',
                    titlefont=dict(
                        family='Arial, sans-serif',
        #                 size=18,
                        color='lightgrey'
                    ),
                    showticklabels=True,
                    tick0=0,
                    dtick=1,
        #             ticklen=4,
        #             tickwidth=4,
                    exponentformat='e',
                    showexponent='all',
                    gridcolor='#bdbdbd',
        #             range=[0, 4.1]
                )
            )

        fig = Figure(data=data, layout=layout)
        iplot(fig, filename='012_3')

    def print_all_graphs(self):
        self.graph_01()
        self.graph_02()
        self.graph_03()
        self.graph_04()

instance = V003(20)
instance.print_all_graphs()
