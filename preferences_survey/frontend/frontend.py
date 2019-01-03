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
                                    html.P(children=[
                                        html.Label(className="left blue-text", children=["*Nome completo:"])
                                    ]),
                                    dcc.Input(id='user_name', placeholder="", type='text',value="")
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
                                        value="",
                                        searchable=False,
                                        clearable=True,
                                        style={'color': '#2196f3'}
                                    ),
                                ]),
                                html.Div(className="input-field col s2",children=[
                                    html.P(children=[
                                        html.Label(className="left blue-text", children=["*Idade:"]),
                                    ]),
                                    dcc.Input(id='user_age', placeholder="20,anos, 30 anos, etc.", type='text',value="")
                                ]),
                            ]),
                            ############################################################################################
                            html.Div(className="row center", children=[
                                html.Div(className="input-field col s6",children=[
                                    html.P(children=[
                                        html.Label(className="left blue-text", children=["*Estado e cidade onde nasceu (caso seja estranjeiro, informe o país):"]),
                                    ]),
                                    dcc.Input(id='user_place_birth', placeholder="São Luís, Maranhão", type='text',value="")
                                ]),
                                html.Div(className="input-field col s6",children=[
                                    html.P(children=[
                                        html.Label(className="left blue-text", children=["*Estado e cidade onde trabalha:"]),
                                    ]),
                                    dcc.Input(id='user_place_work', placeholder="São Luís, Maranhão", type='text',value="")
                                ])
                            ]),
                            ############################################################################################
                            html.Div(className="row center", children=[
                                html.Div(className="input-field col s8",children=[
                                    html.P(children=[
                                        html.Label(className="left blue-text", children=["*Área de formação:"]),
                                    ]),
                                    dcc.Input(id='user_scholarship', placeholder="Área de formação", type='text',value="")
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
                                        value="",
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
                                    dcc.Input(id='user_job', placeholder="Professor, Instrutor, Tutor, etc", type='text',value="")
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
                                    html.Label(className="left blue-text", children=["Caso já tenha desenvolvido algum programa de computador:"]),
                                ]),
                            ]),
                            ############################################################################################
                            html.Div(className="row center", children=[
                                html.Div(className="input-field col s6",children=[
                                    html.P(children=[
                                        html.Label(className="left blue-text", children=["Quando foi a última vez que você programou?"]),
                                    ]),
                                    dcc.Input(id='user_programming_last_time', placeholder="", type='text',value="")
                                ]),
                                html.Div(className="input-field col s6",children=[
                                    html.P(children=[
                                        html.Label(className="left blue-text", children=["Em que linguagem de programação?"]),
                                    ]),
                                    dcc.Input(id='user_programming_language', placeholder="", type='text',value="")
                                ]),
                            ]),
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
                            html.Div(className="row center", children=[
                                html.Div(className="input-field col s7",children=[
                                    html.P(children=[
                                        html.Label(className="left blue-text", children=["*Papeis desempenhados na utilização do AVAs:"]),
                                    ]),
                                    dcc.Input(id='user_job_ead', placeholder="Professor, Tutor, Monitor, etc.", type='text',value="")
                                ]),
                                html.Div(className="input-field col s5",children=[
                                    html.P(children=[
                                        html.Label(className="left blue-text", children=["*Tempo de experiência na utilização de AVAs:"]),
                                    ]),
                                    dcc.Input(id='user_time_experience', placeholder="6 meses, 5 anos, 10 anos, etc.", type='text',value="")
                                ]),
                            ]),
                            ############################################################################################
                            html.Div(className="row center", children=[
                                html.Div(className="input-field col s12",children=[
                                    html.P(children=[
                                        html.Label(className="left blue-text", children=["*Instituições de ensino que trabalha (e que trabalhou) utilizando AVAs:"]),
                                    ]),
                                    dcc.Input(id='user_organization_worked', placeholder="PUC-Rio, UFMA, UFRJ, UEMA, etc.", type='text',value="")
                                ]),
                            ]),
                            ############################################################################################
                            html.Div(className="row center", children=[
                                html.Div(className="input-field col s12",children=[
                                    html.P(children=[
                                        html.Label(className="left blue-text", children=["*Disciplinas ensinadas utilizando AVAs:"]),
                                    ]),
                                    dcc.Input(id='user_subject', placeholder="Disciplinas de computação, Disciplinas da saúde (ex: Síndromes Geriátricas, etc.), Introdução a EaD, etc.", type='text',value="")
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
                                        value="",
                                        searchable=False,
                                        clearable=True,
                                        style={'color': '#2196f3'}
                                    ),
                                ]),
                                html.Div(className="input-field col s6",children=[
                                    html.P(children=[
                                        html.Label(className="left blue-text", children=["*AVAs que utiliza (e que já utilizou):"]),
                                    ]),
                                    dcc.Input(id='user_avas_performed', placeholder="Moodle, Blackboard, etc.", type='text',value="")
                                ]),
                            ]),
                            ############################################################################################
                            html.Div(className="row center", children=[
                                html.Div(className="input-field col s12",children=[
                                    html.P(children=[
                                        html.Label(className="left blue-text", children=["*Recursos que utiliza e já utilizou nos AVAs:"]),
                                    ]),
                                    dcc.Input(id='user_avas_resources', placeholder="Vídeos, ebooks, fórum, chat, badges, etc.", type='text',value="")
                                ]),
                            ]),
                            ############################################################################################
                            html.Div(className="row center", children=[
                                html.Div(className="input-field col s12",children=[
                                    html.P(children=[
                                        html.Label(className="left blue-text", children=["*Faixa etária dos alunos que ensina (e que já ensinou) utilizando AVAs:"]),
                                    ]),
                                    dcc.Input(id='user_students_age', placeholder="18 à 30 anos, 25 à 60 anos, etc.", type='text',value="")
                                ]),
                            ]),
                            ############################################################################################
                            html.Div(className="row center", children=[
                                html.Div(className="input-field col s8",children=[
                                    html.P(children=[
                                        html.Label(className="left blue-text", children=["*Área de formação dos alunos que ensina (e que já ensinou) utilizando AVAs:"]),
                                    ]),
                                    dcc.Input(id='user_students_scholarship', placeholder="Informática, Saúde, etc.", type='text',value="")
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
                                        value="",
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
                            html.Div(className="row center", children=[
                                html.Div(className="input-field col s12",children=[
                                    html.P(children=[
                                        html.Label(className="left blue-text", children=["*Como você acompanha o andamento dos alunos durante o curso:"]),
                                    ]),
                                    dcc.Input(id='user_students_progress', placeholder="", type='text',value="")
                                ]),
                            ]),
                            ############################################################################################
                            html.Div(className="row center", children=[
                                html.Div(className="input-field col s12",children=[
                                    html.P(children=[
                                        html.Label(className="left blue-text", children=["*Quais dados podem ser utilizados para predizer as notas dos alunos?"]),
                                    ]),
                                    dcc.Input(id='user_logs_performance', placeholder="", type='text',value="")
                                ]),
                            ]),
                            ############################################################################################
                            html.Div(className="row center", children=[
                                html.Div(className="input-field col s12",children=[
                                    html.P(children=[
                                        html.Label(className="left blue-text", children=["*Quais dados podem ser utilizados para predizer se o aluno irá abandonar o curso?"]),
                                    ]),
                                    dcc.Input(id='user_logs_dropout', placeholder="", type='text',value="")
                                ]),
                            ]),
                            ############################################################################################
                            html.Div(className="row center", children=[
                                html.Div(className="input-field col s12",children=[
                                    html.P(children=[
                                        html.Label(className="left blue-text", children=["*Quais dados podem ser utilizados para avaliar o engajamento do aluno?"]),
                                    ]),
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
                            html.Div(className="row center", children=[
                                html.Div(className="input-field col s6",children=[
                                    html.P(children=[
                                        html.Label(className="left blue-text", children=["quais dados você analisa?"]),
                                    ]),
                                    dcc.Input(id='user_logs_analyse', placeholder="Acesso ao AVA, realização de tarefas, postagem no fórum, etc.", type='text',value="")
                                ]),
                                html.Div(className="input-field col s6",children=[
                                    html.P(children=[
                                        html.Label(className="left blue-text", children=["como esses dados são apresentados pra você?"]),
                                    ]),
                                    dcc.Input(id='user_logs_presentation', placeholder="Em uma tabela, em gráfico de pizza, em gráfico de barra, etc.", type='text',value="")
                                ]),
                            ]),
                            ############################################################################################
                            html.Br(),html.Br(),html.Br()
                        ])
                    ])
                ])

    def survey_student_information(self):
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
                                        html.Label(className="left blue-text", children=["Selecione os dados que você analisa ou que gostaria de analisar:"]),
                                    ]),
                                    html.Br(),
                                    dcc.Checklist(
                                        id="user_interaction_access_students_logs",
                                        options=options,
                                        values=[],
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
                                    dcc.Input(id='user_interaction_access_students_logs_others', placeholder="", type='text',value="")
                                ]),
                            ]),
                            ############################################################################################
                            html.Div(className="row center", children=[
                                html.Div(className="input-field col s12",children=[
                                    html.P(children=[
                                        html.Label(className="left blue-text", children=["Como você gostaria que esses dados fossem apresentados?"]),
                                    ]),
                                    dcc.Input(id='user_interaction_access_students_logs_presentation', placeholder="Em uma tabela, em gráfico de pizza, em gráfico de barra, etc.", type='text',value="")
                                ]),
                            ]),
                            html.Br(),html.Br(),html.Br(),
                            html.Br(),html.Br(),html.Br(),
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
                                        html.Label(className="left blue-text", children=["lê e interpreta gráficos?"]),
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
                                        value="",
                                        searchable=False,
                                        clearable=True,
                                        style={'color': '#2196f3'}
                                    ),
                                ]),
                                html.Div(className="input-field col s6", children=[
                                    html.P(children=[
                                        html.Label(className="left blue-text", children=["cria gráficos?"]),
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

    def survey_chart_preference(self,question,page):
        return html.Div(className="container", children=[
                    html.Div(className="row", children=[
                        html.Div(className="col s12",children=[
                            html.Div(className="row center", children=[
                                html.H3(className="header center blue-text", children=[question]),
                                html.Br(),html.Br()
                            ]),
                            self.survey_select_page(page)
                        ]),
                    ]),
                    html.Br(),html.Br(),html.Br()
                ])

    def survey_select_page(self,page):
        if page == "prefv001_1":
            return self.charts_v001_1()
        elif page == "prefv001_2":
            return self.charts_v001_2()
        elif page == "prefv008_1":
            return self.charts_v008_1()
        elif page == "prefv008_2":
            return self.charts_v008_2()
        elif page == "prefv002_1":
            return self.charts_v002_1()
        elif page == "prefv003_1":
            return self.charts_v003_1()
        elif page == "prefv009_1":
            return self.charts_v009_1()
        elif page == "prefv004_1":
            return self.charts_v004_1()
        elif page == "prefv010_1":
            return self.charts_v010_1()
        elif page == "prefv005_1":
            return self.charts_v005_1()
        elif page == "prefv006_1":
            return self.charts_v006_1()
        elif page == "prefv011_1":
            return self.charts_v011_1()
        elif page == "prefv007_1":
            return self.charts_v007_1()
        else:
            return None

    def charts_v001_1(self):
        return html.Div(children=[
                    html.Div(className="row", children=[
                        html.Div(className="input-field col s12", children=[
                            html.P(children=[
                                html.Label(className="left blue-text", children=["Numa escala de 1 à 7:"]),
                            ]),
                            #Aqui os charts
                        ]),
                    ]),
                    ############################################################################################
                    html.Div(className="row", children=[
                        html.Div(className="input-field col s12", children=[
                            html.P(children=[
                                html.Label(className="left blue-text", children=["Selecione o gráfico que melhor responde a pergunta:"]),
                            ]),
                            dcc.Dropdown(
                                id='user_chart_fit',
                                placeholder="",
                                options=[
                                    {'label': '1', 'value': '1'},
                                    {'label': '2', 'value': '2'},
                                    {'label': '3', 'value': '3'},
                                    {'label': '4', 'value': '4'},
                                    {'label': '5', 'value': '5'},
                                ],
                                value="",
                                searchable=False,
                                clearable=True,
                                style={'color': '#2196f3'}
                            ),
                        ]),
                    ]),
                ])

    def charts_v001_2(self):
        return html.Div(children=[
                    html.Div(className="row", children=[
                        html.Div(className="input-field col s12", children=[
                            html.P(children=[
                                html.Label(className="left blue-text", children=["Numa escala de 1 à 7:"]),
                            ]),
                            #Aqui os charts
                        ]),
                    ]),
                    ############################################################################################
                    html.Div(className="row", children=[
                        html.Div(className="input-field col s12", children=[
                            html.P(children=[
                                html.Label(className="left blue-text", children=["Selecione o gráfico que melhor responde a pergunta:"]),
                            ]),
                            dcc.Dropdown(
                                id='user_chart_fit',
                                placeholder="",
                                options=[
                                    {'label': '1', 'value': '1'},
                                    {'label': '2', 'value': '2'},
                                    {'label': '3', 'value': '3'},
                                    {'label': '4', 'value': '4'},
                                    {'label': '5', 'value': '5'},
                                ],
                                value="",
                                searchable=False,
                                clearable=True,
                                style={'color': '#2196f3'}
                            ),
                        ]),
                    ]),
                ])

    def charts_v008_1(self):
        return html.Div(children=[
                    html.Div(className="row", children=[
                        html.Div(className="input-field col s12", children=[
                            html.P(children=[
                                html.Label(className="left blue-text", children=["Numa escala de 1 à 7:"]),
                            ]),
                            #Aqui os charts
                        ]),
                    ]),
                    ############################################################################################
                    html.Div(className="row", children=[
                        html.Div(className="input-field col s12", children=[
                            html.P(children=[
                                html.Label(className="left blue-text", children=["Selecione o gráfico que melhor responde a pergunta:"]),
                            ]),
                            dcc.Dropdown(
                                id='user_chart_fit',
                                placeholder="",
                                options=[
                                    {'label': '1', 'value': '1'},
                                    {'label': '2', 'value': '2'},
                                    {'label': '3', 'value': '3'},
                                    {'label': '4', 'value': '4'},
                                    {'label': '5', 'value': '5'},
                                ],
                                value="",
                                searchable=False,
                                clearable=True,
                                style={'color': '#2196f3'}
                            ),
                        ]),
                    ]),
                ])

    def charts_v008_2(self):
        return html.Div(children=[
                    html.Div(className="row", children=[
                        html.Div(className="input-field col s12", children=[
                            html.P(children=[
                                html.Label(className="left blue-text", children=["Numa escala de 1 à 7:"]),
                            ]),
                            #Aqui os charts
                        ]),
                    ]),
                    ############################################################################################
                    html.Div(className="row", children=[
                        html.Div(className="input-field col s12", children=[
                            html.P(children=[
                                html.Label(className="left blue-text", children=["Selecione o gráfico que melhor responde a pergunta:"]),
                            ]),
                            dcc.Dropdown(
                                id='user_chart_fit',
                                placeholder="",
                                options=[
                                    {'label': '1', 'value': '1'},
                                    {'label': '2', 'value': '2'},
                                    {'label': '3', 'value': '3'},
                                    {'label': '4', 'value': '4'},
                                    {'label': '5', 'value': '5'},
                                ],
                                value="",
                                searchable=False,
                                clearable=True,
                                style={'color': '#2196f3'}
                            ),
                        ]),
                    ]),
                ])

    def charts_v002_1(self):
        return html.Div(children=[
                    html.Div(className="row", children=[
                        html.Div(className="input-field col s12", children=[
                            html.P(children=[
                                html.Label(className="left blue-text", children=["Numa escala de 1 à 7:"]),
                            ]),
                            #Aqui os charts
                        ]),
                    ]),
                    ############################################################################################
                    html.Div(className="row", children=[
                        html.Div(className="input-field col s12", children=[
                            html.P(children=[
                                html.Label(className="left blue-text", children=["Selecione o gráfico que melhor responde a pergunta:"]),
                            ]),
                            dcc.Dropdown(
                                id='user_chart_fit',
                                placeholder="",
                                options=[
                                    {'label': '1', 'value': '1'},
                                    {'label': '2', 'value': '2'},
                                    {'label': '3', 'value': '3'},
                                    {'label': '4', 'value': '4'},
                                    {'label': '5', 'value': '5'},
                                ],
                                value="",
                                searchable=False,
                                clearable=True,
                                style={'color': '#2196f3'}
                            ),
                        ]),
                    ]),
                ])

    def charts_v003_1(self):
        return html.Div(children=[
                    html.Div(className="row", children=[
                        html.Div(className="input-field col s12", children=[
                            html.P(children=[
                                html.Label(className="left blue-text", children=["Numa escala de 1 à 7:"]),
                            ]),
                            #Aqui os charts
                        ]),
                    ]),
                    ############################################################################################
                    html.Div(className="row", children=[
                        html.Div(className="input-field col s12", children=[
                            html.P(children=[
                                html.Label(className="left blue-text", children=["Selecione o gráfico que melhor responde a pergunta:"]),
                            ]),
                            dcc.Dropdown(
                                id='user_chart_fit',
                                placeholder="",
                                options=[
                                    {'label': '1', 'value': '1'},
                                    {'label': '2', 'value': '2'},
                                    {'label': '3', 'value': '3'},
                                    {'label': '4', 'value': '4'},
                                    {'label': '5', 'value': '5'},
                                ],
                                value="",
                                searchable=False,
                                clearable=True,
                                style={'color': '#2196f3'}
                            ),
                        ]),
                    ]),
                ])

    def charts_v009_1(self):
        return html.Div(children=[
                    html.Div(className="row", children=[
                        html.Div(className="input-field col s12", children=[
                            html.P(children=[
                                html.Label(className="left blue-text", children=["Numa escala de 1 à 7:"]),
                            ]),
                            #Aqui os charts
                        ]),
                    ]),
                    ############################################################################################
                    html.Div(className="row", children=[
                        html.Div(className="input-field col s12", children=[
                            html.P(children=[
                                html.Label(className="left blue-text", children=["Selecione o gráfico que melhor responde a pergunta:"]),
                            ]),
                            dcc.Dropdown(
                                id='user_chart_fit',
                                placeholder="",
                                options=[
                                    {'label': '1', 'value': '1'},
                                    {'label': '2', 'value': '2'},
                                    {'label': '3', 'value': '3'},
                                    {'label': '4', 'value': '4'},
                                    {'label': '5', 'value': '5'},
                                ],
                                value="",
                                searchable=False,
                                clearable=True,
                                style={'color': '#2196f3'}
                            ),
                        ]),
                    ]),
                ])

    def charts_v004_1(self):
        return html.Div(children=[
                    html.Div(className="row", children=[
                        html.Div(className="input-field col s12", children=[
                            html.P(children=[
                                html.Label(className="left blue-text", children=["Numa escala de 1 à 7:"]),
                            ]),
                            #Aqui os charts
                        ]),
                    ]),
                    ############################################################################################
                    html.Div(className="row", children=[
                        html.Div(className="input-field col s12", children=[
                            html.P(children=[
                                html.Label(className="left blue-text", children=["Selecione o gráfico que melhor responde a pergunta:"]),
                            ]),
                            dcc.Dropdown(
                                id='user_chart_fit',
                                placeholder="",
                                options=[
                                    {'label': '1', 'value': '1'},
                                    {'label': '2', 'value': '2'},
                                    {'label': '3', 'value': '3'},
                                    {'label': '4', 'value': '4'},
                                    {'label': '5', 'value': '5'},
                                ],
                                value="",
                                searchable=False,
                                clearable=True,
                                style={'color': '#2196f3'}
                            ),
                        ]),
                    ]),
                ])

    def charts_v010_1(self):
        return html.Div(children=[
                    html.Div(className="row", children=[
                        html.Div(className="input-field col s12", children=[
                            html.P(children=[
                                html.Label(className="left blue-text", children=["Numa escala de 1 à 7:"]),
                            ]),
                            #Aqui os charts
                        ]),
                    ]),
                    ############################################################################################
                    html.Div(className="row", children=[
                        html.Div(className="input-field col s12", children=[
                            html.P(children=[
                                html.Label(className="left blue-text", children=["Selecione o gráfico que melhor responde a pergunta:"]),
                            ]),
                            dcc.Dropdown(
                                id='user_chart_fit',
                                placeholder="",
                                options=[
                                    {'label': '1', 'value': '1'},
                                    {'label': '2', 'value': '2'},
                                    {'label': '3', 'value': '3'},
                                    {'label': '4', 'value': '4'},
                                    {'label': '5', 'value': '5'},
                                ],
                                value="",
                                searchable=False,
                                clearable=True,
                                style={'color': '#2196f3'}
                            ),
                        ]),
                    ]),
                ])

    def charts_v005_1(self):
        return html.Div(children=[
                    html.Div(className="row", children=[
                        html.Div(className="input-field col s12", children=[
                            html.P(children=[
                                html.Label(className="left blue-text", children=["Numa escala de 1 à 7:"]),
                            ]),
                            #Aqui os charts
                        ]),
                    ]),
                    ############################################################################################
                    html.Div(className="row", children=[
                        html.Div(className="input-field col s12", children=[
                            html.P(children=[
                                html.Label(className="left blue-text", children=["Selecione o gráfico que melhor responde a pergunta:"]),
                            ]),
                            dcc.Dropdown(
                                id='user_chart_fit',
                                placeholder="",
                                options=[
                                    {'label': '1', 'value': '1'},
                                    {'label': '2', 'value': '2'},
                                    {'label': '3', 'value': '3'},
                                    {'label': '4', 'value': '4'},
                                    {'label': '5', 'value': '5'},
                                ],
                                value="",
                                searchable=False,
                                clearable=True,
                                style={'color': '#2196f3'}
                            ),
                        ]),
                    ]),
                ])

    def charts_v006_1(self):
        return html.Div(children=[
                    html.Div(className="row", children=[
                        html.Div(className="input-field col s12", children=[
                            html.P(children=[
                                html.Label(className="left blue-text", children=["Numa escala de 1 à 7:"]),
                            ]),
                            #Aqui os charts
                        ]),
                    ]),
                    ############################################################################################
                    html.Div(className="row", children=[
                        html.Div(className="input-field col s12", children=[
                            html.P(children=[
                                html.Label(className="left blue-text", children=["Selecione o gráfico que melhor responde a pergunta:"]),
                            ]),
                            dcc.Dropdown(
                                id='user_chart_fit',
                                placeholder="",
                                options=[
                                    {'label': '1', 'value': '1'},
                                    {'label': '2', 'value': '2'},
                                    {'label': '3', 'value': '3'},
                                    {'label': '4', 'value': '4'},
                                    {'label': '5', 'value': '5'},
                                ],
                                value="",
                                searchable=False,
                                clearable=True,
                                style={'color': '#2196f3'}
                            ),
                        ]),
                    ]),
                ])

    def charts_v011_1(self):
        return html.Div(children=[
                    html.Div(className="row", children=[
                        html.Div(className="input-field col s12", children=[
                            html.P(children=[
                                html.Label(className="left blue-text", children=["Numa escala de 1 à 7:"]),
                            ]),
                            #Aqui os charts
                        ]),
                    ]),
                    ############################################################################################
                    html.Div(className="row", children=[
                        html.Div(className="input-field col s12", children=[
                            html.P(children=[
                                html.Label(className="left blue-text", children=["Selecione o gráfico que melhor responde a pergunta:"]),
                            ]),
                            dcc.Dropdown(
                                id='user_chart_fit',
                                placeholder="",
                                options=[
                                    {'label': '1', 'value': '1'},
                                    {'label': '2', 'value': '2'},
                                    {'label': '3', 'value': '3'},
                                    {'label': '4', 'value': '4'},
                                    {'label': '5', 'value': '5'},
                                ],
                                value="",
                                searchable=False,
                                clearable=True,
                                style={'color': '#2196f3'}
                            ),
                        ]),
                    ]),
                ])

    def charts_v007_1(self):
        return html.Div(children=[
                    html.Div(className="row", children=[
                        html.Div(className="input-field col s12", children=[
                            html.P(children=[
                                html.Label(className="left blue-text", children=["Numa escala de 1 à 7:"]),
                            ]),
                            #Aqui os charts
                        ]),
                    ]),
                    ############################################################################################
                    html.Div(className="row", children=[
                        html.Div(className="input-field col s12", children=[
                            html.P(children=[
                                html.Label(className="left blue-text", children=["Selecione o gráfico que melhor responde a pergunta:"]),
                            ]),
                            dcc.Dropdown(
                                id='user_chart_fit',
                                placeholder="",
                                options=[
                                    {'label': '1', 'value': '1'},
                                    {'label': '2', 'value': '2'},
                                    {'label': '3', 'value': '3'},
                                    {'label': '4', 'value': '4'},
                                    {'label': '5', 'value': '5'},
                                ],
                                value="",
                                searchable=False,
                                clearable=True,
                                style={'color': '#2196f3'}
                            ),
                        ]),
                    ]),
                ])
