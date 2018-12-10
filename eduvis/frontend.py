import dash
import dash_core_components as dcc
import dash_html_components as html

class frontend:

    _language = "pt"

    def __init__(self, language = None):
        if language != None:
            self._language = language

    def nav(self):
        return html.Nav(className="light-blue lighten-1", role="navigation", children=[
                    html.Div(className="nav-wrapper", children=[                        
                        html.A(id="logo-container", href="#", className="brand-logo left", children=[
                            "EduVis",
                            html.I("school",className="material-icons"),
                        ]),
                    ]),
                ])

    def menu(self):
        return html.Div(className="col s2", children=[
                        html.Br(),html.Br(),html.Br(),
                        html.Div(className="collection", children=[
                            html.A(href="#!", id='opt-1', n_clicks_timestamp='0', className="light-blue-text collection-item",children=[
                                "Assessment run",
                                html.I("insert_chart",className="material-icons right"),
                                # html.Span("1", className="light-blue badge")
                            ]),
                            html.A(href="#!", id='opt-2', n_clicks_timestamp='0', className="light-blue-text collection-item",children=[
                                "Materials access",
                                html.I("insert_chart",className="material-icons right"),
                                # html.Span("1",className="light-blue new badge")
                            ]),
                            html.A(href="#!", id='opt-3', n_clicks_timestamp='0', className="light-blue-text collection-item",children=[
                                "Forum interaction",
                                html.I("insert_chart",className="material-icons right"),
                            ]),
                            html.A(href="#!", id='opt-4', n_clicks_timestamp='0', className="light-blue-text collection-item",children=[
                                "Videos access",
                                html.I("insert_chart",className="material-icons right"),
                                # html.Span("1",className="light-blue badge")
                            ]),
                            html.A(href="#!", id='opt-5', n_clicks_timestamp='0', className="light-blue-text collection-item",children=[
                                "Students clusters",
                                html.I("insert_chart",className="material-icons right"),
                                # html.Span("1",className="light-blue badge")
                            ]),
                            html.A(href="#!", id='opt-6', n_clicks_timestamp='0', className="light-blue-text collection-item",children=[
                                "Students profile",
                                html.I("insert_chart",className="material-icons right"),
                                # html.Span("1",className="light-blue badge")
                            ]),
                            html.A(href="#!", id='opt-7', n_clicks_timestamp='0', className="light-blue-text collection-item",children=[
                                "Course completion",
                                html.I("insert_chart",className="material-icons right"),
                                # html.Span("1",className="light-blue badge")
                            ]),
                            html.A(href="#!", id='opt-8', n_clicks_timestamp='0', className="light-blue-text collection-item",children=[
                                "Students access",
                                html.I("insert_chart",className="material-icons right"),
                                # html.Span("1",className="light-blue badge")
                            ]),
                            html.A(href="#!", id='opt-9', n_clicks_timestamp='0', className="light-blue-text collection-item",children=[
                                "Video interaction",
                                html.I("insert_chart",className="material-icons right"),
                                # html.Span("1",className="light-blue badge")
                            ]),
                            html.A(href="#!", id='opt-10', n_clicks_timestamp='0', className="light-blue-text collection-item",children=[
                                "Video likes",
                                html.I("insert_chart",className="material-icons right"),
                                # html.Span("1",className="light-blue badge")
                            ]),
                            html.A(href="#!", id='opt-11', n_clicks_timestamp='0', className="light-blue-text collection-item",children=[
                                "Student navigate",
                                html.I("insert_chart",className="material-icons right"),
                                # html.Span("1",className="light-blue badge")
                            ]),
                        ]),                        
                        # html.Div(className="divider"),
                        # html.Br(),
                        # html.A(className="light-blue waves-effect waves-light btn",children=[
                        #     "Cloud",
                        #     html.I("cloud",className="material-icons left")
                        # ]),
                    ])

    def footer(self):
        return html.Footer(className="page-footer orange",children=[
                    html.Div(className="container",children=[
                        html.Div(className="row",children=[
                            html.Div(className="col l6 s12",children=[
                                html.H5("Company Bio",className="white-text"),
                                html.P("We are a team of college students working on this project like it's our full time job. Any amount would help support and continue development on this project and is greatly appreciated.",className="grey-text text-lighten-4")
                            ]),
                            html.Div(className="col l3 s12",children=[
                                html.H5("Settings",className="white-text"),
                                html.Ul(children=[
                                    html.Li(children=[
                                        html.A("Link 1",className="white-text",href="#!")
                                    ]),
                                    html.Li(children=[
                                        html.A("Link 2",className="white-text",href="#!")
                                    ]),
                                    html.Li(children=[
                                        html.A("Link 3",className="white-text",href="#!")
                                    ]),
                                    html.Li(children=[
                                        html.A("Link 4",className="white-text",href="#!")
                                    ])
                                ])
                            ]),
                            html.Div(className="col l3 s12",children=[
                                html.H5("Connect",className="white-text"),
                                html.Ul(children=[
                                    html.Li(children=[
                                        html.A("Link 1",className="white-text",href="#!")
                                    ]),
                                    html.Li(children=[
                                        html.A("Link 2",className="white-text",href="#!")
                                    ]),
                                    html.Li(children=[
                                        html.A("Link 3",className="white-text",href="#!")
                                    ]),
                                    html.Li(children=[
                                        html.A("Link 4",className="white-text",href="#!")
                                    ])
                                ])
                            ])
                        ])
                    ]),
                    html.Div(className="footer-copyright",children=[
                        html.Div(className="container",children=[
                            "Made by ",
                            html.A("André",className="orange-text text-lighten-3", href="http://materializecss.com")
                        ])
                    ])
                ])

    # def workspace(self):
    #     return self.workspace_sign_up()
    #     # return self.workspace_teacher()
    
    def workspace_sign_up(self):
        return html.Div(className="row", children=[
                    # self.menu(),
                    html.Div(className="col s12", children=[
                        html.Div(className="section no-pad-bot", id="index-banner",children=[
                            html.Div(className="container",children=[
                                html.Div(className="row center", children=[
                                    
                                ]),
                                html.Br(),html.Br(),
                                html.Div(id='output-state'),
                                html.Br(),html.Br(),                           
                            ]),
                        ]),                        
                    ]),
                ])

    def workspace_teacher(self):
        return html.Div(className="row", children=[
                    self.menu(),
                    html.Div(className="col s10", children=[
                        html.Div(className="section no-pad-bot", id="index-banner",children=[
                            html.Div(className="container",children=[
                                html.Div(className="row center", children=[
                                    html.Form(children=[
                                        html.Div(className="input-field", children=[
                                            dcc.Input(id="", type="search"),
                                            html.Label(className="label-icon", children=[
                                                html.I("search",className="material-icons")
                                            ]),
                                            html.I("close",className="material-icons")
                                        ])
                                    ])
                                ]),
                                html.Br(),html.Br(),
                                html.Div(id='output-state'),
                                html.Br(),html.Br(),
                                # html.A(id="alogo-container", href="#", className="brand-logo left", children=[
                                #     "EduVis",
                                #     html.I("school",className="material-icons"),
                                # ]),
                                
                                # html.Div(className="row center", children=[
                                #     html.H5("A modern responsive front-end framework based on Material Design", className="header col s12 light"),
                                # ]),
                                # html.Div(className="row center", children=[
                                #     html.A("Get Started", href="http://materializecss.com/getting-started.html", id="download-button", className="btn-large waves-effect waves-light orange")
                                # ]),
                            ]),
                        ]),
                        # html.Div(className="container",children=[
                        #     html.Div(className="section",children=[
                        #         html.Div(className="row",children=[
                        #             html.Div(className="col s12 m4",children=[
                        #                 html.Div(className="icon-block",children=[
                        #                     html.H2(className="center light-blue-text",children=[
                        #                         html.I("flash_on",className="material-icons")
                        #                     ]),
                        #                     html.H5("Speeds up development",className="center"),
                        #                     html.P("We did most of the heavy lifting for you to provide a default stylings that incorporate our custom components. Additionally, we refined animations and transitions to provide a smoother experience for developers.",className="light"),
                        #                 ])
                        #             ]),
                        #             html.Div(className="col s12 m4",children=[
                        #                 html.Div(className="icon-block",children=[
                        #                     html.H2(className="center light-blue-text",children=[
                        #                         html.I("flash_on",className="material-icons")
                        #                     ]),
                        #                     html.H5("User Experience Focused",className="center"),
                        #                     html.P("By utilizing elements and principles of Material Design, we were able to create a framework that incorporates components and animations that provide more feedback to users. Additionally, a single underlying responsive system across all platforms allow for a more unified user experience.",className="light"),
                        #                 ])
                        #             ]),
                        #             html.Div(className="col s12 m4",children=[
                        #                 html.Div(className="icon-block",children=[
                        #                     html.H2(className="center light-blue-text",children=[
                        #                         html.I("flash_on",className="material-icons")
                        #                     ]),
                        #                     html.H5("Easy to work with",className="center"),
                        #                     html.P("We have provided detailed documentation as well as specific code examples to help new users get started. We are also always open to feedback and can answer any questions a user may have about Materialize.",className="light"),
                        #                 ])
                        #             ])
                        #         ]),
                        #     ]),
                        #     html.Br(),html.Br(),
                        # ]),
                    ]),
                ])

# @app.callback(
#     Output('output-state', 'children'),
#     [Input('opt-1', 'n_clicks_timestamp'),
#     Input('opt-2', 'n_clicks_timestamp'),
#     Input('opt-3', 'n_clicks_timestamp'),
#     Input('opt-4', 'n_clicks_timestamp'),
#     Input('opt-5', 'n_clicks_timestamp'),
#     Input('opt-6', 'n_clicks_timestamp'),
#     Input('opt-7', 'n_clicks_timestamp'),
#     Input('opt-8', 'n_clicks_timestamp'),
#     Input('opt-9', 'n_clicks_timestamp'),
#     Input('opt-10', 'n_clicks_timestamp'),
#     Input('opt-11', 'n_clicks_timestamp')])

# def display_click_data(opt1, opt2, opt3, opt4, opt5, opt6, opt7, opt8, opt9, opt10, opt11):
#     lst_opt = [int(opt1), int(opt2), int(opt3), int(opt4), int(opt5), int(opt6), int(opt7), int(opt8), int(opt9), int(opt10), int(opt11)]    
#     val_max = max(lst_opt)
    
#     if val_max == 0: 
#         return html.H1(className="header center orange-text", children=["Wellcome to EduVis"]),

#     val_index = lst_opt.index(val_max)+1

#     return control.get_preference_graph(val_index)