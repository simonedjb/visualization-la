import pandas as pd
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath("eduvis"))))

import dash
import dash_core_components as dcc
import dash_html_components as html

from backend import backend
from eduvis import V001, V002, V003, V004, V005, V006, V007, V008, V010#, V009, V011

import visdcc

control = backend.backend()
students = pd.read_csv("assets/names.csv")
view1 = V001.V001(type_result = "dash",language = "pt")
view2 = V002.V002(type_result = "dash",language = "pt")
view3 = V003.V003(type_result = "dash",language = "pt")
view4 = V004.V004(type_result = "dash",language = "pt")
view5 = V005.V005(type_result = "dash",language = "pt")
view6 = V006.V006(type_result = "dash",language = "pt")
view7 = V007.V007(type_result = "dash",language = "pt")
view8 = V008.V008(type_result = "dash",language = "pt")
# view9 = V009.V009(type_result = "dash",language = "pt")
view10 = V010.V010(type_result = "dash",language = "pt")
# view11 = V011.V011(type_result = "dash",language = "pt")

class frontend:

    def __init__(self):
        pass

    def survey_hidden_values(self):
        return html.Div(id='hidden-div', style={'display':'none'})
    
    def survey_warning(self,id):
        return html.Div(className="container", children=[
                    html.Div(className="row", children=[
                        html.Div(className="col s12",children=[
                            html.Div(id=id, className="row center"),
                        ]),
                    ]),
                ])

    def survey_warning_message(self):
        return html.H5(className="header center red-text", children=["Preencha todos os campos com *"]),

    def survey_404(self):
        return html.Div(className="container", children=[
                    html.Div(className="row", children=[
                        html.Div(className="col s12",children=[
                            html.Div(className="row center",children=[
                                html.H1(className="header center blue-text", children=["404 - Essa página não existe"]),
                            ]),
                        ]),
                    ]),
                ])

    def survey_body(self):
        return html.Div(id='page', children=[
                    dcc.Location(id='url', refresh=False),
                    html.Div(id='intermediate-value', style={'display': 'none'}, children=[
                        html.Label(id='user_cache'),
                        html.Label(id='page_cache'),
                    ]),
                    html.Div(id='page-content')
                ])

    def survey_send(self,id,href="",label="Avançar"):
        return html.Div(className="container", children=[
                    html.Div(className="row", children=[
                        html.Div(className="col s12",children=[
                            html.Div(className="row center", children=[
                                dcc.Link(label, id=id,className="waves-effect waves-light btn-large", href=href),
                                # html.Button('Enviar', id='send',className="waves-effect waves-light btn-large", n_clicks=0),
                                html.Br(),html.Br()
                            ]),
                        ]),
                    ]),
                ])

    def survey_end(self):
        return html.Div(className="container", children=[
                    html.Div(className="row", children=[
                        html.Div(className="col s12",children=[
                            html.Div(className="row center", children=[
                                html.H1(className="header center blue-text", children=["Obrigado pela sua participação"]),
                                html.Br(),html.Br()
                            ]),
                        ]),
                    ])
                ])

    def survey_presentation(self):
        return html.Div(className="container", children=[
                    html.Div(className="row", children=[
                        html.Div(className="col s12",children=[
                            html.Div(className="row left", children=[
                                html.H4(className="header left blue-text", children=["Olá,"]),
                                html.Br(),
                                html.H5(className="header left blue-text", children=["Essa é uma pesquisa com fins estritamente acadêmicos sobre preferências de visualizações de dados de acesso e interação em Ambientes Virtuais de Aprendizagem (AVAs)."]),
                                html.Br(),
                                html.H5(className="header left blue-text", children=["Ressaltamos que sua participação é voluntária e todas as informações fornecidas serão mantidas anonimizadas."]),
                                html.Br(),html.Br(),
                                html.H5(className="header left blue-text", children=["Os resultados obtidos nessa pesquisa serão divulgados exclusivamente pelos pesquisadores em formato de relatórios e/ou artigos científicos."]),
                                html.Br(),html.Br(),
                                html.H5(className="header left blue-text", children=["A pesquisa é liderada pela Pontifícia Universidade Católica do Rio de Janeiro. Este estudo está sendo desenvolvido no Programa de Pós-Graduação em Informática, pela aluno de doutorado André Luiz de B. Damasceno com orientação da professora Drª. Simone D. J. Barbosa."]),
                                html.Br(),html.Br(),
                                html.H6(className="header left blue-text", children=["E-mail para contato: adamasceno@inf.puc-rio.br"]),
                                html.Br(),html.Br()
                            ]),
                            
                            html.Div(className="row center", children=[
                                html.Div(className="input-field col s4",children=[
                                    html.P(children=[
                                        html.Label(className="left red-text", children=["Para prosseguir, digite seu email:"]),
                                    ]),
                                    dcc.Input(id='user_email', placeholder="user@gmail.com", type='text',value="")
                                ]),
                            ]),
                        ]),
                    ])
                ])

    def survey_filter(self):
        return html.Div(className="container", children=[
                    html.Div(className="row", children=[
                        html.Div(className="col s12",children=[
                            html.Div(className="row left", children=[                                
                                html.H4(className="header left blue-text", children=["Você tem experiência como instrutor, tutor, monitor ou professor utilizando Ambientes Virtuais de Aprendizagem (AVAs) como Moodle, Blackboard, etc.?"]),
                            ]),
                            ############################################################################################
                            html.Div(className="row center", children=[
                                html.Div(className="input-field col s4 offset-s4", children=[
                                    dcc.Dropdown(
                                        id='user_ead_xp',
                                        placeholder="Sim ou Não",
                                        options=[
                                            {'label': 'Sim', 'value': 'S'},
                                            {'label': 'Não', 'value': 'N'},
                                            
                                        ],
                                        value="",
                                        searchable=False,
                                        clearable=False,
                                        style={'color': '#2196f3'}
                                    ),
                                ]),
                            ]),
                            html.Br(),html.Br(),html.Br()
                        ]),
                    ]),
                ])

    def survey_profile(self, data=[]):
        global control
        return html.Div(className="container", children=[
                    html.Div(className="row", children=[
                        html.Div(className="col s12",children=[
                            html.Div(className="row center", children=[
                                html.H3(className="header center blue-text", children=["Sobre você"]),
                                html.Br(),html.Br()
                            ]),
                            ############################################################################################
                            html.Div(className="row center", children=[
                                html.Div(className="input-field col s8",children=[
                                    html.P(children=[
                                        html.Label(className="left blue-text", children=["*Nome completo:"])
                                    ]),
                                    dcc.Input(id='user_name', placeholder="", type='text',value=control.load_frontend_data('user_name',data))
                                ]),
                                html.Div(className="input-field col s2", children=[
                                    html.P(children=[
                                        html.Label(className="left blue-text", children=["*Gênero:"]),
                                    ]),
                                    dcc.Dropdown(
                                        id='user_gender',
                                        placeholder="M ou F",
                                        options=[
                                            {'label': 'Masculino', 'value': 'M'},
                                            {'label': 'Feminino', 'value': 'F'},
                                            
                                        ],
                                        value=control.load_frontend_data('user_gender',data),
                                        searchable=False,
                                        clearable=True,
                                        style={'color': '#2196f3'}
                                    ),
                                ]),
                                html.Div(className="input-field col s2",children=[
                                    html.P(children=[
                                        html.Label(className="left blue-text", children=["*Idade:"]),
                                    ]),
                                    dcc.Input(id='user_age', placeholder="20,anos, 30 anos, etc.", type='text',value=control.load_frontend_data('user_age',data))
                                ]),
                            ]),
                            ############################################################################################
                            html.Div(className="row center", children=[
                                html.Div(className="input-field col s6",children=[
                                    html.P(children=[
                                        html.Label(className="left blue-text", children=["*Estado e cidade onde nasceu (caso seja estranjeiro, informe o país):"]),
                                    ]),
                                    dcc.Input(id='user_place_birth', placeholder="São Luís, Maranhão", type='text',value=control.load_frontend_data('user_place_birth',data))
                                ]),
                                html.Div(className="input-field col s6",children=[
                                    html.P(children=[
                                        html.Label(className="left blue-text", children=["*Estado e cidade onde trabalha:"]),
                                    ]),
                                    dcc.Input(id='user_place_work', placeholder="São Luís, Maranhão", type='text',value=control.load_frontend_data('user_place_work',data))
                                ])
                            ]),
                            ############################################################################################
                            html.Div(className="row center", children=[
                                html.Div(className="input-field col s8",children=[
                                    html.P(children=[
                                        html.Label(className="left blue-text", children=["*Área de formação:"]),
                                    ]),
                                    dcc.Input(id='user_scholarship', placeholder="Área de formação", type='text',value=control.load_frontend_data('user_scholarship',data))
                                ]),
                                html.Div(className="input-field col s4", children=[
                                    html.P(children=[
                                        html.Label(className="left blue-text", children=["*Grau de escolaridade:"]),
                                    ]),
                                    dcc.Dropdown(
                                        id='user_scholarship_degree',
                                        placeholder="",
                                        options=[
                                            {'label': 'Ensino Médio', 'value': 'Ensino Médio'},
                                            {'label': 'Graduação', 'value': 'Graduação'},
                                            {'label': 'Especialização', 'value': 'Especialização'},
                                            {'label': 'Mestrado', 'value': 'Mestrado'},
                                            {'label': 'Doutorado', 'value': 'Doutorado'},
                                            {'label': 'Pós-doutorado', 'value': 'Pós-doutorado'},
                                        ],
                                        value=control.load_frontend_data('user_scholarship_degree',data),
                                        searchable=False,
                                        clearable=True,
                                        style={'color': '#2196f3'}
                                    ),
                                ])
                            ]),
                            ############################################################################################
                            html.Div(className="row center", children=[
                                html.Div(className="input-field col s6",children=[
                                    html.P(children=[
                                        html.Label(className="left blue-text", children=["*Profissão:"]),
                                    ]),
                                    dcc.Input(id='user_job', placeholder="Professor, Instrutor, Tutor, etc", type='text',value=control.load_frontend_data('user_job',data))
                                ]),
                                html.Div(className="input-field col s6", children=[
                                    html.P(children=[
                                        html.Label(className="left blue-text", children=["*Já desenvolveu algum programa de computador?"]),
                                    ]),
                                    dcc.Dropdown(
                                        id='user_programming_xp',
                                        placeholder="Sim ou Não",
                                        options=[
                                            {'label': 'Sim', 'value': 'S'},
                                            {'label': 'Não', 'value': 'N'},
                                            
                                        ],
                                        value=control.load_frontend_data('user_programming_xp',data),
                                        searchable=False,
                                        clearable=True,
                                        style={'color': '#2196f3'}
                                    ),
                                ])
                            ]),
                            ############################################################################################
                            html.Div(className="row", children=[
                                html.Div(className="input-field col s12", children=[
                                    html.Label(className="left blue-text", children=["Caso já tenha desenvolvido algum programa de computador:"]),
                                ]),
                            ]),
                            ############################################################################################
                            html.Div(className="row center", children=[
                                html.Div(className="input-field col s6",children=[
                                    html.P(children=[
                                        html.Label(className="left blue-text", children=["Quando foi a última vez que você programou?"]),
                                    ]),
                                    dcc.Input(id='user_programming_last_time', placeholder="", type='text',value=control.load_frontend_data('user_programming_last_time',data))
                                ]),
                                html.Div(className="input-field col s6",children=[
                                    html.P(children=[
                                        html.Label(className="left blue-text", children=["Em que linguagem de programação?"]),
                                    ]),
                                    dcc.Input(id='user_programming_language', placeholder="", type='text',value=control.load_frontend_data('user_programming_language',data))
                                ]),
                            ]),
                            html.Br()
                        ]),
                    ])
                ])

    def survey_ead_xp(self, data=[]):
        global control
        return html.Div(className="container", children=[
                    html.Div(className="row", children=[
                        html.Div(className="col s12",children=[
                            html.Div(className="row center", children=[
                                html.H3(className="header center blue-text", children=["Sobre sua experiência com AVAs"]),
                                html.Br(),html.Br()
                            ]),
                            ############################################################################################
                            html.Div(className="row center", children=[
                                html.Div(className="input-field col s7",children=[
                                    html.P(children=[
                                        html.Label(className="left blue-text", children=["*Papeis desempenhados na utilização do AVAs:"]),
                                    ]),
                                    dcc.Input(id='user_job_ead', placeholder="Professor, Tutor, Monitor, etc.", type='text',value=control.load_frontend_data('user_job_ead',data))
                                ]),
                                html.Div(className="input-field col s5",children=[
                                    html.P(children=[
                                        html.Label(className="left blue-text", children=["*Tempo de experiência na utilização de AVAs:"]),
                                    ]),
                                    dcc.Input(id='user_time_experience', placeholder="6 meses, 5 anos, 10 anos, etc.", type='text',value=control.load_frontend_data('user_time_experience',data))
                                ]),
                            ]),
                            ############################################################################################
                            html.Div(className="row center", children=[
                                html.Div(className="input-field col s12",children=[
                                    html.P(children=[
                                        html.Label(className="left blue-text", children=["*Instituições de ensino que trabalha (e que trabalhou) utilizando AVAs:"]),
                                    ]),
                                    dcc.Input(id='user_organization_worked', placeholder="PUC-Rio, UFMA, UFRJ, UEMA, etc.", type='text',value=control.load_frontend_data('user_organization_worked',data))
                                ]),
                            ]),
                            ############################################################################################
                            html.Div(className="row center", children=[
                                html.Div(className="input-field col s12",children=[
                                    html.P(children=[
                                        html.Label(className="left blue-text", children=["*Disciplinas ensinadas utilizando AVAs:"]),
                                    ]),
                                    dcc.Input(id='user_subject', placeholder="Disciplinas de computação, Disciplinas da saúde (ex: Síndromes Geriátricas, etc.), Introdução a EaD, etc.", type='text',value=control.load_frontend_data('user_subject',data))
                                ]),
                            ]),
                            ############################################################################################
                            html.Div(className="row center", children=[
                                html.Div(className="input-field col s6", children=[
                                    html.P(children=[
                                        html.Label(className="left blue-text", children=["*Experiência com qual modalidade de ensino utilizando AVAS:"]),
                                    ]),
                                    dcc.Dropdown(
                                        id='user_ead_modality',
                                        placeholder="Presencial ou a Distância",
                                        options=[
                                            {'label': 'A distância', 'value': 'A distância'},
                                            {'label': 'Presencial', 'value': 'Presencial'},
                                            {'label': 'Ambas', 'value': 'Ambas'},
                                        ],
                                        value=control.load_frontend_data('user_ead_modality',data),
                                        searchable=False,
                                        clearable=True,
                                        style={'color': '#2196f3'}
                                    ),
                                ]),
                                html.Div(className="input-field col s6",children=[
                                    html.P(children=[
                                        html.Label(className="left blue-text", children=["*AVAs que utiliza (e que já utilizou):"]),
                                    ]),
                                    dcc.Input(id='user_avas_performed', placeholder="Moodle, Blackboard, etc.", type='text',value=control.load_frontend_data('user_avas_performed',data))
                                ]),
                            ]),
                            ############################################################################################
                            html.Div(className="row center", children=[
                                html.Div(className="input-field col s12",children=[
                                    html.P(children=[
                                        html.Label(className="left blue-text", children=["*Recursos que utiliza e já utilizou nos AVAs:"]),
                                    ]),
                                    dcc.Input(id='user_avas_resources', placeholder="Vídeos, ebooks, fórum, chat, badges, etc.", type='text',value=control.load_frontend_data('user_avas_resources',data))
                                ]),
                            ]),
                            ############################################################################################
                            html.Div(className="row center", children=[
                                html.Div(className="input-field col s12",children=[
                                    html.P(children=[
                                        html.Label(className="left blue-text", children=["*Faixa etária dos alunos que ensina (e que já ensinou) utilizando AVAs:"]),
                                    ]),
                                    dcc.Input(id='user_students_age', placeholder="18 à 30 anos, 25 à 60 anos, etc.", type='text',value=control.load_frontend_data('user_students_age',data))
                                ]),
                            ]),
                            ############################################################################################
                            html.Div(className="row center", children=[
                                html.Div(className="input-field col s8",children=[
                                    html.P(children=[
                                        html.Label(className="left blue-text", children=["*Área de formação dos alunos que ensina (e que já ensinou) utilizando AVAs:"]),
                                    ]),
                                    dcc.Input(id='user_students_scholarship', placeholder="Informática, Saúde, etc.", type='text',value=control.load_frontend_data('user_students_scholarship',data))
                                ]),
                                html.Div(className="input-field col s4", children=[
                                    html.P(children=[
                                        html.Label(className="left blue-text", children=["*Grau de escolaridade desses alunos:"]),
                                    ]),
                                    dcc.Dropdown(
                                        id='user_students_scholarship_degree',
                                        placeholder="",
                                        options=[
                                            {'label': 'Ensino Médio', 'value': 'Ensino Médio'},
                                            {'label': 'Graduação', 'value': 'Graduação'},
                                            {'label': 'Especialização', 'value': 'Especialização'},
                                            {'label': 'Mestrado', 'value': 'Mestrado'},
                                            {'label': 'Doutorado', 'value': 'Doutorado'},
                                            {'label': 'Pós-doutorado', 'value': 'Pós-doutorado'},
                                        ],
                                        value=control.load_frontend_data('user_students_scholarship_degree',data),
                                        searchable=False,
                                        clearable=True,
                                        style={'color': '#2196f3'}
                                    ),
                                ])
                            ]),
                            ############################################################################################
                            html.Div(className="row center", children=[
                                html.Div(className="input-field col s12",children=[
                                    html.P(children=[
                                        html.Label(className="left blue-text", children=["*Quais informações dos alunos você considera relevante:"]),
                                    ]),
                                    dcc.Input(id='user_students_meaningful', placeholder="", type='text',value=control.load_frontend_data('user_students_meaningful',data))
                                ]),
                            ]),
                            html.Br(),html.Br(),html.Br()
                        ]),
                    ])
                ])

    def survey_logs(self, data=[]):
        global control
        return html.Div(className="container", children=[
                    html.Div(className="row", children=[
                        html.Div(className="col s12",children=[
                            html.Div(className="row center", children=[
                                html.H3(className="header center blue-text", children=["Em relação aos dados dos AVAs"]),
                                html.Br(),html.Br()
                            ]),
                            ############################################################################################
                            html.Div(className="row center", children=[
                                html.Div(className="input-field col s12",children=[
                                    html.P(children=[
                                        html.Label(className="left blue-text", children=["*Como você acompanha o andamento dos alunos durante o curso:"]),
                                    ]),
                                    dcc.Input(id='user_students_progress', placeholder="", type='text',value=control.load_frontend_data('user_students_progress',data))
                                ]),
                            ]),
                            ############################################################################################
                            html.Div(className="row center", children=[
                                html.Div(className="input-field col s12",children=[
                                    html.P(children=[
                                        html.Label(className="left blue-text", children=["*Quais dados podem ser utilizados para predizer as notas dos alunos?"]),
                                    ]),
                                    dcc.Input(id='user_logs_performance', placeholder="", type='text',value=control.load_frontend_data('user_logs_performance',data))
                                ]),
                            ]),
                            ############################################################################################
                            html.Div(className="row center", children=[
                                html.Div(className="input-field col s12",children=[
                                    html.P(children=[
                                        html.Label(className="left blue-text", children=["*Quais dados podem ser utilizados para predizer se o aluno irá abandonar o curso?"]),
                                    ]),
                                    dcc.Input(id='user_logs_dropout', placeholder="", type='text',value=control.load_frontend_data('user_logs_dropout',data))
                                ]),
                            ]),
                            ############################################################################################
                            html.Div(className="row center", children=[
                                html.Div(className="input-field col s12",children=[
                                    html.P(children=[
                                        html.Label(className="left blue-text", children=["*Quais dados podem ser utilizados para avaliar o engajamento do aluno?"]),
                                    ]),
                                    dcc.Input(id='user_logs_engagement', placeholder="", type='text',value=control.load_frontend_data('user_logs_engagement',data))
                                ]),
                            ]),
                            ############################################################################################
                            html.Div(className="row", children=[
                                html.Div(className="input-field col s12", children=[
                                    html.Label(className="left blue-text", children=["Caso você faça análise de algum dado de acesso ou interação dos estudantes no AVA:"]),
                                ]),
                            ]),
                            ############################################################################################
                            html.Div(className="row center", children=[
                                html.Div(className="input-field col s6",children=[
                                    html.P(children=[
                                        html.Label(className="left blue-text", children=["quais dados você analisa?"]),
                                    ]),
                                    dcc.Input(id='user_logs_analyse', placeholder="Acesso ao AVA, realização de tarefas, postagem no fórum, etc.", type='text',value=control.load_frontend_data('user_logs_analyse',data))
                                ]),
                                html.Div(className="input-field col s6",children=[
                                    html.P(children=[
                                        html.Label(className="left blue-text", children=["como esses dados são apresentados pra você?"]),
                                    ]),
                                    dcc.Input(id='user_logs_presentation', placeholder="Em uma tabela, em gráfico de pizza, em gráfico de barra, etc.", type='text',value=control.load_frontend_data('user_logs_presentation',data))
                                ]),
                            ]),
                            ############################################################################################
                            html.Br(),html.Br(),html.Br()
                        ])
                    ])
                ])

    def survey_student_information(self, data=[]):
        global control
        views = control.get_view()
        options = []
        
        for i in range(0, len(views)): 
            questions = control.get_view_question_view(views[i]) 
            for j in range(0, len(questions)): 
                options.append({
                                'label':control.get_view_label_question_view(views[i],questions[j]), #question label
                                'value':str(views[i]+"_"+control.get_view_id_question_view(views[i],questions[j])) #view_id
                               })

        return html.Div(className="container", children=[
                    html.Div(className="row", children=[
                        html.Div(className="col s12",children=[
                            html.Div(className="row center", children=[
                                html.H3(className="header center blue-text", children=["Sobre dados de interação e acesso dos estudantes"]),
                                html.Br(),html.Br()
                            ]),
                            ############################################################################################
                            html.Div(className="row left", children=[
                                html.Div(className="input-field col s12",children=[
                                    html.P(children=[
                                        html.Label(className="left blue-text", children=["*Selecione os dados que você analisa ou que gostaria de analisar:"]),
                                    ]),
                                    html.Br(),
                                    dcc.Checklist(
                                        id="user_interaction_access_students_logs",
                                        options=options,
                                        values=control.load_frontend_data('user_interaction_access_students_logs',data),
                                        labelStyle={"display":"block","margin-top":"15px"},
                                    )
                                ]), 
                            ]),
                            ############################################################################################
                            html.Div(className="row center", children=[
                                html.Div(className="input-field col s12",children=[
                                    html.P(children=[
                                        html.Label(className="left blue-text", children=["Há mais algum dado que você analisa (ou gostaria de analisar) e que não foi apresentada?"]),
                                    ]),
                                    dcc.Input(id='user_interaction_access_students_logs_others', placeholder="", type='text',value=control.load_frontend_data('user_interaction_access_students_logs_others',data))
                                ]),
                            ]),
                            ############################################################################################
                            html.Div(className="row center", children=[
                                html.Div(className="input-field col s12",children=[
                                    html.P(children=[
                                        html.Label(className="left blue-text", children=["Como você gostaria que esses dados fossem apresentados?"]),
                                    ]),
                                    dcc.Input(id='user_interaction_access_students_logs_presentation', placeholder="Em uma tabela, em gráfico de pizza, em gráfico de barra, etc.", type='text',value=control.load_frontend_data('user_interaction_access_students_logs_presentation',data))
                                ]),
                            ]),
                            html.Br(),html.Br(),html.Br(),
                            html.Br(),html.Br(),html.Br(),
                        ])
                    ])
                ])

    def survey_visualization(self, data=[]):
        global control
        return html.Div(className="container", children=[
                    html.Div(className="row", children=[
                        html.Div(className="col s12",children=[
                            html.Div(className="row center", children=[
                                html.H3(className="header center blue-text", children=["Sobre visualização de dados"]),
                                html.Br(),html.Br()
                            ]),
                            ############################################################################################
                            html.Div(className="row", children=[
                                html.Div(className="input-field col s12", children=[
                                    html.Label(className="left blue-text", children=["Com que frequência você:"]),
                                ]),
                            ]),
                            ############################################################################################
                            html.Div(className="row center", children=[
                                html.Div(className="input-field col s6", children=[
                                    html.P(children=[
                                        html.Label(className="left blue-text", children=["*lê e interpreta gráficos?"]),
                                    ]),
                                    dcc.Dropdown(
                                        id='user_view_read',
                                        placeholder="Nunca, uma vez ou outra, etc.",
                                        options=[
                                            {'label': 'Nunca', 'value': 'Nunca'},
                                            {'label': 'Uma vez ou outra', 'value': 'Uma vez ou outra'},
                                            {'label': 'Pelo menos uma vez por mês', 'value': 'Pelo menos uma vez por mês'},
                                            {'label': 'Pelo menos uma vez por semana', 'value': 'Pelo menos uma vez por semana'},
                                            {'label': 'Mais de uma vez por semana', 'value': 'Mais de uma vez por semana'},
                                        ],
                                        value=control.load_frontend_data('user_view_read',data),
                                        searchable=False,
                                        clearable=True,
                                        style={'color': '#2196f3'}
                                    ),
                                ]),
                                html.Div(className="input-field col s6", children=[
                                    html.P(children=[
                                        html.Label(className="left blue-text", children=["*cria gráficos?"]),
                                    ]),
                                    dcc.Dropdown(
                                        id='user_view_make',
                                        placeholder="Nunca, uma vez ou outra, etc.",
                                        options=[
                                            {'label': 'Nunca', 'value': 'Nunca'},
                                            {'label': 'Uma vez ou outra', 'value': 'Uma vez ou outra'},
                                            {'label': 'Pelo menos uma vez por mês', 'value': 'Pelo menos uma vez por mês'},
                                            {'label': 'Pelo menos uma vez por semana', 'value': 'Pelo menos uma vez por semana'},
                                            {'label': 'Mais de uma vez por semana', 'value': 'Mais de uma vez por semana'},
                                        ],
                                        value=control.load_frontend_data('user_view_make',data),
                                        searchable=False,
                                        clearable=True,
                                        style={'color': '#2196f3'}
                                    ),
                                ]),
                            ]),
                        ]),
                    ]),
                    html.Br(),html.Br(),html.Br()
                ])

    def survey_chart_preference(self,question,page, data=[]):
        return html.Div(className="container", children=[
                    html.Div(className="row", children=[
                        html.Div(className="col s12",children=[
                            html.Div(className="row center", children=[
                                html.H3(className="header center blue-text", children=[question]),
                                html.Br(),html.Br()
                            ]),
                            self.survey_select_page(page,data)
                        ]),
                    ]),
                    html.Br(),html.Br(),html.Br()
                ])

    def survey_select_page(self,page,data):
        if page == "prefv001_1":
            return self.charts_v001_1(data)
        elif page == "prefv001_2":
            return self.charts_v001_2(data)
        elif page == "prefv008_1":
            return self.charts_v008_1(data)
        elif page == "prefv008_2":
            return self.charts_v008_2(data)
        elif page == "prefv002_1":
            return self.charts_v002_1(data)
        elif page == "prefv003_1":
            return self.charts_v003_1(data)
        elif page == "prefv009_1":
            return self.charts_v009_1(data)
        elif page == "prefv004_1":
            return self.charts_v004_1(data)
        elif page == "prefv010_1":
            return self.charts_v010_1(data)
        elif page == "prefv005_1":
            return self.charts_v005_1(data)
        elif page == "prefv006_1":
            return self.charts_v006_1(data)
        elif page == "prefv011_1":
            return self.charts_v011_1(data)
        elif page == "prefv007_1":
            return self.charts_v007_1(data)
        else:
            return None

    def linkert_scale(self,id,chart,data,id_load):
        global control
        return html.Div(className="col s12", children=[
                   html.H5(className="center blue-text", children=[str("O "+chart+" responde a pergunta muito bem.")]),
                   html.H6(className="center blue-text", children=[str("*Indique sua opinião sobre a seguinte afirmacao:")]),
                   html.Div(children=[
                       dcc.RadioItems(
                            id=id,
                            className="likert",
                            options=[
                                {'label': 'Discordo totalmente', 'value': 'strong_disagree'},
                                {'label': 'Discordo parcialmente', 'value': 'partially_disagree'},
                                {'label': 'Discordo levemente', 'value': 'slightly_disagree'},
                                {'label': 'Não concordo e nem discordo', 'value': 'neutral'},
                                {'label': 'Concordo levemente', 'value': 'slightly_agree'},
                                {'label': 'Concordo parcialmente', 'value': 'partially_agree'},
                                {'label': 'Concordo totalmente', 'value': 'strong_agree'},
                            ],
                            value=control.load_frontend_data_view(id_load,str(id),data),
                            labelStyle={'display': 'inline-block'}
                        ),
                   ]),
                   html.Br(),
               ])        

    def select_chart(self,id,labels,values,data,id_load):
        global control
        options = []
        
        for i in range(0,len(labels)):
            options.append({'label': labels[i], 'value': values[i]})

        return html.Div(className="input-field col s12", children=[
                    html.P(children=[
                        html.Label(className="left blue-text", children=["*Selecione o gráfico que melhor responde a pergunta:"]),
                    ]),
                    dcc.Dropdown(
                        id=id,
                        placeholder="",
                        options=options,
                        value=control.load_frontend_data_view(id_load,"preference_chart",data),
                        searchable=False,
                        clearable=False,
                        style={'color': '#2196f3'}
                    )
                ])

    def chart_view(self,charts,chart_ids,id_select,id_comments,data,id_load,id_label):
        div_charts = []
        div_id = []
        labels = []
        
        for i in range(0,len(charts)):
            div_id.append(str("div_"+chart_ids[i]))
            labels.append(str("Gráfico "+str(i+1)))

        for i in range(0,len(charts)):
            div_charts.append(
                html.Div(id=div_id[i], className="row center", children=[ #red accent-1
                    html.Div(className="col s12", children=[
                        html.H4(className="header left blue-text", children=[labels[i]]),
                        html.Br(),html.Br()
                    ]),
                    self.div_chart(charts[i]), #Chart
                    self.linkert_scale(chart_ids[i],labels[i],data,str(id_load+id_label)), #Linkert scale options
                ])
            )

        div_charts.append(
            html.Div(className="row", children=[
                self.select_chart(id_select,labels,chart_ids,data,str(id_load+id_label)), #Dropdown selection
            ]),
        )

        div_charts.append(
            html.Div(className="row center", children=[
                html.Div(className="input-field col s12",children=[
                    html.P(children=[
                        html.Label(className="left blue-text", children=["Você tem algum comentário sobre os gráficos?"]),
                    ]),
                    dcc.Input(id=str(id_comments+id_label), placeholder="", type='text',value=control.load_frontend_data(str(id_comments+id_label),data))
                ]),
            ])
        )

        div_charts.append(html.Br())        
        
        return html.Div(children=div_charts)
                
    def div_chart(self,charts):
        div_charts = []
        number_cols = 12/len(charts)

        for i in range(0,len(charts)):
            div_charts.append(
                html.Div(className=str("col s"+str(int(number_cols))+" center"),children=[
                    charts[i]
                ])
            )

        return html.Div(className="row center",children=div_charts)

    def charts_v001_1(self,data):
        global view1 
        view1.generate_dataset(number_students = 20, number_assigns = 10, students_names = students)
        
        id_select="id_chart_v001_1"
        
        charts = [[view1.graph_01()],                  #1
                  [view1.graph_02(),view1.graph_06()], #2
                  [view1.graph_04(),view1.graph_08()], #3
                  [view1.graph_10(),view1.graph_12()], #4
                  [view1.graph_26(),view1.graph_27()], #5
                  [view1.graph_29()],                  #6
                  [view1.graph_31(),view1.graph_32()], #7
                  [view1.graph_34()],                  #8  
                  [view1.graph_35()],                  #9
                  [view1.graph_38()],                  #10
                  [view1.graph_44()],                  #11
                  [view1.graph_47()],                  #12
                ]

        chart_ids = ["chart_01", #1
                     "chart_02", #2
                     "chart_04", #3
                     "chart_10", #4
                     "chart_26", #5
                     "chart_29", #6
                     "chart_31", #7
                     "chart_34", #8
                     "chart_35", #9
                     "chart_38", #10
                     "chart_44", #11
                     "chart_47", #12
                    ]
        
        return self.chart_view(charts,chart_ids,id_select,str("comments_id_chart_v"),data,"user_V","001_1")

    def charts_v001_2(self,data):
        global view1 
        view1.generate_dataset(number_students = 20, number_assigns = 10, students_names = students)
        
        id_select="id_chart_v001_2"

        charts = [[view1.graph_14(),view1.graph_18()], #1
                  [view1.graph_16(),view1.graph_20()], #2
                  [view1.graph_22(),view1.graph_24()], #3
                  [view1.graph_30()],                  #4
                  [view1.graph_36()],                  #5
                  [view1.graph_37()],                  #6
                  [view1.graph_41()],                  #7
                  [view1.graph_50()],                  #8
                  [view1.graph_53()],                  #9
                ]

        chart_ids = ["chart_14", #1
                     "chart_16", #2
                     "chart_22", #3
                     "chart_30", #4
                     "chart_36", #5
                     "chart_37", #6
                     "chart_41", #7
                     "chart_50", #8
                     "chart_53", #9
                    ]

        return self.chart_view(charts,chart_ids,id_select,str("comments_id_chart_v"),data,"user_V","001_2")

    def charts_v008_1(self,data):
        global view8
        view8.generate_dataset(number_students=35, number_weeks=7, students_names = students)

        id_select="id_chart_v008_1"

        charts = [[view8.graph_01()], #1
                  [view8.graph_02()], #2
                  [view8.graph_04()], #3
                  [view8.graph_05()], #4
                  [view8.graph_08()], #5
                  [view8.graph_10()], #6
                  ]

        chart_ids = ["chart_01", #1
                     "chart_02", #2
                     "chart_04", #3
                     "chart_05", #4
                     "chart_08", #5
                     "chart_10", #6
                    ]

        return self.chart_view(charts,chart_ids,id_select,str("comments_id_chart_v"),data,"user_V","008_3")

    def charts_v008_2(self,data):
        global view8
        view8.generate_dataset(number_students=35, number_weeks=7, students_names = students)

        id_select="id_chart_v008_2"

        charts = [[view8.graph_03()], #1
                  [view8.graph_06()], #2
                  [view8.graph_07()], #3
                  [view8.graph_09()], #4
                  [view8.graph_11()], #5
                  ]

        chart_ids = ["chart_03", #1
                     "chart_06", #2
                     "chart_07", #3
                     "chart_09", #4
                     "chart_11", #5
                    ]

        return self.chart_view(charts,chart_ids,id_select,str("comments_id_chart_v"),data,"user_V","008_4")

    def charts_v002_1(self,data):
        global view2
        view2.generate_dataset(number_students = 20, students_names = students)
    
        id_select="id_chart_v002_1"
        charts = [[view2.graph_01()], #1
                  [view2.graph_02()], #2
                  [view2.graph_03()], #3
                  [view2.graph_05()], #4
                  [view2.graph_07()], #5
                  [view2.graph_08()], #6
                  [view2.graph_09()], #7
                  [view2.graph_10()], #8
                  [view2.graph_11()], #9
                  [view2.graph_12()], #10
                ]
        
        chart_ids = ["chart_01", #1
                     "chart_02", #2
                     "chart_03", #3
                     "chart_05", #4
                     "chart_07", #5
                     "chart_08", #6
                     "chart_09", #7
                     "chart_10", #8
                     "chart_11", #9
                     "chart_12", #10
                    ] 
        
        return self.chart_view(charts,chart_ids,id_select,str("comments_id_chart_v"),data,"user_V","002_5")

    def charts_v003_1(self,data):
        global view3
        view3.generate_dataset(number_students = 20, students_names = students)

        id_select="id_chart_v003_1"
        charts = [[view3.graph_01()], #1
                  [view3.graph_02()], #2
                  [view3.graph_04()], #3
                  [view3.graph_06()], #4
                  [view3.graph_08()], #5
                  [view3.graph_09()], #6
                  [view3.graph_10()], #7
                 ] 
        
        chart_ids = ["chart_01", #1
                     "chart_02", #2
                     "chart_04", #3
                     "chart_06", #4
                     "chart_08", #5
                     "chart_09", #6
                     "chart_10", #7
                    ]
        
        return self.chart_view(charts,chart_ids,id_select,str("comments_id_chart_v"),data,"user_V","003_7")

    def charts_v004_1(self,data):
        global view4
        view4.generate_dataset(number_students = 20, students_names = students)

        id_select="id_chart_v004_1"
        charts = [[view4.graph_01()], #1
                  [view4.graph_02()], #2
                  [view4.graph_03()], #3
                  [view4.graph_04()], #4
                  [view4.graph_05()], #5
                  [view4.graph_06()], #6
                  [view4.graph_07()], #7
                  [view4.graph_08()], #8
                  [view4.graph_09()], #9
                  [view4.graph_11()], #10
                 ]
        
        chart_ids = ["chart_01", #1
                     "chart_02", #2
                     "chart_03", #3
                     "chart_04", #4
                     "chart_05", #5
                     "chart_06", #6
                     "chart_07", #7
                     "chart_08", #8
                     "chart_09", #9
                     "chart_11", #10
                    ]
        
        return self.chart_view(charts,chart_ids,id_select,str("comments_id_chart_v"),data,"user_V","004_9")

    def charts_v010_1(self,data):
        global view10
        view10.generate_dataset(number_students=35, number_video=10, students_names = students)

        id_select="id_chart_v010_1"
        charts = [[view10.graph_01()],                   #1
                  [view10.graph_02()],                   #2
                  [view10.graph_03(),view10.graph_05()], #3
                  [view10.graph_07(),view10.graph_09()], #4
                  [view10.graph_11(),view10.graph_13()], #5
                  [view10.graph_15(),view10.graph_16()], #6
                  [view10.graph_18()],                   #7
                  [view10.graph_19(),view10.graph_20()], #8
                  [view10.graph_22()],                   #9
                  [view10.graph_23()],                   #10
                  [view10.graph_24()],                   #11
                  [view10.graph_27()],                   #12
                  [view10.graph_30()],                   #13
                 ]
        
        chart_ids = ["chart_01", #1
                     "chart_02", #2
                     "chart_03", #3
                     "chart_07", #4
                     "chart_11", #5
                     "chart_15", #6
                     "chart_18", #7
                     "chart_19", #8
                     "chart_22", #9
                     "chart_23", #10
                     "chart_24", #11
                     "chart_27", #12
                     "chart_30", #13
                    ]
        
        return self.chart_view(charts,chart_ids,id_select,str("comments_id_chart_v"),data,"user_V","0010_10")

    def charts_v005_1(self,data):
        global view5
        view5.generate_dataset(number_students = 60, students_names = students)

        id_select="id_chart_v005_1"
        charts = [[view5.graph_01()], #1
                  [view5.graph_02()], #2
                  [view5.graph_09()], #3
                  [view5.graph_10()], #4
                  [view5.graph_17()], #5
                  [view5.graph_18()], #6
                 ]
        
        chart_ids = ["chart_01", #1
                     "chart_02", #2
                     "chart_09", #3
                     "chart_10", #4
                     "chart_17", #5
                     "chart_18", #6
                    ]
        
        return self.chart_view(charts,chart_ids,id_select,str("comments_id_chart_v"),data,"user_V","005_11")

    def charts_v006_1(self,data):
        global view6
        view6.generate_dataset(number_students = 60, students_names = students)

        id_select="id_chart_v006_1"
        charts = [[view6.graph_01()], #1
                  [view6.graph_02()], #2
                  [view6.graph_06()], #3
                  [view6.graph_10()], #4
                 ]
        
        chart_ids = ["chart_01", #1
                     "chart_02", #2
                     "chart_06", #3
                     "chart_10", #4
                    ]
        
        return self.chart_view(charts,chart_ids,id_select,str("comments_id_chart_v"),data,"user_V","006_18")

    def charts_v007_1(self,data):
        global view7
        view7.generate_dataset(number_students = 60, students_names = students)

        id_select="id_chart_v007_1"
        charts = [[view7.graph_01()], #1
                  [view7.graph_02()], #2
                  [view7.graph_03()], #3
                  [view7.graph_04()], #4
                 ]
        
        chart_ids = ["chart_01", #1
                     "chart_02", #2
                     "chart_03", #3
                     "chart_04", #4
                    ]

        return self.chart_view(charts,chart_ids,id_select,str("comments_id_chart_v"),data,"user_V","007_23")

    def charts_v009_1(self,data):
        # global view9
        # return self.chart_view(charts,chart_ids,id_select,str("comments_id_chart_v"),data,"user_V","009_8")
        pass

    def charts_v011_1(self,data):
        # global view11
        # return self.chart_view(charts,chart_ids,id_select,str("comments_id_chart_v"),data,"user_V","011_22")
        pass