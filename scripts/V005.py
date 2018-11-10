import pandas as pd
import numpy as np

from plotly.graph_objs import Figure, Layout, Table, Scatter, Box, Violin
from plotly.offline import init_notebook_mode, iplot

from sklearn import metrics
from sklearn.cluster import KMeans


init_notebook_mode(connected=True) # initiate notebook for offline plot

class V005:
    NUMBER_STUDENTS = 50
    DATASET = pd.DataFrame()

    _df_sum = []

    def __init__(self, number_students = 20):
        self.NUMBER_STUDENTS = number_students
        self.generate_dataset()

    def generate_dataset(self):
        self._df_sum = pd.DataFrame(columns=["Students","Grade","AssignTotal","MaterialTotal"])

        self.DATASET = pd.DataFrame(columns=["Students","Grade","Access",
                                                "Forum Access","Forum Post","Forum Replies","Forum Add Thread", 
                                                "Assign1","Assign2","Assign3","Assign4","Video1","Video2", 
                                                "Quiz1","Quiz2","Pdf1","Pdf2","Ebook1","Ebook2",])
        
        self.DATASET.Grade = np.random.triangular(0,85,100,self.NUMBER_STUDENTS)
        self.DATASET["Grade"] = self.DATASET.apply(self.convert_to_int, axis=1)
        
        for i in range(0,self.NUMBER_STUDENTS):
            self.DATASET.loc[i,"Students"] = "Student_"+str(i+1)
            
            if (self.DATASET.loc[i,"Grade"] <= 50):
                self.DATASET.loc[i,"Access"] = np.random.randint(5,26)
                self.DATASET.loc[i,"Forum Post"] = np.random.randint(0,4)
                self.DATASET.loc[i,"Forum Replies"] = np.random.randint(0,4)
                self.DATASET.loc[i,"Forum Add Thread"] = np.random.randint(0,4)

                self.DATASET.loc[i,"Assign1"] = int(0)
                self.DATASET.loc[i,"Assign2"] = int(0)
                self.DATASET.loc[i,"Assign3"] = int(0)
                self.DATASET.loc[i,"Assign4"] = int(0)

                self.DATASET.loc[i,"Video1"] = np.random.randint(0,2)
                self.DATASET.loc[i,"Video2"] = np.random.randint(0,2)
                self.DATASET.loc[i,"Quiz1"] = np.random.randint(0,2)
                self.DATASET.loc[i,"Quiz2"] = np.random.randint(0,2)
                self.DATASET.loc[i,"Pdf1"] = np.random.randint(0,2)
                self.DATASET.loc[i,"Pdf2"] = np.random.randint(0,2)
                self.DATASET.loc[i,"Ebook1"] = np.random.randint(0,2)
                self.DATASET.loc[i,"Ebook2"] = np.random.randint(0,2)

                self.DATASET.loc[i,"Forum Access"] =  self.DATASET.loc[i,"Forum Post"] + self.DATASET.loc[i,"Forum Replies"] + self.DATASET.loc[i,"Forum Add Thread"] + np.random.randint(0,7)
                self._df_sum.loc[i,"AssignTotal"] = self.DATASET.loc[i,"Assign1"] + self.DATASET.loc[i,"Assign2"] + self.DATASET.loc[i,"Assign3"] + self.DATASET.loc[i,"Assign4"]
                self._df_sum.loc[i,"MaterialTotal"] = self.DATASET.loc[i,"Video1"] + self.DATASET.loc[i,"Video2"] + self.DATASET.loc[i,"Quiz1"] + self.DATASET.loc[i,"Quiz2"] + self.DATASET.loc[i,"Pdf1"] + self.DATASET.loc[i,"Pdf2"] + self.DATASET.loc[i,"Ebook1"] + self.DATASET.loc[i,"Ebook2"]  

            elif (self.DATASET.loc[i,"Grade"] <= 60):
                self.DATASET.loc[i,"Access"] = np.random.randint(20,41)
                self.DATASET.loc[i,"Forum Post"] = np.random.randint(0,8)
                self.DATASET.loc[i,"Forum Replies"] = np.random.randint(0,8)
                self.DATASET.loc[i,"Forum Add Thread"] = np.random.randint(0,4)

                self.DATASET.loc[i,"Assign1"] = int(1)
                self.DATASET.loc[i,"Assign2"] = np.random.randint(0,2)
                self.DATASET.loc[i,"Assign3"] = np.random.randint(0,2)
                self.DATASET.loc[i,"Assign4"] = np.random.randint(0,2)

                self.DATASET.loc[i,"Video1"] = np.random.randint(0,5)
                self.DATASET.loc[i,"Video2"] = np.random.randint(0,5)
                self.DATASET.loc[i,"Quiz1"] = np.random.randint(0,5)
                self.DATASET.loc[i,"Quiz2"] = np.random.randint(0,5)
                self.DATASET.loc[i,"Pdf1"] = np.random.randint(0,5)
                self.DATASET.loc[i,"Pdf2"] = np.random.randint(0,5)
                self.DATASET.loc[i,"Ebook1"] = np.random.randint(0,5)
                self.DATASET.loc[i,"Ebook2"] = np.random.randint(0,5)

                self.DATASET.loc[i,"Forum Access"] = self.DATASET.loc[i,"Forum Post"] + self.DATASET.loc[i,"Forum Replies"] + self.DATASET.loc[i,"Forum Add Thread"] + np.random.randint(0,22)
                self._df_sum.loc[i,"AssignTotal"] = self.DATASET.loc[i,"Assign1"] + self.DATASET.loc[i,"Assign2"] + self.DATASET.loc[i,"Assign3"] + self.DATASET.loc[i,"Assign4"]
                self._df_sum.loc[i,"MaterialTotal"] = self.DATASET.loc[i,"Video1"] + self.DATASET.loc[i,"Video2"] + self.DATASET.loc[i,"Quiz1"] + self.DATASET.loc[i,"Quiz2"] + self.DATASET.loc[i,"Pdf1"] + self.DATASET.loc[i,"Pdf2"] + self.DATASET.loc[i,"Ebook1"] + self.DATASET.loc[i,"Ebook2"]

            elif (self.DATASET.loc[i,"Grade"] <= 70):
                self.DATASET.loc[i,"Access"] = np.random.randint(35,57)
                self.DATASET.loc[i,"Forum Post"] = np.random.randint(1,12)
                self.DATASET.loc[i,"Forum Replies"] = np.random.randint(0,12)
                self.DATASET.loc[i,"Forum Add Thread"] = np.random.randint(0,8)

                self.DATASET.loc[i,"Assign1"] = int(1)
                self.DATASET.loc[i,"Assign2"] = np.random.randint(0,2)
                self.DATASET.loc[i,"Assign3"] = np.random.randint(0,2)
                self.DATASET.loc[i,"Assign4"] = int(1)

                self.DATASET.loc[i,"Video1"] = np.random.randint(0,6)
                self.DATASET.loc[i,"Video2"] = np.random.randint(0,6)
                self.DATASET.loc[i,"Quiz1"] = np.random.randint(0,6)
                self.DATASET.loc[i,"Quiz2"] = np.random.randint(0,6)
                self.DATASET.loc[i,"Pdf1"] = np.random.randint(0,6)
                self.DATASET.loc[i,"Pdf2"] = np.random.randint(0,6)
                self.DATASET.loc[i,"Ebook1"] = np.random.randint(0,6)
                self.DATASET.loc[i,"Ebook2"] = np.random.randint(0,6)

                self.DATASET.loc[i,"Forum Access"] =  self.DATASET.loc[i,"Forum Post"] + self.DATASET.loc[i,"Forum Replies"] + self.DATASET.loc[i,"Forum Add Thread"] + np.random.randint(2,26)
                self._df_sum.loc[i,"AssignTotal"] = self.DATASET.loc[i,"Assign1"] + self.DATASET.loc[i,"Assign2"] + self.DATASET.loc[i,"Assign3"] + self.DATASET.loc[i,"Assign4"]
                self._df_sum.loc[i,"MaterialTotal"] = self.DATASET.loc[i,"Video1"] + self.DATASET.loc[i,"Video2"] + self.DATASET.loc[i,"Quiz1"] + self.DATASET.loc[i,"Quiz2"] + self.DATASET.loc[i,"Pdf1"] + self.DATASET.loc[i,"Pdf2"] + self.DATASET.loc[i,"Ebook1"] + self.DATASET.loc[i,"Ebook2"]

            elif (self.DATASET.loc[i,"Grade"] <= 80):
                self.DATASET.loc[i,"Access"] = np.random.randint(50,71)
                self.DATASET.loc[i,"Forum Post"] = np.random.randint(2,21)
                self.DATASET.loc[i,"Forum Replies"] = np.random.randint(2,21)
                self.DATASET.loc[i,"Forum Add Thread"] = np.random.randint(0,7)

                self.DATASET.loc[i,"Assign1"] = int(1)
                self.DATASET.loc[i,"Assign2"] = np.random.randint(0,2)
                self.DATASET.loc[i,"Assign3"] = np.random.randint(0,2)
                self.DATASET.loc[i,"Assign4"] = int(1)

                self.DATASET.loc[i,"Video1"] = np.random.randint(0,11)
                self.DATASET.loc[i,"Video2"] = np.random.randint(1,11)
                self.DATASET.loc[i,"Quiz1"] = np.random.randint(0,11)
                self.DATASET.loc[i,"Quiz2"] = np.random.randint(1,11)
                self.DATASET.loc[i,"Pdf1"] = np.random.randint(0,11)
                self.DATASET.loc[i,"Pdf2"] = np.random.randint(1,11)
                self.DATASET.loc[i,"Ebook1"] = np.random.randint(0,11)
                self.DATASET.loc[i,"Ebook2"] = np.random.randint(1,11)

                self.DATASET.loc[i,"Forum Access"] =  self.DATASET.loc[i,"Forum Post"] + self.DATASET.loc[i,"Forum Replies"] + self.DATASET.loc[i,"Forum Add Thread"] + np.random.randint(4,31)
                self._df_sum.loc[i,"AssignTotal"] = self.DATASET.loc[i,"Assign1"] + self.DATASET.loc[i,"Assign2"] + self.DATASET.loc[i,"Assign3"] + self.DATASET.loc[i,"Assign4"]
                self._df_sum.loc[i,"MaterialTotal"] = self.DATASET.loc[i,"Video1"] + self.DATASET.loc[i,"Video2"] + self.DATASET.loc[i,"Quiz1"] + self.DATASET.loc[i,"Quiz2"] + self.DATASET.loc[i,"Pdf1"] + self.DATASET.loc[i,"Pdf2"] + self.DATASET.loc[i,"Ebook1"] + self.DATASET.loc[i,"Ebook2"]

            elif (self.DATASET.loc[i,"Grade"] <= 90):
                self.DATASET.loc[i,"Access"] = np.random.randint(65,86)
                self.DATASET.loc[i,"Forum Post"] = np.random.randint(5,36)
                self.DATASET.loc[i,"Forum Replies"] = np.random.randint(5,36)
                self.DATASET.loc[i,"Forum Add Thread"] = np.random.randint(1,11)

                self.DATASET.loc[i,"Assign1"] = int(1)
                self.DATASET.loc[i,"Assign2"] = int(1)
                self.DATASET.loc[i,"Assign3"] = np.random.randint(0,2)
                self.DATASET.loc[i,"Assign4"] = int(1)

                self.DATASET.loc[i,"Video1"] = np.random.randint(1,10)
                self.DATASET.loc[i,"Video2"] = np.random.randint(3,14)
                self.DATASET.loc[i,"Quiz1"] = np.random.randint(1,10)
                self.DATASET.loc[i,"Quiz2"] = np.random.randint(3,14)
                self.DATASET.loc[i,"Pdf1"] = np.random.randint(1,10)
                self.DATASET.loc[i,"Pdf2"] = np.random.randint(3,14)
                self.DATASET.loc[i,"Ebook1"] = np.random.randint(1,10)
                self.DATASET.loc[i,"Ebook2"] = np.random.randint(3,14)

                self.DATASET.loc[i,"Forum Access"] =  self.DATASET.loc[i,"Forum Post"] + self.DATASET.loc[i,"Forum Replies"] + self.DATASET.loc[i,"Forum Add Thread"] + np.random.randint(6,36)
                self._df_sum.loc[i,"AssignTotal"] = self.DATASET.loc[i,"Assign1"] + self.DATASET.loc[i,"Assign2"] + self.DATASET.loc[i,"Assign3"] + self.DATASET.loc[i,"Assign4"]
                self._df_sum.loc[i,"MaterialTotal"] = self.DATASET.loc[i,"Video1"] + self.DATASET.loc[i,"Video2"] + self.DATASET.loc[i,"Quiz1"] + self.DATASET.loc[i,"Quiz2"] + self.DATASET.loc[i,"Pdf1"] + self.DATASET.loc[i,"Pdf2"] + self.DATASET.loc[i,"Ebook1"] + self.DATASET.loc[i,"Ebook2"]

            else:
                self.DATASET.loc[i,"Access"] = np.random.randint(80,101)
                self.DATASET.loc[i,"Forum Post"] = np.random.randint(10,41)
                self.DATASET.loc[i,"Forum Replies"] = np.random.randint(10,41)
                self.DATASET.loc[i,"Forum Add Thread"] = np.random.randint(3,14)

                self.DATASET.loc[i,"Assign1"] = int(1)
                self.DATASET.loc[i,"Assign2"] = int(1)
                self.DATASET.loc[i,"Assign3"] = int(1)
                self.DATASET.loc[i,"Assign4"] = int(1)

                self.DATASET.loc[i,"Video1"] = np.random.randint(2,13)
                self.DATASET.loc[i,"Video2"] = np.random.randint(4,15)
                self.DATASET.loc[i,"Quiz1"] = np.random.randint(2,13)
                self.DATASET.loc[i,"Quiz2"] = np.random.randint(4,15)
                self.DATASET.loc[i,"Pdf1"] = np.random.randint(2,13)
                self.DATASET.loc[i,"Pdf2"] = np.random.randint(4,15)
                self.DATASET.loc[i,"Ebook1"] = np.random.randint(2,13)
                self.DATASET.loc[i,"Ebook2"] = np.random.randint(4,15)

                self.DATASET.loc[i,"Forum Access"] =  self.DATASET.loc[i,"Forum Post"] + self.DATASET.loc[i,"Forum Replies"] + self.DATASET.loc[i,"Forum Add Thread"] + np.random.randint(10,41)
                self._df_sum.loc[i,"AssignTotal"] = self.DATASET.loc[i,"Assign1"] + self.DATASET.loc[i,"Assign2"] + self.DATASET.loc[i,"Assign3"] + self.DATASET.loc[i,"Assign4"]
                self._df_sum.loc[i,"MaterialTotal"] = self.DATASET.loc[i,"Video1"] + self.DATASET.loc[i,"Video2"] + self.DATASET.loc[i,"Quiz1"] + self.DATASET.loc[i,"Quiz2"] + self.DATASET.loc[i,"Pdf1"] + self.DATASET.loc[i,"Pdf2"] + self.DATASET.loc[i,"Ebook1"] + self.DATASET.loc[i,"Ebook2"]  


        df_k = self.DATASET.iloc[:,1:] #Selecting features to cluster
        kmeans = KMeans(n_clusters=4, init='random').fit(df_k) #Clustering
        self._df_sum["Cluster"] = np.asarray(kmeans.labels_)
        self._df_sum["Students"] = self.DATASET["Students"]
        self._df_sum["Grade"] = self.DATASET["Grade"]
        self._df_sum["Access"] = self.DATASET["Access"]
        self._df_sum["Forum Access"] = self.DATASET["Forum Access"]
        self._df_sum["Forum Post"] = self.DATASET["Forum Post"]
        self._df_sum["Forum Replies"] = self.DATASET["Forum Replies"]
        self._df_sum["Forum Add Thread"] = self.DATASET["Forum Add Thread"]

    def convert_to_int(self,row):
        return int(row["Grade"])

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
        df = self._df_sum.sort_values(by="Grade")
        Clusters = df.Cluster.unique()        
        color = ["rgb(255,0,0)","rgb(0,0,255)","rgb(127,0,127)","rgb(0,255,0)"]        
        color[Clusters[0]] = "rgb(255,0,0)"
        color[Clusters[1]] = "rgb(127,0,127)"
        color[Clusters[2]] = "rgb(0,0,255)"        
        color[Clusters[3]] = "rgb(0,255,0)"

        trace = []
        for i in range(0, self.NUMBER_STUDENTS):
            trace.append(
                Scatter(
                    x=[self.DATASET.Access[i]], #Access
                    y=[self.DATASET.Grade[i]], #Grade
                    mode='markers',
                    name=self.DATASET.Students[i], #each student name                    
                    text = [str(self.DATASET.Students[i])],                    
                    marker=dict(
                        size=12,
                        symbol=self._df_sum.Cluster[i],
                        color = color[self._df_sum.Cluster[i]],
                        colorscale='Viridis',
                        line=dict(
                            width=2
                        )
                    )
                )
            )

        layout = Layout(
            title='Notas dos estudantes vs acesso ao AVA',
            hovermode = "closest",
            showlegend = True,
            xaxis = dict(
                autorange = False,
                fixedrange = False,
                range = [0, self.DATASET.Access.max()+10],
                rangemode = "normal",
                zeroline= False,
                showline = True,
                title = "Acessos ao AVA",
                # type = "category"
            ),
            yaxis = dict(
                autorange = False,
                fixedrange = False,
                range = [0, self.DATASET.Grade.max()+10],
                rangemode = "normal",
                showline = True,
                title = "Notas",
                # type = "category"
            )
        )

        data = trace
        fig = Figure(data=data, layout=layout)
        iplot(fig, filename='scatter-plot')

    def graph_03(self):
        df = self._df_sum.sort_values(by="Grade")
        Clusters = df.Cluster.unique()        
        color = ["rgb(255,0,0)","rgb(0,0,255)","rgb(127,0,127)","rgb(0,255,0)"]        
        color[Clusters[0]] = "rgb(255,0,0)"
        color[Clusters[1]] = "rgb(127,0,127)"
        color[Clusters[2]] = "rgb(0,0,255)"        
        color[Clusters[3]] = "rgb(0,255,0)"

        trace = []
        for i in range(0, self.NUMBER_STUDENTS):
            trace.append(
                Scatter(
                    x=[self._df_sum.MaterialTotal[i]], #Material Access
                    y=[self.DATASET.Grade[i]], #Grade
                    mode='markers',
                    name=self.DATASET.Students[i], #each student name                    
                    text = [str(self.DATASET.Students[i])],                    
                    marker=dict(
                        size=12,
                        symbol=self._df_sum.Cluster[i],
                        color = color[self._df_sum.Cluster[i]],
                        colorscale='Viridis',
                        line=dict(
                            width=2
                        )
                    )
                )
            )

        layout = Layout(
            title='Notas dos estudantes vs acesso aos materiais',
            hovermode = "closest",
            showlegend = True,
            xaxis = dict(
                autorange = False,
                fixedrange = False,
                range = [0, self._df_sum.MaterialTotal.max()+10],
                rangemode = "normal",
                zeroline= False,
                showline = True,
                title = "Acesso aos materiais",                
            ),
            yaxis = dict(
                autorange = False,
                fixedrange = False,
                range = [0, self.DATASET.Grade.max()+10],
                rangemode = "normal",
                showline = True,
                title = "Notas",
            )
        )

        data = trace
        fig = Figure(data=data, layout=layout)
        iplot(fig, filename='scatter-plot')

    def graph_04(self):
        df = self._df_sum.sort_values(by="Grade")
        Clusters = df.Cluster.unique()        
        color = ["rgb(255,0,0)","rgb(0,0,255)","rgb(127,0,127)","rgb(0,255,0)"]        
        color[Clusters[0]] = "rgb(255,0,0)"
        color[Clusters[1]] = "rgb(127,0,127)"
        color[Clusters[2]] = "rgb(0,0,255)"        
        color[Clusters[3]] = "rgb(0,255,0)"

        trace = []
        for i in range(0, self.NUMBER_STUDENTS):
            trace.append(
                Scatter(
                    x=[self._df_sum.AssignTotal[i]], #AssignAnswered
                    y=[self.DATASET.Grade[i]], #Grade
                    mode='markers',
                    name=self.DATASET.Students[i], #each student name                    
                    text = [str(self.DATASET.Students[i])],                    
                    marker=dict(
                        size=12,
                        symbol=self._df_sum.Cluster[i],
                        color = color[self._df_sum.Cluster[i]],
                        colorscale='Viridis',
                        line=dict(
                            width=2
                        )
                    )
                )
            )

        layout = Layout(
            title='Notas dos estudantes vs atividades respondidas',
            hovermode = "closest",
            showlegend = True,
            xaxis = dict(
                autorange = False,
                fixedrange = False,
                range = [0, self._df_sum.AssignTotal.max()+10],
                rangemode = "normal",
                zeroline= False,
                showline = True,
                title = "Atividades respondidas",                
            ),
            yaxis = dict(
                autorange = False,
                fixedrange = False,
                range = [0, self.DATASET.Grade.max()+10],
                rangemode = "normal",
                showline = True,
                title = "Notas",
            )
        )

        data = trace
        fig = Figure(data=data, layout=layout)
        iplot(fig, filename='scatter-plot')

    def graph_05(self):
        df = self._df_sum.sort_values(by="Grade")
        Clusters = df.Cluster.unique()        
        color = ["rgb(255,0,0)","rgb(0,0,255)","rgb(127,0,127)","rgb(0,255,0)"]        
        color[Clusters[0]] = "rgb(255,0,0)"
        color[Clusters[1]] = "rgb(127,0,127)"
        color[Clusters[2]] = "rgb(0,0,255)"        
        color[Clusters[3]] = "rgb(0,255,0)"

        trace = []
        for i in range(0, self.NUMBER_STUDENTS):
            trace.append(
                Scatter(
                    x=[self.DATASET["Forum Access"][i]], #Acesso ao fórum
                    y=[self.DATASET.Grade[i]], #Grade
                    mode='markers',
                    name=self.DATASET.Students[i], #each student name                    
                    text = [str(self.DATASET.Students[i])],                    
                    marker=dict(
                        size=12,
                        symbol=self._df_sum.Cluster[i],
                        color = color[self._df_sum.Cluster[i]],
                        colorscale='Viridis',
                        line=dict(
                            width=2
                        )
                    )
                )
            )

        layout = Layout(
            title='Notas dos estudantes vs acesso ao fórum',
            hovermode = "closest",
            showlegend = True,
            xaxis = dict(
                autorange = False,
                fixedrange = False,
                range = [0, self.DATASET["Forum Access"].max()+10],
                rangemode = "normal",
                zeroline= False,
                showline = True,
                title = "Acesso ao fórum",
            ),
            yaxis = dict(
                autorange = False,
                fixedrange = False,
                range = [0, self.DATASET.Grade.max()+10],
                rangemode = "normal",
                showline = True,
                title = "Notas",
            )
        )

        data = trace
        fig = Figure(data=data, layout=layout)
        iplot(fig, filename='scatter-plot')

    def graph_06(self):
        df = self._df_sum.sort_values(by="Grade")
        Clusters = df.Cluster.unique()        
        color = ["rgb(255,0,0)","rgb(0,0,255)","rgb(127,0,127)","rgb(0,255,0)"]        
        color[Clusters[0]] = "rgb(255,0,0)"
        color[Clusters[1]] = "rgb(127,0,127)"
        color[Clusters[2]] = "rgb(0,0,255)"        
        color[Clusters[3]] = "rgb(0,255,0)"

        trace = []
        for i in range(0, self.NUMBER_STUDENTS):
            trace.append(
                Scatter(
                    x=[self.DATASET["Forum Post"][i]], #Postagem no fórum
                    y=[self.DATASET.Grade[i]], #Grade
                    mode='markers',
                    name=self.DATASET.Students[i], #each student name                    
                    text = [str(self.DATASET.Students[i])],                    
                    marker=dict(
                        size=12,
                        symbol=self._df_sum.Cluster[i],
                        color = color[self._df_sum.Cluster[i]],
                        colorscale='Viridis',
                        line=dict(
                            width=2
                        )
                    )
                )
            )

        layout = Layout(
            title='Notas dos estudantes vs postagens no fórum',
            hovermode = "closest",
            showlegend = True,
            xaxis = dict(
                autorange = False,
                fixedrange = False,
                range = [0, self.DATASET["Forum Post"].max()+10],
                rangemode = "normal",
                zeroline= False,
                showline = True,
                title = "Postagem no fórum",
            ),
            yaxis = dict(
                autorange = False,
                fixedrange = False,
                range = [0, self.DATASET.Grade.max()+10],
                rangemode = "normal",
                showline = True,
                title = "Notas",
            )
        )

        data = trace
        fig = Figure(data=data, layout=layout)
        iplot(fig, filename='scatter-plot')

    def graph_07(self):
        df = self._df_sum.sort_values(by="Grade")
        Clusters = df.Cluster.unique()        
        color = ["rgb(255,0,0)","rgb(0,0,255)","rgb(127,0,127)","rgb(0,255,0)"]        
        color[Clusters[0]] = "rgb(255,0,0)"
        color[Clusters[1]] = "rgb(127,0,127)"
        color[Clusters[2]] = "rgb(0,0,255)"        
        color[Clusters[3]] = "rgb(0,255,0)"

        trace = []
        for i in range(0, self.NUMBER_STUDENTS):
            trace.append(
                Scatter(
                    x=[self.DATASET["Forum Replies"][i]], #Replies
                    y=[self.DATASET.Grade[i]], #Grade
                    mode='markers',
                    name=self.DATASET.Students[i], #each student name                    
                    text = [str(self.DATASET.Students[i])],                    
                    marker=dict(
                        size=12,
                        symbol=self._df_sum.Cluster[i],
                        color = color[self._df_sum.Cluster[i]],
                        colorscale='Viridis',
                        line=dict(
                            width=2
                        )
                    )
                )
            )

        layout = Layout(
            title='Notas dos estudantes vs postagens respondidas no fórum',
            hovermode = "closest",
            showlegend = True,
            xaxis = dict(
                autorange = False,
                fixedrange = False,
                range = [0, self.DATASET["Forum Replies"].max()+10],
                rangemode = "normal",
                zeroline= False,
                showline = True,
                title = "Postagens respondidas no fórum",
            ),
            yaxis = dict(
                autorange = False,
                fixedrange = False,
                range = [0, self.DATASET.Grade.max()+10],
                rangemode = "normal",
                showline = True,
                title = "Notas",
            )
        )

        data = trace
        fig = Figure(data=data, layout=layout)
        iplot(fig, filename='scatter-plot')

    def graph_08(self):
        df = self._df_sum.sort_values(by="Grade")
        Clusters = df.Cluster.unique()        
        color = ["rgb(255,0,0)","rgb(0,0,255)","rgb(127,0,127)","rgb(0,255,0)"]
        color[Clusters[0]] = "rgb(255,0,0)"
        color[Clusters[1]] = "rgb(127,0,127)"
        color[Clusters[2]] = "rgb(0,0,255)"        
        color[Clusters[3]] = "rgb(0,255,0)"
        
        trace = []
        for i in range(0, self.NUMBER_STUDENTS):
            trace.append(
                Scatter(
                    x=[self.DATASET["Forum Add Thread"][i]], #Init threads in forum
                    y=[self.DATASET.Grade[i]], #Grade
                    mode='markers',
                    name=self.DATASET.Students[i], #each student name                    
                    text = [str(self.DATASET.Students[i])],                    
                    marker=dict(
                        size=12,
                        symbol=self._df_sum.Cluster[i],
                        color = color[self._df_sum.Cluster[i]],
                        colorscale='Viridis',
                        line=dict(
                            width=2
                        )
                    )
                )
            )

        layout = Layout(
            title='Notas dos estudantes vs threads iniciadas no fórum',
            hovermode = "closest",
            showlegend = True,
            xaxis = dict(
                autorange = False,
                fixedrange = False,
                range = [0, self.DATASET["Forum Add Thread"].max()+10],
                rangemode = "normal",
                zeroline= False,
                showline = True,
                title = "Threads iniciadas no fórum",
            ),
            yaxis = dict(
                autorange = False,
                fixedrange = False,
                range = [0, self.DATASET.Grade.max()+10],
                rangemode = "normal",
                showline = True,
                title = "Notas",
            )
        )

        data = trace
        fig = Figure(data=data, layout=layout)
        iplot(fig, filename='scatter-plot')

    def graph_09(self):        
        df = self._df_sum.sort_values(by="Grade")
        Clusters = df.Cluster.unique()
        color = ["rgb(255,0,0)","rgb(127,0,127)","rgb(0,0,255)","rgb(0,255,0)"]        
        # print(Clusters)
        trace = []
        for i in range(0,len(Clusters)):
            trace.append(
                Box(
                    y=df.Grade.loc[df['Cluster']==Clusters[i]].values.tolist(), #Access
                    name="Cluster "+str(i+1),
                    text=df["Students"].loc[df['Cluster']==Clusters[i]].values.tolist(),
                    boxpoints = 'all',
                    marker=dict(
                        color = color[i],
                        line=dict(
                            width=1
                        )                        
                    ),
                    boxmean=True
                )
            )

        layout = Layout(
            title='Variação de notas por cluster',
            # hovermode = "closest",
            showlegend = True,
            yaxis = dict(
                fixedrange = False,
                range = [-1, self.DATASET.Grade.max()+10],
                rangemode = "normal",
                # showline = True,
                title = "Notas",
                zeroline = False,
            )
        )

        data = trace
        fig = Figure(data=data, layout=layout)
        iplot(fig, filename='box-plot')

    def graph_10(self):        
        df = self._df_sum.sort_values(by="Grade")
        Clusters = df.Cluster.unique()
        color = ["rgb(255,0,0)","rgb(127,0,127)","rgb(0,0,255)","rgb(0,255,0)"]        
        # print(Clusters)
        trace = []
        for i in range(0,len(Clusters)):
            trace.append(
                Box(
                    y=df.Access.loc[df['Cluster']==Clusters[i]].values.tolist(), #Access
                    name="Cluster "+str(i+1),
                    text=df["Students"].loc[df['Cluster']==Clusters[i]].values.tolist(),
                    boxpoints = 'all',
                    marker=dict(
                        color = color[i],
                        line=dict(
                            width=1
                        )                        
                    ),
                    boxmean=True
                )
            )

        layout = Layout(
            title='Variação de acessos por cluster',
            # hovermode = "closest",
            showlegend = True,
            yaxis = dict(
                fixedrange = False,
                range = [-1, self.DATASET.Access.max()+10],
                rangemode = "normal",
                # showline = True,
                title = "Acessos",
                zeroline = False,
            )
        )

        data = trace
        fig = Figure(data=data, layout=layout)
        iplot(fig, filename='box-plot')

    def graph_11(self):        
        df = self._df_sum.sort_values(by="Grade")
        Clusters = df.Cluster.unique()
        color = ["rgb(255,0,0)","rgb(127,0,127)","rgb(0,0,255)","rgb(0,255,0)"]        
        # print(Clusters)
        trace = []
        for i in range(0,len(Clusters)):
            trace.append(
                Box(
                    y=df.AssignTotal.loc[df['Cluster']==Clusters[i]].values.tolist(),
                    name="Cluster "+str(i+1),
                    text=df["Students"].loc[df['Cluster']==Clusters[i]].values.tolist(),
                    boxpoints = 'all',
                    marker=dict(
                        color = color[i],
                        line=dict(
                            width=1
                        )                        
                    ),
                    boxmean=True
                )
            )

        layout = Layout(
            title='Variação de atividades respondidas por cluster',
            # hovermode = "closest",
            showlegend = True,
            yaxis = dict(
                fixedrange = False,
                range = [-1, df.AssignTotal.max()+10],
                rangemode = "normal",
                # showline = True,
                title = "Atividades respondidas",
                zeroline = False,
            )
        )

        data = trace
        fig = Figure(data=data, layout=layout)
        iplot(fig, filename='box-plot')

    def graph_12(self):        
        df = self._df_sum.sort_values(by="Grade")
        Clusters = df.Cluster.unique()
        color = ["rgb(255,0,0)","rgb(127,0,127)","rgb(0,0,255)","rgb(0,255,0)"]        
        # print(Clusters)
        trace = []
        for i in range(0,len(Clusters)):
            trace.append(
                Box(
                    y=df["Forum Access"].loc[df['Cluster']==Clusters[i]].values.tolist(),
                    name="Cluster "+str(i+1),
                    text=df["Students"].loc[df['Cluster']==Clusters[i]].values.tolist(),
                    boxpoints = 'all',
                    marker=dict(
                        color = color[i],
                        line=dict(
                            width=1
                        )                        
                    ),
                    boxmean=True
                )
            )

        layout = Layout(
            title='Variação de acesso ao fórum por cluster',
            # hovermode = "closest",
            showlegend = True,
            yaxis = dict(
                fixedrange = False,
                range = [-1, self.DATASET["Forum Access"].max()+10],
                rangemode = "normal",
                # showline = True,
                title = "Acesso ao fórum",
                zeroline = False,
            )
        )

        data = trace
        fig = Figure(data=data, layout=layout)
        iplot(fig, filename='box-plot')

    def graph_13(self):
        df = self._df_sum.sort_values(by="Grade")
        Clusters = df.Cluster.unique()
        color = ["rgb(255,0,0)","rgb(127,0,127)","rgb(0,0,255)","rgb(0,255,0)"]        
        # print(Clusters)
        trace = []
        for i in range(0,len(Clusters)):
            trace.append(
                Box(
                    y=df["Forum Post"].loc[df['Cluster']==Clusters[i]].values.tolist(),
                    name="Cluster "+str(i+1),
                    text=df["Students"].loc[df['Cluster']==Clusters[i]].values.tolist(),
                    boxpoints = 'all',
                    marker=dict(
                        color = color[i],
                        line=dict(
                            width=1
                        )                        
                    ),
                    boxmean=True
                )
            )

        layout = Layout(
            title='Variação de postagem no fórum por cluster',
            # hovermode = "closest",
            showlegend = True,
            yaxis = dict(
                fixedrange = False,
                range = [-1, self.DATASET["Forum Post"].max()+10],
                rangemode = "normal",
                # showline = True,
                title = "Postagem no fórum",
                zeroline = False,
            )
        )

        data = trace
        fig = Figure(data=data, layout=layout)
        iplot(fig, filename='box-plot')

    def graph_14(self):
        df = self._df_sum.sort_values(by="Grade")
        Clusters = df.Cluster.unique()
        color = ["rgb(255,0,0)","rgb(127,0,127)","rgb(0,0,255)","rgb(0,255,0)"]        
        # print(Clusters)
        trace = []
        for i in range(0,len(Clusters)):
            trace.append(
                Box(
                    y=df["Forum Replies"].loc[df['Cluster']==Clusters[i]].values.tolist(),
                    name="Cluster "+str(i+1),
                    text=df["Students"].loc[df['Cluster']==Clusters[i]].values.tolist(),
                    boxpoints = 'all',
                    marker=dict(
                        color = color[i],
                        line=dict(
                            width=1
                        )                        
                    ),
                    boxmean=True
                )
            )

        layout = Layout(
            title='Variação de postagem respondidas no fórum por cluster',
            # hovermode = "closest",
            showlegend = True,
            yaxis = dict(
                fixedrange = False,
                range = [-1, self.DATASET["Forum Replies"].max()+10],
                rangemode = "normal",
                # showline = True,
                title = "Postagens respondidas no fórum",
                zeroline = False,
            )
        )

        data = trace
        fig = Figure(data=data, layout=layout)
        iplot(fig, filename='box-plot')

    def graph_15(self):
        df = self._df_sum.sort_values(by="Grade")
        Clusters = df.Cluster.unique()
        color = ["rgb(255,0,0)","rgb(127,0,127)","rgb(0,0,255)","rgb(0,255,0)"]        
        # print(Clusters)
        trace = []
        for i in range(0,len(Clusters)):
            trace.append(
                Box(
                    y=df["Forum Add Thread"].loc[df['Cluster']==Clusters[i]].values.tolist(),
                    name="Cluster "+str(i+1),
                    text=df["Students"].loc[df['Cluster']==Clusters[i]].values.tolist(),
                    boxpoints = 'all',
                    marker=dict(
                        color = color[i],                        
                        line=dict(
                            width=1
                        )                        
                    ),
                    boxmean=True
                )
            )

        layout = Layout(
            title='Variação de threads iniciadas no fórum por cluster',
            # hovermode = "closest",
            showlegend = True,
            yaxis = dict(
                fixedrange = False,
                range = [-1, self.DATASET["Forum Add Thread"].max()+10],
                rangemode = "normal",
                # showline = True,
                title = "Threads iniciadas no fórum",
                zeroline = False,
            )
        )

        data = trace
        fig = Figure(data=data, layout=layout)
        iplot(fig, filename='box-plot')

    def graph_16(self):
        # https://plot.ly/python/violin/#reference
        # https://plot.ly/python/reference/#violin
        df = self._df_sum.sort_values(by="Grade")
        Clusters = df.Cluster.unique()
        color = ["rgb(255,0,0)","rgb(127,0,127)","rgb(0,0,255)","rgb(0,255,0)"]        
        # print(Clusters)
        data = []
        for i in range(0,len(Clusters)):
            trace = {
                "type":'violin',
                "x":["Cluster "+str(i+1)],
                "y":df["Grade"].loc[df['Cluster']==Clusters[i]].values.tolist(),
                "name":"Cluster "+str(i+1),
                "box":{
                    "visible":True
                    },
                "meanline":{
                    "visible":True
                    }                
            }

        layout = Layout(
            title='Variação de notas por cluster',
            # hovermode = "closest",
            showlegend = True,
            yaxis = dict(
                fixedrange = False,
                range = [-1, self.DATASET["Forum Add Thread"].max()+10],
                rangemode = "normal",
                # showline = True,
                title = "Threads iniciadas no fórum",
                zeroline = False,
            )
        )

        data.append(trace)
        fig = Figure(data=data, layout=layout)
        iplot(fig, filename='box-plot')

    def print_all_graphs(self):
        self.graph_01() #Table raw
        self.graph_02() #Scatter
        self.graph_03()
        self.graph_04()
        self.graph_05()
        self.graph_06()
        self.graph_07()
        self.graph_08()
        self.graph_09() #Box
        self.graph_10()
        self.graph_11()
        self.graph_12()
        self.graph_13()
        self.graph_14()
        self.graph_15()
        self.graph_16() #Violin

instance = V005(60)
instance.print_all_graphs()

# *[MP-017] Students can be clustered into different groups based on their access or interaction patterns.
# *[MP-020] Students with a satisfatory performance ignore part of the materials in distance courses.
# *[MP-028] Student groups that use more forums tend to have a good performance.
# [MP-030] Students groups that do more replies in forums tend to have a good performance.
# [MP-031] Students groups that init threads in forums tend to have a good performance.
# [MP-035] Successful students are more frequently and regularly participating and engaged in online activities.
# [MP-106] Student groups that have more posts are more likely to complete the course.
# *[RQ-02] Identify student access patterns (e.g., login, materials).
# *[RQ-03] Identify student performance patterns.
# [RQ-04] Identify student interest patterns on the course.
# *[RQ-05] Identify student usage patterns on the forum.
# *[RQ-07] Identify student interaction patterns (e.g., materials).
# [RQ-08] Identify student participation patterns on the course.
# [RQ-09] Identify student drop out patterns.
# [RQ-14] Identify pace learning student.
# [RQ-17] Relate both students' navigation and performance.
# [RQ-18] Relate video length and student performance.
# [RQ-21] Relate video script and student performance.
