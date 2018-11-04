import pandas as pd
import numpy as np

from plotly.graph_objs import Figure, Layout, Bar, Table
from plotly.offline import init_notebook_mode, iplot

init_notebook_mode(connected=True) # initiate notebook for offline plot

class V001:
    NUMBER_STUDENTS = 21
    DATASET = pd.DataFrame()
    
    _students = pd.DataFrame()
    _assigns = pd.DataFrame()

    def __init__(self, number_students = 21):
        self.NUMBER_STUDENTS = number_students+1
        self.generate_dataset()

    def generate_dataset(self):
        self.DATASET = pd.DataFrame(columns=["Students","Assign1","Assign2",'Assign3','Assign4'])
        for i in range(1,self.NUMBER_STUDENTS):
            self.DATASET.loc[i] = [np.random.randint(0,2) for n in range(len(self.DATASET.columns))]
            self.DATASET.loc[i,"Students"] = "Student_"+str(i)

        self.get_students_frame()
        self.get_assigns_frame()
        
    def print_dataset(self):
        print(self.DATASET)

    def sum_assigns(self, row):
        return row["Assign1"]+row["Assign2"]+row["Assign3"]+row["Assign4"]    

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
    
    # Histogram number of assessments completed for each student
    def graph_02(self):
        trace = [Bar(
            x=self._students.Name.values,
            y=self._students.Total.values
        )]

        data = trace
        layout = Layout(
            title='Quantidade de tarefas feitas por alunos',
            yaxis=dict(
                # title='AXIS TITLE',
                titlefont=dict(
                    family='Arial, sans-serif',
                    # size=18,
                    color='lightgrey'
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

    # Histogram number of student that have completed each assessment
    def graph_03(self):
        trace011_2 = [Bar(
            x=self._assigns.Name.values,
            y=self._assigns.Total.values
        )]

        data011_2 = trace011_2
        layout011_2 = Layout(
            title='Quantidade de alunos que fizeram as tarefas',
            yaxis=dict(
                # title='Número de alunos',
                titlefont=dict(
                    family='Arial, sans-serif',
                    # size=18,
                    color='lightgrey'
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
        
    def graph_04(self):
        # df = self.DATASET
        # df.replace(value="", to_replace=0, inplace=True)
        # df.replace(value="x", to_replace=1, inplace=True)

        df = pd.DataFrame(columns=self.DATASET.Students.values)
        df.insert(loc=0,column="Assign",value=self.DATASET.columns[1:])
        
        for i in range(0, len(self.DATASET.values)):
            for j in range(0,len(self.DATASET.columns[1:])):
                df.iat[j,i+1] = self.DATASET.iat[i,j+1]
                # if self.DATASET.iat[i,j+1] == 1:
                    # df.iat[j,i+1] = "x"
                # else:
                    # df.iat[j,i+1] = ""

        # df.replace(value="", to_replace=0, inplace=True)
        # df.replace(value="x", to_replace=1, inplace=True)

        # print(df)

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
        


    def print_all_graphs(self):
        self.graph_01()
        self.graph_02()
        self.graph_03()
        self.graph_04()

instance = V001(20)
instance.print_all_graphs()