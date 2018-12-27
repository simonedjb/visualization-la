from frontend import frontend

class feedbackmessage:

    _n_clicks = 0

    interface = frontend.frontend()

    def __init__(self, _n_clicks = 0):
        self.set_clicks(_n_clicks)

    def set_clicks(self,_n_clicks):
        self._n_clicks = _n_clicks

    def add_clicks(self):
        self._n_clicks += 1

    def get_clicks(self):
        return self._n_clicks

    def warning_message(self):
        return self.interface.survey_warning_message()