import pandas as pd
import os, sys
import json

from app.eduvis.backend.connection_db import Connection_DB

class User:
    _user_id = None
    _dashboard_id = None
    _dashboard_type = None
    _conn = Connection_DB()

    def __init__(self,conn,user_id,dashboard_id,dashboard_type):
        self._conn = conn
        self._user_id = user_id
        self._dashboard_id = dashboard_id
        self._dashboard_type = dashboard_type        

    def get_name(self):
        res_db = self._conn.select("user",(int(self._user_id),))
        name = res_db[0][1]
        return name