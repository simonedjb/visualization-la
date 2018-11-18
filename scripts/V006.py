import pandas as pd
import numpy as np

from plotly.graph_objs import Figure, Layout, Bar, Table, Heatmap, Scatter, Box, Violin
from plotly.offline import init_notebook_mode, iplot

from sklearn import metrics
from sklearn.cluster import KMeans


init_notebook_mode(connected=True) # initiate notebook for offline plot

class V006:
    NUMBER_STUDENTS = 50
    DATASET = pd.DataFrame()

    _language = "pt"
    # _df_sum = pd.DataFrame()

    def __init__(self, number_students = 20, language = "pt"):
        self.NUMBER_STUDENTS = number_students
        self._language = language
        self.generate_dataset()

    def generate_dataset(self):
        names = pd.read_csv("names.csv")
        self.DATASET = pd.DataFrame(columns=["Students","Age","Forum Access","Forum Post","Forum Replies","Forum Add Thread","Cluster"])

        self.DATASET.Age = np.random.triangular(18,30,70,self.NUMBER_STUDENTS)
        self.DATASET["Age"] = self.DATASET.apply(self.convert_to_int, axis=1)

        rand_names = [names.group_name[np.random.randint(0,len(names.group_name)+1)] for n in range(0,self.NUMBER_STUDENTS)]
        rand_names.sort()

        for i in range(0,self.NUMBER_STUDENTS):
            self.DATASET.loc[i,"Students"] = rand_names[i]

            if (self.DATASET.loc[i,"Age"] <= 25):
                self.DATASET.loc[i,"Forum Post"] = np.random.randint(0,4)
                self.DATASET.loc[i,"Forum Replies"] = np.random.randint(0,4)
                self.DATASET.loc[i,"Forum Add Thread"] = np.random.randint(0,4)

                self.DATASET.loc[i,"Forum Access"] =  self.DATASET.loc[i,"Forum Post"] + self.DATASET.loc[i,"Forum Replies"] + self.DATASET.loc[i,"Forum Add Thread"] + np.random.randint(0,7)
                self.DATASET.loc[i,"Cluster"] = 1

            elif (self.DATASET.loc[i,"Age"] <= 30):
                self.DATASET.loc[i,"Forum Post"] = np.random.randint(0,8)
                self.DATASET.loc[i,"Forum Replies"] = np.random.randint(0,8)
                self.DATASET.loc[i,"Forum Add Thread"] = np.random.randint(0,4)

                self.DATASET.loc[i,"Forum Access"] = self.DATASET.loc[i,"Forum Post"] + self.DATASET.loc[i,"Forum Replies"] + self.DATASET.loc[i,"Forum Add Thread"] + np.random.randint(0,22)
                self.DATASET.loc[i,"Cluster"] = 2

            elif (self.DATASET.loc[i,"Age"] <= 40):
                self.DATASET.loc[i,"Forum Post"] = np.random.randint(1,12)
                self.DATASET.loc[i,"Forum Replies"] = np.random.randint(0,12)
                self.DATASET.loc[i,"Forum Add Thread"] = np.random.randint(0,8)

                self.DATASET.loc[i,"Forum Access"] =  self.DATASET.loc[i,"Forum Post"] + self.DATASET.loc[i,"Forum Replies"] + self.DATASET.loc[i,"Forum Add Thread"] + np.random.randint(2,26)
                self.DATASET.loc[i,"Cluster"] = 3

            elif (self.DATASET.loc[i,"Age"] <= 50):
                self.DATASET.loc[i,"Forum Post"] = np.random.randint(2,21)
                self.DATASET.loc[i,"Forum Replies"] = np.random.randint(2,21)
                self.DATASET.loc[i,"Forum Add Thread"] = np.random.randint(0,7)

                self.DATASET.loc[i,"Forum Access"] =  self.DATASET.loc[i,"Forum Post"] + self.DATASET.loc[i,"Forum Replies"] + self.DATASET.loc[i,"Forum Add Thread"] + np.random.randint(4,31)
                self.DATASET.loc[i,"Cluster"] = 4

            elif (self.DATASET.loc[i,"Age"] <= 60):
                self.DATASET.loc[i,"Forum Post"] = np.random.randint(5,36)
                self.DATASET.loc[i,"Forum Replies"] = np.random.randint(5,36)
                self.DATASET.loc[i,"Forum Add Thread"] = np.random.randint(1,11)

                self.DATASET.loc[i,"Forum Access"] =  self.DATASET.loc[i,"Forum Post"] + self.DATASET.loc[i,"Forum Replies"] + self.DATASET.loc[i,"Forum Add Thread"] + np.random.randint(6,36)
                self.DATASET.loc[i,"Cluster"] = 5

            else:
                self.DATASET.loc[i,"Forum Post"] = np.random.randint(10,41)
                self.DATASET.loc[i,"Forum Replies"] = np.random.randint(10,41)
                self.DATASET.loc[i,"Forum Add Thread"] = np.random.randint(3,14)

                self.DATASET.loc[i,"Forum Access"] =  self.DATASET.loc[i,"Forum Post"] + self.DATASET.loc[i,"Forum Replies"] + self.DATASET.loc[i,"Forum Add Thread"] + np.random.randint(10,41)
                self.DATASET.loc[i,"Cluster"] = 6
        
        # df_k = self.DATASET.iloc[:,1:] #Selecting features to cluster
        # kmeans = KMeans(n_clusters=5, init='random').fit(df_k) #Clustering
        # self._df_sum["Cluster"] = np.asarray(kmeans.labels_)
        # self._df_sum["Students"] = self.DATASET["Students"]
        # self._df_sum["Age"] = self.DATASET["Age"]
        # self._df_sum["Forum Access"] = self.DATASET["Forum Access"]
        # self._df_sum["Forum Post"] = self.DATASET["Forum Post"]
        # self._df_sum["Forum Replies"] = self.DATASET["Forum Replies"]
        # self._df_sum["Forum Add Thread"] = self.DATASET["Forum Add Thread"]

    def convert_to_int(self,row):
        return int(row["Age"])

    # Table presenting raw data
    def graph_01(self):
        df = self.DATASET

        trace = Table(
            header=dict(
                values=list(df.columns[:len(df.columns)-1]),
                fill = dict(color='#C2D4FF'),
                align = 'center'
            ),
            cells=dict(
                values=[df[i].tolist() for i in df.columns[:len(df.columns)-1]],
                fill = dict(color='#F5F8FF'),
                align = ['left','center']
            )
        )

        data = [trace]
        iplot(data, filename = 'pandas_table')

    # Scatter
    def graph_02(self):
        legend = {"title":"Relação entre a idade dos estudantes e seus acessos no fórum",
                    "xaxis":"Acessos no fórum",
                    "yaxis":"Idade",
                }
        if (self._language == "en"):
            legend = {"title":"Relation between either students' age and their access in the forum",
                        "xaxis":"Access in the forum",
                        "yaxis":"Age",
                    }        
        color = ["rgb(127,0,0)","rgb(255,0,0)","rgb(127,0,127)","rgb(0,0,255)","rgb(0,127,127)","rgb(0,255,0)"]
        trace = []
        for i in range(0, self.NUMBER_STUDENTS):
            trace.append(
                Scatter(
                    x=[self.DATASET["Forum Access"][i]], #Acesso ao fórum
                    y=[self.DATASET.Age[i]], #Age
                    mode='markers',
                    name=self.DATASET.Students[i], #each student name
                    text = [str(self.DATASET.Students[i])],
                    marker=dict(
                        size=12,
                        symbol=self.DATASET.Cluster[i]-1,
                        color = color[self.DATASET.Cluster[i]-1],
                        line=dict(
                            width=2
                        )
                    )
                )
            )

        layout = Layout(
            title=legend['title'],
            hovermode = "closest",
            showlegend = True,
            xaxis = dict(
                title = legend["xaxis"],
                titlefont=dict(
                    # family='Arial, sans-serif',
                    # size=18,
                    color='rgb(180,180,180)',
                ),
                autorange = False,
                fixedrange = False,
                range = [0, self.DATASET["Forum Access"].max()+10],
                rangemode = "normal",
                zeroline= False,
                showline = True,
            ),
            yaxis = dict(
                title = legend["yaxis"],
                titlefont=dict(
                    # family='Arial, sans-serif',
                    # size=18,
                    color='rgb(180,180,180)',
                ),
                autorange = False,
                fixedrange = False,
                range = [0, self.DATASET.Age.max()+10],
                rangemode = "normal",
                showline = True,                
            )
        )

        data = trace
        fig = Figure(data=data, layout=layout)
        iplot(fig, filename='scatter-plot')

    def graph_03(self):
        legend = {"title":"Relação entre a idade dos estudantes e suas postagens no fórum",
                    "xaxis":"Postagens no fórum",
                    "yaxis":"Idade",
                }
        if (self._language == "en"):
            legend = {"title":"Relation between either students' age and their posts in the forum",
                        "xaxis":"Posts in the forum",
                        "yaxis":"Age",
                    }
        color = ["rgb(127,0,0)","rgb(255,0,0)","rgb(127,0,127)","rgb(0,0,255)","rgb(0,127,127)","rgb(0,255,0)"]
        trace = []
        for i in range(0, self.NUMBER_STUDENTS):
            trace.append(
                Scatter(
                    x=[self.DATASET["Forum Post"][i]], #Posts
                    y=[self.DATASET.Age[i]], #Age
                    mode='markers',
                    name=self.DATASET.Students[i], #each student name                    
                    text = [str(self.DATASET.Students[i])],                    
                    marker=dict(
                        size=12,                        
                        symbol=self.DATASET.Cluster[i]-1,
                        color = color[self.DATASET.Cluster[i]-1],
                        line=dict(
                            width=2
                        )
                    )
                )
            )

        layout = Layout(
            title=legend['title'],
            hovermode = "closest",
            showlegend = True,
            xaxis = dict(
                title = legend["xaxis"],
                titlefont=dict(
                    # family='Arial, sans-serif',
                    # size=18,
                    color='rgb(180,180,180)',
                ),
                autorange = False,
                fixedrange = False,
                range = [0, self.DATASET["Forum Post"].max()+10],
                rangemode = "normal",
                zeroline= False,
                showline = True,                
            ),
            yaxis = dict(
                title = legend["yaxis"],
                titlefont=dict(
                    # family='Arial, sans-serif',
                    # size=18,
                    color='rgb(180,180,180)',
                ),
                autorange = False,
                fixedrange = False,
                range = [0, self.DATASET.Age.max()+10],
                rangemode = "normal",
                showline = True,                
            )
        )

        data = trace
        fig = Figure(data=data, layout=layout)
        iplot(fig, filename='scatter-plot')

    def graph_04(self):
        legend = {"title":"Relação entre a idade dos estudantes e suas réplicas no fórum",
                    "xaxis":"Réplicas no fórum",
                    "yaxis":"Idade",
                }
        if (self._language == "en"):
            legend = {"title":"Relation between either students' age and their replies in the forum",
                        "xaxis":"Replies in the forum",
                        "yaxis":"Age",
                    }
        color = ["rgb(127,0,0)","rgb(255,0,0)","rgb(127,0,127)","rgb(0,0,255)","rgb(0,127,127)","rgb(0,255,0)"]
        trace = []
        for i in range(0, self.NUMBER_STUDENTS):
            trace.append(
                Scatter(
                    x=[self.DATASET["Forum Replies"][i]], #Replies
                    y=[self.DATASET.Age[i]], #Age
                    mode='markers',
                    name=self.DATASET.Students[i], #each student name                    
                    text = [str(self.DATASET.Students[i])],                    
                    marker=dict(
                        size=12,                        
                        symbol=self.DATASET.Cluster[i]-1,
                        color = color[self.DATASET.Cluster[i]-1],
                        line=dict(
                            width=2
                        )
                    )
                )
            )

        layout = Layout(
            title=legend['title'],
            hovermode = "closest",
            showlegend = True,
            xaxis = dict(
                title = legend["xaxis"],
                titlefont=dict(
                    # family='Arial, sans-serif',
                    # size=18,
                    color='rgb(180,180,180)',
                ),
                autorange = False,
                fixedrange = False,
                range = [0, self.DATASET["Forum Replies"].max()+10],
                rangemode = "normal",
                zeroline= False,
                showline = True,                
            ),
            yaxis = dict(
                title = legend["yaxis"],
                titlefont=dict(
                    # family='Arial, sans-serif',
                    # size=18,
                    color='rgb(180,180,180)',
                ),
                autorange = False,
                fixedrange = False,
                range = [0, self.DATASET.Age.max()+10],
                rangemode = "normal",
                showline = True,                
            )
        )

        data = trace
        fig = Figure(data=data, layout=layout)
        iplot(fig, filename='scatter-plot')

    def graph_05(self):
        legend = {"title":"Relação entre a idade dos estudantes e seus tópicos adicionados no fórum",
                    "xaxis":"Tópicos no fórum",
                    "yaxis":"Idade",
                }
        if (self._language == "en"):
            legend = {"title":"Relation between either students' age and their threads added in the forum",
                        "xaxis":"Threads in the forum",
                        "yaxis":"Age",
                    }
        color = ["rgb(127,0,0)","rgb(255,0,0)","rgb(127,0,127)","rgb(0,0,255)","rgb(0,127,127)","rgb(0,255,0)"]
        trace = []
        for i in range(0, self.NUMBER_STUDENTS):
            trace.append(
                Scatter(
                    x=[self.DATASET["Forum Add Thread"][i]], #Init threads in forum
                    y=[self.DATASET.Age[i]], #Age
                    mode='markers',
                    name=self.DATASET.Students[i], #each student name                    
                    text = [str(self.DATASET.Students[i])],                    
                    marker=dict(
                        size=12,                        
                        symbol=self.DATASET.Cluster[i]-1,
                        color = color[self.DATASET.Cluster[i]-1],
                        line=dict(
                            width=2
                        )
                    )
                )
            )

        layout = Layout(
            title=legend['title'],
            hovermode = "closest",
            showlegend = True,
            xaxis = dict(
                title = legend["xaxis"],
                titlefont=dict(
                    # family='Arial, sans-serif',
                    # size=18,
                    color='rgb(180,180,180)',
                ),
                autorange = False,
                fixedrange = False,
                range = [0, self.DATASET["Forum Add Thread"].max()+10],
                rangemode = "normal",
                zeroline= False,
                showline = True,                
            ),
            yaxis = dict(
                title = legend["yaxis"],
                titlefont=dict(
                    # family='Arial, sans-serif',
                    # size=18,
                    color='rgb(180,180,180)',
                ),
                autorange = False,
                fixedrange = False,
                range = [0, self.DATASET.Age.max()+10],
                rangemode = "normal",
                showline = True,                
            )
        )

        data = trace
        fig = Figure(data=data, layout=layout)
        iplot(fig, filename='scatter-plot')

    #Box
    def graph_06(self):
        legend = {"title":"Variação de acessos no fórum por idade",
                    "xaxis":"",
                    "yaxis":"Acessos no fórum",
                    "age":{1:"até 25 anos", 2:"26 à 30 anos", 3:"31 à 40 anos", 4: "41 à 50 anos", 5: "51 à 60 anos", 6: "mais de 60 anos"},
                }
        if (self._language == "en"):
            legend = {"title":"Variation of students' access in the forum by age",
                        "xaxis":"",
                        "yaxis":"Access in the forum",
                        "age":{1:"until 25 years", 2:"26 to 30 years", 3:"31 to 40 years", 4: "41 to 50 years", 5: "51 to 60 years", 6: "over 60 years"},
                    }
        df = self.DATASET.sort_values(by="Age")
        Clusters = df.Cluster.unique()
        color = ["rgb(127,0,0)","rgb(255,0,0)","rgb(127,0,127)","rgb(0,0,255)","rgb(0,127,127)","rgb(0,255,0)"]        
        # print(Clusters)
        trace = []
        for i in range(0,len(Clusters)):
            trace.append(
                Box(
                    y=df["Forum Access"].loc[df['Cluster']==Clusters[i]].values.tolist(),
                    name=legend['age'][i+1],
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
            title=legend['title'],
            # hovermode = "closest",
            showlegend = True,
            xaxis = dict(
                title = legend["xaxis"],
                titlefont=dict(
                    # family='Arial, sans-serif',
                    # size=18,
                    color='rgb(180,180,180)',
                ),
            ),
            yaxis = dict(
                title = legend["yaxis"],
                titlefont=dict(
                    # family='Arial, sans-serif',
                    # size=18,
                    color='rgb(180,180,180)',
                ),
                fixedrange = False,
                range = [-1, self.DATASET["Forum Access"].max()+10],
                rangemode = "normal",
                # showline = True,
                zeroline = False,
            )
        )

        data = trace
        fig = Figure(data=data, layout=layout)
        iplot(fig, filename='box-plot')

    def graph_07(self):
        legend = {"title":"Variação de postagens no fórum por idade",
                    "xaxis":"",
                    "yaxis":"Postagens no fórum",
                    "age":{1:"até 25 anos", 2:"26 à 30 anos", 3:"31 à 40 anos", 4: "41 à 50 anos", 5: "51 à 60 anos", 6: "mais de 60 anos"},
                }
        if (self._language == "en"):
            legend = {"title":"Variation of students' posts in the forum by age",
                        "xaxis":"",
                        "yaxis":"Posts in the forum",
                        "age":{1:"until 25 years", 2:"26 to 30 years", 3:"31 to 40 years", 4: "41 to 50 years", 5: "51 to 60 years", 6: "over 60 years"},
                    }
        df = self.DATASET.sort_values(by="Age")
        Clusters = df.Cluster.unique()
        color = ["rgb(127,0,0)","rgb(255,0,0)","rgb(127,0,127)","rgb(0,0,255)","rgb(0,127,127)","rgb(0,255,0)"]        
        # print(Clusters)
        trace = []
        for i in range(0,len(Clusters)):
            trace.append(
                Box(
                    y=df["Forum Post"].loc[df['Cluster']==Clusters[i]].values.tolist(),
                    name=legend['age'][i+1],
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
            title=legend['title'],
            # hovermode = "closest",
            showlegend = True,
            xaxis = dict(
                title = legend["xaxis"],
                titlefont=dict(
                    # family='Arial, sans-serif',
                    # size=18,
                    color='rgb(180,180,180)',
                ),
            ),
            yaxis = dict(
                title = legend["yaxis"],
                titlefont=dict(
                    # family='Arial, sans-serif',
                    # size=18,
                    color='rgb(180,180,180)',
                ),
                fixedrange = False,
                range = [-1, self.DATASET["Forum Post"].max()+10],
                rangemode = "normal",
                # showline = True,
                zeroline = False,
            )
        )

        data = trace
        fig = Figure(data=data, layout=layout)
        iplot(fig, filename='box-plot')

    def graph_08(self):
        legend = {"title":"Variação de réplicas no fórum por idade",
                    "xaxis":"",
                    "yaxis":"Réplicas no fórum",
                    "age":{1:"até 25 anos", 2:"26 à 30 anos", 3:"31 à 40 anos", 4: "41 à 50 anos", 5: "51 à 60 anos", 6: "mais de 60 anos"},
                }
        if (self._language == "en"):
            legend = {"title":"Variation of students' replies in the forum by age",
                        "xaxis":"",
                        "yaxis":"Replies in the forum",
                        "age":{1:"until 25 years", 2:"26 to 30 years", 3:"31 to 40 years", 4: "41 to 50 years", 5: "51 to 60 years", 6: "over 60 years"},
                    }
        df = self.DATASET.sort_values(by="Age")
        Clusters = df.Cluster.unique()
        color = ["rgb(127,0,0)","rgb(255,0,0)","rgb(127,0,127)","rgb(0,0,255)","rgb(0,127,127)","rgb(0,255,0)"]        
        # print(Clusters)
        trace = []
        for i in range(0,len(Clusters)):
            trace.append(
                Box(
                    y=df["Forum Replies"].loc[df['Cluster']==Clusters[i]].values.tolist(),
                    name=legend['age'][i+1],
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
            title=legend['title'],
            # hovermode = "closest",
            showlegend = True,
            xaxis = dict(
                title = legend["xaxis"],
                titlefont=dict(
                    # family='Arial, sans-serif',
                    # size=18,
                    color='rgb(180,180,180)',
                ),
            ),
            yaxis = dict(
                title = legend["yaxis"],
                titlefont=dict(
                    # family='Arial, sans-serif',
                    # size=18,
                    color='rgb(180,180,180)',
                ),
                fixedrange = False,
                range = [-1, self.DATASET["Forum Replies"].max()+10],
                rangemode = "normal",
                # showline = True,
                zeroline = False,
            )
        )

        data = trace
        fig = Figure(data=data, layout=layout)
        iplot(fig, filename='box-plot')

    def graph_09(self):
        legend = {"title":"Variação de tópicos adicionados no fórum por idade",
                    "xaxis":"",
                    "yaxis":"Tópicos no fórum",
                    "age":{1:"até 25 anos", 2:"26 à 30 anos", 3:"31 à 40 anos", 4: "41 à 50 anos", 5: "51 à 60 anos", 6: "mais de 60 anos"},
                }
        if (self._language == "en"):
            legend = {"title":"Variation of students' threads added in the forum by age",
                        "xaxis":"",
                        "yaxis":"Threads in the forum",
                        "age":{1:"until 25 years", 2:"26 to 30 years", 3:"31 to 40 years", 4: "41 to 50 years", 5: "51 to 60 years", 6: "over 60 years"},
                    }
        df = self.DATASET.sort_values(by="Age")
        Clusters = df.Cluster.unique()
        color = ["rgb(127,0,0)","rgb(255,0,0)","rgb(127,0,127)","rgb(0,0,255)","rgb(0,127,127)","rgb(0,255,0)"]        
        # print(Clusters)
        trace = []
        for i in range(0,len(Clusters)):
            trace.append(
                Box(
                    y=df["Forum Add Thread"].loc[df['Cluster']==Clusters[i]].values.tolist(),
                    name=legend['age'][i+1],
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
            title=legend['title'],
            # hovermode = "closest",
            showlegend = True,
            xaxis = dict(
                title = legend["xaxis"],
                titlefont=dict(
                    # family='Arial, sans-serif',
                    # size=18,
                    color='rgb(180,180,180)',
                ),
            ),
            yaxis = dict(
                title = legend["yaxis"],
                titlefont=dict(
                    # family='Arial, sans-serif',
                    # size=18,
                    color='rgb(180,180,180)',
                ),
                fixedrange = False,
                range = [-1, self.DATASET["Forum Add Thread"].max()+10],
                rangemode = "normal",
                # showline = True,
                zeroline = False,
            )
        )

        data = trace
        fig = Figure(data=data, layout=layout)
        iplot(fig, filename='box-plot')

    #Violin
    def graph_10(self):
        legend = {"title":"Variação de acessos no fórum por idade",
                    "xaxis":"",
                    "yaxis":"Acessos no fórum",
                    "age":{1:"até 25 anos", 2:"26 à 30 anos", 3:"31 à 40 anos", 4: "41 à 50 anos", 5: "51 à 60 anos", 6: "mais de 60 anos"},
                }
        if (self._language == "en"):
            legend = {"title":"Variation of students' access in the forum by age",
                        "xaxis":"",
                        "yaxis":"Access in the forum",
                        "age":{1:"until 25 years", 2:"26 to 30 years", 3:"31 to 40 years", 4: "41 to 50 years", 5: "51 to 60 years", 6: "over 60 years"},
                    }
        # https://plot.ly/python/violin/#reference
        # https://plot.ly/python/reference/#violin
        df = self.DATASET.sort_values(by="Age")
        Clusters = df.Cluster.unique()
        color = ["rgb(127,0,0)","rgb(255,0,0)","rgb(127,0,127)","rgb(0,0,255)","rgb(0,127,127)","rgb(0,255,0)"]
        # print(Clusters)
        trace = []
        for i in range(0,len(Clusters)):
            trace.append(
                {
                    "type":'violin',
                    "x":[legend['age'][i+1]]*len(df.loc[df['Cluster']==Clusters[i]]),
                    "y":df["Forum Access"].loc[df['Cluster']==Clusters[i]],
                    "name":legend['age'][i+1],
                    "text":df["Students"].loc[df['Cluster']==Clusters[i]].values.tolist(),
                    "box":{
                        "visible":True
                        },
                    "points": 'all',
                    "meanline":{
                        "visible":True
                        },
                    "line":{
                        "color":color[i],
                    },
                    "marker": {
                        "line": {
                            "width": 1,
                        }
                    },
                }
            )
        
        layout = Layout(
            title=legend['title'],
            hovermode = "closest",
            showlegend = True,
            xaxis = dict(
                title = legend["xaxis"],
                titlefont=dict(
                    # family='Arial, sans-serif',
                    # size=18,
                    color='rgb(180,180,180)',
                ),
            ),
            yaxis = dict(
                title = legend["yaxis"],
                titlefont=dict(
                    # family='Arial, sans-serif',
                    # size=18,
                    color='rgb(180,180,180)',
                ),
                fixedrange = False,
                range = [-15, self.DATASET["Forum Access"].max()+10],                
                rangemode = "normal",
                zeroline = False,
            )
        )

        data = trace
        fig = Figure(data=data, layout=layout)
        iplot(fig, filename='violin', validate = False)

    def graph_11(self):
        legend = {"title":"Variação de postagens no fórum por idade",
                    "xaxis":"",
                    "yaxis":"Postagens no fórum",
                    "age":{1:"até 25 anos", 2:"26 à 30 anos", 3:"31 à 40 anos", 4: "41 à 50 anos", 5: "51 à 60 anos", 6: "mais de 60 anos"},
                }
        if (self._language == "en"):
            legend = {"title":"Variation of students' posts in the forum by age",
                        "xaxis":"",
                        "yaxis":"Posts in the forum",
                        "age":{1:"until 25 years", 2:"26 to 30 years", 3:"31 to 40 years", 4: "41 to 50 years", 5: "51 to 60 years", 6: "over 60 years"},
                    }
        # https://plot.ly/python/violin/#reference
        # https://plot.ly/python/reference/#violin
        df = self.DATASET.sort_values(by="Age")
        Clusters = df.Cluster.unique()
        color = ["rgb(127,0,0)","rgb(255,0,0)","rgb(127,0,127)","rgb(0,0,255)","rgb(0,127,127)","rgb(0,255,0)"]
        # print(Clusters)
        trace = []
        for i in range(0,len(Clusters)):
            trace.append(
                {
                    "type":'violin',
                    "x":[legend['age'][i+1]]*len(df.loc[df['Cluster']==Clusters[i]]),
                    "y":df["Forum Post"].loc[df['Cluster']==Clusters[i]],
                    "name":legend['age'][i+1],
                    "text":df["Students"].loc[df['Cluster']==Clusters[i]].values.tolist(),
                    "box":{
                        "visible":True
                        },
                    "points": 'all',
                    "meanline":{
                        "visible":True
                        },
                    "line":{
                        "color":color[i],
                    },
                    "marker": {
                        "line": {
                            "width": 1,
                        }
                    },
                }
            )
        
        layout = Layout(
            title=legend['title'],
            hovermode = "closest",
            showlegend = True,
            xaxis = dict(
                title = legend["xaxis"],
                titlefont=dict(
                    # family='Arial, sans-serif',
                    # size=18,
                    color='rgb(180,180,180)',
                ),
            ),
            yaxis = dict(
                title = legend["yaxis"],
                titlefont=dict(
                    # family='Arial, sans-serif',
                    # size=18,
                    color='rgb(180,180,180)',
                ),
                fixedrange = False,
                range = [-15, self.DATASET["Forum Post"].max()+10],                
                rangemode = "normal",
                zeroline = False,
            )
        )

        data = trace
        fig = Figure(data=data, layout=layout)
        iplot(fig, filename='violin', validate = False)

    def graph_12(self):
        legend = {"title":"Variação de réplicas no fórum por idade",
                    "xaxis":"",
                    "yaxis":"Réplicas no fórum",
                    "age":{1:"até 25 anos", 2:"26 à 30 anos", 3:"31 à 40 anos", 4: "41 à 50 anos", 5: "51 à 60 anos", 6: "mais de 60 anos"},
                }
        if (self._language == "en"):
            legend = {"title":"Variation of students' replies in the forum by age",
                        "xaxis":"",
                        "yaxis":"Replies in the forum",
                        "age":{1:"until 25 years", 2:"26 to 30 years", 3:"31 to 40 years", 4: "41 to 50 years", 5: "51 to 60 years", 6: "over 60 years"},
                    }
        # https://plot.ly/python/violin/#reference
        # https://plot.ly/python/reference/#violin
        df = self.DATASET.sort_values(by="Age")
        Clusters = df.Cluster.unique()
        color = ["rgb(127,0,0)","rgb(255,0,0)","rgb(127,0,127)","rgb(0,0,255)","rgb(0,127,127)","rgb(0,255,0)"]
        # print(Clusters)
        trace = []
        for i in range(0,len(Clusters)):
            trace.append(
                {
                    "type":'violin',
                    "x":[legend['age'][i+1]]*len(df.loc[df['Cluster']==Clusters[i]]),
                    "y":df["Forum Replies"].loc[df['Cluster']==Clusters[i]],
                    "name":legend['age'][i+1],
                    "text":df["Students"].loc[df['Cluster']==Clusters[i]].values.tolist(),
                    "box":{
                        "visible":True
                        },
                    "points": 'all',
                    "meanline":{
                        "visible":True
                        },
                    "line":{
                        "color":color[i],
                    },
                    "marker": {
                        "line": {
                            "width": 1,
                        }
                    },
                }
            )
        
        layout = Layout(
            title=legend['title'],
            hovermode = "closest",
            showlegend = True,
            xaxis = dict(
                title = legend["xaxis"],
                titlefont=dict(
                    # family='Arial, sans-serif',
                    # size=18,
                    color='rgb(180,180,180)',
                ),
            ),
            yaxis = dict(
                title = legend["yaxis"],
                titlefont=dict(
                    # family='Arial, sans-serif',
                    # size=18,
                    color='rgb(180,180,180)',
                ),
                fixedrange = False,
                range = [-15, self.DATASET["Forum Replies"].max()+10],                
                rangemode = "normal",
                zeroline = False,
            )
        )

        data = trace
        fig = Figure(data=data, layout=layout)
        iplot(fig, filename='violin', validate = False)

    def graph_13(self):
        legend = {"title":"Variação de tópicos adicionados no fórum por idade",
                    "xaxis":"",
                    "yaxis":"Tópicos no fórum",
                    "age":{1:"até 25 anos", 2:"26 à 30 anos", 3:"31 à 40 anos", 4: "41 à 50 anos", 5: "51 à 60 anos", 6: "mais de 60 anos"},
                }
        if (self._language == "en"):
            legend = {"title":"Variation of students' threads added in the forum by age",
                        "xaxis":"",
                        "yaxis":"Threads in the forum",
                        "age":{1:"until 25 years", 2:"26 to 30 years", 3:"31 to 40 years", 4: "41 to 50 years", 5: "51 to 60 years", 6: "over 60 years"},
                    }
        # https://plot.ly/python/violin/#reference
        # https://plot.ly/python/reference/#violin
        df = self.DATASET.sort_values(by="Age")
        Clusters = df.Cluster.unique()
        color = ["rgb(127,0,0)","rgb(255,0,0)","rgb(127,0,127)","rgb(0,0,255)","rgb(0,127,127)","rgb(0,255,0)"]
        # print(Clusters)
        trace = []
        for i in range(0,len(Clusters)):
            trace.append(
                {
                    "type":'violin',
                    "x":[legend['age'][i+1]]*len(df.loc[df['Cluster']==Clusters[i]]),
                    "y":df["Forum Add Thread"].loc[df['Cluster']==Clusters[i]],
                    "name":legend['age'][i+1],
                    "text":df["Students"].loc[df['Cluster']==Clusters[i]].values.tolist(),
                    "box":{
                        "visible":True
                        },
                    "points": 'all',
                    "meanline":{
                        "visible":True
                        },
                    "line":{
                        "color":color[i],
                    },
                    "marker": {
                        "line": {
                            "width": 1,
                        }
                    },
                }
            )
        
        layout = Layout(
            title=legend['title'],
            hovermode = "closest",
            showlegend = True,
            xaxis = dict(
                title = legend["xaxis"],
                titlefont=dict(
                    # family='Arial, sans-serif',
                    # size=18,
                    color='rgb(180,180,180)',
                ),
            ),
            yaxis = dict(
                title = legend["yaxis"],
                titlefont=dict(
                    # family='Arial, sans-serif',
                    # size=18,
                    color='rgb(180,180,180)',
                ),
                fixedrange = False,
                range = [-15, self.DATASET["Forum Add Thread"].max()+10],                
                rangemode = "normal",
                zeroline = False,
            )
        )

        data = trace
        fig = Figure(data=data, layout=layout)
        iplot(fig, filename='violin', validate = False)

    def print_all_graphs(self,language="pt"):
        self._language = language
        self.graph_01() #Table raw
        self.graph_02() #Scatter
        self.graph_03()
        self.graph_04()
        self.graph_05()
        self.graph_06() #Box
        self.graph_07()
        self.graph_08()
        self.graph_09()
        self.graph_10() #Violin
        self.graph_11()
        self.graph_12()
        self.graph_13()

instance = V006(60)
# instance.print_all_graphs("pt")
instance.print_all_graphs("en")