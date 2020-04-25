
class NoInternetException(Exception):

    def __init__(self, message='No detectamos conexion a internet'):
        self.message = message
    def __str__(self):
        return self.message
class WrongCredenciales(Exception):

    def __init__(self, message='Ha proporcionado datos incorrectos para acceder'):
        self.message = message
    def __str__(self):
        return self.message

class BadResponse(Exception):
    
    def __init__(self, message='Error al solicitar recurso',url='url is missing'):
        self.message = message +"\n"+ url
    def __str__(self):
        return self.message
