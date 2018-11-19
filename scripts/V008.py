import pandas as pd
import numpy as np

from plotly.graph_objs import Figure, Layout, Bar, Table, Heatmap, Scatter, Box, Violin
from plotly.offline import init_notebook_mode, iplot

from sklearn import metrics
from sklearn.cluster import KMeans


init_notebook_mode(connected=True) # initiate notebook for offline plot

class V008:
    NUMBER_STUDENTS = 50
    DATASET = pd.DataFrame()

    _language = "pt"
    _weeks = 7

    _df_sum_day = pd.DataFrame()
    _df_sum_week = pd.DataFrame()
    _df_all_day = pd.DataFrame()

    def __init__(self, number_students = 20, language = "pt"):
        self.NUMBER_STUDENTS = number_students
        self._language = language
        self.generate_dataset()

    def generate_dataset(self):
        names = pd.read_csv("names.csv")
        self.DATASET = pd.DataFrame(columns=["Students","Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"])

        rand_names = [names.group_name[np.random.randint(0,len(names.group_name)+1)] for n in range(0,self.NUMBER_STUDENTS)]
        rand_names.sort()

        for i in range(0,self.NUMBER_STUDENTS):
            self.DATASET.loc[i,"Students"] = rand_names[i]            

            lst = sorted(np.random.triangular(0,5,15,int(self._weeks/2)+(self._weeks%2))) + sorted(np.random.triangular(0,5,15,int(self._weeks/2)))
            self.DATASET.loc[i,"Sunday"] = [int(i) for i in lst]

            lst = sorted(np.random.triangular(0,8,18,int(self._weeks/2)+(self._weeks%2))) + sorted(np.random.triangular(0,8,18,int(self._weeks/2)))
            self.DATASET.loc[i,"Monday"] = [int(i) for i in lst]

            lst = sorted(np.random.triangular(0,10,20,int(self._weeks/2)+(self._weeks%2))) + sorted(np.random.triangular(0,10,20,int(self._weeks/2)))
            self.DATASET.loc[i,"Tuesday"] = [int(i) for i in lst]

            lst = sorted(np.random.triangular(0,12,23,int(self._weeks/2)+(self._weeks%2))) + sorted(np.random.triangular(0,12,23,int(self._weeks/2)))
            self.DATASET.loc[i,"Wednesday"] = [int(i) for i in lst]

            lst = sorted(np.random.triangular(0,15,26,int(self._weeks/2)+(self._weeks%2))) + sorted(np.random.triangular(0,15,26,int(self._weeks/2)))
            self.DATASET.loc[i,"Thursday"] = [int(i) for i in lst]

            lst = sorted(np.random.triangular(0,17,28,int(self._weeks/2)+(self._weeks%2))) + sorted(np.random.triangular(0,17,28,int(self._weeks/2)))
            self.DATASET.loc[i,"Friday"] = [int(i) for i in lst]

            lst = sorted(np.random.triangular(0,8,34,int(self._weeks/2)+(self._weeks%2))) + sorted(np.random.triangular(0,8,34,int(self._weeks/2)))
            self.DATASET.loc[i,"Saturday"] = [int(i) for i in lst]

        self._df_sum_day = self.DATASET.apply(self.sum_access_by_day, axis=1, result_type='expand') # Total of access by day
        self._df_sum_day.columns = self.DATASET.columns

        self._df_sum_week = self.DATASET.apply(self.sum_access_by_week, axis=1, result_type='expand') # Total of access by week
        self._df_sum_week.columns = ["Week"+str(i+1) for i in range(0,self._weeks)]
        self._df_sum_week.insert(0,"Students",self.DATASET.Students)

        self._df_all_day = self.DATASET.apply(self.all_day, axis=1, result_type='expand') # All days
        self._df_all_day.insert(0,"Students",self.DATASET.Students)        

    def sum_access_by_day(self,row):
        lst = []
        lst.append(row[0])
        
        for i in range(1,len(row)):
            lst.append(sum(row[i]))
        
        return lst

    def sum_access_by_week(self,row):
        lst = []
        sum = 0
        
        for i in range(0,self._weeks):
            for j in range(1,len(row)):
                sum+=row[j][i]
            lst.append(sum)
            sum = 0

        return lst

    def all_day(self,row):
        lst = []

        for i in range(0,self._weeks):
            for j in range(1,len(row)):
                lst.append(row[j][i])
        
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
        df = self._df_sum_day

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

    def graph_03(self):
        df = self._df_sum_week

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

    # Heatmap
    def graph_04(self):
        legend = {"title":"Número de acessos por estudante",
                    "xaxis":"",
                    "yaxis":"",
                    "columns":{1:"Dom", 2:"Seg", 3:"Ter", 4:"Qua", 5:"Qui", 6:"Sex", 0:"Sáb"},
                    "misc":"dia"
                }
        if (self._language == "en"):
            legend = {"title":"Number of access by student",
                        "xaxis":"",
                        "yaxis":"",
                        "columns":{1:"Sun", 2:"Mon", 3:"Tue", 4:"Wed", 5:"Thu", 6:"Fri", 0:"Sat"},
                        "misc":"day"
                    }
        df = self._df_all_day
        z = []
        for i in range (1, len(df.columns)):
            z.append(df.iloc[:,i].values.tolist())
        
        trace = Heatmap(z=z,
                        y=[legend["columns"][(int((i+1)%7))]+", "+legend["misc"]+" "+str(i+1) for i in range (0,len(df.columns))],
                        # y=[legend["columns"][i] for i in range (1,4)],
                        # y=df.columns[1:len(df.columns)-1], #Assigns
                        x=df.iloc[:,0], #Students
                        colorscale=[[0, 'rgb(255,255,255)'], [1, 'rgb(0,0,255)']],
                        showscale = True
                    )
        
        layout = Layout(
                title = legend["title"],
                autosize=True,
                # width=1050,
                height=950,
                hovermode = "closest",                
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
        self.graph_01() #Table raw
        self.graph_02() 
        self.graph_03()
        self.graph_04() # Heatmap
        # self.graph_05() # Heatmap
        # self.graph_06() #Box
        # self.graph_07()
        # self.graph_08()
        # self.graph_09()
        # self.graph_10() #Violin
        # self.graph_11()
        # self.graph_12()
        # self.graph_13()

instance = V008(35)
# instance.print_all_graphs("pt")
instance.print_all_graphs("en")