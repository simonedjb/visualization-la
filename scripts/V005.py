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
        self.DATASET = pd.DataFrame(columns=["Students","Grade","Access","Forum Access","Forum Post","Forum Replies","Forum Add Thread", 
                                                "Assign1","Assign2","Assign3","Assign4","AssignTotal","Video1","Video2", 
                                                "Quiz1","Quiz2","Pdf1","Pdf2","Ebook1","Ebook2","MaterialTotal"])
        for i in range(1,self.NUMBER_STUDENTS):
            self.DATASET.loc[i,"Students"] = "Student_"+str(i)
            self.DATASET.loc[i,"Grade"] = int(np.random.triangular(0,50,100))
            if (self.DATASET.loc[i,"Grade"] <= 50):
                self.DATASET.loc[i,"Access"] = int(np.random.triangular(5,15,25))
                self.DATASET.loc[i,"Forum Post"] = int(np.random.triangular(0,0,3))
                self.DATASET.loc[i,"Forum Replies"] = int(np.random.triangular(0,0,3))
                self.DATASET.loc[i,"Forum Add Thread"] = int(np.random.triangular(0,0,3))

                self.DATASET.loc[i,"Assign1"] = int(np.random.triangular(0,0,1))
                self.DATASET.loc[i,"Assign2"] = int(np.random.triangular(0,0,1))
                self.DATASET.loc[i,"Assign3"] = int(np.random.triangular(0,0,1))
                self.DATASET.loc[i,"Assign4"] = int(np.random.triangular(0,0,1))

                self.DATASET.loc[i,"Video1"] = int(np.random.triangular(0,0,1))
                self.DATASET.loc[i,"Video2"] = int(np.random.triangular(0,0,1))
                self.DATASET.loc[i,"Quiz1"] = int(np.random.triangular(0,0,1))
                self.DATASET.loc[i,"Quiz2"] = int(np.random.triangular(0,0,1))
                self.DATASET.loc[i,"Pdf1"] = int(np.random.triangular(0,0,1))
                self.DATASET.loc[i,"Pdf2"] = int(np.random.triangular(0,0,1))
                self.DATASET.loc[i,"Ebook1"] = int(np.random.triangular(0,0,1))
                self.DATASET.loc[i,"Ebook2"] = int(np.random.triangular(0,0,1))

                self.DATASET.loc[i,"Forum Access"] =  self.DATASET.loc[i,"Forum Post"] + self.DATASET.loc[i,"Forum Replies"] + self.DATASET.loc[i,"Forum Add Thread"] + int(np.random.triangular(0,3,6))
                self.DATASET.loc[i,"AssignTotal"] = self.DATASET.loc[i,"Assign1"] + self.DATASET.loc[i,"Assign2"] + self.DATASET.loc[i,"Assign3"] + self.DATASET.loc[i,"Assign4"]
                self.DATASET.loc[i,"MaterialTotal"] = self.DATASET.loc[i,"Video1"] + self.DATASET.loc[i,"Video2"] + self.DATASET.loc[i,"Quiz1"] + self.DATASET.loc[i,"Quiz2"] + self.DATASET.loc[i,"Pdf1"] + self.DATASET.loc[i,"Pdf2"] + self.DATASET.loc[i,"Ebook1"] + self.DATASET.loc[i,"Ebook2"]  


            elif (self.DATASET.loc[i,"Grade"] <= 60):
                self.DATASET.loc[i,"Access"] = int(np.random.triangular(20,30,40))
                self.DATASET.loc[i,"Forum Post"] = int(np.random.triangular(0,2,7))
                self.DATASET.loc[i,"Forum Replies"] = int(np.random.triangular(0,2,7))
                self.DATASET.loc[i,"Forum Add Thread"] = int(np.random.triangular(0,2,3))

                self.DATASET.loc[i,"Assign1"] = int(np.random.triangular(0,0,1))
                self.DATASET.loc[i,"Assign2"] = int(np.random.triangular(0,0,1))
                self.DATASET.loc[i,"Assign3"] = int(np.random.triangular(0,0,1))
                self.DATASET.loc[i,"Assign4"] = int(np.random.triangular(0,0,1))

                self.DATASET.loc[i,"Video1"] = int(np.random.triangular(0,1,3))
                self.DATASET.loc[i,"Video2"] = int(np.random.triangular(0,1,3))
                self.DATASET.loc[i,"Quiz1"] = int(np.random.triangular(0,1,3))
                self.DATASET.loc[i,"Quiz2"] = int(np.random.triangular(0,1,3))
                self.DATASET.loc[i,"Pdf1"] = int(np.random.triangular(0,1,3))
                self.DATASET.loc[i,"Pdf2"] = int(np.random.triangular(0,1,3))
                self.DATASET.loc[i,"Ebook1"] = int(np.random.triangular(0,1,3))
                self.DATASET.loc[i,"Ebook2"] = int(np.random.triangular(0,1,3))

                self.DATASET.loc[i,"Forum Access"] =  self.DATASET.loc[i,"Forum Post"] + self.DATASET.loc[i,"Forum Replies"] + self.DATASET.loc[i,"Forum Add Thread"] + int(np.random.triangular(0,7,20))
                self.DATASET.loc[i,"AssignTotal"] = self.DATASET.loc[i,"Assign1"] + self.DATASET.loc[i,"Assign2"] + self.DATASET.loc[i,"Assign3"] + self.DATASET.loc[i,"Assign4"]
                self.DATASET.loc[i,"MaterialTotal"] = self.DATASET.loc[i,"Video1"] + self.DATASET.loc[i,"Video2"] + self.DATASET.loc[i,"Quiz1"] + self.DATASET.loc[i,"Quiz2"] + self.DATASET.loc[i,"Pdf1"] + self.DATASET.loc[i,"Pdf2"] + self.DATASET.loc[i,"Ebook1"] + self.DATASET.loc[i,"Ebook2"]  

            elif (self.DATASET.loc[i,"Grade"] <= 70):
                self.DATASET.loc[i,"Access"] = int(np.random.triangular(35,45,55))
                self.DATASET.loc[i,"Forum Post"] = int(np.random.triangular(1,5,10))
                self.DATASET.loc[i,"Forum Replies"] = int(np.random.triangular(0,5,10))
                self.DATASET.loc[i,"Forum Add Thread"] = int(np.random.triangular(0,4,6))

                self.DATASET.loc[i,"Assign1"] = int(np.random.triangular(0,1,1))
                self.DATASET.loc[i,"Assign2"] = int(np.random.triangular(0,1,1))
                self.DATASET.loc[i,"Assign3"] = int(np.random.triangular(0,1,1))
                self.DATASET.loc[i,"Assign4"] = int(np.random.triangular(0,1,1))

                self.DATASET.loc[i,"Video1"] = int(np.random.triangular(0,2,5))
                self.DATASET.loc[i,"Video2"] = int(np.random.triangular(0,2,5))
                self.DATASET.loc[i,"Quiz1"] = int(np.random.triangular(0,2,5))
                self.DATASET.loc[i,"Quiz2"] = int(np.random.triangular(0,2,5))
                self.DATASET.loc[i,"Pdf1"] = int(np.random.triangular(0,2,5))
                self.DATASET.loc[i,"Pdf2"] = int(np.random.triangular(0,2,5))
                self.DATASET.loc[i,"Ebook1"] = int(np.random.triangular(0,2,5))
                self.DATASET.loc[i,"Ebook2"] = int(np.random.triangular(0,2,5))

                self.DATASET.loc[i,"Forum Access"] =  self.DATASET.loc[i,"Forum Post"] + self.DATASET.loc[i,"Forum Replies"] + self.DATASET.loc[i,"Forum Add Thread"] + int(np.random.triangular(2,10,25))
                self.DATASET.loc[i,"AssignTotal"] = self.DATASET.loc[i,"Assign1"] + self.DATASET.loc[i,"Assign2"] + self.DATASET.loc[i,"Assign3"] + self.DATASET.loc[i,"Assign4"]
                self.DATASET.loc[i,"MaterialTotal"] = self.DATASET.loc[i,"Video1"] + self.DATASET.loc[i,"Video2"] + self.DATASET.loc[i,"Quiz1"] + self.DATASET.loc[i,"Quiz2"] + self.DATASET.loc[i,"Pdf1"] + self.DATASET.loc[i,"Pdf2"] + self.DATASET.loc[i,"Ebook1"] + self.DATASET.loc[i,"Ebook2"]  

            elif (self.DATASET.loc[i,"Grade"] <= 80):
                self.DATASET.loc[i,"Access"] = int(np.random.triangular(50,60,70))
                self.DATASET.loc[i,"Forum Post"] = int(np.random.triangular(2,10,20))
                self.DATASET.loc[i,"Forum Replies"] = int(np.random.triangular(2,10,20))
                self.DATASET.loc[i,"Forum Add Thread"] = int(np.random.triangular(0,4,6))

                self.DATASET.loc[i,"Assign1"] = int(np.random.triangular(0,1,1))
                self.DATASET.loc[i,"Assign2"] = int(np.random.triangular(0,1,1))
                self.DATASET.loc[i,"Assign3"] = int(np.random.triangular(0,1,1))
                self.DATASET.loc[i,"Assign4"] = int(np.random.triangular(0,1,1))

                self.DATASET.loc[i,"Video1"] = int(np.random.triangular(0,5,10))
                self.DATASET.loc[i,"Video2"] = int(np.random.triangular(1,5,10))
                self.DATASET.loc[i,"Quiz1"] = int(np.random.triangular(0,5,10))
                self.DATASET.loc[i,"Quiz2"] = int(np.random.triangular(1,5,10))
                self.DATASET.loc[i,"Pdf1"] = int(np.random.triangular(0,5,10))
                self.DATASET.loc[i,"Pdf2"] = int(np.random.triangular(1,5,10))
                self.DATASET.loc[i,"Ebook1"] = int(np.random.triangular(0,5,10))
                self.DATASET.loc[i,"Ebook2"] = int(np.random.triangular(1,5,10))

                self.DATASET.loc[i,"Forum Access"] =  self.DATASET.loc[i,"Forum Post"] + self.DATASET.loc[i,"Forum Replies"] + self.DATASET.loc[i,"Forum Add Thread"] + int(np.random.triangular(4,15,30))
                self.DATASET.loc[i,"AssignTotal"] = self.DATASET.loc[i,"Assign1"] + self.DATASET.loc[i,"Assign2"] + self.DATASET.loc[i,"Assign3"] + self.DATASET.loc[i,"Assign4"]
                self.DATASET.loc[i,"MaterialTotal"] = self.DATASET.loc[i,"Video1"] + self.DATASET.loc[i,"Video2"] + self.DATASET.loc[i,"Quiz1"] + self.DATASET.loc[i,"Quiz2"] + self.DATASET.loc[i,"Pdf1"] + self.DATASET.loc[i,"Pdf2"] + self.DATASET.loc[i,"Ebook1"] + self.DATASET.loc[i,"Ebook2"]  

            elif (self.DATASET.loc[i,"Grade"] <= 90):
                self.DATASET.loc[i,"Access"] = int(np.random.triangular(65,75,85))
                self.DATASET.loc[i,"Forum Post"] = int(np.random.triangular(5,15,35))
                self.DATASET.loc[i,"Forum Replies"] = int(np.random.triangular(5,15,35))
                self.DATASET.loc[i,"Forum Add Thread"] = int(np.random.triangular(1,7,10))

                self.DATASET.loc[i,"Assign1"] = int(np.random.triangular(0,1,1))
                self.DATASET.loc[i,"Assign2"] = int(1)
                self.DATASET.loc[i,"Assign3"] = int(np.random.triangular(0,1,1))
                self.DATASET.loc[i,"Assign4"] = int(1)

                self.DATASET.loc[i,"Video1"] = int(np.random.triangular(1,4,9))
                self.DATASET.loc[i,"Video2"] = int(np.random.triangular(3,8,13))
                self.DATASET.loc[i,"Quiz1"] = int(np.random.triangular(1,4,9))
                self.DATASET.loc[i,"Quiz2"] = int(np.random.triangular(3,8,13))
                self.DATASET.loc[i,"Pdf1"] = int(np.random.triangular(1,4,9))
                self.DATASET.loc[i,"Pdf2"] = int(np.random.triangular(3,8,13))
                self.DATASET.loc[i,"Ebook1"] = int(np.random.triangular(1,4,9))
                self.DATASET.loc[i,"Ebook2"] = int(np.random.triangular(3,8,13))

                self.DATASET.loc[i,"Forum Access"] =  self.DATASET.loc[i,"Forum Post"] + self.DATASET.loc[i,"Forum Replies"] + self.DATASET.loc[i,"Forum Add Thread"] + int(np.random.triangular(6,18,35))
                self.DATASET.loc[i,"AssignTotal"] = self.DATASET.loc[i,"Assign1"] + self.DATASET.loc[i,"Assign2"] + self.DATASET.loc[i,"Assign3"] + self.DATASET.loc[i,"Assign4"]
                self.DATASET.loc[i,"MaterialTotal"] = self.DATASET.loc[i,"Video1"] + self.DATASET.loc[i,"Video2"] + self.DATASET.loc[i,"Quiz1"] + self.DATASET.loc[i,"Quiz2"] + self.DATASET.loc[i,"Pdf1"] + self.DATASET.loc[i,"Pdf2"] + self.DATASET.loc[i,"Ebook1"] + self.DATASET.loc[i,"Ebook2"]  


            else:
                self.DATASET.loc[i,"Access"] = int(np.random.triangular(80,90,100))
                self.DATASET.loc[i,"Forum Post"] = int(np.random.triangular(10,20,40))
                self.DATASET.loc[i,"Forum Replies"] = int(np.random.triangular(10,20,40))
                self.DATASET.loc[i,"Forum Add Thread"] = int(np.random.triangular(3,9,13))

                self.DATASET.loc[i,"Assign1"] = int(1)
                self.DATASET.loc[i,"Assign2"] = int(1)
                self.DATASET.loc[i,"Assign3"] = int(1)
                self.DATASET.loc[i,"Assign4"] = int(1)

                self.DATASET.loc[i,"Video1"] = int(np.random.triangular(2,6,12))
                self.DATASET.loc[i,"Video2"] = int(np.random.triangular(4,8,14))
                self.DATASET.loc[i,"Quiz1"] = int(np.random.triangular(2,6,12))
                self.DATASET.loc[i,"Quiz2"] = int(np.random.triangular(4,8,14))
                self.DATASET.loc[i,"Pdf1"] = int(np.random.triangular(2,6,12))
                self.DATASET.loc[i,"Pdf2"] = int(np.random.triangular(4,8,14))
                self.DATASET.loc[i,"Ebook1"] = int(np.random.triangular(2,6,12))
                self.DATASET.loc[i,"Ebook2"] = int(np.random.triangular(4,8,14))

                self.DATASET.loc[i,"Forum Access"] =  self.DATASET.loc[i,"Forum Post"] + self.DATASET.loc[i,"Forum Replies"] + self.DATASET.loc[i,"Forum Add Thread"] + int(np.random.triangular(10,20,40))
                self.DATASET.loc[i,"AssignTotal"] = self.DATASET.loc[i,"Assign1"] + self.DATASET.loc[i,"Assign2"] + self.DATASET.loc[i,"Assign3"] + self.DATASET.loc[i,"Assign4"]
                self.DATASET.loc[i,"MaterialTotal"] = self.DATASET.loc[i,"Video1"] + self.DATASET.loc[i,"Video2"] + self.DATASET.loc[i,"Quiz1"] + self.DATASET.loc[i,"Quiz2"] + self.DATASET.loc[i,"Pdf1"] + self.DATASET.loc[i,"Pdf2"] + self.DATASET.loc[i,"Ebook1"] + self.DATASET.loc[i,"Ebook2"]  


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
            symbol = self.DATASET.iloc[0:,21],
            color = self.DATASET.iloc[0:,21], #set color equal to a variable
            colorscale='Viridis',
            line = dict(
            color = 'rgb(105, 105, 105)',
            width = 1
          )
            )
        )
        data = [trace1]
        layout = Layout(
            title='Notas dos estudantes vs acesso ao sistema',
            # title='Number of access in the materials grouped by student',
            hovermode = "closest",
            showlegend = True,
            xaxis = dict(
                fixedrange = False,
                title = "Notas",
                type = "category"
            ),
            yaxis = dict(
                categoryorder = "category ascending",
                fixedrange = False,
                title = "Acesso ao Sistema",
                type = "category"
            )
        )
        fig = Figure(data=data, layout=layout)
        iplot(data, filename='scatter-plot')

    def graph_03(self):

        trace1 = Scatter(
        x = self.DATASET.iloc[0:,2],
        y = self.DATASET.iloc[0:,18],
        text = self.DATASET.iloc[0:,0],

        mode='markers',
        marker=dict(
            size=12,
            symbol = self.DATASET.iloc[0:,21],
            color = self.DATASET.iloc[0:,21], #set color equal to a variable
            colorscale='Viridis',
            line = dict(
            color = 'rgb(105, 105, 105)',
            width = 1
          )
            )
        )
        data = [trace1]
        layout = Layout(
            title='Notas dos estudantes vs acesso ao sistema',
            # title='Number of access in the materials grouped by student',
            hovermode = "closest",
            showlegend = True,
            xaxis = dict(
                fixedrange = False,
                title = "Notas",
                type = "category"
            ),
            yaxis = dict(
                categoryorder = "category ascending",
                fixedrange = False,
                title = "Acesso ao Sistema",
                type = "category"
            )
        )
        fig = Figure(data=data, layout=layout)
        iplot(data, filename='scatter-plot')

    def graph_04(self):

        trace1 = Scatter(
        x = self.DATASET.iloc[0:,2],
        y = self.DATASET.iloc[0:,19],
        text = self.DATASET.iloc[0:,0],

        mode='markers',
        marker=dict(
            size=12,
            symbol = self.DATASET.iloc[0:,21],
            color = self.DATASET.iloc[0:,21], #set color equal to a variable
            colorscale='Viridis',
            line = dict(
            color = 'rgb(105, 105, 105)',
            width = 1
          )
            )
        )
        data = [trace1]
        layout = Layout(
            title='Notas dos estudantes vs acesso ao sistema',
            # title='Number of access in the materials grouped by student',
            hovermode = "closest",
            showlegend = True,
            xaxis = dict(
                fixedrange = False,
                title = "Notas",
                type = "category"
            ),
            yaxis = dict(
                categoryorder = "category ascending",
                fixedrange = False,
                title = "Acesso ao Sistema",
                type = "category"
            )
        )
        fig = Figure(data=data, layout=layout)
        iplot(data, filename='scatter-plot')

    def graph_05(self):

        trace1 = Scatter(
        x = self.DATASET.iloc[0:,2],
        y = self.DATASET.iloc[0:,20],
        text = self.DATASET.iloc[0:,0],

        mode='markers',
        marker=dict(
            size=12,
            symbol = self.DATASET.iloc[0:,21],
            color = self.DATASET.iloc[0:,21], #set color equal to a variable
            colorscale='Viridis',
            line = dict(
            color = 'rgb(105, 105, 105)',
            width = 1
          )
            )
        )
        data = [trace1]
        layout = Layout(
            title='Notas dos estudantes vs acesso ao sistema',
            # title='Number of access in the materials grouped by student',
            hovermode = "closest",
            showlegend = True,
            xaxis = dict(
                fixedrange = False,
                title = "Notas",
                type = "category"
            ),
            yaxis = dict(
                categoryorder = "category ascending",
                fixedrange = False,
                title = "Acesso ao Sistema",
                type = "category"
            )
        )
        fig = Figure(data=data, layout=layout)
        iplot(data, filename='scatter-plot')

    def print_all_graphs(self):
        self.graph_01()
        self.graph_02()
        self.graph_03()
#        self.graph_04()
        self.graph_05()

instance = V005(60)
instance.print_all_graphs()
