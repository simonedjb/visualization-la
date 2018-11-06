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