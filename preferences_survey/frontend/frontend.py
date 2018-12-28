import dash
import dash_core_components as dcc
import dash_html_components as html

from backend import backend

control = backend.backend()

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
        return html.H5(className="header center red-text", children=["Preencha todos os campos"]),

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
                    html.Div(id='intermediate-value', style={'display': 'none'}),
                    html.Div(id='page-content')
                ])

    def survey_send(self,id,href=""):
        return html.Div(className="container", children=[
                    html.Div(className="row", children=[
                        html.Div(className="col s12",children=[
                            html.Div(className="row center", children=[
                                dcc.Link('Avançar', id=id,className="waves-effect waves-light btn-large", href=href),
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

    def survey_profile(self):
        return html.Div(className="container", children=[
                    html.Div(className="row", children=[
                        html.Div(className="col s12",children=[
                            html.Div(className="row center", children=[
                                html.H3(className="header center blue-text", children=["Sobre você"]),
                                html.Br(),html.Br()
                            ]),
                            ############################################################################################
                            html.Div(className="row", children=[
                                html.Div(className="input-field col s8", children=[
                                    html.Label(className="left blue-text", children=["*Nome completo:"]),
                                ]),
                                html.Div(className="input-field col s2", children=[
                                    html.Label(className="left blue-text", children=["*Gênero:"]),
                                ]),
                                html.Div(className="input-field col s2", children=[
                                    html.Label(className="left blue-text", children=["*Idade:"]),
                                ]),
                            ]),
                            ############################################################################################
                            html.Div(className="row center", children=[
                                html.Div(className="input-field col s8",children=[
                                    dcc.Input(id='user_name', placeholder="", type='text',value="")
                                ]),
                                html.Div(className="input-field col s2", children=[
                                    dcc.Dropdown(
                                        id='user_gender',
                                        placeholder="M ou F",
                                        options=[
                                            {'label': 'Masculino', 'value': 'M'},
                                            {'label': 'Feminino', 'value': 'F'},
                                            
                                        ],
                                        value="",
                                        searchable=False,
                                        clearable=True,
                                        style={'color': '#2196f3'}
                                    ),
                                ]),
                                html.Div(className="input-field col s2",children=[
                                    dcc.Input(id='user_age', placeholder="20,anos, 30 anos, etc.", type='text',value="")
                                ]),
                            ]),
                            ############################################################################################
                            html.Div(className="row", children=[
                                html.Div(className="input-field col s4", children=[
                                    html.Label(className="left blue-text", children=["*Email:"]),
                                ]),
                                html.Div(className="input-field col s8", children=[
                                    html.Label(className="left blue-text", children=["*Estado e cidade onde trabalha:"]),
                                ])
                            ]),
                            ############################################################################################
                            html.Div(className="row center", children=[
                                html.Div(className="input-field col s4",children=[
                                    dcc.Input(id='user_email', placeholder="user@gmail.com", type='text',value="")
                                ]),
                                html.Div(className="input-field col s8",children=[
                                    dcc.Input(id='user_place_work', placeholder="São Luís, Maranhão", type='text',value="")
                                ])
                            ]),
                            ############################################################################################
                            html.Div(className="row", children=[
                                html.Div(className="input-field col s8", children=[
                                    html.Label(className="left blue-text", children=["*Área de formação:"]),
                                ]),
                                html.Div(className="input-field col s4", children=[
                                    html.Label(className="left blue-text", children=["*Grau de escolaridade:"]),
                                ]),
                            ]),
                            ############################################################################################
                            html.Div(className="row center", children=[
                                html.Div(className="input-field col s8",children=[
                                    dcc.Input(id='user_scholarship', placeholder="Área de formação", type='text',value="")
                                ]),
                                html.Div(className="input-field col s4", children=[
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
                                        value="",
                                        searchable=False,
                                        clearable=True,
                                        style={'color': '#2196f3'}
                                    ),
                                ])
                            ]),
                            ############################################################################################
                            html.Div(className="row", children=[
                                html.Div(className="input-field col s6", children=[
                                    html.Label(className="left blue-text", children=["*Profissão:"]),
                                ]),
                                html.Div(className="input-field col s6", children=[
                                    html.Label(className="left blue-text", children=["*Já desenvolveu algum programa?"]),
                                ]),
                            ]),
                            ############################################################################################
                            html.Div(className="row center", children=[
                                html.Div(className="input-field col s6",children=[
                                    dcc.Input(id='user_job', placeholder="Professor, Instrutor, Tutor, etc", type='text',value="")
                                ]),
                                html.Div(className="input-field col s6", children=[
                                    dcc.Dropdown(
                                        id='user_programming_xp',
                                        placeholder="Sim ou Não",
                                        options=[
                                            {'label': 'Sim', 'value': 'S'},
                                            {'label': 'Não', 'value': 'N'},
                                            
                                        ],
                                        value="",
                                        searchable=False,
                                        clearable=True,
                                        style={'color': '#2196f3'}
                                    ),
                                ])
                            ]),
                            ############################################################################################
                            # html.Div(className="row center", children=[
                            #     html.Div(className="input-field col s6",children=[
                            #         dcc.Input(id='user_programming_when', placeholder="Quando foi o último programa que você fez?", type='text',value="")
                            #     ]),
                            #     html.Div(className="input-field col s6",children=[
                            #         dcc.Input(id='user_programming_language', placeholder="Em que linguagem foi feito seu último programa?", type='text',value="")
                            #     ]),
                            # ]),
                            html.Br()
                        ]),
                    ])
                ])

    def survey_ead_xp(self):
        return html.Div(className="container", children=[
                    html.Div(className="row", children=[
                        html.Div(className="col s12",children=[
                            html.Div(className="row center", children=[
                                html.H3(className="header center blue-text", children=["Sobre sua experiência com AVAs"]),
                                html.Br(),html.Br()
                            ]),
                            ############################################################################################
                            html.Div(className="row", children=[
                                html.Div(className="input-field col s7", children=[
                                    html.Label(className="left blue-text", children=["*Papeis desempenhados na utilização do AVA:"]),
                                ]),
                                html.Div(className="input-field col s5", children=[
                                    html.Label(className="left blue-text", children=["*Tempo de experiência na utilização de AVA:"]),
                                ]),
                            ]),
                            ############################################################################################
                            html.Div(className="row center", children=[
                                html.Div(className="input-field col s7",children=[
                                    dcc.Input(id='user_job_ead', placeholder="Professor, Tutor, Monitor, etc.", type='text',value="")
                                ]),
                                html.Div(className="input-field col s5",children=[
                                    dcc.Input(id='user_time_experience', placeholder="6 meses, 5 anos, 10 anos, etc.", type='text',value="")
                                ]),
                            ]),
                            ############################################################################################
                            html.Div(className="row", children=[
                                html.Div(className="input-field col s12", children=[
                                    html.Label(className="left blue-text", children=["*Instituições de ensino que trabalha (e que trabalhou) utilizando AVAs:"]),
                                ]),
                            ]),
                            ############################################################################################
                            html.Div(className="row center", children=[
                                html.Div(className="input-field col s12",children=[
                                    dcc.Input(id='user_organization_worked', placeholder="PUC-Rio, UFMA, UFRJ, UEMA, etc.", type='text',value="")
                                ]),
                            ]),
                            ############################################################################################
                            html.Div(className="row", children=[
                                html.Div(className="input-field col s12", children=[
                                    html.Label(className="left blue-text", children=["*Disciplinas ensinadas utilizando AVAs:"]),
                                ]),
                            ]),
                            ############################################################################################
                            html.Div(className="row center", children=[
                                html.Div(className="input-field col s12",children=[
                                    dcc.Input(id='user_subject', placeholder="Disciplinas de computação, Disciplinas da saúde (ex: Síndromes Geriátricas, etc.), Introdução a EaD, etc.", type='text',value="")
                                ]),
                            ]),
                            ############################################################################################
                            html.Div(className="row", children=[
                                html.Div(className="input-field col s4", children=[
                                    html.Label(className="left blue-text", children=["*Modalidade de ensino utilizando AVAs:"]),
                                ]),
                                html.Div(className="input-field col s8", children=[
                                    html.Label(className="left blue-text", children=["*AVAs que utiliza (e que já utilizou):"]),
                                ]),
                            ]),
                            ############################################################################################
                            html.Div(className="row center", children=[
                                html.Div(className="input-field col s4", children=[
                                    dcc.Dropdown(
                                        id='user_ead_modality',
                                        placeholder="Presencial ou a Distância",
                                        options=[
                                            {'label': 'A distância', 'value': 'Totalmente a distância'},
                                            {'label': 'Presencial', 'value': 'Totalmente presencial com apoio de AVAs'},
                                            {'label': 'Ambas', 'value': 'Ambas'},
                                        ],
                                        value="",
                                        searchable=False,
                                        clearable=True,
                                        style={'color': '#2196f3'}
                                    ),
                                ]),
                                html.Div(className="input-field col s8",children=[
                                    dcc.Input(id='user_avas_performed', placeholder="Moodle, Blackboard, etc.", type='text',value="")
                                ]),
                            ]),
                            ############################################################################################
                            html.Div(className="row", children=[
                                html.Div(className="input-field col s12", children=[
                                    html.Label(className="left blue-text", children=["*Modalidade de ensino utilizando AVAs:"]),
                                ]),
                            ]),
                            ############################################################################################
                            html.Div(className="row center", children=[
                                html.Div(className="input-field col s12",children=[
                                    dcc.Input(id='user_avas_resources', placeholder="Recursos que utiliza e já utilizou nos AVAs", type='text',value="")
                                ]),
                            ]),
                            ############################################################################################
                            html.Div(className="row", children=[
                                html.Div(className="input-field col s12", children=[
                                    html.Label(className="left blue-text", children=["*Faixa etária dos alunos que ensina (e que já ensinou) utilizando AVAs:"]),
                                ]),
                            ]),
                            ############################################################################################
                            html.Div(className="row center", children=[
                                html.Div(className="input-field col s12",children=[
                                    dcc.Input(id='user_students_age', placeholder="18 à 30 anos, 25 à 60 anos, etc.", type='text',value="")
                                ]),
                            ]),
                            ############################################################################################
                            html.Div(className="row", children=[
                                html.Div(className="input-field col s8", children=[
                                    html.Label(className="left blue-text", children=["*Área de formação dos alunos que ensina (e que já ensinou) utilizando AVAs:"]),
                                ]),
                                html.Div(className="input-field col s4", children=[
                                    html.Label(className="left blue-text", children=["*Grau de escolaridade desses alunos:"]),
                                ]),
                            ]),
                            ############################################################################################
                            html.Div(className="row center", children=[
                                html.Div(className="input-field col s8",children=[
                                    dcc.Input(id='user_students_scholarship', placeholder="Informática, Saúde, etc.", type='text',value="")
                                ]),
                                html.Div(className="input-field col s4", children=[
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
                                        value="",
                                        searchable=False,
                                        clearable=True,
                                        style={'color': '#2196f3'}
                                    ),
                                ])
                            ]),
                            ############################################################################################
                            html.Div(className="row", children=[
                                html.Div(className="input-field col s12", children=[
                                    html.Label(className="left blue-text", children=["*Quais informações dos alunos você considera relevante:"]),
                                ]),
                            ]),
                            ############################################################################################
                            html.Div(className="row center", children=[
                                html.Div(className="input-field col s12",children=[
                                    dcc.Input(id='user_students_meaningful', placeholder="", type='text',value="")
                                ]),
                            ]),
                            html.Br(),html.Br(),html.Br()
                        ]),
                    ])
                ])

    def survey_logs(self):
        return html.Div(className="container", children=[
                    html.Div(className="row", children=[
                        html.Div(className="col s12",children=[
                            html.Div(className="row center", children=[
                                html.H3(className="header center blue-text", children=["Em relação aos dados dos AVAs"]),
                                html.Br(),html.Br()
                            ]),
                            ############################################################################################
                            html.Div(className="row", children=[
                                html.Div(className="input-field col s12", children=[
                                    html.Label(className="left blue-text", children=["*Como você acompanha o andamento dos alunos durante o curso:"]),
                                ]),
                            ]),
                            ############################################################################################
                            html.Div(className="row center", children=[
                                html.Div(className="input-field col s12",children=[
                                    dcc.Input(id='user_students_progress', placeholder="", type='text',value="")
                                ]),
                            ]),
                            ############################################################################################
                            html.Div(className="row", children=[
                                html.Div(className="input-field col s12", children=[
                                    html.Label(className="left blue-text", children=["*Quais dados podem ser utilizados para predizer as notas dos alunos?"]),
                                ]),
                            ]),
                            ############################################################################################
                            html.Div(className="row center", children=[
                                html.Div(className="input-field col s12",children=[
                                    dcc.Input(id='user_logs_performance', placeholder="", type='text',value="")
                                ]),
                            ]),
                            ############################################################################################
                            html.Div(className="row", children=[
                                html.Div(className="input-field col s12", children=[
                                    html.Label(className="left blue-text", children=["*Quais dados podem ser utilizados para predizer se o aluno irá abandonar o curso?"]),
                                ]),
                            ]),
                            ############################################################################################
                            html.Div(className="row center", children=[
                                html.Div(className="input-field col s12",children=[
                                    dcc.Input(id='user_logs_dropout', placeholder="", type='text',value="")
                                ]),
                            ]),
                            ############################################################################################
                            html.Div(className="row", children=[
                                html.Div(className="input-field col s12", children=[
                                    html.Label(className="left blue-text", children=["*Quais dados podem ser utilizados para avaliar o engajamento do aluno?"]),
                                ]),
                            ]),
                            ############################################################################################
                            html.Div(className="row center", children=[
                                html.Div(className="input-field col s12",children=[
                                    dcc.Input(id='user_logs_engagement', placeholder="", type='text',value="")
                                ]),
                            ]),
                            ############################################################################################
                            html.Div(className="row", children=[
                                html.Div(className="input-field col s12", children=[
                                    html.Label(className="left blue-text", children=["Caso você faça análise de algum dado de acesso ou interação dos estudantes no AVA:"]),
                                ]),
                            ]),
                            ############################################################################################
                            html.Div(className="row", children=[
                                html.Div(className="input-field col s6", children=[
                                    html.Label(className="left blue-text", children=["quais dados você analisa?"]),
                                ]),
                                html.Div(className="input-field col s6", children=[
                                    html.Label(className="left blue-text", children=["como esses dados são apresentados pra você?"]),
                                ]),
                            ]),
                            ############################################################################################
                            html.Div(className="row center", children=[
                                html.Div(className="input-field col s6",children=[
                                    dcc.Input(id='user_logs_analyse', placeholder="Acesso ao AVA, realização de tarefas, postagem no fórum, etc.", type='text',value="")
                                ]),
                                html.Div(className="input-field col s6",children=[
                                    dcc.Input(id='user_logs_presentation', placeholder="Em uma tabela, em gráfico de pizza, em gráfico de barra, etc.", type='text',value="")
                                ]),
                            ]),
                            ############################################################################################
                            html.Div(className="row", children=[
                                html.Div(className="input-field col s12", children=[
                                    html.Label(className="left blue-text", children=["Caso exista algum dado que você gostaria de analisar:"]),
                                ]),
                            ]),
                            ############################################################################################
                            html.Div(className="row", children=[
                                html.Div(className="input-field col s6", children=[
                                    html.Label(className="left blue-text", children=["quais são?"]),
                                ]),
                                html.Div(className="input-field col s6", children=[
                                    html.Label(className="left blue-text", children=["como eles devem ser apresentados?"]),
                                ]),
                            ]),
                            ############################################################################################
                            html.Div(className="row center", children=[
                                html.Div(className="input-field col s6",children=[
                                    dcc.Input(id='user_logs_would_analyse', placeholder="Acesso ao AVA, realização de tarefas, postagem no fórum, etc.", type='text',value="")
                                ]),
                                html.Div(className="input-field col s6",children=[
                                    dcc.Input(id='user_logs_would_analyse_presentation', placeholder="Em uma tabela, em gráfico de pizza, em gráfico de barra, etc.", type='text',value="")
                                ]),
                            ]),
                            ############################################################################################
                            html.Br(),html.Br(),html.Br()
                        ])
                    ])
                ])

    def survey_student_information(self):
        global control
        options = []
        values = control.get_all_view_names()

        for i in range(0,len(values)):
            options.append({'label': control.get_view_label(values[i]), 'value': values[i]})

        return html.Div(className="container", children=[
                    html.Div(className="row", children=[
                        html.Div(className="col s12",children=[
                            html.Div(className="row center", children=[
                                html.H3(className="header center blue-text", children=["Sobre dados de interação e acesso dos estudantes"]),
                                html.Br(),html.Br()
                            ]),
                            ############################################################################################
                            html.Div(className="row", children=[
                                html.Div(className="input-field col s12", children=[
                                    html.Label(className="left blue-text", children=["Selecione os dados que você analisa ou que gostaria de analisar:"]),
                                ]),
                            ]),
                            ############################################################################################
                            html.Div(className="row", children=[
                                html.Div(className="input-field col s12", children=[
                                    html.Label(className="left red-text", children=["(é possível selecionar mais de uma opção)"]),
                                ]),
                            ]),
                            ############################################################################################
                            html.Div(className="row center", children=[
                                html.Div(className="input-field col s12",children=[
                                    dcc.Dropdown(
                                        id='user_interaction_access_students_logs',
                                        placeholder="",
                                        options = options,
                                        value="",
                                        searchable=True,
                                        multi=True,
                                        clearable=False,
                                        style={'color': '#2196f3'}
                                    )
                                ]),
                            ]),
                            ############################################################################################
                            html.Div(className="row", children=[
                                html.Div(className="input-field col s12", children=[
                                    html.Label(className="left blue-text", children=["Há mais algum dado que você analisa (ou gostaria de analisar) e que não foi apresentada?"]),
                                ]),
                            ]),
                            ############################################################################################
                            html.Div(className="row center", children=[
                                html.Div(className="input-field col s12",children=[
                                    dcc.Input(id='user_interaction_access_students_logs_others', placeholder="", type='text',value="")
                                ]),
                            ]),
                            html.Br(),html.Br(),html.Br(),
                            html.Br(),html.Br(),html.Br(),
                        ])
                    ])
                ])

        #Tarefas feitas pelos estudantes, V001
        #Acesso dos estudantes aos materiais (ex: videos, ebooks, etc.), V002
        #Interação dos estudantes no fórum (ex: postagens, acessos, etc.), V003
        #Tempo de permanência dos estudantes nos vídeos, V004
        #Correlação entre as notas e os logs de acesso/interação dos estudantes, V005
        #Correlação entre o perfil (idade, cidade de origem, etc.) e os logs de acesso/interação dos estudantes, V006
        #Predição das notas que os estudante terão ao final do curso e quais abandonarão, V007
        #Acesso dos estudantes no AVA por dia ou semana, V008
        #Interação dos estudantes nos vídeos (play, pause, backward, forward), V009
        #Vídeos que os estudantes entenderam e não entenderam, V010
        #Padrão de navegação dos estudantes no AVA, V011
        

    def survey_visualization(self):
        return html.Div(className="container", children=[
                    html.Div(className="row", children=[
                        html.Div(className="col s12",children=[
                            html.Div(className="row center", children=[
                                html.H3(className="header center blue-text", children=["Visualizações"]),
                                html.Br(),html.Br()
                            ]),
                            ############################################################################################
                            html.Div(className="row", children=[
                                html.Div(className="input-field col s12", children=[
                                    html.Label(className="left blue-text", children=["Com que frequência você:"]),
                                ]),
                            ]),
                            ############################################################################################
                            html.Div(className="row", children=[
                                html.Div(className="input-field col s6", children=[
                                    html.Label(className="left blue-text", children=["lê e interpreta gráficos?"]),
                                ]),
                                html.Div(className="input-field col s6", children=[
                                    html.Label(className="left blue-text", children=["cria gráficos?"]),
                                ]),
                            ]),
                            ############################################################################################
                            html.Div(className="row center", children=[
                                html.Div(className="input-field col s6", children=[
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
                                        value="",
                                        searchable=False,
                                        clearable=True,
                                        style={'color': '#2196f3'}
                                    ),
                                ]),
                                html.Div(className="input-field col s6", children=[
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
                                        value="",
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

    def survey_chart_preference(self,label):
        return html.Div(className="container", children=[
                    html.Div(className="row", children=[
                        html.Div(className="col s12",children=[
                            html.Div(className="row center", children=[
                                html.H3(className="header center blue-text", children=[label]),
                                html.Br(),html.Br()
                            ]),
                        ]),
                    ]),
                    html.Br(),html.Br(),html.Br()
                ])