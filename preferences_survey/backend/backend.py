import os
import numpy as np
import pandas as pd

DB_PATH = "db/"
FILE_EXTENSION = ".csv"

class backend:

    _db = pd.DataFrame()
    _path_db = ""
    _language = "pt"
    _lst_view_name = [] #List of views selected
    _ordained_views = [{"View":"V001","Label":"Tarefas feitas pelos estudantes","Page":"assignsdone"},
                       {"View":"V008","Label":"Acesso dos estudantes no AVA por dia ou semana","Page":"avaaccess"},
                       {"View":"V002","Label":"Acesso dos estudantes aos materiais (ex: videos, ebooks, etc)","Page":"accessmaterials"},
                       {"View":"V003","Label":"Interação dos estudantes no fórum (ex: postagens, acessos, etc)","Page":"foruminteraction"},
                       {"View":"V009","Label":"Interação dos estudantes nos vídeos (play, pause, backward, forward)","Page":"videointeraction"},
                       {"View":"V004","Label":"Tempo de permanência dos estudantes nos vídeos","Page":"videostay"},
                       {"View":"V010","Label":"Vídeos que os estudantes entenderam e não entenderam","Page":"understandingvideo"},
                       {"View":"V005","Label":"Correlação entre as notas e os logs de acesso/interação dos estudantes","Page":"correlationgrade"},
                       {"View":"V006","Label":"Correlação entre o perfil (idade, cidade de origem, etc.) e os logs de acesso/interação dos estudantes","Page":"correlationprofile"},
                       {"View":"V011","Label":"Padrão de navegação dos estudantes no AVA","Page":"navigatepattern"},
                       {"View":"V007","Label":"Predição das notas que os estudante terão ao final do curso e quais abandonarão","Page":"gradeprediction"},
                       {"View":"None","Label":"Nenhuma das opções","Page":"None"}]

    _fields = [{"db":"name", "system":"user_name"}, #nome completo
               {"db":"email", "system":"user_email"}, #email
               {"db":"ead_xp", "system":"user_ead_xp"}, #experiência com ead
               {"db":"gender", "system":"user_gender"}, #gênero
               {"db":"age", "system":"user_age"}, #idade
               {"db":"place_birth", "system":"user_place_birth"}, #local de nascimento
               {"db":"place_work", "system":"user_place_work"}, #local de trabalho
               {"db":"scholarship", "system":"user_scholarship"}, #formação
               {"db":"scholarship_degree", "system":"user_scholarship_degree"}, #grau de formação
               {"db":"job", "system":"user_job"}, #profissão
               {"db":"programming_xp", "system":"user_programming_xp"}, #experiência com programação
               {"db":"job_ead", "system":"user_job_ead"}, #papeis desempenhados na utilização do AVAs
               {"db":"time_AVA_xp", "system":"user_time_experience"}, #tempo de experiência na utilização de AVAs
               {"db":"organization_worked", "system":"user_organization_worked"}, #instituições de ensino que trabalha (e que trabalhou) utilizando AVAs
               {"db":"subjects", "system":"user_subject"}, #disciplinas ensinadas utilizando AVAs
               {"db":"ead_modality_xp", "system":"user_ead_modality"}, #Experiência com qual modalidade de ensino utilizando AVAS
               {"db":"avas_xp", "system":"user_avas_performed"}, #AVAs que utiliza (e que já utilizou)
               {"db":"avas_resources", "system":"user_avas_resources"}, #recursos que utiliza e já utilizou nos AVAs
               {"db":"students_age", "system":"user_students_age"}, #faixa etária dos alunos que ensina (e que já ensinou) utilizando AVAs
               {"db":"students_scholarship", "system":"user_students_scholarship"}, #área de formação dos alunos que ensina (e que já ensinou) utilizando AVAs
               {"db":"students_scholarship_degree", "system":"user_students_scholarship_degree"}, #grau de escolaridade desses alunos
               {"db":"students_meaningful", "system":"user_students_meaningful"}, #informações dos alunos você considera relevante
               {"db":"students_progress", "system":"user_students_progress"}, #como você acompanha o andamento dos alunos durante o curso
               {"db":"logs_analyse", "system":"user_logs_analyse"}, #quais dados você analisa
               {"db":"logs_presentation", "system":"user_logs_presentation"}, #como esses dados são apresentados pra você
               {"db":"logs_performance", "system":"user_logs_performance"}, #quais dados podem ser utilizados para predizer as notas dos alunos
               {"db":"logs_dropout", "system":"user_logs_dropout"}, #quais dados podem ser utilizados para predizer se o aluno irá abandonar o curso
               {"db":"logs_engagement", "system":"user_logs_engagement"}, #quais dados podem ser utilizados para avaliar o engajamento do aluno
               {"db":"selected_views", "system":"user_interaction_access_students_logs"}, #dados que você analisa ou que gostaria de analisar
               {"db":"other_views", "system":"user_interaction_access_students_logs_others"}, #dado que você analisa (ou gostaria de analisar) e que não foi apresentada
               {"db":"presenting_views", "system":"user_interaction_access_students_logs_presentation"}, #como você gostaria que esses dados fossem apresentados
               {"db":"freq_view_read", "system":"user_view_read"}, #com que frequencia você lê e interpreta gráficos
               {"db":"freq_view_make", "system":"user_view_make"}, #com que frequencia você cria gráficos
               {"db":"date_start", "system":"date_start_cache"}, #data de início do survey
               {"db":"date_end", "system":"date_end_cache"}, #data de início do survey
               {"db":"last_page", "system":"page"}, #última tela do formulário respondida no survey
               ]

    def __init__(self, language="pt", email=None):
        self.set_language(language)

        if not email == None:
            path = os.path.join(DB_PATH,email+FILE_EXTENSION)
            if not os.path.exists(path):
                self.db_make_database(email)
            else:
                self.db_load_database(email)

    def set_language(self, language):
        self._language = language

    def db_make_database(self, email):
        self._path_db = os.path.join(DB_PATH,email+FILE_EXTENSION)

        lst = []
        for i in range(0,len(self._fields)):
            lst.append(self._fields[i]["db"])
        
        print("Making DB")

        self._db = pd.DataFrame(columns=lst)
        self._db["email"] = [email]
        self._db.to_csv(self._path_db, index=False)

    def db_load_database(self, email):
        self._path_db = os.path.join(DB_PATH,email+FILE_EXTENSION)
        self._db = pd.read_csv(self._path_db)

    def db_has_database(self, email=None):
        if email == None:
            if len(self._db) == 0:
                return False
        else:
            path = os.path.join(DB_PATH,email+FILE_EXTENSION)
            if not os.path.exists(path):
                return False
        
        return True

    def db_adding_value_json(self, json_var): #adding values in the database using json
        fields = []
        values = []
        
        self.db_adding_value(fields,values)

    def db_adding_value(self, fields, values): #adding values in the database
        for i in range(0,len(fields)):
            column = self.get_relate_column_dabase(fields[i])
            value = values[i]
            self._db[column].loc[0] = value

        self._db.to_csv(self._path_db, index=False)

    def db_select_value(self, fields): #return values of the database
        columns = []
        for i in range(0,len(fields)):
            columns.append(self.get_relate_column_dabase(fields[i]))

        return self._db[columns].values.tolist()[0]

    def get_db(self):
        return self._db

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

    def get_relate_column_dabase(self, field):
        for i in range(0,len(self._fields)):
            if self._fields[i]["system"] == field:
                return self._fields[i]["db"]

        return None

    def get_relate_field_system(self, column):
        for i in range(0,len(self._fields)):
            if self._fields[i]["db"] == column:
                return self._fields[i]["system"]

        return None

# import os
# import numpy as np
# import pandas as pd
# from backend import backend
# control = backend.backend()
# control.db_make_database("andrelbd1@gmail.com")
# df = control.get_db()
# df["email"] = ["andrelbd1@gmail.com"]


# lst = ["V010","V001","V007"] 
# control = backend.backend()
# control.add_view_preference(lst)

# aux = pd.DataFrame(columns=["name","email"])
# aux["email"] = ["foo@gmail.com"]
# df = df.append(aux, sort=False, ignore_index=True)