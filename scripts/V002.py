import pandas as pd
import numpy as np

from plotly.graph_objs import Figure, Layout, Bar, Table, Heatmap, Scatter
from plotly.offline import init_notebook_mode, iplot

init_notebook_mode(connected=True) # initiate notebook for offline plot

class V002:
    NUMBER_STUDENTS = 21
    DATASET = pd.DataFrame()

    def __init__(self, number_students = 21):
        self.NUMBER_STUDENTS = number_students+1
        self.generate_dataset()

    def generate_dataset(self):
        self.DATASET = pd.DataFrame(columns=["Students","Video1","Video2",'Quiz1','Quiz2','Pdf1','Pdf2','Ebook1','Ebook2'])
        for i in range(1,self.NUMBER_STUDENTS):
            self.DATASET.loc[i] = [np.random.randint(0,30) for n in range(len(self.DATASET.columns))]
            self.DATASET.loc[i,"Students"] = "Student_"+str(i) 

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
                title='Number of access in the materials groupes by student',
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
        trace = Heatmap(z=self.DATASET.iloc[:,1:].values,
                        x=self.DATASET.columns[1:], #Materials
                        y=self.DATASET.iloc[:,0].values, #Students
                        colorscale=[[0, 'rgb(255,255,255)'], [1, 'rgb(0,0,255)']],
                    )

        data = [trace]
        layout = Layout(
                title='Number of access in the materials by student',
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

    def graph_04(self):
        trace = Scatter(
            x=self.DATASET.columns[1:], #Materials
            y=self.DATASET.iloc[:,0].values, #Students
            mode='markers',
            marker=dict(
        #         size=[[40,10], [60], [80], [100]],
            )
        )

        data = [trace]
        iplot(data, filename='bubblechart-size')        

    def print_all_graphs(self):
        self.graph_01()
        self.graph_02()
        self.graph_03()
        self.graph_04()

instance = V002(20)
instance.print_all_graphs()