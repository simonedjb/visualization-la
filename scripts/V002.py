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
        self.DATASET = pd.DataFrame(columns=["Students","Video1","Video2",'Quiz1','Quiz2','Pdf1','Pdf2','Ebook1','Ebook2','Total'])
        names = pd.read_csv("names.csv")

        for i in range(1,self.NUMBER_STUDENTS):
            self.DATASET.loc[i] = [np.random.randint(0,30) for n in range(len(self.DATASET.columns))]            
            self.DATASET.loc[i,"Students"] = names.group_name[np.random.randint(0,len(names.group_name)+1)]
        
        self.DATASET['Total'] = self.DATASET.apply(self.sum_row,axis=1)

    def sum_row(self,row):
        total = 0
        for i in range(1, len(row[1:])):
            total += row[i]

        return total

    # Table presenting raw data    
    def graph_01(self):
        df = self.DATASET.sort_values(by=["Students"])
        
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
        iplot(data, filename = 'pandas_table')

    def graph_02(self):
        df = self.DATASET.sort_values(by=["Students"])
        trace = []
        for i in range(1,len(df.columns[1:len(df.columns)])):
            trace.append(Bar(
                    x=df.Students.values,
                    y=df.iloc[:,i].values,
                    name=df.columns[i]
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
                    dtick=5,
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
        df = self.DATASET.sort_values(by=["Students"])
        trace = []
        for i in range(1,len(df.columns[1:len(df.columns)])):
            trace.append(Bar(
                    x=df.Students.values,
                    y=df.iloc[:,i].values,
                    name=df.columns[i]
            ))

        data = trace
        layout = Layout(
                title='Número de acessos nos materiais agrupados por estudante',
                # title='Number of access in the materials grouped by student',
                barmode='stack',
                yaxis=dict(
        #             title='AXIS TITLE',
                    titlefont=dict(
                        family='Arial, sans-serif',
        #                 size=18,
                        color='lightgrey'
                    ),
                    showticklabels=True,
                    tick0=0,
                    dtick=15,
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

    def graph_04(self):
        df = self.DATASET.sort_values(by=["Total","Students"])
        
        trace = []
        for i in range(1,len(df.columns[1:len(df.columns)])):
            trace.append(Bar(
                    x=df.Students.values,
                    y=df.iloc[:,i].values,
                    name=df.columns[i]
            ))

        data = trace
        layout = Layout(
                title='Número de acessos nos materiais agrupados por estudante',
                # title='Number of access in the materials grouped by student',
                barmode='stack',
                yaxis=dict(
        #             title='AXIS TITLE',
                    titlefont=dict(
                        family='Arial, sans-serif',
        #                 size=18,
                        color='lightgrey'
                    ),
                    showticklabels=True,
                    tick0=0,
                    dtick=15,
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

    def graph_05(self):
        df = self.DATASET.sort_values(by=["Students"])
        trace = []
        for i in range(1,len(df.columns[1:len(df.columns)])):
            trace.append(Bar(
                    x=df.iloc[:,i].values,
                    y=df.Students.values,
                    name=df.columns[i],
                    orientation = 'h'
            ))

        data = trace
        layout = Layout(
                title='Número de acessos nos materiais agrupados por estudante',
                # title='Number of access in the materials grouped by student',
                barmode='stack',
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

    def graph_06(self):
        df = self.DATASET.sort_values(by=["Total","Students"])
        trace = []
        for i in range(1,len(df.columns[1:len(df.columns)])):
            trace.append(Bar(
                    x=df.iloc[:,i].values,
                    y=df.Students.values,                    
                    name=df.columns[i],
                    orientation = 'h'
            ))

        data = trace
        layout = Layout(
                title='Número de acessos nos materiais agrupados por estudante',
                # title='Number of access in the materials grouped by student',
                barmode='stack',
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

    def graph_07(self):
        df = self.DATASET.sort_values(by=["Students"])
        
        trace = Heatmap(z=df.iloc[:,1:len(df.columns)-1].values,
                        x=df.columns[1:len(df.columns)-1], #Materials
                        y=df.iloc[:,0].values, #Students
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
        iplot(fig, filename='Heatmap')

    def graph_08(self):
        df = self.DATASET.sort_values(by=["Students"])
        
        trace = Heatmap(z=df.iloc[:,1:len(df.columns)-1].values,
                        x=df.columns[1:len(df.columns)-1], #Materials
                        y=df.iloc[:,0].values, #Students
                        colorscale=[[0, 'rgb(255,255,255)'], [1, 'rgb(0,0,255)']],                        
                    )

        annotations=[]
        for i in range(1,len(df.columns)-1):
            for j in range(0,len(df)):
                annotations.append({
                    "text":str(df.iloc[j,i]),
                    "x":df.columns.values[i],
                    "y":df.iloc[j,0],
                    "xref":'x1', 
                    "yref":'y1',
                    "showarrow":False
                })

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
                ),
                annotations = annotations
            )

        fig = Figure(data=data, layout=layout)
        iplot(fig, filename='Heatmap')

    def graph_09(self):
        # https://plot.ly/python/bubble-charts/
        # https://plot.ly/python/reference/#layout-xaxis
        # https://plot.ly/python/axes/#subcategory-axes
        df = self.DATASET.sort_values(by=["Students"])        
        max_value=0
        for i in range(0, len(df)): #Take the max value in whole dataframe
            if max(df.iloc[:,1:len(df.columns)-1].values[i]) > max_value:
                max_value = max(df.iloc[:,1:len(df.columns)-1].values[i])
        
        sizeref = 2.*max_value/(max_value**2)
        # print (sizeref)

        trace = []
        # for i in range(1, len(df.columns)):
        for i in range(0, len(df)):                    
            trace.append(
                Scatter(
                    x=[df.iloc[i,0]]*len(df.columns), #student
                    y=df.columns[1:len(df.columns)-1], #materials
                    mode='markers',
                    # name=df.iloc[i,0], #each student name
                    name=df.iloc[i,0], #student name
                    # orientation = "h",
                    text = df.iloc[i,1:len(df.columns)-1].values.tolist(),
                    marker=dict(
                        symbol='circle',
                        sizemode='area',
                        sizeref=sizeref,
                        size=df.iloc[i,1:len(df.columns)-1].values.tolist(),
                        color = 'rgb(0,0,255)',
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
        self.graph_05()
        self.graph_06()
        self.graph_07()
        self.graph_08()
        self.graph_09()

instance = V002(20)
instance.print_all_graphs()