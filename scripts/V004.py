import pandas as pd
import numpy as np

from plotly.graph_objs import Figure, Layout, Bar, Table, Heatmap, Scatter
from plotly.offline import init_notebook_mode, iplot

init_notebook_mode(connected=True) # initiate notebook for offline plot

class V004:
    NUMBER_STUDENTS = 20
    DATASET = pd.DataFrame()
    
    _language = "pt"
    _material_name = []
    _df_sum = []

    def __init__(self, number_students = 20, language = "pt"):
        self.NUMBER_STUDENTS = number_students
        self._language = language
        self.generate_dataset()
    
    def generate_dataset(self):
        video_dur = []
        video_dur = [np.random.randint(240,600) for n in range(7)] #video duration ranging between 240 and 600 seconds
        self._material_name = ['Video1','Video2','Video3','Video4','Video5']
        names = pd.read_csv("names.csv")

        self.DATASET = pd.DataFrame(columns=['Students',str(self._material_name[0])+' ('+str(video_dur[0])+'s)',
                        str(self._material_name[1])+' ('+str(video_dur[1])+'s)',str(self._material_name[2])+' ('+str(video_dur[2])+'s)',
                        str(self._material_name[3])+' ('+str(video_dur[3])+'s)',str(self._material_name[4])+' ('+str(video_dur[4])+'s)','Total'])
        
        list_aux = []
        for i in range(0,self.NUMBER_STUDENTS):
            for j  in range(0,len(self.DATASET.columns)):
                list_aux.append(
                        [np.random.randint(5,video_dur[j]) for n in range(np.random.randint(0,5))] #user access ranging between  
                    )                                                                       
            self.DATASET.loc[i] = list_aux
            self.DATASET.loc[i,"Students"] = names.group_name[np.random.randint(0,len(names.group_name)+1)]
            list_aux.clear()

        self.DATASET["Total"] = self.DATASET.apply(self.sum_times, axis=1)

        self._df_sum = pd.DataFrame(columns=self._material_name)
        self._df_sum.insert(loc=0,column="Students",value=self.DATASET.Students)
        self._df_sum.insert(loc=len(self._material_name)+1,column="Total",value=self.DATASET.Total) #Add into the self._df_sum a column to assign Total values
        
        lst = self.DATASET.columns[1:].tolist() #Get all columns after students
        for i in range(0, self.NUMBER_STUDENTS):
            for j in range(0,len(lst)-1): #Iterate all columns, except Total                
                sum_value = sum(self.DATASET.loc[i,lst[j]])                
                self._df_sum.loc[i,self._material_name[j]] = sum_value
        
        # print(self._df_sum)

    def sum_times(self,row):
        lst = self.DATASET.columns[1:].tolist()
        sum_value = 0
        for i in range(len(lst)-1):
            sum_value += sum(row[lst[i]])

        return sum_value    

    # Table presenting raw data    
    def graph_01(self):
        df = self.DATASET.sort_values(by=["Students"])
        
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
        df = self._df_sum.sort_values(by=["Students"])
        
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

    def graph_03(self):
        legend = {"title":"Tempo de acesso aos vídeos por estudante",
                    "xaxis":"",
                    "yaxis":"",
                }
        if (self._language == "en"):
            legend = {"title":"Length of access to videos grouped by student",
                        "xaxis":"",
                        "yaxis":"",
                    }
        # https://plot.ly/python/bubble-charts/
        # https://plot.ly/python/reference/#layout-xaxis
        # https://plot.ly/python/axes/#subcategory-axes
        df = self._df_sum.sort_values(by=["Students"])
        max_value = 0        
        sum_value = 0
        
        for i in range(1,len(df.columns)-1): #Iterate all columns, except Total
            max_local = max(df.iloc[1:,i].values.tolist())
            max_value = max(max_local,max_value)
                
        # sizeref = max_value/(max_value**3)
        sizeref=4.5*max_value/(max_value)        
        # print (max_value)
        # print(sizeref)
        trace = []
        for i in range(0, self.NUMBER_STUDENTS):
            trace.append(
                Scatter(
                    x=[df.iloc[i,0]]*len(df.columns[1:]), #student
                    y=df.columns[1:], #videos
                    mode='markers',
                    name=df.iloc[i,0], #each student name                    
                    # orientation = "h",
                    text = df.iloc[i,1:].values.tolist(),
                    # text = str(s),
                    marker=dict(
                        symbol='circle',
                        sizemode='area',
                        sizeref=sizeref,
                        # size=df.iloc[:,i].values.tolist(),
                        size=df.iloc[i,1:].values.tolist(),
                        color="rgb(0,0,255)",
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
                # categoryorder = "category ascending",
                # domain = [0, 1],
                fixedrange = False,
                range = [-1, len(df)],
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
                # categoryorder = "category descending",
                # domain = [0, 1],
                fixedrange = False,
                range = [-1, len(df.columns[1:])],
                rangemode = "normal",
                showline = True,                
                type = "category"
            )
        )

        data = trace
        fig=Figure(data=data, layout=layout)
        iplot(fig, filename='bubblechart-size')

    def graph_04(self):
        legend = {"title":"Tempo de acesso aos vídeos por estudante",
                    "xaxis":"",
                    "yaxis":"Tempo de acesso em segundos",
                }
        if (self._language == "en"):
            legend = {"title":"Length of access to videos grouped by student",
                        "xaxis":"",
                        "yaxis":"Length of access in seconds",
                    }
        df = self._df_sum.sort_values(by=["Students"])
        trace = []
        for i in range(1,len(df.columns[1:])):
            trace.append(Bar(
                    x=df.Students.values,
                    y=df.iloc[:,i].values,
                    name=df.columns[i]
                    # name=df.iloc[i,0], #each student name
            ))

        data = trace
        layout = Layout(
                title=legend['title'],
                xaxis = dict(
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
                    dtick=100,
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
        legend = {"title":"Tempo de acesso aos vídeos por estudante",
                    "xaxis":"",
                    "yaxis":"Tempo de acesso em segundos",
                }
        if (self._language == "en"):
            legend = {"title":"Length of access to videos grouped by student",
                        "xaxis":"",
                        "yaxis":"Length of access in seconds",
                    }
        df = self._df_sum.sort_values(by=["Students"])
        trace = []
        for i in range(1,len(df.columns[1:])):
            trace.append(Bar(
                    x=df.Students.values,
                    y=df.iloc[:,i].values,
                    name=df.columns[i]
                    # name=df.iloc[i,0], #each student name
            ))

        data = trace
        layout = Layout(
                title=legend['title'],
                barmode='stack',
                xaxis = dict(
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
                    dtick=300,
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
        legend = {"title":"Tempo de acesso aos vídeos por estudante",
                    "xaxis":"",
                    "yaxis":"Tempo de acesso em segundos",
                }
        if (self._language == "en"):
            legend = {"title":"Length of access to videos grouped by student",
                        "xaxis":"",
                        "yaxis":"Length of access in seconds",
                    }        
        df = self._df_sum.sort_values(by=["Total","Students"])
        trace = []
        for i in range(1,len(df.columns[1:])):
            trace.append(Bar(
                    x=df.Students.values,
                    y=df.iloc[:,i].values,
                    name=df.columns[i]
                    # name=df.iloc[i,0], #each student name
            ))

        data = trace
        layout = Layout(
                title=legend['title'],
                barmode='stack',
                xaxis = dict(
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
                    dtick=300,
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
        legend = {"title":"Tempo de acesso aos vídeos por estudante",
                    "xaxis":"Tempo de acesso em segundos",
                    "yaxis":"",
                }
        if (self._language == "en"):
            legend = {"title":"Length of access to videos grouped by student",
                        "xaxis":"Length of access in seconds",
                        "yaxis":"",
                    }
        df = self._df_sum.sort_values(by=["Students"])
        trace = []
        for i in range(1,len(df.columns[1:])):
            trace.append(Bar(
                    x=df.iloc[:,i].values,
                    y=df.Students.values,
                    name=df.columns[i],
                    orientation = 'h'
                    # name=df.iloc[i,0], #each student name
            ))
        
        data = trace
        layout = Layout(
                title=legend['title'],
                barmode='stack',
                xaxis = dict(
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

    def graph_08(self):
        legend = {"title":"Tempo de acesso aos vídeos por estudante",
                    "xaxis":"Tempo de acesso em segundos",
                    "yaxis":"",
                }
        if (self._language == "en"):
            legend = {"title":"Length of access to videos grouped by student",
                        "xaxis":"Length of access in seconds",
                        "yaxis":"",
                    }
        df = self._df_sum.sort_values(by=["Total","Students"])
        trace = []
        for i in range(1,len(df.columns[1:])):
            trace.append(Bar(
                    x=df.iloc[:,i].values,
                    y=df.Students.values,
                    name=df.columns[i],
                    orientation = 'h'
                    # name=df.iloc[i,0], #each student name
            ))
        
        data = trace
        layout = Layout(
                title=legend["title"],
                barmode='stack',
                xaxis = dict(
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

    def print_all_graphs(self,language="pt"):
        self._language = language
        self.graph_01() #Table
        self.graph_02()
        self.graph_03() #Scatter
        self.graph_04() #Bar
        self.graph_05()
        self.graph_06()
        self.graph_07()
        self.graph_08()

instance = V004(20)
instance.print_all_graphs("pt")
# instance.print_all_graphs("en")