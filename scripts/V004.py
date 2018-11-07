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
        video_dur = []
        video_dur = [np.random.randint(240,600) for n in range(7)] #video duration ranging between 240 and 600 seconds
        
        self.DATASET = pd.DataFrame(columns=['Students','Video1 ('+str(video_dur[0])+'s)',
                        'Video2 ('+str(video_dur[1])+'s)','Video3 ('+str(video_dur[2])+'s)',
                        'Video4 ('+str(video_dur[3])+'s)','Video5 ('+str(video_dur[4])+'s)','Total'])
        
        list_aux = []
        for i in range(1,self.NUMBER_STUDENTS):
            for j  in range(0,len(self.DATASET.columns)):
                list_aux.append(                        
                        [np.random.randint(5,video_dur[j]) for n in range(np.random.randint(0,5))] #user access ranging between  
                    )                                                                       
            self.DATASET.loc[i] = list_aux            
            self.DATASET.loc[i,"Students"] = "Student_"+str(i)
            list_aux.clear()

        self.DATASET["Total"] = self.DATASET.apply(self.sum_times, axis=1)

    def sum_times(self,row):
        lst = self.DATASET.columns[1:].tolist()
        sum_value = 0
        for i in range(len(lst)-1):
            sum_value += sum(row[lst[i]])

        return sum_value
    

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


    def graph_02(self):
        # https://plot.ly/python/bubble-charts/
        # https://plot.ly/python/reference/#layout-xaxis
        # https://plot.ly/python/axes/#subcategory-axes
        
        max_value = 0

        lst = self.DATASET.columns[1:].tolist()
        sum_value = 0
        for i in range(len(self.DATASET)):
            for j in range(0,len(lst)-1):
                sum_value = sum(self.DATASET.loc[i,lst[j]])
                max_value = max(sum_value,max_value)
        # Falta pegar o vídeo que teve mais acesso
        sizeref = 2.*max_value/(max_value**2)
        print (max_value)
        # trace = []        
        # for i in range(0, len(self.DATASET)):                    
        #     trace.append(
        #         Scatter(
        #             # x=self.DATASET.iloc[:,0].values, #students
        #             # x=[self.DATASET.iloc[i,0]], #Students
        #             x=[self.DATASET.iloc[i,0]]*len(self.DATASET.columns), #student
        #             y=self.DATASET.columns[1:], #materials
        #             mode='markers',
        #             # name=self.DATASET.iloc[i,0], #each student name
        #             name=self.DATASET.iloc[i,0], #student name
        #             # orientation = "h",
        #             text = self.DATASET.iloc[i,1:].values.tolist(),
        #             marker=dict(
        #                 symbol='circle',
        #                 sizemode='area',
        #                 sizeref=sizeref,
        #                 # size=self.DATASET.iloc[:,i].values.tolist(),
        #                 size=self.DATASET.iloc[i,1:].values.tolist(),
        #                 line=dict(
        #                     width=2
        #                 )
        #             )
        #         )
        #     )

        # layout = Layout(
        #     title='Número de acessos nos materiais por estudante',
        #     # title='Number of access in the materials grouped by student',
        #     hovermode = "closest",
        #     showlegend = True,
        #     xaxis = dict(
        #         autorange = False,
        #         categoryorder = "category ascending",
        #         # domain = [0, 1],
        #         fixedrange = False,
        #         range = [-1, len(self.DATASET)],
        #         rangemode = "normal",
        #         showline = True,
        #         title = "Estudantes",
        #         type = "category"
        #     ),
        #     yaxis = dict(
        #         autorange = False,
        #         categoryorder = "category ascending",
        #         # domain = [0, 1],
        #         fixedrange = False,
        #         range = [-1, len(self.DATASET.columns[1:])],
        #         rangemode = "normal",
        #         showline = True,
        #         title = "Materiais",
        #         type = "category"
        #     )
        # )


    def print_all_graphs(self):
        self.graph_01()
        self.graph_02()
        # self.graph_03()
        # self.graph_04()

instance = V004(20)
instance.print_all_graphs()        