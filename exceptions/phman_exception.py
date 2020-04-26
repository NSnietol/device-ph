class NoResidentsFound(Exception):

    def __init__(self, message='No encontramos los residentes de la propiedad'):
        self.message = message

class NoReservationsFound(Exception):

    def __init__(self, message='No encontramos reservas para esta propiedad'):
        self.message = message

class NoGuardFound(Exception):

    def __init__(self, message='No encontramos este usuario en nuestro sistema'):
        self.message = message
class NoPermissionFound(Exception):

    def __init__(self, message='Usted no cuenta con permisos para administrar este dispositivo'):
        self.message = message


class CouldntCreateDevice(Exception):

    def __init__(self, message='No se pudo registrar el dispostivo'):
        self.message = message

class CouldntUpdateDevice(Exception):

    def __init__(self, message='No se pudo actualizar el dispostivo'):
        self.message = message