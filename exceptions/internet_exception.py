
class NoInternetException(Exception):

    def __init__(self, message):
        self.message = message


class WrongCredenciales(Exception):

    def __init__(self, message):
        self.message = message
