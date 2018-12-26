import dash
import dash_core_components as dcc
import dash_html_components as html

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
                            html.Div(className="row center", children=[
                                html.H3(className="header center blue-text", children=["Olá."]),
                                html.Br(),
                                html.H3(className="header center blue-text", children=["Essa é uma pesquisa com fins estritamente acadêmicos sobre preferências de visualizações de logs de acesso e interação em Ambientes Virtuais de Aprendizagem (AVAs)."]),
                                html.Br(),
                                html.H3(className="header center blue-text", children=["Ressaltamos que sua participação é voluntária e todas as informações fornecidas serão mantidas anonimizadas."]),
                                html.Br(),html.Br()
                            ]),
                        ]),
                    ])
                ])

    def survey_filter(self):
        return html.Div(className="container", children=[
                    html.Div(className="row", children=[
                        html.Div(className="col s12",children=[
                            html.Div(className="row center", children=[                                
                                html.H2(className="header center blue-text", children=["Você tem experiência como instrutor ou tutor ou monitor ou professor de EaD"]),
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
                            html.Div(className="row center", children=[
                                html.Div(className="input-field col s8",children=[
                                    dcc.Input(id='user_name', placeholder="Nome completo", type='text',value="")
                                ]),
                                html.Div(className="input-field col s2", children=[
                                    dcc.Dropdown(
                                        id='user_gender',
                                        placeholder="Gênero",
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
                                    dcc.Input(id='user_age', placeholder="Idade", type='text',value="")
                                ]),
                            ]),
                            ############################################################################################
                            html.Div(className="row center", children=[
                                html.Div(className="input-field col s4",children=[
                                    dcc.Input(id='user_email', placeholder="Email", type='text',value="")
                                ]),
                                html.Div(className="input-field col s8",children=[
                                    dcc.Input(id='user_place_work', placeholder="Estado e cidade onde trabalha", type='text',value="")
                                ])
                            ]),
                            ############################################################################################
                            html.Div(className="row center", children=[
                                html.Div(className="input-field col s4",children=[
                                    dcc.Input(id='user_scholarship', placeholder="Área de formação", type='text',value="")
                                ]),
                                html.Div(className="input-field col s4",children=[
                                    dcc.Input(id='user_job', placeholder="Ocupação", type='text',value="")
                                ]),
                                html.Div(className="input-field col s4", children=[
                                    dcc.Dropdown(
                                        id='user_programming_xp',
                                        placeholder="Experiência em programação",
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
                            html.Br(),html.Br(),html.Br()
                        ]),
                    ])
                ])

    def survey_ead_xp(self):
        return html.Div(className="container", children=[
                    html.Div(className="row", children=[
                        html.Div(className="col s12",children=[
                            html.Div(className="row center", children=[
                                html.H3(className="header center blue-text", children=["Sobre sua experiência com EaD"]),
                                html.Br(),html.Br()
                            ]),
                            ############################################################################################
                            html.Div(className="row center", children=[
                                html.Div(className="input-field col s7",children=[
                                    dcc.Input(id='user_job_ead', placeholder="Papeis desempenhados no ensino a distância (ex: Professor, Tutor, Monitor, etc.)", type='text',value="")
                                ]),
                                html.Div(className="input-field col s5",children=[
                                    dcc.Input(id='user_time_experience', placeholder="Tempo de experiência no EaD", type='text',value="")
                                ]),
                            ]),
                            ############################################################################################
                            html.Div(className="row center", children=[
                                html.Div(className="input-field col s12",children=[
                                    dcc.Input(id='user_organization_worked', placeholder="Instituição de ensino que trabalha (ou que trabalhou) com EaD", type='text',value="")
                                ]),
                            ]),
                            ############################################################################################
                            html.Div(className="row center", children=[
                                html.Div(className="input-field col s12",children=[
                                    dcc.Input(id='user_subject', placeholder="Disciplinas ensinadas no EaD", type='text',value="")
                                ]),
                            ]),
                            ############################################################################################
                            html.Div(className="row center", children=[
                                html.Div(className="input-field col s4", children=[
                                    dcc.Dropdown(
                                        id='user_ead_modality',
                                        placeholder="Modalidade de EaD com experiência",
                                        options=[
                                            {'label': 'Totalmente a distância', 'value': 'Totalmente a distância'},
                                            {'label': 'Presencial com apoio de AVAs', 'value': 'Presencial com apoio de AVAs'},
                                            {'label': 'Ambas', 'value': 'Ambas'},
                                        ],
                                        value="",
                                        searchable=False,
                                        clearable=True,
                                        style={'color': '#2196f3'}
                                    ),
                                ]),
                                html.Div(className="input-field col s8",children=[
                                    dcc.Input(id='user_avas_performed', placeholder="AVAs que utiliza e já utilizou", type='text',value="")
                                ]),
                            ]),
                            ############################################################################################
                            html.Div(className="row center", children=[
                                html.Div(className="input-field col s12",children=[
                                    dcc.Input(id='user_avas_resources', placeholder="Recursos que utiliza e já utilizou nos AVAs", type='text',value="")
                                ]),
                            ]),
                            ############################################################################################
                            html.Div(className="row center", children=[
                                html.Div(className="input-field col s12",children=[
                                    dcc.Input(id='user_profile', placeholder="Perfil dos alunos que você ensina", type='text',value="")
                                ]),
                            ]),
                            ############################################################################################
                            html.Div(className="row center", children=[
                                html.Div(className="input-field col s12",children=[
                                    dcc.Input(id='user_students_meaningful', placeholder="Informações relevantes dos alunos", type='text',value="")
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
                                html.H3(className="header center blue-text", children=["Em relação aos logs dos AVAs"]),
                                html.Br(),html.Br()
                            ]),
                            ############################################################################################
                            html.Div(className="row center", children=[
                                html.Div(className="input-field col s12",children=[
                                    dcc.Input(id='user_logs_presentation', placeholder="Como os logs são apresentados pra você (ex: em uma tabela, gráfico de pizza, barra, etc.)", type='text',value="")
                                ]),
                            ]),
                            ############################################################################################
                            html.Div(className="row center", children=[
                                html.Div(className="input-field col s12",children=[
                                    dcc.Input(id='user_logs_analyse', placeholder="Caso você faça analisa logs, quais são os que você analisa", type='text',value="")
                                ]),
                            ]),
                            ############################################################################################
                            html.Div(className="row center", children=[
                                html.Div(className="input-field col s12",children=[
                                    dcc.Input(id='user_logs_would_analyse', placeholder="Caso há algum log que você gostaria de analisar, quais são eles", type='text',value="")
                                ]),
                            ]),
                            ############################################################################################
                            html.Div(className="row center", children=[
                                html.Div(className="input-field col s12",children=[
                                    dcc.Input(id='user_logs_performance', placeholder="Quais logs podem ser utilizados para indicar que o aluno terá boas notas", type='text',value="")
                                ]),
                            ]),
                            ############################################################################################
                            html.Div(className="row center", children=[
                                html.Div(className="input-field col s12",children=[
                                    dcc.Input(id='user_logs_engagement', placeholder="Quais os logs podem ser utilizados para avaliar o engajamento do aluno", type='text',value="")
                                ]),
                            ]),
                            html.Div(className="row center", children=[

                                #Tarefas realizadas pelos alunos  V01
                                #Acessos ao materiais  V02
                                #Interação do fórum  V03
                                #Acesso aos vídeos   V04
                                #Cluster de alunos  V05
                                #Perfil dos estudantes  V06
                                #Course completion??  V07
                                #Acesso dos estudantes  V08
                                #Interação nos vídeos  V09
                                #Curtidas nos vídeos  V10
                                #Navegação dos estudantes  V11
                            ]),
                            html.Br(),html.Br(),html.Br()
                        ])
                    ])
                ])

    def survey_visualization(self):
        return html.Div(className="container", children=[
                    html.Div(className="row", children=[
                        html.Div(className="col s12",children=[
                            html.Div(className="row center", children=[
                                html.H3(className="header center blue-text", children=["Visualizações"]),
                                html.Br(),html.Br()
                            ]),
                        ]),
                    ]),
                    html.Br(),html.Br(),html.Br()
                ])