import pandas as pd
import numpy as np



from plotly.graph_objs import Figure, Layout, Bar, Table, Heatmap, Scatter
from plotly.offline import init_notebook_mode, iplot

from sklearn import metrics
from sklearn.cluster import KMeans


init_notebook_mode(connected=True) # initiate notebook for offline plot

class V005:
    NUMBER_STUDENTS = 50
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
            self.DATASET.loc[i,"Grade"] = int(np.random.triangular(0,60,100))
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


        dfk = self.DATASET.iloc[0:,1:4]
        kmeans = KMeans(n_clusters=3).fit(dfk)
        self.DATASET["Cluster"] = np.asarray(kmeans.labels_)

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


    def graph_02(self):

        trace1 = Scatter(
        x = self.DATASET.iloc[0:,2],
        y = self.DATASET.iloc[0:,1],
        text = self.DATASET.iloc[0:,0],

        mode='markers',
        marker=dict(
            size=12,
            symbol = self.DATASET.iloc[0:,5],
            color = self.DATASET.iloc[0:,5], #set color equal to a variable
            colorscale='Viridis',
            )
        )
        data = [trace1]
        layout = Layout(
            legend=dict(orientation="h")
        )
        fig = Figure(data=data, layout=layout)

        iplot(data, filename='scatter-plot')

    def print_all_graphs(self):
        self.graph_01()
        self.graph_02()

instance = V005(50)
instance.print_all_graphs()
