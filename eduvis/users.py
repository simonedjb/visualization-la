import os
import pandas as pd
import numpy as np

from six.moves import urllib
from pathlib import Path

class users:
    DIR_PATH = 'db'
    FILE_USER_PATH = 'users.csv'
    FILE_PROFILE_PATH = 'profile.csv'

    _users = pd.DataFrame()
    _profile = pd.DataFrame()
    _id_session = 0

    def __init__(self, user_id = 0):
        users_path = os.path.join(self.DIR_PATH,self.FILE_USER_PATH)
        
        profile_path = os.path.join(self.DIR_PATH,self.FILE_PROFILE_PATH)
        self._profile = pd.read_csv(profile_path,sep=';')
        
        if not os.path.exists(users_path):
            columns = ["v"+str(i+1) for i in range (0, 11)]
            columns.insert(0,"id")
            columns.insert(1,"name")
            columns.insert(2,"username")
            columns.insert(3,"password")
            columns.insert(4,"language")

            self._users = pd.DataFrame(columns=columns)
            self._users.to_csv(users_path,index=False)

        else:
            self._users = pd.read_csv(users_path,sep=';')

        if user_id != 0:
            self.sign_in (user_id=user_id)


    def sign_in(self, username="", password="", user_id=0):
        if user_id != 0:
            if len(self._users.loc[(self._users.id == user_id)]) > 0:
                self._id_session = user_id
                return True
            else:
                return False
        
        if username != "" :
            if len(self._users.loc[(self._users.username == username) & (self._users.password == password)]) > 0:
                self._id_session = self._users.id.loc[(self._users.username == username) & (self._users.password == password)]
                return True

            else:
                return False

        return False

    def get_session(self):
        return self._id_session

    def has_session(self):
        if self._id_session == 0 :
            return False
        
        return True

    def user_graph_preference(self, view = None):
        if not np.isnan(sum(self._users[view].loc[self._users.id == self._id_session].tolist())):
            return self._users[view].loc[self._users.id == self._id_session]
        
        profile = self._users.profile.loc[self._users.id == self._id_session].to_string(index=False)
        return self._profile[view].loc[self._profile.id == int(profile)].tolist()

    def user_language_preference(self,language = None):
        if language == None:
            return self._users.language.loc[self._users.id == self._id_session].to_string(index=False)


# import users
# user = users.users(user_id = 2)
# user._users
# user._users["v1"].loc[user._users.id == 2]


# user._users.profile.loc[user._users.id == 2].to_string(index=False)

# user._profile["v1"].loc[user._profile.id == profile].tolist()

