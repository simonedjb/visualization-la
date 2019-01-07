import os
import numpy as np
import pandas as pd
import ast

DB_PATH = "db/"
FILE_EXTENSION = ".csv"

class backend:

    _db = pd.DataFrame()
    _path_db = ""
    _language = "pt"
    _user = ""
    _lst_view_page = [] #List of page views selected
    _ordained_views = [{"View":"V001","Label":"Tarefas",
                        "Questions":[{"id":"1","Question":"Quais estudantes fizeram e não fizeram as tarefas?","Label":"Estudantes que fizeram e não fizeram as tarefas","Page":"prefv001_1"},
                                     {"id":"2","Question":"Quais tarefas foram e não foram feitas pelos estudantes?","Label":"Tarefas feitas e não feitas pelos estudantes","Page":"prefv001_2"}]
                       },
                       {"View":"V008","Label":"Acesso dos estudantes no AVA",
                        "Questions":[{"id":"3","Question":"Qual a quantidade de acesso dos estudantes por dia?","Label":"Quantidade de acesso dos estudantes por dia","Page":"prefv008_1"},
                                     {"id":"4","Question":"Qual a quantidade de acesso dos estudantes por semana?","Label":"Quantidade de acesso dos estudantes por semana","Page":"prefv008_2"}]
                       },
                       {"View":"V002","Label":"Acesso dos estudantes aos materiais (ex: videos, ebooks, etc)",
                        "Questions":[{"id":"5","Question":"Quais os estudantes que mais acessaram os materias?","Label":"Acesso dos estudantes aos materiais (ex: videos, ebooks, etc)","Page":"prefv002_1"},
                                     {"id":"6","Question":"Quais os materiais mais acessados pelos estudantes?","Label":"Materiais mais acessados pelos estudantes (ex: videos, ebooks, etc)","Page":"prefv002_1"}] #Falta fazer quais os materiais mais acessados pelos estudantes
                       },
                       {"View":"V003","Label":"Interação dos estudantes no fórum (ex: postagens, acessos, etc)",
                        "Questions":[{"id":"7","Question":"Qual o número de acessos, postagens e curtidas dos estudantes?","Label":"Número de acessos, postagens e curtidas dos estudantes","Page":"prefv003_1"}]
                       },
                       {"View":"V009","Label":"Interação dos estudantes nos vídeos (play, pause, seek backward, seek forward)",
                        "Questions":[{"id":"8","Question":"Como os alunos interagem no player de vídeo (play, pause, seek backward, seek forward)?","Label":"Interação dos estudantes nos vídeos (play, pause, seek backward, seek forward)","Page":"prefv009_1"}]
                       },
                       {"View":"V004","Label":"Tempo de permanência dos estudantes nos vídeos",
                        "Questions":[{"id":"9","Question":"Qual tempo de permanência dos estudantes nos vídeos?","Label":"Tempo de permanência dos estudantes nos vídeos","Page":"prefv004_1"}]
                       },
                       {"View":"V010","Label":"Entendimento dos vídeos pelos estudantes",
                        "Questions":[{"id":"10","Question":"Quais vídeos os estudantes entenderam e não entenderam?","Label":"Vídeos que os estudantes entenderam e não entenderam","Page":"prefv010_1"}]
                       },
                       {"View":"V005","Label":"Correlação entre as notas e os dados de acesso/interação dos estudantes",
                        "Questions":[{"id":"11","Question":"Qual a correlação entre as notas e os dados de acesso no AVA?","Label":"Correlação entre as notas e os dados de acesso no AVA","Page":"prefv005_1"},
                                     {"id":"12","Question":"Qual a correlação entre as notas e os dados de acesso nos AVAs materiais do AVA?","Label":"Correlação entre as notas e os dados de acesso nos AVAs materiais do AVA","Page":"prefv005_1"},
                                     {"id":"13","Question":"Qual a correlação entre as notas e a quantidade de tarefas feitas?","Label":"Correlação entre as notas e a quantidade de tarefas feitas","Page":"prefv005_1"},
                                     {"id":"14","Question":"Qual a correlação entre as notas e os dados de acesso no fórum?","Label":"Correlação entre as notas e os dados de acesso no fórum","Page":"prefv005_1"},
                                     {"id":"15","Question":"Qual a correlação entre as notas e a quantidade de postagens no fórum ?","Label":"Correlação entre as notas e a quantidade de postagens no fórum ","Page":"prefv005_1"},
                                     {"id":"16","Question":"Qual a correlação entre as notas e a quantidade de postagens de respostas no fórum ?","Label":"Correlação entre as notas e a quantidade de postagens de respostas no fórum ","Page":"prefv005_1"},
                                     {"id":"17","Question":"Qual a correlação entre as notas e a quantidade de tópicos adicionados no fórum?","Label":"Correlação entre as notas e a quantidade de tópicos adicionados no fórum","Page":"prefv005_1"}]
                       },
                       {"View":"V006","Label":"Correlação entre o perfil (idade, cidade de origem, etc.) e os logs de acesso/interação dos estudantes no fórum",
                        "Questions":[{"id":"18","Question":"Qual a correlação entre a idade dos alunos e os dados de acesso no Fórum?","Label":"Correlação entre a idade dos alunos e os dados de acesso no Fórum","Page":"prefv006_1"},
                                     {"id":"19","Question":"Qual a correlação entre a idade dos alunos e a quantidade de postagens no Fórum?","Label":"Correlação entre a idade dos alunos e a quantidade de postagens no Fórum","Page":"prefv006_1"},
                                     {"id":"20","Question":"Qual a correlação entre a idade dos alunos e a quantidade de postagens de respostas no Fórum?","Label":"Correlação entre a idade dos alunos e a quantidade de postagens de respostas no Fórum","Page":"prefv006_1"},
                                     {"id":"21","Question":"Qual a correlação entre a idade dos alunos e a quantidade de tópicos adicionados no fórum?","Label":"Correlação entre a idade dos alunos e a quantidade de tópicos adicionados no fórum","Page":"prefv006_1"}]
                       },
                       {"View":"V011","Label":"Padrão de navegação dos estudantes no AVA",
                        "Questions":[{"id":"22","Question":"Qual o padrão de navegação dos estudantes no AVA?","Label":"Padrão de navegação dos estudantes no AVA","Page":"prefv011_1"}]
                       },
                       {"View":"V007","Label":"Predição das notas e dos estudantes desistentes",
                        "Questions":[{"id":"23","Question":"Qual a previsão de notas e dos estudantes desistentes?","Label":"Predição das notas e dos estudantes desistentes","Page":"prefv007_1"}]
                       }
                      ]

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
               {"db":"programming_last_time", "system":"user_programming_last_time"}, #última vez que programou
               {"db":"programming_language", "system":"user_programming_language"}, #linguagem que programou pela última vez
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
               {"db":"V001_1", "system":"user_V001_1"}, #<-
               {"db":"comments_V001_1", "system":"comments_id_chart_v001_1"},
               {"db":"V001_2", "system":"user_V001_2"}, #<-
               {"db":"comments_V001_2", "system":"comments_id_chart_v001_2"},
               {"db":"V002_5", "system":"user_V002_5"}, #<-
               {"db":"comments_V002_5", "system":"comments_id_chart_v002_5"},
               {"db":"V003_7", "system":"user_V003_7"}, #<-
               {"db":"comments_V003_7", "system":"comments_id_chart_v003_7"},
               {"db":"V004_9", "system":"user_V004_9"}, #<-
               {"db":"comments_V004_9", "system":"comments_id_chart_v004_9"},
               {"db":"V005_11", "system":"user_V005_11"}, #<-
               {"db":"comments_V005_11", "system":"comments_id_chart_v005_11"},
               {"db":"V006_18", "system":"user_V006_18"}, #<-
               {"db":"comments_V006_18", "system":"comments_id_chart_v006_18"},
               {"db":"V007_23", "system":"user_V007_23"}, #<-
               {"db":"comments_V007_23", "system":"comments_id_chart_v007_23"},
               {"db":"V008_3", "system":"user_V008_3"}, #<-
               {"db":"comments_V008_3", "system":"comments_id_chart_v008_3"},
               {"db":"V008_4", "system":"user_V008_4"}, #<-
               {"db":"comments_V008_4", "system":"comments_id_chart_v008_4"},
               {"db":"V009_8", "system":"user_V009_8"}, #<-
               {"db":"comments_V009_8", "system":"comments_id_chart_v009_8"},
               {"db":"V010_10", "system":"user_V010_10"}, #<-
               {"db":"comments_V010_10", "system":"comments_id_chart_v010_10"},
               {"db":"V011_22", "system":"user_V011_22"}, #<-
               {"db":"comments_V011_22", "system":"comments_id_chart_v011_22"},
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
        print("Loading DB")

        self._user = email
        self._path_db = os.path.join(DB_PATH,self._user+FILE_EXTENSION)
        self._db = pd.read_csv(self._path_db)
        self.load_lst_view()

    def db_has_database(self, email=None):
        if email == None:
            if len(self._db) == 0:
                return False
        else:
            path = os.path.join(DB_PATH,email+FILE_EXTENSION)
            if not os.path.exists(path):
                return False
        
        return True

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

    def load_lst_view(self):
        self.clear_lst_view()
        if not str(self.db_select_value(["user_interaction_access_students_logs"])[0]) == "nan":
            lst = ast.literal_eval(self.db_select_value(["user_interaction_access_students_logs"])[0])
            print(lst)
            if len(lst) > 0:
                lst_sorted = sorted(lst)
                for i in range(0,len(lst_sorted)):
                    val = lst_sorted[i]
                    print(val)
                    view = val.split('_')[0]
                    id_view = val.split('_')[1]
                    self.add_view_page_preference(self.get_view_page_question_view(view,id_view))
                
                print("Pages: ")
                print(self._lst_view_page)
        
    def clear_lst_view(self):
        self._lst_view_page = []

    def add_view_page_preference(self, page): #adding all view preferences
        if not page in self._lst_view_page:
            self._lst_view_page.append(page)

    def get_view_page_preference(self):
        return self._lst_view_page

    def has_next_page(self, current_view = None):
        if current_view == None:
            if len(self._lst_view_page) > 0:
                return True

        if current_view in self._lst_view_page:
            if (self._lst_view_page.index(current_view)+1) < len(self._lst_view_page):
                return True
        
        return False

    def get_next_page(self, current_view = None):
        if current_view == None:
            return self._lst_view_page[0]
        return self._lst_view_page[self._lst_view_page.index(current_view)+1]

    def get_view(self):
        lst = []
        for i in range(0,len(self._ordained_views)):
            lst.append(self._ordained_views[i]["View"])
        return lst

    def get_view_label_view(self, current_view):
        for i in range(0,len(self._ordained_views)):
            if self._ordained_views[i]["View"] == current_view:
                return self._ordained_views[i]["Label"]

        return None

    def get_view_question_view(self, current_view):
        lst = []
        for i in range(0,len(self._ordained_views)):
            if self._ordained_views[i]["View"] == current_view:
                questions = self._ordained_views[i]["Questions"]
                for j in range(0,len(questions)):
                    lst.append(questions[j]["Question"])
                return lst

        return None

    def get_view_label_question_view(self, current_view, current_question):
        for i in range(0,len(self._ordained_views)):
            if self._ordained_views[i]["View"] == current_view:
                questions = self._ordained_views[i]["Questions"]
                for j in range(0,len(questions)):
                    if questions[j]["Question"] == current_question: 
                        return questions[j]["Label"]
        return None

    def get_view_page_question_view(self, current_view, id):
        for i in range(0,len(self._ordained_views)):
            if self._ordained_views[i]["View"] == current_view:
                questions = self._ordained_views[i]["Questions"]
                for j in range(0,len(questions)):
                    if questions[j]["id"] == id: 
                        return questions[j]["Page"]
        return None

    def get_view_id_question_view(self, current_view, current_question):
        for i in range(0,len(self._ordained_views)):
            if self._ordained_views[i]["View"] == current_view:
                questions = self._ordained_views[i]["Questions"]
                for j in range(0,len(questions)):
                    if questions[j]["Question"] == current_question:
                        return questions[j]["id"]
        return None

    def get_view_question_page_view(self, current_view, page):
        for i in range(0,len(self._ordained_views)):
            if self._ordained_views[i]["View"] == current_view:
                questions = self._ordained_views[i]["Questions"]
                for j in range(0,len(questions)):
                    if questions[j]["Page"] == page:
                        return questions[j]["Question"]
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

    def record_data(self, user = None, data = []):
        if user == None:
            return False
        
        fields = []
        values = []
        
        load_views = False
        
        for i in range(0,len(data)):
            fields.append(data[i]["field"])
            values.append(data[i]["value"])
            if(data[i]["field"] == "user_interaction_access_students_logs"):
                load_views = True
            
        self.db_adding_value(fields,values)
        if load_views:
            self.db_load_database(self._user)

        return True

    def load_frontend_data(self,field,data=[]):
        for i in range(0,len(data)):
            if(data[i]["field"] == field):
                return data[i]['value']
        
        return ""

    def load_frontend_data_view(self,id_view,field,data=[]):
        lst = []
        for i in range(0,len(data)):
            if(data[i]["field"] == id_view):
                lst = data[i]['value']
                for j in range(0,len(lst)):
                    if(lst[j]["field"] == field):
                        return lst[j]['value']

        return ""


# import os
# import numpy as np
# import pandas as pd
# from backend import backend
# control = backend.backend()
# control.db_load_database("andrelbd1@gmail.com")
# df = control.get_db()



# lst = ["V010","V001","V007"] 
# control = backend.backend()
# control.add_view_page_preference(lst)

# aux = pd.DataFrame(columns=["name","email"])
# aux["email"] = ["foo@gmail.com"]
# df = df.append(aux, sort=False, ignore_index=True)