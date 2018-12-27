import numpy as np
import pandas as pd

class backend:

    _language = "pt"
    _lst_view_name = [] #List of views selected
    _ordained_views = [{"View":"V001","Label":"Tarefas feitas pelos estudantes","Page":"assignsdone"},
                       {"View":"V008","Label":"Acesso dos estudantes no AVA por dia ou semana","Page":"avaaccess"},
                       {"View":"V002","Label":"Acesso dos estudantes aos materiais (ex: videos, ebooks, etc)","Page":"accessmaterials"},
                       {"View":"V003","Label":"Interação dos estudantes no fórum (ex: postagens, acessos, etc)","Page":"foruminteraction"},
                       {"View":"V009","Label":"Interação dos estudantes nos vídeos (play, pause, backward, forward)","Page":"videointeraction"},
                       {"View":"V004","Label":"Tempo de permanencia dos estudantes nos vídeos","Page":"videostay"},
                       {"View":"V010","Label":"Vídeos que os estudantes entenderam e não entenderam","Page":"understandingvideo"},
                       {"View":"V005","Label":"Correlação entre as notas e os logs de acesso/interação dos estudantes","Page":"correlationgrade"},
                       {"View":"V006","Label":"Correlação entre o perfil (idade, cidade de origem, etc.) e os logs de acesso/interação dos estudantes","Page":"correlationprofile"},
                       {"View":"V011","Label":"Padrão de navegação dos estudantes no AVA","Page":"navigatepattern"},
                       {"View":"V007","Label":"Predição das notas que os estudante terão ao final do curso e quais abandonarão","Page":"gradeprediction"}]

    def __init__(self, language = "pt"):
        self.set_language(language)

    def set_language(self,language):
        self._language = language

    def clear(self):
        self._lst_view_name = []

    def add_view_preference(self, lst_view): #adding all view preferences
        lst_views = self.get_all_view_names()
        for i in range(0,len(lst_views)):
            if lst_views[i] in lst_view:
                self._lst_view_name.append(lst_views[i])

    def get_view_preference(self):
        return self._lst_view_name

    def has_next_view(self, current_view = None):
        if current_view == None:
            if len(self._lst_view_name) > 0:
                return True

        if current_view in self._lst_view_name:
            if (self._lst_view_name.index(current_view)+1) < len(self._lst_view_name):
                return True
        
        return False

    def get_next_view(self, current_view = None):
        if current_view == None:
            return self._lst_view_name[0]
        return self._lst_view_name[self._lst_view_name.index(current_view)+1]

    def get_next_page(self, current_view = None):
        return self.get_view_page(self.get_next_view(current_view))

    def get_all_view_names(self):
        lst = []
        for i in range(0,len(self._ordained_views)):
            lst.append(self._ordained_views[i]["View"])
        return lst

    def get_view_label(self, current_view):
        for i in range(0,len(self._ordained_views)):
            if self._ordained_views[i]["View"] == current_view:
                return self._ordained_views[i]["Label"]

        return None

    def get_view_page(self, current_view):
        for i in range(0,len(self._ordained_views)):
            if self._ordained_views[i]["View"] == current_view:
                return self._ordained_views[i]["Page"]

        return None

# from backend import backend
# control = backend.backend()
# lst = ["V010","V001","V007"] 
# control = backend.backend()
# control.add_view_preference(lst)
