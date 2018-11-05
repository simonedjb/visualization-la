import pandas as pd
import numpy as np

from plotly.graph_objs import Figure, Layout, Bar, Table
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
    # Histogram number of assessments completed for each student
    def graph_02(self):
        trace = [Bar(
             x=self._students.Name.values,
             y=self._students.Interactions.values
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


    def print_all_graphs(self):
        self.graph_01()
        self.graph_02()

instance = V003(20)
instance.print_all_graphs()
