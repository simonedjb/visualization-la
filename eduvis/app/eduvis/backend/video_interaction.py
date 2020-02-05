import pandas as pd
import os, sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath("visualizations"))))

from app.eduvis.backend.connection_db import Connection_DB
from visualizations import V009

class Video_Interaction:
    _user_id = None
    _dashboard_id = None
    _dashboard_type = None
    _conn = Connection_DB()
    _students = pd.DataFrame()
    _view9 = V009.V009(type_result = "flask",language = "pt")    

    def __init__(self,conn,user_id,dashboard_id,dashboard_type):
        self._conn = conn
        self._user_id = user_id
        self._dashboard_id = dashboard_id
        self._dashboard_type = dashboard_type
        self._students = pd.read_csv("app/eduvis/names.csv")

        self._view9.generate_dataset(number_actions = 100, video_size = 30, students_names = self._students)
    
    def title(self):
        res = None
        # Interação dos estudantes nos vídeos (play, pause, seek backward, seek forward) # 9.1 # T21
        res = self._conn.select("topics",(21,))
        return res[0][0]

    def topic(self):
        return "T21"

    def charts(self,focus_chart): # focus_chart ["id","layout"]):
        lst_charts = []
        lst_charts = self._conn.select("topics_charts",(21,))
         
        print(lst_charts)
        charts = []
        for i in range(0, len(lst_charts)):
            curr = lst_charts[i][0].split("@")            
            id = int(curr[1])
            # print(id)
            charts.append(self._view9.get_chart(id)[focus_chart])

        # Interação dos estudantes nos vídeos (play, pause, seek backward, seek forward) # 9.1 # T21
        # charts = [self._view9.graph_01()[focus_chart], #1
        #           self._view9.graph_02()[focus_chart], #2
        #           self._view9.graph_03()[focus_chart], #3
        #           self._view9.graph_05()[focus_chart], #4
        #          ]

        return charts

    def charts_active(self):
        topic_id = 21 # Interação dos estudantes nos vídeos (play, pause, seek backward, seek forward) # 9.1 # T21
        
        charts_value = []
        res_db = self._conn.select("user_dashboard_charts_active_by_topic",(self._user_id, self._dashboard_id, self._dashboard_type, topic_id))
        for i in range(0,len(res_db)):
            charts_value.append(res_db[i][6])

        return charts_value