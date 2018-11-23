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
        legend = {"title":"Número de estudantes que entenderam os vídeos",
                    "xaxis":"",
                    "yaxis":"Número de estudantes",
                }
        if (self._language == "en"):
            legend = {"title":"Number of students that understood the video",
                        "xaxis":"",
                        "yaxis":"Number of students",
                    }

        df = self._df_sum_feedback
        trace = [Bar(
            x=df.Videos.values,
            y=df.Understood.values,
        )]

        data = trace
        layout = Layout(
            title = legend["title"],
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
                tick0=0,
                dtick=5,
                # ticklen=5,
                # tickwidth=4,
                exponentformat='e',
                showexponent='all',
                gridcolor='#bdbdbd',
                # range=[0, 4.1]
            )
        )

        fig = Figure(data=data, layout=layout)
        iplot(fig, filename='Bar')

    def graph_04(self):
        legend = {"title":"Número de estudantes que não entenderam os vídeos",
                    "xaxis":"",
                    "yaxis":"Número de estudantes",
                }
        if (self._language == "en"):
            legend = {"title":"Number of students that do not understood the video",
                        "xaxis":"",
                        "yaxis":"Number of students",
                    }

        df = self._df_sum_feedback
        trace = [Bar(
            x=df.Videos.values,
            y=df.Misunderstood.values,
        )]

        data = trace
        layout = Layout(
            title = legend["title"],
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
                tick0=0,
                dtick=5,
                # ticklen=5,
                # tickwidth=4,
                exponentformat='e',
                showexponent='all',
                gridcolor='#bdbdbd',
                # range=[0, 4.1]
            )
        )

        fig = Figure(data=data, layout=layout)
        iplot(fig, filename='Bar')

    def graph_05(self):
        legend = {"title":"Número de estudantes que entenderam os vídeos",
                    "xaxis":"Número de estudantes",
                    "yaxis":"",
                }
        if (self._language == "en"):
            legend = {"title":"Number of students that understood the video",
                        "xaxis":"Number of students",
                        "yaxis":"",
                    }

        df = self._df_sum_feedback
        trace = [Bar(
            x=df.Understood.values,
            y=df.Videos.values,
            orientation='h'
        )]

        data = trace
        layout = Layout(
            title = legend["title"],
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
                tick0=0,
                dtick=1,
                # ticklen=5,
                # tickwidth=4,
                exponentformat='e',
                showexponent='all',
                gridcolor='#bdbdbd',
                # range=[0, 4.1]
            )
        )

        fig = Figure(data=data, layout=layout)
        iplot(fig, filename='Bar')

    def graph_06(self):
        legend = {"title":"Número de estudantes que não entenderam os vídeos",
                    "xaxis":"Número de estudantes",
                    "yaxis":"",
                }
        if (self._language == "en"):
            legend = {"title":"Number of students that do not understood the video",
                        "xaxis":"Number of students",
                        "yaxis":"",
                    }

        df = self._df_sum_feedback
        trace = [Bar(
            x=df.Misunderstood.values,
            y=df.Videos.values,
            orientation='h'
        )]

        data = trace
        layout = Layout(
            title = legend["title"],
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
                tick0=0,
                dtick=1,
                # ticklen=5,
                # tickwidth=4,
                exponentformat='e',
                showexponent='all',
                gridcolor='#bdbdbd',
                # range=[0, 4.1]
            )
        )

        fig = Figure(data=data, layout=layout)
        iplot(fig, filename='Bar')

    #Lollipop
    def graph_07(self):
        legend = {"title":"Número de estudantes que entenderam os vídeos",
                    "xaxis":"Número de estudantes",
                    "yaxis":"",
                    "text_s":"estudante",
                    "text_p":"estudantes",
                }
        if (self._language == "en"):
            legend = {"title":"Number of students that understood the video",
                        "xaxis":"Number of students",
                        "yaxis":"",
                        "text_s":"student",
                        "text_p":"students",
                    }
        df = self._df_sum_feedback
        
        trace = []
        trace.append(
            Bar(
                x=df.Understood.values,
                y=df.Videos.values,
                width=[0.07]*20,
                orientation = 'h',
                name="",
                text="",
                marker=dict(
                        color = 'lightgray',
                        # line=dict(
                        #     color = 'lightgray',
                        #     width=2
                        # )
                    )
            )
        )
        
        for i in range(0, max(df.Understood.values.tolist())+1):
            text=str(i)+" "+legend['text_p'],
            if i==1:
                text=str(i)+" "+legend['text_s'],

            trace.append(
                Scatter(
                    x=[i]*len(df.Videos),
                    y=df.Videos.loc[df["Understood"]==i].values.tolist(),
                    mode='markers',
                    name = "",                 
                    text=text*len(df.Videos.loc[df["Understood"]==i]),                    
                    marker=dict(
                        symbol='circle',
                        sizemode='area',
                        color = 'rgb(0,0,255)',
                        line=dict(
                            width=2
                        )
                    )                
                )                        
            )

        data = trace
        
        layout = Layout(
            title = legend["title"],
            showlegend=False,
            # showgrid=False,
            hovermode = "closest",
            xaxis=dict(
                title = legend["xaxis"],
                titlefont=dict(
                    # family='Arial, sans-serif',
                    # size=18,
                    color='rgb(180,180,180)',
                ),
                tick0=0,
                dtick=1,
                showgrid=True
            ),
            yaxis=dict(
                title = legend["yaxis"],
                titlefont=dict(
                    # family='Arial, sans-serif',
                    # size=18,
                    color='rgb(180,180,180)',
                ),
                showticklabels=True,
                tick0=0,
                dtick=1,
                showgrid=False,
                # ticklen=4,
                # tickwidth=4,
                exponentformat='e',
                showexponent='all',
                gridcolor='#bdbdbd',
                # range=[0, 4.1]
            )
        )

        fig = Figure(data=data, layout=layout)
        iplot(fig, filename='Lollipop')

    def graph_08(self):
        legend = {"title":"Número de estudantes que não entenderam os vídeos",
                    "xaxis":"Número de estudantes",
                    "yaxis":"",
                    "text_s":"estudante",
                    "text_p":"estudantes",
                }
        if (self._language == "en"):
            legend = {"title":"Number of students that do not understood the video",
                        "xaxis":"Number of students",
                        "yaxis":"",
                        "text_s":"student",
                        "text_p":"students",
                    }
        df = self._df_sum_feedback
        
        trace = []
        trace.append(
            Bar(
                x=df.Misunderstood.values,
                y=df.Videos.values,
                width=[0.07]*20,
                orientation = 'h',
                name="",
                text="",
                marker=dict(
                        color = 'lightgray',
                        # line=dict(
                        #     color = 'lightgray',
                        #     width=2
                        # )
                    )
            )
        )
        
        for i in range(0, max(df.Misunderstood.values.tolist())+1):
            text=str(i)+" "+legend['text_p'],
            if i==1:
                text=str(i)+" "+legend['text_s'],

            trace.append(
                Scatter(
                    x=[i]*len(df.Videos),
                    y=df.Videos.loc[df["Misunderstood"]==i].values.tolist(),
                    mode='markers',
                    name = "",                 
                    text=text*len(df.Videos.loc[df["Misunderstood"]==i]),                    
                    marker=dict(
                        symbol='circle',
                        sizemode='area',
                        color = 'rgb(0,0,255)',
                        line=dict(
                            width=2
                        )
                    )                
                )                        
            )

        data = trace
        
        layout = Layout(
            title = legend["title"],
            showlegend=False,
            # showgrid=False,
            hovermode = "closest",
            xaxis=dict(
                title = legend["xaxis"],
                titlefont=dict(
                    # family='Arial, sans-serif',
                    # size=18,
                    color='rgb(180,180,180)',
                ),
                tick0=0,
                dtick=1,
                showgrid=True
            ),
            yaxis=dict(
                title = legend["yaxis"],
                titlefont=dict(
                    # family='Arial, sans-serif',
                    # size=18,
                    color='rgb(180,180,180)',
                ),
                showticklabels=True,
                tick0=0,
                dtick=1,
                showgrid=False,
                # ticklen=4,
                # tickwidth=4,
                exponentformat='e',
                showexponent='all',
                gridcolor='#bdbdbd',
                # range=[0, 4.1]
            )
        )

        fig = Figure(data=data, layout=layout)
        iplot(fig, filename='Lollipop')

    #Scatter
    def graph_09(self):
        # https://plot.ly/python/bubble-charts/
        # https://plot.ly/python/reference/#layout-xaxis
        # https://plot.ly/python/axes/#subcategory-axes
        legend = {"title":"Vídeos entendidos por estudante",
                    "xaxis":"",
                    "yaxis":"",
                }
        if (self._language == "en"):
            legend = {"title":"Understood videos by students",
                        "xaxis":"",
                        "yaxis":"",
                    }
        df = self.DATASET

        sizeref = 0.01
        
        trace = []
        for i in range(0, len(df)):                    
            trace.append(
                Scatter(
                    x=[df.iloc[i,0]]*len(df.columns), #student
                    y=df.columns[1:], #assigns
                    mode='markers',
                    # name=df.iloc[i,0], #each student name
                    name=df.iloc[i,0], #student name
                    # text = df.iloc[i,1:].values.tolist(),
                    marker=dict(
                        symbol='circle',
                        sizemode='area',
                        sizeref=sizeref,
                        size=df.iloc[i,1:].values.tolist(),
                        color = 'rgb(0,0,255)',
                        line=dict(
                            width=2
                        )
                    )
                )
            )

        layout = Layout(
            title=legend['title'],
            # title='Number of access in the materials grouped by student',
            hovermode = "closest",
            showlegend = True,
            xaxis = dict(
                title = legend['xaxis'],
                titlefont=dict(
                    # family='Arial, sans-serif',
                    # size=18,
                    color='rgb(180,180,180)',
                ),
                autorange = False,
                # categoryorder = "category ascending",
                # domain = [0, 1],
                fixedrange = False,
                range = [-1, len(df)],
                rangemode = "normal",
                showline = True,                
                type = "category"
            ),
            yaxis = dict(
                title = legend['yaxis'],
                titlefont=dict(
                    # family='Arial, sans-serif',
                    # size=18,
                    color='rgb(180,180,180)',
                ),
                autorange = False,
                # categoryorder = "category ascending",
                # domain = [0, 1],
                fixedrange = False,
                range = [-1, len(df.columns[1:])],
                rangemode = "normal",
                showline = True,                
                type = "category"
            )
        )

        data = trace
        fig=Figure(data=data, layout=layout)
        iplot(fig, filename='bubblechart-size')

    def graph_10(self):
        # https://plot.ly/python/bubble-charts/
        # https://plot.ly/python/reference/#layout-xaxis
        # https://plot.ly/python/axes/#subcategory-axes
        legend = {"title":"Vídeos não entendidos por estudante",
                    "xaxis":"",
                    "yaxis":"",
                }
        if (self._language == "en"):
            legend = {"title":"Misunderstood videos by students",
                        "xaxis":"",
                        "yaxis":"",
                    }
        df = self.DATASET

        sizeref = 0.01
        
        trace = []
        for i in range(0, len(df)):
            x = df.iloc[i,1:].values.tolist()
            y = [-1]*len(df.columns[1:])
            z = [i + j for i, j in zip(x, y)]
            values = [i*(-1) for i in z]
            trace.append(
                Scatter(
                    x=[df.iloc[i,0]]*len(df.columns), #student
                    y=df.columns[1:], #assigns
                    mode='markers',
                    # name=df.iloc[i,0], #each student name
                    name=df.iloc[i,0], #student name
                    # text = df.iloc[i,1:].values.tolist(),
                    marker=dict(
                        symbol='circle',
                        sizemode='area',
                        sizeref=sizeref,
                        size=values,
                        color = 'rgb(0,0,255)',
                        line=dict(
                            width=2
                        )
                    )
                )
            )

        layout = Layout(
            title=legend['title'],
            # title='Number of access in the materials grouped by student',
            hovermode = "closest",
            showlegend = True,
            xaxis = dict(
                title = legend['xaxis'],
                titlefont=dict(
                    # family='Arial, sans-serif',
                    # size=18,
                    color='rgb(180,180,180)',
                ),
                autorange = False,
                # categoryorder = "category ascending",
                # domain = [0, 1],
                fixedrange = False,
                range = [-1, len(df)],
                rangemode = "normal",
                showline = True,                
                type = "category"
            ),
            yaxis = dict(
                title = legend['yaxis'],
                titlefont=dict(
                    # family='Arial, sans-serif',
                    # size=18,
                    color='rgb(180,180,180)',
                ),
                autorange = False,
                # categoryorder = "category ascending",
                # domain = [0, 1],
                fixedrange = False,
                range = [-1, len(df.columns[1:])],
                rangemode = "normal",
                showline = True,                
                type = "category"
            )
        )

        data = trace
        fig=Figure(data=data, layout=layout)
        iplot(fig, filename='bubblechart-size')

    def graph_11(self):
        # https://plot.ly/python/bubble-charts/
        # https://plot.ly/python/reference/#layout-xaxis
        # https://plot.ly/python/axes/#subcategory-axes
        legend = {"title":"Número de estudantes que entenderam os vídeos",
                    "xaxis":"",
                    "yaxis":"",
                    "columns":{1:"Entendidos", 2:"Não<br>entendidos"}
                }
        if (self._language == "en"):
            legend = {"title":"Number of students that understood the videos",
                        "xaxis":"",
                        "yaxis":"",
                        "columns":{1:"Understood", 2:"Misunderstood"}
                    }
        df = self._df_sum_feedback.iloc[:,0:3]
        sizeref = 0.03
        
        trace = []
        for i in range(0, len(df)):                    
            trace.append(
                Scatter(
                    x=[df.iloc[i,0]]*len(df.columns), #videos
                    # y=df.columns[1:], #features ()
                    y=[legend["columns"][i] for i in range (1,3)],
                    mode='markers',                    
                    name=df.iloc[i,0], #videos
                    text = df.iloc[i,1:].values.tolist(),
                    marker=dict(
                        symbol='circle',
                        sizemode='area',
                        sizeref=sizeref,
                        size=df.iloc[i,1:].values.tolist(),
                        color = 'rgb(0,0,255)',
                        line=dict(
                            width=2
                        )
                    )
                )
            )

        layout = Layout(
            title=legend['title'],
            # title='Number of access in the materials grouped by student',
            hovermode = "closest",
            showlegend = True,
            xaxis = dict(
                title = legend['xaxis'],
                titlefont=dict(
                    # family='Arial, sans-serif',
                    # size=18,
                    color='rgb(180,180,180)',
                ),
                autorange = False,
                # categoryorder = "category ascending",
                # domain = [0, 1],
                fixedrange = False,
                range = [-1, len(df)],
                rangemode = "normal",
                showline = True,                
                type = "category"
            ),
            yaxis = dict(
                title = legend['yaxis'],
                titlefont=dict(
                    # family='Arial, sans-serif',
                    # size=18,
                    color='rgb(180,180,180)',
                ),
                autorange = False,
                # categoryorder = "category ascending",
                # domain = [0, 1],
                fixedrange = False,
                range = [-1, len(df.columns[1:])],
                rangemode = "normal",
                showline = True,                
                type = "category"
            )
        )

        data = trace
        fig=Figure(data=data, layout=layout)
        iplot(fig, filename='bubblechart-size')
    
    #Heatmap
    def graph_12(self):
        legend = {"title":"Vídeos entendidos por estudante",
                    "xaxis":"",
                    "yaxis":"",
                }
        if (self._language == "en"):
            legend = {"title":"Understood videos by students",
                        "xaxis":"",
                        "yaxis":"",
                    }
        df = self.DATASET
        z = []
        for i in range (1, len(df.columns)):
            z.append(df.iloc[:,i].values.tolist())

        trace = Heatmap(z=z,
                        y=df.columns[1:], #Videos
                        x=df.iloc[:,0], #Students
                        colorscale=[[0, 'rgb(255,255,255)'], [1, 'rgb(0,0,255)']],
                        showscale = False
                    )
        
        layout = Layout(
                title = legend['title'],                
                autosize=False,
                width=950,
                height=350,
                hovermode = "closest",
                xaxis=dict(
                    title = legend['xaxis'],
                    titlefont=dict(
                    # family='Arial, sans-serif',
                    # size=18,
                    color='rgb(180,180,180)',
                ),
                ),                
                yaxis=dict(
                    title = legend['yaxis'],
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

    def graph_13(self):
        legend = {"title":"Vídeos não entendidos por estudante",
                    "xaxis":"",
                    "yaxis":"",
                }
        if (self._language == "en"):
            legend = {"title":"Misunderstood videos by students",
                        "xaxis":"",
                        "yaxis":"",
                    }
        df = self.DATASET
        z = []
        for i in range (1, len(df.columns)):
            x = df.iloc[:,i].values.tolist()
            y = [-1]*len(x)
            f = [a + b for a, b in zip(x, y)]
            values = [a*(-1) for a in f]
            z.append(values)

        trace = Heatmap(z=z,
                        y=df.columns[1:], #Videos
                        x=df.iloc[:,0], #Students
                        colorscale=[[0, 'rgb(255,255,255)'], [1, 'rgb(0,0,255)']],
                        showscale = False
                    )
        
        layout = Layout(
                title = legend['title'],                
                autosize=False,
                width=950,
                height=350,
                hovermode = "closest",
                xaxis=dict(
                    title = legend['xaxis'],
                    titlefont=dict(
                    # family='Arial, sans-serif',
                    # size=18,
                    color='rgb(180,180,180)',
                ),
                ),                
                yaxis=dict(
                    title = legend['yaxis'],
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

    def graph_14(self):
        legend = {"title":"Número de estudantes que entenderam os vídeos",
                    "xaxis":"",
                    "yaxis":"",
                    "columns":{1:"Entendidos", 2:"Não<br>entendidos"}
                }
        if (self._language == "en"):
            legend = {"title":"Number of students that understood the videos",
                        "xaxis":"",
                        "yaxis":"",
                        "columns":{1:"Understood", 2:"Misunderstood"}
                    }
        df = self._df_sum_feedback.iloc[:,0:3]
        z = []
        for i in range (1, len(df.columns)):
            z.append(df.iloc[:,i].values.tolist())

        trace = Heatmap(z=z,
                        # y=df.columns[1:], #Videos
                        y=[legend["columns"][i] for i in range (1,3)],
                        x=df.iloc[:,0], #Students
                        colorscale=[[0, 'rgb(255,255,255)'], [1, 'rgb(0,0,255)']],
                        showscale = True
                    )
        
        layout = Layout(
                title = legend['title'],                
                autosize=False,
                width=950,
                height=350,
                hovermode = "closest",
                xaxis=dict(
                    title = legend['xaxis'],
                    titlefont=dict(
                    # family='Arial, sans-serif',
                    # size=18,
                    color='rgb(180,180,180)',
                ),
                ),                
                yaxis=dict(
                    title = legend['yaxis'],
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

    #Grouped Bar
    def graph_15(self):
        legend = {"title":"Número de estudantes que entenderam e não entenderam os vídeos",
                    "xaxis":"",
                    "yaxis":"",
                    "columns":{1:"Entendidos", 2:"Não<br>entendidos"}
                }
        if (self._language == "en"):
            legend = {"title":"Number of students that understood and misunderstood the videos",
                        "xaxis":"",
                        "yaxis":"",
                        "columns":{1:"Understood", 2:"Misunderstood"}
                    }
        
        df = self._df_sum_feedback
        
        trace = []
        for i in range(1,len(df.columns[1:len(df.columns)])): 
            trace.append(Bar(
                    x=df.Videos.values,
                    y=df.iloc[:,i].values,
                    # name=df.columns[i]
                    name=legend['columns'][i]
            ))            

        data = trace
        layout = Layout(
                title=legend["title"],
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
                    tick0=0,
                    dtick=5,
        #             ticklen=4,
        #             tickwidth=4,
                    exponentformat='e',
                    showexponent='all',
                    gridcolor='#bdbdbd',
        #             range=[0, 4.1]
                )
            )

        fig = Figure(data=data, layout=layout)
        iplot(fig, filename='Grouped_Bar')

    #Stacked Bar
    def graph_16(self):
        legend = {"title":"Número de estudantes que entenderam e não entenderam os vídeos",
                    "xaxis":"",
                    "yaxis":"",
                    "columns":{1:"Entendidos", 2:"Não<br>entendidos"}
                }
        if (self._language == "en"):
            legend = {"title":"Number of students that understood and misunderstood the videos",
                        "xaxis":"",
                        "yaxis":"",
                        "columns":{1:"Understood", 2:"Misunderstood"}
                    }

        df = self._df_sum_feedback
        trace = []
        for i in range(1,len(df.columns[1:len(df.columns)])):         
            trace.append(Bar(
                    x=df.Videos.values,
                    y=df.iloc[:,i].values,
                    # name=df.columns[i]
                    name=legend['columns'][i]
            ))

        data = trace
        layout = Layout(
                title=legend["title"],
                xaxis=dict(
                    title = legend["xaxis"],
                    titlefont=dict(
                        # family='Arial, sans-serif',
                        # size=18,
                        color='rgb(180,180,180)',
                    ),
                ),
                barmode='stack',
                yaxis=dict(
                    title = legend["yaxis"],
                    titlefont=dict(
                        # family='Arial, sans-serif',
                        # size=18,
                        color='rgb(180,180,180)',
                    ),
                    showticklabels=True,
                    tick0=0,
                    dtick=5,
        #             ticklen=4,
        #             tickwidth=4,
                    exponentformat='e',
                    showexponent='all',
                    gridcolor='#bdbdbd',
        #             range=[0, 4.1]
                )
            )

        fig = Figure(data=data, layout=layout)
        iplot(fig, filename='Stacked_Bar')

    def graph_17(self):
        legend = {"title":"Número de estudantes que entenderam e não entenderam os vídeos",
                    "xaxis":"",
                    "yaxis":"",
                    "columns":{1:"Entendidos", 2:"Não<br>entendidos"}
                }
        if (self._language == "en"):
            legend = {"title":"Number of students that understood and misunderstood the videos",
                        "xaxis":"",
                        "yaxis":"",
                        "columns":{1:"Understood", 2:"Misunderstood"}
                    }

        df = self._df_sum_feedback
        trace = []
        for i in range(1,len(df.columns[1:len(df.columns)])):
            trace.append(Bar(                    
                    x=df.iloc[:,i].values,
                    y=df.Videos.values,
                    # name=df.columns[i],
                    name=legend['columns'][i],
                    orientation = 'h'
            ))

        data = trace
        layout = Layout(
                title=legend["title"],
                barmode='stack',
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
                    tick0=0,
                    dtick=1,
        #             ticklen=4,
        #             tickwidth=4,
                    exponentformat='e',
                    showexponent='all',
                    gridcolor='#bdbdbd',
        #             range=[0, 4.1]
                )
            )

        fig = Figure(data=data, layout=layout)
        iplot(fig, filename='Stacked_Bar')

    def print_all_graphs(self,language="pt"):
        self._language = language
        self.graph_01() # Table
        self.graph_02()
        self.graph_03() #Bar
        self.graph_04() 
        self.graph_05() 
        self.graph_06()
        self.graph_07() #Lollipop
        self.graph_08()
        self.graph_09() #Scatter
        self.graph_10()
        self.graph_11()
        self.graph_12() #Heatmap
        self.graph_13()
        self.graph_14()
        self.graph_15() #Grouped Bar
        self.graph_16() #Stacked Bar
        self.graph_17()
        #Falta apresentar os gráficos de barra ordenados 
        


instance = V010(number_students=35, number_video=10)
instance.print_all_graphs("pt")
# instance.print_all_graphs("en")
