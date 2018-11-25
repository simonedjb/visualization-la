import pandas as pd
import numpy as np

from plotly.graph_objs import Figure, Layout, Bar, Table, Heatmap, Scatter, Box, Violin
from plotly.offline import init_notebook_mode, iplot

from sklearn import metrics
from sklearn.cluster import KMeans


init_notebook_mode(connected=True) # initiate notebook for offline plot

class V008:
    NUMBER_STUDENTS = 50
    NUMBER_WEEKS = 7
    DATASET = pd.DataFrame()

    _language = "pt"
    _work_deadline = (int(NUMBER_WEEKS/2)+(NUMBER_WEEKS%2))*7
    _test_day = NUMBER_WEEKS*7
    
    _df_sum_day = pd.DataFrame()
    _df_sum_week = pd.DataFrame()
    _df_all_day = pd.DataFrame()

    def __init__(self, number_students = 20, number_weeks = 7, language = "pt"):
        self.NUMBER_STUDENTS = number_students
        self.NUMBER_WEEKS = number_weeks

        self._language = language
        self._work_deadline = (int(self.NUMBER_WEEKS/2)+(self.NUMBER_WEEKS%2))*7
        self._test_day = self.NUMBER_WEEKS*7
        
    def generate_dataset(self):
        names = pd.read_csv("names.csv")
        self.DATASET = pd.DataFrame(columns=["Students","Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"])

        rand_names = [names.group_name[np.random.randint(0,len(names.group_name)+1)] for n in range(0,self.NUMBER_STUDENTS)]
        rand_names.sort()

        for i in range(0,self.NUMBER_STUDENTS):
            self.DATASET.loc[i,"Students"] = rand_names[i]            

            lst = sorted(np.random.triangular(0,5,15,int(self.NUMBER_WEEKS/2)+(self.NUMBER_WEEKS%2))) + sorted(np.random.triangular(0,5,15,int(self.NUMBER_WEEKS/2)))
            self.DATASET.loc[i,"Sunday"] = [int(i) for i in lst]

            lst = sorted(np.random.triangular(0,8,18,int(self.NUMBER_WEEKS/2)+(self.NUMBER_WEEKS%2))) + sorted(np.random.triangular(0,8,18,int(self.NUMBER_WEEKS/2)))
            self.DATASET.loc[i,"Monday"] = [int(i) for i in lst]

            lst = sorted(np.random.triangular(0,10,20,int(self.NUMBER_WEEKS/2)+(self.NUMBER_WEEKS%2))) + sorted(np.random.triangular(0,10,20,int(self.NUMBER_WEEKS/2)))
            self.DATASET.loc[i,"Tuesday"] = [int(i) for i in lst]

            lst = sorted(np.random.triangular(0,12,23,int(self.NUMBER_WEEKS/2)+(self.NUMBER_WEEKS%2))) + sorted(np.random.triangular(0,12,23,int(self.NUMBER_WEEKS/2)))
            self.DATASET.loc[i,"Wednesday"] = [int(i) for i in lst]

            lst = sorted(np.random.triangular(0,15,26,int(self.NUMBER_WEEKS/2)+(self.NUMBER_WEEKS%2))) + sorted(np.random.triangular(0,15,26,int(self.NUMBER_WEEKS/2)))
            self.DATASET.loc[i,"Thursday"] = [int(i) for i in lst]

            lst = sorted(np.random.triangular(0,17,28,int(self.NUMBER_WEEKS/2)+(self.NUMBER_WEEKS%2))) + sorted(np.random.triangular(0,17,28,int(self.NUMBER_WEEKS/2)))
            self.DATASET.loc[i,"Friday"] = [int(i) for i in lst]

            lst = sorted(np.random.triangular(0,8,34,int(self.NUMBER_WEEKS/2)+(self.NUMBER_WEEKS%2))) + sorted(np.random.triangular(0,8,34,int(self.NUMBER_WEEKS/2)))
            self.DATASET.loc[i,"Saturday"] = [int(i) for i in lst]

        self._df_sum_day = self.DATASET.apply(self.sum_access_by_day, axis=1, result_type='expand') # Total of access by day
        self._df_sum_day.columns = self.DATASET.columns

        self._df_sum_week = self.DATASET.apply(self.sum_access_by_week, axis=1, result_type='expand') # Total of access by week
        self._df_sum_week.columns = ["Week"+str(i+1) for i in range(0,self.NUMBER_WEEKS)]
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
        
        for i in range(0,self.NUMBER_WEEKS):
            for j in range(1,len(row)):
                sum+=row[j][i]
            lst.append(sum)
            sum = 0

        return lst

    def all_day(self,row):
        lst = []

        for i in range(0,self.NUMBER_WEEKS):
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
        legend = {"title":"Número de acessos dos estudantes por dia",
                    "xaxis":"",
                    "yaxis":"",
                    "columns":{1:"Dom", 2:"Seg", 3:"Ter", 4:"Qua", 5:"Qui", 6:"Sex", 0:"Sáb"},
                    "misc":{1:"dia", 2:"Trabalho", 3:"Prova"},
                }
        if (self._language == "en"):
            legend = {"title":"Number of students' access by day",
                        "xaxis":"",
                        "yaxis":"",
                        "columns":{1:"Sun", 2:"Mon", 3:"Tue", 4:"Wed", 5:"Thu", 6:"Fri", 0:"Sat"},
                        "misc":{1:"day", 2:"Work", 3:"Test"},
                    }
        df = self._df_all_day
        z = []
        for i in range (1, len(df.columns)):
            z.append(df.iloc[:,i].values.tolist())        
        
        lst = [legend["columns"][(int((i+1)%7))]+", "+legend["misc"][1]+" "+str(i+1) for i in range (0,len(df.columns[1:]))]
        lst[self._work_deadline-1] = "<b>"+legend["columns"][(int(self._work_deadline%7))]+", "+legend["misc"][2]+"</b>"
        lst[self._test_day-1] = "<b>"+legend["columns"][(int(self._test_day%7))]+", "+legend["misc"][3]+"</b>"
        
        trace = Heatmap(z=z, #Access
                        y=lst, #Days
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

    def graph_05(self):
        legend = {"title":"Número de acessos dos estudantes por dia",
                    "xaxis":"",
                    "yaxis":"",
                    "columns":{1:"Dom", 2:"Seg", 3:"Ter", 4:"Qua", 5:"Qui", 6:"Sex", 0:"Sáb"},
                    "misc":{1:"dia", 2:"Trabalho", 3:"Prova"},
                }
        if (self._language == "en"):
            legend = {"title":"Number of students' access by day",
                        "xaxis":"",
                        "yaxis":"",
                        "columns":{1:"Sun", 2:"Mon", 3:"Tue", 4:"Wed", 5:"Thu", 6:"Fri", 0:"Sat"},
                        "misc":{1:"day", 2:"Work", 3:"Test"},
                    }
        df = self._df_all_day
        z = []
        max_value = 0
        for i in range (1, len(df.columns)):
            z.append(df.iloc[:,i].values.tolist())
            max_local = max(df.iloc[:,i].values.tolist())
            max_value = max(max_local,max_value)
        
        lst = [legend["columns"][(int((i+1)%7))]+", "+legend["misc"][1]+" "+str(i+1) for i in range (0,len(df.columns[1:]))]
        lst[self._work_deadline-1] = "<b>"+legend["columns"][(int(self._work_deadline%7))]+", "+legend["misc"][2]+"</b>"
        lst[self._test_day-1] = "<b>"+legend["columns"][(int(self._test_day%7))]+", "+legend["misc"][3]+"</b>"

        trace = Heatmap(z=z, #Access
                        y=lst, #Days
                        x=df.iloc[:,0], #Students
                        colorscale=[[0, 'rgb(255,255,255)'], [1, 'rgb(0,0,255)']],
                        showscale = True
                    )
        
        annotations=[]
        for i in range(1,len(df.columns)):
            for j in range(0,len(df)):
                color = 'rgb(0,0,0)'
                if df.iloc[j,i] > max_value/2:
                    color = 'rgb(255,255,255)'
                annotations.append({
                    "text":str(df.iloc[j,i]),
                    "y":lst[i-1],
                    "x":df.iloc[j,0],
                    "xref":'x1', 
                    "yref":'y1',
                    "showarrow":False,
                    "font":{
                        # family='Courier New, monospace',
                        # size=16,
                        "color":color
                    }
                })
        
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
                ),
                annotations = annotations
            )

        data = [trace]
        fig = Figure(data=data, layout=layout)
        iplot(fig, filename='Heatmap')

    def graph_06(self):
        legend = {"title":"Número de acessos dos estudantes por semana",
                    "xaxis":"",
                    "yaxis":"",
                    "columns":'semana',
                    "misc":{1:"Trabalho", 2:"Prova"},
                }
        if (self._language == "en"):
            legend = {"title":"Number of students' access by week",
                        "xaxis":"",
                        "yaxis":"",
                        "columns":"week",
                        "misc":{1:"Work", 2:"Test"},
                    }
        df = self._df_sum_week
        z = []
        for i in range (1, len(df.columns)):
            z.append(df.iloc[:,i].values.tolist())        
        
        lst = [legend["columns"]+" "+str(i+1) for i in range (0,len(df.columns[1:]))]
        lst[int(self._work_deadline/7)-1] = "<b>"+legend["columns"]+" "+str(int(self._work_deadline/7))+",<br>"+legend["misc"][1]+"</b>"
        lst[int(self._test_day/7)-1] = "<b>"+legend["columns"]+" "+str(int(self._test_day/7))+",<br>"+legend["misc"][2]+"</b>"
        
        trace = Heatmap(z=z, #Access
                        y=lst, #Weeks
                        x=df.iloc[:,0], #Students
                        colorscale=[[0, 'rgb(255,255,255)'], [1, 'rgb(0,0,255)']],
                        showscale = True
                    )
        
        layout = Layout(
                title = legend["title"],
                autosize=True,
                # width=1050,
                # height=950,
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

    def graph_07(self):
        legend = {"title":"Número de acessos dos estudantes por semana",
                    "xaxis":"",
                    "yaxis":"",
                    "columns":'semana',
                    "misc":{1:"Trabalho", 2:"Prova"},
                }
        if (self._language == "en"):
            legend = {"title":"Number of students' access by week",
                        "xaxis":"",
                        "yaxis":"",
                        "columns":"week",
                        "misc":{1:"Work", 2:"Test"},
                    }
        df = self._df_sum_week
        z = []
        max_value = 0
        for i in range (1, len(df.columns)):
            z.append(df.iloc[:,i].values.tolist())
            max_local = max(df.iloc[:,i].values.tolist())
            max_value = max(max_local,max_value)
        
        lst = [legend["columns"]+" "+str(i+1) for i in range (0,len(df.columns[1:]))]
        lst[int(self._work_deadline/7)-1] = "<b>"+legend["columns"]+" "+str(int(self._work_deadline/7))+",<br>"+legend["misc"][1]+"</b>"
        lst[int(self._test_day/7)-1] = "<b>"+legend["columns"]+" "+str(int(self._test_day/7))+",<br>"+legend["misc"][2]+"</b>"
        
        trace = Heatmap(z=z, #Access
                        y=lst, #Weeks
                        x=df.iloc[:,0], #Students
                        colorscale=[[0, 'rgb(255,255,255)'], [1, 'rgb(0,0,255)']],
                        showscale = True
                    )
        
        annotations=[]
        for i in range(1,len(df.columns)):
            for j in range(0,len(df)):
                color = 'rgb(0,0,0)'
                if df.iloc[j,i] > max_value/2:
                    color = 'rgb(255,255,255)'
                annotations.append({
                    "text":str(df.iloc[j,i]),
                    "y":lst[i-1],
                    "x":df.iloc[j,0],
                    "xref":'x1', 
                    "yref":'y1',
                    "showarrow":False,
                    "font":{
                        # "family":'Courier New, monospace',
                        "size":9,
                        "color":color
                    }
                })

        layout = Layout(
                title = legend["title"],
                autosize=True,
                # width=1050,
                # height=950,
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
                ),
                annotations=annotations
            )

        data = [trace]
        fig = Figure(data=data, layout=layout)
        iplot(fig, filename='Heatmap')

    # Box
    def graph_08(self):
        legend = {"title":"Número de acessos dos estudantes por dia",
                    "xaxis":"",
                    "yaxis":"Acessos",
                    "columns":{1:"Dom", 2:"Seg", 3:"Ter", 4:"Qua", 5:"Qui", 6:"Sex", 0:"Sáb"},
                    "misc":{1:"dia", 2:"Trabalho", 3:"Prova"},
                }
        if (self._language == "en"):
            legend = {"title":"Number of students' access by day",
                        "xaxis":"",
                        "yaxis":"Access",
                        "columns":{1:"Sun", 2:"Mon", 3:"Tue", 4:"Wed", 5:"Thu", 6:"Fri", 0:"Sat"},
                        "misc":{1:"day", 2:"Work", 3:"Test"},
                    }
        df = self._df_all_day
        max_value = 0
        for i in range (1, len(df.columns)):            
            max_local = max(df.iloc[:,i].values.tolist())
            max_value = max(max_local,max_value)

        lst = [legend["columns"][(int((i+1)%7))]+", "+legend["misc"][1]+" "+str(i+1) for i in range (0,len(df.columns[1:]))]
        lst[self._work_deadline-1] = "<b>"+legend["columns"][(int(self._work_deadline%7))]+", "+legend["misc"][2]+"</b>"
        lst[self._test_day-1] = "<b>"+legend["columns"][(int(self._test_day%7))]+", "+legend["misc"][3]+"</b>"
                
        trace = []
        for i in range(1,len(df.columns)):
            color = "rgb(0,0,255)"
            if i == self._work_deadline or i == self._test_day:
                color = "rgb(255,0,0)"
            
            trace.append(
                Box(
                    y=df.iloc[:,i].values.tolist(), #Access
                    name=lst[i-1],
                    text=df["Students"].values.tolist(),
                    boxpoints = 'all',
                    marker=dict(
                        color = color,
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
                range = [-1, max_value+5],
                rangemode = "normal",
                # showline = True,                
                zeroline = False,
            )
        )

        data = trace
        fig = Figure(data=data, layout=layout)
        iplot(fig, filename='box-plot')

    def graph_09(self):
        legend = {"title":"Número de acessos dos estudantes por semana",
                    "xaxis":"",
                    "yaxis":"Acessos",
                    "columns":'semana',
                    "misc":{1:"Trabalho", 2:"Prova"},
                }
        if (self._language == "en"):
            legend = {"title":"Number of students' access by week",
                        "xaxis":"",
                        "yaxis":"Access",
                        "columns":"week",
                        "misc":{1:"Work", 2:"Test"},
                    }
        df = self._df_sum_week
        
        max_value = 0
        for i in range (1, len(df.columns)):            
            max_local = max(df.iloc[:,i].values.tolist())
            max_value = max(max_local,max_value)

        lst = [legend["columns"]+" "+str(i+1) for i in range (0,len(df.columns[1:]))]
        lst[int(self._work_deadline/7)-1] = "<b>"+legend["columns"]+" "+str(int(self._work_deadline/7))+",<br>"+legend["misc"][1]+"</b>"
        lst[int(self._test_day/7)-1] = "<b>"+legend["columns"]+" "+str(int(self._test_day/7))+",<br>"+legend["misc"][2]+"</b>"
                
        trace = []
        for i in range(1,len(df.columns)):
            color = "rgb(0,0,255)"            
            if i == int(self._work_deadline/7) or i == int(self._test_day/7):
                color = "rgb(255,0,0)"

            trace.append(
                Box(
                    y=df.iloc[:,i].values.tolist(), #Access                    
                    name=lst[i-1],
                    text=df["Students"].values.tolist(),
                    boxpoints = 'all',
                    marker=dict(
                        color = color,
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
                range = [-1, max_value+5],
                rangemode = "normal",
                # showline = True,                
                zeroline = False,
            )
        )

        data = trace
        fig = Figure(data=data, layout=layout)
        iplot(fig, filename='box-plot')

    # Violin
    def graph_10(self):
        legend = {"title":"Número de acessos dos estudantes por dia",
                    "xaxis":"",
                    "yaxis":"Acessos",
                    "columns":{1:"Dom", 2:"Seg", 3:"Ter", 4:"Qua", 5:"Qui", 6:"Sex", 0:"Sáb"},
                    "misc":{1:"dia", 2:"Trabalho", 3:"Prova"},
                }
        if (self._language == "en"):
            legend = {"title":"Number of students' access by day",
                        "xaxis":"",
                        "yaxis":"Access",
                        "columns":{1:"Sun", 2:"Mon", 3:"Tue", 4:"Wed", 5:"Thu", 6:"Fri", 0:"Sat"},
                        "misc":{1:"day", 2:"Work", 3:"Test"},
                    }
        
        df = self._df_all_day
        max_value = 0
        for i in range (1, len(df.columns)):            
            max_local = max(df.iloc[:,i].values.tolist())
            max_value = max(max_local,max_value)

        lst = [legend["columns"][(int((i+1)%7))]+", "+legend["misc"][1]+" "+str(i+1) for i in range (0,len(df.columns[1:]))]
        lst[self._work_deadline-1] = "<b>"+legend["columns"][(int(self._work_deadline%7))]+", "+legend["misc"][2]+"</b>"
        lst[self._test_day-1] = "<b>"+legend["columns"][(int(self._test_day%7))]+", "+legend["misc"][3]+"</b>"
                
        trace = []
        for i in range(1,len(df.columns)):
            color = "rgb(0,0,255)"
            if i == self._work_deadline or i == self._test_day:
                color = "rgb(255,0,0)"
            trace.append(
                {
                    "type":'violin',
                    "x":[lst[i-1]]*len(df),
                    "y":df.iloc[:,i].values.tolist(), #Access
                    "name":lst[i-1],
                    "text":df["Students"].values.tolist(),
                    "box":{
                        "visible":True
                        },
                    "points": 'all',
                    "meanline":{
                        "visible":True
                        },
                    "line":{
                        "color":color,
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
                range = [-15, max_value+10],
                rangemode = "normal",
                zeroline = False,
            )
        )

        data = trace
        fig = Figure(data=data, layout=layout)
        iplot(fig, filename='violin', validate = False)

    def graph_11(self):
        legend = {"title":"Número de acessos dos estudantes por semana",
                    "xaxis":"",
                    "yaxis":"Acessos",
                    "columns":'semana',
                    "misc":{1:"Trabalho", 2:"Prova"},
                }
        if (self._language == "en"):
            legend = {"title":"Number of students' access by week",
                        "xaxis":"",
                        "yaxis":"Access",
                        "columns":"week",
                        "misc":{1:"Work", 2:"Test"},
                    }
        
        df = self._df_sum_week
        max_value = 0
        for i in range (1, len(df.columns)):            
            max_local = max(df.iloc[:,i].values.tolist())
            max_value = max(max_local,max_value)

        lst = [legend["columns"]+" "+str(i+1) for i in range (0,len(df.columns[1:]))]
        lst[int(self._work_deadline/7)-1] = "<b>"+legend["columns"]+" "+str(int(self._work_deadline/7))+",<br>"+legend["misc"][1]+"</b>"
        lst[int(self._test_day/7)-1] = "<b>"+legend["columns"]+" "+str(int(self._test_day/7))+",<br>"+legend["misc"][2]+"</b>"
                
        trace = []
        for i in range(1,len(df.columns)):
            color = "rgb(0,0,255)"            
            if i == int(self._work_deadline/7) or i == int(self._test_day/7):
                color = "rgb(255,0,0)"
            trace.append(
                {
                    "type":'violin',
                    "x":[lst[i-1]]*len(df),
                    "y":df.iloc[:,i].values.tolist(), #Access
                    "name":lst[i-1],
                    "text":df["Students"].values.tolist(),
                    "box":{
                        "visible":True
                        },
                    "points": 'all',
                    "meanline":{
                        "visible":True
                        },
                    "line":{
                        "color":color,
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
                range = [-15, max_value+10],
                rangemode = "normal",
                zeroline = False,
            )
        )

        data = trace
        fig = Figure(data=data, layout=layout)
        iplot(fig, filename='violin', validate = False)

    def print_all_graphs(self,language="pt"):
        self._language = language
        self.graph_01() #Table
        self.graph_02() 
        self.graph_03()
        self.graph_04() #Heatmap
        self.graph_05()
        self.graph_06() 
        self.graph_07()
        self.graph_08() #Box
        self.graph_09()
        self.graph_10() #Violin
        self.graph_11()        

instance = V008(number_students=35, number_weeks=7)
instance.generate_dataset()
instance.print_all_graphs("pt")
# instance.print_all_graphs("en")