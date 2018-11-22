import pandas as pd
import numpy as np

from plotly.graph_objs import Figure, Layout, Bar, Table, Heatmap, Scatter, Box, Violin
from plotly.offline import init_notebook_mode, iplot

from sklearn import metrics
from sklearn.cluster import KMeans


init_notebook_mode(connected=True) # initiate notebook for offline plot

class V010:
    NUMBER_STUDENTS = 20
    NUMBER_VIDEOS = 10
    DATASET = pd.DataFrame()
    
    _language = "pt"
    _understood = 1
    _misunderstood = 0
    _video_name = []
    _video_dur = []
    _df_sum_feedback = pd.DataFrame()
    
    def __init__(self, number_students = 20, number_video = 10, language = "pt"):
        self.NUMBER_STUDENTS = number_students
        self.NUMBER_VIDEOS = number_video
        self._language = language
        self.generate_dataset()

    def generate_dataset(self):
        self._video_dur = [np.random.randint(240,600) for n in range(self.NUMBER_VIDEOS)] #video duration ranging between 240 and 600 seconds
        self._video_name = ["Video"+str(i+1) for i in range (0, self.NUMBER_VIDEOS)]
        
        names = pd.read_csv("names.csv")
        rand_names = [names.group_name[np.random.randint(0,len(names.group_name)+1)] for n in range(0,self.NUMBER_STUDENTS)]
        rand_names.sort()

        self.DATASET = pd.DataFrame(columns=self._video_name)
        self.DATASET.insert(0,"Students", rand_names)
        
        for i in range(1,len(self.DATASET.columns)):
            self.DATASET.iloc[:,i] = [self._understood]*self.NUMBER_STUDENTS #Adding 'well-understanding' to Video[i]
            number_doubts = np.random.randint(0,self.NUMBER_STUDENTS+1) #Get a random number of students with doubts in Video[i]
            index = np.random.randint(0,self.NUMBER_STUDENTS,number_doubts) #Get a random students index with doubts in Video[i]
            for j in range(0, number_doubts):
                self.DATASET.iloc[int(index[j]),i] = self._misunderstood #Adding doubt to Video[i] for student with index[j]

        self._df_sum_feedback = pd.DataFrame(columns=["Videos","Understood","Misunderstood","Total"])
        self._df_sum_feedback.Videos = self.DATASET.columns[1:].tolist()
        self._df_sum_feedback.Understood = self.sum_feedback(True) # Sum all understood feedback
        self._df_sum_feedback.Misunderstood = self.sum_feedback(False) # Sum all misunderstood feedback
        self._df_sum_feedback.Total = [len(self.DATASET)]*len(self.DATASET.columns[1:])

    def sum_feedback(self, understood=True):
        if understood == True:
            feedback = self._understood
        else:
            feedback = self._misunderstood

        lst = []
        for i in range(1,len(self.DATASET.columns)):
            key = self.DATASET.columns[i]
            lst.append(len(self.DATASET.loc[self.DATASET[key]==feedback]))
    
        return lst

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

    def graph_02(self):
        df = self._df_sum_feedback

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

    #Bar
    def graph_03(self):
        df = self._df_sum_feedback

        

    def print_all_graphs(self,language="pt"):
        self._language = language
        self.graph_01() # Table
        self.graph_02()
        self.graph_03() #Bar
        # self.graph_04() 
        # self.graph_05() 
        # self.graph_06()
        # self.graph_07() #Scatter
        # self.graph_08()
        
        #Lollipop
        #Heatmap

instance = V010(number_students=35, number_video=10)
instance.print_all_graphs("pt")
# instance.print_all_graphs("en")
