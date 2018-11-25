import pandas as pd
import numpy as np

from plotly.graph_objs import Figure, Layout, Bar, Table, Heatmap, Scatter
from plotly.offline import init_notebook_mode, iplot

init_notebook_mode(connected=True) # initiate notebook for offline plot

class V001:
    NUMBER_STUDENTS = 20
    NUMBER_ASSIGNS = 4
    DATASET = pd.DataFrame()
    
    _language = "pt"
    _assign_name = []
    _students = pd.DataFrame()
    _assigns = pd.DataFrame()

    def __init__(self, language="pt"):
        self.language = language

    def generate_dataset(self, number_students = 20, number_assigns = 4):
        self.NUMBER_STUDENTS = number_students
        self.NUMBER_ASSIGNS = number_assigns

        self._assign_name = ["Assign"+str(i+1) for i in range (0, self.NUMBER_ASSIGNS)]

        names = pd.read_csv("names.csv")
        rand_names = [names.group_name[np.random.randint(0,len(names.group_name)+1)] for n in range(0,self.NUMBER_STUDENTS)]
        rand_names.sort()

        self.DATASET = pd.DataFrame(columns=self._assign_name)
        for i in range(0,self.NUMBER_STUDENTS):
            self.DATASET.loc[i] = [np.random.randint(0,2) for n in range(len(self.DATASET.columns))]            
        
        self.DATASET.insert(0,"Students", rand_names)

        self.get_students_frame()
        self.get_assigns_frame()

    def sum_assigns_done(self,row):
        lst = self.DATASET.columns[1:].tolist()
        sum_value = 0
        for i in range(len(lst)):
            sum_value += row[lst[i]]

        return sum_value

    def sum_assigns_undone(self,row):
        lst = self.DATASET.columns[1:].tolist()
        sum_value = 0
        for i in range(len(lst)):
            sum_value += row[lst[i]]

        return len(lst)-sum_value

    def get_student(self, row):
        return row["Students"]

    def get_students_frame(self):
        self._students = pd.DataFrame(columns=["Name","Total_Done","Total_Undone"])
        self._students["Total_Done"] = self.DATASET.apply(self.sum_assigns_done, axis=1)
        self._students["Total_Undone"] = self.DATASET.apply(self.sum_assigns_undone, axis=1)
        self._students["Name"] = self.DATASET.apply(self.get_student, axis=1)
        # print (self._students)

    def get_assigns_frame(self):
        self._assigns = pd.DataFrame(columns=["Name","Total_Done","Total_Undone"])
        for i in range (0, len(self.DATASET.columns[1:])):
            self._assigns.loc[i,"Name"] = self.DATASET.columns[i+1]
            self._assigns.loc[i,"Total_Done"] = self.DATASET[self.DATASET.columns[i+1]].sum()
            self._assigns.loc[i,"Total_Undone"] = len(self.DATASET) - self._assigns.loc[i,"Total_Done"]
        
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
                values=[df[i].tolist() for i in df.columns],
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

        df = self._students.iloc[:,[0,1]]
        trace = [Bar(
            x=df.iloc[:,0].values,
            y=df.iloc[:,1].values
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
                    
        df = self._students.sort_values(by=["Total_Done","Name"]).iloc[:,[0,1]]        
        trace = [Bar(
            x=df.iloc[:,0].values,
            y=df.iloc[:,1].values
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
        df = self._students.iloc[:,[0,1]]
        trace = [Bar(
            x=df.iloc[:,1].values,
            y=df.iloc[:,0].values,
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
        df = self._students.sort_values(by=["Total_Done","Name"]).iloc[:,[0,1]]
        trace = [Bar(
            x=df.iloc[:,1].values,
            y=df.iloc[:,0].values,
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
    
    # Barchart number of assign not completed for each student
    def graph_06(self):
        legend = {"title":"Quantidade de tarefas <b>não</b> feitas por alunos",
                    "xaxis":"",
                    "yaxis":"Número de atividades",
                }
        if (self._language == "en"):
            legend = {"title":"Number of assigns <b>not</b> completed by students",
                        "xaxis":"",
                        "yaxis":"Number of assigns",
                    }

        df = self._students.iloc[:,[0,2]]
        trace = [Bar(
            x=df.iloc[:,0].values,
            y=df.iloc[:,1].values,
            marker=dict(
                color='rgb(255,126,24)',
            ),
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

    def graph_07(self):
        legend = {"title":"Quantidade de tarefas <b>não</b> feitas por alunos",
                    "xaxis":"",
                    "yaxis":"Número de atividades",
                    }
        if (self._language == "en"):
            legend = {"title":"Number of assigns <b>not</b> completed by students",
                    "xaxis":"",
                    "yaxis":"Number of assigns",
                    }
                    
        df = self._students.sort_values(by=["Total_Undone","Name"]).iloc[:,[0,2]]        
        trace = [Bar(
            x=df.iloc[:,0].values,
            y=df.iloc[:,1].values,
            marker=dict(
                color='rgb(255,126,24)',
            ),
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

    def graph_08(self):
        legend = {"title":"Quantidade de tarefas <b>não</b> feitas por alunos",
                    "xaxis":"Número de atividades",
                    "yaxis":"",
                    }
        if (self._language == "en"):
            legend = {"title":"Number of assigns <b>not</b> completed by students",
                    "xaxis":"Number of assigns",
                    "yaxis":"",
                    }
        df = self._students.iloc[:,[0,2]]
        trace = [Bar(
            x=df.iloc[:,1].values,
            y=df.iloc[:,0].values,
            orientation = 'h',
            marker=dict(
                color='rgb(255,126,24)',
            ),
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

    def graph_09(self):
        legend = {"title":"Quantidade de tarefas <b>não</b> feitas por alunos",
                    "xaxis":"Número de atividades",
                    "yaxis":"",
                }
        if (self._language == "en"):
            legend = {"title":"Number of assigns <b>not</b> completed by students",
                        "xaxis":"Number of assigns",
                        "yaxis":"",
                    }
        df = self._students.sort_values(by=["Total_Undone","Name"]).iloc[:,[0,2]]
        trace = [Bar(
            x=df.iloc[:,1].values,
            y=df.iloc[:,0].values,
            orientation = 'h',
            marker=dict(
                color='rgb(255,126,24)',
            ),
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
    def graph_10(self):
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
        df = self._students.iloc[:,[0,1]]
        trace = []
        trace.append(
            Bar(
                x=df.iloc[:,1].values,
                y=df.iloc[:,0].values,
                width=[0.07]*20,
                orientation = 'h',
                name="",
                text="",
                marker=dict(
                        color = 'lightgray',                        
                    )
            )
        )
        
        for i in range(1, len(self.DATASET.columns)):
            text=str(i)+" "+legend['text_p'],
            if i==1:
                text=str(i)+" "+legend['text_s'],

            trace.append(
                Scatter(
                    x=[i]*len(df.Name.loc[df["Total_Done"]==i]),
                    # x=[3]*20, #student
                    y=df.Name.loc[df["Total_Done"]==i].values.tolist(),
                    mode='markers',
                    name = "",                    
                    text=text*len(df.Name.loc[df["Total_Done"]==i]),                    
                    marker=dict(
                        symbol='circle',
                        sizemode='area',
                        color = 'rgb(0,0,255)',
                        line=dict(
                            width=0
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

    def graph_11(self):
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
        df = self._students.sort_values(by=["Total_Done","Name"]).iloc[:,[0,1]]
        trace = []
        trace.append(
            Bar(
                x=df.iloc[:,1].values,
                y=df.iloc[:,0].values,
                width=[0.07]*20,
                orientation = 'h',
                name="",
                text="",
                marker=dict(
                        color = 'lightgray',                        
                    )
            )
        )
        
        for i in range(1, len(self.DATASET.columns)):
            text=str(i)+" "+legend['text_p'],
            if i==1:
                text=str(i)+" "+legend['text_s'],

            trace.append(
                Scatter(
                    x=[i]*len(df.Name.loc[df["Total_Done"]==i]),
                    # x=[3]*20, #student
                    y=df.Name.loc[df["Total_Done"]==i].values.tolist(),
                    mode='markers',
                    name = "",                    
                    text=text*len(df.Name.loc[df["Total_Done"]==i]),                    
                    marker=dict(
                        symbol='circle',
                        sizemode='area',
                        color = 'rgb(0,0,255)',
                        line=dict(
                            width=0
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

    def graph_12(self):
        legend = {"title":"Quantidade de tarefas <b>não</b> feitas por alunos",
                    "xaxis":"Número de atividades",
                    "yaxis":"",
                    "text_s":"atividades",
                    "text_p":"atividades",
                }
        if (self._language == "en"):
            legend = {"title":"Number of assigns <b>not</b> completed by students",
                        "xaxis":"Number of assigns",
                        "yaxis":"",
                        "text_s":"assign",
                        "text_p":"assigns",
                    }
        df = self._students.iloc[:,[0,2]]
        trace = []
        trace.append(
            Bar(
                x=df.iloc[:,1].values,
                y=df.iloc[:,0].values,
                width=[0.07]*20,
                orientation = 'h',
                name="",
                text="",
                marker=dict(
                        color = 'lightgray',                        
                    )
            )
        )
        
        for i in range(1, len(self.DATASET.columns)):
            text=str(i)+" "+legend['text_p'],
            if i==1:
                text=str(i)+" "+legend['text_s'],

            trace.append(
                Scatter(
                    x=[i]*len(df.Name.loc[df["Total_Undone"]==i]),
                    # x=[3]*20, #student
                    y=df.Name.loc[df["Total_Undone"]==i].values.tolist(),
                    mode='markers',
                    name = "",                    
                    text=text*len(df.Name.loc[df["Total_Undone"]==i]),                    
                    marker=dict(
                        symbol='circle',
                        sizemode='area',
                        color = 'rgb(255,126,24)',
                        line=dict(
                            width=0
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
        legend = {"title":"Quantidade de tarefas <b>não</b> feitas por alunos",
                    "xaxis":"Número de atividades",
                    "yaxis":"",
                    "text_s":"atividades",
                    "text_p":"atividades",
                }
        if (self._language == "en"):
            legend = {"title":"Number of assigns <b>not</b> completed by students",
                        "xaxis":"Number of assigns",
                        "yaxis":"",
                        "text_s":"assign",
                        "text_p":"assigns",
                    }
        df = self._students.sort_values(by=["Total_Undone","Name"]).iloc[:,[0,2]]
        trace = []
        trace.append(
            Bar(
                x=df.iloc[:,1].values,
                y=df.iloc[:,0].values,
                width=[0.07]*20,
                orientation = 'h',
                name="",
                text="",
                marker=dict(
                        color = 'lightgray',                        
                    )
            )
        )
        
        for i in range(1, len(self.DATASET.columns)):
            text=str(i)+" "+legend['text_p'],
            if i==1:
                text=str(i)+" "+legend['text_s'],

            trace.append(
                Scatter(
                    x=[i]*len(df.Name.loc[df["Total_Undone"]==i]),
                    # x=[3]*20, #student
                    y=df.Name.loc[df["Total_Undone"]==i].values.tolist(),
                    mode='markers',
                    name = "",                    
                    text=text*len(df.Name.loc[df["Total_Undone"]==i]),                    
                    marker=dict(
                        symbol='circle',
                        sizemode='area',
                        color = 'rgb(255,126,24)',
                        line=dict(
                            width=0
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
    def graph_14(self):
        legend = {"title":"Quantidade de estudantes que fizeram as tarefas",
                    "xaxis":"",
                    "yaxis":"Número de estudantes",
                }
        if (self._language == "en"):
            legend = {"title":"Number of students that completed the assigns",
                        "xaxis":"",
                        "yaxis":"Number of students",
                    }
        df = self._assigns.iloc[:,[0,1]]
        trace = [Bar(
            x=df.iloc[:,0].values,
            y=df.iloc[:,1].values
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
                # range=[0, 13]
            )
        )

        fig = Figure(data=data, layout=layout)
        iplot(fig, filename='Bar')
    
    def graph_15(self):
        legend = {"title":"Quantidade de alunos que fizeram as tarefas",
                    "xaxis":"",
                    "yaxis":"Número de estudantes",
                }
        if (self._language == "en"):
            legend = {"title":"Number of students that completed the assigns",
                        "xaxis":"",
                        "yaxis":"Number of students",
                    }
        df = self._assigns.sort_values(by=["Total_Done","Name"]).iloc[:,[0,1]]
        trace = [Bar(
            x=df.iloc[:,0].values,
            y=df.iloc[:,1].values
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
                # range=[0, 13]
            )
        )

        fig = Figure(data=data, layout=layout)
        iplot(fig, filename='Bar')
  
    def graph_16(self):
        legend = {"title":"Quantidade de estudantes que fizeram as tarefas",
                    "xaxis":"Número de estudantes",
                    "yaxis":"",
                }
        if (self._language == "en"):
            legend = {"title":"Number of students that completed the assigns",
                        "xaxis":"Number of students",
                        "yaxis":"",
                    }
        df = self._assigns.iloc[:,[0,1]]
        trace = [Bar(
            x=df.iloc[:,1].values,
            y=df.iloc[:,0].values,
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

    def graph_17(self):
        legend = {"title":"Quantidade de estudantes que fizeram as tarefas",
                    "xaxis":"Número de estudantes",
                    "yaxis":"",
                }
        if (self._language == "en"):
            legend = {"title":"Number of students that completed the assigns",
                        "xaxis":"Number of students",
                        "yaxis":"",
                    }
        df = self._assigns.sort_values(by=["Total_Done","Name"]).iloc[:,[0,1]]
        trace = [Bar(
            x=df.iloc[:,1].values,
            y=df.iloc[:,0].values,
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

    def graph_18(self):
        legend = {"title":"Quantidade de estudantes <b>não</b> que fizeram as tarefas",
                    "xaxis":"",
                    "yaxis":"Número de estudantes",
                }
        if (self._language == "en"):
            legend = {"title":"Number of students who <b>not</b> completed the assigns",
                        "xaxis":"",
                        "yaxis":"Number of students",
                    }
        df = self._assigns.iloc[:,[0,2]]
        trace = [Bar(
            x=df.iloc[:,0].values,
            y=df.iloc[:,1].values,
            marker=dict(
                color='rgb(255,126,24)',
            ),
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
                # range=[0, 13]
            )
        )

        fig = Figure(data=data, layout=layout)
        iplot(fig, filename='Bar')
    
    def graph_19(self):
        legend = {"title":"Quantidade de alunos que <b>não</b> fizeram as tarefas",
                    "xaxis":"",
                    "yaxis":"Número de estudantes",
                }
        if (self._language == "en"):
            legend = {"title":"Number of students who <b>não</b> completed the assigns",
                        "xaxis":"",
                        "yaxis":"Number of students",
                    }
        df = self._assigns.sort_values(by=["Total_Undone","Name"]).iloc[:,[0,2]]
        trace = [Bar(
            x=df.iloc[:,0].values,
            y=df.iloc[:,1].values,
            marker=dict(
                color='rgb(255,126,24)',
            ),
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
                # range=[0, 13]
            )
        )

        fig = Figure(data=data, layout=layout)
        iplot(fig, filename='Bar')
  
    def graph_20(self):
        legend = {"title":"Quantidade de estudantes que <b>não</b> fizeram as tarefas",
                    "xaxis":"Número de estudantes",
                    "yaxis":"",
                }
        if (self._language == "en"):
            legend = {"title":"Number of students who <b>not</b> completed the assigns",
                        "xaxis":"Number of students",
                        "yaxis":"",
                    }
        df = self._assigns.iloc[:,[0,2]]
        trace = [Bar(
            x=df.iloc[:,1].values,
            y=df.iloc[:,0].values,
            orientation = 'h',
            marker=dict(
                color='rgb(255,126,24)',
            ),
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

    def graph_21(self):
        legend = {"title":"Quantidade de estudantes que <b>não</b> fizeram as tarefas",
                    "xaxis":"Número de estudantes",
                    "yaxis":"",
                }
        if (self._language == "en"):
            legend = {"title":"Number of students who <b>not</b> completed the assigns",
                        "xaxis":"Number of students",
                        "yaxis":"",
                    }
        df = self._assigns.sort_values(by=["Total_Undone","Name"]).iloc[:,[0,2]]
        trace = [Bar(
            x=df.iloc[:,1].values,
            y=df.iloc[:,0].values,
            orientation = 'h',
            marker=dict(
                color='rgb(255,126,24)',
            ),
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
    def graph_22(self):
        legend = {"title":"Quantidade de estudantes que fizeram as tarefas",
                    "xaxis":"Número de estudantes",
                    "yaxis":"",
                    "text_s":"estudante",
                    "text_p":"estudantes",
                }
        if (self._language == "en"):
            legend = {"title":"Number of students who completed the assigns",
                        "xaxis":"Number of students",
                        "yaxis":"",
                        "text_s":"student",
                        "text_p":"students",
                    }
        df = self._assigns.iloc[:,[0,1]]
        
        trace = []
        trace.append(
            Bar(
                x=df.iloc[:,1].values,
                y=df.iloc[:,0].values,
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
        
        for i in range(0, max(df.Total_Done.tolist())+1):
            text=str(i)+" "+legend['text_p'],
            if i==1:
                text=str(i)+" "+legend['text_s'],

            trace.append(
                Scatter(
                    x=[i]*len(df.Name.loc[df["Total_Done"]==i]),
                    y=df.Name.loc[df["Total_Done"]==i].values.tolist(),
                    mode='markers',
                    name = "",                    
                    text=text*len(df.Name.loc[df["Total_Done"]==i]),                    
                    marker=dict(
                        symbol='circle',
                        sizemode='area',
                        color = 'rgb(0,0,255)',
                        line=dict(
                            width=0
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

    def graph_23(self):
        legend = {"title":"Quantidade de estudantes que fizeram as tarefas",
                    "xaxis":"Número de estudantes",
                    "yaxis":"",
                    "text_s":"estudante",
                    "text_p":"estudantes",
                }
        if (self._language == "en"):
            legend = {"title":"Number of students who completed the assigns",
                        "xaxis":"Number of students",
                        "yaxis":"",
                        "text_s":"student",
                        "text_p":"students",
                    }
        df = self._assigns.sort_values(by=["Total_Done","Name"]).iloc[:,[0,1]]

        trace = []
        trace.append(
            Bar(
                x=df.iloc[:,1].values,
                y=df.iloc[:,0].values,
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
        
        for i in range(0, max(df.Total_Done.tolist())+1):
            text=str(i)+" "+legend['text_p'],
            if i==1:
                text=str(i)+" "+legend['text_s'],

            trace.append(
                Scatter(
                    x=[i]*len(df.Name.loc[df["Total_Done"]==i]),
                    y=df.Name.loc[df["Total_Done"]==i].values.tolist(),
                    mode='markers',
                    name = "",                    
                    text=text*len(df.Name.loc[df["Total_Done"]==i]),                    
                    marker=dict(
                        symbol='circle',
                        sizemode='area',
                        color = 'rgb(0,0,255)',
                        line=dict(
                            width=0
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
    
    def graph_24(self):
        legend = {"title":"Quantidade de estudantes que <b>não</b> fizeram as tarefas",
                    "xaxis":"Número de estudantes",
                    "yaxis":"",
                    "text_s":"estudante",
                    "text_p":"estudantes",
                }
        if (self._language == "en"):
            legend = {"title":"Number of students who <b>not</b> completed the assigns",
                        "xaxis":"Number of students",
                        "yaxis":"",
                        "text_s":"student",
                        "text_p":"students",
                    }
        df = self._assigns.iloc[:,[0,2]]
        
        trace = []
        trace.append(
            Bar(
                x=df.iloc[:,1].values,
                y=df.iloc[:,0].values,
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
        
        for i in range(0, max(df.Total_Undone.tolist())+1):
            text=str(i)+" "+legend['text_p'],
            if i==1:
                text=str(i)+" "+legend['text_s'],

            trace.append(
                Scatter(
                    x=[i]*len(df.Name.loc[df["Total_Undone"]==i]),
                    y=df.Name.loc[df["Total_Undone"]==i].values.tolist(),
                    mode='markers',
                    name = "",                    
                    text=text*len(df.Name.loc[df["Total_Undone"]==i]),                    
                    marker=dict(
                        symbol='circle',
                        sizemode='area',
                        color = 'rgb(255,126,24)',
                        line=dict(
                            width=0
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

    def graph_25(self):
        legend = {"title":"Quantidade de estudantes <b>não</b> que fizeram as tarefas",
                    "xaxis":"Número de estudantes",
                    "yaxis":"",
                    "text_s":"estudante",
                    "text_p":"estudantes",
                }
        if (self._language == "en"):
            legend = {"title":"Number of students who <b>not</b> completed the assigns",
                        "xaxis":"Number of students",
                        "yaxis":"",
                        "text_s":"student",
                        "text_p":"students",
                    }
        df = self._assigns.sort_values(by=["Total_Undone","Name"]).iloc[:,[0,2]]

        trace = []
        trace.append(
            Bar(
                x=df.iloc[:,1].values,
                y=df.iloc[:,0].values,
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
        
        for i in range(0, max(df.Total_Undone.tolist())+1):
            text=str(i)+" "+legend['text_p'],
            if i==1:
                text=str(i)+" "+legend['text_s'],

            trace.append(
                Scatter(
                    x=[i]*len(df.Name.loc[df["Total_Undone"]==i]),
                    y=df.Name.loc[df["Total_Undone"]==i].values.tolist(),
                    mode='markers',
                    name = "",                    
                    text=text*len(df.Name.loc[df["Total_Undone"]==i]),                    
                    marker=dict(
                        symbol='circle',
                        sizemode='area',
                        color = 'rgb(255,126,24)',
                        line=dict(
                            width=0
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
    def graph_26(self):
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
        df = self.DATASET

        sizeref = 0.01
        # print (sizeref)

        trace = []
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
                            width=0
                        )
                    )
                )
            )

        layout = Layout(
            title=legend['title'],
            # title='Number of access in the materials grouped by student',
            hovermode = "closest",
            showlegend = False,
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
                # categoryorder = "category ascending",
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

    def graph_27(self):
        # https://plot.ly/python/bubble-charts/
        # https://plot.ly/python/reference/#layout-xaxis
        # https://plot.ly/python/axes/#subcategory-axes
        legend = {"title":"Atividades <b>não</b> feitas por estudante",
                    "xaxis":"",
                    "yaxis":"",
                }
        if (self._language == "en"):
            legend = {"title":"Assigns <b>not</b> completed by students",
                        "xaxis":"",
                        "yaxis":"",
                    }
        df = self.DATASET

        sizeref = 0.01
        # print (sizeref)

        trace = []
        for i in range(0, len(df)):
            x = df.iloc[i,1:].values.tolist()
            y = [-1]*len(df.columns[1:])
            z = [i + j for i, j in zip(x, y)]
            values = [i*(-1) for i in z]
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
                        size=values,
                        color = 'rgb(255,126,24)',
                        line=dict(
                            width=0
                        )
                    )
                )
            )

        layout = Layout(
            title=legend['title'],
            # title='Number of access in the materials grouped by student',
            hovermode = "closest",
            showlegend = False,
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
                # categoryorder = "category ascending",
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

    def graph_28(self):
        # https://plot.ly/python/bubble-charts/
        # https://plot.ly/python/reference/#layout-xaxis
        # https://plot.ly/python/axes/#subcategory-axes
        legend = {"title":"Atividades feitas e <b>não</b> feitas por estudante",
                    "xaxis":"",
                    "yaxis":"",
                }
        if (self._language == "en"):
            legend = {"title":"Assigns completed and <b>not</b> completed by students",
                        "xaxis":"",
                        "yaxis":"",
                    }
        df = self.DATASET

        sizeref = 0.01
        # print (sizeref)

        trace = []
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
                            width=0
                        )
                    )
                )
            )

        for i in range(0, len(df)):
            x = df.iloc[i,1:].values.tolist()
            y = [-1]*len(df.columns[1:])
            z = [i + j for i, j in zip(x, y)]
            values = [i*(-1) for i in z]
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
                        size=values,
                        color = 'rgb(255,126,24)',
                        line=dict(
                            width=0
                        )
                    )
                )
            )

        layout = Layout(
            title=legend['title'],
            # title='Number of access in the materials grouped by student',
            hovermode = "closest",
            showlegend = False,
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
                # categoryorder = "category ascending",
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

    def graph_29(self):
        # https://plot.ly/python/bubble-charts/
        # https://plot.ly/python/reference/#layout-xaxis
        # https://plot.ly/python/axes/#subcategory-axes
        legend = {"title":"Número de atividades feitas e <b>não</b> feitas por estudante",
                    "xaxis":"",
                    "yaxis":"",
                    "columns":{1:"Feitas", 2:"Não<br>feitas"}
                }
        if (self._language == "en"):
            legend = {"title":"Number of assigns completed and <b>not</b> completed student",
                        "xaxis":"",
                        "yaxis":"",
                        "columns":{1:"Completed", 2:"Not completed"}
                    }
        df = self._students.iloc[:,0:3]
        sizeref = 0.05
        
        trace = []
        for i in range(0, len(df)):                    
            trace.append(
                Scatter(
                    x=[df.iloc[i,0]]*len(df.columns),
                    y=[legend["columns"][i] for i in range (1,2)],
                    mode='markers',                    
                    name=df.iloc[i,0], #videos
                    text = df.iloc[i,1:].values.tolist(),
                    marker=dict(
                        symbol='circle',
                        sizemode='area',
                        sizeref=sizeref,
                        size=df.iloc[i,1:].values.tolist(),
                        color = 'rgb(0,0,255)',
                        line=dict(
                            width=2
                        )
                    )
                )
            )
            trace.append(
                Scatter(
                    x=[df.iloc[i,0]]*len(df.columns),
                    y=[legend["columns"][i] for i in range (2,3)],
                    mode='markers',                    
                    name=df.iloc[i,0],
                    text = df.iloc[i,2:].values.tolist(),
                    marker=dict(
                        symbol='circle',
                        sizemode='area',
                        sizeref=sizeref,
                        size=df.iloc[i,2:].values.tolist(),
                        color='rgb(255,126,24)',
                        line=dict(
                            width=2
                        )
                    )
                )
            )

        layout = Layout(
            title=legend['title'],
            hovermode = "closest",
            showlegend = False,
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
                # categoryorder = "category ascending",
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

    def graph_30(self):
        # https://plot.ly/python/bubble-charts/
        # https://plot.ly/python/reference/#layout-xaxis
        # https://plot.ly/python/axes/#subcategory-axes
        legend = {"title":"Número de estudantes que fizeram e <b>não</b> fizeram as atividades",
                    "xaxis":"",
                    "yaxis":"",
                    "columns":{1:"Feitas", 2:"Não<br>feitas"}
                }
        if (self._language == "en"):
            legend = {"title":"Number of students who completed and <b>not</b> completed the assigns",
                        "xaxis":"",
                        "yaxis":"",
                        "columns":{1:"Completed", 2:"Not completed"}
                    }
        df = self._assigns.iloc[:,0:3]
        sizeref = 0.05
        
        trace = []
        for i in range(0, len(df)):                    
            trace.append(
                Scatter(
                    x=[df.iloc[i,0]]*len(df.columns),
                    y=[legend["columns"][i] for i in range (1,2)],
                    mode='markers',                    
                    name=df.iloc[i,0], #videos
                    text = df.iloc[i,1:].values.tolist(),
                    marker=dict(
                        symbol='circle',
                        sizemode='area',
                        sizeref=sizeref,
                        size=df.iloc[i,1:].values.tolist(),
                        color = 'rgb(0,0,255)',
                        line=dict(
                            width=2
                        )
                    )
                )
            )
            trace.append(
                Scatter(
                    x=[df.iloc[i,0]]*len(df.columns),
                    y=[legend["columns"][i] for i in range (2,3)],
                    mode='markers',                    
                    name=df.iloc[i,0],
                    text = df.iloc[i,2:].values.tolist(),
                    marker=dict(
                        symbol='circle',
                        sizemode='area',
                        sizeref=sizeref,
                        size=df.iloc[i,2:].values.tolist(),
                        color='rgb(255,126,24)',
                        line=dict(
                            width=2
                        )
                    )
                )
            )

        layout = Layout(
            title=legend['title'],
            hovermode = "closest",
            showlegend = False,
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
                # categoryorder = "category ascending",
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
    def graph_31(self):
        legend = {"title":"Atividades feitas por estudante",
                    "xaxis":"",
                    "yaxis":"",
                }
        if (self._language == "en"):
            legend = {"title":"Assigns completed by students",
                        "xaxis":"",
                        "yaxis":"",
                    }
        df = self.DATASET
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

    def graph_32(self):
        legend = {"title":"Atividades <b>não</b> feitas por estudante",
                    "xaxis":"",
                    "yaxis":"",
                }
        if (self._language == "en"):
            legend = {"title":"Assigns <b>not</b> completed by students",
                        "xaxis":"",
                        "yaxis":"",
                    }
        df = self.DATASET
        z = []
        for i in range (1, len(df.columns)):
            x = df.iloc[:,i].values.tolist()
            y = [-1]*len(x)
            f = [a + b for a, b in zip(x, y)]
            values = [a*(-1) for a in f]
            z.append(values)
        # for i in range (1, len(df.columns)):
        #     z.append(df.iloc[:,i].values.tolist())

        trace = Heatmap(z=z,
                        y=df.columns[1:], #Assigns
                        x=df.iloc[:,0], #Students
                        colorscale=[[0, 'rgb(255,255,255)'], [1, 'rgb(255,126,24)']],
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

    def graph_33(self):
        legend = {"title":"Atividades feitas e <b>não</b> feitas por estudante",
                    "xaxis":"",
                    "yaxis":"",
                }
        if (self._language == "en"):
            legend = {"title":"Assigns completed and <b>not</b> completed by students",
                        "xaxis":"",
                        "yaxis":"",
                    }
        df = self.DATASET
        z = []
        for i in range (1, len(df.columns)):
            z.append(df.iloc[:,i].values.tolist())

        trace = Heatmap(z=z,
                        y=df.columns[1:], #Assigns
                        x=df.iloc[:,0], #Students
                        colorscale=[[0, 'rgb(255,126,24)'], [1, 'rgb(0,0,255)']],
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

    def graph_34(self):
        legend = {"title":"Número de atividades feitas e <b>não</b> feitas por estudante",
                    "xaxis":"",
                    "yaxis":"",
                    "columns":{1:"Feitas", 2:"Não<br>feitas"}
                }
        if (self._language == "en"):
            legend = {"title":"Number of assigns completed and <b>not</b> completed student",
                        "xaxis":"",
                        "yaxis":"",
                        "columns":{1:"Completed", 2:"Not completed"}
                    }
        df = self._students.iloc[:,0:3]
        z = []
        for i in range (1, len(df.columns)):
            z.append(df.iloc[:,i].values.tolist())
        
        trace = []
        trace.append(Heatmap(z=z,
                        y=[legend["columns"][i] for i in range (1,len(df.columns))],
                        x=df.iloc[:,0], #Students
                        colorscale=[[0, 'rgb(255,255,255)'], [1, 'rgb(0,0,255)']],
                        showscale = True
                    ))

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

        data = trace
        fig = Figure(data=data, layout=layout)
        iplot(fig, filename='Heatmap')

    def graph_35(self):
        legend = {"title":"Número de atividades feitas e <b>não</b> feitas por estudante",
                    "xaxis":"",
                    "yaxis":"",
                    "columns":{1:"Feitas", 2:"Não<br>feitas"}
                }
        if (self._language == "en"):
            legend = {"title":"Number of assigns completed and <b>not</b> completed student",
                        "xaxis":"",
                        "yaxis":"",
                        "columns":{1:"Completed", 2:"Not completed"}
                    }
        df = self._students.iloc[:,0:3]
        z = []
        max_value = 0
        for i in range (1, len(df.columns)):
            z.append(df.iloc[:,i].values.tolist())
            max_local = max(df.iloc[:,i].values.tolist())
            max_value = max(max_local,max_value)
        
        trace = []
        trace.append(Heatmap(z=z,
                        y=[legend["columns"][i] for i in range (1,len(df.columns))],
                        x=df.iloc[:,0], #Students
                        colorscale=[[0, 'rgb(255,255,255)'], [1, 'rgb(0,0,255)']],
                        showscale = True
                    ))

        annotations=[]
        for i in range(1,len(df.columns)):
            for j in range(0,len(df)):
                color = 'rgb(0,0,0)'
                if df.iloc[j,i] > max_value/2:
                    color = 'rgb(255,255,255)'
                annotations.append({
                    "text":str(df.iloc[j,i]),
                    "y":legend["columns"][i],
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
                ),
                annotations = annotations
            )

        data = trace
        fig = Figure(data=data, layout=layout)
        iplot(fig, filename='Heatmap')

    def graph_36(self):
        legend = {"title":"Número de estudantes que fizeram e <b>não</b> fizeram as atividades",
                    "xaxis":"",
                    "yaxis":"",
                    "columns":{1:"Feitas", 2:"Não<br>feitas"}
                }
        if (self._language == "en"):
            legend = {"title":"Number of students who completed and <b>not</b> completed the assigns",
                        "xaxis":"",
                        "yaxis":"",
                        "columns":{1:"Completed", 2:"Not completed"}
                    }
        df = self._assigns.iloc[:,0:3]
        z = []
        for i in range (1, len(df.columns)):
            z.append(df.iloc[:,i].values.tolist())
        
        trace = []
        trace.append(Heatmap(z=z,
                        y=[legend["columns"][i] for i in range (1,len(df.columns))],
                        x=df.iloc[:,0], #Students
                        colorscale=[[0, 'rgb(255,255,255)'], [1, 'rgb(0,0,255)']],
                        showscale = True
                    ))

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

        data = trace
        fig = Figure(data=data, layout=layout)
        iplot(fig, filename='Heatmap')

    def graph_37(self):
        legend = {"title":"Número de estudantes que fizeram e <b>não</b> fizeram as atividades",
                    "xaxis":"",
                    "yaxis":"",
                    "columns":{1:"Feitas", 2:"Não<br>feitas"}
                }
        if (self._language == "en"):
            legend = {"title":"Number of students who completed and <b>not</b> completed the assigns",
                        "xaxis":"",
                        "yaxis":"",
                        "columns":{1:"Completed", 2:"Not completed"}
                    }
        df = self._assigns.iloc[:,0:3]
        z = []
        max_value = 0
        for i in range (1, len(df.columns)):
            z.append(df.iloc[:,i].values.tolist())
            max_local = max(df.iloc[:,i].values.tolist())
            max_value = max(max_local,max_value)
        
        trace = []
        trace.append(Heatmap(z=z,
                        y=[legend["columns"][i] for i in range (1,len(df.columns))],
                        x=df.iloc[:,0], #Students
                        colorscale=[[0, 'rgb(255,255,255)'], [1, 'rgb(0,0,255)']],
                        showscale = True
                    ))

        annotations=[]
        for i in range(1,len(df.columns)):
            for j in range(0,len(df)):
                color = 'rgb(0,0,0)'
                if df.iloc[j,i] > max_value/2:
                    color = 'rgb(255,255,255)'
                annotations.append({
                    "text":str(df.iloc[j,i]),
                    "y":legend["columns"][i],
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
                ),
                annotations = annotations
            )

        data = trace
        fig = Figure(data=data, layout=layout)
        iplot(fig, filename='Heatmap')

    def print_all_graphs(self,language="pt"):
        self._language = language
        self.graph_01() #Table
        self.graph_02() #Barchart
        self.graph_03()
        self.graph_04()
        self.graph_05()
        self.graph_06()
        self.graph_07()
        self.graph_08()
        self.graph_09()
        self.graph_10() #Lollipop
        self.graph_11()
        self.graph_12()
        self.graph_13()
        self.graph_14() #Barchart
        self.graph_15()
        self.graph_16()
        self.graph_17()
        self.graph_18()
        self.graph_19() 
        self.graph_20()
        self.graph_21()
        self.graph_22() #Lollipop
        self.graph_23()
        self.graph_24() 
        self.graph_25() 
        self.graph_26() #Scatter
        self.graph_27()
        self.graph_28()
        self.graph_29()
        self.graph_30()
        self.graph_31() #Heatmap
        self.graph_32()
        self.graph_33()
        self.graph_34()
        self.graph_35()
        self.graph_36()
        self.graph_37()

instance = V001()
instance.generate_dataset(number_students = 20, number_assigns = 10)
instance.print_all_graphs("pt")
# instance.print_all_graphs("en")