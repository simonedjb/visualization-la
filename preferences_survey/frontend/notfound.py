from dash.dependencies import Input, Output, State
import dash_html_components as html
import dash_core_components as dcc

from app import app

from frontend import frontend
from backend import backend, feedbackmessage

feedmsg = feedbackmessage.feedbackmessage()
control = backend.backend()
interface = frontend.frontend()

_page_name = "notfound"

layout = html.Div([
    interface.survey_404(),
    interface.survey_send("send_"+_page_name,'/','voltar')
])