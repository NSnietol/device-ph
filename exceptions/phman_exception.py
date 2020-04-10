class NoResidentsFound(Exception):

    def __init__(self, message):
        self.message = message

class NoReservationsFound(Exception):

    def __init__(self, message):
        self.message = message