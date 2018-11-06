import pandas as pd
import numpy as np

from plotly.graph_objs import Figure, Layout, Bar, Table, Heatmap, Scatter
from plotly.offline import init_notebook_mode, iplot

init_notebook_mode(connected=True) # initiate notebook for offline plot

class V004:
    NUMBER_STUDENTS = 21
    DATASET = pd.DataFrame()

    def __init__(self, number_students = 21):
        self.NUMBER_STUDENTS = number_students+1
        self.generate_dataset()

    def generate_dataset(self):
        self.DATASET = pd.DataFrame(columns=['Students','Video1','Video2','Video3','Video4','Video5'])
        list_aux = []
        for i in range(1,self.NUMBER_STUDENTS):
            for j  in range(0,len(self.DATASET.columns)):
                list_aux.append(                        
                        [np.random.randint(5,360) for n in range(np.random.randint(0,5))]
                    )                                                                       
            self.DATASET.loc[i] = list_aux            
            self.DATASET.loc[i,"Students"] = "Student_"+str(i)
            list_aux.clear()
        
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
                values=[df[i].tolist() for i in df.columns[:]],                
                fill = dict(color='#F5F8FF'),
                align = ['left','center']
            )
        )

        data = [trace] 
        iplot(data, filename = 'pandas_table')

    def print_all_graphs(self):
        self.graph_01()
    #     # self.graph_02()
    #     # self.graph_03()
    #     # self.graph_04()

instance = V004(20)
instance.print_all_graphs()        