import pandas as pd
import numpy as np

from plotly.graph_objs import Figure, Layout, Bar, Table, Heatmap, Scatter
from plotly.offline import init_notebook_mode, iplot

init_notebook_mode(connected=True) # initiate notebook for offline plot

class V001:
    NUMBER_STUDENTS = 21
    DATASET = pd.DataFrame()
    
    _students = pd.DataFrame()
    _assigns = pd.DataFrame()
    _language = "pt"

    def __init__(self, number_students = 21, language="pt"):
        self.NUMBER_STUDENTS = number_students+1
        self.language = language
        self.generate_dataset()        

    def generate_dataset(self):
        self.DATASET = pd.DataFrame(columns=["Students","Assign1","Assign2",'Assign3','Assign4'])
        names = pd.read_csv("names.csv")

        for i in range(1,self.NUMBER_STUDENTS):
            self.DATASET.loc[i] = [np.random.randint(0,2) for n in range(len(self.DATASET.columns))]
            self.DATASET.loc[i,"Students"] = names.group_name[np.random.randint(0,len(names.group_name)+1)]

        self.get_students_frame()
        self.get_assigns_frame()

    def sum_assigns(self,row):
        lst = self.DATASET.columns[1:].tolist()
        sum_value = 0
        for i in range(len(lst)):
            sum_value += row[lst[i]]

        return sum_value

    def get_student(self, row):
        return row["Students"]

    def get_students_frame(self):
        self._students = pd.DataFrame(columns=["Name","Total"])
        self._students["Total"] = self.DATASET.apply(self.sum_assigns, axis=1)
        self._students["Name"] = self.DATASET.apply(self.get_student, axis=1)
        # print (self._students)

    def get_assigns_frame(self):
        self._assigns = pd.DataFrame(columns=["Name","Total"])
        for i in range (0, len(self.DATASET.columns[1:])):
            self._assigns.loc[i,"Name"] = self.DATASET.columns[i+1]
            self._assigns.loc[i,"Total"] = self.DATASET[self.DATASET.columns[i+1]].sum()           
        # print (self._assigns)

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
    
    # Barchart number of assign completed for each student
    def graph_02(self):
        legend = {"title":"Quantidade de tarefas feitas por alunos",
                    "xaxis":"",
                    "yaxis":"Número de atividades",
                }
        if (self._language == "en"):
            legend = {"title":"Number of assigns completed by students",
                        "xaxis":"",
                        "yaxis":"Number of assigns",
                    }

        df = self._students.sort_values(by=["Name"])
        trace = [Bar(
            x=df.Name.values,
            y=df.Total.values
        )]

        data = trace
        layout = Layout(
            title = legend["title"],
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
                # ticklen=4,
                # tickwidth=4,
                exponentformat='e',
                showexponent='all',
                gridcolor='#bdbdbd',
                # range=[0, 4.1]
            )
        )

        fig = Figure(data=data, layout=layout)
        iplot(fig, filename='Bar')

    def graph_03(self):
        legend = {"title":"Quantidade de tarefas feitas por alunos",
                    "xaxis":"",
                    "yaxis":"Número de atividades",
                    }
        if (self._language == "en"):
            legend = {"title":"Number of assigns completed by students",
                    "xaxis":"",
                    "yaxis":"Number of assigns",
                    }
                    
        df = self._students.sort_values(by=["Total","Name"])
        trace = [Bar(
            x=df.Name.values,
            y=df.Total.values
        )]
        
        data = trace
        layout = Layout(
            title = legend["title"],
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
                # ticklen=4,
                # tickwidth=4,
                exponentformat='e',
                showexponent='all',
                gridcolor='#bdbdbd',
                # range=[0, 4.1]
            )
        )

        fig = Figure(data=data, layout=layout)
        iplot(fig, filename='011_1')

    def graph_04(self):
        legend = {"title":"Quantidade de tarefas feitas por alunos",
                    "xaxis":"Número de atividades",
                    "yaxis":"",
                    }
        if (self._language == "en"):
            legend = {"title":"Number of assigns completed by students",
                    "xaxis":"Number of assigns",
                    "yaxis":"",
                    }
        df = self._students.sort_values(by=["Name"])
        trace = [Bar(
            x=df.Total.values,
            y=df.Name.values,
            orientation = 'h'
        )]

        data = trace
        layout = Layout(
            title = legend["title"],
            xaxis=dict(
                title = legend["xaxis"],
                titlefont=dict(
                    # family='Arial, sans-serif',
                    # size=18,
                    color='rgb(180,180,180)',
                ),
                tick0=0,
                dtick=1,
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
                # ticklen=4,
                # tickwidth=4,
                exponentformat='e',
                showexponent='all',
                gridcolor='#bdbdbd',
                # range=[0, 4.1]
            )
        )

        fig = Figure(data=data, layout=layout)
        iplot(fig, filename='011_1')

    def graph_05(self):
        legend = {"title":"Quantidade de tarefas feitas por alunos",
                    "xaxis":"Número de atividades",
                    "yaxis":"",
                }
        if (self._language == "en"):
            legend = {"title":"Number of assigns completed by students",
                        "xaxis":"Number of assigns",
                        "yaxis":"",
                    }
        df = self._students.sort_values(by=["Total","Name"])
        trace = [Bar(
            x=df.Total.values,
            y=df.Name.values,
            orientation = 'h'            
        )]

        data = trace
        layout = Layout(
            title = legend["title"],
            xaxis=dict(
                title = legend["xaxis"],
                titlefont=dict(
                    # family='Arial, sans-serif',
                    # size=18,
                    color='rgb(180,180,180)',
                ),
                tick0=0,
                dtick=1,
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
                # ticklen=4,
                # tickwidth=4,
                exponentformat='e',
                showexponent='all',
                gridcolor='#bdbdbd',
                # range=[0, 4.1]
            )
        )

        fig = Figure(data=data, layout=layout)
        iplot(fig, filename='011_1')

    # Lollipop number of assign completed for each student
    def graph_06(self):
        legend = {"title":"Quantidade de tarefas feitas por alunos",
                    "xaxis":"Número de atividades",
                    "yaxis":"",
                    "text_s":"atividades",
                    "text_p":"atividades",
                }
        if (self._language == "en"):
            legend = {"title":"Number of assigns completed by students",
                        "xaxis":"Number of assigns",
                        "yaxis":"",
                        "text_s":"assign",
                        "text_p":"assigns",
                    }
        df = self._students.sort_values(by=["Name"])
        # df = self._students
        trace = []
        trace.append(
            Bar(
                x=df.Total.values,
                y=df.Name.values,
                width=[0.07]*20,
                orientation = 'h',
                name="",
                text="",
                marker=dict(
                        color = 'lightgray',
                        # line=dict(
                        #     color = 'lightgray',
                        #     width=2
                        # )
                    )
            )
        )
        
        for i in range(1, len(self.DATASET.columns)):
            text=str(i)+" "+legend['text_p'],
            if i==1:
                text=str(i)+" "+legend['text_s'],

            trace.append(
                Scatter(
                    x=[i]*len(df.Name.loc[df["Total"]==i]),
                    # x=[3]*20, #student
                    y=df.Name.loc[df["Total"]==i].values.tolist(),
                    mode='markers',
                    # name=self.DATASET.iloc[i,0], #each student name
                    # name=self.DATASET.iloc[i,0], #student name
                    # orientation = "h",
                    name = "",                    
                    text=text*len(df.Name.loc[df["Total"]==i]),                    
                    marker=dict(
                        symbol='circle',
                        sizemode='area',
                        # sizeref=sizeref,
                        # size=self.DATASET.iloc[:,i].values.tolist(),
                        # size=self.DATASET.iloc[i,1:].values.tolist(),
                        color = 'rgb(0,0,255)',
                        line=dict(
                            width=2
                        )
                    )
                )        
            )

        data = trace
        
        layout = Layout(
            title = legend["title"],
            showlegend=False,
            # showgrid=False,
            hovermode = "closest",
            xaxis=dict(
                title = legend["xaxis"],
                titlefont=dict(
                    # family='Arial, sans-serif',
                    # size=18,
                    color='rgb(180,180,180)',
                ),
                tick0=0,
                dtick=1,
                showgrid=True
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
                showgrid=False,
                # ticklen=4,
                # tickwidth=4,
                exponentformat='e',
                showexponent='all',
                gridcolor='#bdbdbd',
                # range=[0, 4.1]
            )
        )

        fig = Figure(data=data, layout=layout)
        iplot(fig, filename='Lollipop')

    def graph_07(self):
        legend = {"title":"Quantidade de tarefas feitas por alunos",
                    "xaxis":"Número de atividades",
                    "yaxis":"",
                    "text_s":"atividades",
                    "text_p":"atividades",
                }
        if (self._language == "en"):
            legend = {"title":"Number of assigns completed by students",
                        "xaxis":"Number of assigns",
                        "yaxis":"",
                        "text_s":"assign",
                        "text_p":"assigns",
                    }
        df = self._students.sort_values(by=["Total","Name"])
        # df = self._students
        trace = []
        trace.append(
            Bar(
                x=df.Total.values,
                y=df.Name.values,
                width=[0.07]*20,
                orientation = 'h',
                name="",
                text="",
                marker=dict(
                        color = 'lightgray',
                        # line=dict(
                        #     color = 'lightgray',
                        #     width=2
                        # )
                    )
            )
        )
        
        for i in range(1, len(self.DATASET.columns)):
            text=str(i)+" "+legend['text_p'],
            if i==1:
                text=str(i)+" "+legend['text_s'],

            trace.append(
                Scatter(
                    x=[i]*len(df.Name.loc[df["Total"]==i]),
                    # x=[3]*20, #student
                    y=df.Name.loc[df["Total"]==i].values.tolist(),
                    mode='markers',
                    # name=self.DATASET.iloc[i,0], #each student name
                    # name=self.DATASET.iloc[i,0], #student name
                    # orientation = "h",
                    name = "",                    
                    text=text*len(df.Name.loc[df["Total"]==i]),                    
                    marker=dict(
                        symbol='circle',
                        sizemode='area',
                        # sizeref=sizeref,
                        # size=self.DATASET.iloc[:,i].values.tolist(),
                        # size=self.DATASET.iloc[i,1:].values.tolist(),
                        color = 'rgb(0,0,255)',
                        line=dict(
                            width=2
                        )
                    )
                )        
            )

        data = trace
        
        layout = Layout(
            title = legend["title"],
            showlegend=False,
            # showgrid=False,
            hovermode = "closest",
            xaxis=dict(
                title = legend["xaxis"],
                titlefont=dict(
                    # family='Arial, sans-serif',
                    # size=18,
                    color='rgb(180,180,180)',
                ),
                tick0=0,
                dtick=1,
                showgrid=True
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
                showgrid=False,
                # ticklen=4,
                # tickwidth=4,
                exponentformat='e',
                showexponent='all',
                gridcolor='#bdbdbd',
                # range=[0, 4.1]
            )
        )

        fig = Figure(data=data, layout=layout)
        iplot(fig, filename='Lollipop')

    # Barchart number of students that have completed each assign
    def graph_08(self):
        legend = {"title":"Quantidade de estudantes que fizeram as tarefas",
                    "xaxis":"",
                    "yaxis":"Número de estudantes",
                }
        if (self._language == "en"):
            legend = {"title":"Number of students that completed the assigns",
                        "xaxis":"",
                        "yaxis":"Number of students",
                    }
        df = self._assigns.sort_values(by=["Name"])
        trace011_2 = [Bar(
            x=df.Name.values,
            y=df.Total.values
        )]
        
        data011_2 = trace011_2
        layout011_2 = Layout(
            title = legend["title"],
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
                # ticklen=4,
                # tickwidth=4,
                exponentformat='e',
                showexponent='all',
                gridcolor='#bdbdbd',
                # range=[0, 13]
            )
        )

        fig011_2 = Figure(data=data011_2, layout=layout011_2)
        iplot(fig011_2, filename='011_2')
    
    def graph_09(self):
        legend = {"title":"Quantidade de alunos que fizeram as tarefas",
                    "xaxis":"",
                    "yaxis":"Número de estudantes",
                }
        if (self._language == "en"):
            legend = {"title":"Number of students that completed the assigns",
                        "xaxis":"",
                        "yaxis":"Number of students",
                    }
        df = self._assigns.sort_values(by=["Total","Name"])
        trace011_2 = [Bar(
            x=df.Name.values,
            y=df.Total.values
        )]

        data011_2 = trace011_2
        layout011_2 = Layout(            
            title = legend["title"],
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
                # ticklen=4,
                # tickwidth=4,
                exponentformat='e',
                showexponent='all',
                gridcolor='#bdbdbd',
                # range=[0, 13]
            )
        )

        fig011_2 = Figure(data=data011_2, layout=layout011_2)
        iplot(fig011_2, filename='011_2')
  
    def graph_10(self):
        legend = {"title":"Quantidade de estudantes que fizeram as tarefas",
                    "xaxis":"Número de estudantes",
                    "yaxis":"",
                }
        if (self._language == "en"):
            legend = {"title":"Number of students that completed the assigns",
                        "xaxis":"Number of students",
                        "yaxis":"",
                    }
        df = self._assigns.sort_values(by=["Name"])
        trace = [Bar(
            x=df.Total.values,
            y=df.Name.values,
            orientation = 'h'            
        )]

        data = trace
        layout = Layout(
            title = legend["title"],
            xaxis=dict(
                title = legend["xaxis"],
                titlefont=dict(
                    # family='Arial, sans-serif',
                    # size=18,
                    color='rgb(180,180,180)',
                ),
                tick0=0,
                dtick=1,
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
                # ticklen=4,
                # tickwidth=4,
                exponentformat='e',
                showexponent='all',
                gridcolor='#bdbdbd',
                # range=[0, 4.1]
            )
        )

        fig = Figure(data=data, layout=layout)
        iplot(fig, filename='011_1')

    def graph_11(self):
        legend = {"title":"Quantidade de estudantes que fizeram as tarefas",
                    "xaxis":"Número de estudantes",
                    "yaxis":"",
                }
        if (self._language == "en"):
            legend = {"title":"Number of students that completed the assigns",
                        "xaxis":"Number of students",
                        "yaxis":"",
                    }
        df = self._assigns.sort_values(by=["Total","Name"])
        trace = [Bar(
            x=df.Total.values,
            y=df.Name.values,
            orientation = 'h'            
        )]

        data = trace
        layout = Layout(
            title = legend["title"],
            xaxis=dict(
                title = legend["xaxis"],
                titlefont=dict(
                    # family='Arial, sans-serif',
                    # size=18,
                    color='rgb(180,180,180)',
                ),
                tick0=0,
                dtick=1,
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
                # ticklen=4,
                # tickwidth=4,
                exponentformat='e',
                showexponent='all',
                gridcolor='#bdbdbd',
                # range=[0, 4.1]
            )
        )

        fig = Figure(data=data, layout=layout)
        iplot(fig, filename='011_1')

    # Lollipop number of students that have completed each assign
    def graph_12(self):
        legend = {"title":"Quantidade de estudantes que fizeram as tarefas",
                    "xaxis":"Número de estudantes",
                    "yaxis":"",
                    "text_s":"estudante",
                    "text_p":"estudantes",
                }
        if (self._language == "en"):
            legend = {"title":"Number of students that completed the assigns",
                        "xaxis":"Number of students",
                        "yaxis":"",
                        "text_s":"student",
                        "text_p":"students",
                    }
        df = self._assigns.sort_values(by=["Name"])
        
        trace = []
        trace.append(
            Bar(
                x=df.Total.values,
                y=df.Name.values,
                width=[0.04]*20,
                orientation = 'h',
                name="",
                text="",
                marker=dict(
                        color = 'lightgray',
                        # line=dict(
                        #     color = 'lightgray',
                        #     width=2
                        # )
                    )
            )
        )
        
        for i in range(0, max(df.Total.tolist())+1):
            text=str(i)+" "+legend['text_p'],
            if i==1:
                text=str(i)+" "+legend['text_s'],

            trace.append(
                Scatter(
                    x=[i]*len(df.Name.loc[df["Total"]==i]),
                    # x=[3]*20, #student
                    y=df.Name.loc[df["Total"]==i].values.tolist(),
                    mode='markers',
                    name = "",                    
                    text=text*len(df.Name.loc[df["Total"]==i]),                    
                    marker=dict(
                        symbol='circle',
                        sizemode='area',
                        # sizeref=sizeref,
                        # size=self.DATASET.iloc[:,i].values.tolist(),
                        # size=self.DATASET.iloc[i,1:].values.tolist(),
                        color = 'rgb(0,0,255)',
                        line=dict(
                            width=2
                        )
                    )
                )        
            )

        data = trace
        
        layout = Layout(
            title = legend["title"],
            showlegend=False,
            # showgrid=False,
            hovermode = "closest",
            xaxis=dict(
                title = legend["xaxis"],
                titlefont=dict(
                    # family='Arial, sans-serif',
                    # size=18,
                    color='rgb(180,180,180)',
                ),
                tick0=0,
                dtick=1,
                showgrid=True
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
                showgrid=False,
                # ticklen=4,
                # tickwidth=4,
                exponentformat='e',
                showexponent='all',
                gridcolor='#bdbdbd',
                # range=[0, 4.1]
            )
        )

        fig = Figure(data=data, layout=layout)
        iplot(fig, filename='Lollipop')

    def graph_13(self):
        legend = {"title":"Quantidade de estudantes que fizeram as tarefas",
                    "xaxis":"Número de estudantes",
                    "yaxis":"",
                    "text_s":"estudante",
                    "text_p":"estudantes",
                }
        if (self._language == "en"):
            legend = {"title":"Number of students that completed the assigns",
                        "xaxis":"Number of students",
                        "yaxis":"",
                        "text_s":"student",
                        "text_p":"students",
                    }
        df = self._assigns.sort_values(by=["Total","Name"])
        
        trace = []
        trace.append(
            Bar(
                x=df.Total.values,
                y=df.Name.values,
                width=[0.04]*20,
                orientation = 'h',
                name="",
                text="",
                marker=dict(
                        color = 'lightgray',
                        # line=dict(
                        #     color = 'lightgray',
                        #     width=2
                        # )
                    )
            )
        )
        
        for i in range(0, max(df.Total.tolist())+1):
            text=str(i)+" "+legend['text_p'],
            if i==1:
                text=str(i)+" "+legend['text_s'],

            trace.append(
                Scatter(
                    x=[i]*len(df.Name.loc[df["Total"]==i]),
                    # x=[3]*20, #student
                    y=df.Name.loc[df["Total"]==i].values.tolist(),
                    mode='markers',
                    name = "",                    
                    text=text*len(df.Name.loc[df["Total"]==i]),                    
                    marker=dict(
                        symbol='circle',
                        sizemode='area',
                        # sizeref=sizeref,
                        # size=self.DATASET.iloc[:,i].values.tolist(),
                        # size=self.DATASET.iloc[i,1:].values.tolist(),
                        color = 'rgb(0,0,255)',
                        line=dict(
                            width=2
                        )
                    )
                )        
            )

        data = trace
        
        layout = Layout(
            title = legend["title"],
            showlegend=False,
            # showgrid=False,
            hovermode = "closest",
            xaxis=dict(
                title = legend["xaxis"],
                titlefont=dict(
                    # family='Arial, sans-serif',
                    # size=18,
                    color='rgb(180,180,180)',
                ),
                tick0=0,
                dtick=1,
                showgrid=True
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
                showgrid=False,
                # ticklen=4,
                # tickwidth=4,
                exponentformat='e',
                showexponent='all',
                gridcolor='#bdbdbd',
                # range=[0, 4.1]
            )
        )

        fig = Figure(data=data, layout=layout)
        iplot(fig, filename='Lollipop')
    
    # Scatter assigns completed by each students
    def graph_14(self):
        # https://plot.ly/python/bubble-charts/
        # https://plot.ly/python/reference/#layout-xaxis
        # https://plot.ly/python/axes/#subcategory-axes
        legend = {"title":"Atividades feitas por estudante",
                    "xaxis":"",
                    "yaxis":"",
                }
        if (self._language == "en"):
            legend = {"title":"Assigns completed by students",
                        "xaxis":"",
                        "yaxis":"",
                    }
        df = self.DATASET.sort_values(by=["Students"])

        sizeref = 0.01
        # print (sizeref)

        trace = []
        # for i in range(1, len(df.columns)):
        for i in range(0, len(df)):                    
            trace.append(
                Scatter(
                    x=[df.iloc[i,0]]*len(df.columns), #student
                    y=df.columns[1:], #assigns
                    mode='markers',
                    # name=df.iloc[i,0], #each student name
                    name=df.iloc[i,0], #student name
                    # text = df.iloc[i,1:].values.tolist(),
                    marker=dict(
                        symbol='circle',
                        sizemode='area',
                        sizeref=sizeref,
                        # size=df.iloc[:,i].values.tolist(),
                        size=df.iloc[i,1:].values.tolist(),
                        color = 'rgb(0,0,255)',
                        line=dict(
                            width=2
                        )
                    )
                )
            )

        layout = Layout(
            title=legend['title'],
            # title='Number of access in the materials grouped by student',
            hovermode = "closest",
            showlegend = True,
            xaxis = dict(
                title = legend['xaxis'],
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
                title = legend['yaxis'],
                titlefont=dict(
                    # family='Arial, sans-serif',
                    # size=18,
                    color='rgb(180,180,180)',
                ),
                autorange = False,
                categoryorder = "category ascending",
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

    # Heatmap assigns completed by each students
    def graph_15(self):
        legend = {"title":"Atividades feitas por estudante",
                    "xaxis":"",
                    "yaxis":"",
                }
        if (self._language == "en"):
            legend = {"title":"Assigns completed by students",
                        "xaxis":"",
                        "yaxis":"",
                    }
        df = self.DATASET.sort_values(by=["Students"])
        z = []
        for i in range (1, len(df.columns)):
            z.append(df.iloc[:,i].values.tolist())

        trace = Heatmap(z=z,
                        y=df.columns[1:], #Assigns
                        x=df.iloc[:,0], #Students
                        colorscale=[[0, 'rgb(255,255,255)'], [1, 'rgb(0,0,255)']],
                        showscale = False
                    )
        
        layout = Layout(
                title = legend['title'],                
                autosize=False,
                width=950,
                height=350,
                hovermode = "closest",
                xaxis=dict(
                    title = legend['xaxis'],
                    titlefont=dict(
                    # family='Arial, sans-serif',
                    # size=18,
                    color='rgb(180,180,180)',
                ),
                ),                
                yaxis=dict(
                    title = legend['yaxis'],
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

    def print_all_graphs(self,language="pt"):
        self._language = language
        self.graph_01() #Table
        self.graph_02() #Barchart
        self.graph_03()
        self.graph_04()
        self.graph_05()
        self.graph_06() #Lollipop
        self.graph_07()
        self.graph_08() #Barchart
        self.graph_09()
        self.graph_10()
        self.graph_11()
        self.graph_12() #Lollipop
        self.graph_13()            
        self.graph_14() #Scatter
        self.graph_15() #Heatmap

instance = V001(20)
instance.print_all_graphs("pt")
# instance.print_all_graphs("en")