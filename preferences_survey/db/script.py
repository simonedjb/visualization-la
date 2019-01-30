import ast
import pandas as pd
import numpy as np
import os

from pathlib import Path
from six.moves import urllib

class preferences:
    dataset = pd.DataFrame()
    desc = ''
    path_file = 'z_official_dataset.csv'
    instance_name = ''
    charts = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    likert = ['strong_disagree','partially_disagree','slightly_disagree','neutral','slightly_agree','partially_agree','strong_agree']
    charts_evaluation = []
    legend = []
    
    def __init__(self, path_file=None):
        if path_file != None:
            self.path_file= path_file
        
        self.load(self.path_file,'infer',',',None,None,'infer','UTF-8')
    
    def load(self, path_file, compression='infer', sep=',', nrows=None, skiprows=None,header='infer',encoding='UTF-8'):
        self.dataset = pd.read_csv(path_file, compression=compression, nrows=nrows, skiprows=skiprows, error_bad_lines=False, sep=sep, encoding=encoding, low_memory=False, header=header)
        print("dataset loaded: "+self.path_file)
        print("")

    def list_columns(self):
        print("Columns: ")
        print(self.dataset.columns.values.tolist())

    def load_legends(self, columns=[]):
        if columns==[]:
            print("Without columns")
        
        print("Assigning letters legends to each chart:"+str(self.charts))
        for i in range(0,len(columns)):
            lst = ast.literal_eval(self.dataset[columns[i]].dropna().head(1).tolist()[0])
            dictionary = []
            for j in range(0,len(lst)-1):
                dictionary.append({"field":lst[j]["field"],"chart":self.charts[j]})
            self.legend.append(dictionary)
            print("V"+str(i+1)+": "+str(self.legend[i]))
            print("")
            

    def get_legend(self,v_index,chart):
        lst = self.legend[v_index]
        for i in range(0,len(lst)):
            if lst[i]["field"] == chart:
                # print(lst[i]["chart"])
                return lst[i]["chart"]

    def preferences_chart(self, columns=[], field_name=''):
        if columns==[]:
            print("Without columns")

        if len(self.legend) == 0:
            self.load_legends(columns=columns)
        
        values=[]
        view=[]
        for i in range(0,len(columns)):
            values.append(self.dataset[columns[i]])
            view.append([0]*len(self.charts)) #count most selected charts
            # print(values)
        
        print("Instructor preferences: "+str(["View "+str(i+1) for i in range(len(columns))]))
        for i in range(0,len(values[0])): #iterate in the lines
            pref_chart = []
            pref_legend = []
            for j in range(0,len(columns)):
                if str(values[j][i]) == "nan":
                    pref_chart.append(None)
                    pref_legend.append(None)
                else:
                    lst = values[j][i]
                    lst = ast.literal_eval(lst)
                    for k in range(0,len(lst)):
                        if lst[k]['field'] == field_name:
                            pref_chart.append(lst[k]["value"])
                            legend = self.get_legend(j,lst[k]["value"])
                            pref_legend.append(legend)
                            view[j][self.charts.index(legend)] += 1

            # print("Instructor "+str(i+1)+": "+str(pref_chart))
            print("Instructor "+str(i+1)+": "+str(pref_legend))
            pref_chart = [] 
            pref_legend = []
        
        print("")
        print("Charts more chosen by view: "+str(self.charts))
        for i in range(0,len(view)):
            print("View "+str(i+1)+": chart "+str(self.charts[view[i].index(max(view[i]))])+" was most chosen by "+str(max(view[i]))+" instructors. More details: "+str(view[i]))
            # print("View "+str(i+1)+": "+str(self.charts[view[i].index(max(view[i]))])+" Total: "+str(max(view[i])))
        print("")

        return view


    def chart_evaluation(self, columns=[], field_name=''):
        if columns==[]:
            print("Without columns")

        if len(self.legend) == 0:
            self.load_legends(columns=columns)

        # print(self.legend)
        values=[]
        # self.charts_evaluation=[]
        for i in range(0,len(columns)):
            values.append(self.dataset[columns[i]])
            self.charts_evaluation.append([[0 for j in range(len(self.likert))] for k in range(len(self.legend[i]))])
            
        for i in range(0,len(values[0])): #iterate in the lines
            # print("##########################################")
            # print("Instructor "+str(i+1))
            pref_chart = []
            pref_legend = []
            for j in range(0,len(columns)): 
                # print("V "+str(j+1))
                if str(values[j][i]) == "nan":
                    pref_chart.append(None)
                    pref_legend.append(None)
                else:
                    lst = values[j][i]
                    lst = ast.literal_eval(lst)
                    for k in range(0,len(lst)):
                        if lst[k]['field'] != field_name:
                            # print(lst[k]['field'])
                            # print(lst[k]['value'])
                            # print(self.likert.index(lst[k]['value']))
                            # print("")
                            self.charts_evaluation[j][k][self.likert.index(lst[k]['value'])] += 1
                            # self.charts_evaluation[view][chart][evaluate]
        
        print("Charts evaluation of each visualization: "+str(self.likert))
        for i in range(0,len(self.charts_evaluation)):
            for j in range(0,len(self.charts_evaluation[i])):
                print("V"+str(i+1)+"->Chart "+str(self.charts[j])+": "+str(self.charts_evaluation[i][j]))
            print("V"+str(i+1)+": "+str(len(self.charts_evaluation[i]))+" charts")
            print("")

        return self.chart_evaluation

columns = ['V001_1', 'V002_5', 'V003_7', 'V004_9', 'V005_11', 'V006_18', 'V007_23', 'V008_4', 'V009_8', 'V010_10', 'V011_22']
pref = preferences()
pref.load_legends(columns)
pref.preferences_chart(columns,"preference_chart")
pref.chart_evaluation(columns,"preference_chart")
