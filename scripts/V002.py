import pandas as pd
import numpy as np

from plotly.graph_objs import Figure, Layout, Bar, Table, Heatmap, Scatter
from plotly.offline import init_notebook_mode, iplot

init_notebook_mode(connected=True) # initiate notebook for offline plot

class V002:
    NUMBER_STUDENTS = 21
    DATASET = pd.DataFrame()
    
    _language = "pt"

    def __init__(self, number_students = 21, language = "pt"):
        self.NUMBER_STUDENTS = number_students+1
        self._language = language
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
        legend = {"title":"Número de acessos nos materiais agrupados por estudante",
                    "xaxis":"",
                    "yaxis":"Número de acessos",
                }
        if (self._language == "en"):
            legend = {"title":"Number of access in the materials grouped by student",
                        "xaxis":"",
                        "yaxis":"Number of access",
                    }
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
                title=legend["title"],
                xaxis=dict(
                    title = legend["xaxis"],
                    titlefont=dict(
                        # family='Arial, sans-serif',
                        # size=18,
                        color='rgb(180,180,180)',
                    ),
                ),
                yaxis=dict(
                    title = legend["yaxis"],
                    titlefont=dict(
                        # family='Arial, sans-serif',
                        # size=18,
                        color='rgb(180,180,180)',
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
        legend = {"title":"Número de acessos nos materiais agrupados por estudante",
                    "xaxis":"",
                    "yaxis":"Número de acessos",
                }
        if (self._language == "en"):
            legend = {"title":"Number of access in the materials grouped by student",
                        "xaxis":"",
                        "yaxis":"Number of access",
                    }
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
                title=legend["title"],
                barmode='stack',
                xaxis=dict(
                    title = legend["xaxis"],
                    titlefont=dict(
                        # family='Arial, sans-serif',
                        # size=18,
                        color='rgb(180,180,180)',
                    ),
                ),
                yaxis=dict(
                    title = legend["yaxis"],
                    titlefont=dict(
                        # family='Arial, sans-serif',
                        # size=18,
                        color='rgb(180,180,180)',
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
        legend = {"title":"Número de acessos nos materiais agrupados por estudante e ordenados pelo total de acesso",
                    "xaxis":"",
                    "yaxis":"Número de acessos",
                }
        if (self._language == "en"):
            legend = {"title":"Number of access in the materials grouped by student sorted by total access",
                        "xaxis":"",
                        "yaxis":"Number of access",
                    }
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
                title=legend["title"],
                barmode='stack',
                xaxis=dict(
                    title = legend["xaxis"],
                    titlefont=dict(
                        # family='Arial, sans-serif',
                        # size=18,
                        color='rgb(180,180,180)',
                    ),
                ),
                yaxis=dict(
                    title = legend["yaxis"],
                    titlefont=dict(
                        # family='Arial, sans-serif',
                        # size=18,
                        color='rgb(180,180,180)',
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
        legend = {"title":"Número de acessos nos materiais agrupados por estudante",
                    "xaxis":"Número de acessos",
                    "yaxis":"",
                }
        if (self._language == "en"):
            legend = {"title":"Number of access in the materials grouped by student",
                        "xaxis":"Number of access",
                        "yaxis":"",
                    }
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
                title=legend["title"],
                barmode='stack',
                xaxis=dict(
                    title = legend["xaxis"],
                    titlefont=dict(
                        # family='Arial, sans-serif',
                        # size=18,
                        color='rgb(180,180,180)',
                    ),
                ),
                yaxis=dict(
                    title = legend["yaxis"],
                    titlefont=dict(
                        # family='Arial, sans-serif',
                        # size=18,
                        color='rgb(180,180,180)',
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
        legend = {"title":"Número de acessos nos materiais agrupados por estudante e ordenados pelo total de acesso",
                    "xaxis":"Número de acessos",
                    "yaxis":"",
                }
        if (self._language == "en"):
            legend = {"title":"Number of access in the materials grouped by student sorted by total access",
                        "xaxis":"Number of access",
                        "yaxis":"",
                    }
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
                title = legend["title"],                
                barmode='stack',
                xaxis=dict(
                    title = legend["xaxis"],
                    titlefont=dict(
                        # family='Arial, sans-serif',
                        # size=18,
                        color='rgb(180,180,180)',
                    ),
                ),
                yaxis=dict(
                    title = legend["yaxis"],
                    titlefont=dict(
                        # family='Arial, sans-serif',
                        # size=18,
                        color='rgb(180,180,180)',
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
        legend = {"title":"Número de acessos nos materiais por estudante",
                    "xaxis":"",
                    "yaxis":"",
                }
        if (self._language == "en"):
            legend = {"title":"Number of access in the materials by student",
                        "xaxis":"",
                        "yaxis":"",
                    }
        df = self.DATASET.sort_values(by=["Students"])
        z = []
        for i in range (1, len(df.columns)-1):
            z.append(df.iloc[:,i].values.tolist())
        
        trace = Heatmap(z=z,
                        y=df.columns[1:len(df.columns)-1], #Assigns
                        x=df.iloc[:,0], #Students
                        colorscale=[[0, 'rgb(255,255,255)'], [1, 'rgb(0,0,255)']],
                        showscale = True
                    )
        
        layout = Layout(
                # title='Número de acessos nos materiais por estudante',
                title=legend["title"],
                autosize=False,
                width=950,
                height=350,
                hovermode = "closest",                
                xaxis=dict(
                    title = legend["xaxis"],
                    titlefont=dict(
                        # family='Arial, sans-serif',
                        # size=18,
                        color='rgb(180,180,180)',
                    ),
                ),                
                yaxis=dict(
                    title = legend["yaxis"],
                    titlefont=dict(
                        # family='Arial, sans-serif',
                        # size=18,
                        color='rgb(180,180,180)',
                    ),
                    showticklabels=True,
                    type="category",                    
                    tick0=0,
                    dtick=1,
                    exponentformat='e',
                    showexponent='all',
                    gridcolor='#bdbdbd',
                )
            )

        data = [trace]
        fig = Figure(data=data, layout=layout)
        iplot(fig, filename='Heatmap')

    def graph_08(self):
        legend = {"title":"Número de acessos nos materiais por estudante",
                    "xaxis":"",
                    "yaxis":"",
                }
        if (self._language == "en"):
            legend = {"title":"Number of access in the materials by student",
                        "xaxis":"",
                        "yaxis":"",
                    }
        df = self.DATASET.sort_values(by=["Students"])
        z = []
        max_value = 0
        
        for i in range (1, len(df.columns)-1):
            z.append(df.iloc[:,i].values.tolist())
            max_local = max(df.iloc[:,i].values.tolist())
            max_value = max(max_local,max_value)
        
        trace = Heatmap(z=z,
                        y=df.columns[1:len(df.columns)-1],
                        x=df.iloc[:,0], #Students
                        colorscale=[[0, 'rgb(255,255,255)'], [1, 'rgb(0,0,255)']],
                        showscale = True
                    )

        annotations=[]
        for i in range(1,len(df.columns)-1):
            for j in range(0,len(df)):
                color = 'rgb(0,0,0)'
                if df.iloc[j,i] > max_value/2:
                    color = 'rgb(255,255,255)'
                annotations.append({
                    "text":str(df.iloc[j,i]),
                    "y":df.columns.values[i],
                    "x":df.iloc[j,0],
                    "xref":'x1', 
                    "yref":'y1',
                    "showarrow":False,
                    "font":{
                        # family='Courier New, monospace',
                        # size=16,
                        "color":color
                    }
                })
        
        layout = Layout(
                title = legend["title"],
                autosize=False,
                width=950,
                height=350,
                hovermode = "closest",
                xaxis=dict(
                    title = legend["xaxis"],
                    titlefont=dict(
                        # family='Arial, sans-serif',
                        # size=18,
                        color='rgb(180,180,180)',
                    ),
                ),                
                yaxis=dict(
                    title = legend["yaxis"],
                    titlefont=dict(
                        # family='Arial, sans-serif',
                        # size=18,
                        color='rgb(180,180,180)',
                    ),
                    showticklabels=True,
                    type="category",                    
                    tick0=0,
                    dtick=1,
                    exponentformat='e',
                    showexponent='all',
                    gridcolor='#bdbdbd',                    
                ),
                annotations = annotations
            )

        data = [trace]
        fig = Figure(data=data, layout=layout)
        iplot(fig, filename='Heatmap')

    def graph_09(self):
        legend = {"title":"Número de acessos nos materiais por estudante",
                    "xaxis":"",
                    "yaxis":"",
                }
        if (self._language == "en"):
            legend = {"title":"Number of access in the materials grouped by student",
                        "xaxis":"",
                        "yaxis":"",
                    }
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
                    x=[df.iloc[i,0]]*(len(df.columns)-2), #student
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
            title=legend["title"],
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
                # categoryorder = "category ascending",
                # domain = [0, 1],
                fixedrange = False,
                range = [-1, len(self.DATASET)],
                rangemode = "normal",
                showline = True,                
                type = "category"
            ),
            yaxis = dict(
                title = legend["yaxis"],
                titlefont=dict(
                    # family='Arial, sans-serif',
                    # size=18,
                    color='rgb(180,180,180)',
                ),
                autorange = False,
                categoryorder = "category ascending",
                # domain = [0, 1],
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

    def print_all_graphs(self,language="pt"):
        self._language = language
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
# instance.print_all_graphs("pt")
instance.print_all_graphs("en")