from flask import Blueprint, request, render_template, flash, Response, g, session, redirect, url_for
from flask_wtf import Form
from sqlalchemy import and_, update

import json
import plotly
import plotly.plotly as py
import plotly.graph_objs as go

import numpy as np

import dateutil.parser
from datetime import datetime
from dateutil.relativedelta import relativedelta

# local application imports
from app.eduvis.constants import DEFAULT_USER_ID
from app.eduvis.constants import DEFAULT_STATIC_DASHBOARD_ID
from app.eduvis.constants import DEFAULT_CUSTOMIZABLE_DASHBOARD_ID
from app.eduvis.constants import STATIC_DASHBOARD_TYPE
from app.eduvis.constants import CUSTOMIZABLE_DASHBOARD_TYPE

# from app import db
from app.eduvis.backend.dashboard import Dashboard
from app.eduvis.backend.connection_db import Connection_DB

from app.eduvis.backend.user import User

from app.eduvis.backend.access import Access
from app.eduvis.backend.assignment import Assignment
from app.eduvis.backend.cluster import Cluster
from app.eduvis.backend.prediction import Prediction
from app.eduvis.backend.material import Material
from app.eduvis.backend.forum import Forum
from app.eduvis.backend.video_access import Video_Access
from app.eduvis.backend.age import Age
from app.eduvis.backend.video_interaction import Video_Interaction
from app.eduvis.backend.video_understood import Video_Understood
from app.eduvis.backend.navigation import Navigation


mod = Blueprint("eduvis", __name__, url_prefix='/eduvis')

_conn = Connection_DB()

_user_id = None
_static_dashboard_id = None
_customizable_dashboard_id = None

def load_user_info():
    global _user_id
    global _static_dashboard_id
    global _customizable_dashboard_id
    
    _user_id = DEFAULT_USER_ID
    _static_dashboard_id = DEFAULT_STATIC_DASHBOARD_ID
    _customizable_dashboard_id = DEFAULT_CUSTOMIZABLE_DASHBOARD_ID
    
    # print("--------------------------------------------------")
    # print("load_user_info()")
    # print((_user_id, _static_dashboard_id, _customizable_dashboard_id))
    # print("--------------------------------------------------")

def view_information():
    lst_view_information = []
    lst_view_information.append({"View":"V001","Topic":"Tarefas", "id":"assignments", "Label_pt":"Atividades", "Label_en":"Assignments completion",
                                 "Questions":[{"id":"1","Question":"Quais estudantes fizeram e não fizeram as tarefas?","Sub_topic":"Estudantes que fizeram e não fizeram as tarefas","Label_pt":"estudantes que completaram"},
                                              {"id":"2","Question":"Quais tarefas foram e não foram feitas pelos estudantes?","Sub_topic":"Tarefas feitas e não feitas pelos estudantes","Label_pt":"atividades completadas"}]})
    lst_view_information.append({"View":"V002","Topic":"Acesso dos estudantes aos materiais (ex: videos, ebooks, etc)", "id":"materials", "Label_pt": "Materiais acessados", "Label_en": "Materials accessed",
                                 "Questions":[{"id":"3","Question":"Quais os estudantes que mais acessaram os materias?","Sub_topic":"Acesso dos estudantes aos materiais (ex: videos, ebooks, etc)","Label_pt":"estudantes que acessaram"},
                                              {"id":"4","Question":"Quais os materiais mais acessados pelos estudantes?","Sub_topic":"Materiais mais acessados pelos estudantes (ex: videos, ebooks, etc)","Label_pt":"materiais mais acessados"}]}) #Falta fazer quais os materiais mais acessados pelos estudantes
    lst_view_information.append({"View":"V003","Topic":"Interação dos estudantes no fórum (ex: postagens, acessos, etc)", "id":"forum", "Label_pt": "Uso do fórum", "Label_en": "Forum usage",
                                 "Questions":[{"id":"5","Question":"Qual o número de acessos, postagens e curtidas dos estudantes?","Sub_topic":"Número de acessos, postagens e curtidas dos estudantes","Label_pt":"Uso do fórum"}]})
    lst_view_information.append({"View":"V004","Topic":"Tempo de permanência dos estudantes nos vídeos", "id":"video_access", "Label_pt": "Videos accessados", "Label_en": "Video accessed",
                                 "Questions":[{"id":"6","Question":"Qual tempo de permanência dos estudantes nos vídeos?","Sub_topic":"Tempo de permanência dos estudantes nos vídeos","Label_pt":"Videos accessados"}]})
    lst_view_information.append({"View":"V005","Topic":"Correlação entre as notas e os dados de acesso/interação dos estudantes", "id":"cluster", "Label_pt": "Correlação entre notas", "Label_en": "Student clusters",
                                 "Questions":[{"id":"7","Question":"Qual a correlação entre as notas e os dados de acesso no AVA?","Sub_topic":"Correlação entre as notas e os dados de acesso no AVA","Label_pt":"acessos ao ambiente"},
                                              {"id":"8","Question":"Qual a correlação entre as notas e os dados de acesso nos AVAs materiais do AVA?","Sub_topic":"Correlação entre as notas e os dados de acesso nos AVAs materiais do AVA","Label_pt": "materiais acessados"},
                                              {"id":"9","Question":"Qual a correlação entre as notas e a quantidade de tarefas feitas?","Sub_topic":"Correlação entre as notas e a quantidade de tarefas feitas","Label_pt": "atividades completadas"},
                                              {"id":"10","Question":"Qual a correlação entre as notas e os dados de acesso no fórum?","Sub_topic":"Correlação entre as notas e os dados de acesso no fórum","Label_pt":"acesso ao fórum"},
                                              {"id":"11","Question":"Qual a correlação entre as notas e a quantidade de postagens no fórum ?","Sub_topic":"Correlação entre as notas e a quantidade de postagens no fórum ","Label_pt":"postagens no fórum"},
                                              {"id":"12","Question":"Qual a correlação entre as notas e a quantidade de postagens de respostas no fórum ?","Sub_topic":"Correlação entre as notas e a quantidade de postagens de respostas no fórum ","Label_pt":"respostas no fórum"},
                                              {"id":"13","Question":"Qual a correlação entre as notas e a quantidade de tópicos adicionados no fórum?","Sub_topic":"Correlação entre as notas e a quantidade de tópicos adicionados no fórum","Label_pt":"tópicos no fórum"}]})
    lst_view_information.append({"View":"V006","Topic":"Correlação entre o perfil (idade, cidade de origem, etc.) e os logs de acesso/interação dos estudantes no fórum", "id":"age", "Label_pt": "Correlação entre idade", "Label_en": "Student profiles",
                                 "Questions":[{"id":"14","Question":"Qual a correlação entre a idade dos alunos e os dados de acesso no Fórum?","Sub_topic":"Correlação entre a idade dos alunos e os dados de acesso no Fórum","Label_pt":"acesso ao fórum"},
                                              {"id":"15","Question":"Qual a correlação entre a idade dos alunos e a quantidade de postagens no Fórum?","Sub_topic":"Correlação entre a idade dos alunos e a quantidade de postagens no Fórum","Label_pt":"postagens no fórum"},
                                              {"id":"16","Question":"Qual a correlação entre a idade dos alunos e a quantidade de postagens de respostas no Fórum?","Sub_topic":"Correlação entre a idade dos alunos e a quantidade de postagens de respostas no Fórum","Label_pt":"respostas no fórum"},
                                              {"id":"17","Question":"Qual a correlação entre a idade dos alunos e a quantidade de tópicos adicionados no fórum?","Sub_topic":"Correlação entre a idade dos alunos e a quantidade de tópicos adicionados no fórum","Label_pt":"tópicos no fórum"}]})
    lst_view_information.append({"View":"V007","Topic":"Predição das notas e dos estudantes desistentes", "id":"prediction", "Label_pt": "Predição de performance", "Label_en": "Performance prediction",
                                 "Questions":[{"id":"18","Question":"Qual a previsão de notas e dos estudantes desistentes?","Sub_topic":"Predição das notas e dos estudantes desistentes","Label_pt":"Predição de performance"}]})
    lst_view_information.append({"View":"V008","Topic":"Acesso dos estudantes no AVA", "id":"access", "Label_pt": "Acesso dos estudantes", "Label_en": "Student access",
                                 "Questions":[{"id":"19","Question":"Qual a quantidade de acesso dos estudantes por dia?","Sub_topic":"Quantidade de acesso dos estudantes por dia","Label_pt":"acessos por dia"},
                                              {"id":"20","Question":"Qual a quantidade de acesso dos estudantes por semana?","Sub_topic":"Quantidade de acesso dos estudantes por semana","Label_pt":"acessos por semana"}]})
    lst_view_information.append({"View":"V009","Topic":"Interação dos estudantes nos vídeos (play, pause, seek backward, seek forward)", "id":"video_interaction", "Label_pt": "Interação no vídeo", "Label_en": "Video interaction",
                                 "Questions":[{"id":"21","Question":"Como os alunos interagem no player de vídeo (play, pause, seek backward, seek forward)?","Sub_topic":"Interação dos estudantes nos vídeos (play, pause, seek backward, seek forward)","Label_pt":"Interação no vídeo"}]})
    lst_view_information.append({"View":"V010","Topic":"Entendimento dos vídeos pelos estudantes", "id":"video_understood", "Label_pt": "Entendimento do vídeo", "Label_en": "Video understood",
                                 "Questions":[{"id":"22","Question":"Quais vídeos os estudantes entenderam e não entenderam?","Sub_topic":"Vídeos que os estudantes entenderam e não entenderam","Label_pt":"Entendimento do vídeo"}]})
    lst_view_information.append({"View":"V011","Topic":"Padrão de navegação dos estudantes no AVA", "id":"navigation", "Label_pt": "Navegação dos estudantes", "Label_en": "Student navigation",
                                 "Questions":[{"id":"23","Question":"Qual o padrão de navegação dos estudantes no AVA?","Sub_topic":"Padrão de navegação dos estudantes no AVA","Label_pt":"Navegação dos estudantes"}]})
    return lst_view_information
                      

def left_menu_info_UNASUS():
    lst_left_menu_info = []
    lst_left_menu_info.append({"id":"assignments", "label_pt":"Atividades", "label_en":"Assignments completion", "sub_menu":["atividades completadas", "estudantes que completaram"], "view":1})
    lst_left_menu_info.append({"id":"materials", "label_pt":"Materiais acessados", "label_en":"Materials accessed", "sub_menu":["estudantes que acessaram", "materiais mais acessados"], "view":2})
    lst_left_menu_info.append({"id":"forum", "label_pt":"Uso do fórum", "label_en":"Forum usage", "sub_menu":[], "view":3})
    lst_left_menu_info.append({"id":"cluster", "label_pt":"Correlação entre notas", "label_en":"Student clusters", "sub_menu":["acessos ao ambiente", "atividades completadas", "materiais acessados", "acesso ao fórum", "postagens no fórum"], "view":5})
    lst_left_menu_info.append({"id":"prediction", "label_pt":"Predição de performance", "label_en":"Performance prediction", "sub_menu":[], "view":7})
    lst_left_menu_info.append({"id":"access", "label_pt":"Acesso dos estudantes", "label_en":"Student access", "sub_menu":["acessos por dia", "acessos por semana"], "view":8})

    # sorted_list = sorted(lst_left_menu_info, key=lambda k: k['label_en'])
    sorted_list = sorted(lst_left_menu_info, key=lambda k: k['label_pt'])
    return sorted_list

def left_menu_info():
    lst = view_information()
    
    lst_left_menu_info = []
    for i in range(len(lst)):
        sub_menu=[]
        lst_question = lst[i]["Questions"]
        if len(lst_question) > 1:
            for j in range(len(lst_question)):
                sub_menu.append(lst_question[j]["Label_pt"])

        curr_dict = {"id":lst[i]["id"], "label_pt":lst[i]["Label_pt"], "label_en":lst[i]["Label_en"],"view":int(lst[i]["View"].replace("V","")),"sub_menu":sub_menu}

        lst_left_menu_info.append(curr_dict)

    # sorted_list = sorted(lst_left_menu_info, key=lambda k: k['label_en'])
    sorted_list = sorted(lst_left_menu_info, key=lambda k: k['label_pt'])
    return sorted_list

@mod.before_request
def before_request():
    # app_before_request()
    load_user_info()

@mod.route('/')
def index():
    # Redirecionar para a tela de entrevista inicial
    return redirect('/eduvis/invite/')
    # return redirect('/eduvis/interview/aboutyou/')
    # return redirect('/eduvis/interview/avaxp/')
    # return redirect('/eduvis/interview/data/')
    # return redirect('/eduvis/dashboard/')

@mod.route('/invite/')
def invite():
    return render_template('eduvis/frontend/invite.html')

@mod.route('/post_invite/', methods=['POST'])
def invite_data():
    if request.method == 'POST':
        print("--------------------------------post_invite--------------------------------")
    else:
        pass
    
    return redirect('/eduvis/interview/aboutyou/')

@mod.route('/interview/aboutyou/')
def aboutyou():
    return render_template('eduvis/frontend/interview/aboutyou.html')

@mod.route('/interview/post_aboutyou/', methods=['POST'])
def aboutyou_data():
    if request.method == 'POST':
        print("--------------------------------post_aboutyou--------------------------------")
    else:
        pass
    
    return redirect('/eduvis/interview/avaxp/')

@mod.route('/interview/avaxp/')
def avaxp():
    return render_template('eduvis/frontend/interview/avaxp.html')

@mod.route('/interview/post_avaxp/', methods=['POST'])
def avaxp_data():
    if request.method == 'POST':
        print("--------------------------------post_avaxp--------------------------------")
    else:
        pass
    
    return redirect('/eduvis/interview/data/')

@mod.route('/interview/data/')
def data():    
    lst = view_information()
    
    lst_topics = []
    for i in range(len(lst)):
        sub_topic=[]
        lst_question = lst[i]["Questions"]
    
        for j in range(len(lst_question)):
            sub_topic.append({"id":lst_question[j]["id"],"label_pt":lst_question[j]["Sub_topic"]})
    
        curr_dict = {"label_pt":lst[i]["Label_pt"],"view":int(lst[i]["View"].replace("V","")),"sub_topic":sub_topic}
    
        lst_topics.append(curr_dict)
    
    sorted_list = sorted(lst_topics, key=lambda k: k['label_pt'])
    
    return render_template('eduvis/frontend/interview/data.html', selecting=sorted_list)

@mod.route('/interview/post_data/', methods=['POST'])
def data_data():
    if request.method == 'POST':
        print("--------------------------------post_data--------------------------------")
    else:
        pass
    
    return redirect('/eduvis/interview/visualizationxp/')

@mod.route('/interview/visualizationxp/')
def visualizationxp():
    return render_template('eduvis/frontend/interview/visualizationxp.html')

@mod.route('/interview/post_visualizationxp/', methods=['POST'])
def visualizationxp_data():
    if request.method == 'POST':
        print("--------------------------------post_visualizationxp--------------------------------")
    else:
        pass
    
    return redirect('/eduvis/static_dashboard/')

@mod.route('/evaluation_static_dashboard/')
def evaluation_static_dashboard():
    dashboard = Dashboard(_conn, _user_id, _static_dashboard_id, STATIC_DASHBOARD_TYPE)
    user = User(_conn, _user_id, _static_dashboard_id, STATIC_DASHBOARD_TYPE)
    return render_template('eduvis/frontend/dashboard/evaluate.html', userName=user.get_name(), charts_topic=dashboard.topic(), charts_id=dashboard.charts("id"), charts_layout=dashboard.charts("layout"), titleCharts=dashboard.title(), post_action="/eduvis/post_evaluation_static_dashboard/")

@mod.route('/post_evaluation_static_dashboard/', methods=['POST'])
def evaluation_static_dashboard_data():
    if request.method == 'POST':
        print("--------------------------------post_evaluation_static_dashboard--------------------------------")
    else:
        pass

    return redirect('/eduvis/customizable_dashboard/')

@mod.route('/evaluation_customizable_dashboard/')
def evaluation_customizable_dashboard():
    dashboard = Dashboard(_conn, _user_id, _customizable_dashboard_id, CUSTOMIZABLE_DASHBOARD_TYPE)
    user = User(_conn, _user_id, _customizable_dashboard_id, CUSTOMIZABLE_DASHBOARD_TYPE)
    return render_template('eduvis/frontend/dashboard/evaluate.html', userName=user.get_name(), charts_topic=dashboard.topic(), charts_id=dashboard.charts("id"), charts_layout=dashboard.charts("layout"), titleCharts=dashboard.title(), post_action="/eduvis/post_evaluation_customizable_dashboard/")

@mod.route('/post_evaluation_customizable_dashboard/', methods=['POST'])
def evaluation_customizable_dashboard_data():
    if request.method == 'POST':
        print("--------------------------------post_evaluation_customizable_dashboard--------------------------------")
    else:
        pass

    return redirect('/eduvis/thankyou/')

@mod.route('/static_dashboard/')
def static_dashboard():
    # global _user_id
    # global _static_dashboard_id
    
    # form = ConsentForm(request.form)
    # return render_template('questionnaire/consent.html', form=form)
    # return render_template('eduvis/frontend/dashboard.html', form=form)
    # load_user_info()    
    
    dashboard = Dashboard(_conn, _user_id, _static_dashboard_id, STATIC_DASHBOARD_TYPE)
    user = User(_conn, _user_id, _static_dashboard_id, STATIC_DASHBOARD_TYPE)
    return render_template('eduvis/frontend/dashboard/dashboard.html', userName=user.get_name(), charts_topic=dashboard.topic(), charts_id=dashboard.charts("id"), charts_layout=dashboard.charts("layout"), titleCharts=dashboard.title(), enableLeftMenu=STATIC_DASHBOARD_TYPE, leftMenuInfo=left_menu_info(), amountSelectedVG=dashboard.amount_by_view())

    # return render_template('eduvis/frontend/dashboard/dashboard.html')

@mod.route('/customizable_dashboard/')
def customizable_dashboard():
    dashboard = Dashboard(_conn, _user_id, _customizable_dashboard_id, CUSTOMIZABLE_DASHBOARD_TYPE)
    user = User(_conn, _user_id, _customizable_dashboard_id, CUSTOMIZABLE_DASHBOARD_TYPE)
    return render_template('eduvis/frontend/dashboard/dashboard.html', userName=user.get_name(), charts_topic=dashboard.topic(), charts_id=dashboard.charts("id"), charts_layout=dashboard.charts("layout"), titleCharts=dashboard.title(), enableLeftMenu=CUSTOMIZABLE_DASHBOARD_TYPE, leftMenuInfo=left_menu_info(), amountSelectedVG=dashboard.amount_by_view())

    # return render_template('eduvis/frontend/dashboard/dashboard.html')

@mod.route('/thankyou/')
def thankyou():
    return render_template('eduvis/frontend/thankyou.html')    

@mod.route('/add_chart/', methods=['POST'])
def add_chart():
    raw_data = json.loads(request.data.decode("utf-8"))
    
    # print(raw_data)
    # print(type(raw_data))
    # print("-----------------------")
    # print(raw_data['chart'])
    # print(type(raw_data['chart']))
    # print("-----------------------")
    # print(raw_data['value'])
    # print(type(raw_data['value']))
    
    # now = datetime.now()
    # current_time = now.strftime("%Y-%m-%d %H:%M:%S")

    # # _conn.create_database()
    # # data = ""
    # data = ("André Luiz", current_time)
    # _conn.insert("tb_user",data)

    dashboard = Dashboard(_conn, _user_id, _customizable_dashboard_id, CUSTOMIZABLE_DASHBOARD_TYPE)
    dashboard.set_dashboard(raw_data)

    resp = Response(json.dumps('OK'), mimetype='application/json')
    resp.status_code = 200
    return resp

@mod.route('/set_order/', methods=['POST'])
def set_order():
    raw_data = json.loads(request.data.decode("utf-8"))
    
    print("Set Order")
    print(raw_data)

    dashboard = Dashboard(_conn, _user_id, _customizable_dashboard_id, _dashboard_type)
    dashboard.set_order(raw_data)

    resp = Response(json.dumps('OK'), mimetype='application/json')
    resp.status_code = 200
    return resp

@mod.route('/access1/')
def access1(): # <!-- VG-08 -->
    access = Access(_conn, _user_id, _customizable_dashboard_id, CUSTOMIZABLE_DASHBOARD_TYPE)
    dashboard = Dashboard(_conn, _user_id, _customizable_dashboard_id, CUSTOMIZABLE_DASHBOARD_TYPE)
    user = User(_conn, _user_id, _customizable_dashboard_id, CUSTOMIZABLE_DASHBOARD_TYPE)
    return render_template('eduvis/frontend/dashboard/configure.html', userName=user.get_name(), charts_id=access.charts("day","id"), charts_layout=access.charts("day","layout"), titleCharts=access.title("day"), topic=access.topic("day"), charts_active=access.charts_active("day"), enableLeftMenu=CUSTOMIZABLE_DASHBOARD_TYPE, leftMenuInfo=left_menu_info(), amountSelectedVG=dashboard.amount_by_view())

@mod.route('/access2/')
def access2(): # <!-- VG-08 -->
    access = Access(_conn, _user_id, _customizable_dashboard_id, CUSTOMIZABLE_DASHBOARD_TYPE)
    dashboard = Dashboard(_conn, _user_id, _customizable_dashboard_id, CUSTOMIZABLE_DASHBOARD_TYPE)
    user = User(_conn, _user_id, _customizable_dashboard_id, CUSTOMIZABLE_DASHBOARD_TYPE)
    return render_template('eduvis/frontend/dashboard/configure.html', userName=user.get_name(), charts_id=access.charts("week","id"), charts_layout=access.charts("week","layout"), titleCharts=access.title("week"), topic=access.topic("week"), charts_active=access.charts_active("week"), enableLeftMenu=CUSTOMIZABLE_DASHBOARD_TYPE, leftMenuInfo=left_menu_info(), amountSelectedVG=dashboard.amount_by_view())

@mod.route('/assignments1/')
def assignments1(): # <!-- VG-01 -->
    assignment = Assignment(_conn, _user_id, _customizable_dashboard_id, CUSTOMIZABLE_DASHBOARD_TYPE)
    dashboard = Dashboard(_conn, _user_id, _customizable_dashboard_id, CUSTOMIZABLE_DASHBOARD_TYPE)
    user = User(_conn, _user_id, _customizable_dashboard_id, CUSTOMIZABLE_DASHBOARD_TYPE)
    return render_template('eduvis/frontend/dashboard/configure.html', userName=user.get_name(), charts_id=assignment.charts("student","id"), charts_layout=assignment.charts("student","layout"), titleCharts=assignment.title("student"), topic=assignment.topic("student"), charts_active=assignment.charts_active("student"), enableLeftMenu=CUSTOMIZABLE_DASHBOARD_TYPE, leftMenuInfo=left_menu_info(), amountSelectedVG=dashboard.amount_by_view())

@mod.route('/assignments2/')
def assignments2(): # <!-- VG-01 -->
    assignment = Assignment(_conn, _user_id, _customizable_dashboard_id, CUSTOMIZABLE_DASHBOARD_TYPE)
    dashboard = Dashboard(_conn, _user_id, _customizable_dashboard_id, CUSTOMIZABLE_DASHBOARD_TYPE)
    user = User(_conn, _user_id, _customizable_dashboard_id, CUSTOMIZABLE_DASHBOARD_TYPE)
    return render_template('eduvis/frontend/dashboard/configure.html', userName=user.get_name(), charts_id=assignment.charts("assignment","id"), charts_layout=assignment.charts("assignment","layout"), titleCharts=assignment.title("assignment"), topic=assignment.topic("assignment"), charts_active=assignment.charts_active("assignment"), enableLeftMenu=CUSTOMIZABLE_DASHBOARD_TYPE, leftMenuInfo=left_menu_info(), amountSelectedVG=dashboard.amount_by_view())

@mod.route('/cluster1/')
def cluster1(): # <!-- VG-05 -->
    cluster = Cluster(_conn, _user_id, _customizable_dashboard_id, CUSTOMIZABLE_DASHBOARD_TYPE)
    dashboard = Dashboard(_conn, _user_id, _customizable_dashboard_id, CUSTOMIZABLE_DASHBOARD_TYPE)
    user = User(_conn, _user_id, _customizable_dashboard_id, CUSTOMIZABLE_DASHBOARD_TYPE)
    return render_template('eduvis/frontend/dashboard/configure.html', userName=user.get_name(), charts_id=cluster.charts("grades_access","id"), charts_layout=cluster.charts("grades_access","layout"), titleCharts=cluster.title("grades_access"), topic=cluster.topic("grades_access"), charts_active=cluster.charts_active("grades_access"), enableLeftMenu=CUSTOMIZABLE_DASHBOARD_TYPE, leftMenuInfo=left_menu_info(), amountSelectedVG=dashboard.amount_by_view())

@mod.route('/cluster2/')
def cluster2(): # <!-- VG-05 -->
    cluster = Cluster(_conn, _user_id, _customizable_dashboard_id, CUSTOMIZABLE_DASHBOARD_TYPE)
    dashboard = Dashboard(_conn, _user_id, _customizable_dashboard_id, CUSTOMIZABLE_DASHBOARD_TYPE)
    user = User(_conn, _user_id, _customizable_dashboard_id, CUSTOMIZABLE_DASHBOARD_TYPE)
    return render_template('eduvis/frontend/dashboard/configure.html', userName=user.get_name(), charts_id=cluster.charts("grades_assignments","id"), charts_layout=cluster.charts("grades_assignments","layout"), titleCharts=cluster.title("grades_assignments"), topic=cluster.topic("grades_assignments"), charts_active=cluster.charts_active("grades_assignments"), enableLeftMenu=CUSTOMIZABLE_DASHBOARD_TYPE, leftMenuInfo=left_menu_info(), amountSelectedVG=dashboard.amount_by_view())

@mod.route('/cluster3/')
def cluster3(): # <!-- VG-05 -->    
    cluster = Cluster(_conn, _user_id, _customizable_dashboard_id, CUSTOMIZABLE_DASHBOARD_TYPE)
    dashboard = Dashboard(_conn, _user_id, _customizable_dashboard_id, CUSTOMIZABLE_DASHBOARD_TYPE)
    user = User(_conn, _user_id, _customizable_dashboard_id, CUSTOMIZABLE_DASHBOARD_TYPE)
    return render_template('eduvis/frontend/dashboard/configure.html', userName=user.get_name(), charts_id=cluster.charts("grades_access_materials","id"), charts_layout=cluster.charts("grades_access_materials","layout"), titleCharts=cluster.title("grades_access_materials"), topic=cluster.topic("grades_access_materials"), charts_active=cluster.charts_active("grades_access_materials"), enableLeftMenu=CUSTOMIZABLE_DASHBOARD_TYPE, leftMenuInfo=left_menu_info(), amountSelectedVG=dashboard.amount_by_view())

@mod.route('/cluster4/')
def cluster4(): # <!-- VG-05 -->
    cluster = Cluster(_conn, _user_id, _customizable_dashboard_id, CUSTOMIZABLE_DASHBOARD_TYPE)
    dashboard = Dashboard(_conn, _user_id, _customizable_dashboard_id, CUSTOMIZABLE_DASHBOARD_TYPE)
    user = User(_conn, _user_id, _customizable_dashboard_id, CUSTOMIZABLE_DASHBOARD_TYPE)
    return render_template('eduvis/frontend/dashboard/configure.html', userName=user.get_name(), charts_id=cluster.charts("grades_access_forum","id"), charts_layout=cluster.charts("grades_access_forum","layout"), titleCharts=cluster.title("grades_access_forum"), topic=cluster.topic("grades_access_forum"), charts_active=cluster.charts_active("grades_access_forum"), enableLeftMenu=CUSTOMIZABLE_DASHBOARD_TYPE, leftMenuInfo=left_menu_info(), amountSelectedVG=dashboard.amount_by_view())

@mod.route('/cluster5/')
def cluster5(): # <!-- VG-05 -->
    cluster = Cluster(_conn, _user_id, _customizable_dashboard_id, CUSTOMIZABLE_DASHBOARD_TYPE)
    dashboard = Dashboard(_conn, _user_id, _customizable_dashboard_id, CUSTOMIZABLE_DASHBOARD_TYPE)
    user = User(_conn, _user_id, _customizable_dashboard_id, CUSTOMIZABLE_DASHBOARD_TYPE)
    return render_template('eduvis/frontend/dashboard/configure.html', userName=user.get_name(), charts_id=cluster.charts("grades_forum_post","id"), charts_layout=cluster.charts("grades_forum_post","layout"), titleCharts=cluster.title("grades_forum_post"), topic=cluster.topic("grades_forum_post"), charts_active=cluster.charts_active("grades_forum_post"), enableLeftMenu=CUSTOMIZABLE_DASHBOARD_TYPE, leftMenuInfo=left_menu_info(), amountSelectedVG=dashboard.amount_by_view())

@mod.route('/cluster6/')
def cluster6(): # <!-- VG-05 -->
    cluster = Cluster(_conn, _user_id, _customizable_dashboard_id, CUSTOMIZABLE_DASHBOARD_TYPE)
    dashboard = Dashboard(_conn, _user_id, _customizable_dashboard_id, CUSTOMIZABLE_DASHBOARD_TYPE)
    user = User(_conn, _user_id, _customizable_dashboard_id, CUSTOMIZABLE_DASHBOARD_TYPE)
    return render_template('eduvis/frontend/dashboard/configure.html', userName=user.get_name(), charts_id=cluster.charts("grades_forum_reply","id"), charts_layout=cluster.charts("grades_forum_reply","layout"), titleCharts=cluster.title("grades_forum_reply"), topic=cluster.topic("grades_forum_reply"), charts_active=cluster.charts_active("grades_forum_reply"), enableLeftMenu=CUSTOMIZABLE_DASHBOARD_TYPE, leftMenuInfo=left_menu_info(), amountSelectedVG=dashboard.amount_by_view())

@mod.route('/cluster7/')
def cluster7(): # <!-- VG-05 -->
    cluster = Cluster(_conn, _user_id, _customizable_dashboard_id, CUSTOMIZABLE_DASHBOARD_TYPE)
    dashboard = Dashboard(_conn, _user_id, _customizable_dashboard_id, CUSTOMIZABLE_DASHBOARD_TYPE)
    user = User(_conn, _user_id, _customizable_dashboard_id, CUSTOMIZABLE_DASHBOARD_TYPE)
    return render_template('eduvis/frontend/dashboard/configure.html', userName=user.get_name(), charts_id=cluster.charts("grades_forum_thread","id"), charts_layout=cluster.charts("grades_forum_thread","layout"), titleCharts=cluster.title("grades_forum_thread"), topic=cluster.topic("grades_forum_thread"), charts_active=cluster.charts_active("grades_forum_thread"), enableLeftMenu=CUSTOMIZABLE_DASHBOARD_TYPE, leftMenuInfo=left_menu_info(), amountSelectedVG=dashboard.amount_by_view())

@mod.route('/prediction1/')
def prediction1(): # <!-- VG-07 -->
    prediction = Prediction(_conn, _user_id, _customizable_dashboard_id, CUSTOMIZABLE_DASHBOARD_TYPE)
    dashboard = Dashboard(_conn, _user_id, _customizable_dashboard_id, CUSTOMIZABLE_DASHBOARD_TYPE)
    user = User(_conn, _user_id, _customizable_dashboard_id, CUSTOMIZABLE_DASHBOARD_TYPE)
    return render_template('eduvis/frontend/dashboard/configure.html', userName=user.get_name(), charts_id=prediction.charts("id"), charts_layout=prediction.charts("layout"), titleCharts=prediction.title(), topic=prediction.topic(), charts_active=prediction.charts_active(), enableLeftMenu=CUSTOMIZABLE_DASHBOARD_TYPE, leftMenuInfo=left_menu_info(), amountSelectedVG=dashboard.amount_by_view())

@mod.route('/materials1/')
def materials1(): #  <!-- VG-02 -->
    material = Material(_conn, _user_id, _customizable_dashboard_id, CUSTOMIZABLE_DASHBOARD_TYPE)
    dashboard = Dashboard(_conn, _user_id, _customizable_dashboard_id, CUSTOMIZABLE_DASHBOARD_TYPE)
    user = User(_conn, _user_id, _customizable_dashboard_id, CUSTOMIZABLE_DASHBOARD_TYPE)
    return render_template('eduvis/frontend/dashboard/configure.html', userName=user.get_name(), charts_id=material.charts("access_students","id"), charts_layout=material.charts("access_students","layout"), titleCharts=material.title("access_students"), topic=material.topic("access_students"), charts_active=material.charts_active("access_students"), enableLeftMenu=CUSTOMIZABLE_DASHBOARD_TYPE, leftMenuInfo=left_menu_info(), amountSelectedVG=dashboard.amount_by_view())

@mod.route('/materials2/')
def materials2(): #  <!-- VG-02 -->
    material = Material(_conn, _user_id, _customizable_dashboard_id, CUSTOMIZABLE_DASHBOARD_TYPE)
    dashboard = Dashboard(_conn, _user_id, _customizable_dashboard_id, CUSTOMIZABLE_DASHBOARD_TYPE)
    user = User(_conn, _user_id, _customizable_dashboard_id, CUSTOMIZABLE_DASHBOARD_TYPE)
    return render_template('eduvis/frontend/dashboard/configure.html', userName=user.get_name(), charts_id=material.charts("access_materials","id"), charts_layout=material.charts("access_materials","layout"), titleCharts=material.title("access_materials"), topic=material.topic("access_materials"), charts_active=material.charts_active("access_materials"), enableLeftMenu=CUSTOMIZABLE_DASHBOARD_TYPE, leftMenuInfo=left_menu_info(), amountSelectedVG=dashboard.amount_by_view())

@mod.route('/forum1/')
def forum1(): # <!-- VG-03 -->
    forum = Forum(_conn, _user_id, _customizable_dashboard_id, CUSTOMIZABLE_DASHBOARD_TYPE)
    dashboard = Dashboard(_conn, _user_id, _customizable_dashboard_id, CUSTOMIZABLE_DASHBOARD_TYPE)
    user = User(_conn, _user_id, _customizable_dashboard_id, CUSTOMIZABLE_DASHBOARD_TYPE)
    return render_template('eduvis/frontend/dashboard/configure.html', userName=user.get_name(), charts_id=forum.charts("id"), charts_layout=forum.charts("layout"), titleCharts=forum.title(), topic=forum.topic(), charts_active=forum.charts_active(), enableLeftMenu=CUSTOMIZABLE_DASHBOARD_TYPE, leftMenuInfo=left_menu_info(), amountSelectedVG=dashboard.amount_by_view())

@mod.route('/video_access1/')
def video_access1(): # <!-- VG-04 -->
    video_access = Video_Access(_conn, _user_id, _customizable_dashboard_id, CUSTOMIZABLE_DASHBOARD_TYPE)
    dashboard = Dashboard(_conn, _user_id, _customizable_dashboard_id, CUSTOMIZABLE_DASHBOARD_TYPE)
    user = User(_conn, _user_id, _customizable_dashboard_id, CUSTOMIZABLE_DASHBOARD_TYPE)
    return render_template('eduvis/frontend/dashboard/configure.html', userName=user.get_name(), charts_id=video_access.charts("id"), charts_layout=video_access.charts("layout"), titleCharts=video_access.title(), topic=video_access.topic(), charts_active=video_access.charts_active(), enableLeftMenu=CUSTOMIZABLE_DASHBOARD_TYPE, leftMenuInfo=left_menu_info(), amountSelectedVG=dashboard.amount_by_view())

@mod.route('/age1/')
def age1(): # <!-- VG-06 -->
    age = Age(_conn, _user_id, _customizable_dashboard_id, CUSTOMIZABLE_DASHBOARD_TYPE)
    dashboard = Dashboard(_conn, _user_id, _customizable_dashboard_id, CUSTOMIZABLE_DASHBOARD_TYPE)
    user = User(_conn, _user_id, _customizable_dashboard_id, CUSTOMIZABLE_DASHBOARD_TYPE)
    return render_template('eduvis/frontend/dashboard/configure.html', userName=user.get_name(), charts_id=age.charts("age_access_forum","id"), charts_layout=age.charts("age_access_forum","layout"), titleCharts=age.title("age_access_forum"), topic=age.topic("age_access_forum"), charts_active=age.charts_active("age_access_forum"), enableLeftMenu=CUSTOMIZABLE_DASHBOARD_TYPE, leftMenuInfo=left_menu_info(), amountSelectedVG=dashboard.amount_by_view())

@mod.route('/age2/')
def age2(): # <!-- VG-06 -->
    age = Age(_conn, _user_id, _customizable_dashboard_id, CUSTOMIZABLE_DASHBOARD_TYPE)
    dashboard = Dashboard(_conn, _user_id, _customizable_dashboard_id, CUSTOMIZABLE_DASHBOARD_TYPE)
    user = User(_conn, _user_id, _customizable_dashboard_id, CUSTOMIZABLE_DASHBOARD_TYPE)
    return render_template('eduvis/frontend/dashboard/configure.html', userName=user.get_name(), charts_id=age.charts("age_forum_post","id"), charts_layout=age.charts("age_forum_post","layout"), titleCharts=age.title("age_forum_post"), topic=age.topic("age_forum_post"), charts_active=age.charts_active("age_forum_post"), enableLeftMenu=CUSTOMIZABLE_DASHBOARD_TYPE, leftMenuInfo=left_menu_info(), amountSelectedVG=dashboard.amount_by_view())

@mod.route('/age3/')
def age3(): # <!-- VG-06 -->
    age = Age(_conn, _user_id, _customizable_dashboard_id, CUSTOMIZABLE_DASHBOARD_TYPE)
    dashboard = Dashboard(_conn, _user_id, _customizable_dashboard_id, CUSTOMIZABLE_DASHBOARD_TYPE)
    user = User(_conn, _user_id, _customizable_dashboard_id, CUSTOMIZABLE_DASHBOARD_TYPE)
    return render_template('eduvis/frontend/dashboard/configure.html', userName=user.get_name(), charts_id=age.charts("age_forum_reply","id"), charts_layout=age.charts("age_forum_reply","layout"), titleCharts=age.title("age_forum_reply"), topic=age.topic("age_forum_reply"), charts_active=age.charts_active("age_forum_reply"), enableLeftMenu=CUSTOMIZABLE_DASHBOARD_TYPE, leftMenuInfo=left_menu_info(), amountSelectedVG=dashboard.amount_by_view())

@mod.route('/age4/')
def age4(): # <!-- VG-06 -->
    age = Age(_conn, _user_id, _customizable_dashboard_id, CUSTOMIZABLE_DASHBOARD_TYPE)
    dashboard = Dashboard(_conn, _user_id, _customizable_dashboard_id, CUSTOMIZABLE_DASHBOARD_TYPE)
    user = User(_conn, _user_id, _customizable_dashboard_id, CUSTOMIZABLE_DASHBOARD_TYPE)
    return render_template('eduvis/frontend/dashboard/configure.html', userName=user.get_name(), charts_id=age.charts("age_forum_topic","id"), charts_layout=age.charts("age_forum_topic","layout"), titleCharts=age.title("age_forum_topic"), topic=age.topic("age_forum_topic"), charts_active=age.charts_active("age_forum_topic"), enableLeftMenu=CUSTOMIZABLE_DASHBOARD_TYPE, leftMenuInfo=left_menu_info(), amountSelectedVG=dashboard.amount_by_view())

@mod.route('/video_interaction1/')
def video_interaction1(): # <!-- VG-09 -->
    video_interaction = Video_Interaction(_conn, _user_id, _customizable_dashboard_id, CUSTOMIZABLE_DASHBOARD_TYPE)
    dashboard = Dashboard(_conn, _user_id, _customizable_dashboard_id, CUSTOMIZABLE_DASHBOARD_TYPE)
    user = User(_conn, _user_id, _customizable_dashboard_id, CUSTOMIZABLE_DASHBOARD_TYPE)
    return render_template('eduvis/frontend/dashboard/configure.html', userName=user.get_name(), charts_id=video_interaction.charts("id"), charts_layout=video_interaction.charts("layout"), titleCharts=video_interaction.title(), topic=video_interaction.topic(), charts_active=video_interaction.charts_active(), enableLeftMenu=CUSTOMIZABLE_DASHBOARD_TYPE, leftMenuInfo=left_menu_info(), amountSelectedVG=dashboard.amount_by_view())

@mod.route('/video_understood1/')
def video_understood1(): # <!-- VG-10 -->
    video_understood = Video_Understood(_conn, _user_id, _customizable_dashboard_id, CUSTOMIZABLE_DASHBOARD_TYPE)
    dashboard = Dashboard(_conn, _user_id, _customizable_dashboard_id, CUSTOMIZABLE_DASHBOARD_TYPE)
    user = User(_conn, _user_id, _customizable_dashboard_id, CUSTOMIZABLE_DASHBOARD_TYPE)
    return render_template('eduvis/frontend/dashboard/configure.html', userName=user.get_name(), charts_id=video_understood.charts("id"), charts_layout=video_understood.charts("layout"), titleCharts=video_understood.title(), topic=video_understood.topic(), charts_active=video_understood.charts_active(), enableLeftMenu=CUSTOMIZABLE_DASHBOARD_TYPE, leftMenuInfo=left_menu_info(), amountSelectedVG=dashboard.amount_by_view())

@mod.route('/navigation1/')
def navigation1(): # <!-- VG-11 -->
    navigation = Navigation(_conn, _user_id, _customizable_dashboard_id, CUSTOMIZABLE_DASHBOARD_TYPE)
    dashboard = Dashboard(_conn, _user_id, _customizable_dashboard_id, CUSTOMIZABLE_DASHBOARD_TYPE)
    user = User(_conn, _user_id, _customizable_dashboard_id, CUSTOMIZABLE_DASHBOARD_TYPE)
    return render_template('eduvis/frontend/dashboard/configure.html', userName=user.get_name(), charts_id=navigation.charts("id"), charts_layout=navigation.charts("layout"), titleCharts=navigation.title(), topic=navigation.topic(), charts_active=navigation.charts_active(), enableLeftMenu=CUSTOMIZABLE_DASHBOARD_TYPE, leftMenuInfo=left_menu_info(), amountSelectedVG=dashboard.amount_by_view())





# @mod.route('/post/', methods=['GET', 'POST'])
# def consent():

    # form = ConsentForm(request.form)

    # if form.validate_on_submit():
    #     # create an questionnaire instance not yet stored in the database
    #     profile = ProfAnswer.NewProfileToRegister(consent=form.accept.data)

    #     # insert the record in our database and commit it
    #     db.session.add(profile)
    #     db.session.commit()

    #     # log the user in, as he now has an id
    #     session[SESSION_NAME_QUESTIONNAIRE_ID] = profile.id

    #     # redirect user to the 'index' method of the user module
    #     return redirect(url_for('questionnaire.profquestions'))
    #     # return redirect(url_for('eduvis.profquestions'))

    # return render_template('questionnaire/consent.html', form=form)
    # return render_template('eduvis/base.html', form=form)
    # return render_template('eduvis/home.html', form=form)

# @mod.route('/profquestions/', methods=['GET', 'POST'])
# # @requires_profile
# @requires_session
# def profquestions():
#     form = ProfileForm(request.form)

#     if form.validate_on_submit():

#         this_profile_id = session[SESSION_NAME_QUESTIONNAIRE_ID]

#         # update values
#         prof = ProfAnswer.query.get(this_profile_id)
#         prof.name=form.name.data
#         prof.age=form.age.data
#         prof.degree=form.degree.data
#         prof.job=form.job.data
#         prof.create_chart=form.create_chart.data
#         prof.view_chart=form.view_chart.data

#         # update the record in our database and commit it
#         db.session.commit()

#         # redirect user to the 'index' method of the user module
#         form = QuestionForm(step=1)
#         return redirect(url_for('questionnaire.visquestions', step=1))

#     return render_template('questionnaire/profquestions.html', form=form)


# @mod.route('/visquestions/', methods=['GET', 'POST'])
# # @requires_profile
# @requires_session
# def visquestions():

#     this_profile_id = session[SESSION_NAME_QUESTIONNAIRE_ID]

#     if this_profile_id is not None:
#         form = QuestionForm(request.form)

#         # n_step = 1
#         n_step = int(request.values.get('step'))
#         question_form = Questions.query.filter(Questions.id == n_step).all()
#         question_form_id = question_form[0].id

#         # b_step = n_step - 1

#         if form.validate_on_submit():

#             step = int(request.form['step'])
#             question_form = Questions.query.filter(Questions.id == step).all()
#             question_form_id = question_form[0].id

#             # order of the asnwers + some ajustments to put in format '1,2,3'

#             f_order = request.form.get('f_order')

#             if(f_order != ''):
#                 x = f_order.replace('item[]=', '')
#                 n_order = x.replace('&', '')
#             else:
#                 #TODO: modificar depois para a ordem da resposta que virá do banco
#                 n_order = '123'

#             # check if this user has already filled out this question - back button?
#             quesRegistered = VisAnswer.query.filter(and_(VisAnswer.profile_id == this_profile_id,
#                                                          VisAnswer.question_id == question_form_id)).first()


#             if quesRegistered is not None:
#                 # update answers for this page
#                 q_id = quesRegistered.id

#                 # get user from the database
#                 vis = VisAnswer.query.get(q_id)

#                 # update values
#                 vis.answer_sel = n_order

#                 # update the record in our database and commit it
#                 db.session.commit()



#                 # question = VisAnswer.query.filter_by(id=q_id).update(dict(answer_sel=n_order, profile_id=profile_id, question_id=q_id,
#                 #                                      step=step))
#                 # db.session.commit()

#                 # question = VisAnswer.update(). \
#                 #     where(id == q_id). \
#                 #     values(answer_sel=n_order, profile_id=profile_id, question_id=q_id,
#                 #                                      step=step)
#                 # db.session.update(question)

#             else:
#                 question = VisAnswer.NewAnswerToRegister(answer_sel=n_order, profile_id=this_profile_id,
#                                                          question_id=question_form_id, step=step)

#                 # insert the record in our database and commit it
#                 db.session.add(question)
#                 db.session.commit()

#             n_step = step + 1
#             form = QuestionForm(step=n_step)

#             if (n_step > 10):
#                 return redirect(url_for('questionnaire.thankyou'))

#             # order = n_order

#         if n_step == 10:
#             submit_button = "Finalizar"
#         else:
#             submit_button = "Próxima"

#         progress = (n_step)*10

#         a = AswerOrder()
#         order = a.getAnswer(n_step, this_profile_id, question_form_id)
#         # rdm = a.randomOrder(question_form[0].id)

#         #graph 1
#         count = 500
#         xScale = np.linspace(0, 100, count)
#         yScale = np.random.randn(count)

#         # Create a trace
#         trace = go.Scatter(
#             x=xScale,
#             y=yScale
#         )

#         data = [trace]
#         graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

#         #graph 2
#         count = 500
#         xScale = np.linspace(0, 100, count)
#         y0_scale = np.random.randn(count)
#         y1_scale = np.random.randn(count)
#         y2_scale = np.random.randn(count)

#         # Create traces
#         trace0 = go.Scatter(
#             x=xScale,
#             y=y0_scale
#         )
#         trace1 = go.Scatter(
#             x=xScale,
#             y=y1_scale
#         )
#         trace2 = go.Scatter(
#             x=xScale,
#             y=y2_scale
#         )
#         data = [trace0, trace1, trace2]
#         graphJSON_2 = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

#         # response.headers.add('Cache-Control', 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0')
#         return render_template('questionnaire/visquestions.html', form=form, step=n_step, question_form=question_form,
#                                profile_id=this_profile_id, submit_button=submit_button, progress=progress, f_order=order,
#                                graphJSON=graphJSON, graphJSON_2=graphJSON_2)



#     else:
#         return render_template('questionnaire/thankyou.html')


# @mod.route('/thankyou/', methods=['GET'])
# # @requires_logout
# def thankyou():
#     session.pop(SESSION_NAME_QUESTIONNAIRE_ID, None)
#     return render_template('questionnaire/thankyou.html')
#     # return redirect(url_for('questionnaire.thankyou'))


# @mod.route('/logout/', methods=['GET'])
# def logout():
#     # remove the username from the session if it's there
#     session.pop(SESSION_NAME_QUESTIONNAIRE_ID, None)

#     # flash will display a message to the user
#     # flash('Do not forget keep the exercises')

#     # redirect user to the 'index' method of the user module
#     return redirect(url_for('questionnaire.index'))
