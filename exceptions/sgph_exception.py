class NoUserFound(Exception):

    def __init__(self, message='Usuario no registrado en el sistema'):
        self.message = message
    def __str__(self):
        return self.message

class NoDeviceFound(Exception):

    def __init__(self, message='Dispositivo no encontrado'):
        self.message = message
    def __str__(self):
        return self.message

class UserNoAllowed(Exception):

    def __init__(self, message='Este usuario no cuenta permisos'):
        self.message = message
    def __str__(self):
        return self.message