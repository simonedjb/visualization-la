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
                title='Número de acessos nos materiais agrupados por estudante',
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
        trace = Heatmap(z=self.DATASET.iloc[:,1:].values,
                        x=self.DATASET.columns[1:], #Materials
                        y=self.DATASET.iloc[:,0].values, #Students
                        colorscale=[[0, 'rgb(255,255,255)'], [1, 'rgb(0,0,255)']],
                    )

        data = [trace]
        layout = Layout(
                title='Número de acessos nos materiais por estudante',
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

    def graph_04(self):
        # https://plot.ly/python/bubble-charts/
        # https://plot.ly/python/reference/#layout-xaxis
        # https://plot.ly/python/axes/#subcategory-axes
        
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
                    # x=self.DATASET.iloc[:,0].values, #students
                    # x=[self.DATASET.iloc[i,0]], #Students
                    x=[self.DATASET.iloc[i,0]]*len(self.DATASET.columns), #student
                    y=self.DATASET.columns[1:], #materials
                    mode='markers',
                    # name=self.DATASET.iloc[i,0], #each student name
                    name=self.DATASET.iloc[i,0], #student name
                    # orientation = "h",
                    text = self.DATASET.iloc[i,1:].values.tolist(),
                    marker=dict(
                        symbol='circle',
                        sizemode='area',
                        sizeref=sizeref,
                        # size=self.DATASET.iloc[:,i].values.tolist(),
                        size=self.DATASET.iloc[i,1:].values.tolist(),
                        line=dict(
                            width=2
                        )
                    )
                )
            )

        layout = Layout(
            title='Número de acessos nos materiais por estudante',
            # title='Number of access in the materials grouped by student',
            hovermode = "closest",
            showlegend = True,
            xaxis = dict(
                autorange = False,
                # categoryorder = "category ascending",
                # domain = [0, 1],
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
                # domain = [0, 1],
                fixedrange = False,
                range = [-1, len(self.DATASET.columns[1:])],
                rangemode = "normal",
                showline = True,
                title = "Materiais",
                type = "category"
            )
        )

        data = trace
        fig=Figure(data=data, layout=layout)
        iplot(fig, filename='bubblechart-size')        

    def print_all_graphs(self):
        self.graph_01()
        self.graph_02()
        self.graph_03()
        self.graph_04()

instance = V002(20)
instance.print_all_graphs()