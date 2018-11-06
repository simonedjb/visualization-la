import pandas as pd
import numpy as np

from plotly.graph_objs import Figure, Layout, Bar, Table, Heatmap, Scatter
from plotly.offline import init_notebook_mode, iplot


init_notebook_mode(connected=True) # initiate notebook for offline plot

class V005:
    NUMBER_STUDENTS = 31
    DATASET = pd.DataFrame()

    _students = pd.DataFrame()
    _assigns = pd.DataFrame()

    def __init__(self, number_students = 21):
        self.NUMBER_STUDENTS = number_students+1
        self.generate_dataset()

    def generate_dataset(self):
        self.DATASET = pd.DataFrame(columns=["Students","Grade","Access", "Forum Post", "Forum Access"])
        for i in range(1,self.NUMBER_STUDENTS):
            self.DATASET.loc[i,"Students"] = "Student_"+str(i)
            self.DATASET.loc[i,"Grade"] = int(np.random.triangular(0,75,100))
            if (self.DATASET.loc[i,"Grade"] <= 50):
                self.DATASET.loc[i,"Access"] = int(np.random.triangular(0,10,30))
                self.DATASET.loc[i,"Forum Post"] = int(np.random.triangular(0,0,3))
                self.DATASET.loc[i,"Forum Access"] =  self.DATASET.loc[i,"Forum Post"] + int(np.random.triangular(0,5,10))

            elif (self.DATASET.loc[i,"Grade"] <= 60):
                self.DATASET.loc[i,"Access"] = int(np.random.triangular(0,30,50))
                self.DATASET.loc[i,"Forum Post"] = int(np.random.triangular(0,2,7))
                self.DATASET.loc[i,"Forum Access"] =  self.DATASET.loc[i,"Forum Post"] + int(np.random.triangular(0,10,30))

            elif (self.DATASET.loc[i,"Grade"] <= 70):
                    self.DATASET.loc[i,"Access"] = int(np.random.triangular(0,45,80))
                    self.DATASET.loc[i,"Forum Post"] = int(np.random.triangular(0,3,10))
                    self.DATASET.loc[i,"Forum Access"] =  self.DATASET.loc[i,"Forum Post"] + int(np.random.triangular(0,20,40))

            elif (self.DATASET.loc[i,"Grade"] <= 80):
                self.DATASET.loc[i,"Access"] = int(np.random.triangular(0,60,100))
                self.DATASET.loc[i,"Forum Post"] = int(np.random.triangular(0,5,20))
                self.DATASET.loc[i,"Forum Access"] =  self.DATASET.loc[i,"Forum Post"] + int(np.random.triangular(0,25,60))

            elif (self.DATASET.loc[i,"Grade"] <= 90):
                self.DATASET.loc[i,"Access"] = int(np.random.triangular(0,70,110))
                self.DATASET.loc[i,"Forum Post"] = int(np.random.triangular(0,7,35))
                self.DATASET.loc[i,"Forum Access"] =  self.DATASET.loc[i,"Forum Post"] + int(np.random.triangular(0,35,70))

            else:
                self.DATASET.loc[i,"Access"] = int(np.random.triangular(0,85,120))
                self.DATASET.loc[i,"Forum Post"] = int(np.random.triangular(0,10,40))
                self.DATASET.loc[i,"Forum Access"] = self.DATASET.loc[i,"Forum Post"] + int(np.random.triangular(0,45,80))

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


    def print_all_graphs(self):
        self.graph_01()

instance = V005(20)
instance.print_all_graphs()
